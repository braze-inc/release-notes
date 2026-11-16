# Set up RCS

> This article covers the requirements needed to get your RCS channel running.

Setting up RCS is as straightforward as setting up SMS. Keep reading to learn how you can begin sending rich and interactive messages.

## Step 1: Meet the eligibility criteria

To be eligible for sending RCS with Braze, your business must meet three criteria upfront:

1. Your current Braze contract must include Message or Action Credits. 
2. You must send your RCS messages to a Braze-supported country listed in the following dropdown.

**Braze-supported RCS countries**


- Austria
- Brazil
- Canada
- Colombia (Infobip only)
- Czech Republic
- Denmark
- France
- Germany
- Italy
- Mexico
- Netherlands
- Norway
- Poland
- Singapore
- Slovakia
- Spain
- Sweden
- United Kingdom
- United States



{: start="3"}
3. You must procure an RCS SKU(s) in your contract.

RCS is available with Infobip and Twilio as your SMS service provider. For feature differences, refer to [Provider differences](#provider-differences).

## Step 2: Register an RCS-verified sender

Before you can send RCS messages, you must register an RCS-verified sender. This is the representation of your brand that users see on their mobile devices, which includes your brand’s name, logo, a verification badge, and an optional tagline. The RCS-verified sender reinforces customer trust and confirms your messages come from an authenticated source. 

![An example RCS-verified sender in an RCS message called "Cat Failz Cafe".](https://www.braze.com/docs/assets/img/rcs/rcs_sender.png?fab92ec899380150cc13efd9cb65d5ec){: style="max-width:60%;"}

After you have added the RCS SKU(s) to your order form, Braze is notified and contacts you with RCS sender registration information. The format of these depends on the countries you wish to send RCS messages to. 

When you've submitted your completed forms to Braze, Braze completes the registration process on your behalf. 

### Step 2.1: Set up SMS fallbacks for RCS subscription groups

Because current carrier coverage varies by country, and user hardware and software support vary by individual, SMS fallback is a key component of having a successful RCS program today. We recommend setting up SMS fallback. If a carrier doesn’t support RCS or a user’s device is unable to receive RCS messages, SMS fallback sends your message regardless, so that you never miss an important moment with your users.

We highly recommend reviewing your current SMS opt-in experience, subscription groups, and audience segmentation before deploying your first RCS campaign. If needed, your customer success manager is always available to provide guidance and help you navigate the setup process.

#### How SMS fallback works with events and segmentation




When you use SMS fallback with RCS, the event behavior depends on whether the message is successfully sent through RCS or falls back to SMS:

- **If the RCS send succeeds:** You receive an RCS send event and an RCS delivery event.
- **If the RCS send falls back to SMS:** You receive an RCS send event, an RCS rejection event, and an SMS delivery event. The SMS delivery event has `IS_SMS_FALLBACK=TRUE`.




For SMS and RCS, received message [segmentation filters](https://www.braze.com/docs/user_guide/audience/segments/segmentation_filters) (such as [Received Message from Campaign](https://www.braze.com/docs/user_guide/audience/segments/segmentation_filters#received-message-from-campaign) and [Received Message from Canvas Step](https://www.braze.com/docs/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step)) evaluate when a message is sent, not when it reaches the user's device. With SMS fallback enabled, users can still match these filters if an RCS message is rejected and falls back to SMS, or if the fallback SMS isn't delivered to the user's device.




**Note:**


RCS messages sent from a [Content Optimizer](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step) step don't support SMS fallback.



### Timeline for carrier approval

The timeline for carrier approval varies by country and can also vary within a country. Carrier approval typically takes 3–6 weeks. This is an estimate, and timelines vary by carrier and country. A test sender is typically approved within one week.

When your RCS-verified sender is approved, our operations team updates your subscription groups as needed to confirm they have the RCS sender included in them. 

## Step 3: Set up subscription groups

Your customer success manager helps you add approved RCS-verified senders to a subscription group. For how existing and new groups work, and for traffic migration details, see [SMS and RCS subscription groups](https://www.braze.com/docs/sms_rcs_subscription_groups).

## Provider differences {#provider-differences}

RCS is available with Infobip and Twilio. Most of the setup flow is the same for both, and the composer only shows the options your provider supports. The main differences are described in the following table:

| Capability | Infobip | Twilio |
| --- | --- | --- |
| Text message length | Up to 3,072 characters | Up to 1,600 characters |
| Suggested replies and Open URL suggestions on Text messages | Supported | Supported |
| Standalone Media message type (including PDF and audio) | Supported | Not supported |
| Card: media card | Supported | Supported |
| Card: text-only card | Supported | Not supported |
| Card: suggestions outside the card | Supported | Not supported |
| Card: buttons | 1 to 4 | 1 to 4 |
| Card description | Up to 2,000 characters | Up to 1,600 characters |
| Media file size | Up to 100&nbsp;MB | Up to 16&nbsp;MB |
| SMS fallback sender | Infobip SMS sender in the same subscription group | Twilio SMS sender in the same subscription group |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCS provider differences" }

For the full list of Card options by provider, see [Provider support for RCS messages](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/create#provider-support-for-card-messages).

## Migrating SMS traffic to RCS

You can add an RCS sender to an existing SMS subscription group or create a separate RCS subscription group. The two approaches behave differently:

| Aspect | Same subscription group (recommended for upgrading SMS traffic) | Separate subscription groups |
| --- | --- | --- |
| Eligibility | SMS-subscribed users are automatically eligible for RCS. | You must migrate users into the RCS group. |
| Opt-outs | A STOP sent to either the SMS or the RCS sender unsubscribes the user from the whole group. | Opt-outs in one group don't carry over to the other. You're responsible for keeping subscription states aligned—for example, by unsubscribing users from the RCS group when they opt out of SMS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Same versus separate SMS and RCS subscription groups" }

Also keep these limits in mind:

- A subscription group can't mix SMS service providers, and an RCS sender can belong to only one subscription group. If your SMS sender and RCS sender use different providers, they must be in separate groups, and their subscription states won't sync.
- Users can't opt in by messaging the RCS sender. Opt-in keywords go through the SMS sender in the same group.


If you have separate SMS and RCS subscription groups, you can migrate users from SMS to RCS using a one-step Canvas. For step-by-step instructions, see [Migrate SMS traffic to RCS](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#migrate-sms-traffic-to-rcs).

## Considerations

### Frequency capping and Message Prioritization {#frequency-capping-and-message-prioritization}

RCS sends are included in [global frequency capping](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over) through the same channel rule as SMS, and that rule also applies to Message Prioritization. There is no separate RCS frequency capping or prioritization rule.
