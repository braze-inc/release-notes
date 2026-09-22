# September 17, 2026 release

## Data & Reporting

### Push Performance dashboards: Push Analytics Hub



The [Push Performance dashboards](https://www.braze.com/docs/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) provide a channel-wide view of performance, insights, and deliverability across campaigns and Canvases. Compare key rates with industry benchmarks, rank campaigns, and analyze engagement trends. Frequency and cadence reports roll out by the end of September.

### Cloud Data Ingestion visual mapper



The [Cloud Data Ingestion visual mapper](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/visual_mapper) lets you create User Attributes syncs by mapping columns from existing warehouse tables or views to Braze fields. This no-code option supports Snowflake, Redshift, BigQuery, Databricks, and Fabric; use the [SQL editor](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sql_editor) for advanced transformations.

### eCommerce recommended events (basic and nested properties) 



Filter eCommerce recommended events by their [event properties](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/ecommerce_events#property-filters), both basic (for example, order total) and nested (for example, `products[0].metadata.category`), in triggers, action paths, conversion events, exit criteria, and more.

### Usage alerts



[Usage alerts](https://www.braze.com/docs/user_guide/administer/global/billing/usage_alerts) notify dashboard users when Action Credit consumption crosses 50%, 75%, 90%, or 100% of your allotment for the current credits period. The Credits Usage **Overview** tab also shows a banner at 90% or higher usage.

## BrazeAI<sup>TM</sup>

### Braze MCP server



The remote-hosted [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server) connects AI agents to Braze analytics and content workflows through OAuth, with no local package, configuration file, or API key. Access is limited by the signed-in user's permissions and OAuth scopes, and includes beta support for the Campaigns and Segments API and [Operator Connect](https://www.braze.com/docs/user_guide/brazeai/mcp_server/operator_connect).

### Operator can create and edit drag-and-drop designs



[Operator](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities) can create complete drag-and-drop designs or edit individual blocks from natural-language prompts while preserving Liquid and personalization. This is available across message editors, templates, Content Blocks, landing pages, Banners, and the email preference center.

### Knowledge sources



[Knowledge sources](https://www.braze.com/docs/user_guide/brazeai/agents/knowledge_sources) give Canvas Step Agents and Catalog Agents focused catalog context, improving data retrieval compared with referencing an entire catalog in agent instructions.

### Content Optimizer step updates



The [Content Optimizer](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step) now optimizes email preheaders, sender names, and images. It also supports up to four email components (625 combinations) or three SMS/MMS/RCS components (125 combinations) per step.

## Orchestration

### Custom Canvas alerts



[Custom Canvas alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/custom_canvas_alerts) support percentage thresholds based on the previous seven days. Combine percentage and volume rules with AND or OR logic to identify unexpected changes in Canvas entries or sends.

## Channels & Touchpoints

### Connected Content debugger



The [Connected Content debugger](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) shows live request and response details in **Preview & Test**, helping you verify endpoints, headers, payloads, and Liquid before launch. It's available across Banners, Canvas Context steps, and messaging channels.

### Multi-language support for webhooks



[Multi-language messaging for webhooks](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) lets you localize payload values from one campaign, Canvas step, or template using translation tags. This replaces complex Liquid logic and separate webhooks for each language.

### SCIM Provisioning for IdP Groups



[SCIM provisioning](https://www.braze.com/docs/user_guide/administer/global/user_management/automated_user_provisioning#accessing-scim-provisioning-settings) can sync groups from Okta and Microsoft Entra ID to Braze custom roles, keeping dashboard access aligned with identity provider group membership.

### Shopify segments



Manage [Shopify segment syncs](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_segments_sync) from the Shopify integration page, including one-time syncs, status tracking, and pause or resume controls.

### Shopify SMS double opt-in



Use [SMS double opt-in](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_overview#sms-double-opt-in) to send a branded confirmation text through Braze instead of Shopify's confirmation email.

### Banners in Shopify standard integrations



Enable [Banners for Shopify standard integrations](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_standard_integration#step-6-activate-channels-optional) from your integration settings without additional development.

### Manage Subscriptions block



The [**Manage Subscriptions** block](https://www.braze.com/docs/user_guide/messaging/landing_pages/manage_subscriptions) on landing pages now supports email, SMS, and WhatsApp subscription groups.

### Liquid tags for subscription group unsubscribes and WhatsApp username



Use the `{% subscription_group_unsubscribe_url <subscription_group_id> %}` [Liquid tag](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) for one-click email subscription group unsubscribes without changing global subscription state. You can also use `{{whats_app.${inbound_username}}}` to retrieve a contact's username from [inbound WhatsApp messages](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/messaging_users).

### WhatsApp carousel messages—API sending



Send WhatsApp carousel messages through the Braze API using the [carousel card object](https://www.braze.com/docs/api/objects_filters/messaging/whats_app_object#carousel-card-object).

### Multiple link shortening domains



Add [multiple link shortening domains](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains#assigning-custom-domains-to-subscription-groups) for SMS, MMS, and RCS so your messages don't depend on one shared domain.

## Partnerships

### Globalization Partners International (GPI) - Message Personalization - Localization

[Globalization Partners International](https://www.braze.com/docs/partners/gpi) (GPI) connects Braze content with human and AI-powered translation services across more than 200 languages, then returns completed translations through the Translation API.

### GrowSurf - Message Personalization - Referrals

[GrowSurf](https://www.braze.com/docs/partners/growsurf) sends referral and affiliate program data to Braze as custom attributes for segmentation and Liquid personalization.

## SDK

The following SDK updates have been released. For more details, see [SDK Changelogs](https://www.braze.com/docs/developer_guide/changelogs).

### SDK breaking updates

The following major SDK releases include breaking changes:

- [Cordova SDK 17.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1700) updates the native Android and Swift bridges. On iOS, Content Card extras are now JavaScript objects instead of JSON-encoded strings.
- [Xamarin SDK 10.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md) updates the native bindings and Kotlin dependencies. It also deprecates compatibility-layer symbols and introduces non-blocking initialization and identifier access.
- [Segment Swift SDK 10.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md) requires Braze Swift SDK 18.x.
- [React Native SDK 23.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/23.0.0) updates the native Android and Swift bindings, including non-blocking Swift calls and a geofence registration fix.

### Summary of recent SDK features and fixes

- [Vega SDK 0.5.0](https://github.com/braze-inc/braze-vega-sdk) supports the latest Vega OS and React Native 0.83.
- [Android SDK 43.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4311) fixes issues with Banners, `unregisterPush`, DUST, and stability.
- [Swift SDK 18.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1820) adds public protocols for Braze modules and deprecates `BrazeKitCompat` and `BrazeUICompat` symbols.
- [Swift SDK 18.2.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1821) fixes HTML in-app message closing, custom attribute syncing, and early data requests.
- [React Native SDK 23.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/23.0.0) updates native bindings and adds logout methods.
- [Web SDK 6.11.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#6110) adds `registerPush()` and fixes logout storage and duplicate in-app message events.
- [Web SDK 6.12.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#6120) adds optional Shopify eCommerce event metadata and treats null optional fields as absent.
- [Web SDK 6.12.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#6121) fixes handling for in-app messages containing disallowed `javascript:` or `data:` URIs.
- [Web SDK 6.13.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#6130) adds beta support for a conversational chat widget.
- [Segment Swift SDK 10.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md) updates the Braze Swift SDK bindings.
- [Xamarin SDK 10.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md), [Cordova SDK 17.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1700), and [Flutter SDK 22.1.0](https://github.com/braze-inc/braze-flutter-sdk/blob/master/CHANGELOG.md) update native Swift and Android bindings; Flutter also adds logout methods.

