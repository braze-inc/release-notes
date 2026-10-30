# Link API-triggered Canvas requests to Currents messaging events

> Trace an API-triggered Canvas request through to its messaging outcomes by passing a correlation ID as a Canvas entry property, stamping it onto the send event with `message_extras`, and joining engagement events on `dispatch_id` and `user_id`.

## About this example

Pyrite Financial, a fictional financial services brand, triggers a Canvas from its own systems each time a consumer transaction needs an alert. It calls [`/canvas/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases) per event. Its analytics team wants to know which trigger request produced which send, delivery, and click in [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) or [Snowflake Data Sharing](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake). Both include the same messaging event data.

Messaging events in Currents and Snowflake Data Sharing do not carry your trigger request identifier on their own. This example shows how to:

1. Generate a correlation ID in your sending system and pass it as a Canvas entry property on the trigger request.
2. Reference that property in the message body with the [`message_extras` Liquid tag](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras), which writes it to the `message_extras` field on the send event.
3. Join the send event to delivery and click events on `dispatch_id` and `user_id`.

Use this when an external system owns the trigger and you need to report on downstream engagement per request. If a campaign rather than a Canvas fits your use case, use a [send identifier](https://www.braze.com/docs/api/identifier_types#send-identifier) instead. The `send_id` field is supported by the campaign messaging endpoints, not by `/canvas/trigger/send`.

## Considerations

- `dispatch_id` alone is not a unique key for Canvas. Braze treats Canvas steps as triggered events, so a step may generate a unique `dispatch_id` per user per send, or a shared `dispatch_id` across users in the same send. Always pair it with `user_id`. For more information, see [Dispatch ID behavior](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/dispatch_id).
- The `message_extras` field appears on send events only. Delivery, open, and click events don't include it, which is why the correlation ID travels through the send event and then joins outward.
- Message extras are attached at send time per message, so a Canvas with several Message steps needs the tag in each step you plan to report on.
- All `message_extras` keys and values together must stay under 1,000 bytes (1&nbsp;KB), and Braze truncates longer values. Whitespace counts toward the limit.
- The resulting JSON contains string values only. Use a Liquid variable as a key or value. Don't nest other Liquid tags inside `message_extras`.
- Currents events store the Braze user ID in `user_id` and your own identifier in `external_user_id`. Join on `user_id`, and select `external_user_id` when you need to match rows back to your systems.
- Use [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) or [Snowflake Data Sharing](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake) for this pattern. Both expose the same messaging event fields, including `message_extras` on send events.
- Currents and Snowflake schemas flag `message_extras` as PII. Use an opaque request ID rather than consumer data.
- The `context` object on a Canvas trigger request can be up to 50&nbsp;KB, shared across all properties you pass.

## Setup

### Step 1: Generate a correlation ID per request

In your sending system, create an identifier for each trigger request—for example, a UUID—and store it with your own request log. Keep it opaque and short enough to fit the `message_extras` size limit.

### Step 2: Pass the ID as a Canvas entry property

Include the ID in the `context` object on your [`/canvas/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases) request. Set it per recipient when each user has a distinct ID, or at the top level when one ID covers every recipient in the request.

```json
{
  "canvas_id": "canvas_identifier",
  "recipients": [
    {
      "external_user_id": "user_identifier",
      "context": {
        "request_id": "8f14e45f-ceea-467a-9e30-6b1b1c4a7d20"
      }
    }
  ]
}
```

Canvas entry properties are available as [context variables](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables) throughout the Canvas.

### Step 3: Stamp the ID onto the send event

In each Message step you want to report on, assign the context variable and pass it to `message_extras`.


```liquid
{% assign request_id = context.${request_id} %}
{% message_extras :key request_id :value {{request_id}} %}
```


Braze attaches the key-value pair to the `message_extras` field on the send event at send time.

### Step 4: Verify with a test send

Send a test entry through the Canvas, then confirm the send event in Currents or Snowflake Data Sharing contains `message_extras` with your `request_id` key. If the field is empty, check the [tag syntax](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras#checking-syntax). Mistyped delimiters and out-of-order keys and values are the common causes.

### Step 5: Join sends to delivery and click events

With the ID on the send event, join outward on `dispatch_id` and `user_id`. The following [Query Builder](https://www.braze.com/docs/user_guide/analytics/reports/query_builder) example reports delivery and click outcomes per request for email:


```sql
WITH sends AS (
  SELECT
    USER_ID,
    EXTERNAL_USER_ID,
    DISPATCH_ID,
    PARSE_JSON(MESSAGE_EXTRAS):request_id::STRING AS request_id,
    TIME AS send_time
  FROM USERS_MESSAGES_EMAIL_SEND_SHARED
  WHERE MESSAGE_EXTRAS IS NOT NULL
    AND PARSE_JSON(MESSAGE_EXTRAS):request_id IS NOT NULL
)
SELECT
  s.request_id AS "Request ID",
  s.EXTERNAL_USER_ID AS "External User ID",
  MIN(s.send_time) AS "Sent",
  MIN(d.TIME) AS "Delivered",
  MIN(c.TIME) AS "First Click"
FROM sends AS s
LEFT JOIN USERS_MESSAGES_EMAIL_DELIVERY_SHARED AS d
  ON d.USER_ID = s.USER_ID
  AND d.DISPATCH_ID = s.DISPATCH_ID
LEFT JOIN USERS_MESSAGES_EMAIL_CLICK_SHARED AS c
  ON c.USER_ID = s.USER_ID
  AND c.DISPATCH_ID = s.DISPATCH_ID
GROUP BY 1, 2
ORDER BY 3 DESC;
```


Swap in the tables for the channel you send on—for example, `USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED` and `USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED` for push. For the full column list per table, see the [SQL table reference](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).

The Query Builder example is one path. Apply the same joins in [Snowflake Data Sharing](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake) or on Currents exports to your own warehouse: parse `message_extras` on the send event, then join engagement events on `dispatch_id` and `user_id`.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Message extras Liquid tag</span></span></div></a></li><li><a href="/docs/user_guide/messaging/messaging_fundamentals/dispatch_id"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Dispatch ID behavior</span></span></div></a></li><li><a href="/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">POST: Send Canvas messages using API-triggered delivery</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Context variables</span></span></div></a></li><li><a href="/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Message engagement events</span></span></div></a></li><li><a href="/docs/partners/data_and_analytics/data_warehouses/snowflake"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Snowflake Data Sharing</span></span></div></a></li><li><a href="/docs/user_guide/analytics/reports/query_builder"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Query Builder</span></span></div></a></li><li><a href="/docs/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">SQL table reference</span></span></div></a></li></ul>
