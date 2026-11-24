# Collect user opt-ins

> The following article lists some common SMS, MMS, and RCS opt-in methods.

## Option 1: Ask users to text your short or long code

Ask users to text "START", "UNSTOP", "YES", or a custom opt-in keyword to your number to automatically add them to your subscription group. On your website, mobile app, or even advertising, you can request users do this to opt-in, and you can offer an incentive if it's helpful.

## Option 2: Users opt-in via in-app message

To allow users to opt into SMS from an in-app message, use the [phone number capture form](https://www.braze.com/docs/user_guide/messaging/templates/in_app_message_templates/phone_number_capture) provided by Braze to create a branded form that allows you to collect phone numbers and grow your SMS list.

![In-app message composer with a template for phone number capture.](https://www.braze.com/docs/assets/img_archive/dnd_iam_phone_capture_select.png?9705db2c897ba9a1271967175c8d01a2){: style="max-width:80%;"}

Braze recommends that you also use the [SMS double opt-in](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) feature. This feature automatically works with the in-app message phone number capture form, prompting users to confirm their intent after submitting their phone number via the form.

## Option 3: Sign-up flow

When a new user signs up or registers on the website or app, ask for their phone number and email. Include a checkbox to receive promotional emails and SMS. 

After the user signs up, create or update their profile and set subscription status with one of these REST API options:

- Use the [`/users/track` endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) to create or update the user and set their SMS subscription group in one call. Include `subscription_groups` in the user attributes object.


```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```


- For users who already have a Braze profile, use the [`/subscription/status/set` endpoint](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status) to update subscription group status. This endpoint does not create user profiles.


```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```


**Note:**


To enter users into the [SMS double opt-in](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) workflow when subscribing through the REST API, set `use_double_opt_in_logic` to `true` in your request. This parameter is supported by [`/subscription/status/set`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status), [`/v2/subscription/status/set`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2), and [`/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track). A user profile must exist for the subscription state to be updated with `/subscription/status/set`. If no user profile is associated with the provided phone number, the subscription state isn't updated.
<br><br>
Subscription updates through the REST API don't automatically trigger welcome messages. To send a welcome message, create an action-based campaign with the [Update Subscription Group Status](https://www.braze.com/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#update-subscription-group-status) trigger and set the update source to **REST API**.


