# Monitor Content Card delivery with alerts and Currents

> Use debugging tools, threshold alerts, Currents events, and API monitoring to catch Content Card delivery drops before users report them.

## About this example

Pyrite Financial, a fictional mobile banking brand, renders a Content Card in a dedicated slot on its app home screen. That slot is expected to hold a card for the most users, so an empty slot is a signal worth investigating.

This example shows how to:

1. Validate the Content Card integration in testing with the SDK Debugger, internal groups, and the Event user log
2. Set campaign or Canvas threshold alerts on expected message volume
3. Track Canvas entries, Content Card sends, impressions, and aborts in [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents)
4. Watch the REST API endpoints that trigger messaging for volume drops and non-200 responses
5. Add supplemental send-volume checks in Datadog or with Canvas export endpoints
6. Log app-side fallback behavior that Braze cannot observe

Use this when a Content Card placement is business-critical and you need an operational signal that delivery has dropped. Each step is optional, so start with the ones your workspace already supports.

## Considerations

- Decide first whether every targeted user should always see a card in the placement, or whether an empty slot is acceptable for some users. Volume thresholds and fallback logic depend on that answer.
- Braze monitors SDK connectivity and reports incidents on the [Braze status page](https://braze.statuspage.io/). This example covers what you monitor yourself: campaign and Canvas configuration, message volume, API traffic, and app-side fallback behavior.
- Not every trigger produces a message. After a trigger reaches Braze, journey logic, targeting, frequency capping, and rate limiting can all reduce sends. Compare trigger volume to send volume as a trend, not as a one-to-one match.
- Event-level monitoring requires Currents. Without Currents, use campaign and Canvas analytics, threshold alerts, and the REST export endpoints instead.
- Datadog metrics report send counts only and can differ slightly from the Braze dashboard and Currents.
- Excessive refreshes can be rate limited. The SDK enforces per-device rate limits on Content Card refresh requests. Call the refresh method at meaningful points in the user lifecycle rather than repeatedly in quick succession. See [Content Cards rate limit](https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed#rate-limit) and [Improve latency for Content Cards as banners](https://www.braze.com/docs/user_guide/channels/content_cards/best_practices/improving_low_latency_requirements).
- Liquid can intentionally suppress a card. When [Liquid aborts a message](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), Braze logs a Content Card Abort event rather than a send. Treat aborts as expected behavior for conditional content and as a signal only when the volume changes.
- If your app shows default content when no card is available, track that in your own app analytics. Braze only knows what it sent, not whether your app showed a card or a placeholder.

## Setup

### Step 1: Validate the integration before launch

Confirm expected behavior so that production alerts reflect real problems rather than integration gaps.

1. Create a debugging session in the [SDK Debugger](https://www.braze.com/docs/developer_guide/sdk_integration/debugging) to watch SDK activity in real time and confirm that card requests and impressions are logged.
2. Add test accounts to an [internal group](https://www.braze.com/docs/user_guide/administer/global/user_management/internal_groups) so you can test the campaign or Canvas against test users before launch.
3. Check the [Event user log](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) for an individual user to confirm which campaign delivered each card to the SDK.

Record the send, impression, and abort volumes you see during testing. These become the baseline for the thresholds you set.

### Step 2: Set threshold alerts on the campaign or Canvas

Threshold alerts notify you by email or webhook when message volume falls outside the range you expect. Webhook alerts can route to a Slack channel or an on-call system.

- **Campaigns:** Set upper and lower thresholds on the campaign analytics page. For setup steps, see [Campaign alerts](https://www.braze.com/docs/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts).
- **Canvases:** Configure alerts on user entries, messages sent, or both from the **Manage Alerts** page. For setup steps, see [Canvas threshold alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts).

Choose a lower threshold that is less than normal volume and greater than zero, so a partial drop triggers a notification instead of waiting for a complete outage.

### Step 3: Track entries, sends, and impressions in Currents

Currents streams message engagement and customer behavior events to your data platform in near real time, which lets you monitor volume and latency outside the Braze dashboard.

For a Content Card sent from a Canvas, these events cover the path from entry to impression.

| Event | Currents event name | What it tells you |
| --- | --- | --- |
| Canvas Entry | `users.canvas.Entry` | A user entered the Canvas that sends the card |
| Content Card Send | `users.messages.contentcard.Send` | Braze created and sent the card for the user |
| Content Card Impression | `users.messages.contentcard.Impression` | The card recorded an impression for the user |
| Content Card Abort | `users.messages.contentcard.Abort` | Liquid logic prevented the card from being sent |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Currents events for Content Card delivery" }

For a Content Card campaign, monitor the send, impression, and abort events, and filter on `campaign_id`.

- **Volume monitoring:** Track sends and impressions per Canvas or campaign over a fixed window and alert when volume falls below a threshold based on historical data.
- **Latency monitoring:** Compare entry events to send events for create latency, and send events to impression events for display latency. If cards are created at first impression, measuring from entry to impression mixes create and display time, so use send-to-impression timing for display latency.

Comparing volumes across stages helps identify common failure modes:

- Fewer entries point to an upstream trigger or audience problem.
- Steady entries with fewer sends can point to journey logic, targeting, or Liquid aborts. If cards are created at first impression, it can also mean users have not opened the app yet.
- Steady sends with fewer impressions point to something between card creation and display, such as SDK refresh, placement rendering, or device rate limits.

For event payloads and fields, see [Message engagement events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

### Step 4: Watch API traffic and error responses

If your triggers originate from your own systems, monitor the API layer that feeds them.

1. Set up [API usage alerts](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts) on the endpoints that trigger your messaging. Configure conditions for volume drops and increases in non-200 responses.
2. Review non-`200` responses for those endpoints. A rise in error responses can indicate that a recent release introduced a malformed request or that calls are hitting a rate limit.

### Step 5: Add supplemental volume checks

Use these when you want send-volume data in an existing observability tool or a scheduled job.

- **Datadog:** The [Datadog integration](https://www.braze.com/docs/partners/data_and_analytics/business_intelligence/datadog) provides the `braze.messaging.sent` metric, tagged with campaign, Canvas, and Canvas step identifiers. Use it for send counts from a specific message step in a given time frame. Those counts approximate Content Card Send volume at an aggregate level and do not include user or send identifiers.
- **Export endpoints:** Poll [`/canvas/data_series`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics) and [`/canvas/data_summary`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics_summary) for Canvas entries and message sends, then compare results across runs to spot trends and anomalies.

### Step 6: Log fallback behavior in your app

Braze reports what it sent, not what your app rendered. Add app-side logging or analytics for the cases that Braze cannot observe:

- The feed refresh completed, but no cards were available for the placement.
- The app displayed fallback content instead of a card.
- The refresh request failed or was rate limited.

Send these as custom events if you want them alongside Braze data, or keep them in your own analytics platform and compare them to Currents impression volume.

### Step 7: Triage when an alert fires

Work through these checks in order:

1. Confirm there is no active incident on the [Braze status page](https://braze.statuspage.io/).
2. In Currents (or Canvas and campaign analytics), compare entry, send, impression, and abort volumes for the same window. If cards are created at first impression, entry volume can exceed send volume until users open the app—account for that when you compare volumes.
3. Check API usage alerts and non-`200` responses on the endpoints that trigger the message.
4. Compare app-side fallback or empty-placement events to Currents impression volume.
5. Reproduce with a sample user in the [SDK Debugger](https://www.braze.com/docs/developer_guide/sdk_integration/debugging) and the [Event user log](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log).

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/channels/content_cards/reporting"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Content Card reporting</span></span></div></a></li><li><a href="/docs/user_guide/channels/content_cards/create_a_content_card/card_creation"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Card creation</span></span></div></a></li><li><a href="/docs/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Campaign alerts</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Canvas threshold alerts</span></span></div></a></li><li><a href="/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Message engagement events</span></span></div></a></li><li><a href="/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">API usage alerts</span></span></div></a></li></ul>
