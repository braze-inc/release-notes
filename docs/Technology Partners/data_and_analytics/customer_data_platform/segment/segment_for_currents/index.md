# Segment for Currents  

> [Segment](https://segment.com) is a customer data platform that helps you collect, clean, and activate your customer data. This reference article will give an overview of the connection between Braze Currents and Segment and describe requirements and processes for proper implementation and usage.

The Braze and Segment integration allows you to leverage Braze Currents to export your Braze events to Segment to drive deeper analytics into conversions, retention, and product usage. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Segment account | A [Segment account](https://app.segment.com/login) is required to take advantage of this partnership. |
| Braze destination | You must have already [set up Braze as a destination](https://www.braze.com/docs/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) in your Segment integration.<br><br>This includes providing the correct Braze data center and REST API key in your [connection settings](https://www.braze.com/docs/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | In order to export data back into Segment, you need to have [Braze Currents](https://www.braze.com/docs/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Obtain Segment write key

In your Segment dashboard, select your Segment source. Next, go to **Settings > API keys**. Here you will find the **Segment Write Key**.

**Warning:**


It's important to keep your Segment write key up to date. If your connector's credentials expire, the connector will stop sending events. If this persists for more than **5 days**, the connector's events will be dropped, and data will be permanently lost.



### Step 2: Create a new Currents connector

1. In Braze, navigate to **Partner Integrations** > **Data Export**.
2. Click **+ Create New Current** > **Segment Data Export**.
3. Next, provide an integration name, contact email, Segment write key, and Segment region.

![The Segment Currents page in Braze. Here, you can find fields for integration name, contact email, segment region, and API key.](https://www.braze.com/docs/assets/img/segment/segment_currents_integration_config.png?583c85048b7eeaa0b382cb7ecacc4f9c)

### Step 3: Export message engagement events

Next, select the message engagement events you would like to export. Reference the following export events and properties table listed. All events sent to Segment will include the user's `external_user_id` as the `userId` and the user's `braze_id` as the `anonymousId`.

Keep in mind, Braze only sends event data for users without an `external_user_id` if **Include events from anonymous users** is checked.



**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





![List of all available message engagement events on the Segment Currents page in Braze.](https://www.braze.com/docs/assets/img/segment/segment_currents_data_config.png?7186edab8433f388df296aed6f8bc3bd)

Lastly, select **Launch Current**.








To read more, visit Segment [documentation](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/).

## Updating your Current

To update your Currents connector after launching, do the following:

1. In Braze, navigate to **Partner Integrations** > **Data Export**.
2. Locate and your Currents connector in the list.
3. Select <i class="fas fa-pencil"></i>&nbsp;**Edit**.
4. Make your changes.
5. Select **Update Current**.

This will not stop your existing export and will begin sending events according to your new selection.

**Note:**


It may take some time for your changes to take effect.



## Supported Currents events

Braze supports exporting the following events to Segment:

- [Message engagement events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Customer behavior events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

For the payload structure of each event, select the **Segment** tab in the [message engagement events glossary](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) and [customer behavior events glossary](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

