# Quiet hours

> Quiet hours prevent messages from being sent during a specified time window. You can use them to avoid contacting users at inconvenient times (like overnight or early in the morning) while still sending at an optimal time outside that window.

**Note:**


You can also set [workspace quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) as a default for a messaging channel across your workspace. Workspace quiet hours requires the appropriate user permissions.



## How quiet hours work

You can configure quiet hours at the campaign or Canvas level in the campaign or Canvas composer. When quiet hours are enabled and a message would otherwise be sent during the restricted window, Braze holds the message and delivers it at the next available time after quiet hours end.

For example, if quiet hours run from 10 pm to 6 am and a message is scheduled for 5:30 am, Braze delivers it at 6 am instead.

**Note:**


Quiet hours apply in each user's local time zone.



## Quiet hours and Intelligent Timing

Quiet hours and Intelligent Timing operate independently. Enabling quiet hours does not require Intelligent Timing to be on, and the same is true in reverse. In general, we recommend choosing one or the other rather than using both together, unless there are policy, compliance, or other requirements that make quiet hours necessary alongside Intelligent Timing.

- **Without Intelligent Timing:** Quiet hours act as a no-send window for your scheduled send time. If the scheduled time falls within quiet hours, the message is held and sent when the window closes.
- **With Intelligent Timing:** Braze still calculates each user's optimal send time. If that time falls within quiet hours, the message is held and delivered at the nearest edge of the quiet window instead.

**Note:**


When Intelligent Timing is active for an action-based campaign, the quiet hours fallback controls (**Abort message** versus **Send at next available time**) may be hidden in the campaign builder. Intelligent Timing adjusts send times that fall inside quiet hours to the nearest edge of the quiet hours window. The abort fallback option is not available when Intelligent Timing is on.



For more information on configuring quiet hours within an Intelligent Timing campaign, see [Intelligent Timing](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_timing).

## Quiet hours and API sends

Quiet hours also apply to messages you send through the REST API. The following table shows which window applies to each send type and what happens when a message falls in quiet hours.

| Send type | Quiet hours that apply | If the send time falls in quiet hours |
|---|---|---|
| API-triggered campaign | The campaign's quiet hours, or [workspace quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) for the channel | Braze doesn't send the message. |
| API-triggered Canvas | The Canvas or Message step quiet hours, or workspace quiet hours for the channel | Braze follows the Canvas fallback setting (**Abort message** or **Send at next available time**). |
| API campaign (`/messages/send` or `/messages/schedule/create`) | Workspace quiet hours only. Campaign-level quiet hours don't apply. | Braze doesn't send the message. To send anyway, set `ignore_workspace_quiet_hours` to `true` in a request to the [`/messages/send` endpoint](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Quiet hours for API sends" }

- API-triggered campaigns don't hold messages. The **Send at next available time** option is only available for action-based campaigns, so Braze doesn't send a message that falls in quiet hours. To deliver outside quiet hours, schedule the send for a time outside the window, or use `at_optimal_time`, which factors quiet hours into each user's send time.
- The API call still succeeds. Braze checks quiet hours when it processes the send, after it returns the API response. If quiet hours stop a message, the API doesn't return an error. These messages appear in the [Message Activity Log](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).

## Considerations

- **Messages send at the same time when quiet hours end.** If a large audience has messages held during quiet hours, all of those messages send at once when the window closes. For time-sensitive campaigns, consider how this affects delivery timing.
- **Quiet hours are not the same as aborting a message.** Aborting a message discards it entirely. Quiet hours hold the message and deliver it later.
- **Quiet hours do not re-evaluate segment membership for a held send.** Braze checks segment membership when the message is triggered. If the user is eligible then, Braze holds the message and sends it when quiet hours end. This is separate from [re-evaluating segment membership at send-time](https://www.braze.com/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#audience-criteria-evaluation) or Canvas [delivery validations](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations).
- **Quiet hours are separate from frequency capping and rate limiting.** Each of these delivery controls applies independently. A message that clears frequency and rate limits can still be held by quiet hours, and a message held by quiet hours is evaluated against frequency capping and rate limits when it eventually sends. For how Braze evaluates frequency capping relative to quiet hours, see [When frequency capping is checked](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping#when-frequency-capping-is-checked).

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Workspace quiet hours</span></span></div></a></li><li><a href="/docs/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices#comply-with-sms-sending-times"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Comply with SMS, MMS, and RCS sending times</span></span></div></a></li></ul>
