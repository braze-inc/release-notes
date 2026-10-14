# Persist push notifications in a Content Card message inbox

> Keep important push content available after a notification is dismissed. Send a matching Content Card into a custom in-app message inbox, and filter that inbox with key-value pairs.

## About this example

Pyrite Financial, a fictional mobile banking brand, is starting to send push notifications with Braze. After a consumer dismisses a push notification, the message is gone from the device UI.

The Marketing and Product teams want consumers to open a persistent message inbox from a bell icon in the app. Consumers can reopen document-ready alerts, transaction notices, and planned outage messages there.

They already use Content Cards in another part of the app (for example, articles). This pattern adds a second Content Card placement, a message inbox that can receive:

- A push notification only
- A Content Card only
- A push notification and a matching Content Card together

A tap on the push notification and a tap on the Content Card can deep link to the same destination (for example, documents). For some push messages, the tap opens the inbox itself.

This example shows how to orchestrate push notification and Content Card delivery. To build the custom inbox UI in the SDK, see [Tutorial: Content Card inboxes](https://www.braze.com/docs/developer_guide/content_cards/content_card_inbox). For card layout details, see [Creating custom Content Cards](https://www.braze.com/docs/developer_guide/content_cards/creating_cards/#message-inbox).

## Considerations

- Content Cards remain available for up to 30 days after you send them. They count toward the per-user feed limit of 250 non-expired cards, including dismissed cards. Each card payload is limited to 2&nbsp;KB after Liquid renders. See [Create a Content Card](https://www.braze.com/docs/user_guide/channels/content_cards/create_a_content_card).
- If you already use Content Cards elsewhere in your app, use key-value pairs (for example, `feed_type: inbox` versus `feed_type: article`) to create separate placements. Each screen then shows only its cards. All cards share one SDK feed until your app filters them. See [Customizing Content Card feeds](https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed/#implementing-multiple-feeds).
- Content Cards refresh automatically at session start. Additional refreshes use [`requestContentCardsRefresh`](https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed). Refresh when the inbox opens or on pull-to-refresh. Avoid continuous or every-tab refreshes so you do not hit [refresh rate limits](https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed/#rate-limit).
- Custom inbox UIs must [log impressions, clicks, and dismissals](https://www.braze.com/docs/developer_guide/content_cards/logging_analytics) manually. Unread badges (for example, a dot on the bell icon) are managed by your app.
- Every push notification that should persist in the inbox needs a matching Content Card. Include the correct key-value pairs and deep links. Use a multichannel campaign template or Canvas template so the Content Card channel stays included.
- Use a [multichannel campaign](https://www.braze.com/docs/user_guide/messaging/campaigns/creating_campaign/#create-a-multichannel-campaign) for a simultaneous push notification and Content Card send with no follow-up logic. Use [Canvas](https://www.braze.com/docs/user_guide/messaging/canvas) when you need delays, branching, re-engagement, or later steps based on engagement.

## Setup

### Step 1: Define inbox key-value pairs and deep links

Agree on the `extras` (key-value pairs) the app uses to filter and act on inbox cards. The following table shows an example set.

| Key | Example value | Purpose |
| --- | --- | --- |
| `feed_type` | `inbox` | Include the card in the message inbox (exclude from other feeds) |
| `message_type` | `document`, `outage`, `transaction` | Optional grouping or styling in the inbox UI |
| `doc_id` | `12345` | Optional ID so the app can dismiss the card when the consumer opens that document |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Example inbox key-value pairs" }

Decide deep link targets for each use case. The following table lists example targets.

| Use case | Push notification deep link | Content Card deep link |
| --- | --- | --- |
| New document or transaction | Documents or transactions screen | Same destination |
| Planned outage | Message inbox | Inbox card detail or status page |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Example deep link targets" }

Ask your engineering team to implement filtering, optional unread state, and analytics against these keys. Reuse the same keys in every inbox Content Card.

### Step 2: Choose a multichannel campaign or Canvas

Choose a multichannel campaign or Canvas based on the journey. The following table compares the two paths.

| Situation | Recommended path |
| --- | --- |
| One-time or scheduled announcement with no follow-up (for example, planned outage) | Multichannel campaign with push notifications and Content Cards |
| Event-triggered journey with possible follow-up (for example, document available, then remind if unread) | Canvas with a Message step that includes push notifications and Content Cards |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaign versus Canvas for push notification and Content Card pairing" }

For an example of this pattern, see [Content Cards in Canvas — Push notification inbox](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/#push-notification-inbox).

### Step 3: Configure message delivery

#### Multichannel campaign

1. Go to **Messaging** > **Campaigns**, select **Create campaign**, then select **Multichannel**.
2. On the **Compose** step, select **Add channel** and add push and Content Cards.
3. Compose the push notification. In **On-Click Behavior**, set the deep link to the inbox or another in-app destination.
4. Compose the Content Card with matching or complementary copy. On the **Settings** tab, select **Add New Pair** and add the inbox key-value pairs from Step 1. Set the Content Card deep link.
5. Schedule action-based delivery for events such as a new document. Use scheduled delivery for planned outages. Define the audience.
6. Save a template or checklist so future inbox-backed push campaigns include the Content Card channel and the same `extras`.

#### Canvas

1. Go to **Messaging** > **Canvas**, then select **Create Canvas**. Set the entry schedule and audience for the journey (for example, a custom event when a document is ready).
2. Add a Message step that includes both push and Content Cards. Use consecutive Message steps if the flow needs them.
3. Compose the push notification and Content Card the same way as in the campaign path, including deep links and inbox key-value pairs.
4. Optionally add later steps that use Content Card engagement. For example, if no click occurs within 48 hours, send a follow-up message. Before you depend on those filters, confirm which analytics your custom inbox logs.

### Step 4: Confirm app inbox behavior

Before launch, confirm with your engineering team that the app:

1. Subscribes once to Content Card updates early in the app lifecycle. Reuse an existing subscription if Content Cards are already live elsewhere.
2. Renders the inbox from cached cards, then refreshes on open or pull-to-refresh.
3. Filters to cards whose `extras` match the inbox (for example, `feed_type` equals `inbox`).
4. Logs impressions, clicks, and dismissals for the custom UI. On React Native, use these SDK methods:
   - `getCachedContentCards`
   - `requestContentCardsRefresh`
   - `logContentCardImpression`
   - `logContentCardClicked`
   - `logContentCardDismissed`
   - `processContentCardClickAction`
   - Prefer `getCachedContentCards` over the deprecated `getContentCards` method.
5. Optionally dismisses a card when the consumer completes the related action (for example, opens `doc_id` in documents). Do this in addition to a dismiss tap in the inbox.

### Step 5: Test the three delivery modes

- **Push notification only:** The notification arrives, and no inbox card appears.
- **Content Card only:** The card appears in the inbox, and no push notification is sent.
- **Push notification and Content Card:** Both send together, and the deep links behave as designed. The card remains after the push notification is dismissed. The unread badge, dismissal, and analytics behave as expected.

Test refresh under realistic navigation so rate limits do not block inbox updates during testing.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/channels/content_cards/create_a_content_card"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Create a Content Card</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Content Cards in Canvas</span></span></div></a></li><li><a href="/docs/user_guide/messaging/campaigns/creating_campaign"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Create a multichannel campaign</span></span></div></a></li><li><a href="/docs/developer_guide/content_cards/content_card_inbox"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Tutorial: Content Card inboxes</span></span></div></a></li><li><a href="/docs/developer_guide/content_cards/creating_cards"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Creating custom Content Cards</span></span></div></a></li><li><a href="/docs/developer_guide/content_cards/customizing_cards/feed"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Customizing the Content Card feed</span></span></div></a></li><li><a href="/docs/developer_guide/content_cards/logging_analytics"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Logging Content Card analytics</span></span></div></a></li><li><a href="/docs/user_guide/channels/push/create_a_push_message"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Create a push message</span></span></div></a></li></ul>
