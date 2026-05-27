# Twilio

**Warning:**


Note that support for the Twilio Webhook Integration will be discontinued on January 31, 2020. If you wish to still access SMS services with Braze, see our [SMS documentation](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/). 



For this example, we'll configure the Braze webhook channel to send SMS and MMS to your users, via Twilio's [message sending API](https://www.twilio.com/docs/api/rest/sending-messages). For your convenience, a Twilio webhook template is included on the dashboard.

## HTTP URL

The Webhook URL is provided by Twilio in your dashboard. This URL is unique to your Twilio account since it contains your Twilio account ID (`TWILIO_ACCOUNT_SID`).

In our Twilio example, the webhook URL is `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. You can find this URL in the *Getting Started* section of the Twilio console.

![Twilio_Console](https://www.braze.com/docs/assets/img_archive/Twilio_Console.png?3b2e42e4f25190863a6ce6cf7a8610ba)

## Request Body

The Twilio API expects the request body to be URL-encoded, so we have to start by changing the request type in the Braze webhook composer to `Raw Text`. The required parameters for the body of the request are *To*, *From*, and *Body*.

The following screenshot is an example of what your request might look like if you are sending an SMS to each user's phone number, with the body "Hello from Braze!".

- You'll need to have valid phone numbers on each user profile in your target audience.
- To meet Twilio's request format, use the `url_param_escape` Liquid filter on your message contents. This filter encodes a string so all the characters are allowed in an HTML request; for example, the plus character (`+`) in the phone number `+12125551212` is forbidden in URL-encoded data and will be converted to `%2B12125551212`.

![Webhook Body](https://www.braze.com/docs/assets/img_archive/Webhook_Body.png?4cf2c088181477c5b3e9ed16bc5c3de9)

## Request Headers and Method

Twilio requires two request headers, the request Content-Type and an [HTTP Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side) header. Add them to your webhook by clicking the gear icon on beside the webhook composer, then clicking *Add New Pair* twice.

Header Name | Header Value
--- | ---
Content-Type | `application/x-www-form-urlencoded`
Authorization | `Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}`

Be sure to replace `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` with values from your Twilio dashboard. Lastly, Twilio's API endpoint is expecting an HTTP POST request, so choose that option in the dropdown for *HTTP Method*.

![Webhook Method](https://www.braze.com/docs/assets/img_archive/Webhook_Method.png?5e3ee18f8848a8a1d5f7dc4e51c0520c)

## Preview Your Request

Use the webhook composer to preview the request for a random user, or for a user with particular credentials, to ensure that the request is rendering properly.

![Webhook Preview](https://www.braze.com/docs/assets/img_archive/Webhook_Preview.png?49ceacc7717247634d782f5b49e11431)

