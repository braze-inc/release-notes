# May 28, 2026 release

## Data & Reporting

### Push Performance dashboard

The [Push Performance dashboard](https://www.braze.com/docs/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) gives you a single, channel-level view of push engagement, including sends, bounces, deliveries, and direct, influenced, and total open rates over a configurable time window. Use it to understand the overall health of your push channel without rolling up data from individual campaigns or Canvases.

### Geolocation fields in catalog selections



Catalogs now support distance-based filtering with the new geolocation field type and Catalog Selection operators. This helps you create more relevant location-aware experiences, such as showing each user their nearest restaurant, filtering open properties within 50 km for a real estate campaign, or targeting stores near a specific event. Instead of approximating geographic targeting with city or region codes, you can filter catalog items by proximity to a center point, including a Liquid user attribute such as a user's most recent location. For more information, see [Selections](https://www.braze.com/docs/user_guide/data/activation/catalogs/selections#how-it-works).

### Banner and RCS for Report Builder

[Report Builder](https://www.braze.com/docs/report_builder/) supports Banner as a channel and RCS as a sub-category under SMS, so you can measure performance for both directly in your custom reports alongside every other Braze channel.

### `ecommerce.cart_updated` event actions

The [`ecommerce.cart_updated` event](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples) supports `add` and `remove` actions alongside `replace`, allowing you to send incremental cart changes instead of a full cart snapshot on every update. 

## BrazeAI<sup>TM</sup>

### Content Optimizer for SMS, MMS, and RCS messages



You can use [Content Optimizer](https://www.braze.com/docs/user_guide/brazeai/content_optimizer) to optimize hooks, bodies, and CTAs for SMS, MMS, and RCS messages. Content Optimizer is an agent that helps you test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically.

## Orchestration

### Workspace time zones



Use [workspace time zones](https://www.braze.com/docs/user_guide/administer/global/admin_settings/workspace_time_zone) to define specific time zones for individual workspaces. This makes scheduled campaigns and Canvases (that don’t use local time or Intelligent Timing) send according to the workspace's designated time zone, rather than the overarching company time zone.

Workspace time zones for message sending are rolling out gradually, so you may not see these settings in your dashboard yet.

## Channels & Touchpoints

### WhatsApp `inbound_profile_name`

You can automatically capture a user's WhatsApp display name from Meta's inbound messaging webhook and write it to the user's Braze profile. When an inbound WhatsApp message is received, Braze exposes the profile name as a new WhatsApp Liquid attribute, [`{{whats_app.${inbound_profile_name}}}`](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/), which you can reference in a Canvas User Update step to save to a profile field.

### Orphaned SMS subscription states

Braze [automatically manages orphaned subscription state records](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#how-braze-handles-orphaned-subscription-states) (subscription data stored for a phone number or email address not tied to any user profile) to prevent unintended subscription state inheritance. This protects users from scenarios where a newly created user profile incorrectly inherits subscription state from a previously deleted or unrelated user.

## Partnerships

### Chord - Customer Data Platform

[Chord](https://www.chord.co/) provides a customer data platform that captures and standardizes events from your eCommerce storefront. When you connect Chord to Braze, purchase activity, behavioral events, and identity updates flow into Braze so you can trigger campaigns and keep profiles current without building those pipelines yourself.

For more information, see [Chord](https://www.braze.com/docs/partners/chord/).

### Better Email - Templates

[Better Email](https://www.betteremail.dev) is a collaborative email creation platform built around an Email Design System. Teams can design, manage, and export production-ready emails from a shared system of blocks and styles, ensuring brand consistency at scale without relying on developers or agencies.

For more information, see [Better Email](https://www.braze.com/docs/partners/better_email/).

### DailyPlay - Dynamic Content

[DailyPlay](https://dailyplay.ai/) is a gamification platform. Use it to launch personalized, branded games and built-in reward systems that deepen engagement and improve retention.

For more information, see [DailyPlay](https://www.braze.com/docs/partners/dailyplay/).

## SDK

### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- [Flutter SDK 19.0.0](https://pub.dev/packages/braze_plugin/changelog#1900)
    - The minimum supported Dart version is `2.17.0`.
    - SDK logging is now controlled on the Dart layer.
    - Updates the native SDK bindings, including the native Android bridge from [Braze Android SDK 41.1.1 to 42.2.0](https://github.com/braze-inc/braze-android-sdk/compare/v41.1.1...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Fixes a crash.
- [Cordova 16.0.1](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/16.0.1)
    - Fixes iOS initialization when using `cordova-ios` 8 with the `SwiftDelegate` template.
- [Unity SDK 11.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Updates the native SDK bindings, including the native iOS bridge from Braze [Swift SDK 13.2.0 to 14.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updates the native Android bridge from [Braze Android SDK 36.0.0 to 42.2.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v42.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The minimum required Android SDK version is 23. For more information, see [Braze Android SDK version information](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
    - Updated the minimum required Unity version to Unity 6 ([6000.0.66f2](https://unity.com/releases/editor/whats-new/6000.0.66f2) or later).
    - Removed News Feed.
        - Removed `RequestFeedRefresh()`, `RequestFeedRefreshFromCache()`, `LogFeedDisplayed()`, `LogCardImpression(string)`, `LogCardClicked(string)`.
    - Fixes minor bugs.
- [React Native 20.1.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/20.1.0)
    - Updates the Android SDK bindings.
    - Fixes a push notification deep linking issue.
- [Segment Swift 8.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#800)
    - Updates the Braze Swift SDK bindings to require releases from the `14.0.0+` SemVer denomination.
        - This allows compatibility with any version of the Braze SDK from `14.0.0` up to, but not including, `15.0.0`.
        - Refer to the [changelog entry for `14.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1400) for more information on potential breaking changes.
    - Adds support for SDK Authentication.