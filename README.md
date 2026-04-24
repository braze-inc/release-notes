# Braze release notes

This is a public-facing repository for Braze release notes. It highlights what is new at Braze and is maintained by the [Braze Docs team](https://github.com/braze-inc/docs-team).

## Source and publishing flow

Public markdown documentation is mirrored from [`www.braze.com/docs`](https://www.braze.com/docs/) using each page's rendered `index.md` endpoint.

- Sync cadence: weekdays (Monday through Friday, automated; Saturday and Sunday changes roll into Monday's pull request)
- Manual sync: workflow dispatch available in GitHub Actions
- Branch behavior: workflow commits mirrored content to the `docs-sync/public-docs-mirror` branch and opens (or updates) a pull request to `main`; a Docs team reviewer approves and merges the PR to update `main`
- Destination structure: `docs/User Guide`, `docs/Developer Guide`, `docs/API`, `docs/Technology Partners`, and `docs/What's New`
- Change reports: daily change log written to `changes/YYYY-MM-DD.md`

For a full technical reference, including a line-by-line walkthrough of the workflow and sync script, see [ARCHITECTURE.md](ARCHITECTURE.md).

## How to subscribe to updates

You can subscribe to repository updates from the **Watch** menu on GitHub.

1. Open this repository on GitHub.
2. Select **Watch**.
3. Choose a notification level:
   - **All Activity**: Notify on all activity.
   - **Participating and @mentions**: Notify only when you are directly involved.
   - **Custom**: Choose specific events.

## GitHub notifications and alerts

GitHub can send alerts through the web UI and email, based on your personal notification settings.

To manage alerts:

1. Go to GitHub **Settings**.
2. Open **Notifications**.
3. Configure:
   - Email and web notifications
   - Watched repository behavior
   - Notification routing and filtering

For details, see [GitHub notifications documentation](https://docs.github.com/en/subscriptions-and-notifications).
