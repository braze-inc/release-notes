# User profiles

> User profiles are a great way to find information about specific users. All persistent data associated with a user is stored in their user profile.

## Access profiles

To access a user's profile, go to the **Search Users** page and search for a user by any of the following:

- External user ID
- Braze ID
- Email
- Phone number
- Push token
- User alias with the format "[user_alias]:[alias_name]", such as "amplitude_id:user_123"

If a match is found, you can view the information you've recorded for this user with the Braze SDK. Otherwise, if your search returns multiple user profiles, you can merge each profile individually or perform a bulk user merge. For a full walkthrough, see [Merge duplicate users](https://www.braze.com/docs/user_guide/audience/manage_audience/merge_duplicate_users).

**Note:**


**Search Users** is not the same as **User Lookup** in the segment or campaign composer. **User Lookup** tests whether a specific user matches your audience and accepts only `external_id` or `braze_id`. **Search Users** on this page supports email, phone, push token, and user alias. For more information, see [Testing segments](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment#testing-segments).



**Important:**


When a phone number is used in the search, it is changed into [`E.164`](https://en.wikipedia.org/wiki/e.164) format. Users whose phone numbers cannot be changed into `E.164` format (for example, because the phone number has an invalid country code or area code) cannot be searched by phone number.



![Search results with a banner that reads "Multiple users match your search criteria" and two buttons labeled Previous and Next.](https://www.braze.com/docs/assets/img_archive/User_Search_Nonunique.png?3e8d565dbd2240f02df9e8fbd505e852){: style="max-width:60%;"}

## Use cases

User profiles are a great resource for troubleshooting and testing because you can easily access information about a user's engagement history, segment membership, device, and operating system.

For example, if a user reports a problem and you aren't sure what device and operating system they are using, you can use the [Overview tab](#overview-tab) to find this information (as long as you have their email or user ID). You can also view a user's language, which could be helpful if you're troubleshooting a [multi-lingual campaign](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization) that didn't behave as expected.

You can use the [Engagement tab](#engagement-tab) to verify whether a certain user received a campaign. In addition, if this particular user did receive the campaign, you can see when they received it. You can also verify whether a user is in a certain segment and whether a user is opted in to push, email, or both. This information is useful for troubleshooting purposes. For example, you should check this information if a user doesn't receive a campaign that you expected them to receive or receives a campaign that you did not expect them to receive.

## Elements of user profile

There are five main sections of a user's profile.

- **Overview:** Basic information about the user, session data, custom attributes, custom events, purchases, and the most recent device that the user logged into.
- **Engagement:** Information about the user's contact settings, campaigns received, segments, communication stats, install attribution, and random bucket number.
- **Event History:** Custom events and purchases from the past 30 days (up to 100 most recent), with full event properties shown as JSON.
- **Messaging History:** Messaging-related events for this user from the past 30 days, loaded from Braze's data warehouse when you open the tab.
- **Feature Flags Eligibility:** Validate which feature flags a user is currently eligible for across rollouts, canvas steps, and experiments. 




### Overview tab {#overview-tab}

The **Overview** tab contains basic information about a user and their interactions with your app or website.

| Overview category | Contains |
| --- | --- |
| Profile | Gender, age group, location, language, locale, time zone, and birthday. |
| Sessions overview | How many sessions they had, when their first and last sessions were, and on which apps. |
| Custom attributes | Which custom attributes are attributed to this user and their associated value, including nested custom attributes. |
| Recent devices | How many devices they logged in on, details on each device, and their associated advertising IDs (if any). |
| Custom events | Which custom events this user has performed, how many times, and when they last performed each event. |
| Purchases | Lifetime revenue attributed to this user, their last purchase, total number of purchases, and a list of each purchase. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Overview tab #overview-tab" }

For more information on this data, see [SDK data collection](https://www.braze.com/docs/user_guide/data/unification/user_data/sdk_data_collection).


<a id="engagement-tab"></a>


### Engagement tab

The **Engagement** tab contains information about a user's interactions with the messages you sent them using Braze.

| Engagement category | Contains |
| --- | --- |
| Contact settings | Subscription status for email, SMS, and push, and the subscription groups this user is associated with for these three channels. This section also includes changelog information for push tokens. Refer to [email](https://www.braze.com/docs/user_guide/channels/email/subscriptions), [SMS](https://www.braze.com/docs/sms_rcs_subscription_groups), and [push](https://www.braze.com/docs/user_guide/channels/push/push_setup/push_subscription_states) for information on how subscriptions and opt-ins are set. |
| Campaigns received | **Campaigns received** reflects channel-specific send and view timing. Most channels record a send when Braze passes the message to the delivery provider, even when the message is not ultimately delivered. **Content Cards** are different: campaigns appear here only after the user views the card in the app. For a breakdown by channel, see [When campaigns appear in Campaigns received](#when-campaigns-appear-in-campaigns-received). <br><br>When a message is received, opened, or clicked, Braze updates data for all profiles that share the same channel identifier as the profile that logged the interaction (for example, the same email address for email, or the same phone number for SMS or WhatsApp). Users who share an identifier with someone who received, opened, or clicked the message can match this filter even if they were not originally in the campaign or were not directly sent the message.<br><br>These lists use [messaging interaction data](https://www.braze.com/docs/api/data_retention/messaging_interaction_data) (including expiration rules) when determining what appears for retargeting and history.<br><br> Select a campaign from the list to view it. |
| Segments | Segments this user is included in. Select a segment from the list to view it. |
| Communication stats | When this user last received messages from you from each channel. |
| Install attribution | Information about how and when a user installed your app. Learn more about [understanding user installs](https://www.braze.com/docs/user_guide/messaging/campaigns/ideas_and_strategies/install_attribution). |
| Miscellaneous | The user's [random bucket number](https://www.braze.com/docs/user_guide/messaging/ab_testing/concepts/random_bucket_numbers). |
| Canvas messages received | Canvas messages this user has received and when. This section shows messaging interaction history (such as email sends and opens), not Canvas entry history. A user can appear here even if they never entered the Canvas (for example, when another profile sharing the same email address received or opened the message). An open can also create a new entry for a shared email profile that was not originally sent the message.<br><br>Send timing, shared channel identifiers, and [messaging interaction data](https://www.braze.com/docs/api/data_retention/messaging_interaction_data) expiration follow the same rules as **Campaigns received**. See [When campaigns appear in Campaigns received](#when-campaigns-appear-in-campaigns-received).<br><br>Select a message from the list to view it. |
| Predictions | [Churn prediction](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_churn) and [event prediction](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_events) scores for this user. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Engagement tab" }


<a id="event-history-tab"></a>


### Event History tab

**Note:**


To view the **Event History** tab, you need the **Search Users**, **View User Event Properties**, and **View PII** [permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions), because event properties can contain personal data.



The **Event History** tab shows the custom events and purchases a user has logged. Use it to verify event data is arriving correctly and troubleshoot user-level issues directly in the dashboard—no data exports or external tooling required.

| Event History category | Contains |
| --- | --- |
| Event list | Custom events and purchases from the past 30 days (up to 100 most recent), ordered newest first. |
| Event type | Whether the row is a **Custom Event** or **Purchase**. |
| Timestamp | When the event was logged. |
| Event name | The name of the custom event or purchase. |
| Event properties | Full event properties for the event, shown as JSON. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Event History tab" }




### When campaigns appear in Campaigns received {#when-campaigns-appear-in-campaigns-received}

In general, Braze lists a campaign under **Campaigns received** after it attempts to send the message. A delivery to the user's device or inbox is not required for a send to be logged. **Canvas messages received** follows the same channel-specific rules for each Canvas message type.

**Tip:**


When timestamps are displayed in relative format (such as "6 days ago"), hover over them to see the exact date and time.



- **Email:** Braze logs a send when the message is handed off to your email service provider (ESP). After that handoff, the message is not aborted because of Liquid logic, rate limiting, or the user being marked as unreachable. The next events are often a delivery or a bounce.
- **Push:** Braze logs a send when the message is handed off to the push provider (for example, Apple Push Notification service (APNs) or Firebase Cloud Messaging (FCM)). The provider usually tries to deliver immediately; if the device is unavailable (for example, offline), the provider may retry until the message expires.
- **In-app messages:** Braze logs a send when the campaign is launched.
- **Content Cards:** When Braze records a _Sent_ event depends on delivery type and your **Card Creation** setting. A Content Card campaign appears under **Campaigns received** on the user profile only after the user views the card in the app. For the full breakdown, see [When sends are logged](https://www.braze.com/docs/user_guide/channels/content_cards/reporting#when-sends-are-logged) and [Campaigns Received and retargeting filters](https://www.braze.com/docs/user_guide/channels/content_cards/reporting#campaigns-received-and-retargeting-filters) in the Content Card reporting article.
- **SMS, WhatsApp, and webhooks:** Braze logs a send when the message enters the delivery path for that channel (for example, the SMS or WhatsApp provider, or your webhook endpoint).

**Note:**


These descriptions cover when a send is logged for **Campaigns received**. They are separate from [message aborts](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) that can stop a message before it reaches a provider.



![The Engagement tab of a user profile displaying their contact settings and communication statistics.](https://www.braze.com/docs/assets/img_archive/profiles_engagement_tab.png?308b978aab12e87f79677f25a8468038)

### Messaging History tab {#messaging-history-tab}

The **Messaging History** tab shows messaging-related events for an individual user from the past 30 days. Events include sends, deliveries, opens, clicks, inbound messages, aborts, frequency capping, and more, depending on the channel.

Braze loads this tab from its data warehouse when you open it. Results can take a short time to appear while the queries finish. After results load, Braze caches them briefly so revisiting the same profile soon after can return the same set without re-querying.

**Note:**


**Messaging History** is not the same as **Event History**. **Event History** lists custom events and purchases (past 30 days, up to 100 most recent). **Messaging History** lists message engagement events from campaigns, Canvases, and related messaging activity.



![The Messaging History tab showing which campaigns and Canvases a user has received.](https://www.braze.com/docs/assets/img_archive/profiles_messaging_history_tab.png?82660adfd8ea760b065a4c3230414afe)

#### Messaging History versus Engagement tab data

Use this comparison when a message, count, or timestamp on the profile doesn't match what you see under **Messaging History**.

| Profile surface | What it shows | Retention and scope | Common reason it differs from Messaging History |
| --- | --- | --- | --- |
| **Overview** | Lifetime-style profile values such as session counts, purchase totals, and custom event counts—not a message event log. | Stored on the user profile. | A purchase or custom event count is not a messaging event, so it never appears in **Messaging History**. |
| **Engagement** > **Communication stats** | Last time this user received a message on each channel (and last received any message). | Stored on the user profile as last-received timestamps. | A last-received time can be older than 30 days, so the corresponding send may no longer appear in **Messaging History**. |
| **Engagement** > **Campaigns received** / **Canvas messages received** | Campaigns and Canvas messages associated with this profile for retargeting and troubleshooting. | Uses [messaging interaction data](https://www.braze.com/docs/api/data_retention/messaging_interaction_data), including expiration and restore rules. Shared channel identifiers can add entries that weren't sent to this exact profile. | A campaign can appear here when the send is older than 30 days, when interaction data was restored, or when another profile sharing the same email or phone logged the interaction. Those cases may not appear (or may look different) in **Messaging History**. |
| **Messaging History** | Event-level messaging activity (send, delivery, open, inbound SMS, abort, and similar). | Past 30 days from the data warehouse for this Braze user ID. | Empty campaign names, missing inbound events, or missing older sends usually mean the event is outside the 30-day window, never landed in the warehouse for this user ID, or was sent without campaign metadata. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Messaging History versus Engagement tab data" }

#### Retention, limits, and older history

- **Retention:** **Messaging History** includes events from the past 30 days only.
- **Item limit:** **Event History** is limited to the 100 most recent custom events and purchases. **Messaging History** loads up to the 1,000 most recent events for each event type on each channel (for example, 1,000 email sends and 1,000 email opens) from the 30-day window, then paginates them. On a busy profile, older events of a high-volume type can be missing even though they are less than 30 days old. Filters narrow the events already loaded; they don't load more.
- **Latency:** Opening the tab starts warehouse queries. Wait for the table to finish loading before concluding an event is missing. Newly sent messages also need time to land in the warehouse before they can appear.
- **Merges:** After a user merge, **Messaging History** is not rewritten onto the surviving profile. Message engagement history used for **Campaigns received** can transfer, but pre-merge warehouse events stay tied to the orphaned user ID. For details, see [User profile lifecycle](https://www.braze.com/docs/user_guide/data/unification/user_data/user_profile_lifecycle#reporting-and-merged-profiles).
- **Older than 30 days:** Use [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) message engagement events, [Snowflake](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake), campaign or Canvas analytics, or a [user profile export](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier). Profile exports and **Campaigns received** follow [messaging interaction data](https://www.braze.com/docs/api/data_retention/messaging_interaction_data) availability, which is separate from the 30-day **Messaging History** window.

#### Viewing and understanding events

For each event in the **Messaging History** table, you can see the messaging channel, event type, timestamp, associated campaign or Canvas message, and destination or device details when available. To filter for specific events, select **Filters** and choose events from the list.

Braze queries most events for a channel only when the profile shows activity on that channel (for example, a last-received timestamp, or an impression for in-app messages and Content Cards). Abort events are queried for every channel, and so are Retry events when message prioritization is enabled. Content Cards send events are always queried so available-card sends can appear even before an impression.

##### Message engagement events

The following message engagement events can appear in **Messaging History**. To learn how specific events are tracked, see the [Message engagement event glossary](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

| Channel | Engagement events available |
| --- | --- |
| Email | Abort<br>Bounce<br>Click<br>Deferral<br>Delivery<br>Frequency capped<br>Mark as spam<br>Open (see [note on email open event](#note-on-email-open-event))<br>Retry<br>Send<br>Soft bounce<br>Unsubscribe |
| SMS | Abort<br>Carrier send<br>Delivery<br>Delivery failure<br>Frequency capped<br>Inbound receive<br>Rejection<br>Retry<br>Send |
| RCS | Abort<br>Click<br>Delivery<br>Frequency capped<br>Inbound receive<br>Read<br>Rejection<br>Send<br>SMS fallback |
| Push | Abort<br>Bounce<br>Frequency capped<br>Influenced open<br>iOS Foreground<br>Open<br>Retry<br>Send |
| In-app message | Abort<br>Click<br>Frequency capped<br>Impression |
| Content Cards | Abort<br>Click<br>Dismiss<br>Frequency capped<br>Impression<br>Send |
| Webhooks | Abort<br>Frequency capped<br>Retry<br>Send |
| WhatsApp | Abort<br>Delivery<br>Failure<br>Frequency capped<br>Inbound receive<br>Read<br>Retry<br>Send |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message engagement events" }

**Note:**


**Retry** events appear when message prioritization is enabled for your company. **RCS** events appear when RCS is enabled for your company. Frequency capped events are abort events with a frequency-capping reason; filter for **Frequency capped** separately from other abort reasons. In-app message and Content Card **Abort** events have no filter option, so they appear only when no filters are applied.



##### Message abort events

Message abort events occur when a message was aborted because of conditional logic in [Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) or [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content), Liquid rendering timeouts, frequency capping, or related send-path decisions. When available, the event label can show a more specific reason such as **Frequency capped** or **Deprioritized**.

##### Frequency cap events

A frequency capped event occurs when a user qualifies for a message but doesn't receive it because of [frequency capping](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) settings. Customize frequency capping from **Settings** > **Frequency Capping Rules**.

##### Blank destinations

Some message sends may appear in **Messaging History** with blank destinations (shown as "—"). Some channels, such as Content Cards and webhooks, don't gather device data on message send.

Content Cards sends are logged when the card is available to be viewed. Because Content Cards can be viewed on multiple devices, device data isn't logged for a send. Instead, that information is logged on impression (when the card is viewed). Webhooks are sent to a system endpoint (not a device), so device data isn't applicable.

#### Note on email open event {#note-on-email-open-event}

Email open tracking is error-prone in any tool, including Braze. With a variety of privacy protection features offered by different email clients that either block the automatic loading of images or load them proactively on the server, email open events are susceptible to both false positives and false negatives.

While email open statistics can be useful in aggregate, for example, to compare the effectiveness of different subject lines, you shouldn't assume an individual open event for an individual user is meaningful.

#### Why are events missing or fields blank in Messaging History?

Some fields or entire events may be absent in the following scenarios:

- **Outside the 30-day window:** The event is older than 30 days. Check **Campaigns received**, **Communication stats**, Currents, or Snowflake instead.
- **Still loading or not yet in the warehouse:** Wait for the tab query to finish. Very recent sends may not have landed yet. Braze caches loaded results for about 10 minutes, so reopen the tab after that to check for newer events.
- **API send without campaign metadata:** Events from the [/messages/send endpoint](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages#creating-new-users-with-api-sends) (and similar API sends) don't populate **Campaign/Canvas** when the request omits `campaign_id` and `message_variation_id`. Those fields are optional. When you include them, Braze can show campaign metadata in **Messaging History**.
- **Missing Message Sent variation name:** The campaign may not have message variations.
- **Manual test send:** Manual tests can appear in **Messaging History** without the campaign or Canvas name.
- **Seed or internal test audience:** **Messaging History** may show limited campaign or Canvas metadata compared with production sends.
- **Merged or orphaned profiles:** If a message appears under **Campaigns received** but not in **Messaging History**, the user may have received it on a profile that was later merged. **Campaigns received** can transfer; **Messaging History** does not rewrite warehouse events onto the surviving user ID. Look up the orphaned profile's `braze_id` in Currents, Snowflake, or **Messaging History** for that ID. See [User profile lifecycle](https://www.braze.com/docs/user_guide/data/unification/user_data/user_profile_lifecycle#reporting-and-merged-profiles).
- **Inbound SMS or other channel gaps:** Braze queries SMS (and related) history when the profile has a last-received SMS timestamp. If that channel never recorded a last-received value on this profile, related events may not be queried. Shared phone numbers and merges can also separate inbound events from the profile you're viewing.

## Attribute change history and ingestion source {#attribute-change-history}

The user profile shows the current value of default and custom attributes. Braze does not keep a full attribute change log on the dashboard profile (no previous value, no timestamp per attribute change, and no ingestion source on the **Overview** tab).

Exceptions and alternatives:

| Need | Where to look | Limits |
| --- | --- | --- |
| Current attribute values | **Overview** tab on the user profile, or a [user profile export](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier) | Shows current state only. Braze doesn't store time-series graphs for custom attributes on the profile. See [Custom attributes](https://www.braze.com/docs/user_guide/data/activation/attributes/custom_attributes). |
| Push token moves between users | **Engagement** > **Contact settings** push token changelog | Covers push token changelog entries only, not general attributes. See [Push subscription states](https://www.braze.com/docs/user_guide/channels/push/push_setup/push_subscription_states). |
| When a profile attribute changed and from which source | Currents [`users.profile.Update`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events#user-profile-update-events) (`update_source`) | Requires the User Profiles and Attributes entitlement for Currents. Streams the updated attributes and source for each update your connector receives. It does not reconstruct a full previous-value timeline by itself—compare successive events or use Snowflake history views. Retention follows your Currents destination storage. |
| Subscription status changes and source | Currents [Global Subscription State Change](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events) (`state_change_source`) and [Subscription Group State Change](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events) events | Covers subscription changes, not every custom attribute. |
| Historical default or custom attribute values with source | Snowflake [user attribute history views](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake/user_attributes/#historical-change-logs) (`UPDATE_SOURCE`, `EFF_DT`, `END_DT`) | Rolling 6 months, snapshotted about every 12 hours. Multiple updates inside a 12-hour window can collapse into one record. Requires Snowflake Data Share. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Attribute change history and ingestion source" }

**Important:**


Cloud Data Ingestion (CDI) profile updates are recorded with the same update source label as REST API updates in Currents and Snowflake (`REST API` / equivalent `UPDATE_SOURCE`). You can't distinguish CDI from other REST API updates using `update_source` alone.



Common `update_source` / `UPDATE_SOURCE` values include SDK, REST API, Dashboard, CSV Import, Canvas, Canvas User Update Step, Preference Center, Shopify, User Merge, and related subscription or provider sources. Exact strings depend on the export surface (Currents vs Snowflake).

## Data size constraints

Braze doesn't enforce an overall capacity on the total size of a user profile. However, specific data types associated with users have defined size capacities.

### Custom attribute arrays

Custom attribute arrays (including arrays of objects) have a capacity of 100 KB. When you send an array that exceeds this capacity, the custom attribute isn't processed. The API returns a success response (201), but the array doesn't appear in the user profile and existing data for that attribute isn't updated.

If your arrays approach this capacity, consider limiting the number of objects you populate to keep the total size within 100 KB.

For more information on custom attributes, see [Custom attribute data types](https://www.braze.com/docs/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types).

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/data/unification/user_data/user_profile_lifecycle"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">User profile lifecycle</span></span></div></a></li><li><a href="/docs/api/endpoints/export/user_data/post_users_identifier"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">POST: Export user profile by identifier</span></span></div></a></li><li><a href="/docs/api/endpoints/user_data/post_user_delete"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">POST: Delete users</span></span></div></a></li></ul>
