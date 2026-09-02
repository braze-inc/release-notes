# Create an SMS, MMS, or RCS message

> Create personalized SMS, MMS, and Rich Communication Services (RCS) messages in campaigns or Canvas. The selected subscription group determines which message types and senders are available.

## Prerequisites

Before you start, make sure you have the following:

| Requirement | Description |
| --- | --- |
| Sender setup | Complete [sender setup](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup). To send MMS, your subscription group needs an MMS-enabled phone number. To send RCS, complete [RCS setup](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup) and add a verified RCS sender. |
| Subscription group | Create a [subscription group](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) that contains the senders for this message. |
| User phone numbers and consent | Import users' phone numbers and collect the appropriate [SMS, MMS, and RCS opt-ins](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins). |
| Campaign or Canvas | Use a campaign for a single targeted message or Canvas for a multi-step user journey. |
| Message or Action Credits | Confirm that your account has credits available. Sending SMS, MMS, and RCS messages from Braze uses these credits. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS, MMS, and RCS message prerequisites" }

## Create a message

### Step 1: Choose where to build your message




1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **SMS/MMS/RCS**, or, for campaigns targeting multiple channels, select **Multichannel Campaign**.
3. Name your campaign something clear and meaningful.
4. Add [Teams](https://www.braze.com/docs/user_guide/administer/global/user_management/teams) and [Tags](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/tags) as needed.
  - Tags make your campaigns easier to find and use in reports.
5. Add and name the variants for your campaign. You can include SMS/MMS and RCS variants in the same campaign. For more information, see [Multivariate and A/B testing](https://www.braze.com/docs/user_guide/messaging/ab_testing).

**Tip:**


If your campaign variants have similar content, compose the first message before adding more variants. You can then select **Copy from Variant** from the **Add Variant** dropdown.






1. [Create your Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas) using the Canvas composer.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) and specify a delay as needed.
4. Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Choose any other messaging channels which you would like to pair with your message.





### Step 2: Select a subscription group and message type

Select the **Subscription Group** that contains the sender for this message. Braze uses the selected group when calculating the reachable audience and determining send-time eligibility.

The subscription group you select determines which message types are available in the composer:

| Subscription group type | Available message types |
| --- | --- |
| SMS-only | SMS |
| SMS with MMS-enabled numbers | SMS and MMS |
| RCS-enabled with a verified RCS sender | RCS and SMS when the group also contains an SMS sender. MMS is also available when that sender is MMS-enabled. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message types available by subscription group" }

**Tip:**


Add at least one SMS sender to an RCS subscription group so you can send an SMS fallback when RCS delivery fails.



If the subscription group supports both protocols, select **SMS/MMS** or **RCS**. For RCS, select **Text**, **Media**, or **Card**.

### Step 3: Compose your message

The fields and limits in the composer depend on the message type you selected.




#### SMS and MMS fields and settings

| Field or setting | Description |
| --- | --- |
| **Language** | Insert language-specific content into the message. |
| **Message** | Enter up to 1,600 characters, including Liquid, Connected Content, and emojis. The composer estimates the encoding, character count, and number of billable SMS segments. An MMS message can contain media without a message body. |
| **Media** | For an MMS-enabled subscription group, add one PNG, JPEG, or GIF image from the media library or by URL. You can add a vCard instead of an image. |
| **Link shortening** | Shorten HTTP and HTTPS URLs and track engagement. For legacy link shortening, select basic or advanced tracking. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS and MMS fields and settings" }

SMS messages use GSM-7 or UCS-2 encoding and are charged per message segment. A single character can change the encoding and increase the number of billable segments. For encoding rules, segment sizes, and the segment calculator, see [SMS and RCS billing calculators](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/billing_calculator).

![SMS composer showing message copy and its estimated character and segment counts.](https://www.braze.com/docs/assets/img/sms_campaign_compose.png?6033aa6952be0c73a2609384b296e0fe)

#### MMS media specifications



















To send business details that users can save to their device contacts, see [Contact cards](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/create/contact_card). Sending a contact card is charged as an MMS.







































MMS availability and rendering depend on the receiving carrier. When a carrier cannot accept MMS, the media becomes a link in the SMS body through the provider. Avoid sending MMS to Google Voice numbers because its limited MMS support can cause unreliable delivery.

When a user sends inbound media, Braze exposes its URLs in [Currents SMS inbound events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) and through `{{sms.${inbound_media_urls}}}` in Liquid.




#### RCS message types

| Message type | Fields and settings | Limits and behavior |
| --- | --- | --- |
| **Text** | Required message body, optional suggested replies or Open URL actions, optional SMS fallback, and link shortening | The message body can contain up to 1,600 or 3,072 characters, depending on the SMS service provider. Add up to five suggestions. |
| **Media** | Required image, video, document, or audio; optional message body; optional suggestions, SMS fallback, and link shortening | The message body can contain up to 1,600 or 3,072 characters, depending on the provider, and is billed as an additional RCS message. Add up to five suggestions. |
| **Card** | Media card or text-only card, title, description, buttons, optional suggestions, and optional SMS fallback | The title can contain up to 200 characters. The description can contain up to 1,600 or 2,000 characters, depending on the provider. Add between one and four buttons. Provider support determines whether text-only cards and suggestions outside the card are available. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="RCS message types, fields, and limits" }

Suggestions can be suggested replies, which pre-populate the user's text input, or Open URL actions. Add up to 25 characters of text to each suggestion and a URL of up to 2,048 characters to each Open URL action.

For any RCS message type, turn on **Send SMS if RCS fails** to add a fallback message of up to 1,600 characters. The selected subscription group must contain an SMS sender. For **Card** messages, links in the description aren't clickable; use an Open URL button instead.

Some SMS service providers don't support standalone **Media** messages or text-only cards. The composer displays only the supported RCS message types. For **Card** messages, link shortening applies only to links in the SMS fallback.

RCS message billing depends on the message type and content. For basic, rich, and rich card billing rules, see [RCS message billing](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/billing_calculator#rcs-message-billing).

#### RCS media specifications

The composer accepts a media URL with up to 1,000 characters. Available formats and maximum file size depend on the SMS service provider.

| File type | Specifications |
| --- | --- |
| All | Maximum file size is 16&nbsp;MB or 100&nbsp;MB, depending on the provider. |
| Image | JPEG, JPG, GIF, PNG |
| Video | H263, M4V, MP4, MPEG, MPEG-4, WEBM |
| Document | PDF. Available for **Media** messages, but not media cards. |
| Audio | AAC, MP3, MPEG, MP4, 3GPP, OGG. Provider support varies. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="RCS media specifications" }










































#### Personalization

Use [Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid), [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content), emojis, and language-specific content to personalize your message. Include a default value for Liquid personalization so profiles with incomplete data don't receive blank content.

To create message copy from a prompt, use [Generate copy](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities#generate-copy) with Operator.

For languages written from right to left, see [Creating right-to-left messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

#### Create conversational message workflows (RCS)

Conversational message workflows let you respond dynamically to users, creating a back-and-forth messaging experience. To build a workflow, create a Canvas and then combine suggested replies with [Action Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/action_paths) to direct your workflow based on which reply a user selects.

1. In the Canvas builder, create an RCS message step with multiple suggested replies.

![RCS message composer with suggested replies.](https://www.braze.com/docs/assets/img/rcs/suggested_replies.png?45e82379185042e96693250cdbce4331)

{: start="2"}
2. Connect that message to an Action Path with an action group for each suggested reply.
3. For each action group:
   - Select the trigger **Send an SMS inbound message**.
   - Set the message body to be the same as the corresponding suggested reply.

![Action Path step configured with three action groups, one for each suggested reply.](https://www.braze.com/docs/assets/img/rcs/quick_reply.png?0c62088a5f0358d10e98000470e4b7c4)

{: start="4"}
4. Connect each action group to an RCS message step, and then add content based on the associated suggested reply.
5. Continue the conversational workflow by adding suggested replies to any follow-up messages.
6. Repeat steps 2–4 until the workflow is complete.

![Canvas showing a conversational workflow with two Action Paths.](https://www.braze.com/docs/assets/img/rcs/full_conversational_workflow.png?781ed5bdec428617f44cc79f8d356b51)

### Step 4: Configure link shortening

Turn on **Link shortening** to shorten HTTP and HTTPS URLs and track clicks for SMS, MMS, and supported RCS links. Depending on the version available in your workspace, select basic or advanced tracking, or use unified link shortening.

Advanced tracking adds user-level click data for segmentation and retargeting. Unified link shortening combines SMS and RCS shortened links into one personalized format. For supported URLs, Liquid behavior, testing requirements, custom domains, and retargeting, see [Link shortening](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening).

Braze shortens up to 25 links in a message. A URL longer than 4,000 characters can't be shortened and causes the message to fail at send time.

### Step 5: Preview and test your message

Go to the **Test** tab to preview the message as a user or send a test SMS, MMS, or RCS message to a [content test group](https://www.braze.com/docs/user_guide/administer/global/user_management/internal_groups#content-test-groups) or individual user.

**Tip:**


Use the [SMS segment calculator](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator) to estimate how many segments your message contains.



![Previewing SMS copy from the Test tab of the composer. In the profile section, the First Name field is set to "James". In the preview section, the SMS now reads "Hi James, we appreciate your support!"](https://www.braze.com/docs/assets/img/sms_campaign_test.png?d011f361e30b9af969dd0f8f40e0b680)

For MMS, the receiving phone determines whether the media appears before or after the message body.

For RCS, the operating system, device manufacturer, carrier, and messaging app control rendering. Test on real devices because the Braze preview may differ from the received message. For more information, see [Why doesn't my RCS message render accurately on iOS devices?](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/faqs#why-doesnt-my-rcs-message-render-accurately-on-ios-devices).

For more information, see [Send test messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=sms%2Fmms%20and%20rcs).

### Step 6: Build the remainder of your campaign or Canvas




#### Choose a delivery schedule or trigger

Deliver messages at a scheduled time or in response to an action or API trigger. For scheduling and trigger options, see [Schedule your campaign](https://www.braze.com/docs/user_guide/messaging/campaigns/schedule_your_campaign).

Configure delivery controls such as [re-eligibility](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) and [frequency capping](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping). For action-based delivery, set the campaign duration and [Quiet Hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours).

#### Choose users to target

[Target users](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/target_users) by selecting segments and filters. Braze calculates exact segment membership before sending the message.

The selected subscription group filters for subscribed users. SMS and MMS recipients also need a valid phone number. RCS recipients need an RCS-capable device and carrier connection; use an SMS fallback to reach eligible users when RCS delivery fails.

**Important:**


Your message will only be sent to users who already match the conditions you set in the **Target Audience** step. After that, they still need to meet the trigger you define in the **Schedule Delivery** step. Think of the target audience as a waiting room—only people already inside can move forward when the next action happens. 



For click and interaction targeting, see [User retargeting](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting).

#### Choose conversion events

Use [conversion events](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/conversion_events) to measure actions after a user receives the campaign. Set a conversion window of up to 30 days.




Complete the remaining sections of your Canvas. For entry schedules, audience settings, and sending controls, see [Create a Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas).




### Step 7: Review and deploy

After you've finished building your campaign or Canvas, review its details and test the message before sending it.

After launch, use [SMS, MMS, and RCS reporting](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/reporting) to review message performance.

## Things to know

- SMS is charged per message segment, MMS at its own rate, and RCS per message type. Review the [SMS and RCS billing calculators](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/billing_calculator) before sending.
- MMS supports one image or vCard. Carrier support determines whether recipients receive media or an image link.
- RCS capabilities and limits vary by SMS service provider. The composer displays only the options available for the selected subscription group.
- You can send a pre-recorded voicemail as audio in an RCS **Media** message.
- Rendering and interaction behavior vary by device, carrier, operating system, and messaging app.
