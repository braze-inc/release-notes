# Braze release notes

This is a public-facing repository for Braze release notes. It highlights what is new at Braze and is maintained by the [Braze Docs team](https://github.com/braze-inc/docs-team).

## Source and publishing flow

Public markdown documentation is mirrored from [`www.braze.com/docs`](https://www.braze.com/docs/) using each page's rendered `index.md` endpoint.

- Sync cadence: daily (automated)
- Manual sync: workflow dispatch available in GitHub Actions
- Branch behavior: workflow runs on `main` and commits mirrored content to `main`
- Destination structure: `docs/User Guide`, `docs/Developer Guide`, `docs/API`, `docs/Technology Partners`, and `docs/What's New`
- Change reports: daily change log written to `changes/YYYY-MM-DD.md`

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
