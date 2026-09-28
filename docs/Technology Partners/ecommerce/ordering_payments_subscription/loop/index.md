# Loop

> [Track by Loop](https://www.loopreturns.com/track/) is Loop's tracking product for eCommerce customers. It follows packages across carriers, normalizes fulfillment statuses, and sends those events to Braze for messaging.

_This integration is maintained by Track by Loop._

## About the integration

When a shipping event occurs (for example, shipment created, in transit, out for delivery, delivered, or stalled), Track by Loop calls the Braze REST API to trigger an [API-triggered campaign](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) or [API-triggered Canvas](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases). Each call includes shipment and order properties you can use for Liquid personalization. Braze remains the system of record for eligibility, frequency capping, and message delivery across the channels you configure.

## Use cases

- Send shipping updates such as "your order is on the way," "out for delivery," and "delivered," with tracking number, carrier, ETA, and a branded tracking URL.
- Trigger stalled-shipment or delivery-error Canvases so support and retention teams can respond to where-is-my-order tickets.
- Promote replenishment, reviews, or related products when a package is delivered or arriving soon.
- Enter a Canvas from the same Track by Loop event and branch into email, SMS, or push based on subscription state.

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A Track by Loop account | A Track by Loop account is required for this integration. |
| A Braze REST API key | A Braze REST API key with `campaigns.trigger.send`, `canvas.trigger.send`, or both permissions. Create this key in the Braze dashboard from **Settings** > **APIs and Identifiers** > **API Keys**. For more information, see [Creating REST API keys](https://www.braze.com/docs/api/basics#creating-rest-api-keys). |
| A Braze REST endpoint | Your workspace REST endpoint (origin only), for example `https://rest.iad-01.braze.com`. The host must match your Braze cluster (`*.braze.com` or `*.braze.eu`). For more information, see [REST API endpoints](https://www.braze.com/docs/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Create API-triggered campaigns or Canvases in Braze

1. In Braze, create a campaign or Canvas for each fulfillment moment you plan to message (for example, Delivered).
2. Set delivery to **API-triggered**. For more information, see [API-triggered delivery](https://www.braze.com/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).
3. Build message copy with Liquid personalization for order, tracking, and consumer data, including a deep link to the tracking page. Reference trigger properties with `{{api_trigger_properties.${your_property}}}`.
4. Copy the [API identifier](https://www.braze.com/docs/api/identifier_types) for that campaign or Canvas. You enter this value in Track by Loop in a later step.

### Step 2: Connect credentials in Track by Loop

1. In Track by Loop, go to **Settings** > **Integrations** > **Braze**.
2. Enter your REST endpoint (origin only), for example `https://rest.iad-01.braze.com`.
3. Paste your REST API key.
4. Select **Save credentials**.

### Step 3: Map fulfillment events

Under **Event mappings**, each row is a Track by Loop fulfillment event. These are the same events Track by Loop uses for other marketing integrations.

For each event:

1. Select **Campaign** or **Canvas**.
2. Paste the Braze API identifier for the campaign or Canvas you created.
3. Save the row.

## Customization

### Choose campaign or Canvas per event

Use a campaign when a single message is enough. Use a Canvas when you need delays, channel fallback, or branching (for example, SMS if the consumer is not subscribed to email). Track by Loop stores one mapping per event as either a campaign or a Canvas.

## Using this integration

Track by Loop targets one recipient per event:

1. If a Shopify customer ID is present, Track by Loop sets `external_user_id` in the recipient object to that ID as a string. This matches customers who set the Braze `external_id` to the Shopify customer ID.
2. If no customer ID is available, Track by Loop sets `email` on the recipient object and uses Braze email [prioritization](https://www.braze.com/docs/api/endpoints/user_data/post_user_identify#identifying-users-by-email-addresses-and-phone-numbers) of `unidentified`, then `most_recently_updated`.

The consumer must already have a Braze profile reachable by that identifier.

## Test the connection

On the Braze integration settings page in Track by Loop, send a test event to confirm your campaign or Canvas mapping.

1. Under **Test connection**, select **Campaign** or **Canvas**.
2. Paste the API identifier of an active API-triggered campaign or Canvas.
3. Enter a test recipient email for a Braze user who already exists and can receive that channel.
4. Select **Send test trigger**.
