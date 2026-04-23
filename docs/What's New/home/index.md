# What's new in Braze

**Tip:**


For more information on any of the updates listed on this page, contact your account manager or [open a support ticket](https://www.braze.com/docs/user_guide/administer/personal/braze_support/). Check out our [SDK Changelogs](https://www.braze.com/docs/developer_guide/changelogs) for more information about our monthly SDK releases, improvements, and breaking changes.



**April 2, 2026**



## April 2, 2026 release

### Data & Reporting

#### New Banner channel fields in Currents and Datashare events

Braze added fields for existing Banner channel events in Currents and Datashare exports. For a list of these event and field updates, see [Changes in Version 7](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage).

#### Mixpanel EU and India data center support for Currents

The Currents Mixpanel integration now supports Mixpanel's EU and India data centers. When you configure a Mixpanel integration, you can choose which Mixpanel region Braze sends your data to. This update supports Mixpanel's growing international footprint for mutual customers. For more information, see [Mixpanel](https://www.braze.com/docs/partners/data_and_analytics/analytics/mixpanel).

#### Reusable Cloud Data Ingestion (CDI) sources and syncs



Cloud Data Ingestion (CDI) has a new design that separates sources and syncs, so you can reuse one source across multiple syncs. Existing syncs migrate automatically to the new sources and syncs model with no downtime. Go to **Cloud Data Ingestion** > **Sources** to view, edit, or create sources, then select a source from the dropdown when creating a sync. This change reduces repetitive setup, and creates a foundation for future enhancements. For more information, see [Setting up data warehouse integrations](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### File support tickets from BrazeAI Operator<sup>TM</sup>



[BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator/) now includes a flow to file Braze support tickets without leaving the dashboard. For steps, auto-included context, and tips for faster resolution, see [File support tickets with BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator/support_tickets/).

### Orchestration

#### Multi-language translations



After adding locales to your workspace, use [multi-language translations](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) to target users in different languages all within a single push, email, Banner, in-app message, or Content Block.

![Locale previews](https://www.braze.com/docs/assets/img/multi-language_support/multi_language_user_preview.png?f55b1a40baaba6ede110adbbda7cbf8e){: style="max-width:70%;"}

#### Canvas Context enhancements



In Canvas, you can now reference context variables to set:

- An [expiration](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/context_variables/#set-an-expiration) for Banners and in-app messages in a Message step
- A [personalized delays](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/context_variables/#action-path-delays) for Action Paths steps

In the Context variable name field, you can also enter the context variable name or select it from the dropdown in the step editor. For more details, see [Context](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context/) and [Context variables](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/context_variables/).

### Channels & Touchpoints

#### KakaoTalk



[KakaoTalk](https://www.braze.com/docs/kakaotalk) is a messaging channel that enables broadcast messaging and 1:1 chat with users. Create a personalized user experience by using Liquid and other dynamic content to build an environment that fosters and enhances a rich user experience with your brand.

![A KakaoTalk list item message.](https://www.braze.com/docs/assets/img/kakaotalk/wide_image.png?cc34a0abe27faa0167d07982b3019022){: style="max-width:70%;"}

#### Banners in Canvas



You can use [Banners](https://www.braze.com/docs/user_guide/channels/banners/) as a messaging channel in Canvas [Message steps](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step/). Banners allow you to personalize app or website content dynamically, reflecting real-time user eligibility and behavior.

### Partnerships

#### CataBoom - Message Personalization - Visual and Interactive Content

[CataBoom](https://www.braze.com/docs/partners/cataboom) is a gamification platform. Brands use it to build and launch interactive digital experiences, including spin-to-win games, quizzes, and instant-win games. Those experiences deepen engagement and collect first-party data.

#### Denada - Message Orchestration - Templates

[Denada](https://www.braze.com/docs/partners/denada) is an AI-powered marketing creative platform that lets subject matter experts create on-brand marketing materials through natural conversation. With Denada, teams can go from ideation to finished email content without needing design expertise.

#### Poq - eCommerce - Mobile app platform

[Poq](https://www.braze.com/docs/partners/poq) enables enterprise businesses to rapidly launch, manage, and scale fully native iOS and Android apps—delivering high-performance mobile experiences that drive commerce and bring your brand promise to life.

#### The Trade Desk – Canvas Audience Sync

Using the [Braze Audience Sync to The Trade Desk](https://www.braze.com/docs/partners/canvas_audience_sync/trade_desk_audience_sync/), you can dynamically sync your first-party user data from Braze directly into The Trade Desk for ad retargeting, lookalike modeling, and suppression.

### SDK

#### Connect your Integrated Development Environment (IDE) to the Docs MCP

Use AI coding assistants to accelerate your Braze integration workflow by connecting your Integrated Development Environment (IDE) to the Braze Docs MCP through Context7. This gives your assistant direct access to current Braze documentation, so it can generate more accurate SDK guidance, code examples, and troubleshooting help in your development environment. For setup steps in Cursor, Claude Desktop, and VS Code, see [Building with an LLM](https://www.braze.com/docs/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp).

#### SDK breaking updates

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




**March 5, 2026**



## March 5, 2026 release

### Data & Reporting

#### New data center



Braze has launched a new [data center](https://www.braze.com/docs/user_guide/data/infrastructure/data_centers/): JP-01. You can sign up for region-specific data centers when setting up your Braze account.

#### Context variables



[Context variables](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context) are temporary pieces of data you can create and use within a user’s journey through a specific Canvas. Each time a user enters the Canvas—even if they have entered it before—the context variables will be redefined based on the latest entry data and Canvas setup. This approach allows each Canvas entry to maintain its own independent context, allowing users to have multiple active states within the same journey while retaining the specific context for each state.

#### Cloud Data Ingestion sources



[Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) has a new UI that separates sources from syncs, letting you reuse a single source across any number of syncs. This reduces duplicate configuration and simplifies setup when you have multiple syncs. If you have existing syncs, they're automatically migrated to the new sources-and-syncs structure with no downtime. To get started, go to **Cloud Data Ingestion** > **Sources** to view, edit, or create sources, then select a source from the dropdown when creating a sync.

#### Additional fields for Currents and Data Share events



[Currents and Data Share events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) now include the following new fields to deepen the data available for analytics and downstream systems:

- `agentconsole.AgentExecuted`: Added `error` (string)—a description of any error that occurred.
- `agentconsole.ToolInvocation`: Added `request_id` (string)—a unique ID for the overall LLM request and complete execution.
- `users.messages.rcs.InboundReceive`: Added `canvas_variation_name` (string)—the name of the Canvas variation the user received.

#### Campaign and Canvas fields for Snowflake Data Share



[Snowflake Data Share](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3) now includes additional fields reflecting Campaign and Canvas information across 66 existing tables, including:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSV pre-import validation and error reporting



[CSV user imports](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users/) now support pre-import validation and detailed error reporting. Before importing, select **Validate file before importing** on the **Import Users** page—Braze will scan your file and generate a report identifying rows that will fail entirely (errors) and rows that will succeed with some values skipped (warnings). You can download the report, fix your CSV, and re-upload, or proceed as-is. After the import completes, a downloadable report of any rows that failed is also available, with the exact reason for each issue.

#### Messaging diagnostics dashboard



The [Messaging Diagnostics dashboard](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard/) provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected.

### BrazeAI<sup>TM</sup>

#### Braze Agents in Agent Console



[Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents/) are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences. When you create an agent, you define its purpose and set guardrails for how it should behave. After it’s live, the agent can be [deployed](https://www.braze.com/docs/user_guide/brazeai/agents/deploying_agents) in Braze to generate personalized copy, make real-time decisions, or update catalog fields.

### Orchestration

#### Granular user permissions



Braze is introducing [granular permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/), a more flexible way to manage user access. Refer to [Migrating to granular permissions](https://www.braze.com/docs/granular_permissions_migration/) to learn about the migration process, including how legacy permissions map to granular permissions.

#### Channel-based rate limiting



When setting a delivery speed rate limit for a multi-channel campaign or Canvas, you can choose to set either a shared rate limit or a [channel-based limit](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases). When a multichannel campaign or Canvas uses channel-based rate limiting, the rate limit applies to each of the selected channels. For example, you can set your campaign or Canvas to send a maximum of 5,000 webhooks and 2,500 SMS messages per minute across the campaign or Canvas.

#### Canvas Context step



[Canvas Context steps](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context) let you create and update one or more variables for a user as they move through a Canvas. For example, if you have a Canvas that manages seasonal discounts, you can use a context variable to store a different discount code each time a user enters the Canvas.

### Channels & Touchpoints

#### Translate locales in Content Blocks



After adding locales to your workspace, you can [target users in different languages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) all within a Content Block.

### Partnerships

#### Algolia - Search Recommendations

[Algolia](https://www.braze.com/docs/partners/ecommerce/product_search_recommendations/algolia) is a search and discovery platform that helps developers build fast, relevant, and scalable search experiences. With a powerful API-first approach, Algolia combines advanced ranking algorithms with AI-driven insights for seamless site search, navigation, and personalized content discovery.

#### Anthropic - AI Model Provider

[Anthropic](https://www.braze.com/docs/partners/ai_model_providers/anthropic) is an AI safety and research company developing Claude, a next-generation AI assistant built to be helpful, honest, and safe for a wide range of language tasks.

#### Canva - Message Personalization - Creative Studio

[Canva](https://www.braze.com/docs/partners/canva) syncs your images in Canva directly to the Braze Media library, streamlining your creative workflow and keeping your visual assets up to date across all your messaging channels.

#### DOTS.ECO - Rewards

[DOTS.ECO](https://www.braze.com/docs/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

#### Figma - Message Personalization - Creative Studio

[Figma](https://www.braze.com/docs/partners/figma) is a collaborative design platform that allows you to build, design, and prototype products. Use this integration to send images and visual assets from Figma directly into the Braze media library.

#### Flybuy - Message Personalization - Location

[Flybuy](https://www.braze.com/docs/partners/message_personalization/location/flybuy) by Radius Networks is the leading omnichannel location platform leveraging AI-powered technology to optimize speed of service across pickup, delivery, drive-thru, and dine-in. Through its integrated Marketing Suite, Flybuy also enables brands to deliver hyper-targeted, moment-based messages, helping to drive engagement, increase check size, and support broader loyalty initiatives.

#### Google Gemini - AI Model Provider

[Google Gemini](https://www.braze.com/docs/partners/ai_model_providers/google_gemini) is Google’s family of AI models that combines advanced reasoning across text, code, and images to help brands deliver smarter, more personalized experiences.

#### Limbik - Message Personalization - Personalization Engines

[Limbik](https://www.braze.com/docs/partners/message_personalization/dynamic_content/personalization_engines/limbik) is your AI resonance layer—predicting how real audiences interpret and respond to messages, concepts, and AI outputs before they reach the market. Powered by continuous primary research across 60+ countries and 25+ languages, Limbik delivers human-validated synthetic audiences—digital populations that simulate real audience response at machine speed and with research-grade accuracy (95% confidence, 1.5% to 3% margin of error). Limbik gives you the ability to immediately ensure your messaging resonates with what your target audience believes and feels.

#### Linkrunner - Message Orchestration - Attribution

[Linkrunner](https://www.braze.com/docs/partners/message_orchestration/attribution/linkrunner) is a mobile attribution and analytics platform that helps you track and analyze your user acquisition campaigns.

#### Mailizio - Message Orchestration - Templates

[Mailizio](https://www.braze.com/docs/partners/message_orchestration/templates/Mailizio) is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio's integration to Braze, you can export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

#### Open Loyalty - Data and Analytics - Loyalty

[Open Loyalty](https://www.braze.com/docs/partners/data_and_analytics/loyalty/openloyalty) is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user's loyalty status changes.

#### OpenAI - AI Model Provider

[OpenAI](https://www.braze.com/docs/partners/ai_model_providers/openai) creates advanced AI models, like GPT, that enable natural language understanding and generation, empowering brands to build and scale meaningful customer interactions.

#### Shopgate - Channels

[Shopgate](https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/shopgate) is a mobile commerce and omnichannel platform that helps merchants create shopping apps and improve the efficiency of brick-and-mortar stores through fulfillment tools and clienteling, meaning personalized in-store customer support based on customer data.

#### Splio - Data and Analytics - Cohort Import

[Splio](https://www.braze.com/docs/partners/data_and_analytics/cohort_import/splio) is an audience-building tool that lets you increase the number of campaigns and revenue without harming customer experience, and provides analytics to track the performance of CRM campaigns both online and offline.

### SDK

#### SDK breaking updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

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




**February 5, 2026**



## February 5, 2026 release

### BrazeAI<sup>TM</sup>

#### Content Optimizer



[Content Optimizer](https://www.braze.com/docs/user_guide/brazeai/content_optimizer) is a continuous, high-variant content testing Canvas step that delivers automated engagement optimization. Using a drag-and-droppable interface similar to the message step, define the components to test, generate variants using AI (or enter them manually), and use Liquid tags to map these components to your message content.

Built on a non-contextual multi-armed bandit optimizer, Content Optimizer sends a single message per user, determining which combination of component variants to deliver based on predictive recommendations. As the step gathers data over time, high-performing variants naturally increase in send allocation while poor-performing variants decrease. Content Optimizer works best with repeated-send Canvases that have consistent daily user volume (at least a few thousand users per day) to enable continuous optimization.

### Data & Reporting

#### eCommerce recommended events



To match eCommerce recommended events with the existing purchase event, we added the ["Places Order" conversion event](https://www.braze.com/docs/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), which is similar to “Makes Purchase".

### Channels & Touchpoints

#### Translate locales in banners



After adding locales to your workspace, [target users in different languages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#translating-locales) all within a single banner.

#### Configure width for drag-and-drop Content Blocks

[Adjust the width of your Content Block](https://www.braze.com/docs/user_guide/channels/email/drag_and_drop/dnd_editor_blocks/#using-the-editor-to-add-a-content-block) by selecting the button in the navigation menu. The default width is 100% when not specified in your email global style settings; otherwise, the global settings will be honored.

![A double-sided arrow with an option to edit the width.](https://www.braze.com/docs/assets/img_archive/content_block_width_updated.png?14e436ba0d3a6292dd5ef7e526dc2cde){: style="max-width:30%;" }

#### Use automated IP warming



Use [automated IP warming](https://www.braze.com/docs/user_guide/channels/email/email_setup/ip_warming/#automated-ip-warming) to gradually increase your daily send volume, allowing inbox providers to learn and trust your sending patterns. Braze sends to your most engaged subscribers first, which allows daily volume to grow at a pace that matches best practices.

### Partnerships

#### LinkedIn – Canvas Audience Sync

Using the [Braze Audience Sync to LinkedIn](https://www.braze.com/docs/partners/canvas_audience_sync/linkedin_audience_sync/), add user data from your Braze integration to LinkedIn customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria normally used to trigger a message (such as push, email, SMS, and webhook) in a Braze Canvas based on user data can now trigger an ad to that user in your LinkedIn customer lists.

#### Oracle Crowdtwist - Data & analytics

[Oracle Crowdtwist](https://www.braze.com/docs/partners/crowdtwist) is a leading cloud-native customer loyalty solution to empower brands to offer personalized customer experiences. Their solution offers over 100 out-of-the-box engagement paths, providing rapid time-to-value for marketers to develop a more complete view of the customer.

#### Fullstory - Dynamic Content

[Fullstory’s](https://www.braze.com/docs/partners/fullstory/) behavioral data platform helps technology leaders make better, more informed decisions. By injecting digital behavioral data into their analytics stack, Fullstory's patented technology unlocks the power of quality behavioral data at scale–transforming every digital visit into actionable insights. 

#### Open Loyalty - Data & analytics

[Open Loyalty](https://www.braze.com/docs/partners/openloyalty) is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user's loyalty status changes.

#### DOTS.ECO - Extensions

[DOTS.ECO](https://www.braze.com/docs/partners/docs.eco) lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

#### Mailizio - Message orchestration

[Mailizio](https://www.braze.com/docs/partners/mailizio/) is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio's integration to Braze, export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

### APIs

#### Media Library POST APIs



Media Library assets can now be added via API, enabling customers, partners, and agencies to automate more of their message creation workflows. Use the [API](https://www.braze.com/docs/api/endpoints/media_library/manage_assets/create) to upload an asset file directly or copy a file from an existing URL. This feature unlocks integration and automation capabilities.

### Currents and Datashare

#### Agent Console Events for Storage destinations and Datashare



Two new [events](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) are now available for Storage destinations (AWS S3, GCS, and Azure Blob Storage) and Snowflake Datashare: `agentconsole.AgentExecuted` and `agentconsole.ToolInvocation`. These events enable you to analyze Agent Console usage and details in your downstream systems, helping you understand and get the most out of your agent usage. Agents allow you to create and deploy intelligent agents that can perform specific tasks across Braze, including generating content in canvases or catalogs and routing users down different paths based on intelligent decisioning. For more information, see the [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### New 'Retry' events for individual channels



New [retry events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) are now available for email, LINE, push notifications, SMS, webhooks, and WhatsApp channels. These events provide visibility into when frequency capping results in a scheduled message being delayed rather than aborted. When a message is deprioritized or frequency capped, it can now be retried within a configured retry window, giving you better insight into message delivery patterns and frequency capping impacts. For more information, see the [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Add new 'time_ms' field to TokenStateChange event



A new `time_ms` field has been added to the [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) event, providing millisecond-level granularity for tracking push token state changes. This enhanced precision helps you understand the latest status of a push token when multiple changes occur within the same second, giving you confidence in downstream systems that you have the correct subscription status. For more information, see the [Currents changelog](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Send Anonymous user to Tealium Destinations



Events that do not have an external user ID defined can now be streamed to [Tealium](https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents) destinations. When you select the "Include events from anonymous users" checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

##### Send Anonymous user to CustomHTTP Destinations



Events that do not have an external user ID defined can now be streamed to CustomHTTP destinations. When you select the "Include events from anonymous users" checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

#### Email Open event — "machine_open" field

The [Email Open event](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) now generates the "machine_open" field value to report on the [_Machine Open_](https://www.braze.com/docs/user_guide/analytics/reporting/report_metrics#machine-opens) metric. 

### SDK

The following SDK updates have been released. Swift SDK v14.0.1 fixes an issue with the handling of universal links. Android SDK v40.2.0 fixes a potential memory leak and resolves an issue with multiple sessions being opened when transparent activities are present. Expo SDK v3.2.0 adds the `forwardUniversalLinks` option (default: false) to configure the native Swift SDK handling of universal links.

#### SDK breaking updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Renamed `BrazeConfig.Builder.setIsLocationCollectionEnabled()` to `setIsAutomaticLocationCollectionEnabled()`.
    - Renamed `BrazeConfig.isLocationCollectionEnabled` to `isAutomaticLocationCollectionEnabled`.
    - Renamed `BrazeConfigurationProvider.isLocationCollectionEnabled` to `isAutomaticLocationCollectionEnabled`.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)




**January 8, 2026**


## January 8, 2026 release

### Data & Reporting

#### Updates to Currents events



These following changes were made to Currents in Version 4:

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

#### Export sync logs by all rows



In the [Cloud Data Ingestion **Sync Log** dashboard](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), choose to export the row-level logs for a sync run by:

* **Rows with errors:** Downloads a file containing only the rows that had an **Error** status.
* **All rows:** Downloads a file containing every row processed in the run.

### Channels & Touchpoints

#### Bring Your Own (BYO) WhatsApp connector

The [Bring Your Own (BYO) WhatsApp connector](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/byo_connector/) offers a partnership between Braze and Infobip, in which you give Braze access to your Infobip WhatsApp Business Manager (WABA). This allows you to manage and pay for messaging costs directly with Infobip while using Braze for segmentation, personalization, and campaign orchestration. 

#### Banners in Canvas



Select **Banners** as a messaging channel in a [Message step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step) for Canvas. Use the drag-and-drop editor to create personalized inline messages, providing non-intrusive, contextually relevant experiences that update automatically at the start of each user session. 

#### Dynamic BCC



With [dynamic BCC](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/email_preferences/?tab=bcc%20address#dynamic-bcc), use Liquid in your BCC address. Note that this feature is only available in **Email Preferences** and can’t be set on the campaign itself. Only one BCC address per email recipient is allowed.

#### Channel-based rate limits

As an alternative to a rate limit that gets shared across an entire multi-channel campaign or Canvas, select a specific rate limit per channel. In this case, the rate limit will apply to each of your selected channels. For example, set your campaign or Canvas to send a maximum of 5,000 webhooks and 2,500 SMS messages per minute across the campaign or Canvas. For more details, see [Rate limiting and frequency capping](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping).

### Partnerships

#### LILT - Localization

[LILT](https://www.braze.com/docs/partners/lilt/) is the complete AI solution for enterprise translation and content creation. LILT enables global organizations to scale and optimize their content, product, communications, and support operations, with AI agents and fully automated workflows.

### SDK breaking updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Removes News Feed.
        - This fully removes all UI elements, data models, and actions associated with News Feed.
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)




**December 9, 2025**



## December 9, 2025

### Data & Reporting

#### Adding Google Tag Manager to a landing page

To add Google Tag Manager to your landing pages, add a Custom Code block to your landing page in the drag-and-drop editor, then [insert the Tag Manager code](https://www.braze.com/docs/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page) into the block.

### Orchestration

#### SMS Liquid use case

The [Respond with different messages based on inbound SMS keyword](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases#sms-keyword-response) use case incorporates dynamic SMS keyword processing to respond to specific inbound messages with different message copy. For example, you can send different responses when someone texts “START” versus “JOIN”.

#### Allowlisting for Connected Content

You can allowlist specific URLs to be used for [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call). To access this feature, contact your customer success manager.

### Channels & Touchpoints

#### SMS character encoding

Our [SMS segment calculator](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator) now has character encoding! Select **Display Character Encoding** to identify which characters are encoded as GSM-7 or UCS-2. 

![SMS segment calculator with a sample SMS message entered in the textbox and the character encoding turned on.](https://www.braze.com/docs/assets/img/sms/character_encoding.png?9545163f307597e2f6b1b0564c086d5a){: style="max-width:70%;"}

#### WhatsApp messages with optimization

Because MM API for WhatsApp doesn’t offer 100% deliverability, it's important to understand how to retarget users who may not have received your message on other channels. 

To retarget users, we recommend building a segment of users who didn’t receive a specific message. To do this, filter by the error code `131049`, which indicates that a marketing template message was not sent due to WhatsApp’s per-user marketing template limit enforcement. You can do this by [using Braze Currents or SQL Segment Extensions](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Partnerships

#### OtherLevels - Dynamic content

[OtherLevels](https://www.braze.com/docs/partners/otherlevels/) is an experience platform that uses generative AI to transform how sports brands, publishers, and operators connect with their customers by transforming traditional content into on-brand personalized video and rich media experiences at scale.

### SDK

#### SDK breaking updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)




**November 11, 2025**



## November 11, 2025

### Data flexibility

#### `Live Activities Push to Start Registered for App` segmentation filter

The `Live Activities Push to Start Registered for App` filter segments your users by whether they are registered to start a Live Activity through iOS push notifications for a specific app.

#### RFM SQL Segment Extension

You can create an [RFM (recency, frequency, monetary) Segment Extension](https://www.braze.com/docs/rfm_segments/) to target your best users by measuring their purchasing habits.

RFM analysis is a marketing technique that identifies your best users by scoring users on a scale from 0—3 for each category (recency, frequency, monetary), where 3 is the best score and 0 is the worst. Recency, frequency, and monetary values are all based on data from a specific time range of your choosing.

#### Custom attributes — Values 

When viewing a usage report, select the [**Values** tab](https://www.braze.com/docs/user_guide/data/activation/custom_data/custom_attributes/#values-tab) to view the top values of the selected custom attributes based on a sample of approximately 250,000 users.

#### Sync logs and observability for Cloud Data Ingestion



The Cloud Data Ingestion (CDI) [Sync Log dashboard](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs/) allows you to monitor all data processed by CDI, verify whether data was synced successfully, and diagnose any issues with “incorrect” or missing data.

#### Multi-rule feature flag rollouts

Use [multi-rule feature flag rollouts](https://www.braze.com/docs/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) to define a sequence of rules for evaluating users, which allows for precise segmentation and controlled feature releases. This method is ideal for deploying the same feature to diverse audiences.

#### Mapping to catalog fields for drag-and-drop product blocks

In your catalog settings, you can select the **Product blocks** toggle to [map to specific fields](https://www.braze.com/docs/user_guide/messaging/design_and_edit/product_blocks/#catalog-setup) and information in your catalog. This allows you to select which fields to use as the product title, product URL, and image URL.

#### Frequency capping abort events in Currents

When using Currents, you can now reference `abort_type` in the channel abort events. This identifies that a message has been aborted due to frequency capping and includes which frequency capping rule caused the abort. This helps inform how you set up your frequency capping rules. Refer to [Message engagement events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) for specific Currents event details.

### Robust channels

#### Background row images 



You can [add a background row image](https://www.braze.com/docs/user_guide/channels/in_app_messages/customize/style_settings/#background-image) to an in-app message or landing page in the **Row properties** panel. Toggle on **Background image**, and then provide an image URL or select an image from the [media library](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library/). Finally, configure your alt text, size, position, and whether the image repeats to create patterns across the row.

![A row background image of a pizza that has a horizontal repeat pattern.](https://www.braze.com/docs/assets/img_archive/background_row.png?7eb107ac958fdbf5ea9dca2fd0724fd0)

#### Copy preview link

Use **Copy preview link** in your [Banners](https://www.braze.com/docs/user_guide/channels/banners/create_a_banner/#step-5-test-your-message-optional), [email custom footers](https://www.braze.com/docs/user_guide/channels/email/customize/custom_email_footer/#creating-your-custom-footer), and [email opt-in and unsubscribe pages](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/email_preferences/?tab=custom%20footer#subscription-pages-and-footers) to generate a shareable link that shows how your content will look like for a random user.

#### WhatsApp messages with optimized delivery

Use Meta’s advanced AI systems to deliver your marketing messages to more users who are most likely to engage with them, significantly boosting deliverability and message engagement.

[WhatsApp messages with optimized delivery](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery/) are sent using Meta's new [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/), which provides superior performance compared to the traditional Cloud API. This new sending pipeline helps you better reach users who value and want to receive your messages.

#### WhatsApp Flows

When incorporating a WhatsApp Flow message into a Braze Canvas or campaign, you may want to capture and utilize specific information that users submit through the Flow. Braze needs to receive additional information regarding the structure of the user response, specifically the expected shape of the JSON response, to generate the required nested custom attribute (NCA) schema.

Now you can give Braze the information about the response structure by [saving the Flow response as a custom attribute](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) and completing a test send.

#### Editable user preview

You can [edit individual fields from a random or existing user](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook#customizing-an-existing-user) to help test dynamic content within your message. Select **Edit** to convert the selected user into a custom user you can modify.

![The "Preview as a User" tab with an "Edit" button.](https://www.braze.com/docs/assets/img_archive/edit_user_preview.png?01261cefe71937167833dfcc6ecdf35c){: style="max-width:50%;"}

### AI and ML automation

#### BrazeAI Decisioning Studio™ Go

You can now set up your integration with [BrazeAI Decisioning Studio™ Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/) by referencing these configuration articles for:

- [Braze](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Klaviyo](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Salesforce Marketing Cloud](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)

#### New features for Braze Agents



You can now customize your [Braze Agent](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents) by:

- Applying [brand guidelines](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/brand_guidelines) for your agent to adhere to in its response. 
- Referencing a catalog to further personalize your message.
- Structuring an agent's output by providing the [output format](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents/#output-format).
- Adjusting the [temperature](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents/#temperature) for the level of deviation for your agent's output.

### ChatGPT models with BrazeAI Operator<sup>TM</sup>



You can select from these GPT models to use for different request types with [Operator](https://www.braze.com/docs/user_guide/brazeai/operator):

- GPT-5 nano
- GPT-5 mini (default)
- GPT-5

### New Braze partnerships

#### StackAdapt - Advertising

[StackAdapt](https://www.braze.com/docs/partners/stackadapt/) is an AI-powered marketing platform that delivers targeted performance-driven advertising. It allows you to sync user profile data from Braze into the StackAdapt Data Hub. By connecting the two platforms, you can create a unified view of your customers and activate first-party data to improve ad performance.

#### Cloudinary - Dynamic content

[Cloudinary](https://www.braze.com/docs/partners/cloudinary/) is an image and video platform that empowers you to manage, edit, optimize, and deliver images and video on a massive scale to any campaign across channels and customer journeys. When integrated and enabled, Cloudinary's media management will power and provide dynamic, contextual, and personalized asset delivery for your Braze campaigns and Canvases.

#### Kameleoon - A/B testing

[Kameleoon](https://www.braze.com/docs/partners/kameleoon/) is an optimization solution with experiment, AI-powered personalization, and feature management capabilities in a single unified platform.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Fixes the Typescript type for the callback of `subscribeToInAppMessage` and `addListener` for `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - These listeners now properly return a callback with the new `InAppMessageEvent` type. Previously, the methods were annotated to return a `BrazeInAppMessage` type, but it was actually returning a `String`.
         - If you are using either subscription API, ensure that the behavior of your in-app messages are unchanged after updating to this version. See our sample code in `BrazeProject.tsx`.
    - The APIs `logInAppMessageClicked`, `logInAppMessageImpression`, and `logInAppMessageButtonClicked` now accept only a `BrazeInAppMessage` object to match its existing public interface.
        - Previously, it would accept both a `BrazeInAppMessage` object as well as a `String`.
    - `BrazeInAppMessage.toString()` now returns a human-readable string instead of the JSON string representation.
        - To get the JSON string representation of an in-app message, use `BrazeInAppMessage.inAppMessageJsonString`.
    - On iOS, `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` has been moved to `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - This new method is a now a class method instead of an instance method.
    - Adds nullability annotations to `BrazeReactUtils` methods.
    - Removes the following deprecated methods and properties from the API:
        - `getInstallTrackingId(callback:)` in favor of `getDeviceId`.
        - `registerAndroidPushToken(token:)` in favor of `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` in favor of `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` in favor of `payload_type`.
        - `PushNotificationEvent.deeplink` in favor of `url`.
        - `PushNotificationEvent.content_text` in favor of `body`.
        - `PushNotificationEvent.raw_android_push_data` in favor of `android`.
        - `PushNotificationEvent.kvp_data` in favor of `braze_properties`.
    - Updates the native Android SDK version bindings [from Braze Android SDK 39.0.0 to 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [.NET MAUI (Xamarin) SDK Version 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Updated the iOS binding [from Braze Swift SDK 12.1.0 to 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). This includes Xcode 26 support.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Updates the native Android bridge [from Braze Android SDK 39.0.0 to 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)




**October 14, 2025**



## October 14, 2025 release

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) replaces A/B testing with AI decisioning that personalizes everything, and maximizes any metric: drive dollars, not clicks. With BrazeAI Decisioning Studio™, you can optimize any business KPI. Refer to our dedicated section [BrazeAI Decisioning Studio™](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) for sample use cases and key features.

### Data flexibility

#### New Currents events

These new events were added to the [Currents glossary](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events):

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

These new fields were added to the following Currents events:

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`: 
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`: 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Suppression lists



[Suppression lists](https://www.braze.com/docs/user_guide/audience/suppression_lists/) are groups of users who automatically do not receive any campaigns or Canvases. Suppression lists are defined by segment filters, and users enter and exit suppression lists as they meet filter criteria.

#### Zero-copy personalization



Sync Canvas triggers using Cloud Data Ingestion for [zero-copy personalization](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). This feature accesses user-specific information from your data storage solution and passes it to a destination Canvas. Canvas steps can optionally include personalization fields that are not persisted on Braze user profiles.

#### Canvas Context variables for Audience Paths and Decision Split steps



You can [create context variable filters](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#context-variable-filters) that use previously-declared context variables in [Audience Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/audience_paths) and [Decision Split](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/decision_split) steps.

### Unlocking creativity

#### Deal Cards for emails

Use [Deal Cards](https://www.braze.com/docs/user_guide/channels/email/html_editor/gmail_promotions_tab) to provide key deal information directly at the top of email bodies. This allows recipients to quickly understand the offer details and take action.

#### Templates for Banners

When you [compose your Banner](https://www.braze.com/docs/user_guide/channels/banners/create_a_banner/), you can now start with a blank template, use a Braze template, or select a saved Banner template.

### Robust channels

#### Suppression lists


 
[Suppression lists](https://www.braze.com/docs/user_guide/audience/suppression_lists/) specify groups of users who will never receive messages. Admins can create suppression lists with segment filters to narrow down a user group the same way you would for segmentation.

#### LINE click tracking



When [LINE click tracking](https://www.braze.com/docs/line/click_tracking/) is turned on, Braze automatically shortens your URLs, adds tracking mechanisms, and records clicks in real time. While LINE offers aggregate click data, Braze provides granular user information that is timely and actionable. This data empowers you to create more targeted segmentation and retargeting strategies, such as segmenting users based on click behavior and triggering messages in response to specific clicks.

#### SMS and RCS bot click filtering



[SMS and RCS bot click filtering](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering/) enhances campaign analytics and workflows by excluding suspected bot clicks. A “bot click” refers to automated clicks on shortened links in SMS and RCS messages, such as those from web crawlers, Android and iOS link previews, or CPaaS security software. This feature facilitates accurate reporting, segmentation, and orchestration to engage real users.

#### Transfer WhatsApp phone numbers

Transfer a WhatsApp Business Account (WABA) phone number and its associated subscription group [from one workspace to another](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/transfer_between_workspaces/) within Braze.

#### WhatsApp Flows response messages and preview

In a Canvas, you can create a WhatsApp message step that uses a [response message](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) and flow message. You can also select **Preview Flow** to preview the Flow directly in Braze to confirm it behaves as expected.

#### WhatsApp product messages

[Product messages](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/product_messages/) empower you to send interactive WhatsApp messages that showcase products directly from your Meta catalog.

#### Integrating Braze and WhatsApp with an external system

[Leverage the power of AI chatbots and live agent hand-offs](https://www.braze.com/docs/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems/) on the WhatsApp channel to streamline your customer support operations. By automating routine inquiries and seamlessly transitioning to human agents when needed, you can significantly improve response times and enhance the overall customer experience.

### AI and ML automation

#### Braze Agents



[Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents/) are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences.

### New Braze partnerships

#### Jasper - Templates

The [Jasper](https://www.braze.com/docs/partners/jasper/) integration with Braze empowers you to streamline content creation and campaign execution. With Jasper, your marketing teams can generate high-quality, on-brand copy in minutes. Braze then facilitates the delivery of these messages to the right audience at the optimal time. This integration fosters seamless workflows, reduces manual effort, and drives stronger engagement outcomes.

#### Swym - Loyalty and retargeting

[Swym](https://www.braze.com/docs/partners/swym/) helps eCommerce brands capture shopping intent with Wishlists, Save for Later, Gift Registry, and Back-in-Stock alerts. Using rich, permission-based data, you can craft hyper-targeted campaigns and deliver personalized shopping experiences that drive engagement, boost conversions, and increase loyalty.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; you can find all other updates by checking the corresponding SDK changelogs.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Updated the native Android bridge [from Braze Android SDK 37.0.0 to 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The minimum required GradlePluginKotlinVersion is now 2.1.0.
    - Updated the native iOS bridge [from Braze Swift SDK 12.0.0 to 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). This includes Xcode 26 support.
    - Removes support for News Feed. The following APIs have been removed:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Updates the native Android SDK version bindings [from Braze Android SDK 37.0.0 to 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Removes support for News Feed. The following APIs have been removed:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Updated the native iOS bridge [from Braze Swift SDK 12.0.0 to 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). This includes Xcode 26 support.



**September 16, 2025**



## September 16, 2025 release

### Data flexibility

#### Braze Data Platform

Braze Data Platform is a set of comprehensive, composable set of data capabilities and partner integrations that empowers you to create personalized, impactful experiences across the customer lifecycle. Learn more about the three data related jobs to be done: 

- [Data unification](https://www.braze.com/docs/user_guide/data/unification)
- [Data activation](https://www.braze.com/docs/user_guide/data/activation)
- [Data distribution](https://www.braze.com/docs/user_guide/data/distribution)

#### Custom Banner properties



You can use custom properties from your Banner campaign to retrieve key–value data through the SDK and modify your app’s behavior or appearance. To learn more, see [Custom Banner properties](https://www.braze.com/docs/developer_guide/banners/placements/#custom-properties).

#### Token authentication



When using Braze Connected Content, you may find that certain APIs require a token instead of a username and password. Braze can store credentials that hold [token authentication header values](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-token-authentication).

#### Promotion codes

You can save promotion codes to a user’s profile through a User Update step. For more information, refer to [Saving promotion codes to user profiles](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes#save-to-profile).

### Unlocking creativity

#### Braze Pilot

[Braze Pilot](https://www.braze.com/docs/user_guide/get_started/braze_pilot/) is a publicly available app for Android and iOS that allows you to launch messages from your Braze dashboard to your phone. Check out [Getting started with Braze Pilot](https://www.braze.com/docs/user_guide/get_started/braze_pilot/getting_started/) for a walkthrough of downloading the app, initializing the connection to your Braze dashboard, and completing the setup.

### New Braze partnerships

#### Blings - Visual and interactive content

[Blings](https://www.braze.com/docs/partners/blings/) is a next-generation personalized video platform that enables you to deliver real-time, interactive, and data-driven video experiences across channels at scale.

#### Shopify standard integration with third-party tool

For Shopify online stores, we recommend using Braze’s standard integration method to support the Braze SDKs on your site.

However, we understand that you may prefer using a third-party tool, like Google Tag Manager, so we put together a guide on how you can. To get started, see [Shopify: Third-party tagging](https://www.braze.com/docs/shopify_standard_integration_third_party_tagging/).

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Updates the native Android bridge from Braze Android SDK `36.0.0` to `39.0.0`.
    - Updates the native iOS bridge from Braze Swift SDK `12.0.0` to `13.2.0`. This includes Xcode 26 support.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Updates the Braze Swift SDK bindings to require releases from the `13.0.0+` SemVer denomination. This allows compatibility with any version of the Braze SDK from `13.0.0` up to, but not including, `14.0.0`.



**August 19, 2025**



## August 19, 2025 release

### Time zone consistency standardization to Canvas Context



If you're participating in the [Canvas Context step early access](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context), all timestamps with a datetime type from trigger event properties in action-based Canvases will always be normalized to [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). To learn more about this, refer to [Time zone consistency standardization](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context#time-zone-consistency-standardization).

### Data flexibility

#### Self-serve custom domains



[Self-serve custom domains](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains/) empower you to configure and manage your own custom domains for SMS, RCS, and WhatsApp—directly from your Braze dashboard. You can easily add, monitor, and manage up to 10 custom domains in one place.

#### Segment funnel statistics

Select [View funnel statistics](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment/#viewing-funnel-statistics) to display the statistics for that filter group and see how each added filter impacts your segment statistics. You’ll see an estimated count and percentage for users who are targeted by all filters up to that point. Once the statistics are displayed for a filter group, they will update automatically whenever you change the filters. 

#### New response fields for `/campaigns/details` endpoint for push notifications

The `messages` response for push notifications now includes two new fields:

- `image_url`: An image URL for an Android notification image, an iOS notification image, or a web push icon image.
- `large_image_url`: A web notification image URL for Android Chrome and Windows web push actions.

#### Defining PII fields

Selecting and [defining certain fields as PII fields](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings#view-pii) only affects what Users can view on the Braze dashboard and does not impact how the End User data in such PII fields is handled.

Consult your legal team to align your dashboard’s settings with any privacy regulations and policies applicable to your company, including those related to [data retention](https://www.braze.com/docs/api/data_retention/).

#### Sharing a Report Builder download link

You can [share a dashboard link](https://www.braze.com/docs/user_guide/analytics/reporting/report_builder/#sharing-a-report) to the report by selecting **Share** and then **Share a link** or **Send or schedule an email**.

### Unlocking creativity

#### Custom head tags for drag-and-drop emails

Use `<head>` tags to add CSS and metadata in your email message. For example, you can use these tags to add a stylesheet or favicon. Liquid is supported in `<head>` tags.

### Robust channels

#### Fuzzy out-out best practices

We've added a [best practices section](https://www.braze.com/docs) to help you thoughtfully configure your fuzzy opt-out message and create a clear, compliant, and positive experience for your subscribers.

#### WhatsApp Flows



[WhatsApp Flows](https://www.braze.com/docs/whatsapp_flows/) is an enhancement to the existing WhatsApp channel, allowing you to create interactive and dynamic messaging experiences. 

#### WhatsApp inbound product questions

Users can respond to your product or catalog message with [product questions](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/product_messages/#receiving-inbound-product-questions). These arrive as inbound messages, which can then be sorted with an Action Path.

Additionally, Braze extracts the product ID and catalog ID from these questions, so if you wish to automate responses or send questions to another team (such as customer support), you can include those details.

### AI and ML automation

#### New BrazeAI™ use case articles

We’ve added new use case articles to help you get the most out of BrazeAI™. These guides highlight practical ways to apply AI to your engagement strategies, including:

- [Predictive Churn](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_churn/use_case/): Identify customers at risk of churning and take action early.
- [Predictive Events](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_events/use_case/): Anticipate key user actions and shape experiences in real time.
- [Recommendations](https://www.braze.com/docs/user_guide/brazeai/recommendations/use_case ): Deliver more relevant content and products based on customer behavior.

#### MCP server



The [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server/), a secure and read-only connection, lets AI tools like Claude and Cursor access non-PII Braze data to answer questions, analyze trends, and provide insights without altering data.

### SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Extends the functionality of `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` to be triggered for "Optional" authentication errors.
        - The delegate method `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` will now be triggered for both "Required" and "Optional" authentication errors.
        - If you want to only handle "Required" SDK authentication errors, add a check ensuring that `BrazeSDKAuthError.optional` is false inside your implementation of this delegate method.
    - Fixes the usage of `Braze.Configuration.sdkAuthentication` to take effect when enabled.
        - Previously, the value of this configuration was not consumed by the SDK and the token was always attached to requests if it was present.
        - Now, the SDK will only attach the SDK authentication token to outgoing network requests when this configuration is enabled.
    - The setters for all properties of `Braze.FeatureFlag` and all properties of `Braze.Banner` have been made `private`. The properties of these classes are now read-only.
    - Removes the `Braze.Banner.id` property, which was deprecated in version `11.4.0`.
        - Instead, use `Braze.Banner.trackingId` to read a banner's campaign tracking ID.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Updates the native Android SDK version bindings from [Braze Android SDK 36.0.0 to 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updates the native Swift SDK version bindings from [Braze Swift SDK 12.0.0 to 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - The `sdkAuthenticationError` event will now trigger for both "Required" and "Optional" authentication errors.
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Added support for .NET 9.0 for the iOS and Android bindings.
        - This removes support for .NET 8.0.
        - This requires a [minimum version of iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Updated the Android binding from [Braze Android 32.0.0 to 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the iOS binding from [Braze Swift SDK 10.0.0 to 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - This release contains APIs for the Banners feature but is not currently fully supported by this SDK. If you wish to use Banners in your .NET MAUI app, contact your customer support manager before integrating into your application.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Updated the internal iOS implementation of `enableSdk` method to use `setEnabled`: instead of `_requestEnableSDKOnNextAppRun`, which was deprecated in the Swift SDK.
    - Calling this method no longer requires the app to be re-launched to take effect. The SDK will now become enabled as soon as this method is executed.
    - Updated the native Android bridge from [Braze Android SDK `36.0.0` to `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).



