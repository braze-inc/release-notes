# RudderStack

> [RudderStack](https://rudderstack.com/) is a customer data platform for developers that collects and routes customer event data to your data warehouse and dozens of other tools, including Braze. It offers native SDKs for web and mobile, server-side libraries for your backend, and a transformation framework for shaping event data in flight.

The Braze and RudderStack integration gives you a native SDK integration for your Android, iOS, and web applications, plus a server-to-server integration from your backend services — so you can send user attributes, custom events, and ecommerce events to Braze from every surface through one pipeline.

This integration is maintained by RudderStack.

## About this integration

RudderStack sits upstream of Braze as your event collection and routing layer. You instrument your apps and services once with RudderStack, then fan the same event stream out to Braze alongside your warehouse and other destinations — without adding another SDK or tracking plan per tool.

For a marketer, this means the user attributes, behavioral events, and purchase or ecommerce activity you segment and message on in Braze arrive already standardized and governed. Because RudderStack also lands the same events in your warehouse, the audiences you build in Braze stay consistent with the numbers your data team reports.

## Use cases

- **Unified cross-platform profiles:** Send identify traits from web, iOS, Android, and your backend into a single Braze user profile, using externalId to align Braze identity with your system of record.
- **Ecommerce lifecycle messaging:** Map standard RudderStack ecommerce events to [Braze recommended ecommerce events](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/) to power abandoned-cart, post-purchase, refund, and cancellation campaigns.
- **Warehouse-driven personalization:** Use RudderStack Reverse ETL to push computed traits and model outputs from your warehouse into Braze as custom attributes for segmentation.
- **Data point cost control:** Turn on trait deduplication so RudderStack sends only changed attributes to Braze, reducing data point consumption.
- **Governed consent and filtering:** Apply OneTrust consent categories and event filtering before data reaches Braze.

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A RudderStack account | A [RudderStack account](https://app.rudderstack.com/) is required to take advantage of this partnership. |
| A configured source | A [source](https://www.rudderstack.com/docs/dashboard-guides/sources/) is the origin of any data sent to RudderStack, such as a website, mobile app, or backend server. Configure a source before setting up Braze as a destination. |
| A Braze REST API key | A Braze REST API key with the following [permissions](https://www.braze.com/docs/api/basics/#rest-api-key-permissions):<br>- `users.track`<br>- `users.identify`<br>- `users.delete`<br>- `users.alias.new`<br>- `users.merge`<br>- `users.export.ids`<br><br>Create this key in the Braze dashboard from **Settings** > **APIs and Identifiers** > **API Keys**. |
| A Braze Default App Identifier Key | In the Braze dashboard, go to **Settings** > **APIs and Identifiers** > **App Identifiers** and copy the identifier for your app. |
| A Braze data center | Your [data center](https://www.braze.com/docs/user_guide/data/data_centers/) aligns with your Braze dashboard [instance](https://www.braze.com/docs/api/basics/#endpoints). RudderStack lists the [supported data centers](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#supported-braze-data-centers). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

## Integrate RudderStack

### Step 1: Add a source in RudderStack

1. Log in to your [RudderStack dashboard](https://app.rudderstack.com/).
2. Set up the source you want to send data from — for example, a [JavaScript](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/), iOS, Android, or server-side source.
3. Open the **Overview** tab of your source and select **Add Destination > Create new destination**.

### Step 2: Configure Braze as a destination

1. Select **Braze** from the list of destinations, then click **Continue**.
2. Enter a destination name.
3. Under **Connection settings**, provide your **Default App Identifier Key**, **REST API Key**, and **Data Center**.
4. Optionally turn on **Enable Platform-specific App Identifier Keys** (Beta) to supply separate Android, iOS, and web app identifier keys for accurate attribution in Braze. This applies to device and hybrid mode only, and requires a minimum device mode integration version — see [how API key selection works](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/device-mode/#how-api-key-selection-works).

### Step 3: Choose the connection mode

Choose how RudderStack delivers events to Braze:

- [**Device mode**](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/device-mode/) (side-by-side): RudderStack loads the Braze native SDK and sends event data to Braze directly from your client (browser or mobile app).
- [**Cloud mode**](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/) (server-to-server): The RudderStack SDK sends event data to the RudderStack server, which transforms it and routes it to Braze.
- [**Hybrid mode**](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/hybrid-mode/): Send iOS and Android auto-generated and user-generated events to Braze over a single connection.

For device mode, add the Braze integration for your platform to your project:

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

In hybrid mode, RudderStack initializes the Braze SDK, sends all user-generated events (identify, track, page, screen, group) through cloud mode, and sends auto-generated events that require the Braze SDK — such as in-app messages and push notifications — through device mode.

Learn more about RudderStack's [connection modes](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) and the benefits of each.

## Customize RudderStack

### Step 1: Configure event settings

In the RudderStack dashboard, under the Braze destination's [event settings](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#event-settings):

1. **Enable ecommerce recommended events** (Beta): Maps RudderStack ecommerce track events to Braze recommended ecommerce events (ecommerce.*). This setting is turned on by default. See [Send ecommerce events to Braze](#send-ecommerce-events-to-braze) for more information.
2. **Enable subscription groups in group call**: Sends the subscription group status in your group events. Cloud mode only.
3. **Use Custom Attributes Operation**: Lets you use Braze's [nested custom attributes](https://www.braze.com/docs/user_guide/data/activation/attributes/nested_custom_attribute_support/) to create segments and personalize messages using a custom attribute object. Cloud mode only.

### Step 2: Configure deduplication settings

1. Turn on **Deduplicate Traits** in the Braze destination's [deduplication settings](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#deduplication-settings).
2. Make sure your REST API key includes the `users.export.ids` permission.

RudderStack then sends only changed or modified user attributes to Braze, reducing [data point](https://www.braze.com/docs/user_guide/data_and_analytics/data_points/) consumption. This works in both cloud mode and device mode, and for Reverse ETL sources. See [User Trait Deduplication in Braze](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/).

**Note:**


Deduplication is available on the RudderStack [Growth and Enterprise](https://www.rudderstack.com/pricing/) plans. In cloud mode it uses the Braze [`/users/export/ids`](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier/) endpoint, which is rate limited. If the limit is exceeded, RudderStack sends all attributes without deduplication until volume returns below the limit.



### Step 3: Configure web SDK and other settings

For [web device mode](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode), configure the following [web SDK settings](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#web-sdk-settings):

- **Show Braze logs**: Shows Braze logs to your users.
- **Use web push notifications**: Enables web push. Requires a service worker on your site.
- **Enable HTML in-app messages**: Enables HTML in-app messages.
- **Track events for anonymous users**: Tracks anonymous user activity and sends it to Braze.

Under [other settings](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#other-settings):

- **Client-side Events Filtering**: Specifies which events are blocked or allowed to flow to Braze. See [Client-side Events Filtering](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **OneTrust Cookie Categories**: Associates [OneTrust](https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/) cookie consent groups with Braze.

**Note:**


In web device mode, RudderStack loads the Braze native SDK from https://js.appboycdn.com/. Depending on your site's content security policy, you may need to allowlist this domain.



## Use RudderStack with Braze

### Step 1: Map RudderStack methods to Braze

Braze supports the RudderStack identify, track, screen, page, group, and alias methods.

| Method | Behavior in Braze |
| --- | --- |
| [identify](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#identify) | Creates or updates a Braze user profile with a unique user ID and optional traits such as name, email, and phone. Use the [externalId field](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#set-a-custom-user-id-externalid) to explicitly set a custom Braze user ID; Braze prefers externalId and falls back to userId. |
| [track](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#track) | Records user actions as Braze custom events, along with their properties. |
| [page](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#page) | Records website page views and related page information. |
| [screen](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#screen) | Records mobile screen views and related screen information. |
| [group](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#group) | Associates a user with a group by sending a custom attribute named `ab_rudder_group_<groupId>` set to true. To update [subscription group](https://www.braze.com/docs/api/endpoints/subscription_groups/) status, turn on **Enable subscription groups in group call** and send the status in the group call — either email or phone is required. |
| [alias](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#alias) | Merges different identities of a known user. Supported in cloud mode only. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RudderStack methods in Braze" }

**Deleting a user**

Delete a user in Braze using the [Suppression with Delete regulation](https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation) of the RudderStack [User Suppression API](https://www.rudderstack.com/docs/api/user-suppression-api/). Your REST API key must include the `users.delete` permission. RudderStack forwards the deletion request but does not guarantee deletion within a 30-day window — confirm fulfillment with Braze.

**Nested custom attributes**

With **Use Custom Attributes Operation** turned on, you can send user traits as [nested custom attributes](https://www.braze.com/docs/user_guide/data/activation/attributes/nested_custom_attribute_support/) and perform add, update, and remove operations on them. `identifier` is required for update and remove. If no operation is specified, RudderStack uses create. Set `mergeObjectsUpdateOperation` to true in the event's properties to deep merge updates.

See [Send user traits as nested custom attributes](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/#send-user-traits-as-nested-custom-attributes) for more information.

### Step 2: Send ecommerce events to Braze {#send-ecommerce-events-to-braze}

When **Enable ecommerce recommended events** (Beta) is turned on, RudderStack maps supported [RudderStack ecommerce](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) track events to [Braze recommended ecommerce events](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/) (ecommerce.*):

| RudderStack event | Braze event | action |
| --- | --- | --- |
| Product Viewed | ecommerce.product_viewed | — |
| Product Added | ecommerce.cart_updated | add |
| Product Removed | ecommerce.cart_updated | remove |
| Checkout Started | ecommerce.checkout_started | — |
| Order Completed | ecommerce.order_placed | — |
| Order Refunded | ecommerce.order_refunded | — |
| Order Cancelled | ecommerce.order_cancelled | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RudderStack to Braze ecommerce events mapping" }

Event names are matched after trimming whitespace and ignoring case, so `order completed` and `Order Completed` both map. The mapping is identical in cloud mode and device mode. In hybrid mode, user-generated track events are sent through cloud mode, so the same mapping applies.

**Important:**


When this setting is turned on, `Order Completed` is sent as one `ecommerce.order_placed` custom event per order instead of Braze [purchases](https://www.braze.com/docs/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data). Rebuild your Braze purchase and revenue analytics and **Made Purchase** segments against `ecommerce.order_placed`. To keep the legacy purchase mapping, turn **Enable ecommerce recommended events** off.



For the complete [field mappings](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/recommended-ecommerce-events/#field-mappings), per-product properties, automatic fields (source, action, metadata), and payload examples, see [Braze Recommended Ecommerce Events](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/recommended-ecommerce-events/).

## Considerations

**Ecommerce event validation:** Braze requires certain fields for commerce handling. RudderStack's behavior when one is absent:

| Scenario | Behavior |
| --- | --- |
| Required field missing | RudderStack still sends the event, with the field absent. A required field sent as `null`, `""`, `{}`, or `[]` is scrubbed from the payload and treated the same as a missing field. |
| Braze rejects the event | Braze returns errors for such events — RudderStack also shows these events as aborted. |
| Device mode | The RudderStack SDK logs a warning listing the missing fields in the browser console, Logcat, or Xcode console depending on your SDK log level. |
| Cloud mode | An event that Braze rejects is discarded and counted as a failed delivery on the destination [Events](https://www.rudderstack.com/docs/dashboard-guides/event-metrics/destinations/#event-details) tab in RudderStack. Click the event row in the **Event details** table to see the Braze error and a sample payload. |
| Type mismatches | Handled on the same path. RudderStack applies lossless type coercion where possible — numeric strings become numbers for float fields, integral strings become integers. A value that cannot be coerced without loss is sent as-is. In device mode, the SDK logs a type-mismatch warning. In cloud mode, an event Braze rejects for a type mismatch is discarded. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ecommerce event validation behavior" }

- **Batching and MAU rate limits:** For accounts on Braze [Monthly Active Users pricing plans](https://www.braze.com/docs/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau), RudderStack batches identify and track events at 75 events per batch. Accounts not on MAU plans use 225 events per batch.
- **Braze UI features:** The server-to-server (cloud mode) integration does not support Braze UI features such as push notifications or in-app messaging. These are supported by the device mode integration.
- **Server-side SDKs:** RudderStack's server-side SDKs (Java, Python, Node.js, Go, Ruby, PHP, .NET, Rust) support cloud mode only, because they run in your backend and cannot load the Braze SDK.
- **Flutter and React Native device mode:** Device mode support for Flutter and React Native applies to Android and iOS only. For a Flutter web build, use cloud mode, or create a separate RudderStack JavaScript source and use its write key for the web build.

## Troubleshooting

### My ecommerce events are failing in cloud mode

In cloud mode, an event that Braze rejects is discarded and counted as a failed delivery. Open the destination **Events** tab in RudderStack, click the event row in the **Event details** table, and review the Braze error and sample payload.

See [Missing required fields](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/recommended-ecommerce-events/#missing-required-fields) for more information.

### My Braze purchase and revenue reports stopped populating

**Enable ecommerce recommended events** is turned on, so `Order Completed` is sent as an `ecommerce.order_placed` custom event instead of a Braze purchase. Rebuild your purchase and revenue analytics and **Made Purchase** segments against `ecommerce.order_placed`, or turn the setting off to restore the legacy purchase mapping.

### I see "[Braze Deduplication]: Duplicate user detected, the user is dropped" in RudderStack logs

This message comes from RudderStack when **Deduplicate Traits** is turned on and RudderStack drops unchanged user traits before forwarding to Braze. It is not a Braze error.

RudderStack compares incoming identify and track traits against the user profile and skips attributes with no delta, reducing Braze data point usage. If you need every trait sent on each call, turn off **Deduplicate Traits** in your RudderStack Braze destination settings — be aware this can increase data point consumption.

See [User Trait Deduplication in Braze](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/) for more details.

### Some custom attributes are not deduplicated even though their values have not changed

Make sure the data type of each custom attribute sent in your events matches the type configured in the Braze dashboard, and that dates and timestamps use a Braze-supported format. Otherwise, deduplication will not work correctly.

