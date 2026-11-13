# November 12, 2026 release

## Data & Reporting

### Segment reporting



[Segment reporting](https://www.braze.com/docs/user_guide/analytics/reports/report_builder/segment_reporting) adds segments as a primary reporting dimension and a drilldown in Report Builder. You can measure how segments perform over time, see which campaigns and Canvases target a segment, and compare engagement across segments for a single campaign or Canvas.

### Query Builder date range and expanded exports



[Query Builder](https://www.braze.com/docs/user_guide/analytics/reports/query_builder) reports include a date range filter. You can query up to one year of history, or up to two years when your workspace has Snowflake Data Sharing or Currents. CSV exports can include up to 100,000 rows.

### Account objects



[Account objects](https://www.braze.com/docs/user_guide/data/activation/accounts) let you model the businesses behind your users, such as companies, franchises, properties, or households. Link users to accounts with a role, connect accounts to each other to model hierarchies, and then segment and personalize messages with account data instead of copying it to every user profile. Send account data to Braze through the [Data Objects API](https://www.braze.com/docs/api/endpoints/data_objects) or Cloud Data Ingestion, or edit accounts in the dashboard.

Account objects require a short onboarding. Complete the questionnaire on the **Accounts** page, and Braze sets up your environment based on your use case and data volume. Each account starts with a limit of 50,000 account records.

### Calculated attributes



[Calculated attributes](https://www.braze.com/docs/user_guide/data/activation/attributes/calculated_attributes) turn event data into profile attributes with a no-code formula builder. Choose an aggregation, a purchase or eCommerce event, and a time frame of up to two years, then activate the attribute so Braze refreshes values daily and writes them to user profiles for segmentation. Each workspace can have up to 25 active calculated attributes.

### Cloud Data Ingestion visual mapper



The Cloud Data Ingestion [visual mapper](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/visual_mapper) is a no-code way to sync data. Instead of writing SQL or building a separate table for Braze to sync, load an existing table or view from your warehouse, then map its columns to Braze fields. The visual mapper is available for all Cloud Data Ingestion warehouse sources and for the attributes, events, and Canvas trigger sync types.

After you create a Snowflake, Redshift, Databricks, Fabric, or BigQuery source, create a sync and load a table. You can also use the Source Explorer to browse available tables and views. Map each column to a Braze field, including the required columns: a Braze-accepted identifier, such as `external_id`, and `UPDATED_AT` for change tracking. Syncing `PAYLOAD` tables with the [SQL editor](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sql_editor) continues to be supported.

### Cloud Data Ingestion: Workload Identity Federation for Google sources



Cloud Data Ingestion supports authenticating with [Workload Identity Federation](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/google_bigquery#workload-identity-federation) (WIF) for Google Cloud Storage and Google BigQuery sources. When you create a source, select **Workload Identity Federation** as the authentication method and enter its configuration.

### Cloud Data Ingestion to BrazeAI Decisioning Studio



Cloud Data Ingestion has a [BrazeAI Decisioning Studio destination](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/decisioning_studio) that sends data from your data warehouse directly to Decisioning Studio, so you don't need custom ETL jobs that drop raw files into GCS buckets. Decisioning Studio uses the data for reinforcement learning and AI decisioning. Only data warehouse sources are supported, and the destination is available only to Braze and BrazeAI Decisioning Studio customers.

In the sync flow, select **BrazeAI Decisioning Studio** as the destination after you pick a source. Tag the data as a user profile, message engagement event, conversion event, or other asset type. Then write a query in the SQL editor to shape the data, and choose one or more columns as the primary or composite key.

### API request log



The [API request log](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/api_request_log) shows the API requests sent to Braze, so you can validate an initial integration or troubleshoot an existing one. Braze keeps logged requests for 14 days and includes the request payload when available, up to 8 KiB. Filter requests by date, time, API key, endpoint, status, and request body contents.

### Databricks OpenSharing for EU clusters



[Databricks OpenSharing](https://www.braze.com/docs/opensharing) (formerly Delta Sharing) is available for customers hosted on EU clusters. It securely shares Braze event and campaign data with your Databricks account without copying or replicating data. Shared data is read-only, and you can query it with Databricks SQL to create reports, perform attribution modeling, and join Braze data with other data in Databricks. It includes the same engagement data that Braze delivers to other Currents destinations and Snowflake Data Sharing.

### Data Distribution monthly release



Version 14 of the Data Distribution release (Currents, Data Sharing, and OpenSharing) went out on November 4, 2026. It adds events for Data Objects and for tracking API request completion, and it adds `canvas_entry_id` to various channel events. For details, see [Currents Event Changelogs](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

### Workload Identity Federation for Currents

Workload Identity Federation (WIF) is an additional way to authenticate a Currents integration for [Google Cloud Storage](https://www.braze.com/docs/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents#workload-identity-federation-auth-method) or [Azure Blob Storage](https://www.braze.com/docs/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents#workload-identity-federation-auth-method). Braze authenticates with a short-lived identity token instead of a long-lived credential such as a service account key, so there's no static secret to leak or rotate. Existing options, such as service account keys and certificates, remain available.

## BrazeAI<sup>TM</sup>

### Verified MCP clients



On the [MCP Clients](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin/#manage-mcp-clients) page, admins can approve Braze-verified MCP clients by name—including ChatGPT, Claude, Claude Code, Cursor, OpenAI Codex, and Visual Studio Code—instead of entering each client's redirect URIs by hand.

### Remote MCP server support for IP allowlisting



Companies that use [IP allowlisting](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings/#dashboard-ip-allowlisting) can use the remote [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server/setup) and [Operator Connect](https://www.braze.com/docs/user_guide/brazeai/mcp_server/operator_connect). Braze lets MCP server and Operator Connect requests through your IP allowlist, so admins don't need to add Braze IP addresses to their allowlist.

### Workspace endpoints for the Braze MCP server



MCP clients connected to Braze can list, look up, create, update, and delete workspaces, within the connected user's permissions. The [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server/available_api_functions) includes workspace tools. You see only the workspaces you belong to, and look-ups return only the fields you can view. You can update a workspace's name, time zone, and email settings within your permissions. Creating and deleting a workspace requires a company admin. For example, a company admin can ask Claude to create a workspace for a new market without signing in to Braze.

### Agent Console enhancements

You can do the following in the [Agent Console](https://www.braze.com/docs/user_guide/brazeai/agents):

- [Agentic Standards](https://www.braze.com/docs/user_guide/brazeai/agents/agentic_standards) are generally available. Free workspaces include 25 evaluation runs per month. Paid workspaces have no monthly run-count limit.
- Create a Campaign or Canvas Standard from a Braze template or from scratch.
- [Copy Canvas Step Agents and Agentic Standards](https://www.braze.com/docs/user_guide/brazeai/agents/reference#copy-to-workspace) to another workspace in the same company.
- Format agent instructions with Markdown, and switch between **Edit** and **Preview** while you write them.
- On the paid tier, [evaluation logs](https://www.braze.com/docs/user_guide/brazeai/agents/agentic_standards#review-evaluation-logs) show each run's share of the monthly usage limit and who ran it.
- [Conversational Agents](https://www.braze.com/docs/user_guide/brazeai/agents/conversational_agents) remains in beta. You can run simulations, and workflow attributes can use allowed values.

### Brand guidelines



You can generate [brand guidelines](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/brand_guidelines) from uploaded files, such as a brand book, and from website URLs, or write them yourself. Guidelines can be up to 100,000 characters. Test a guideline by generating example copy or by validating existing content, then add it as context for Operator or an agent.

### Skills



[Skills](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities/skills) are reusable instructions Operator follows when they fit the task, such as a naming convention or a required email footer. Create a skill on the Skills page, ask Operator to remember a rule, or create and edit skills from another AI tool through the Braze MCP server. Operator applies skills for everyone in the workspace, including through [Operator Connect](https://www.braze.com/docs/user_guide/brazeai/mcp_server/operator_connect).

### External MCP servers



[External MCP servers](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities/mcp_servers) let Operator use tools from other products, such as Jira, Notion, or GitHub. An admin adds a remote server and chooses which tools Operator can use. You sign in with your own account. Operator asks for approval before it takes action in the other product. Contact your Braze account manager to participate in the early access.

### Agents and Context



The **Agent Console** entry in the navigation is now **Agents**. A **Context** section in that menu brings together Skills, brand guidelines, Agentic Standards, knowledge sources, and external MCP servers. Existing pages keep their permissions, and previous URLs redirect.

### Optimize with BrazeAI and Intelligent Timing improvements



[Optimize with BrazeAI](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection) (formerly Intelligent Selection) uses a fixed control group as the baseline for lift, and you can choose whether optimization continues indefinitely or stops when BrazeAI is 95% confident. [Intelligent Timing](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_timing) now adjusts for daylight saving time so sends stay on the correct local time when clocks change.

### AI item recommendations: improved creation flow



The [AI item recommendation](https://www.braze.com/docs/user_guide/brazeai/item_recommendations/creating_recommendations/ai) creation flow shows which catalog and events produce the best recommendations before you commit. After you pick a catalog, Braze shows automatic mapping results as selectable cards ranked by match quality, so you don't have to choose between Order Placed and a custom event and then find out at the last step whether the fields mapped well. Each card shows when matches were last updated. Updates run automatically and can take up to 30 minutes. Before Braze builds the recommendation, a summary step recaps the catalog, event, and field mappings you selected.

### More flexible experiments

Experiments are more flexible across campaigns and Canvases, including [Experiment Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step):

- You can turn off Winning Variant or Personalized Variant on a campaign during the experiment phase. The holdout group still receives messages at their originally scheduled time.
- Control group and variant percentages stay the same when you turn **Optimize with BrazeAI** on or off.
- **Optimization Event** is the label across campaign A/B tests, Experiment Paths, and Content Optimizer.

### Decisioning Studio Go agent status indicators



[Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup#training-period) reporting shows which stage an agent is in after launch, from the first send through training and personalization, so you can tell whether the agent is still preparing or already learning.

### Self-serve action banks for Decisioning Studio Pro



An [action bank](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/design_agents) is the library of options Decisioning Studio chooses from for each customer, such as messages, offers, and send times. Decisioning Studio Pro customers can view and edit their action bank in the Braze dashboard, with help from BrazeAI Operator. Your account team chooses which action bank fields you can edit, such as subject line or offer code, separately for each dimension. You can add actions, turn actions on or off, change active dates, and edit the allowed fields. Operator supports more complex requests, such as deactivating all subject lines that reference the holidays. Your edits are saved as a draft, and your account team reviews and launches them.

### Braze email stats in Decisioning Studio Go agent reporting



[Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring) agents show the standard Braze email stats you use on campaigns: sends, opens, clicks, unsubscribes, and bounces. The numbers are summed across everything the agent has sent, so you can see how the agent performs in the same metrics you use elsewhere in Braze.

## Orchestration

### Partner app governance



Admins can approve or block [OAuth Partner Apps](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin/#oauth-partner-apps)—such as creative studio partners—and choose which workspaces each app can reach.

### Sign in to Braze Bonfire Community with Braze



Dashboard users can open **Community** and select **Sign in to Braze Bonfire Community** to sign in with their Braze account. **Braze Bonfire Community** appears under [OAuth Partner Apps](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin/#braze-bonfire-community) and defaults to approved.

### Terminate roaming sessions



Under [Dashboard IP allowlisting](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings/#terminate-roaming-sessions), turn on **Terminate roaming sessions** so Braze ends a dashboard session as soon as it continues from an IP outside your allowlist.

### Suspend dormant accounts



In [Security Settings](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings/#dormant-accounts), turn on **Suspend dormant accounts** to automatically suspend dashboard users after 180 days without a sign-in. Braze emails users 15 days and one day before suspension, then sends a suspension notice.

### Workspace quiet hours



[Workspace quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) set a default quiet hours window for a messaging channel across the workspace. Campaigns and Canvases on that channel follow the window automatically, and you can still opt individual campaigns or Canvases out or set campaign-level quiet hours. 

### Multi-channel support in Message Prioritization



[Message Prioritization](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization) applies to multi-channel campaigns and multi-channel Canvases. You can opt multi-channel campaigns in to Message Prioritization, and bring prioritization to the multi-channel steps in your Canvases.

### Send to Destination



The [Send to Destination step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/send_to_destination) sends users from one Canvas to another as soon as they reach the step. Users who meet the destination audience enter immediately, including when that Canvas uses scheduled or action-based entry. They continue in the source Canvas. The step follows the destination Canvas re-entry rules and isn't subject to API rate limits.

### Send to a Decisioning Studio Go agent



In a [Send to Destination](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/send_to_destination#send-users-to-a-decisioning-studio-go-agent) step, set **Destination type** to **Decisioning Studio agent** to add users to a [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/composing_with_canvas) agent. On the agent, select **Add directly to the audience**, and include that agent with the segment's `Decisioning Studio Agent` filter. Users continue in the source Canvas.

### Workspace Canvas alerts



[Workspace Canvas alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/workspace_canvas_alerts#notifications) set default alerts for every Canvas in a workspace. Braze provisions alerts for user entries, message sends, and archived Canvases. Each alert starts off. When you turn one on, it covers active Canvases and new Canvases unless a Canvas opts out. Notify recipients by email, webhook, or a Slack incoming webhook. Contact your Braze account manager to participate in the early access.

### Slack notifications for Canvas alerts

[Custom Canvas alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/custom_canvas_alerts) are generally available, and [workspace Canvas alerts](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/workspace_canvas_alerts#notifications) are in early access. Both can post a notification to Slack with an incoming webhook URL. The channel is set when you create the webhook in Slack. You can enable email, Slack, a webhook, or any combination.

## Channels & Touchpoints

### WhatsApp BSUID Request Contact Info flow



You can send WhatsApp messages that use Meta's Share Contact Info button, then capture the phone number a user shares. This identifies users who reach you with only a business-scoped user ID (BSUID) and connects them to existing profiles. For the workflow, see [Request contact info for WhatsApp BSUID-only users](https://www.braze.com/docs/user_guide/channels/whatsapp/use_cases/request_contact_info_bsuid).

### Key-value pairs for drag-and-drop in-app messages



You can add [key-value pairs](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs/#in-app-messages) to in-app messages in both the traditional editor and the drag-and-drop editor.

### Email subscription Liquid tags in landing pages



You can use [email subscription Liquid tags](https://www.braze.com/docs/user_guide/channels/email/subscriptions) in the click actions of buttons and links on [landing pages](https://www.braze.com/docs/user_guide/messaging/landing_pages). Tags such as `${email_unsubscribe_url}`, `${set_user_to_subscribed_url}`, and `${set_user_to_unsubscribed_url}` work on landing pages the same way they do in email.

In the drag-and-drop editor, select a button or link, set its click action to a URL, and enter the tag. When an identified user, such as one who arrived through a landing page Liquid tag in a message, selects it, Braze resolves the tag for that user so they can unsubscribe, opt in, or manage their email preferences from the page. For example, you can build a branded unsubscribe page with a short survey, a re-engagement page with a one-click resubscribe button, or an opt-in page that subscribes the user in a single click.

### Webhook credentials



[Webhooks](https://www.braze.com/docs/user_guide/channels/webhooks/create_a_webhook#use-a-saved-credential-optional) can authenticate with a saved credential instead of an API key typed into the message. This matches [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call), which uses the same stored credentials. Credentials are stored once at **Settings** > **Credential Management**, referenced by name in the composer, and never shown again after you save them. They belong to one workspace, and each credential needs an allowed domain to be used with webhooks.

In the webhook composer, enter an HTTPS URL with a fixed hostname, then select a saved credential in **Credential**. The selector lists credentials whose allowed domain matches the URL's hostname. The webhook preview omits the credential reference and its authentication headers, and test sends apply the same credential.

To open **Credential Management**, users need the "View Credential Management" permission. To create, edit, or delete credentials, they need "Edit Credential Management". For details, see [Manage saved credentials](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#manage-saved-credentials).

### Shopify configurable attributes and customer metafields sync



With the [Shopify standard integration](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_standard_integration/#sync-customer-metafields-as-user-attributes), you can sync up to 20 Shopify customer metafield definitions to Braze user profiles as nested custom attributes, then use them for segmentation and personalization. For how values are typed, updated, and used in messaging, see [Shopify customer metafields](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/#shopify-customer-metafields).

### Shopify attribute sync: empty value handling



When Shopify sends an empty value for a synced user attribute, choose whether Braze [keeps or clears](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/#empty-values-from-shopify) the value already on the profile. Integrations default to keeping the existing value.

### Shopify order events: enrichment and Order Placed opt-out



Add up to 20 [Shopify order metafields](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_data_features/order_metafields) to supported order events for segmentation and personalization. If another system is the source of truth for orders, you can [turn off Shopify Order Placed events](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_standard_integration/#send-order-placed-events-from-another-source) for a store so each order is counted once.

### Shopify WhatsApp consent collection



Sync WhatsApp marketing opt-ins from Shopify into Braze WhatsApp subscription groups, alongside email and SMS consent. Configure this in the [Shopify standard integration](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_standard_integration) setup, and see [WhatsApp marketing opt-ins](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_overview#whatsapp-marketing-opt-ins) for how states map to Braze.

### IP pools and IP addresses



Amazon SES customers with verified domains can create [IP pools and add dedicated IP addresses](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains/ip_pools) on the **Sender Verification** page. The sender profile questionnaire recommends a setup from your sending volume, or you can create IP pools yourself. Braze assigns the dedicated IP addresses from your contract.

### Intelligent IP warming



[Automated IP warming](https://www.braze.com/docs/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming?tab=intelligent) has an **Intelligent** audience option. Upload your engagement history from your previous email provider, and Braze prioritizes sending to the users most likely to engage. New IPs build reputation on your best users, without you building or ranking segments by hand.

## Partnerships

### Microsoft Ads – Canvas Audience Sync



[Audience Sync to Microsoft Ads](https://www.braze.com/docs/partners/canvas_audience_sync/microsoft_audience_sync) lets you add or remove Braze users from Microsoft Advertising customer lists from Canvas, so you can retarget and suppress across Bing, MSN, and the Microsoft Audience Network.

### FeedOtter - Message Orchestration - Templates

[FeedOtter](https://www.braze.com/docs/partners/message_orchestration/templates/feedotter) is a content-to-email automation platform that turns content from CMSs, websites, feeds, APIs, databases, and spreadsheets into polished emails. The Braze and FeedOtter integration lets you collect and build newsletter content in FeedOtter, then publish each issue to a Braze email template and send it to the segment you choose.

### Zendesk Support Handoff - Instant Chat

[Zendesk](https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/instant_chat/zendesk_support_handoff) is a customer service platform for omnichannel support. With this integration, your Braze Conversational AI agent can hand a live conversation to a human support agent in Zendesk when it needs to. After the handoff, a person takes over in the Zendesk Agent Workspace, and messages flow both ways until the agent closes the conversation.

## SDK

The following SDK updates have been released. For more details, see [SDK Changelogs](https://www.braze.com/docs/developer_guide/changelogs).

### SDK breaking updates

The following major SDK releases include breaking changes:

- [Android SDK 45.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4500) changes `BannerView` so it hosts a `WebView` instead of being one. `WebView` methods called on `BannerView` no longer compile. Jetpack Compose `ContentCardsList` calls `cardUpdateHandler` when the list resumes, when cached cards load, and after a card is dismissed, and shows cards once the host lifecycle reaches `RESUMED`. `com.braze:android-sdk-jetpack-compose` now depends on Material 3 instead of Material 2. If your app relied on the SDK to provide `androidx.compose.material`, add it yourself.
- [Android SDK 45.0.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4501) updates Kotlin from 2.2.20 to 2.4.21.
- [React Native SDK 24.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/24.0.0) updates the native iOS bridge from Braze Swift SDK 18.2.1 to 19.1.0, which raises the minimum supported iOS version from 12.0 to 15.0, and updates the native Android bridge from Braze Android SDK 43.1.1 to 44.0.0. On iOS, `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]` is replaced by `[BrazeReactDataTranslator formatPushPayload:withUrlOverride:]`.
- [Expo plugin 6.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/6.0.0) requires Expo 57.0.23 or newer and Braze React Native SDK 24.0.0 or newer. That React Native SDK raises the minimum iOS version to 15.0.
- [Cordova SDK 17.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1700) updates the native bridges to Android SDK 43.1.1 and Swift SDK 18.2.0. On iOS, Content Card extras are now a JavaScript object instead of a JSON string, so remove `JSON.parse`.
- [Xamarin SDK 11.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md) updates the bindings to Android SDK 43.1.1 and Swift SDK 18.2.0, adds .NET 10.0, and drops .NET 9.0.

### Summary of recent SDK features and fixes

- [Android SDK 45.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4500) adds Kotlin `Flow` subscriptions for Content Cards, Feature Flags, Banners, and `changeUser` events. Reported control impressions may decrease. It also fixes crashes (Android 16 `BannerView` and some Honor devices), dropped or backlogged custom events, and dismissed banners reappearing.
- [Android SDK 45.0.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4501) fixes a freeze when the SDK blocked the shared IO thread pool, and adds `BrazeLogger.redactSecrets` to redact secrets from SDK logs.
- [Swift SDK 19.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1910) fixes `unregisterPush` and `logout` failing after an app restart, missing dashboard key-value pairs on push notifications without deep links, missing video push thumbnails on iOS 26.5 and later, and a crash during rapid network status changes. It also adds a public `extras` property on `Braze.Notifications.Payload`.
- [Swift SDK 19.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1920) adds an optional `catalogName` on product viewed events, support for triggering in-app messages when an array or object custom event or purchase property exists, and `Braze.Configuration.Logger.redactSecrets`.
- [Web SDK 7.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#710) adds [Web Targeting](https://www.braze.com/docs/developer_guide/banners/web_targeting) for Banners, including `braze.insertWebTargetingBanners()`, `braze.automaticallyInsertWebTargetingBanners()`, and an `enableWebTargetingBannerRetryLoop` option that defaults to `true`.
- [Roku SDK 2.2.1](https://github.com/braze-inc/braze-roku-sdk/releases/tag/v2.2.1) fixes a crash when a templated in-app message request fails during intermittent or no connectivity.
- [Roku SDK 2.3.0](https://github.com/braze-inc/braze-roku-sdk/releases/tag/v2.3.0) adds optional automatic display of modal in-app messages with `BrazeDefaultInAppMessage`, and handlers so an app can render or process selected messages itself.
- [React Native SDK 24.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/24.0.0) adds `populateInitialPayloadFromNotificationResponse:`, which fixes `getInitialPushPayload()` returning `null` on a cold start from a push tap when the app uses the UIKit scene life cycle. It also fixes iOS build failures (`pod install` with dynamic frameworks and Xcode 26.6).
- [React Native SDK 24.0.1](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/24.0.1) fixes an Android issue where `Braze.initialize()` with the same API key and endpoint tore down the running SDK and deleted geofences on later launches.
- [Expo plugin 5.2.1](https://github.com/braze-inc/braze-expo-plugin/releases/tag/5.2.1) fixes Android Gradle configuration on Android Gradle Plugin 9 or newer with built-in Kotlin, and adds missing TypeScript types for several Android config props.
- [Expo plugin 6.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/6.0.0) fixes `Braze.getInitialPushPayload()` returning null on an iOS cold start from a push tap when the app uses the UIKit scene life cycle.
- [Cordova SDK 17.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1700) deprecates `getContentCardsFromServer` (use `requestContentCardsRefresh()` plus `getContentCardsFromCache()`), and fixes an Android crash on in-app message arrival and several Android build failures.
