# Handle unknown phone numbers - new users

> You may find that after you get SMS, MMS, and RCS running with Braze, you receive messages from unknown users. The following steps describe how an unidentified user and number get processed.

## Opt-in/out and custom keyword workflow for unknown numbers

Braze automatically addresses an unknown number in one of three ways:

1. If an opt-in keyword is texted:
  * Braze creates an anonymous profile
  * Braze sets the phone attribute
  * Subscribes the user to the corresponding subscription group based on what opt-in keyword was received by Braze.<br><br>
2. If an opt-out keyword is texted:
  * Braze creates an anonymous profile
  * Braze sets the phone attribute
  * Unsubscribes the user from the corresponding subscription group based on what opt-out keyword was received by Braze.<br><br>
3. If any other message is texted:
  * By default, Braze ignores the message and does nothing.
  * If [catch-all inbound handling](#catch-all-inbound-handling-for-unknown-numbers) is turned on for your workspace, Braze creates an anonymous, unsubscribed profile and logs the message.<br><br>

## Catch-all inbound handling for unknown numbers




**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





When a phone number without a Braze profile sends a message that doesn't match an opt-in or opt-out keyword, Braze does the following:

1. Creates an anonymous user profile with that phone number. The profile isn't subscribed to your subscription group.
2. Logs the inbound message to the profile and triggers the **Inbound SMS Received** event.
3. Sends your auto-response, if you have one, at most once per phone number every 24 hours. Braze never sends an auto-response to a number that has opted out.

If the person later texts an opt-in keyword, Braze subscribes the same profile.

### Forward inbound messages to your team

Create an action-based webhook campaign triggered by **Inbound SMS Received** to send messages to your support platform or middleware. Example payload:


```json
{
  "from": "{{${phone_number}}}",
  "to": "{YOUR_SHORT_CODE}",
  "body": "{{sms.${inbound_message_body}}}",
  "mediaUrls": ["{{sms.${inbound_media_urls}}}"]
}
```


### Inbound photos

Inbound MMS messages can include photos. Braze exposes media URLs through Liquid `{{sms.${inbound_media_urls}}}` and [Currents SMS inbound events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) so your webhook or support tools can retrieve them. Download or copy the file when your webhook receives it.

### Things to know

- Profiles created from inbound messages count toward your monthly active users.
- To combine a new profile with an existing customer profile, use the [`/users/merge`](https://www.braze.com/docs/api/endpoints/user_data/post_users_merge) endpoint.
