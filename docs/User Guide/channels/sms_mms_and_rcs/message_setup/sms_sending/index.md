# SMS, MMS, and RCS sending basics

> Review the subscription, geographic permissions, billing, and keyword fundamentals that apply when you send SMS, MMS, and RCS messages with Braze. For full composer steps, see [Create an SMS, MMS, or RCS message](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/create).

## Select your subscription group

Send SMS, MMS, and RCS messages from a [subscription group](https://www.braze.com/docs/sms_rcs_subscription_groups). A subscription group contains sending entities—such as short codes, long codes, alphanumeric sender IDs, and RCS-verified senders—for a specific messaging purpose. Use separate subscription groups for use cases such as transactional and promotional messaging.

Before you send RCS, complete [RCS setup](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup) to get a verified RCS sender added to the group. For number types and throughput, see [Sender setup](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Geographic permissions

Each SMS, MMS, and RCS subscription group has a country allowlist under **Geographic Permissions**. Braze only sends to phone numbers in allowlisted countries. Configure the allowlist before launch so test sends and campaigns are not aborted for a destination country.

For admin steps, High Fraud Risk countries, and abort visibility, see [Geographic permissions](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

## Compose the message

For message fields, character limits, personalization, media, link shortening, and RCS message types, see [Create an SMS, MMS, or RCS message](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/create).

## Understand message segments and character limits

SMS messages use GSM-7 or UCS-2 encoding and are charged per message segment. RCS billing depends on message type. For encoding rules, segment sizes, the segment calculator, and RCS billing categories, see [SMS and RCS billing calculators](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/billing_calculator).

## Keyword customization (optional)

Regulations require responses to opt-in, opt-out, and Help or Info keywords. Define keywords, responses, and language-specific keyword sets through [Keyword processing](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

## Related sending guidance

<ul class="guide_tiles"><li><a href="/docs/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Best practices for SMS, MMS, and RCS</span><span class="guide_tile_description">Multi-country sending, high-volume tips, and quiet hours for sending-time compliance.</span></span></div></a></li><li><a href="/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Workspace quiet hours</span><span class="guide_tile_description">Apply an SMS/MMS/RCS quiet hours window across campaigns and Canvases in the workspace.</span></span></div></a></li><li><a href="/docs/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Preventing SMS, MMS, and RCS traffic pumping fraud</span><span class="guide_tile_description">How traffic pumping works and how geographic allowlisting reduces exposure.</span></span></div></a></li></ul>
