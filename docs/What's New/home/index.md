# What's new in Braze

## September 17, 2026

### Braze MCP server

**Area:** BrazeAI™
**Status:** General availability

The remote-hosted [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server) connects AI agents to Braze analytics and content workflows through OAuth, with no local package, configuration file, or API key. Access is limited by the signed-in user's permissions and OAuth scopes, and includes beta support for the Campaigns and Segments API and [Operator Connect](https://www.braze.com/docs/user_guide/brazeai/mcp_server/operator_connect).

### Content Optimizer step updates

**Area:** BrazeAI™
**Status:** Beta

The [Content Optimizer](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step) now optimizes email preheaders, sender names, and images. It also supports up to four email components (625 combinations) or three SMS/MMS/RCS components (125 combinations) per step.

### Knowledge sources

**Area:** BrazeAI™
**Status:** General availability

[Knowledge sources](https://www.braze.com/docs/user_guide/brazeai/agents/knowledge_sources) give Canvas Step Agents and Catalog Agents focused catalog context, improving data retrieval compared with referencing an entire catalog in agent instructions.

### Operator can create and edit drag-and-drop designs

**Area:** BrazeAI™
**Status:** General availability

[Operator](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities) can create complete drag-and-drop designs or edit individual blocks from natural-language prompts while preserving Liquid and personalization. This is available across message editors, templates, Content Blocks, landing pages, Banners, and the email preference center.

### Banners in Shopify standard integrations

**Area:** Channels & Touchpoints
**Status:** Early access

Enable [Banners for Shopify standard integrations](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_standard_integration#step-6-activate-channels-optional) from your integration settings without additional development.

### Connected Content debugger

**Area:** Channels & Touchpoints
**Status:** General availability

The [Connected Content debugger](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) shows live request and response details in **Preview & Test**, helping you verify endpoints, headers, payloads, and Liquid before launch. It's available across Banners, Canvas Context steps, and messaging channels.

### Liquid tags for subscription group unsubscribes and WhatsApp username

**Area:** Channels & Touchpoints
**Status:** General availability

Use the `` [Liquid tag](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) for one-click email subscription group unsubscribes without changing global subscription state. You can also use `{{whats_app.${inbound_username}}}` to retrieve a contact's username from [inbound WhatsApp messages](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/messaging_users).

### Manage Subscriptions block

**Area:** Channels & Touchpoints
**Status:** General availability

The [**Manage Subscriptions** block](https://www.braze.com/docs/user_guide/messaging/landing_pages/manage_subscriptions) on landing pages now supports email, SMS, and WhatsApp subscription groups.

### Multi-language support for webhooks

**Area:** Channels & Touchpoints
**Status:** General availability

[Multi-language messaging for webhooks](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) lets you localize payload values from one campaign, Canvas step, or template using translation tags. This replaces complex Liquid logic and separate webhooks for each language.

### Multiple link shortening domains

**Area:** Channels & Touchpoints
**Status:** General availability

Add [multiple link shortening domains](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains#assigning-custom-domains-to-subscription-groups) for SMS, MMS, and RCS so your messages don't depend on one shared domain.

### SCIM Provisioning for Okta and Microsoft Entra ID

**Area:** Channels & Touchpoints
**Status:** Early access

[SCIM provisioning](https://www.braze.com/docs/user_guide/administer/global/user_management/automated_user_provisioning#accessing-scim-provisioning-settings) can sync groups from Okta and Microsoft Entra ID to Braze custom roles, keeping dashboard access aligned with identity provider group membership.

### Shopify SMS double opt-in

**Area:** Channels & Touchpoints
**Status:** General availability

Use [SMS double opt-in](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_overview#sms-double-opt-in) to send a branded confirmation text through Braze instead of Shopify's confirmation email.

### Shopify segments

**Area:** Channels & Touchpoints
**Status:** Beta

Manage [Shopify segment syncs](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_segments_sync) from the Shopify integration page, including one-time syncs, status tracking, and pause or resume controls.

### WhatsApp carousel messages—API sending

**Area:** Channels & Touchpoints
**Status:** General availability

Send WhatsApp carousel messages through the Braze API using the [carousel card object](https://www.braze.com/docs/api/objects_filters/messaging/whats_app_object#carousel-card-object).

### Cloud Data Ingestion visual mapper

**Area:** Data & Reporting
**Status:** Early access

The [Cloud Data Ingestion visual mapper](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/visual_mapper) lets you create User Attributes syncs by mapping columns from existing warehouse tables or views to Braze fields. This no-code option supports Snowflake, Redshift, BigQuery, Databricks, and Fabric; use the [SQL editor](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sql_editor) for advanced transformations.

### Push Performance dashboards: Push Analytics Hub

**Area:** Data & Reporting
**Status:** General availability

The [Push Performance dashboards](https://www.braze.com/docs/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) provide a channel-wide view of performance, insights, and deliverability across campaigns and Canvases. Compare key rates with industry benchmarks, rank campaigns, and analyze engagement trends. Frequency and cadence reports roll out by the end of September.

### Usage alerts

**Area:** Data & Reporting
**Status:** Early access

[Usage alerts](https://www.braze.com/docs/user_guide/administer/global/billing/usage_alerts) notify dashboard users when Action Credit consumption crosses 50%, 75%, 90%, or 100% of your allotment for the current credits period. The Credits Usage **Overview** tab also shows a banner at 90% or higher usage.

### eCommerce recommended events (basic and nested properties)

**Area:** Data & Reporting
**Status:** General availability

Filter eCommerce recommended events by their [event properties](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/ecommerce_events#property-filters), both basic (for example, order total) and nested (for example, `products[0].metadata.category`), in triggers, action paths, conversion events, exit criteria, and more.

### Custom Canvas alerts

**Area:** Orchestration
**Status:** Early access

[Custom Canvas alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/custom_canvas_alerts) support percentage thresholds based on the previous seven days. Combine percentage and volume rules with AND or OR logic to identify unexpected changes in Canvas entries or sends.

### Globalization Partners International (GPI) - Message Personalization - Localization

**Area:** Partners

[Globalization Partners International](https://www.braze.com/docs/partners/gpi) (GPI) connects Braze content with human and AI-powered translation services across more than 200 languages, then returns completed translations through the Translation API.

### GrowSurf - Message Personalization - Referrals

**Area:** Partners

[GrowSurf](https://www.braze.com/docs/partners/growsurf) sends referral and affiliate program data to Braze as custom attributes for segmentation and Liquid personalization.

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The following major SDK releases include breaking changes:

- [Cordova SDK 17.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1700) updates the native Android and Swift bridges. On iOS, Content Card extras are now JavaScript objects instead of JSON-encoded strings.
- [Xamarin SDK 10.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md) updates the native bindings and Kotlin dependencies. It also deprecates compatibility-layer symbols and introduces non-blocking initialization and identifier access.
- [Segment Swift SDK 10.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md) requires Braze Swift SDK 18.x.
- [React Native SDK 23.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/23.0.0) updates the native Android and Swift bindings, including non-blocking Swift calls and a geofence registration fix.

### Summary of recent SDK features and fixes

**Area:** SDK

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

## August 20, 2026

### Content Optimizer step updates

**Area:** BrazeAI™
**Status:** Beta

The [Content Optimizer](https://www.braze.com/docs/user_guide/brazeai/content_optimizer) step includes the following updates:

- **Step states:** Content Optimizer steps show whether they're in **Learning**, **Optimizing**, or **Action Recommended**, so you can see where each step stands.
- **Pre-launch setup checks:** Content Optimizer checks for key misconfigurations while you draft, so you can catch issues before you launch.
- **Track which combination each user received:** A new Liquid tag and user profile visibility let you track which variant combination each user received, end to end.
- **New Currents data:** Three new event types let you pull Content Optimizer data into your warehouse: `users.canvas.costep.Send`, `users.canvas.costep.Conversion`, and `contentoptimizer.ComponentStore`.

For setup details, see [Content Optimizer step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

### Operator can act on more dashboard pages

**Area:** BrazeAI™
**Status:** General availability

[Operator](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities) can complete work from additional dashboard pages when you describe the outcome in natural language. Examples include building reports and dashboards, working from email template and Content Block list pages, importing or managing users, creating predictions, and updating more admin and settings surfaces.

For example, on the Report Builder page, ask Operator to build a report that shows workspace SMS engagement over the last 30 days.

For representative coverage, see [What you can do with Operator](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities). Ask Operator on the page you're on for the most current answer.

### Operator can create and edit Canvases

**Area:** BrazeAI™
**Status:** General availability

[Operator](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities) can create a draft Canvas from a natural-language description, and edit an existing Canvas the same way. Describe the journey you want—entry criteria, delays, and messages—and Operator assembles a draft you review and refine before you launch it.

For example, ask Operator to build an abandoned cart journey that waits one hour after cart abandonment, sends an email reminder, then a push after 24 hours if the user still hasn't purchased.

For supported steps and limitations, see [What you can do with Operator](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities).

### Operator can navigate the dashboard for you

**Area:** BrazeAI™
**Status:** General availability

[Operator](https://www.braze.com/docs/user_guide/brazeai/operator#navigate-the-dashboard) can navigate to a different dashboard page to complete your request. When a prompt needs a different part of the dashboard, Operator identifies the destination, proposes the navigation, and takes you there before continuing its work.

This lets Operator chain multi-step work from a single prompt. For example, if you ask Operator from the home page to set up your drag-and-drop editor settings to match your brand guidelines, it navigates you to the relevant email settings and continues helping you from there.

By default, Operator asks you to approve a proposed navigation before it moves you to a new page. To let Operator navigate without waiting for your approval each time, turn on [Auto-approve actions](https://www.braze.com/docs/user_guide/brazeai/operator/reviewing_actions#auto-approve-actions).

### Connected Content debugger

**Area:** Channels & Touchpoints
**Status:** Early access

The [Connected Content debugger](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) shows the live request and response for each Connected Content call in **Preview & Test**, so you can verify your endpoint, headers, and Liquid tags before you launch a campaign or Canvas. Open **View details** to inspect the URL, method, status code, request and response headers, payload, duration, and whether the response was served from cache.

During early access, the debugger is available for Content Cards, email, in-app messages, push, SMS/MMS/RCS, webhooks, and WhatsApp.

### Custom form blocks and JavaScript bridge for landing pages

**Area:** Channels & Touchpoints
**Status:** General availability

Landing pages now support [custom form blocks](https://www.braze.com/docs/user_guide/messaging/landing_pages/custom_form_blocks) and a [JavaScript bridge](https://www.braze.com/docs/user_guide/messaging/landing_pages/javascript_bridge), so you can capture custom form input and sync client-side events and attributes through your landing page experience.

### In-app message and landing page surveys

**Area:** Channels & Touchpoints
**Status:** General availability

Braze surveys collect feedback in [in-app messages](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys/) and [landing pages](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys/) that you can analyze and use in follow-up messaging.

### KakaoTalk carousel message

**Area:** Channels & Touchpoints
**Status:** General availability

A [KakaoTalk carousel message](https://www.braze.com/docs/user_guide/channels/kakaotalk/create_kakaotalk_message#step-2-compose-your-kakaotalk-message) includes up to six scrollable cards. Each card has an image, header, message, optional Website URL, and at least one button.

### Manage Subscriptions block for landing pages

**Area:** Channels & Touchpoints
**Status:** General availability

The [Manage Subscriptions](https://www.braze.com/docs/user_guide/messaging/landing_pages/manage_subscriptions) block lets users view, opt in to, and update email subscription groups on a landing page.

### Multi-step landing page forms

**Area:** Channels & Touchpoints
**Status:** General availability

[Multi-step landing page forms](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) let you split a long form across multiple steps in a single **Form** row, with a built-in confirmation step after submission.

### WhatsApp Template Builder improvements

**Area:** Channels & Touchpoints
**Status:** General availability

[WhatsApp Template Builder](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/) supports more creation paths and template options:

- **Create templates while building campaigns and Canvases:** Create a new WhatsApp template directly in the composer instead of only selecting existing templates from Content.
- **Carousel response messages:** Build carousel layouts as response messages, not only as outbound templates.
- **New template types: Utility and Flow:** Template Builder supports Utility templates and Flow templates, including when you create templates from campaigns, Canvases, or the standalone Content Templates experience.

### Cloud Data Ingestion SQL editor

**Area:** Data & Reporting
**Status:** General availability

The [SQL editor](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sql_editor) lets you create and edit Cloud Data Ingestion (CDI) syncs by writing a SQL query against any table or view in your data warehouse, rather than building and maintaining a dedicated Braze-specific table. It's available for all sync data types across all CDI data warehouse sources: Snowflake, Redshift, BigQuery, Databricks, and Fabric.

### Cloud Data Ingestion for Google Cloud Storage and Azure Blob Storage

**Area:** Data & Reporting
**Status:** General availability

Cloud Data Ingestion (CDI) supports two new file storage sources: Google Cloud Storage, generally available now, and Azure Blob Storage, coming the week of August 31, 2026. Both sources work like the existing Amazon S3 source—Braze ingests files as soon as they're written to the bucket or container—so customers on Google Cloud or Azure get the same speed and reliability without replicating files into S3 or building a custom integration.

### Cloud Data Ingestion to BrazeAI Decisioning Studio

**Area:** Data & Reporting
**Status:** Early access

Cloud Data Ingestion (CDI) can now sync data warehouse data directly to BrazeAI Decisioning Studio for customers using both products, so you can bring in data beyond your Braze workspace for reinforcement learning and AI decisioning without building custom ETL jobs. This early access release supports Snowflake sources, with additional data warehouse sources coming soon.

### Cloud Data Ingestion visual mapper

**Area:** Data & Reporting
**Status:** Beta

The [visual mapper](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/visual_mapper) lets you create a Cloud Data Ingestion (CDI) sync by mapping an existing data warehouse table's columns to Braze fields directly in the dashboard, with no SQL or dedicated table required. This beta release supports User Attributes syncs across all CDI data warehouse sources. The visual mapper and the SQL editor are complementary: use the visual mapper for direct column-to-field mapping, and the SQL editor for advanced cases like transformations, joins, and conditional logic.

### Automatic Team assignment

**Area:** Orchestration
**Status:** General availability

For users with Team-level permissions only, Braze can assign a [Teams](https://www.braze.com/docs/user_guide/administer/global/user_management/teams#automatic-team-assignment) automatically during object creation.

### Custom Canvas alerts

**Area:** Orchestration
**Status:** Early access

[Custom Canvas alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/custom_canvas_alerts) notify you when user entries or messages sent fall outside the volume you expect. Set a threshold, choose how often Braze checks it (every 3 to 12 hours, or every 24 hours), and get notified by email, webhook, or both when a rule is met. You can create multiple alerts for the same Canvas, including on drafts—the alert starts checking after the Canvas launches.

### Workspace quiet hours

**Area:** Orchestration
**Status:** Early access

[Workspace quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) let you set a default quiet hours window for a messaging channel across your entire workspace. Every campaign and Canvas on that channel respects the window in each recipient's local time zone. You can keep the workspace default, or opt out and apply a campaign or Canvas-specific window instead.

Messages that would send during the window are held for later delivery or aborted, depending on the campaign type. Workspace quiet hours never modify message content.

### Amazon Bedrock - AI Model Provider

**Area:** Partners

[Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed AWS service that provides access to foundation models from leading AI companies through a unified API, so brands can build and scale generative AI applications on AWS.

For more information, see [Amazon Bedrock](https://www.braze.com/docs/partners/amazon_bedrock).

### Audience Sync: Google Data Manager API

**Area:** Partners
**Status:** Early access

[Audience Sync to Google](https://www.braze.com/docs/partners/canvas_audience_sync/google_audience_sync) supports Google Data Manager API in early access.

### Bynder - Message Orchestration - CMS and DAM

**Area:** Partners

[Bynder](https://www.bynder.com) is a digital asset management (DAM) platform that helps customers create, manage, find, and distribute approved digital assets (images, videos, and other creative) from a single source of truth. When integrated with Braze, Bynder's Universal Compact View (UCV) Google Chrome extension lets marketers search for and select Bynder assets without leaving the Braze dashboard. Insert links to those assets directly into campaigns and Canvases.

For more information, see [Bynder](https://www.braze.com/docs/partners/bynder).

### Multiplied Media - Message Personalization - Visual and Interactive Content

**Area:** Partners

[Multiplied Media](https://multiplied.media) is a creative and automation studio that uses your CRM data to create personalized images, GIFs, and video—a unique asset for each customer. The Multiplied Media and Braze integration lets you send this media through email, push notifications, in-app messages, Content Cards, and WhatsApp.

For more information, see [Multiplied Media](https://www.braze.com/docs/partners/multiplied_media).

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Unity SDK 12.0.0
    - Updated the native iOS bridge [from Braze Swift SDK 14.1.0 to 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/14.1.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native Android bridge [from Braze Android SDK 42.2.0 to 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.2.0...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Flutter SDK 22.0.0
    - Updates the native Android bridge [from Braze Android SDK 42.3.1 to 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.3.1...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updates the native iOS bridge [from Braze Swift SDK 17.0.0 to 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/17.0.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Swift SDK 18.0.0-18.1.0
    - Renames `Braze.Ecommerce.ProductViewedEvent.typeIdentifiers` to `type` on Swift and Objective-C API surfaces.
    Renames Live Activities push-to-start update events on `Braze.LiveActivities.UpdateEvent.ActivityType`, which are emitted when using Braze.`LiveActivities.subscribeToStateUpdates(_:)`:
        - `pushToStartOptedOut` to `pushToStartUnregistered`
        - `pushToStartOptOutFlushed` to `pushToStartUnregisterFlushed`

### Summary of recent SDK features and fixes

**Area:** SDK

- **Swift SDK v18.1.0:** Adds push token logout methods, in addition to the existing push logout method, to support additional logout use cases. Also updates the eCommerce event type.
- **Flutter SDK v22.0.0:** Updates the native bridge to inherit functionality from the Android and Swift SDKs.
- **Unity SDK v12.0.0:** Updates the native bridge to inherit functionality from the Android and Swift SDKs.

For more details, see the [SDK Changelogs](https://www.braze.com/docs/developer_guide/changelogs).

## July 23, 2026

### Operator can now update Settings pages for you

**Area:** BrazeAI™
**Status:** General availability

[Operator](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities) can now make changes directly on more Settings pages, so you can describe a change in natural language instead of clicking through configuration screens. Supported pages include:

- Quiet hours
- Push settings
- Messaging rate limits
- Messaging rules and always-on approval workflows
- Other identifiers and API limits
- Contact information

For example, on the Quiet hours page, ask Operator to set quiet hours from 9 PM to 8 AM for SMS.

### Remote Braze MCP server

**Area:** BrazeAI™
**Status:** Early access

The [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server) is a remote-hosted connection that lets you connect AI agents such as Claude, ChatGPT, Cursor, VSCode, Codex, Google Antigravity, and Claude Code directly to Braze. Through natural language, agents can read campaign, Canvas, and segment analytics, custom attributes, events, KPIs, and catalogs, and create or update email templates, Content Blocks, and media library assets. No user-profile PII is exposed.

To connect, paste a single endpoint URL into your MCP client—`https://mcp.braze.com/mcp` for US or `https://mcp.braze.eu/mcp` for EU—then sign in with OAuth, including SSO. The server launches with the available tools.

### Grid view for the media library

**Area:** Channels & Touchpoints
**Status:** General availability

The media library and select template libraries now offer a grid view alongside the existing list view. Grid view displays assets as thumbnails with key metadata (name, type, last modified), making it faster to find images and creative by sight instead of by filename. Filtering and search work the same in both views.

### HTML editor for Banners

**Area:** Channels & Touchpoints
**Status:** General availability

When you compose a Banner, you can now build it [using the HTML editor](https://www.braze.com/docs/user_guide/channels/banners/create_a_banner#compose-a-banner). The HTML editor is best for teams that already maintain their own HTML templates or want full control over markup and styling for Banners. You can write or paste custom HTML directly into the editor.

### Push credentials update API

**Area:** Channels & Touchpoints
**Status:** General availability

You can now update push credentials programmatically with the [Update push credentials endpoint](https://www.braze.com/docs/api/endpoints/apps/post_update_push_credential). Each request updates one app and one platform (`apple`, `firebase`, `huawei`, or `kindle`) and accepts credential payloads as Base64-encoded values. This helps teams manage large app portfolios and credential rotation policies without relying on manual dashboard uploads.

### Replace a file in the media library

**Area:** Channels & Touchpoints
**Status:** General availability

You can now [replace the file of an existing media library asset](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library#replace-a-file) while keeping its URL and asset ID stable. Because the URL doesn't change, any campaign, Canvas, Content Block, or template that references that asset automatically reflects the updated file, so you don't have to manually re-upload or re-link it everywhere it's used.

### Shareable Preview support for more channels

**Area:** Channels & Touchpoints
**Status:** General availability

[Shareable Preview](https://www.braze.com/docs/user_guide/channels/email/html_editor#step-3b-preview-and-test-your-message) now supports the following additional channels:

- SMS, MMS, and RCS
- WhatsApp
- Push
- Content Cards
- LINE

From a campaign or message, generate a link and share it with reviewers who don't have Braze dashboard access—brand, legal, or an outside agency, for example. Recipients open the link in any browser to see the message rendered as a customer would, including any test personalization.

### Shopify self-serve SDK version upgrade

**Area:** Channels & Touchpoints
**Status:** General availability

New [Shopify](https://www.braze.com/docs/partners/ecommerce/shopify/) customers are provisioned on the latest Braze Web SDK and JavaScript SDK versions during setup. Existing customers can view their current SDK version in integration settings, get notified when a newer version is available, and self-serve upgrades from integration settings.

### Survey rating scale for in-app messages and landing pages

**Area:** Channels & Touchpoints
**Status:** Early access

Add a numeric rating scale to a form block in both [landing page surveys](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) and [in-app message surveys](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) to capture sentiment, satisfaction, and likelihood-to-recommend without any custom code. Three ranges are supported: 1–10, 1–5, and 0–10 (the standard NPS range).

### WhatsApp limited time offer templates

**Area:** Channels & Touchpoints
**Status:** General availability

[WhatsApp limited time offer templates](https://www.braze.com/docs/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates) display a time-sensitive promotional offer with an optional countdown as the offer nears expiration. Use this layout for time-boxed promotions, such as seasonal sales or offers personalized to a user attribute.

### CSV Custom Events mapper

**Area:** Data & Reporting
**Status:** General availability

The [CSV import flow](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users/csv_import#about-csv-import) for custom events now includes a mapper that lets you map event names and event property headers to Braze fields before import. This update brings the custom events experience in line with the custom attributes flow and reduces the need to reformat files before upload. The flow includes uploading a CSV, mapping required fields and events, mapping event properties, and then selecting targeting preferences before import. If your file already matches the expected format, you can continue through the flow without making mapping changes.

### Catalogs free storage now supports up to 500 MB

**Area:** Data & Reporting
**Status:** General availability

The free version of [catalogs](https://www.braze.com/docs/user_guide/data/activation/catalogs/create#tiers) now supports up to 500 MB of storage across all CSV files.

### Messaging Observability

**Area:** Data & Reporting
**Status:** General availability

[Messaging Observability](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder/messaging_observability) provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected. Contact your customer success manager for access to the feature.

### Teams audience scoping

**Area:** Orchestration
**Status:** General availability

The [Teams](https://www.braze.com/docs/user_guide/administer/global/user_management/teams/) audience configuration now supports multiple filters.

### Refiner - Surveys

**Area:** Partners

[Refiner](https://refiner.io) is an in-app survey platform for SaaS and mobile apps. It enables product and voice-of-customer teams to launch targeted in-app surveys and continuously collect NPS, CSAT, CES, product feedback, and zero-party user data.

### Stayfilm - Visual and Interactive Content

**Area:** Partners

[Stayfilm](https://www.stayfilm.com/) is a REST API for automated, personalized video production at scale. The platform integrates data, images, text, soundtracks, narration, and visual effects to generate customized video content for eCommerce, marketplaces, CRM workflows, and marketing campaigns.

### Validity - Data and Analytics

**Area:** Partners

[Validity Everest](https://www.validity.com/everest/) is an email deliverability platform that helps you measure inbox placement and protect your sending reputation. The Braze and Validity integration syncs your Everest seed list to Braze, automatically seeds qualifying campaigns and Canvases, and pulls engagement metrics back into Validity Inbox so you can compare seed-based placement with real subscriber engagement.

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- [Android SDK 43.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v43.0.0)
    - Adds `unregisterPush` and logout methods.
    - Adds additional fields to eCommerce events.
    - Adds exponential backoff for push notification image loading.
- [Swift SDK 17.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Adds additional fields to eCommerce events.
    - Makes data states predictable after initialization.
    - Adds non-blocking accessors for device and user identifiers.
    - Removes the deprecated push-to-start update API on `Braze.LiveActivities`.
- [Web SDK 6.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Adds `unregisterPush` and logout methods.
    - Adds additional fields to eCommerce events.
    - Fixes a Banner and Content Card issue related to redundant refreshes on startup.
    - Adds a public method for Banner dismissal.
- [Flutter SDK 21.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/v21.0.0)
    - Updates the native iOS bridge.
    - Removes deprecated methods.
    - Updates `changeUser`, `enableSDK`, and `disableSDK` handlers to return completion results.
- [Expo SDK 5.2.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/v5.2.0)
    - Updates the sample app to Expo SDK 56.
- [React Native SDK 22.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/22.0.0)
    - Adds support for Banner dismissals.
    - Includes binding updates.

## June 25, 2026

### Agent Console enhancements

**Area:** BrazeAI™

You can do the following in the [Agent Console](https://www.braze.com/docs/user_guide/brazeai/agents/):

- Configure pre-set use cases with Operator through the **Create agent** button dropdown.
- Duplicate existing agents from the agent list.
- Save agents as drafts during creation and complete configurations later.
- Set fallback output values for Canvas agents to prevent output variables from setting to null if the agent errors out.
- Set required input fields for a Catalog agentic field, so that the agent doesn't run if a required input field value is empty or missing.
- Re-run an agent for all empty cells of an agentic column to fill any missing values without re-running the entire column.

### Agent Console templates built with Operator

**Area:** BrazeAI™

When building an agent in **Agent Console**, you can choose to create a custom agent or select an option in **Create an agent with Operator** to use BrazeAI Operator to apply a starting template. Operator can pre-configure instructions, output fields, and context for the following Agent Console starting templates.

For more details, see [Create custom agents](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents/#agent-templates-built-with-operator).

### Edit a launched Content Optimizer step

**Area:** BrazeAI™
**Status:** Beta

After your Canvas is launched, you can now [update a Content Optimizer step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step/#edit-a-launched-step) to:

- Add new variants to any existing component, either manually or using AI-generated suggestions, up to the five-variant limit per component.
- Deactivate variants to stop sending them to users.
- Re-activate previously deactivated variants, as long as doing so keeps the component at or below the five-variant limit.

### Operator support for Content Blocks

**Area:** BrazeAI™

[Operator](https://www.braze.com/docs/user_guide/brazeai/operator/) can now create and edit [Content Blocks](https://www.braze.com/docs/user_guide/messaging/design_and_edit/content_blocks/)—the reusable snippets you build once and reference across multiple messages—directly from a natural-language prompt. From the **Content Blocks** page, ask Operator to create a new Content Block from scratch or edit an existing one, and Operator generates or updates the content for you to review.

### Operator support for campaign creation and editing

**Area:** BrazeAI™

[Operator](https://www.braze.com/docs/user_guide/brazeai/operator/) can now create and edit entire campaigns, not just compose messages. From a single natural-language prompt or campaign brief, Operator builds a ready-to-review campaign end to end—composing the message, scheduling delivery, targeting an audience, and assigning conversion events—then recaps what it built in the review step. Previously, Operator could compose the message (one of the five campaign creation steps); it now has visibility and control over the remaining Schedule, Target, Assign, and Review steps.

This functionality is available from the **Campaigns** page or from within any existing campaign. As a result, Operator can:

- Respond to prompts such as "I want to send our lapsed users a push notification with a 20% off promo code the next time they open the app or log a custom event that cancels their subscription".
- Assist you in each individual step of the campaign wizard, with full visibility into what you're working on and the ability to change form inputs on the page.
- Navigate to the correct step in the wizard to begin taking action, whether you start from an open campaign or the **Campaigns** page.

### Unified BrazeAI assistants in Operator

**Area:** BrazeAI™

The standalone BrazeAI assistants found throughout the dashboard are unified into [BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator/), establishing Operator as the single AI assistant for marketer-facing generative AI assistance across the dashboard. The following assistants now route through Operator:

- AI Liquid Agent
- AI Copywriter
- AI HTML Email Template agent
- AI Image generator
- Content QA with AI
- AI Copilot for Data Transformations


The existing entry points remain where each legacy assistant button used to live. Instead of opening a standalone assistant, these entry points now open the Operator pane with dynamic prompts that are pre-scoped to your task. These entry points provide a direct route into Operator so you can use these capabilities without adjusting your existing workflows.

### Custom click tracking for Banners

**Area:** Channels & Touchpoints
**Status:** General availability

For more granular click tracking for Banners, you can [assign a custom identifier](https://www.braze.com/docs/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional) to each interactive element using the **Identifier for Reporting** field in its properties panel.

### Optimize with BrazeAI™

**Area:** Channels & Touchpoints
**Status:** Early access

**Optimize with BrazeAI™** automatically turns on when you add multiple push variants, applies recommended experiment defaults, and optimizes toward the highest-performing variant. You can turn it off if you need to send immediately. For more information, see [Optimizing A/B tests with BrazeAI](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection).

### Quick Push A/B Testing

**Area:** Channels & Touchpoints
**Status:** General availability

Quick Push A/B Testing now supports multi-platform push campaigns and Canvas steps through variant groups, so you can test aligned iOS and Android message variations in one workflow. For more information, refer to [Multiple platform push messages](https://www.braze.com/docs/user_guide/channels/push/create_a_push_message/multiple_platform_push/#use-cases).

### Re-eligibility for Banners

**Area:** Channels & Touchpoints

When re-eligibility is enabled for Banner campaigns, users who dismiss a Banner can become eligible again after a configurable cooldown window that starts at dismissal. If re-eligibility isn't turned on, dismissed users remain ineligible. To configure re-eligibility, see [Configure re-eligibility](https://www.braze.com/docs/user_guide/channels/banners/create_a_banner/#re-eligibility). Note that Canvas Banner steps use Canvas re-entry settings instead.

### User dismissals for Banners

**Area:** Channels & Touchpoints
**Status:** General availability

You can allow users to manually dismiss a Banner by selecting **Banner can be dismissed** when configuring dismissal behavior. This option is beneficial in scenarios where you want to promote a limited-time sale for all app users, but allow them to dismiss the message if they aren't interested.

See [Configure dismissal behavior](https://www.braze.com/docs/user_guide/channels/banners/create_a_banner/#dismiss-behavior) for details on enabling dismissal and customizing the dismiss button.

### WhatsApp test send results

**Area:** Channels & Touchpoints

After sending a test WhatsApp message, you can view a [detailed delivery report](https://www.braze.com/docs/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-4-view-test-send-results) directly in the message composer. This helps you confirm your message reached the intended recipient and troubleshoot failures before launch.

### Data point exclusions

**Area:** Data & Reporting
**Status:** General availability

[eCommerce recommended events](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/ecommerce_events/) no longer count toward billable data points. You can adopt Braze eCommerce events (`ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`) without data point consumption.

### Deliverability Center surfaces Microsoft SNDS data for Amazon SES customers

**Area:** Data & Reporting

For workspaces that send email through Amazon SES, the [Deliverability Center](https://www.braze.com/docs/deliverability_center/) displays Microsoft SNDS metrics for your dedicated sending IPs. Braze backfills up to 90 days of historical SNDS data when this feature is turned on for your workspace.

### Event History tab

**Area:** Data & Reporting
**Status:** General availability

The **Event History** tab on [user profiles](https://www.braze.com/docs/user_guide/audience/manage_audience/user_profiles/) lists the user's custom events and purchases from the past 30 days (up to 100 most recent). Use it to confirm an SDK or API integration is sending events as expected, debug why a user did (or didn't) enter an event-triggered campaign or Canvas, or investigate a support escalation about a specific user.

### Metric name update for Content Cards and Banners

**Area:** Data & Reporting

The _Unique Recipients_ metric has been renamed to _Unique Daily Impressions_ for Content Cards and Banners. _Unique Daily Impressions_ refer to the number received from Braze and is based on the `user_id`. Unique daily impressions are counted at the campaign or Canvas step level. For more details, refer to the [Metrics glossary](https://www.braze.com/docs/user_guide/analytics/metrics_glossary).

### User deletion

**Area:** Data & Reporting
**Status:** General availability

[User deletion](https://www.braze.com/docs/user_guide/audience/manage_audience/user_profiles/delete_users/) lets you manage your database by removing profiles that are no longer needed, created in error, or required to be deleted for compliance (such as GDPR or CCPA).

### Convercus - Data and Analytics - Loyalty

**Area:** Partners

[Convercus](https://www.braze.com/docs/partners/data_and_analytics/loyalty/convercus/) is a SaaS loyalty and coupon platform that helps brands and retailers grow customer frequency, basket value, and repurchase rates through omnichannel loyalty programs and personalized coupon campaigns.

### Copy Pastd - Message Orchestration - Templates

**Area:** Partners

[Copy Pastd](https://www.braze.com/docs/partners/copy_pastd/) Building Blocks is a drag-and-drop email builder that pushes Liquid-powered Content Blocks and full templates directly into your Braze workspace. Design once, sync to Braze, and reuse the same components across campaigns, Canvases, and triggered flows without rebuilding HTML each time.

### Databricks Mosaic - AI Model Providers

**Area:** Partners

[Databricks Mosaic](https://www.braze.com/docs/partners/databricks_mosaic/) is Databricks' unified platform for building, deploying, and managing AI and machine learning models at scale on the Databricks Data Intelligence Platform.

### DinMo - Data and Analytics - Reverse ETL

**Area:** Partners

[DinMo](https://www.braze.com/docs/partners/dinmo/) is a composable customer data platform (CDP) that connects your cloud data warehouse to Braze through reverse Extract, Transform, Load (ETL). Marketing teams can build audience segments from warehouse data, sync user attributes and events into Braze, and keep subscription statuses up to date without CSV uploads or engineering support.

### EmailShepherd - Message Orchestration - Templates

**Area:** Partners

[EmailShepherd](https://www.braze.com/docs/partners/emailshepherd/) is an agentic email creation platform built on your Email Design System that allows your whole marketing team—and AI agents—to produce on-brand, production-ready emails without bottlenecks. The Braze integration publishes approved emails directly to your Braze workspace, so marketers can scale email production in Braze without sacrificing brand consistency.

### Talkable - Message Personalization - Referrals

**Area:** Partners

[Talkable](https://www.braze.com/docs/partners/talkable/) helps consumer brands turn happy customers into a scalable referral channel. With the Braze integration, marketing email opt-ins captured in Talkable referral campaigns flow into Braze in real time, giving your team the consent, context, and campaign data you need to welcome, segment, and engage every new advocate and friend.

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- [Swift SDK 14.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Android SDK 42.3.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.3.0)
    - `BannerView`: `BannerDismissSnapshot` fields passed to `onDismissCallback` are now non-null. If the SDK cannot resolve `placementId`, `stableKey`, or `trackingId`, the callback is skipped and a warning is logged.
- [Web SDK 6.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Adds support for new eCommerce event methods.
- [Swift SDK 14.2.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1421)
- [Swift SDK 15.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Banners: `onDismiss` now receives `Braze/BannerDismissalEvent` instead of `Braze/Banner`.
    - Raises the Xcode version to 26.0 (17A324).
    - Raises the minimum Mac Catalyst deployment target from iOS 13 (macOS 10.15 Catalina) to iOS 16 (macOS 13 Ventura).
        - Mac Catalyst users on macOS 12 Monterey or earlier are no longer supported.
    - Removes the ability to control whether the SDK prevents showing in-app messages to different users in certain edge cases.
        - Removes the option to configure through `Braze.Configuration.preventInAppMessageDisplayForDifferentUser`.
        - The SDK will now always behave as if this configuration option were set to true.
    - Updates the `Braze.WebViewBridge.ScriptMessageHandler` and `Braze.WebViewBridge.SchemeHandler` init to have non-optional `channel` parameter.
- [Android SDK 42.3.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4231)
    - Adds support for new eCommerce event methods.
    - Adds Banner dismissal methods for custom UI implementations.
    - Includes HTML in-app message bug fixes.
- [Swift SDK 15.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1501)
- [React Native 21.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/21.0.0)
    - Updates native Swift and Android SDK version bindings.
    - Updates the native Swift SDK version bindings [from Braze Swift SDK 14.0.4 to 15.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/14.0.4...15.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Corrects Content Cards JSDoc.
        - Raises the Xcode version to 26.0 (17A324).
- [Swift SDK 15.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Adds support for new eCommerce event methods.
    - Adds Banner dismissal methods for custom UI implementations.
    - Adds example implementations for building custom UI with Banners.
    - Adds pass-through Live Activities observability, allowing errors and update events to be tracked with more precision and granularity.
    - Adds async callback-based getters for Content Cards and deprecates older getters.
    - Improves state management stability.
- [Segment Swift 9.0.0](https://github.com/braze-inc/braze-segment-swift/releases/tag/9.0.0)
    - Updates the Braze Swift SDK bindings to require releases from the `15.0.0+` SemVer denomination.
        - This allows compatibility with any version of the Braze SDK from `15.0.0` up to, but not including, `16.0.0`.
        - Raises the Xcode version to 26.0 (17A324).
        - Refer to the changelog entry for [`15.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1500) for more information on potential breaking changes.
- [React Native 21.1.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/21.1.0)
- [Swift SDK 15.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

## May 28, 2026

### Content Optimizer for SMS, MMS, and RCS messages

**Area:** BrazeAI™
**Status:** Beta

You can use [Content Optimizer](https://www.braze.com/docs/user_guide/brazeai/content_optimizer) to optimize hooks, bodies, and CTAs for SMS, MMS, and RCS messages. Content Optimizer helps you test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically.

### Orphaned SMS subscription states

**Area:** Channels & Touchpoints

Braze [automatically manages orphaned subscription state records](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#how-braze-handles-orphaned-subscription-states) (subscription data stored for a phone number or email address not tied to any user profile) to prevent unintended subscription state inheritance. This protects users from scenarios where a newly created user profile incorrectly inherits subscription state from a previously deleted or unrelated user.

### WhatsApp `inbound_profile_name`

**Area:** Channels & Touchpoints

You can automatically capture a user's WhatsApp display name from Meta's inbound messaging webhook and write it to the user's Braze profile. When an inbound WhatsApp message is received, Braze exposes the profile name as a new WhatsApp Liquid attribute, [`{{whats_app.${inbound_profile_name}}}`](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/), which you can reference in a Canvas User Update step to save to a profile field.

### Banner and RCS for Report Builder

**Area:** Data & Reporting

[Report Builder](https://www.braze.com/docs/report_builder/) supports Banner as a channel and RCS as a sub-category under SMS, so you can measure performance for both directly in your custom reports alongside every other Braze channel.

### Geolocation fields in catalog selections

**Area:** Data & Reporting
**Status:** General availability

Catalogs now support distance-based filtering with the new geolocation field type and Catalog Selection operators. This helps you create more relevant location-aware experiences, such as showing each user their nearest restaurant, filtering open properties within 50 km for a real estate campaign, or targeting stores near a specific event. Instead of approximating geographic targeting with city or region codes, you can filter catalog items by proximity to a center point, including a Liquid user attribute such as a user's most recent location. For more information, see [Selections](https://www.braze.com/docs/user_guide/data/activation/catalogs/selections).

### Push Performance dashboard

**Area:** Data & Reporting

The [Push Performance dashboard](https://www.braze.com/docs/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) gives you a single, channel-level view of push engagement, including sends, bounces, deliveries, and direct, influenced, and total open rates over a configurable time window. Use it to understand the overall health of your push channel without rolling up data from individual campaigns or Canvases.

### `ecommerce.cart_updated` event actions

**Area:** Data & Reporting

The [`ecommerce.cart_updated` event](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples) supports `add` and `remove` actions alongside `replace`, allowing you to send incremental cart changes instead of a full cart snapshot on every update.

### Workspace time zones

**Area:** Orchestration
**Status:** General availability

Use [workspace time zones](https://www.braze.com/docs/user_guide/administer/global/admin_settings/workspace_time_zone) to define specific time zones for individual workspaces. This makes scheduled campaigns and Canvases (that don’t use local time or Intelligent Timing) send according to the workspace's designated time zone, rather than the overarching company time zone.

Workspace time zones for message sending are rolling out gradually, so you may not see these settings in your dashboard yet.

### Better Email - Templates

**Area:** Partners

[Better Email](https://www.betteremail.dev) is a collaborative email creation platform built around an Email Design System. Teams can design, manage, and export production-ready emails from a shared system of blocks and styles, ensuring brand consistency at scale without relying on developers or agencies.

For more information, see [Better Email](https://www.braze.com/docs/partners/better_email/).

### Chord - Customer Data Platform

**Area:** Partners

[Chord](https://www.chord.co/) provides a customer data platform that captures and standardizes events from your eCommerce storefront. When you connect Chord to Braze, purchase activity, behavioral events, and identity updates flow into Braze so you can trigger campaigns and keep profiles current without building those pipelines yourself.

For more information, see [Chord](https://www.braze.com/docs/partners/chord/).

### DailyPlay - Dynamic Content

**Area:** Partners

[DailyPlay](https://dailyplay.ai/) is a gamification platform. Use it to launch personalized, branded games and built-in reward systems that deepen engagement and improve retention.

For more information, see [DailyPlay](https://www.braze.com/docs/partners/dailyplay/).

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

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

## April 30, 2026

### Shopify product tags, metafields, and collections

**Area:** Channels & Touchpoints
**Status:** General availability

You can now [sync Shopify product tags, collections, and metafields](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_catalogs/) from your Shopify store into your Braze catalog. This provides richer product data for personalization, segmentation, and catalog-based messaging without custom workarounds.

### WhatsApp Template Builder

**Area:** Channels & Touchpoints
**Status:** Early access

The [WhatsApp Template Builder](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/) lets you create and submit WhatsApp message templates directly in Braze—no need to switch between Braze and the Meta Business Manager. After Meta approves your template, use it in as many campaigns and Canvases as you’d like.

### New Banner and WhatsApp Currents updates

**Area:** Currents & Datashare
**Status:** General availability

Currents and Datashare now include a new `Banner.Dismiss` event and additional fields for existing WhatsApp events.

Previously, these Banner dismissal events and WhatsApp fields were not available in export data.

For more information, see [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

### Quick User Add for individual profile creation

**Area:** Data & Reporting
**Status:** General availability

You can now create an individual user profile from **Import Users** by selecting **Quick User Add** and entering an email or external ID.

Previously, creating users from this workflow required CSV upload or an automated ingestion method.

For more information, see [CSV import](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users/csv_import/).

### Zero-copy CDI syncs for Canvas triggers

**Area:** Data & Reporting
**Status:** General availability

CDI now supports the `Canvas triggers` data type for zero-copy personalization. You can trigger Canvases from warehouse or S3 data and pass context fields without persisting those fields on Braze user profiles.

Previously, CDI syncs required data to be written to Braze profiles for this type of personalization workflow.

For more information, see [Zero-copy personalization using CDI](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/zero_copy_sync/).

### eCommerce recommended events

**Area:** Data & Reporting
**Status:** General availability

[eCommerce recommended events](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/) cover six steps in the purchase journey: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled`, and `order_refunded`. When you successfully send these events, Braze validates the data and makes it available to a growing set of platform features.

### Canvas Context enhancements

**Area:** Orchestration
**Status:** General availability

In Canvas, you can now reference context variables to set:

- A removal event for Content Cards
- The expiration of Content Cards

For more details, see [Card creation](https://www.braze.com/docs/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas).

### Delivery validation advancement behavior for Message steps

**Area:** Orchestration
**Status:** General availability

[Delivery validations](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step/#delivery-validations) provide an additional check to confirm your audience meets the delivery criteria at message send. If a user doesn’t meet the set delivery validations for a Message step, you can use the **Delivery validations advancement behavior** setting to determine if the user should advance to the next step or exit the Canvas.

### Granular permissions migration

**Area:** Orchestration
**Status:** General availability

Managing who can access your account and perform specific actions is critical for both security and operational efficiency. To give you more control, Braze is introducing [granular permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions), a more flexible and precise way to manage user access across your account.

### Multi-language translations

**Area:** Orchestration
**Status:** General availability

Compose [multi-language messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) with quick, one-time locale setup that doesn't require complex code and enables you to send to all of your markets with confidence.

### Send to Destination Canvas component

**Area:** Orchestration
**Status:** General availability

The [Send to Destination step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/send_to_destination) allows you to send users from one Canvas to another. For example, if you have two Canvases that share messaging for promotional offers, you can use Send to Destination to connect these Canvases.

### Workspace messaging rate limits

**Area:** Orchestration
**Status:** General availability

Use [workspace messaging rate limits](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/messaging_rate_limits) to regulate the delivery rate of your outgoing messages from your platform to make sure your users are receiving the messages they need to. Workspace messaging rate limits are rolling out gradually, so you may not see these settings in your dashboard yet.

### GRAVTY - Data and Analytics - Loyalty

**Area:** Partners
**Status:** General availability

[GRAVTY®](https://www.braze.com/docs/partners/data_and_analytics/loyalty/lji) is an enterprise-grade loyalty platform from Loyalty Juggernaut Inc. (LJI) that enables brands across retail, travel, restaurants (including quick-service restaurants), and financial services to design, manage, and scale next-generation programs—driving measurable growth in engagement, retention, and customer lifetime value through personalized, data-led experiences.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

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

## April 2, 2026

### File support tickets from BrazeAI Operator™

**Area:** BrazeAI™
**Status:** General availability

[BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator/) now includes a flow to file Braze support tickets without leaving the dashboard. For steps, auto-included context, and tips for faster resolution, see [File support tickets with BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator/support_tickets/).

### Banners in Canvas

**Area:** Channels & Touchpoints
**Status:** General availability

You can use [Banners](https://www.braze.com/docs/user_guide/channels/banners) as a messaging channel in Canvas [Message steps](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step). Banners allow you to personalize app or website content dynamically, reflecting real-time user eligibility and behavior.

### KakaoTalk

**Area:** Channels & Touchpoints
**Status:** General availability

[KakaoTalk](https://www.braze.com/docs/kakaotalk) is a messaging channel that enables broadcast messaging and 1:1 chat with users. Create a personalized user experience by using Liquid and other dynamic content to build an environment that fosters and enhances a rich user experience with your brand.

![A KakaoTalk list item message.](https://www.braze.com/docs/assets/img/kakaotalk/wide_image.png){: style="max-width:70%;"}

### Mixpanel EU and India data center support for Currents

**Area:** Data & Reporting

The Currents Mixpanel integration now supports Mixpanel's EU and India data centers. When you configure a Mixpanel integration, you can choose which Mixpanel region Braze sends your data to. This update supports Mixpanel's growing international footprint for mutual customers. For more information, see [Mixpanel](https://www.braze.com/docs/partners/data_and_analytics/analytics/mixpanel).

### New Banner channel fields in Currents and Datashare events

**Area:** Data & Reporting

Braze added fields for existing Banner channel events in Currents and Datashare exports. For a list of these event and field updates, see [Changes in Version 7](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage).

### Reusable Cloud Data Ingestion (CDI) sources and syncs

**Area:** Data & Reporting
**Status:** Early access

Cloud Data Ingestion (CDI) has a new design that separates sources and syncs, so you can reuse one source across multiple syncs. Existing syncs migrate automatically to the new sources and syncs model with no downtime. Go to **Cloud Data Ingestion** > **Sources** to view, edit, or create sources, then select a source from the dropdown when creating a sync. This change reduces repetitive setup, and creates a foundation for future enhancements. For more information, see [Setting up data warehouse integrations](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).

### Canvas Context enhancements

**Area:** Orchestration
**Status:** General availability

In Canvas, you can now reference context variables to set:

- An [expiration](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables#set-an-expiration) for Banners and in-app messages in a Message step
- A [personalized delays](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables#action-paths-delays) for Action Paths steps

In the Context variable name field, you can also enter the context variable name or select it from the dropdown in the step editor. For more details, see [Context](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context) and [Context variables](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

### Multi-language translations

**Area:** Orchestration
**Status:** General availability

After adding locales to your workspace, use [multi-language translations](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) to target users in different languages all within a single push, email, Banner, in-app message, or Content Block.

![Locale previews](https://www.braze.com/docs/assets/img/multi-language_support/multi_language_user_preview.png){: style="max-width:70%;"}

### CataBoom - Message Personalization - Visual and Interactive Content

**Area:** Partners

[CataBoom](https://www.braze.com/docs/partners/cataboom) is a gamification platform. Brands use it to build and launch interactive digital experiences, including spin-to-win games, quizzes, and instant-win games. Those experiences deepen engagement and collect first-party data.

### Denada - Message Orchestration - Templates

**Area:** Partners

[Denada](https://www.braze.com/docs/partners/denada) is an AI-powered marketing creative platform that lets subject matter experts create on-brand marketing materials through natural conversation. With Denada, teams can go from ideation to finished email content without needing design expertise.

### Poq - eCommerce - Mobile app platform

**Area:** Partners

[Poq](https://www.braze.com/docs/partners/poq) enables enterprise businesses to rapidly launch, manage, and scale fully native iOS and Android apps—delivering high-performance mobile experiences that drive commerce and bring your brand promise to life.

### The Trade Desk – Canvas Audience Sync

**Area:** Partners

Using the [Braze Audience Sync to The Trade Desk](https://www.braze.com/docs/partners/canvas_audience_sync/trade_desk_audience_sync/), you can dynamically sync your first-party user data from Braze directly into The Trade Desk for ad retargeting, lookalike modeling, and suppression.

### Connect your Integrated Development Environment (IDE) to the Docs MCP

**Area:** SDK

Use AI coding assistants to accelerate your Braze integration workflow by connecting your Integrated Development Environment (IDE) to the Braze Docs MCP through Context7. This gives your assistant direct access to current Braze documentation, so it can generate more accurate SDK guidance, code examples, and troubleshooting help in your development environment. For setup steps in Cursor, Claude Desktop, and VS Code, see [Building with an LLM](https://www.braze.com/docs/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp).

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

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

## March 5, 2026

### Braze Agents in Agent Console

**Area:** BrazeAI™
**Status:** General availability

[Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents/) are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences. When you create an agent, you define its purpose and set guardrails for how it should behave. After it’s live, the agent can be [deployed](https://www.braze.com/docs/user_guide/brazeai/agents/deploying_agents) in Braze to generate personalized copy, make real-time decisions, or update catalog fields.

### Translate locales in Content Blocks

**Area:** Channels & Touchpoints
**Status:** Early access

After adding locales to your workspace, you can [target users in different languages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) all within a Content Block.

### Additional fields for Currents and Data Share events

**Area:** Data & Reporting
**Status:** General availability

[Currents and Data Share events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) now include the following new fields to deepen the data available for analytics and downstream systems:

- `agentconsole.AgentExecuted`: Added `error` (string)—a description of any error that occurred.
- `agentconsole.ToolInvocation`: Added `request_id` (string)—a unique ID for the overall LLM request and complete execution.
- `users.messages.rcs.InboundReceive`: Added `canvas_variation_name` (string)—the name of the Canvas variation the user received.

### CSV pre-import validation and error reporting

**Area:** Data & Reporting
**Status:** General availability

[CSV user imports](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users/) now support pre-import validation and detailed error reporting. Before importing, select **Validate file before importing** on the **Import Users** page—Braze will scan your file and generate a report identifying rows that will fail entirely (errors) and rows that will succeed with some values skipped (warnings). You can download the report, fix your CSV, and re-upload, or proceed as-is. After the import completes, a downloadable report of any rows that failed is also available, with the exact reason for each issue.

### Campaign and Canvas fields for Snowflake Data Share

**Area:** Data & Reporting
**Status:** General availability

[Snowflake Data Share](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) now includes additional fields reflecting Campaign and Canvas information across 66 existing tables, including:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

### Cloud Data Ingestion sources

**Area:** Data & Reporting
**Status:** Early access

[Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) has a new UI that separates sources from syncs, letting you reuse a single source across any number of syncs. This reduces duplicate configuration and simplifies setup when you have multiple syncs. If you have existing syncs, they're automatically migrated to the new sources-and-syncs structure with no downtime. To get started, go to **Cloud Data Ingestion** > **Sources** to view, edit, or create sources, then select a source from the dropdown when creating a sync.

### Context variables

**Area:** Data & Reporting
**Status:** General availability

[Context variables](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) are temporary pieces of data you can create and use within a user’s journey through a specific Canvas. Each time a user enters the Canvas—even if they have entered it before—the context variables will be redefined based on the latest entry data and Canvas setup. This approach allows each Canvas entry to maintain its own independent context, allowing users to have multiple active states within the same journey while retaining the specific context for each state.

### Messaging Observability

**Area:** Data & Reporting
**Status:** Early access

[Messaging Observability](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder/messaging_observability) provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected.

### New data center

**Area:** Data & Reporting
**Status:** General availability

Braze has launched a new [data center](https://www.braze.com/docs/user_guide/data/infrastructure/data_centers/): JP-01. You can sign up for region-specific data centers when setting up your Braze account.

### Canvas Context step

**Area:** Orchestration
**Status:** General availability

[Canvas Context steps](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context/) let you create and update one or more variables for a user as they move through a Canvas. For example, if you have a Canvas that manages seasonal discounts, you can use a context variable to store a different discount code each time a user enters the Canvas.

### Channel-based rate limiting

**Area:** Orchestration
**Status:** General availability

When setting a delivery speed rate limit for a multi-channel campaign or Canvas, you can choose to set either a shared rate limit or a [channel-based limit](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases). When a multichannel campaign or Canvas uses channel-based rate limiting, the rate limit applies to each of the selected channels. For example, you can set your campaign or Canvas to send a maximum of 5,000 webhooks and 2,500 SMS messages per minute across the campaign or Canvas.

### Granular user permissions

**Area:** Orchestration
**Status:** Early access

Braze is introducing [granular permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/), a more flexible way to manage user access. Refer to [Migrating to granular permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) to learn about the migration process, including how legacy permissions map to granular permissions.

### Algolia - Search Recommendations

**Area:** Partners

[Algolia](https://www.braze.com/docs/partners/ecommerce/product_search_recommendations/algolia) is a search and discovery platform that helps developers build fast, relevant, and scalable search experiences. With a powerful API-first approach, Algolia combines advanced ranking algorithms with AI-driven insights for seamless site search, navigation, and personalized content discovery.

### Anthropic - AI Model Provider

**Area:** Partners

[Anthropic](https://www.braze.com/docs/partners/ai_model_providers/anthropic) is an AI safety and research company developing Claude, a next-generation AI assistant built to be helpful, honest, and safe for a wide range of language tasks.

### Canva - Message Personalization - Creative Studio

**Area:** Partners

[Canva](https://www.braze.com/docs/partners/canva) syncs your images in Canva directly to the Braze Media library, streamlining your creative workflow and keeping your visual assets up to date across all your messaging channels.

### DOTS.ECO - Rewards

**Area:** Partners

[DOTS.ECO](https://www.braze.com/docs/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

### Figma - Message Personalization - Creative Studio

**Area:** Partners

[Figma](https://www.braze.com/docs/partners/figma) is a collaborative design platform that allows you to build, design, and prototype products. Use this integration to send images and visual assets from Figma directly into the Braze media library.

### Flybuy - Message Personalization - Location

**Area:** Partners

[Flybuy](https://www.braze.com/docs/partners/message_personalization/location/flybuy) by Radius Networks is the leading omnichannel location platform leveraging AI-powered technology to optimize speed of service across pickup, delivery, drive-thru, and dine-in. Through its integrated Marketing Suite, Flybuy also enables brands to deliver hyper-targeted, moment-based messages, helping to drive engagement, increase check size, and support broader loyalty initiatives.

### Google Gemini - AI Model Provider

**Area:** Partners

[Google Gemini](https://www.braze.com/docs/partners/ai_model_providers/google_gemini) is Google’s family of AI models that combines advanced reasoning across text, code, and images to help brands deliver smarter, more personalized experiences.

### Limbik - Message Personalization - Personalization Engines

**Area:** Partners

[Limbik](https://www.braze.com/docs/partners/message_personalization/dynamic_content/personalization_engines/limbik) is your AI resonance layer—predicting how real audiences interpret and respond to messages, concepts, and AI outputs before they reach the market. Powered by continuous primary research across 60+ countries and 25+ languages, Limbik delivers human-validated synthetic audiences—digital populations that simulate real audience response at machine speed and with research-grade accuracy (95% confidence, 1.5% to 3% margin of error). Limbik gives you the ability to immediately ensure your messaging resonates with what your target audience believes and feels.

### Linkrunner - Message Orchestration - Attribution

**Area:** Partners

[Linkrunner](https://www.braze.com/docs/partners/message_orchestration/attribution/linkrunner) is a mobile attribution and analytics platform that helps you track and analyze your user acquisition campaigns.

### Mailizio - Message Orchestration - Templates

**Area:** Partners

[Mailizio](https://www.braze.com/docs/partners/message_orchestration/templates/Mailizio) is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio's integration to Braze, you can export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

### Open Loyalty - Data and Analytics - Loyalty

**Area:** Partners

[Open Loyalty](https://www.braze.com/docs/partners/data_and_analytics/loyalty/openloyalty) is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user's loyalty status changes.

### OpenAI - AI Model Provider

**Area:** Partners

[OpenAI](https://www.braze.com/docs/partners/ai_model_providers/openai) creates advanced AI models, like GPT, that enable natural language understanding and generation, empowering brands to build and scale meaningful customer interactions.

### Shopgate - Channels

**Area:** Partners

[Shopgate](https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/shopgate) is a mobile commerce and omnichannel platform that helps merchants create shopping apps and improve the efficiency of brick-and-mortar stores through fulfillment tools and clienteling, meaning personalized in-store customer support based on customer data.

### Splio - Data and Analytics - Cohort Import

**Area:** Partners

[Splio](https://www.braze.com/docs/partners/data_and_analytics/cohort_import/splio) is an audience-building tool that lets you increase the number of campaigns and revenue without harming customer experience, and provides analytics to track the performance of CRM campaigns both online and offline.

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Updated the Android binding from [Braze Android SDK 37.0.0 to 41.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the iOS binding from [Braze Swift SDK 13.3.0 to 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Added new transitive NuGet dependencies required by the Braze Android SDK:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib has been updated from 2.0.21.3 to 2.3.0.1. If your project explicitly pins this package to an older version, you will need to update it to avoid restore errors.
    - Removed the News Feed feature.
        - This feature was removed from the native Android SDK in version [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0).
        - This feature was removed from the native Swift SDK in version [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0).
    - The BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData enum case has been renamed to BRZInAppMessageDismissalReason.WipeData.
- [Expo Plugin 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - This version requires 19.0.0 of the Braze React Native SDK.
    - (Android) Fixed a memory leak in the data persistence layer.
    - (Android) Added support for Braze.getInitialPushPayload() to handle push notification deep links when the app is launched from a terminated state. This resolves an issue where deep links from push notifications were not handled on Android when the app was cold started.
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Updates the native Swift SDK version bindings from Braze Swift SDK 13.3.0 to 14.0.1.
    - Updates the native Android SDK version bindings from Braze Android SDK 40.0.2 to 41.0.0.

## February 5, 2026

### Media Library POST APIs

**Area:** APIs
**Status:** General availability

Media Library assets can now be added via API, enabling customers, partners, and agencies to automate more of their message creation workflows. You can use the [API](https://www.braze.com/docs/api/endpoints/media_library/manage_assets/create) to upload an asset file directly or copy a file from an existing URL. This feature unlocks integration and automation capabilities.

### Content Optimizer

**Area:** BrazeAI™
**Status:** Beta

[Content Optimizer](https://www.braze.com/docs/user_guide/brazeai/content_optimizer) is a continuous, high-variant content testing Canvas step that delivers automated engagement optimization. Using a drag-and-droppable interface similar to the message step, you can define the components you want to test, generate variants using AI (or enter them manually), and use Liquid tags to map these components to your message content.

Built on a non-contextual multi-armed bandit optimizer, Content Optimizer sends a single message per user, determining which combination of component variants to deliver based on predictive recommendations. As the step gathers data over time, high-performing variants naturally increase in send allocation while poor-performing variants decrease. Content Optimizer works best with repeated-send Canvases that have consistent daily user volume (at least a few thousand users per day) to enable continuous optimization.

### Configure width for drag-and-drop Content Blocks

**Area:** Channels & Touchpoints

[Adjust the width of your Content Block](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) by selecting the button in the navigation menu. The default width is 100% when not specified in your email global style settings; otherwise, the global settings will be honored.

![A double-sided arrow with an option to edit the width.](https://www.braze.com/docs/assets/img_archive/content_block_width_updated.png){: style="max-width:30%;" }

### Translate locales in banners

**Area:** Channels & Touchpoints
**Status:** Early access

After adding locales to your workspace, you can [target users in different languages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) all within a single banner.

### Use automated IP warming

**Area:** Channels & Touchpoints
**Status:** Early access

You can use [automated IP warming](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming) to gradually increase your daily send volume, allowing inbox providers to learn and trust your sending patterns. Braze sends to your most engaged subscribers first, which allows daily volume to grow at a pace that matches best practices.

### Add new 'time_ms' field to TokenStateChange event

**Area:** Currents & Datashare
**Status:** General availability

A new `time_ms` field has been added to the [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) event, providing millisecond-level granularity for tracking push token state changes. This enhanced precision helps you understand the latest status of a push token when multiple changes occur within the same second, giving you confidence in downstream systems that you have the correct subscription status. For more information, see the [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

### Agent Console Events for Storage destinations and Datashare

**Area:** Currents & Datashare
**Status:** General availability

Two new [events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) are now available for Storage destinations (AWS S3, GCS, and Azure Blob Storage) and Snowflake Datashare: `agentconsole.AgentExecuted` and `agentconsole.ToolInvocation`. These events enable you to analyze Agent Console usage and details in your downstream systems, helping you understand and get the most out of your agent usage. Agents allow you to create and deploy intelligent agents that can perform specific tasks across Braze, including generating content in canvases or catalogs and routing users down different paths based on intelligent decisioning. For more information, see the [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

### Email Open event — "machine_open" field

**Area:** Currents & Datashare

The [Email Open event](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) now generates the "machine_open" field value so you can report on the [_Machine Open_](https://www.braze.com/docs/user_guide/analytics/metrics_glossary#machine-opens) metric.

### New 'Retry' events for individual channels

**Area:** Currents & Datashare
**Status:** General availability

New [retry events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) are now available for email, LINE, push notifications, SMS, webhooks, and WhatsApp channels. These events provide visibility into when frequency capping results in a scheduled message being delayed rather than aborted. When a message is deprioritized or frequency capped, it can now be retried within a configured retry window, giving you better insight into message delivery patterns and frequency capping impacts. For more information, see the [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

### Send Anonymous user to Tealium Destinations

**Area:** Currents & Datashare
**Status:** General availability

Events that do not have an external user ID defined can now be streamed to [Tealium](https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1) destinations. When you select the "Include events from anonymous users" checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

#### Send Anonymous user to CustomHTTP Destinations



Events that do not have an external user ID defined can now be streamed to CustomHTTP destinations. When you select the "Include events from anonymous users" checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

### eCommerce recommended events

**Area:** Data & Reporting
**Status:** Early access

To match eCommerce recommended events with the existing purchase event, we added the ["Places Order" conversion event](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/conversion_events/), which is similar to "Makes Purchase".

### DOTS.ECO - Extensions

**Area:** Partners

[DOTS.ECO](https://www.braze.com/docs/partners/dots.eco) lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

### Fullstory - Dynamic Content

**Area:** Partners

[Fullstory’s](https://www.braze.com/docs/partners/fullstory/) behavioral data platform helps technology leaders make better, more informed decisions. By injecting digital behavioral data into their analytics stack, Fullstory's patented technology unlocks the power of quality behavioral data at scale–transforming every digital visit into actionable insights.

### LinkedIn – Canvas Audience Sync

**Area:** Partners

Using the [Braze Audience Sync to LinkedIn](https://www.braze.com/docs/partners/canvas_audience_sync/linkedin_audience_sync/), you can add user data from your Braze integration to LinkedIn customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria you’d normally use to trigger a message (such as push, email, SMS, and webhook) in a Braze Canvas based on your user data can now trigger an ad to that user in your LinkedIn customer lists.

### Mailizio - Message orchestration

**Area:** Partners

[Mailizio](https://www.braze.com/docs/partners/mailizio/) is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio's integration to Braze, you can export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

### Open Loyalty - Data & analytics

**Area:** Partners

[Open Loyalty](https://www.braze.com/docs/partners/openloyalty) is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user's loyalty status changes.

### Oracle Crowdtwist - Data & analytics

**Area:** Partners

[Oracle Crowdtwist](https://www.braze.com/docs/partners/crowdtwist) is a leading cloud-native customer loyalty solution to empower brands to offer personalized customer experiences. Their solution offers over 100 default engagement paths, providing rapid time-to-value for marketers to develop a more complete view of the customer.

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Renamed `BrazeConfig.Builder.setIsLocationCollectionEnabled()` to `setIsAutomaticLocationCollectionEnabled()`.
    - Renamed `BrazeConfig.isLocationCollectionEnabled` to `isAutomaticLocationCollectionEnabled`.
    - Renamed `BrazeConfigurationProvider.isLocationCollectionEnabled` to `isAutomaticLocationCollectionEnabled`.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

## January 8, 2026

### Banners in Canvas

**Area:** Channels & Touchpoints
**Status:** Early access

You can select **Banners** as a messaging channel in a [Message step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step/) for Canvas. You can use the drag-and-drop editor to create personalized inline messages, providing non-intrusive, contextually relevant experiences that update automatically at the start of each user session.

### Bring Your Own (BYO) WhatsApp connector

**Area:** Channels & Touchpoints

The [Bring Your Own (BYO) WhatsApp connector](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/byo_connector/) offers a partnership between Braze and Infobip, in which you give Braze access to your Infobip WhatsApp Business Manager (WABA). This allows you to manage and pay for messaging costs directly with Infobip while using Braze for segmentation, personalization, and campaign orchestration.

### Channel-based rate limits

**Area:** Channels & Touchpoints

As an alternative to a rate limit that gets shared across an entire multi-channel campaign or Canvas, you can select a specific rate limit per channel. In this case, the rate limit will apply to each of your selected channels. For example, you can set your campaign or Canvas to send a maximum of 5,000 webhooks and 2,500 SMS messages per minute across the campaign or Canvas. For more details, see [Rate limiting and frequency capping](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping/).

### Dynamic BCC

**Area:** Channels & Touchpoints
**Status:** General availability

With [dynamic BCC](https://www.braze.com/docs/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc), you can use Liquid in your BCC address. Note that this feature is only available in **Email Preferences** and can’t be set on the campaign itself. Only one BCC address per email recipient is allowed.

### Export sync logs by all rows

**Area:** Data & Reporting
**Status:** Early access

In the [Cloud Data Ingestion **Sync Log** dashboard](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), you can choose to export the row-level logs for a sync run by:

* **Rows with errors:** Downloads a file containing only the rows that had an **Error** status.
* **All rows:** Downloads a file containing every row processed in the run.

### Updates to Currents events

**Area:** Data & Reporting
**Status:** General availability

The following changes were made to Currents in Version 4:

* Field changes to event type `users.behaviors.pushnotification.TokenStateChange`:
    * Added new `string` field `push_token`: Push token of the event
* Field changes to event type `users.messages.pushnotification.Bounce`:
    * Added new `string` field `push_token`: Push token of the event
* Field changes to event type `users.messages.pushnotification.Send`:
    * Added new `string` field `push_token`: Push token of the event
* Field changes to event type `users.messages.rcs.Click`:
    * Added new `string` field `canvas_variation_name`: Name of the Canvas variation this user received
    * Field `user_phone_number` is now *optional*.
* Field changes to event type `users.messages.rcs.InboundReceive`:
    * Field `user_id` is now *optional*.
* Field changes to event type `users.messages.rcs.Rejection`:
    * Added new `string` field `canvas_step_message_variation_id`: API ID of the Canvas step message variation this user received


Refer to the [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) for the event changes for each release.

### LILT - Localization

**Area:** Partners

[LILT](https://www.braze.com/docs/partners/lilt/) is the complete AI solution for enterprise translation and content creation. LILT enables global organizations to scale and optimize their content, product, communications, and support operations, with AI agents and fully automated workflows.

## December 9, 2025

### SMS character encoding

**Area:** Channels & Touchpoints

Our [SMS segment calculator](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator) now has character encoding! Select **Display Character Encoding** to identify which characters are encoded as GSM-7 or UCS-2. 

![SMS segment calculator with a sample SMS message entered in the textbox and the character encoding turned on.](https://www.braze.com/docs/assets/img/sms/character_encoding.png){: style="max-width:70%;"}

### WhatsApp messages with optimization

**Area:** Channels & Touchpoints

Because MM API for WhatsApp doesn’t offer 100% deliverability, it's important to understand how to retarget users who may not have received your message on other channels. 

To retarget users, we recommend building a segment of users who didn’t receive a specific message. To do this, filter by the error code `131049`, which indicates that a marketing template message was not sent due to WhatsApp’s per-user marketing template limit enforcement. You can do this by [using Braze Currents or SQL Segment Extensions](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Adding Google Tag Manager to a landing page

**Area:** Data & Reporting

To add Google Tag Manager to your landing pages, add a Custom Code block to your landing page in the drag-and-drop editor, then [insert the Tag Manager code](https://www.braze.com/docs/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page) into the block.

### Allowlisting for Connected Content

**Area:** Orchestration

You can allowlist specific URLs to be used for [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/). To access this feature, contact your customer success manager.

### SMS Liquid use case

**Area:** Orchestration

The [Respond with different messages based on inbound SMS keyword](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#sms-keyword-response) use case incorporates dynamic SMS keyword processing to respond to specific inbound messages with different message copy. For example, you can send different responses when someone texts “START” versus “JOIN”.

### OtherLevels - Dynamic content

**Area:** Partners

[OtherLevels](https://www.braze.com/docs/partners/otherlevels/) is an experience platform that uses generative AI to transform how sports brands, publishers, and operators connect with their customers by transforming traditional content into on-brand personalized video and rich media experiences at scale.

### SDK breaking updates

**Area:** SDK
**Status:** Breaking

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## November 11, 2025

### BrazeAI Decisioning Studio™ Go

**Area:** BrazeAI™

You can now set up your integration with [BrazeAI Decisioning Studio™ Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/) by referencing these configuration articles for:

- [Braze](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)
- [Klaviyo](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)
- [Salesforce Marketing Cloud](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup)

### ChatGPT models with BrazeAI™ Operator

**Area:** BrazeAI™
**Status:** Beta

You can select from these GPT models to use for different request types with [Operator](https://www.braze.com/docs/user_guide/brazeai/operator):

- GPT-5 nano
- GPT-5 mini (default)
- GPT-5

### New features for Braze Agents

**Area:** BrazeAI™
**Status:** Beta

You can now customize your [Braze Agent](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents) by:

- Applying [brand guidelines](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/brand_guidelines/) for your agent to adhere to in its response. 
- Referencing a catalog to further personalize your message.
- Structuring an agent's output by providing the [output format](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents#select-output).
- Adjusting the [temperature](https://www.braze.com/docs/user_guide/brazeai/agents/reference) for the level of deviation for your agent's output.

### Background row images

**Area:** Channels & Touchpoints
**Status:** General availability

You can [add a background row image](https://www.braze.com/docs/user_guide/channels/in_app_messages/customize/style_settings#background-image) to an in-app message or landing page in the **Row properties** panel. Toggle on **Background image**, and then provide an image URL or select an image from the [media library](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library/). Finally, configure your alt text, size, position, and whether the image repeats to create patterns across the row.

![A row background image of a pizza that has a horizontal repeat pattern.](https://www.braze.com/docs/assets/img_archive/background_row.png)

### Copy preview link

**Area:** Channels & Touchpoints

Use **Copy preview link** in your [Banners](https://www.braze.com/docs/user_guide/channels/banners/create_a_banner/#step-5-test-your-message-optional), [email custom footers](https://www.braze.com/docs/user_guide/channels/email/customize/custom_email_footer/#create-your-custom-footer), and [email opt-in and unsubscribe pages](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/email_preferences/?tab=custom%20footer#subscription-pages-and-footers) to generate a shareable link that shows how your content looks for a random user.

### Editable user preview

**Area:** Channels & Touchpoints

You can [edit individual fields from a random or existing user](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook#customizing-an-existing-user) to help test dynamic content within your message. Select **Edit** to convert the selected user into a custom user you can modify.

![The "Preview as a User" tab with an "Edit" button.](https://www.braze.com/docs/assets/img_archive/edit_user_preview.png){: style="max-width:50%;"}

### WhatsApp Flows

**Area:** Channels & Touchpoints

When incorporating a WhatsApp Flow message into a Braze Canvas or campaign, you may want to capture and utilize specific information that users submit through the Flow. Braze needs to receive additional information regarding the structure of the user response, specifically the expected shape of the JSON response, to generate the required nested custom attribute (NCA) schema.

Now you can give Braze the information about the response structure by [saving the Flow response as a custom attribute](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) and completing a test send.

### WhatsApp messages with optimized delivery

**Area:** Channels & Touchpoints

Use Meta’s advanced AI systems to deliver your marketing messages to more users who are most likely to engage with them, significantly boosting deliverability and message engagement.

[WhatsApp messages with optimized delivery](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/) are sent using Meta's new [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/), which provides superior performance compared to the traditional Cloud API. This new sending pipeline helps you better reach users who value and want to receive your messages.

### Custom attributes — Values

**Area:** Data & Reporting

When viewing a usage report, select the [**Values** tab](https://www.braze.com/docs/user_guide/data/activation/custom_data/custom_attributes/#values-tab) to view the top values of the selected custom attributes based on a sample of approximately 250,000 users.

### Frequency capping abort events in Currents

**Area:** Data & Reporting

When using Currents, you can now reference `abort_type` in the channel abort events. This identifies that a message has been aborted due to frequency capping and includes which frequency capping rule caused the abort. This helps inform how you set up your frequency capping rules. Refer to [Message engagement events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) for specific Currents event details.

### Mapping to catalog fields for drag-and-drop product blocks

**Area:** Data & Reporting

In your catalog settings, you can select the **Product blocks** toggle to [map to specific fields](https://www.braze.com/docs/user_guide/messaging/design_and_edit/product_blocks/#catalog-setup) and information in your catalog. This allows you to select which fields to use as the product title, product URL, and image URL.

### Multi-rule feature flag rollouts

**Area:** Data & Reporting

Use [multi-rule feature flag rollouts](https://www.braze.com/docs/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) to define a sequence of rules for evaluating users, which allows for precise segmentation and controlled feature releases. This method is ideal for deploying the same feature to diverse audiences.

### RFM SQL Segment Extension

**Area:** Data & Reporting

You can create an [RFM (recency, frequency, monetary) Segment Extension](https://www.braze.com/docs/rfm_segments/) to target your best users by measuring their purchasing habits.

RFM analysis is a marketing technique that identifies your best users by scoring users on a scale from 0—3 for each category (recency, frequency, monetary), where 3 is the best score and 0 is the worst. Recency, frequency, and monetary values are all based on data from a specific time range of your choosing.

### Sync logs and observability for Cloud Data Ingestion

**Area:** Data & Reporting
**Status:** General availability

The Cloud Data Ingestion (CDI) [Sync Log dashboard](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs/) allows you to monitor all data processed by CDI, verify whether data was synced successfully, and diagnose any issues with “incorrect” or missing data.

### `Live Activities Push to Start Registered for App` segmentation filter

**Area:** Data & Reporting

The [`Live Activities Push to Start Registered for App` filter](https://www.braze.com/docs/user_guide/audience/segments/segmentation_filters/#live-activities-push-to-start-registered-for-app) segments your users by whether they are registered to start a Live Activity through iOS push notifications for a specific app.

### Cloudinary - Dynamic content

**Area:** Partners

[Cloudinary](https://www.braze.com/docs/partners/cloudinary/) is an image and video platform that empowers you to manage, edit, optimize, and deliver images and video on a massive scale to any campaign across channels and customer journeys. When integrated and enabled, Cloudinary's media management will power and provide dynamic, contextual, and personalized asset delivery for your Braze campaigns and Canvases.

### Kameleoon - A/B testing

**Area:** Partners

[Kameleoon](https://www.braze.com/docs/partners/kameleoon/) is an optimization solution with experiment, AI-powered personalization, and feature management capabilities in a single unified platform.

### StackAdapt - Advertising

**Area:** Partners

[StackAdapt](https://www.braze.com/docs/partners/stackadapt/) is an AI-powered marketing platform that delivers targeted performance-driven advertising. It allows you to sync user profile data from Braze into the StackAdapt Data Hub. By connecting the two platforms, you can create a unified view of your customers and activate first-party data to improve ad performance.
