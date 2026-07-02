<br>
<br>


## Understand subscription group timeseries

On the **Subscription Group** page, timeseries charts report:

- **Subscription Group Size:** users subscribed to that group on a given date
- **Subscription Group Unsubscribed Size:** users unsubscribed from that group on a given date

For dashboard guidance, see [Viewing subscription group sizes](https://www.braze.com/docs/user_guide/channels/email/subscriptions/#viewing-subscription-group-sizes).

These metrics are group-specific. They can differ from the segment filter `Email Subscription Status is Unsubscribed`, which reflects global email subscription state rather than a single subscription group. For very large workspaces, Braze may display estimated counts when exact counts are unavailable.

## Avoid duplicate users from email capture forms

Before you create a user from an email capture form, call [`/subscription/status/get`](https://www.braze.com/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) to check whether the profile already exists. If the response is "User not found", create the user with [`/subscription/status/set`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Otherwise, update the existing profile instead of creating a duplicate.

## Snowflake `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` events

The `USERS_MESSAGES_EMAIL_UNSUBSCRIBE` Snowflake table logs message-level email unsubscribes originating from the recipient's side—clicking an unsubscribe link, the email client's one-click List-Unsubscribe, preference center submissions, and ESP-reported unsubscribes. Unsubscribes made through the REST API are not included in this table; those emit [`users.behaviors.subscriptiongroup.StateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events) or [`users.behaviors.subscription.GlobalStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/#global-subscription-state-change-events) events instead.

## SMS test messages and subscription groups

To receive an SMS test message, the recipient must belong to the SMS subscription group you select when sending the test.
