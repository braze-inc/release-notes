# Notify consumers of order updates with Content Cards

> Keep a custom Content Card feed current with the latest order status by logging order updates from your order management system (OMS), sending Content Cards for updates such as shipped or cancelled, and dismissing stale cards in the app with key-value pairs.

## About this example

Flash & Thread, a fictional clothing and beauty retailer, wants a horizontal Content Card feed in its mobile apps where each card shows the status of a purchase—for example, when an order moves from `picked` to `dispatched` (shipped), or when it is `cancelled`.

Its order management system stores the consumer's email, order number, order status, and tracking URL, and can call Braze when those values update. Marketing wants status-specific card copy (for example, "Your order is on the way" for `dispatched` versus "We're preparing your order" for `picked`). Dismiss older cards for the same order (such as a `picked` card after a `dispatched` card has arrived) so consumers only see the latest status.

This example shows how to:

1. Log a custom event (for example, `order_update`) to [`/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) when the order management system records a status change such as pending, held, picked, dispatched, or cancelled
2. Trigger a separate action-based Content Card campaign for each of those statuses, with Liquid personalization from event properties
3. Set key-value pairs (`extras`) such as `order_number` and `order_hierarchy` on each card
4. In a custom Content Card feed, keep only the card with the highest `order_hierarchy` for each `order_number` and dismiss the rest

Use this when dashboard removal events alone cannot target a single order's card among many cards from the same journey.

## Considerations

- Content Cards expire and are purged after at most 30 days from send. Set a shorter expiration for terminal statuses (for example, cancelled) when you want them to leave the feed sooner. See [Create a Content Card](https://www.braze.com/docs/user_guide/channels/content_cards/create_a_content_card).
- If the order management system only has email, identify the user on `/users/track` with the secondary `email` identifier. Prefer `external_id` when the order management system has it. User aliases remain an option when you need a custom identifier type; set `alias_name` to the identifier value and `alias_label` to the type (for example, `email`). See [Identifier resolution](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/#identifier-resolution) and [User alias object](https://www.braze.com/docs/api/objects_filters/user_alias_object).
- Custom event properties are available for Liquid personalization and event-property segmentation when you use the event-triggered path. They do not persist on the profile as attributes unless you also write them as attributes.
- API-triggered Content Card campaigns are an alternative that avoids logging a custom event (and its data points), but each campaign needs its own trigger send, and you lose event-property segmentation for that signal.
- Custom feeds do not refresh mid-session until the next session start or a manual [`requestContentCardsRefresh`](https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed) call. Call refresh when the consumer opens or pulls to refresh the order feed.
- Fully custom Content Card UIs require [manual analytics logging](https://www.braze.com/docs/developer_guide/content_cards/logging_analytics) (impressions, clicks, dismissals). Subclassing the default feed is less work but does not support a horizontal carousel.
- This hierarchy logic assumes one active status per order number at a time. If one order can have multiple concurrent statuses (for example, split warehouse fulfillments), add another key (such as a fulfillment ID) and include it in your keep-or-dismiss rules.
- App-side dismissal logic requires a new app release. Test in a development workspace before production.

## Setup

### Step 1: Log order updates from the order management system

When the order management system records a status change, send a custom event to `/users/track`. Include event properties the Content Card personalizes and that the app reads from `extras`.

The following table shows example properties:

| Property | Purpose |
| --- | --- |
| `order_number` | Groups cards for the same order |
| `order_status` | Status label for copy and campaign filters |
| `tracking_url` | Optional deep link or button URL |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Order update event properties" }

An example request that identifies the user by email is:

```json
POST https://rest.iad-01.braze.com/users/track
Content-Type: application/json
Authorization: Bearer {YOUR_REST_API_KEY}

{
  "events": [
    {
      "email": "alex@example.com",
      "name": "order_update",
      "time": "2026-09-28T16:02:05Z",
      "properties": {
        "order_number": "12345",
        "order_status": "picked",
        "tracking_url": "https://www.flashandthread.example/track/12345"
      }
    }
  ]
}
```

Use your workspace REST endpoint and an API key with `users.track` permission. Replace the sample email and order values with your order management system's payload.

### Step 2: Create a Content Card campaign per order status

Create one action-based Content Card campaign for each status you send (for example, `pending`, `held`, `picked`, `dispatched`, `cancelled`).

1. Go to **Messaging** > **Campaigns**, select **Create campaign**, then select **Content Cards**.
2. Set action-based delivery on the `order_update` custom event. Filter on the matching `order_status` event property so only that status enters this campaign.
3. Use Liquid event properties to personalize the card title or body:


```liquid
Order {{event_properties.${order_number}}} is {{event_properties.${order_status}}}.
```


{: start="4"}
4. On the **Settings** tab, select **Add new pair** and add the key-value pairs used by the app:

| Key | Value |
| --- | --- |
| `order_number` | `{{event_properties.${order_number}}}` |
| `order_status` | `{{event_properties.${order_status}}}` (or the fixed status for that campaign) |
| `order_hierarchy` | Integer for this status (hardcoded per campaign) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Card key-value pairs" }

The following table shows an example hierarchy. The app keeps the card with the highest value for each order:

| Status | `order_hierarchy` |
| --- | --- |
| pending | 1 |
| held | 2 |
| picked | 3 |
| dispatched | 4 |
| cancelled | 5 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Example order hierarchy values" }

{: start="5"}
5. Set card expiration (up to 30 days). Prefer a shorter duration for terminal statuses.

Dashboard removal events apply at the campaign level and cannot remove only one order's card while leaving others from the same campaign. That is why the app dismisses stale cards using `extras`.

### Step 3: Keep the latest card per order in the custom feed

Subscribe to Content Card updates in your custom feed, read `extras`, and for each `order_number` keep the card with the highest `order_hierarchy`. Dismiss the rest with your platform's dismiss API so analytics stay accurate.

For each card in the feed:

1. Read `order_number` and `order_hierarchy` from `extras`.
2. Find the highest `order_hierarchy` among cards that share that `order_number`.
3. If the card's hierarchy matches the highest value, show it (map card fields into your custom UI object).
4. Otherwise, dismiss the card.

Implement the subscribe and dismiss calls with the current SDK for your platform. Start from:

- [Creating cards](https://www.braze.com/docs/developer_guide/content_cards/creating_cards)
- [Customizing the feed](https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed)
- [Logging analytics](https://www.braze.com/docs/developer_guide/content_cards/logging_analytics)

When the consumer is already in the app, call `requestContentCardsRefresh` so new order cards appear without waiting for the next session.

### Step 4: Test the journey end to end

1. Send a sequence of `order_update` events for the same order with rising `order_status` values.
2. Confirm each status campaign sends the expected card and Liquid resolves.
3. Confirm the feed shows one card per order and that lower-hierarchy cards are dismissed.
4. Confirm impressions, clicks, and dismissals appear in campaign analytics for your custom UI.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/channels/content_cards/create_a_content_card"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Create a Content Card</span></span></div></a></li><li><a href="/docs/developer_guide/content_cards/customizing_cards/behavior"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Content Card key-value pairs and behavior</span></span></div></a></li><li><a href="/docs/developer_guide/content_cards/creating_cards"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Creating custom Content Cards</span></span></div></a></li><li><a href="/docs/developer_guide/content_cards/customizing_cards/feed"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Customizing the Content Card feed</span></span></div></a></li><li><a href="/docs/developer_guide/content_cards/logging_analytics"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Logging Content Card analytics</span></span></div></a></li><li><a href="/docs/api/endpoints/user_data/post_user_track"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">POST: Create and update users</span></span></div></a></li></ul>
