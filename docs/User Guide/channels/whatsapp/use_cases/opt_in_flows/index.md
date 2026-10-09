# WhatsApp opt-in flows

> Build a flow that collects WhatsApp opt-ins from your users, confirms their subscription, and updates their subscription status in Braze.

## Requirements

Before setting up opt-in flows, confirm the following are in place:

| Requirement | Description |
| --- | --- |
| WhatsApp Business Account | Your WhatsApp Business Account is connected to Braze and your subscription group is configured. |
| Meta opt-in policy | You understand Meta's [WhatsApp opt-in requirements](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) and Braze [opt-in and opt-out](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) guidance. Users must explicitly agree to receive messages from your business before you can message them. |
| Opt-in data plan | You have a plan for where opt-in data is captured and how it is passed to Braze (through SDK, API, or your data pipeline). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## How opt-ins work in Braze

When a user agrees to receive WhatsApp messages from your business, their subscription status must be updated to **Subscribed** in Braze before they can receive messages from your WhatsApp subscription group. An inbound WhatsApp message alone does not subscribe the user. Set subscription status using one of these methods, depending on how opt-in data is collected:

| Method | Description |
| --- | --- |
| Braze SDK | Update a user's subscription status when a user completes an opt-in action in your app |
| Braze API | Send a subscription status update when opt-in data is captured outside the app (for example, through a web form or third-party integration) |
| Inbound WhatsApp message | When a user messages your business (for example, after scanning a QR code), configure a Canvas or campaign with a [User Update step](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#user-update-step), webhook, or API call to set their subscription status. See [Inbound WhatsApp message](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#inbound-whatsapp-message). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription status update methods" }

## Opt-in confirmation with a response message

As a best practice, always confirm a user's subscription with an immediate WhatsApp message. It sets expectations, reinforces the value of the channel, and gives users an easy way to opt out if they enrolled by mistake.

Because the user initiates the conversation by scanning a QR code or directly messaging your number, the 24-hour conversation window is open. This means you can send a response message for confirmation rather than a pre-approved template.

**Note:**


If the user opts in through a form or checkbox and hasn't messaged your WhatsApp number yet, the conversation window isn't open. Use a Meta-approved [template message](https://www.braze.com/docs/user_guide/channels/whatsapp/create_a_whatsapp_message) for confirmation instead.



### Set up a confirmation Canvas

Create one Canvas that both updates subscription status and sends the confirmation when the opt-in keyword arrives.

1. Go to **Messaging** > **Canvas** and select **Create Canvas**.
2. Name your Canvas (for example, "WhatsApp — Opt-In Confirmation").
3. Under **Entry Schedule**, select **Action-Based**.
4. Set the **entry trigger** to **Send a WhatsApp inbound message**. Filter the message body to your opt-in keyword (for example, "JOIN") so unrelated inbound messages don't enter the Canvas.
5. Add a [User Update step](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#user-update-step) to set the user's subscription status to **Subscribed**.
6. Add a **Message** step after the User Update.
7. Select **WhatsApp** > your subscription group > **Response** as the message type.
8. Choose the **Text** layout and write a short confirmation message. For example, "You're now subscribed to [Brand] on WhatsApp. We'll send you [brief description of what they'll receive]. Reply [your opt-out keyword] at any time to unsubscribe."
9. (Optional) Add a **Quick reply** layout instead of plain text to prompt the user's next action (for example, "Browse offers" or "Track my order").

**Tip:**


Make the confirmation message short to reduce confusion and help maintain a healthy opt-out rate. Tell users exactly what they signed up for and how to opt out. Opt-out keywords such as "STOP" only unsubscribe users if you configure that keyword flow in Braze. For details about opt-out keywords, see [Opt-ins and opt-outs](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#general-opt-out-keywords).



## Updating subscription status in Braze

After a user opts in, use one of the following update methods to set the user's subscription status to **Subscribed** in Braze. This allows them to receive future messages from your WhatsApp subscription group.




Call the subscription group status update method when the user completes the opt-in action in your app (for example, submits a form or checks a box). For SDK methods by platform, see [Setting users' WhatsApp subscription groups](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#setting-users-whatsapp-subscription-groups).




Send a `POST` request to the `/subscription/status/set` endpoint with the user's phone number, subscription group ID, and status set to `subscribed`. This approach works for opt-ins collected outside the Braze SDK, such as web forms, POS systems, or third-party integrations. For request parameters, permissions, and examples, see [POST: Update user's subscription group status](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).




If your opt-in flow routes users to send a message to your WhatsApp business number, configure a Canvas or campaign that updates subscription status when that inbound message is received—for example with a [User Update step](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#user-update-step) or webhook. Inbound messages do not subscribe users by themselves. For setup steps, see [Inbound WhatsApp message](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#inbound-whatsapp-message).




## Opt-in method: QR code

A WhatsApp QR code links directly to a pre-filled message in WhatsApp. When a user scans the code, WhatsApp opens with your business number and an optional pre-filled message body. The user sends the message to initiate the conversation and confirm their opt-in.

### Step 1: Generate your WhatsApp QR code

1. In **Meta Business Manager**, navigate to your WhatsApp Business Account.
2. Under **WhatsApp Manager** > **Phone Numbers**, select your business phone number.
3. Select **WhatsApp Links** (or **QR Code**, depending on your Meta interface version).
4. Set a pre-filled message for users to send when they scan the code (for example, "I'd like to subscribe" or a keyword like "JOIN"). This message is the inbound trigger you use in Braze.
5. Download or copy the QR code for use in your marketing materials.

### Step 2: Set up subscription update and confirmation

Follow [Opt-in confirmation with a response message](#opt-in-confirmation-with-a-response-message) to create one action-based Canvas that:

1. Enters on **Send a WhatsApp inbound message** filtered to your opt-in keyword (for example, "JOIN").
2. Uses a [User Update step](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#user-update-step) to set subscription status to **Subscribed**.
3. Sends a WhatsApp **Response** confirmation message.

You can also split subscription update and confirmation into separate Canvases that share the same inbound trigger, but a single Canvas keeps entry and message order easier to manage. For other inbound update approaches, see [Inbound WhatsApp message](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#inbound-whatsapp-message).

### Step 3: Place the QR code

Deploy your QR code anywhere users can scan it: packaging, in-store signage, print ads, email campaigns, or your website. For digital placements, consider linking the QR code URL directly so users on mobile can tap instead of scan.

**Important:**


Meta requires that opt-in collection points clearly disclose that the user is agreeing to receive WhatsApp messages from your business. The opt-in surface—whether physical or digital—must include this disclosure before the user scans or taps.



## Opt-in method: Other collection surfaces

For users who aren't scanning a QR code, opt-ins are typically collected through standard web or app interfaces. In these cases, subscription status is updated through the Braze SDK or API after the user completes the action.

**Important:**


Because the user hasn't yet sent your business a WhatsApp message, the 24-hour conversation window isn't open when they opt in through a form or checkbox. Your confirmation message must be a Meta-approved template message (not a response message).



### Phone number capture form

A phone number capture form asks users to enter their phone number and consent to WhatsApp messaging, and is typically placed on a brand website or in a post-purchase flow.

#### Setup

1. Build the form on your website or in your app. The form must include a clear disclosure that the user is consenting to WhatsApp messages, along with your terms and privacy policy.
2. On form submission, pass the user's phone number and consent status to Braze through the Braze API (`/subscription/status/set` endpoint) or your data pipeline if you're using a CDP.
3. If the user is already identified in Braze, their profile updates. If they're new, create the user profile first using the `/users/track` endpoint, then update their subscription status.
4. Send a confirmation template message through the API after the status update, or set up an action-based Canvas that enters on **WhatsApp subscription group status** changing to subscribed and sends a WhatsApp **Template** message.

**Tip:**


If your form collects both email and phone, consider sending a multi-channel opt-in confirmation. Use WhatsApp for immediate confirmation and email as a fallback if WhatsApp delivery fails.



### Checkbox on a registration or checkout page

A checkbox can be embedded in an existing flow—such as account creation, checkout, or profile setup—and let users opt in to WhatsApp messaging at a natural moment in the experience.

#### Setup

1. Add the checkbox to your registration or checkout form. Label it clearly (for example, "Send me order updates and offers on WhatsApp"). Pre-checking the box on behalf of the user isn't valid consent; the user must check the box.
2. After the user submits the form with the checkbox checked, update their subscription status in Braze through the Braze SDK or API.
3. Confirm with a Meta-approved WhatsApp template message: send it through the API after the status update, or use an action-based Canvas that enters on **WhatsApp subscription group status** and sends a **Template** message.

## Opt-in method: QR code on TV (streaming service example)

Displaying a QR code on a TV screen lets viewers opt in to WhatsApp with a second device. The flow is the same as a standard QR code opt-in, but the placement and user experience require additional consideration.

### How the flow works

1. A QR code appears on the TV screen (in an ad, during a break between content, or as an on-screen prompt in the streaming app).
2. The viewer scans the code with their phone.
3. WhatsApp opens on the phone with your business number and a pre-filled message.
4. The viewer sends the message to confirm their opt-in.
5. Braze receives the inbound message. Your configured Canvas or campaign updates their subscription status (for example, with a User Update step) and sends the confirmation response message.

### Setup considerations

Follow the same steps as [Opt-in method: QR code](#opt-in-method-qr-code). The key differences are in how the QR code is deployed and how the experience is designed for a TV context.




- Make the QR code large enough to scan from a typical viewing distance (8–10 feet). A minimum size of 400×400 px is recommended for full-screen TV display, but test on actual hardware before launching.
- Display the code for long enough for viewers to pick up their phone and scan, at least 10–15 seconds, or longer if it appears alongside other on-screen content.
- Include a short text prompt near the code (for example, "Scan to get exclusive updates on WhatsApp").




Use a short, simple keyword as the pre-filled message body (for example, "JOIN" or "SUBSCRIBE"). Viewers may not read the pre-filled text carefully before tapping send, so keep it unambiguous.




### User identity

If the viewer is logged in to your streaming app on their TV and you can match their phone number to their existing Braze profile (through the API or a logged-in scan flow), their subscription status update attaches to their existing profile.

If the viewer scans as an anonymous or new user, Braze creates a new profile on inbound message receipt. You may need a merge or identity resolution step for [User identity management](https://www.braze.com/docs/user_guide/data/unification/user_data/user_profile_lifecycle/).

**Tip:**


If your streaming app shows the QR code during an ad, coordinate with your ad server or content management system to track when the code was displayed alongside Braze subscription data. This helps you measure opt-in lift attributable to specific placements or creatives.



## Measure performance

Track the health and growth of your opt-in program using the following metrics.

| Metric | What to look for |
| --- | --- |
| **Subscription group size** | Monitor growth over time in **Audience** > **Subscription Groups** to understand opt-in volume by collection method. |
| **Confirmation message delivery rate** | A low delivery rate on your confirmation Canvas may indicate phone number quality issues or subscription status not being set before the message attempts to send. |
| **Opt-out rate** | Track opt-outs after the confirmation message and after the first few campaign sends. A spike early in the lifecycle may indicate a mismatch between what users expected when they opted in and what they received. |
| **QR code scan volume** | If your QR code is hosted on a landing page or tracked link, use UTM parameters or a URL shortener with analytics to measure scan-to-opt-in conversion by placement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Opt-in performance metrics" }
