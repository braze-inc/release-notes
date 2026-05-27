# April 30, 2026 release

## Data & Reporting

### Quick User Add for individual profile creation



You can now create an individual user profile from **Import Users** by selecting **Quick User Add** and entering an email or external ID.

Previously, creating users from this workflow required CSV upload or an automated ingestion method.

For more information, see [CSV import](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users/csv_import/).

### Zero-copy CDI syncs for Canvas triggers



CDI now supports the `Canvas triggers` data type for zero-copy personalization. You can trigger Canvases from warehouse or S3 data and pass context fields without persisting those fields on Braze user profiles.

Previously, CDI syncs required data to be written to Braze profiles for this type of personalization workflow.

For more information, see [Zero-copy personalization using CDI](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/zero_copy_sync/).

### eCommerce recommended events



[eCommerce recommended events](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/) cover six steps in the purchase journey: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled`, and `order_refunded`. When you successfully send these events, Braze validates the data and makes it available to a growing set of platform features.

## Currents and Datashare

### New Banner and WhatsApp Currents updates



Currents and Datashare now include a new `Banner.Dismiss` event and additional fields for existing WhatsApp events.

Previously, these Banner dismissal events and WhatsApp fields were not available in export data.

For more information, see [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

## Orchestration

### Multi-language translations



Compose [multi-language messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) with quick, one-time locale setup that doesn’t require complex code and enables you send to all of your markets with confidence.

### Granular permissions migration



Managing who can access your account and perform specific actions is critical for both security and operational efficiency. To give you more control, Braze is introducing [granular permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/granular_permissions_migration/), a more flexible and precise way to manage user access across your account.

### Send to Destination Canvas component



The [Send to Destination step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/send_to_destination) allows you to send users from one Canvas to another. For example, if you have two Canvases that share messaging for promotional offers, you can use Send to Destination to connect these Canvases.

### Canvas Context enhancements



In Canvas, you can now reference context variables to set:

- A removal event for Content Cards
- The expiration of Content Cards

For more details, see [Card creation](https://www.braze.com/docs/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas).

### Delivery validation advancement behavior for Message steps



[Delivery validations](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step/#delivery-validations) provide an additional check to confirm your audience meets the delivery criteria at message send. If a user doesn’t meet the set delivery validations for a Message step, you can use the **Delivery validations advancement behavior** setting to determine if the user should advance to the next step or exit the Canvas.

### Workspace messaging rate limits



Use [workspace messaging rate limits](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/messaging_rate_limits) to regulate the delivery rate of your outgoing messages from your platform to make sure your users are receiving the messages they need to. Workspace messaging rate limits are rolling out gradually, so you may not see these settings in your dashboard yet.

## Channels & Touchpoints

### WhatsApp Template Builder



The [WhatsApp Template Builder](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/) lets you create and submit WhatsApp message templates directly in Braze—no need to switch between Braze and the Meta Business Manager. After Meta approves your template, use it in as many campaigns and Canvases as you’d like.

### Shopify product tags, metafields, and collections



You can now [sync Shopify product tags, collections, and metafields](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_catalogs/) from your Shopify store into your Braze catalog. This provides richer product data for personalization, segmentation, and catalog-based messaging without custom workarounds.

## Partnerships

### GRAVTY - Data and Analytics - Loyalty



[GRAVTY®](https://www.lji.io/) is an enterprise-grade loyalty platform from Loyalty Juggernaut Inc. (LJI) that enables brands across retail, travel, restaurants (including quick-service restaurants), and financial services to design, manage, and scale next-generation programs—driving measurable growth in engagement, retention, and customer lifetime value through personalized, data-led experiences.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
## SDK

The following SDK updates have been released. For more details, see [SDK changelogs](https://www.braze.com/docs/releases/sdk_changelogs/).

### SDK breaking updates



The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [React Native SDK 19.2.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.2.0)
    - Delayed initialization support.
- [Android SDK 42.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.0.0)
    - Bug fixes for In-app messages and Banners.
- [Swift SDK 14.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.1.0)
    - Banner dismissals support.
- [Web SDK 6.7.0](https://github.com/braze-inc/braze-web-sdk/releases/tag/v6.7.0)
    - Banner dismissals support.
- [Android SDK 42.1.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.1.0)
    - Banner dismissals support.
- [Braze Segment Android 17.0.0](https://github.com/braze-inc/braze-segment-android/releases/tag/v17.0.0)
    - This is the final release of the Braze Segment Android plugin because it uses Analytics-Android, which reached end-of-support in March 2026. Migrate to the [Braze Segment Kotlin plugin](https://github.com/braze-inc/braze-segment-kotlin), which uses [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin).
    - Upgrades native SDK versions.
