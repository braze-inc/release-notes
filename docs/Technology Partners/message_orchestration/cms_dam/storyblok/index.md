# Storyblok

> [Storyblok](https://www.storyblok.com/) is a headless content management system with a visual editor. It models, manages, and delivers structured content through a REST Content Delivery API that returns JSON, so the same content can power any front end or downstream tool. This guide covers two ways to bring Storyblok content into Braze: Connected Content (pull at send time) and Content Blocks sync (push at publish time). The two approaches can also be combined.

_This integration is maintained by Storyblok._

## About this integration

There are two integration patterns. They differ in when content moves and who builds what:

| Pattern | How it works |
| --- | --- |
| Connected Content (pull at send time) | Braze calls the Storyblok API while a message renders and prints the fields into the message. There is no service to build. You configure everything in Liquid. |
| Content Blocks sync (push at publish time) | A service you host listens for Storyblok publish events and pushes the content into Braze as Content Blocks. Marketers then use those blocks natively, with no call at send time. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Storyblok integration patterns" }

### Choosing an integration pattern

Choose the approach that fits your needs:

- Start with Connected Content if you want the fastest path, have no service to host, or need content that changes per recipient.
- Choose Content Blocks sync if you want content resident in Braze with no send-time dependency, faster sends at high volume, or marketers browsing blocks natively, and you have the engineering capacity to build and monitor a small service.
- Combine both when it fits. Sync static shared content as blocks, and use Connected Content for the parts that must change per recipient.

**Important:**


The Content Blocks sync service is a reference implementation. Adapt it to your content model and test it in your environment before relying on it in production.



## Prerequisites

Before you start, you need the following:

| Requirement | Description |
| --- | --- |
| A Storyblok account | A Storyblok space with a Public access token. Create the token in Storyblok from **Settings** > **Access Tokens**. |
| A Braze REST API key | A Braze REST API key with the `content_blocks.create`, `content_blocks.update`, and `content_blocks.list` permissions. Create this key in the Braze dashboard from **Settings** > **APIs and Identifiers**. Required for Content Blocks sync only. |
| A Braze REST endpoint | [Your Braze REST endpoint URL](https://www.braze.com/docs/api/basics#endpoints). Your endpoint depends on the Braze URL for your instance. Required for Content Blocks sync only. |
| A host for the sync service | Anywhere that exposes a public HTTPS URL, such as a small container, a serverless function, or a Node host. Required for Content Blocks sync only. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Shared setup: Storyblok credentials

Both approaches need these credentials.

1. Log in to [Storyblok](https://app.storyblok.com/) and open your space.
2. Go to **Settings** > **Access Tokens** and copy a **Public** token. Public tokens are read-only, safe to use in delivery requests, and return published content.
3. Note the region of your space. The Content Delivery API base URL depends on where the space is hosted:

| Region | Base URL |
| --- | --- |
| European Union | `https://api.storyblok.com/v2/cdn` |
| United States | `https://api-us.storyblok.com/v2/cdn` |
| Canada | `https://api-ca.storyblok.com/v2/cdn` |
| Australia | `https://api-ap.storyblok.com/v2/cdn` |
| China | `https://app.storyblokchina.cn/v2/cdn` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Storyblok Content Delivery API base URLs by region" }

## Connected Content

Braze makes an HTTP call to Storyblok while a message is being rendered, stores the JSON response in a variable, and prints any field from it into the message. Nothing is built on either side. It is a configuration, done entirely in Liquid inside a Braze Content Block.

**Note:**


Connected Content is not available in the Braze free trial, where outbound calls are disabled. Use a workspace with Connected Content enabled.



### Step 1: Create the Braze Content Block

1. In Braze, go to **Content** > **Content Blocks** > **Create Content Block** > HTML code editor.
2. Paste the following, replacing the base URL with the one for your region, the token with your Public token, and the slug with your story's `full_slug`:


```liquid
{% assign sb_base = "https://api.storyblok.com/v2/cdn" %}
{% assign sb_token = "YOUR_PUBLIC_TOKEN" %}
{% assign sb_slug = "posts/welcome-message" %}

{% connected_content {{sb_base}}/spaces/me?token={{sb_token}} :save space_data %}
{% connected_content {{sb_base}}/stories/{{sb_slug}}?version=published&cv={{space_data.space.version}}&token={{sb_token}} :save response %}
```


{: start="3"}
3. Name the Content Block with a stable, descriptive name such as `storyblok_welcome_message`, then select **Launch Content Block**.

**Important:**


Storyblok's Content Delivery API redirects any request that does not include a cache version (`cv`) parameter, returning an HTTP 301 to the same URL with the latest `cv` appended. Braze Connected Content does not follow redirects, so a single call without `cv` renders nothing. The first call fetches the current `cv` from the space endpoint, and the second passes it to the story request, which then returns a 200 directly. Do not hardcode a `cv`, or you serve stale content after every publish.



**Tip:**


Instead of repeating your token in every Content Block, save it as its own Content Block or a workspace-level value and reference it, so it lives in a single place to rotate.



### Step 2: Render the content in a campaign or Canvas

1. Create or edit an email campaign, then open **Edit Email Body**.
2. Insert the Content Block from Step 1. On its own it produces no visible output, because it only fetches and saves the response. It acts as the engine that loads the data.
3. Print the fields you need with JSON dot notation. A single story returns a `story` object with your content nested under `story.content`:


```html
<h1>{{response.story.content.title}}</h1>
<p>{{response.story.content.intro}}</p>
<a href="{{response.story.content.cta_url}}">{{response.story.content.cta_label}}</a>
```


Field names come from your Storyblok component, so they vary by content model. To inspect the full structure while building, print the raw object temporarily with `{{response}}`.

{: start="4"}
4. Use **Preview & Test**, send to a test user, confirm the content renders, then launch. Connected Content fires at render time, so the call to Storyblok only happens on send or preview.

### Step 3: Optimize images (optional)

Transform Storyblok assets on the fly using the [Image Service](https://www.storyblok.com/docs/api/image-service) by appending parameters to the asset URL. Add `/m/` to enable optimization and automatic WebP conversion, a size, and any filters:


```html
<img src="{{response.story.content.image.filename}}/m/600x0/filters:quality(80)" />
```


### Step 4: Personalize per recipient (optional)

Because Braze knows each user, you can pass a user attribute into the Storyblok request to fetch different content per recipient. For example, serve a framework-specific tutorial based on a custom attribute:


```liquid
{% connected_content {{sb_base}}/stories/tutorials/{{custom_attribute.${framework}}}?version=published&cv={{space_data.space.version}}&token={{sb_token}} :save response %}
```


This assumes the attribute is already populated on the Braze user profile. Populating user data is handled on the Braze implementation side and is out of scope for this guide.

### Rate limits and caching

Connected Content fires on every send, so each send consumes Storyblok API requests. Two caching layers keep this efficient:

- Braze caches GET responses for five minutes by default. Extend it with `:cache_max_age` (up to four hours) or disable it with `:no_cache`. Use `:no_cache` only while testing so you see edits immediately, and remove it for production, or a large send multiplies requests to Storyblok.
- Storyblok serves cached content by `cv`. Cached requests have a much higher rate limit (around 1,000 per second) than uncached ones (around 50 per second). The two-call pattern keeps you on the cached path.

For high-volume campaigns, keep Braze caching on. To recover from occasional errors such as `429` or `5xx` responses, add `:retry` to the Connected Content tag so Braze retries the request.

## Content Blocks sync

**Important:**


This sync service is a reference implementation. Adapt it to your content model and test it in your environment before relying on it in production.



A service you host listens for Storyblok publish events, fetches the story, renders it to HTML, and creates or updates a matching Braze Content Block through the REST API. Marketers then insert the block like any other, with no call at send time.

### How it works

1. A Storyblok webhook fires when a story is published.
2. Your service receives the webhook, fetches the story from the Content Delivery API, and renders it to HTML.
3. Your service creates or updates a matching Braze Content Block through the REST API.
4. Marketers insert the Content Block in campaigns and Canvases like any other block.

### Step 1: Create a Braze API key

In Braze, go to **Settings** > **APIs and Identifiers** > **Create API Key** and grant it only the `content_blocks.create`, `content_blocks.update`, and `content_blocks.list` permissions. Copy the key and note your REST endpoint URL for the same instance.

### Step 2: Deploy the sync service

A minimal Node service captures the raw body for optional signature verification, fetches the story, renders the fields you care about, and upserts the Content Block.

The following code is an example built against a sample content model. The two functions that render HTML, `renderContent` and `renderBlock`, assume specific component and field names (`teaser`, `feature`, `grid`, and fields such as `title`, `intro`, and `cta_url`). These are placeholders, not Storyblok defaults. Your space uses its own components and fields, so treat these two functions as the part you rewrite, mapping your real component and field names to the HTML you want in each Content Block. Everything else in the service (webhook handling, fetching the story, matching the block by its ID prefix, and the create and update logic) works unchanged regardless of your content model.

```javascript
import express from "express";
import crypto from "crypto";

const app = express();
app.use(express.json({ verify: (req, _res, buf) => { req.rawBody = buf; } }));

const {
  STORYBLOK_TOKEN,
  STORYBLOK_BASE = "https://api.storyblok.com/v2/cdn",
  STORYBLOK_WEBHOOK_SECRET,
  BRAZE_REST_ENDPOINT,
  BRAZE_API_KEY,
  PORT = 3000,
} = process.env;

function slugPart(story) {
  return story.slug.replace(/[^a-zA-Z0-9]+/g, "_");
}

// ID first: this is the stable identity used for matching. The slug is decorative
// and may change. Because we match on the "sb_<id>_" prefix, a changed slug never
// breaks the match, and the block name (and its Liquid tag) stays stable.
function blockNameForStory(story) {
  return `sb_${story.id}_${slugPart(story)}`;
}

// "Welcome message · posts/welcome-message" visible in the Braze Content Blocks list
function blockDescriptionForStory(story) {
  return `${story.name} · ${story.full_slug}`;
}

// Adapt this to your content model. Richtext fields need a proper resolver, not shown here.
function renderBlock(block) {
  switch (block.component) {
    case "teaser":
      return block.headline ? `<h1>${block.headline}</h1>` : "";
    case "feature":
      return block.name ? `<p>${block.name}</p>` : "";
    case "grid":
      return (block.columns || []).map(renderBlock).filter(Boolean).join("\n");
    default:
      return "";
  }
}

function renderContent(story) {
  const c = story.content || {};
  const flat = [
    c.title ? `<h1>${c.title}</h1>` : "",
    c.intro ? `<p>${c.intro}</p>` : "",
    c.image?.filename ? `<img src="${c.image.filename}/m/600x0/filters:quality(80)" />` : "",
    (c.cta_url && c.cta_label) ? `<a href="${c.cta_url}">${c.cta_label}</a>` : "",
  ].filter(Boolean).join("\n");
  if (flat) return flat;
  return (c.body || []).map(renderBlock).filter(Boolean).join("\n");
}

async function fetchStory(storyId) {
  const url = `${STORYBLOK_BASE}/stories/${storyId}?token=${STORYBLOK_TOKEN}&version=published`;
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Storyblok fetch failed: ${res.status}`);
  return (await res.json()).story;
}

const USER_AGENT = "partner-Storyblok-Braze-Content-Sync/1.0";

// Calls the Braze REST API with a User-Agent header and retries with exponential
// backoff on 429 (rate limited) and 5xx responses. Honors Retry-After when present.
async function brazeFetch(url, options = {}, maxRetries = 5) {
  const headers = {
    Authorization: `Bearer ${BRAZE_API_KEY}`,
    "User-Agent": USER_AGENT,
    ...(options.headers || {}),
  };
  for (let attempt = 0; ; attempt++) {
    const res = await fetch(url, { ...options, headers });
    const retryable = res.status === 429 || res.status >= 500;
    if (!retryable || attempt >= maxRetries) return res;
    const retryAfter = Number(res.headers.get("retry-after"));
    const delay = retryAfter > 0
      ? retryAfter * 1000
      : Math.min(2 ** attempt * 500, 30000) + Math.random() * 250;
    await new Promise((resolve) => setTimeout(resolve, delay));
  }
}

// Match on the stable "sb_<id>_" prefix, so a changed slug never breaks the match.
// At scale, replace this listing with a persistent story-id to block-id map.
async function findBlockByStoryId(storyId) {
  const url = `${BRAZE_REST_ENDPOINT}/content_blocks/list?limit=1000`;
  const res = await brazeFetch(url);
  if (!res.ok) throw new Error(`Braze list failed: ${res.status}`);
  const data = await res.json();
  const prefix = `sb_${storyId}_`;
  return (data.content_blocks || []).find(b => b.name && b.name.startsWith(prefix)) ?? null;
}

async function brazePost(path, body) {
  const res = await brazeFetch(`${BRAZE_REST_ENDPOINT}/content_blocks/${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`Braze ${path} failed: ${res.status} ${await res.text()}`);
  return res.json();
}

async function upsertBlock(story) {
  const existing = await findBlockByStoryId(story.id);
  const description = blockDescriptionForStory(story);
  const content = renderContent(story);
  if (existing) {
    // Reuse the existing name so the Liquid tag never changes, even if the slug moved.
    return brazePost("update", {
      content_block_id: existing.content_block_id,
      name: existing.name,
      description,
      content,
      state: "active",
    });
  }
  return brazePost("create", {
    name: blockNameForStory(story),
    description,
    content,
    state: "active",
  });
}

async function retractBlock(storyId) {
  const existing = await findBlockByStoryId(storyId);
  if (!existing) return null;
  // Braze does not allow reverting an active block to draft, so clear the content instead.
  // name is required on update, so pass the existing one unchanged.
  return brazePost("update", {
    content_block_id: existing.content_block_id,
    name: existing.name,
    content: "<!-- unpublished -->",
  });
}

function verifySignature(req) {
  if (!STORYBLOK_WEBHOOK_SECRET) return true;
  // Confirm the exact header name and hash algorithm against Storyblok's current webhook docs before trusting this.
  const signature = req.get("webhook-signature");
  const expected = crypto.createHmac("sha1", STORYBLOK_WEBHOOK_SECRET).update(req.rawBody).digest("hex");
  return signature === expected;
}

app.post("/storyblok-webhook", async (req, res) => {
  try {
    if (!verifySignature(req)) return res.status(401).send("bad signature");
    const { action, story_id } = req.body;

    if (action === "published" || action === "moved") {
      const story = await fetchStory(story_id);
      const result = await upsertBlock(story);
      console.log("Synced:", result.liquid_tag || result.content_block_id);
      return res.status(200).send("ok");
    }

    if (action === "unpublished" || action === "deleted") {
      // story_id alone is enough, since we match on the ID prefix. No slug needed.
      await retractBlock(story_id);
      console.log(`${action}: cleared content for story ${story_id}`);
      return res.status(200).send("ok");
    }

    res.status(200).send("ignored");
  } catch (err) {
    console.error(err);
    res.status(500).send("error"); // a 500 makes Storyblok retry
  }
});

app.listen(PORT, () => console.log(`Listening on ${PORT}`));
```

Set the environment variables (`STORYBLOK_TOKEN`, `BRAZE_REST_ENDPOINT`, `BRAZE_API_KEY`, and optionally `STORYBLOK_WEBHOOK_SECRET` and `STORYBLOK_BASE` for non-EU regions), then run it on a host with a public HTTPS URL.

### Step 3: Configure the Storyblok webhook

In Storyblok, go to **Settings** > **Webhooks**, create a webhook pointing at your service URL (for example, `https://your-host/storyblok-webhook`), and enable the following story events:

- **Story published** creates or updates the Content Block in Braze.
- **Story unpublished** clears the block content so it renders nothing in emails. The block is not deleted, to avoid breaking campaigns that already reference it.
- **Story deleted** clears the block content the same way. The block itself remains in Braze.
- **Story moved** re-syncs the block with the updated description, which includes the new path. The block name is keyed on the story ID, so the Liquid tag in campaigns stays valid even though the slug changed.

If you set a secret, put the same value in `STORYBLOK_WEBHOOK_SECRET`.

### Step 4: Test the sync

1. Publish a story in Storyblok.
2. Check your service logs for a `Synced` line with the generated Liquid tag.
3. In Braze, go to **Content** > **Content Blocks** and confirm a block named like `sb_218330706569315_welcome_message` exists with your rendered HTML and a description like `Welcome message · posts/welcome-message`.
4. Insert that block in a test email, use **Preview & Test**, and confirm it renders. No Connected Content, no send-time call.
5. Edit the story, publish again, and confirm the block updates.
6. Move or rename the story, publish, and confirm the same block updates (same Liquid tag, new path in the description) rather than a duplicate being created.

## Considerations

- Static content: A synced block is identical for every recipient. For per-user content, use Connected Content instead. The two can coexist.
- No folders: Braze Content Blocks have no folder hierarchy. The Storyblok path is embedded in the block description (for example, `Welcome message · posts/welcome-message`) so marketers can identify where a block comes from without leaving Braze.
- Naming and the Liquid tag: A Content Block's name generates its Liquid tag, so campaigns reference it by name. To keep that reference stable, this guide keys the name on the story ID (`sb_<id>_<slug>`) and matches on the `sb_<id>_` prefix. As a result, renaming or moving a story in Storyblok updates the content but keeps the same block name and Liquid tag, so existing campaigns keep working. The readable slug in the name is for convenience only and may become out of date after a rename; the current title and path are always kept fresh in the block `description` field, which is shown in the Content Blocks list. Choose a naming convention that fits your own workflow before syncing at scale.
- Freshness is sync-bound: Content is as current as the last successful sync. If a sync fails, Braze serves the old block with no error at send time. Calls to Braze already retry with exponential backoff; add alerting for syncs that still fail after retries.
- Matching by listing does not scale: Listing all blocks on every sync and filtering by ID prefix is fine for a test. In production, store a Storyblok story-id to `content_block_id` map so lookups are direct.
- Richtext needs rendering: Storyblok richtext is JSON, not HTML. Use a richtext resolver before writing it into a block.
- Unpublish and delete: Braze does not allow reverting an active Content Block to draft. Unpublishing or deleting a story instead clears the block content to `<!-- unpublished -->`, so it renders nothing in emails. The block itself remains in Braze. Remove it manually if needed.
- Size and rate: The Content Blocks API shares the default limit of 250,000 requests per hour, which is ample for content sync. Keep block content within Braze's per-block size limit.

## Troubleshooting

| Issue | Resolution |
| --- | --- |
| Preview renders nothing, Connected Content shows a 301 | The request is missing the `cv` parameter, so Storyblok redirects and Braze does not follow it. Use the two-call pattern in Connected Content Step 1. |
| Preview renders nothing, Connected Content shows a 404 | The `full_slug` does not match a published story, or the base URL does not match your region. Verify both. |
| Edits do not appear | You are seeing Braze's five-minute cache, a hardcoded `cv`, or both. Add `:no_cache` while testing and fetch `cv` dynamically from the space endpoint. |
| Content Block does not appear in Braze | Confirm the Braze REST API key has the required Content Block permissions and that the REST endpoint matches your Braze instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

## Additional resources

<ul class="guide_tiles"><li><a href="https://www.storyblok.com/docs/api/content-delivery/v2"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Storyblok Content Delivery API</span></span></div></a></li><li><a href="https://www.storyblok.com/docs/api/content-delivery/v2/stories/retrieve-a-single-story"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Retrieve a single story</span></span></div></a></li><li><a href="https://www.storyblok.com/docs/api/image-service"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Storyblok Image Service</span></span></div></a></li><li><a href="https://www.storyblok.com/docs/guide/in-depth/webhooks"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Storyblok webhooks</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/connected_content"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Braze Connected Content</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/content_blocks"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Braze Content Blocks</span></span></div></a></li><li><a href="/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Create Content Block API</span></span></div></a></li><li><a href="/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Update Content Block API</span></span></div></a></li><li><a href="/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">List Content Blocks API</span></span></div></a></li></ul>
