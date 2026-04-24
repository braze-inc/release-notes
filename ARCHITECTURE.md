# Architecture and technical specification

This document describes how the `braze-inc/release-notes` repository is built, how the daily mirror works end-to-end, and the exact behavior of every moving part. It is the canonical reference for how this repo stays in sync with [`www.braze.com/docs`](https://www.braze.com/docs/).

## Table of contents

- [Overview](#overview)
- [Repository layout](#repository-layout)
- [How the mirror works](#how-the-mirror-works)
- [Source of truth: the public sitemap](#source-of-truth-the-public-sitemap)
- [Sync script reference (`scripts/sync_public_docs_markdown.py`)](#sync-script-reference-scriptssync_public_docs_markdownpy)
- [GitHub Actions workflow reference (`.github/workflows/sync-release-notes.yml`)](#github-actions-workflow-reference-githubworkflowssync-release-notesyml)
- [Branching, pull request, and review flow](#branching-pull-request-and-review-flow)
- [Daily change reports](#daily-change-reports)
- [What goes in vs. what is excluded](#what-goes-in-vs-what-is-excluded)
- [Operational behavior](#operational-behavior)
- [Failure modes and handling](#failure-modes-and-handling)
- [Security model](#security-model)
- [Common tasks](#common-tasks)
- [FAQ](#faq)

## Overview

The `release-notes` repository is a **public, read-only mirror** of the markdown content that powers `www.braze.com/docs`. It exists so external users, partners, and AI systems can clone or fetch a flat tree of public documentation as plain markdown without scraping the live site.

Key properties:

- **One direction.** Content flows from `braze.com/docs` → `release-notes`. The mirror never publishes back to the docs site.
- **Sitemap-driven.** No hardcoded page list. Whatever pages the live site advertises in its sitemap are the pages we mirror, automatically.
- **Markdown-only.** Each public page exposes a rendered markdown endpoint via the "View as Markdown" button on `braze.com/docs`. The mirror requests that endpoint for every page.
- **Weekday automation.** A GitHub Actions cron runs Monday through Friday at 06:00 UTC. Manual runs are available via `workflow_dispatch` any time.
- **PR-gated.** The workflow never pushes to `main` directly. It pushes to a dedicated mirror branch and opens (or updates) a single pull request to `main`. The Docs team approves and merges.
- **Auditable.** Every run that produces changes writes a `changes/YYYY-MM-DD.md` summary listing every added, modified, or deleted file.

## Repository layout

```
release-notes/
├── .github/
│   └── workflows/
│       └── sync-release-notes.yml      # The sync workflow
├── ARCHITECTURE.md                     # This document
├── LICENSE
├── README.md                           # User-facing summary
├── changes/
│   └── YYYY-MM-DD.md                   # One file per sync run that produced changes
├── docs/
│   ├── API/                            # Mirrors /docs/api/...
│   ├── Developer Guide/                # Mirrors /docs/developer_guide/...
│   ├── Technology Partners/            # Mirrors /docs/partners/...
│   ├── User Guide/                     # Mirrors /docs/user_guide/...
│   └── What's New/                     # Mirrors /docs/releases/...
└── scripts/
    └── sync_public_docs_markdown.py    # Sitemap fetch + per-page download
```

The five `docs/` subfolders correspond exactly to the five top-level tabs at the top of `braze.com/docs`. Folder hierarchy beneath each tab mirrors the URL path on the site, and each leaf is named `index.md` (the same filename the live site serves at the markdown endpoint).

## How the mirror works

At a high level, every run does the following:

1. Check out `main` of `release-notes`.
2. Run `scripts/sync_public_docs_markdown.py`:
   1. Fetch `https://www.braze.com/docs/sitemap.xml`.
   2. For every URL in the sitemap that lives under one of the five sections, request the page's rendered markdown at `<page-url>/index.md`.
   3. Write each successful response into `sync-staging/<Section>/<sub-path>/index.md`.
3. `rsync --delete` each `sync-staging/<Section>/` over the corresponding `docs/<Section>/` so additions, modifications, and removals are all reflected.
4. Stage every change to the five `docs/<Section>/` folders.
5. If nothing actually changed, log "No markdown changes detected." and exit clean. No commit, no push, no PR.
6. If changes exist, write a `changes/YYYY-MM-DD.md` summary, commit everything, force-push to a dedicated mirror branch (`docs-sync/public-docs-mirror`), then open or update a pull request from that branch to `main`.
7. A Docs team reviewer approves and merges the PR to update `main`.

## Source of truth: the public sitemap

The script reads `https://www.braze.com/docs/sitemap.xml`, which is the official, live, public list of every documentation URL on `braze.com/docs`. This means:

- New pages added to the docs site automatically appear in the next sync.
- Pages removed from the docs site are dropped from the mirror in the next sync (because of `rsync --delete`).
- Renamed pages are reflected as a delete plus an add at the new path.
- Translations and other non-English locales are excluded (see [What goes in vs. what is excluded](#what-goes-in-vs-what-is-excluded)).

Because the sitemap is the only input for what to mirror, the mirror is automatically forward-compatible with new sections, new sub-trees, and reorganizations on the docs site, with one exception: top-level **sections** are filtered explicitly (see `SECTION_MAP` below), so adding a brand-new top-level tab requires updating the script.

## Sync script reference (`scripts/sync_public_docs_markdown.py`)

The full script is small. This section walks through each piece.

### Constants

```python
SITEMAP_URL = "https://www.braze.com/docs/sitemap.xml"
USER_AGENT = "Mozilla/5.0 (compatible; release-notes-sync/1.0)"
REQUEST_TIMEOUT_SECONDS = 30
```

- `SITEMAP_URL` is the only entry point. The script does not crawl pages directly.
- `USER_AGENT` is set explicitly because the `braze.com` edge returns 403 for the default Python `urllib` user-agent on some paths.
- `REQUEST_TIMEOUT_SECONDS` bounds each individual HTTP fetch.

### Section map

```python
SECTION_MAP = {
    "user_guide": "User Guide",
    "developer_guide": "Developer Guide",
    "api": "API",
    "partners": "Technology Partners",
    "releases": "What's New",
}
```

This is the only place the five top-level tabs are listed. Keys are the URL path segment used by `braze.com/docs` (e.g., `developer_guide` in `/docs/developer_guide/...`); values are the human-readable folder names used inside `docs/`.

If a brand-new top-level tab is ever added to the docs site, this mapping is the one place you'd extend.

### Locale filter

```python
LOCALE_PREFIXES = {"de", "es", "fr", "ja", "ko", "pt-br", "pt_br"}
```

Any sitemap URL whose first path segment matches one of these is dropped. The mirror is English-only.

### `fetch_bytes(url)`

Sends a GET request with the custom user agent and timeout. Returns raw bytes. Errors are propagated to callers.

### `sitemap_urls(xml_bytes)`

Parses the sitemap XML using `xml.etree.ElementTree` and the standard sitemap namespace (`http://www.sitemaps.org/schemas/sitemap/0.9`). Returns a list of every `<loc>` value the sitemap declares.

### `build_targets(urls)`

Filters and rewrites every sitemap URL into a `(markdown_url, destination_path)` pair:

1. Drop URLs not on `www.braze.com`.
2. Drop URLs not under `/docs/`.
3. Drop URLs whose first path segment is a locale prefix.
4. Drop URLs whose first path segment is not in `SECTION_MAP`.
5. Map the section segment to the destination folder name (e.g., `developer_guide` → `Developer Guide`).
6. Construct the markdown URL by appending `/index.md` to the page path. This is the same endpoint the "View as Markdown" button hits on the live site.
7. Construct the destination path as `<Section>/<sub-path>/index.md`.

The function dedupes by destination path and returns a sorted list for deterministic ordering.

### `main()`

1. Recreate `sync-staging/` from scratch so each run starts clean.
2. Pre-create empty `sync-staging/<Section>/` folders so the workflow's `rsync --delete` step always has a source directory to mirror, even if the section is temporarily empty.
3. Fetch the sitemap and build the target list.
4. For each target, fetch the markdown URL and write the response body to `sync-staging/<dest>`. HTTP errors are recorded in `failures` and the loop continues.
5. Print summary counters: how many endpoints were discovered, how many were successfully fetched, and how many were skipped (with the first 20 failures listed for quick inspection).

The script never modifies `docs/` directly. The workflow does that with `rsync`, which makes the staging step idempotent and safe to re-run locally.

## GitHub Actions workflow reference (`.github/workflows/sync-release-notes.yml`)

The workflow has one job, `sync`, with five steps. This section explains every line.

### Triggers

```yaml
on:
  schedule:
    - cron: "0 6 * * 1-5"
  workflow_dispatch:
```

- `schedule`: a cron expression that fires Monday through Friday at 06:00 UTC. The `1-5` field means "day-of-week 1 through 5" (Monday–Friday). Saturday (`6`) and Sunday (`0`) are skipped, so any docs changes between Friday's run and Monday's run are bundled into Monday's pull request.
- `workflow_dispatch`: enables manual runs from the Actions tab. Manual runs are independent of the schedule and can be invoked any day, including weekends, when an on-demand mirror is needed.

GitHub may delay scheduled runs by up to ~15 minutes during platform load. This is normal and does not affect correctness.

### Permissions

```yaml
permissions:
  contents: write
  pull-requests: write
```

- `contents: write` lets the job push to the dedicated mirror branch.
- `pull-requests: write` lets the job call `gh pr create` and `gh pr edit` to manage the mirror PR.

The job uses the built-in `GITHUB_TOKEN` only. There are no long-lived secrets, no PATs, and no cross-repo tokens.

### Concurrency

```yaml
concurrency:
  group: mirror-public-docs-markdown
  cancel-in-progress: true
```

If a second run is queued (for example, the schedule fires while a manual run is still going), the in-progress run is canceled and the new one proceeds. This guarantees only one sync ever races to update the mirror branch and PR at a time.

### Environment

```yaml
env:
  SYNC_BRANCH: docs-sync/public-docs-mirror
```

The single long-lived branch name used as the head of the mirror PR. The workflow always force-pushes the latest mirror commit onto this branch, so it represents "the most recent attempt to update `main`" at any time.

### Job

```yaml
jobs:
  sync:
    runs-on: ubuntu-latest
```

A single job on a stock Ubuntu runner. No matrix, no cache, no extra services.

### Step 1: Checkout

```yaml
- name: Checkout destination repo on main
  uses: actions/checkout@v5
  with:
    fetch-depth: 0
    ref: main
```

- `ref: main` ensures the mirror is always built against the current `main`, not against the mirror branch's previous state.
- `fetch-depth: 0` pulls the full history so subsequent `git diff`/`git push` operations have everything they need.

### Step 2: Build the mirror

```yaml
- name: Build sitemap-driven markdown mirror from public docs
  run: |
    set -euo pipefail
    python3 scripts/sync_public_docs_markdown.py

    mkdir -p docs
    for section in "User Guide" "Developer Guide" "API" "Technology Partners" "What's New"; do
      mkdir -p "docs/${section}"
      rsync -av --delete "sync-staging/${section}/" "docs/${section}/"
    done
```

- `set -euo pipefail` makes the script fail fast on any error.
- The Python script populates `sync-staging/`.
- For each of the five sections, `rsync -av --delete` copies the staged tree into `docs/<Section>/`, removing files that no longer exist in the staging output. This is the step that makes deletes propagate from the docs site into the mirror.
- The trailing slash on `sync-staging/${section}/` tells `rsync` to copy contents (not the directory itself), so the result is `docs/<Section>/<sub-path>/...`.

### Step 3: Stage and detect changes

```yaml
- name: Stage mirror output and detect changes
  id: diff
  run: |
    set -euo pipefail
    git add -A -- "docs/User Guide" "docs/Developer Guide" "docs/API" "docs/Technology Partners" "docs/What's New"

    if git diff --cached --quiet; then
      echo "changed=false" >> "$GITHUB_OUTPUT"
      echo "No markdown changes detected."
    else
      echo "changed=true" >> "$GITHUB_OUTPUT"
    fi
```

- `git add -A --` stages every addition, modification, and deletion under the five mirrored folders. The `--` makes the listed paths positional pathspecs so quoted folder names with spaces are interpreted correctly.
- `git diff --cached --quiet` exits 0 when the index is unchanged and nonzero when there are staged changes. The result is captured into `$GITHUB_OUTPUT` so later steps can branch on it via `if: steps.diff.outputs.changed == 'true'`.
- When nothing changed, the step exits cleanly and the workflow ends green without committing, pushing, or opening any PR. This is the common case on quiet days.

### Step 4: Write the daily change report

```yaml
- name: Write daily changes report
  if: steps.diff.outputs.changed == 'true'
  run: |
    set -euo pipefail
    TODAY="$(date -u +%Y-%m-%d)"
    LOG_FILE="changes/${TODAY}.md"
    mkdir -p changes

    CHANGES="$(git diff --cached --name-status -- "docs/User Guide" "docs/Developer Guide" "docs/API" "docs/Technology Partners" "docs/What's New")"
    COUNT="$(printf "%s\n" "$CHANGES" | sed '/^$/d' | wc -l | tr -d ' ')"

    {
      echo "# Daily docs markdown sync - ${TODAY}"
      echo
      echo "## Summary"
      echo "- Source: https://www.braze.com/docs/sitemap.xml"
      echo "- Changed files: ${COUNT}"
      echo
      echo "## Changes"
      printf "%s\n" "$CHANGES" | sed '/^$/d' | while IFS=$'\t' read -r status path; do
        echo "- ${status} \`${path}\`"
      done
    } > "$LOG_FILE"

    git add "$LOG_FILE"
```

- Runs only when changes exist.
- `TODAY` is in UTC so report filenames match the run timestamp regardless of where the runner is physically located.
- `git diff --cached --name-status` outputs one line per change, prefixed with the change type (`A` added, `M` modified, `D` deleted, `R` renamed, `C` copied).
- The report is written to `changes/YYYY-MM-DD.md` and includes the source URL, total count, and per-file lines like:
  ```
  - M `docs/User Guide/messaging/campaigns/faq/index.md`
  - A `docs/Developer Guide/getting_started/build_with_llm/index.md`
  - D `docs/Technology Partners/ecommerce/loyalty/voucherify/voucherify/index.md`
  ```
- The report file is staged so it travels with the rest of the changes in the upcoming commit.

### Step 5: Commit, push, open or update the PR

```yaml
- name: Commit and push to mirror branch, then open or update the mirror PR
  if: steps.diff.outputs.changed == 'true'
  env:
    GH_TOKEN: ${{ github.token }}
  run: |
    set -euo pipefail

    git config user.name "github-actions[bot]"
    git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

    TODAY="$(date -u +%Y-%m-%d)"
    git commit -m "Mirror public docs markdown from braze.com/docs (${TODAY})"

    git push --force "https://x-access-token:${GH_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" "HEAD:${SYNC_BRANCH}"

    PR_NUMBER="$(gh pr list --state open --base main --head "${SYNC_BRANCH}" --json number --jq '.[0].number // empty')"
    PR_TITLE="Mirror public docs markdown from braze.com/docs (${TODAY})"
    PR_BODY="Automated daily sync of public-facing markdown from https://www.braze.com/docs into docs/User Guide, docs/Developer Guide, docs/API, docs/Technology Partners, and docs/What's New."

    if [ -z "${PR_NUMBER}" ]; then
      gh pr create --base main --head "${SYNC_BRANCH}" --title "${PR_TITLE}" --body "${PR_BODY}"
      PR_NUMBER="$(gh pr list --state open --base main --head "${SYNC_BRANCH}" --json number --jq '.[0].number')"
      echo "Opened mirror PR #${PR_NUMBER}. A Docs team reviewer must approve and merge it to update main."
    else
      gh pr edit "${PR_NUMBER}" --title "${PR_TITLE}" --body "${PR_BODY}"
      echo "Updated existing mirror PR #${PR_NUMBER}. A Docs team reviewer must approve and merge it to update main."
    fi
```

- Runs only when changes exist.
- Commit author is the GitHub Actions bot. The email format `41898282+github-actions[bot]@users.noreply.github.com` is the standard noreply address GitHub recognizes for this app.
- The commit message includes the UTC date, e.g. `Mirror public docs markdown from braze.com/docs (2026-04-24)`.
- The push uses the built-in `GH_TOKEN` against an HTTPS URL (`x-access-token` is the documented username for token-based pushes). It is a `--force` push because the mirror branch always represents the latest sync state, not an accumulated history.
- The PR lookup, create, and edit calls all use `gh` (preinstalled on `ubuntu-latest`). If a PR is already open from `docs-sync/public-docs-mirror` to `main`, the workflow updates its title and body instead of opening a new one. This guarantees there is **at most one open mirror PR** at any time.

## Branching, pull request, and review flow

The repo's `main` is protected. The ruleset on `main` requires:

- changes made via pull request,
- one approving review, and
- a code-owner review.

The workflow respects this by never pushing to `main`. Instead:

1. Every successful run with changes pushes a single commit to **`docs-sync/public-docs-mirror`** (force-pushed; this branch is not meant for human commits).
2. The workflow opens (or updates) **one** PR titled `Mirror public docs markdown from braze.com/docs (YYYY-MM-DD)` whose head is `docs-sync/public-docs-mirror` and base is `main`.
3. A Docs team reviewer approves and merges the PR.
4. After merge, `main` reflects the latest mirror state. The next run will detect "no changes" against `main` and exit clean unless the docs site has changed again.

If the next sync runs while the prior PR is still open, the workflow force-pushes the new content onto the same branch and updates the existing PR's title/body to the latest date. Reviewers see one rolling PR rather than a backlog.

## Daily change reports

Each run that produces changes writes `changes/YYYY-MM-DD.md`. These files form a permanent audit trail on `main` so anyone can answer "what changed on day X?" without scanning git history.

Format:

```markdown
# Daily docs markdown sync - 2026-04-24

## Summary
- Source: https://www.braze.com/docs/sitemap.xml
- Changed files: 162

## Changes
- M `docs/User Guide/messaging/campaigns/faq/index.md`
- A `docs/Developer Guide/getting_started/build_with_llm/index.md`
- D `docs/Technology Partners/ecommerce/loyalty/voucherify/voucherify/index.md`
...
```

The change types map directly to git's `--name-status` codes: `A` (added), `M` (modified), `D` (deleted), `R<score>` (renamed), `C<score>` (copied).

## What goes in vs. what is excluded

**Included:**

- Every English `braze.com/docs` URL listed in the public sitemap whose first path segment is `user_guide`, `developer_guide`, `api`, `partners`, or `releases`, when its `<page>/index.md` endpoint returns a successful response.

**Excluded:**

- Non-English locales (`de`, `es`, `fr`, `ja`, `ko`, `pt-br`).
- URLs outside `/docs/`.
- URLs in sections other than the five mapped tabs.
- The top-level tab landing pages (e.g., `/docs/user_guide/home`, `/docs/developer_guide/home`) and bare section URLs whose markdown endpoints return 404 on the live site.
- Any page whose `index.md` returns an HTTP error during the run; these are reported in the run log under "Skipped N pages with fetch errors" without failing the run.

The mirror is intentionally an *English-only*, *public-only*, *as-rendered-by-Jekyll* snapshot of the docs site. It contains no source-form Liquid, no `_includes`, no front-matter scaffolding from the `braze-docs` repository.

## Operational behavior

### Day-to-day timeline

- **Mon–Fri 06:00 UTC:** scheduled run kicks off. Within ~3 minutes:
  - If the live docs site has not changed since the last merge to `main`, the run logs "No markdown changes detected." and ends. No commit, no PR.
  - Otherwise, the workflow opens a fresh PR (or updates the existing rolling PR) titled with today's UTC date.
- **Sat–Sun:** the schedule does not fire. Manual runs via `workflow_dispatch` still work if needed.
- **Following Monday:** any docs changes from Friday through Sunday are bundled into Monday's PR.
- **Docs team review window:** PRs are reviewed and merged on the team's normal cadence. Until merge, additional weekday runs continue updating the same PR rather than stacking new ones.

### Idempotency

The full pipeline is idempotent. Re-running the workflow when the site has not changed produces no output. Re-running after a partial failure simply rebuilds from the sitemap and replaces the staging output.

### Concurrency

The `concurrency` group ensures only one job runs at a time and an in-progress run is canceled if a new one starts. There is never a risk of two workflow runs racing to update the same branch.

## Failure modes and handling

| Failure | What happens | Recovery |
|---|---|---|
| Sitemap fetch returns non-200 (e.g., temporary `braze.com` outage) | The Python script raises and the workflow fails on Step 2 with a clear error. | Re-run via `workflow_dispatch` once the site is healthy. |
| Individual page `<url>/index.md` returns 404 or 5xx | Page is skipped, recorded in the script's `failures` list, and printed in the run log. The run still succeeds. | None needed — these are typically genuine landing pages without a markdown endpoint. If you expected a markdown endpoint, check the docs site. |
| GitHub returns 5xx during push or PR API calls | The step fails; the cron will retry on the next scheduled run. Manual `workflow_dispatch` is also available. | Re-run after GitHub recovers. The mirror branch is force-pushed, so partial state is overwritten cleanly. |
| Branch protection or repository ruleset on `main` rejects a direct push | Cannot happen by design — the workflow never pushes to `main`, only to the mirror branch. | None needed. |
| Stale paths in `git add` pathspecs after a deletion (e.g., the legacy `docs/releases` path issue) | `git add` exits 128 with `pathspec did not match any files`. | Remove the obsolete pathspec from the workflow. |
| Mirror PR has merge conflicts after a long delay | The PR shows conflicts in the GitHub UI. | Either merge `main` into the PR branch and resolve, or simply re-run the workflow — the next run rebuilds the mirror branch from `main` and resolves the conflict automatically. |

## Security model

- **Token surface:** only the built-in `GITHUB_TOKEN` is used, scoped to this repository.
- **Permissions surface:** `contents: write` and `pull-requests: write` on this repo only.
- **Cross-repo trust:** none. The workflow does not call into other repositories or services beyond `www.braze.com` (read-only) and `api.github.com` (via `gh`).
- **Secrets stored:** none beyond the built-in token.
- **Inputs:** the only external inputs are the public sitemap and the public markdown endpoints on `www.braze.com/docs`. There is no path for untrusted input to alter the workflow's behavior.

## Common tasks

### Run a manual sync now

1. Go to **Actions** → `Mirror public docs markdown from braze-docs`.
2. Click **Run workflow**, leave the branch as `main`, click **Run workflow** again.
3. Wait ~3 minutes. If the run prints `No markdown changes detected.`, the site is in sync. Otherwise, an open PR will appear in **Pull requests**.

### Review and merge the mirror PR

1. Open the PR titled `Mirror public docs markdown from braze.com/docs (YYYY-MM-DD)`.
2. Confirm `changes/YYYY-MM-DD.md` accurately summarizes the diff.
3. Spot-check a handful of changed files if needed.
4. Approve and merge.

### Inspect what a previous run did

Open `changes/YYYY-MM-DD.md` for that date.

### Add a new top-level tab to the mirror

If `braze.com/docs` ever ships a sixth top-level tab:

1. Add the new entry to `SECTION_MAP` in `scripts/sync_public_docs_markdown.py`.
2. Add the human-readable folder name to the `for section in ...` loop and to the two pathspec lists in `.github/workflows/sync-release-notes.yml`.
3. Update this document and `README.md`.

### Drop a section from the mirror

1. Remove the entry from `SECTION_MAP`.
2. Remove the folder from the `for section in ...` loop and pathspec lists.
3. Manually delete the `docs/<Section>/` folder in a regular PR.

## FAQ

**Q: If nothing on the docs site changed, will the workflow still open a PR?**
No. It exits with `No markdown changes detected.` and creates nothing.

**Q: How often does the workflow run?**
Mondays through Fridays at 06:00 UTC, plus any manual runs via the Actions tab.

**Q: Why weekdays only?**
Docs site changes typically don't ship over the weekend, and bundling Friday-through-Sunday changes into Monday's PR keeps reviewer overhead low. Manual runs are still available any day if needed.

**Q: Where does the content actually come from?**
The sitemap at `https://www.braze.com/docs/sitemap.xml` lists every public page. For each page, the workflow downloads the same markdown the "View as Markdown" button serves on the live site, at `<page-url>/index.md`.

**Q: Why is `docs/Developer Guide/getting_started/index.md` included if section landings aren't?**
The exclusion only applies to landing pages whose markdown endpoint returns 404 (currently the five tab-level `<section>/home` pages and the bare `<section>/` URLs). Section sub-landings like `getting_started/index.md` do return real markdown content on the live site, so they are mirrored.

**Q: Can two PRs ever be open at once?**
No. The workflow looks up the existing open PR with head `docs-sync/public-docs-mirror` and base `main`; if one exists, it updates that PR instead of opening a new one. There is at most one mirror PR at any time.

**Q: What happens if the sync runs while the prior PR is still open?**
The mirror branch is force-pushed to the latest content and the existing PR's title and body are updated to the current date. Reviewers see a single rolling PR with the freshest content.

**Q: How is `main` protected from accidental writes?**
A repository ruleset on `main` requires changes via pull request with one approving review and a code-owner review. The workflow honors this by pushing only to the mirror branch and opening a PR for human review.

**Q: How do I tell whether a missed run was an outage or just a quiet day?**
Open the latest run under **Actions** → `Mirror public docs markdown from braze-docs`. A green run with `No markdown changes detected.` is a quiet day. A red run shows the failing step's logs.
