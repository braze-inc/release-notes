# Campaign and Canvas statuses

> Learn about statuses for campaigns and Canvases and how you can use them in the dashboard.

## Filtering by status

To filter your campaigns or Canvases by status, select **All Statuses**, then choose a status.

![The 'All Statuses' dropdown in the Braze dashboard.](https://www.braze.com/docs/assets/img/messaging_fundamentals/filter-by-status.png?fee3bf8ce589eaf87bb6639a76c134cf){: style="max-width:70%;"}

## Changing the status

To change the status of a campaign or Canvas, select the <i class="fas fa-ellipsis-vertical"></i> menu, then choose a status.

![A list of Canvases in the Braze dashboard, with the menu open for one of the Canvases.](https://www.braze.com/docs/assets/img/messaging_fundamentals/change-status.png?91bcf7baed3b46fafad93254e1663f4d)

## Available statuses

These are the available statuses for campaigns and Canvases:

| Status | Description |
| --- | --- |
| Active | Active campaigns and Canvases are in the process of sending. By default, you'll see active campaigns and Canvases on the respective pages. |
| Draft | Drafts of campaigns and Canvases are saved but not launched. To continue editing and begin sending, you can select the draft by going to **Messaging** in the Braze dashboard and selecting **Canvas** or **Campaigns**. |
| Archived | Archived campaigns and Canvases are messages that are no longer being sent. These campaigns and Canvases are also removed from the statistic graphs on the [**Home**](https://www.braze.com/docs/user_guide/analytics/dashboards/home) and [**Revenue**](https://www.braze.com/docs/user_guide/analytics/reports/revenue_report) pages.|
| Stopped | Stopped campaigns and Canvases are paused, but you can still edit them. To resume a Canvas, go to the **Summary** step of the Canvas builder and select **Resume Canvas**. For campaigns, select the <i class="fas fa-ellipsis-vertical"></i> menu, then **Resume**. For more information, refer to [Stopped Canvas behavior](#stopped-canvas-behavior). |
| Idle | When a campaign or Canvas is no longer sending messages, Braze will assign it an idle status to help sort and manage your list of campaigns and Canvases. You can view each idle campaign or Canvas and the date Braze automatically stops it. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Available statuses" }

### Stopped Canvas behavior {#stopped-canvas-behavior}

When a Canvas is stopped, the following occurs:

- **Scheduled messages:** Your scheduled messages won't be sent, regardless of a user's place in the Canvas. This also includes users who were queued because of rate limiting.
- **Email sends:** Email sends may not stop immediately, as your email service provider (ESP) may continue processing your existing requests.
- **Delay steps:** Users in a [delay step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/delay_step) will remain there as normal, but will exit the Canvas when the set period ends.
- **Draft changes:** Any draft changes to the Canvas will be discarded when the Canvas is stopped.

#### When you resume a Canvas

To resume the Canvas, go to the **Summary** step of the Canvas builder and select **Resume Canvas**. When you resume a Canvas, users whose scheduled time has not yet passed continue through their journey from where they left off:

- Users in Delay steps: The delay keeps counting down while a Canvas is stopped. If a user's delay ends while the Canvas is stopped, they exit the Canvas. If you resume before it ends, they advance at their original time. For example, a user is two hours into a 24-hour delay when you stop the Canvas. They exit 22 hours later unless you resume the Canvas before then. For more information, see [Stopping Canvases](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch#stopping-canvases).
- Users waiting for messages: Any scheduled messages that were pending when the Canvas was stopped are sent as scheduled when you resume the Canvas—as long as the scheduled time hasn't already passed.
- Users who exited: Users who exited the Canvas during the stopped period (for example, users who were in Delay steps and reached the end of their delay) won't re-enter the Canvas when you resume it.

#### Local time zone behavior

If your Canvas is configured to **Enter users into this Canvas in their local time zone**, keep these considerations in mind when stopping and resuming:

- Entry windows: When you resume the Canvas, users enter based on their local time zone as originally configured. Braze continues evaluating entry eligibility according to each user's time zone.
- Missed entry windows: If the Canvas was stopped during a scheduled entry window for users in certain time zones, those users won't enter retroactively when the Canvas is resumed. Entry evaluation resumes going forward.

#### Common scenarios

##### Mistake in message content

You launch a Canvas but notice a typo in one of the messages. Stop the Canvas, edit the message in draft mode, then resume. Users who haven't received the message yet get the corrected version. Users who already received it won't receive it again.

##### Targeting issue

You realize the Canvas is targeting the wrong segment. Stop the Canvas immediately to prevent more users from entering. Any users currently in Delay steps will exit when their delay period ends. You can then create a new Canvas with the correct targeting.

## Best practices

### Monitor your messages by status

You can monitor your messages by status to review the performance details. For example, if you have a series of active campaigns, you can evaluate the performance of each campaign with their engagement metrics and make adjustments as needed. If instead you have a few stopped Canvases, you can consider whether they should be resumed for messaging or archived entirely.

**Tip:**


Looking for more ways to stay organized? Add [teams](https://www.braze.com/docs/user_guide/administer/global/user_management/teams) and [tags](https://www.braze.com/docs/user_guide/messaging/governance/tags) to provide more context at-a-glance.



### Audit your active messages

By performing audits of your active campaigns and Canvases, you can assess the relevance and performance, and remove or update any outdated campaigns and Canvases to keep your messaging fresh.
