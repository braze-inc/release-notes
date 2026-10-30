# Workspace Canvas alerts

> Workspace Canvas alerts let you set default alerts for every Canvas in a workspace, so you're proactively notified when user entries, message sends, or Canvas status changes occur outside what you expect, without configuring each Canvas individually.




**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





Workspace Canvas alerts are separate from [custom Canvas alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/custom_canvas_alerts), which you can create for a single Canvas. Use workspace alerts as the default safety net across your workspace. Use custom alerts when a specific Canvas needs its own rules.

## Prerequisites

To enable or edit workspace Canvas alerts, you need workspace admin access. To view workspace Canvas alerts, you need the "View Canvases" permission. For more information, see [Permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions).

| Permission | Access |
| --- | --- |
| Workspace Admin | Enable, disable, and edit workspace Canvas alerts. |
| View Canvases | View workspace Canvas alerts. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workspace Canvas alerts permissions" }

## How it works

Braze provisions three workspace Canvas alerts for your workspace. Each alert starts **disabled**. When you enable an alert, it applies to every active Canvas in the workspace, and to new Canvases created while the alert stays enabled—unless you opt out a Canvas.

You can monitor:

- **User entries:** Percentage change in users entering a Canvas, compared with a 7-day same-slot rolling average
- **Message sends:** Percentage change in messages sent from a Canvas, compared with a 7-day same-slot rolling average
- **Canvas archived:** When any Canvas in the workspace is archived

For user entries and message sends, Braze checks each Canvas on a 24-hour schedule by default. When one or more Canvases cross your thresholds, Braze sends a notification that includes the Canvases that breached the rules.

## Set up a workspace Canvas alert

1. Go to **Settings** > **Workspace Alerts**.
2. Select **Messaging**.
3. Select the alert you want to configure (**User Entries**, **Message Sends**, or **Canvas Archived**).
4. Review or edit the alert rules and notification settings.
5. Select **Save alert**.
6. On the **Messaging** page, turn the alert on. Confirm when prompted. Enabling applies the alert to the active Canvases currently covered in the workspace, plus any new Canvases created while it stays enabled.

Saving an alert doesn't enable it. Enable the alert from the **Messaging** page after you save.

## Alert rules

### User Entries and Message Sends

These alerts compare the current volume for each Canvas to a baseline. The baseline is a 7-day rolling average for the same evaluation window. By default, each alert uses:

- Less than 50% of the baseline (drop)
- Greater than 100% of the baseline (spike)

The two conditions are combined with **OR**, so either a drop or a spike can trigger the alert. You can edit the percentage thresholds. Braze checks these alerts every 24 hours by default.

### Canvas Archived

This alert notifies you when the status of any Canvas in the workspace changes to archived. It doesn't use volume thresholds or a rolling average.

## Notifications

Choose how recipients are notified when a workspace alert is met. You can enable one or both methods for a single alert:

- **Email:** Select recipient groups (**All admins**, **All object editors**), add individual email addresses, or both. By default, new workspace alerts email **All admins**.
- **Webhook:** Enter the webhook URL, and optionally add custom request headers required by your destination.

**Note:**


Workspace Canvas alerts don't send to Slack as a dedicated channel yet. Use email or webhook for notifications.



## Opt out for a single Canvas

By default, enabled workspace alerts apply to active Canvases. To change which workspace alerts apply to one Canvas:

1. Open the Canvas and go to **Canvas Analytics**.
2. In the **Alerts** section, select the workspace alerts summary (or **View workspace alerts**).
3. Turn off **Use workspace alerts for this Canvas**, or clear the individual workspace alerts that shouldn't apply.
4. Select **Save preferences**.

Custom Canvas alerts for that Canvas aren't affected by workspace alert opt-outs.

## Considerations

- **Disabled by default:** Workspace Canvas alerts don't send notifications until a workspace admin enables them.
- **Coverage while enabled:** An enabled alert covers active Canvases in the workspace and new Canvases created while it remains enabled, except Canvases that opt out.
- **Custom alerts stay separate:** You can still create up to two [custom Canvas alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/custom_canvas_alerts) per Canvas for Canvas-specific thresholds and schedules.
- **Draft Canvases:** Workspace volume alerts evaluate active Canvases. A draft Canvas isn't included until it launches.

## Frequently asked questions

### How are workspace Canvas alerts different from custom Canvas alerts?

Workspace Canvas alerts are defaults for the whole workspace. Custom Canvas alerts are rules you create for one Canvas (up to two per Canvas), with their own thresholds, check frequency, and recipients.

### Who receives the default email notifications?

By default, workspace alerts email the **All admins** recipient group. You can change recipients when you edit the alert.

### Do workspace alert webhooks count toward webhook usage?

No. Workspace Canvas alert webhooks don't count toward webhook rate limits or usage metrics.
