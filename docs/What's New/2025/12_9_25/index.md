# December 9, 2025 release

## Data & Reporting

### Adding Google Tag Manager to a landing page

To add Google Tag Manager to your landing pages, add a Custom Code block to your landing page in the drag-and-drop editor, then [insert the Tag Manager code](https://www.braze.com/docs/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) into the block.

## Orchestration

### SMS Liquid use case

The [Respond with different messages based on inbound SMS keyword](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) use case incorporates dynamic SMS keyword processing to respond to specific inbound messages with different message copy. For example, you can send different responses when someone texts “START” versus “JOIN”.

### Allowlisting for Connected Content

You can allowlist specific URLs to be used for [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/). To access this feature, contact your customer success manager.

## Channels & Touchpoints

### SMS character encoding

Our [SMS segment calculator](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator) now has character encoding! Select **Display Character Encoding** to identify which characters are encoded as GSM-7 or UCS-2. 

![SMS segment calculator with a sample SMS message entered in the textbox and the character encoding turned on.](https://www.braze.com/docs/assets/img/sms/character_encoding.png?9545163f307597e2f6b1b0564c086d5a){: style="max-width:70%;"}

### WhatsApp messages with optimization

Because MM API for WhatsApp doesn’t offer 100% deliverability, it's important to understand how to retarget users who may not have received your message on other channels. 

To retarget users, we recommend building a segment of users who didn’t receive a specific message. To do this, filter by the error code `131049`, which indicates that a marketing template message was not sent due to WhatsApp’s per-user marketing template limit enforcement. You can do this by [using Braze Currents or SQL Segment Extensions](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels).

## Partnerships

### OtherLevels - Dynamic content

[OtherLevels](https://www.braze.com/docs/partners/otherlevels/) is an experience platform that uses generative AI to transform how sports brands, publishers, and operators connect with their customers by transforming traditional content into on-brand personalized video and rich media experiences at scale.

## SDK

### SDK breaking updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)