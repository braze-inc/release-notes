# October 15, 2026 release

## Data & Reporting

### Industry Benchmarks dashboard



The [Industry Benchmarks dashboard](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder/industry_benchmarks_dashboard) compares your email, push, Content Card, and SMS performance against aggregated benchmarks from your industry, region, and sub-industry.

### Teams support for Catalogs



You can assign a catalog to a Team. Admins can grant the View Catalogs, Edit Catalogs, Export Catalogs, and Delete Catalogs [Team-level permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/teams#available-team-level-permissions). Users with these permissions see and manage only their Team's catalogs, so admins don't need to grant workspace-wide catalog access.

## BrazeAI<sup>TM</sup>

### BrazeAI Decisioning Studio™ Go



[BrazeAI Decisioning Studio™ Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go) is an AI decisioning agent for recurring email programs. Instead of picking one winning subject line, send time, or image for the whole audience, the agent selects the best combination for each recipient based on their past engagement, with a random control group so you can measure lift.

### Content Optimizer



[Content Optimizer](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step) is a Canvas step that tests high volumes of content variants for email, push notifications, SMS, MMS, and RCS, and automatically optimizes toward better-performing combinations.

### Agentic Standards



[Agentic Standards](https://www.braze.com/docs/user_guide/brazeai/agents/agentic_standards) let you define Campaign Standards and Canvas Standards. These are rules and rulesets for brand guidelines, organizational conventions, and technical requirements—then run an agentic evaluation before launch. Operator can help draft rules as you configure a standard, so you can reduce manual oversight and check that campaigns and Canvases are ready to launch.

## Orchestration

### Message Prioritization



[Message Prioritization](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization) is an optional layer on top of frequency capping. When multiple opted-in campaigns or Canvas Message steps compete for the same user, categories and ranked rules decide which message sends—not which was scheduled first. Braze can hold back a lower-priority send to preserve cap space for a higher-priority one, and retry windows let deprioritized messages compete again later.

## Data & Reporting

### Messaging Observability



[Messaging Observability](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder/messaging_observability) now traces events across a Canvas or campaign so you can audit entries, suppressions, failures, and sends in one place. For Canvases, progression events show how users move through the journey separately from send outcomes.

## Channels & Touchpoints

### Intelligent IP warming



[Automated IP warming](https://www.braze.com/docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming) now supports Intelligent ranking alongside manual segment ranking. Upload a CSV of recent email opens and clicks from your previous provider, and Braze scores matching users by predicted engagement so the warm-up ramp sends to the most engaged users first.

### Email NPS Survey block



Add a 0–10 [NPS Survey](https://www.braze.com/docs/user_guide/channels/email/drag_and_drop/nps_survey) block to drag-and-drop emails. Recipients select a score in their inbox and land on a Braze survey landing page.

### Apex proxying for new custom domains



New [custom domains](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains) for link shortening use A and AAAA records that point directly to the Braze link infrastructure, instead of a CNAME to a shared domain. Existing custom domains keep working as they are.

### IP-based bot click filtering



[SMS and RCS bot click filtering](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering) checks the IP address and user agent of each click. Clicks from known automated link scanners are flagged as suspected bot clicks and excluded from reported click metrics.

### Web Targeting for Banners



[Web Targeting for Banners](https://www.braze.com/docs/user_guide/channels/banners/web_targeting) lets you place a Banner on your website from the dashboard using a CSS selector and insertion method, without a code change for each placement. After a one-time Web SDK auto-insertion setup, you can update targeting entirely from Braze.

### Real-time updates for Content Cards



Content Cards now reach a user's device as soon as they happen during a session, with no manual refresh required. [Real-time delivery](https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed#real-time-delivery) covers campaign eligibility, Canvas step entry, card removals, and API-triggered sends. The SDK keeps a live connection open for the session, so Braze pushes updates to the device instead of waiting for the next session or refresh. Real-time delivery requires Swift SDK 18.0.0 or later, Android SDK 43.1.1 or later, or Web SDK 6.12.0 or later.

### Shopify historical backfill updates



During [Shopify historical backfill](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) setup, choose how much history to bring into Braze at setup, instead of the fixed 90 days of orders and one year of customers. For Orders, you can choose 90 days, 1 year, or 2 years; for customers, you can choose the past year, 2 years, or all time.

## Partnerships

### Google DV360 – Canvas Audience Sync



Using [Audience Sync to Google DV360](https://www.braze.com/docs/partners/canvas_audience_sync/dv360_audience_sync), you can sync Braze audiences to Google Display & Video 360 to target, trigger, and suppress ads across DV360 inventory such as YouTube, connected TV, and the open web.

### Bidease - Message Orchestration - Retargeting

[Bidease](https://www.braze.com/docs/partners/message_orchestration/retargeting/bidease) is a mobile demand-side platform (DSP) for app user acquisition and retargeting. The Braze and Bidease integration lets you use your Braze segments as audiences in Bidease campaigns, so you can re-engage lapsed users, reach high-value users, or exclude existing users from acquisition campaigns, with audiences kept in sync with your segments automatically.

## SDK

The following SDK updates have been released. For more details, see [SDK Changelogs](https://www.braze.com/docs/developer_guide/changelogs).

### SDK breaking updates

The following major SDK releases include breaking changes:

- [Swift SDK 19.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1900) raises the minimum supported versions to iOS 15.0 and tvOS 15.0, and removes `BrazeInAppMessageUI.DisplayChoice.later` in favor of `BrazeInAppMessageUI.DisplayChoice.reenqueue`. It also changes `requestBannersRefresh` to merge into the existing Banner cache instead of replacing it.
- [Android SDK 44.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4400) changes `requestBannersRefresh` to merge into the existing Banner cache instead of replacing it, and adds a size limit for the Banner content cache.
- [Web SDK 7.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#700) changes `braze.requestBannersRefresh()` to update only the placements it requests, and `braze.getAllBanners()` no longer returns expired Banners. Refresh callbacks are now called at most once per call.
- [Flutter SDK 23.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/master/CHANGELOG.md) raises the minimum supported versions to Flutter 3.44.0 and Dart 3.12.0, and migrates the Android build to Android Gradle Plugin 9.2.1.

### Summary of recent SDK features and fixes

- [Swift SDK 19.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1900) adds `subscribeToEvents(_:)` and `eventsStream` for Content Cards, Banners, and Feature Flags, and deprecates `subscribeToUpdates(_:)`. Banner refreshes now merge into the existing cache.
- [Android SDK 43.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4320) fixes crashes when calling `wipeData()`, `disableSdk()`, or `logout()` during SDK initialization, and fixes the Content Cards feed rendering under the system bars.
- [Android SDK 44.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4400) adds `subscribeToContentCardsEvents`, `subscribeToBannersEvents`, and `subscribeToFeatureFlagsEvents`, and deprecates the matching `subscribeTo*Updates` methods. Banner refreshes now merge into the existing cache.
- [Web SDK 7.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#700) adds `braze.subscribeToContentCardsEvents()`, `braze.subscribeToBannersEvents()`, and `braze.subscribeToFeatureFlagsEvents()`, and deprecates the matching `subscribeTo*Updates()` methods. Banner refreshes now update only the placements they request.
- [Flutter SDK 23.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/master/CHANGELOG.md) fixes an Android issue where `getCachedContentCards()` never completed when the native cache was null. The method now returns an empty list.
- [React Native SDK 23.1.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/23.1.0) adds `Braze.logout()` and `Braze.unregisterPush()` to support logout use cases.
