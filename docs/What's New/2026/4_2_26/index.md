# April 2, 2026 release

## Data & Reporting

### New Banner channel fields in Currents and Datashare events

Braze added fields for existing Banner channel events in Currents and Datashare exports. For a list of these event and field updates, see [Changes in Version 7](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage).

### Mixpanel EU and India data center support for Currents

The Currents Mixpanel integration now supports Mixpanel's EU and India data centers. When you configure a Mixpanel integration, you can choose which Mixpanel region Braze sends your data to. This update supports Mixpanel's growing international footprint for mutual customers. For more information, see [Mixpanel](https://www.braze.com/docs/partners/data_and_analytics/analytics/mixpanel).

### Reusable Cloud Data Ingestion (CDI) sources and syncs



Cloud Data Ingestion (CDI) has a new design that separates sources and syncs, so you can reuse one source across multiple syncs. Existing syncs migrate automatically to the new sources and syncs model with no downtime. Go to **Cloud Data Ingestion** > **Sources** to view, edit, or create sources, then select a source from the dropdown when creating a sync. This change reduces repetitive setup, and creates a foundation for future enhancements. For more information, see [Setting up data warehouse integrations](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).

## BrazeAI<sup>TM</sup>

### File support tickets from BrazeAI Operator<sup>TM</sup>



[BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator/) now includes a flow to file Braze support tickets without leaving the dashboard. For steps, auto-included context, and tips for faster resolution, see [File support tickets with BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator/support_tickets/).

## Orchestration

### Multi-language translations



After adding locales to your workspace, use [multi-language translations](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) to target users in different languages all within a single push, email, Banner, in-app message, or Content Block.

![Locale previews](https://www.braze.com/docs/assets/img/multi-language_support/multi_language_user_preview.png?f55b1a40baaba6ede110adbbda7cbf8e){: style="max-width:70%;"}

### Canvas Context enhancements



In Canvas, you can now reference context variables to set:

- An [expiration](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#set-an-expiration) for Banners and in-app messages in a Message step
- A [personalized delays](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#action-path-delays) for Action Paths steps

In the Context variable name field, you can also enter the context variable name or select it from the dropdown in the step editor. For more details, see [Context](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/context) and [Context variables](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/context_variables).

## Channels & Touchpoints

### KakaoTalk



[KakaoTalk](https://www.braze.com/docs/kakaotalk) is a messaging channel that enables broadcast messaging and 1:1 chat with users. Create a personalized user experience by using Liquid and other dynamic content to build an environment that fosters and enhances a rich user experience with your brand.

![A KakaoTalk list item message.](https://www.braze.com/docs/assets/img/kakaotalk/wide_image.png?cc34a0abe27faa0167d07982b3019022){: style="max-width:70%;"}

### Banners in Canvas



You can use [Banners](https://www.braze.com/docs/user_guide/message_building_by_channel/banners/) as a messaging channel in Canvas [Message steps](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/message_step). Banners allow you to personalize app or website content dynamically, reflecting real-time user eligibility and behavior.

## Partnerships

### CataBoom - Message Personalization - Visual and Interactive Content

[CataBoom](https://www.braze.com/docs/partners/cataboom) is a gamification platform. Brands use it to build and launch interactive digital experiences, including spin-to-win games, quizzes, and instant-win games. Those experiences deepen engagement and collect first-party data.

### Denada - Message Orchestration - Templates

[Denada](https://www.braze.com/docs/partners/denada) is an AI-powered marketing creative platform that lets subject matter experts create on-brand marketing materials through natural conversation. With Denada, teams can go from ideation to finished email content without needing design expertise.

### Poq - eCommerce - Mobile app platform

[Poq](https://www.braze.com/docs/partners/poq) enables enterprise businesses to rapidly launch, manage, and scale fully native iOS and Android apps—delivering high-performance mobile experiences that drive commerce and bring your brand promise to life.

### The Trade Desk – Canvas Audience Sync

Using the [Braze Audience Sync to The Trade Desk](https://www.braze.com/docs/partners/canvas_audience_sync/trade_desk_audience_sync/), you can dynamically sync your first-party user data from Braze directly into The Trade Desk for ad retargeting, lookalike modeling, and suppression.

## SDK

### Connect your Integrated Development Environment (IDE) to the Docs MCP

Use AI coding assistants to accelerate your Braze integration workflow by connecting your Integrated Development Environment (IDE) to the Braze Docs MCP through Context7. This gives your assistant direct access to current Braze documentation, so it can generate more accurate SDK guidance, code examples, and troubleshooting help in your development environment. For setup steps in Cursor, Claude Desktop, and VS Code, see [Building with an LLM](https://www.braze.com/docs/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp).

### SDK breaking updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Cordova 15.0.0](https://github.com/braze-inc/braze-cordova-sdk/releases/tag/15.0.0)
    - Updated the native Android bridge [from Braze Android SDK 39.0.0 to 41.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v41.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native iOS bridge [from Braze Swift SDK 13.2.0 to 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Fixes an issue with `subscribeToInAppMessage` involving the success callback.
- [Roku SDK 2.2.1](https://github.com/braze-inc/braze-roku-sdk/releases/tag/v2.2.1)
    - Fixes a crash when processing a failed HTTP request for templated in-app messages while the device has intermittent or no connectivity.
- [Web SDK 6.6.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#660)
    - Adds the `cookieExpiryInDays` initialization option to configure cookie duration from the default of 400 days.
- [Flutter SDK 18.0.0](https://pub.dev/packages/braze_plugin/changelog#1800)
    - Adds delayed initialization support.
    - Streamlines the iOS integration process to not require writing native code to forward Content Cards, Banners, feature flags, in-app messages, or push notification updates from the native SDK.
        - The SDK will now automatically set up these subscriptions when the Braze instance is created.
        - This matches the existing behavior on Android.
        - To migrate, remove any manual calls to `braze.contentCards.subscribeToUpdates()`, `braze.banners.subscribeToUpdates()`, `braze.notifications.subscribeToUpdates`, `braze.featureFlags.subscribeToUpdates` and `braze.inAppMessagePresenter` in the `AppDelegate`.
        - By default, in-app messages will be presented. To override this, set a custom in-app message presenter using the `postInitialization` closure in `BrazePlugin.configure(_:postInitialization:)`.
- [Swift SDK 14.0.4](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1404)
    - Fixes a bug with push automation on SDK re-initialization.
    - Fixes an issue where invalid images in push stories were not filtered out.
- [Swift SDK 14.0.3](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1403)