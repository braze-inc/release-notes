# Best practices for SMS, MMS, and RCS 

> Learn more about best practices for SMS, MMS, and RCS with Braze, including our recommendations for opt-out monitoring, traffic pumping, and sending times.

## Opt-out monitoring recommendations

Complying with recipient requests to opt-out of communications is required by law. Failing to comply with requests by SMS recipients to opt-out of the channel can incur penalties, including fines, and can lead to lawsuits. Braze has features in place to enable robust SMS and MMS opt-in and out management, plus mechanisms to assist in making sure requests are correctly processed.

Under their subscription agreements with us, our customers are solely responsible  for their compliance with applicable law in their use of our services. Accordingly, we strongly recommend that customers pay close attention to correctly configuring their SMS set-up, and that they test those set-ups thoroughly, take measures to monitor opt-out compliance, and act promptly should they identify instances of non-compliance with opt-out requests.

When setting up SMS and MMS in Braze to manage opt-ins and opt-outs, refer to the following list of resources:
* [SMS subscription groups](https://www.braze.com/docs/sms_rcs_subscription_groups): Subscription groups and opt-in/out methods and statuses.
* [Subscription Group REST APIs](https://www.braze.com/docs/api/endpoints/subscription_groups): How to process opt-ins and outs they receive from a source other than a direct response to a message.
* [Keyword processing](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): Explanations for how Braze approaches keyword processing and management.
* [SMS double opt-in](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): Requires users to explicitly confirm their opt-in intent before they can receive SMS messages. SMS double opt-in is a requirement for some countries, so Braze recommends configuring this.
* [SMS message sending](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): Fundamentals of SMS sending at Braze, including the importance of subscription groups, requirements for SMS segments and message bodies, and more.

### Considerations

When SMS and MMS are set up across multiple instances, misconfiguration can cause campaign or Canvas opt-outs to be sent to the wrong workspace.

* Braze has monitoring in place to identify such instances. If this behavior is flagged, Braze redirects opt-outs to the correct instance and backfills any opt-outs that occurred during the period.
* We strongly recommend customers test opt-outs for each subscription group they have in Braze. Identifying this issue before launching a message is better than mitigating after an issue has been identified.

Braze manages SMS/MMS subscriptions at both the user profile (`user_id`) level and the phone number (`channel_id`) level. When a phone number is opted-in or out, the update applies to all profiles which share that number. In the case where an end user opted-in with a certain phone number, but then changes phone number, the new phone number inherits the subscription group status of the user. Accordingly, if an end user has opted-out, but then re-enters the app or website with a new phone number, they do not receive unwanted messages.

## Phone number list hygiene recommendations

Maintaining phone number list hygiene helps you keep valid consent and reachability data over time. Braze marks some phone numbers as invalid to help reduce compliance risk, support consent-based messaging practices, and avoid sending to numbers that may no longer belong to the original user.

For reasons why phone numbers are typically marked invalid, see [Handling invalid phone numbers](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

We recommend the following workflow to remove invalid phone numbers:

1. Identify impacted phone numbers through the [`/sms/invalid_phone_numbers` endpoint](https://www.braze.com/docs/api/endpoints/sms/get_query_invalid_numbers).
2. Differentiate between phone numbers that are deactivated, marked invalid due to provider errors, and marked invalid due to formatting issues (`invalid_format`, such as non-E.164 numbers). Use the `reason` filter on the invalid phone numbers API to query by category. For more information, see [Handling invalid phone numbers](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).
3. For deactivated phone numbers, re-verify the phone number with the user. After the user confirms their phone number, remove the phone number from the invalid list through the [`/sms/invalid_phone_numbers/remove` endpoint](https://www.braze.com/docs/api/endpoints/sms/post_remove_invalid_numbers).

## Traffic pumping recommendations

### What is traffic pumping?

Traffic pumping is a form of fraud that occurs when a bad actor uses an online form to trigger SMS messages to be sent at high volume (for example opt-in messages or one-time passwords). The bad actor sets up a premium rate phone number for these messages to be sent to and claims a revenue share from the mobile operator with which the premium rate number has been set up, thus generating illicit revenue.

### How to spot traffic pumping

* Premium rate numbers supporting this kind of scam are often, but not always, set up in countries outside of your normal sending geographies.
* Unusual spikes in sending of messages from online forms might indicate traffic pumping.
    * We recommend setting up [campaign alerts](https://www.braze.com/docs/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) to cap and notify if an implausibly high number of messages are sent.
* Incomplete online forms can indicate programmatic form filling.
* When building online forms, we recommend setting rules to ensure forms are fully complete and use tools such as CAPTCHA to minimise risk.

### Impact of traffic pumping

Customers are responsible for monitoring the traffic that they are sending and are invoiced for all SMS sent through their account. Between Braze and Customer, Customer is the party in the better position to detect and prevent traffic pumping.

## Multi-country SMS sending

Some brands may wish to send to a group of users that have phone numbers from different countries. In order to send an SMS message to a phone number in a particular country, it is best practice to use a long code or short code that is from the same country. In fact, short codes can only send SMS to phone numbers from the same country the short code was created in. 

To overcome this limitation, during the subscription groups [setup process](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups), groups can be set up to hold long and short codes from multiple different countries. When completed, phone numbers with the same country code as the target user's phone number are automatically used when launching a campaign. You don't need to create separate campaigns for users with phone numbers with different country codes, allowing you to launch one campaign or use one Canvas component to target relevant users.

![SMS payloads are sent using the same country code as the target user's phone number.](https://www.braze.com/docs/assets/img/sms/multi_country_subgroups.png?3ec2053263d96c3d56d7e42047e6da2d)

### General sending best practices

1. **Get permission.** One of the most important rules for using SMS as a business is that you must first gain permission from customers to contact them. Failing to do so can damage your brand and result in hefty legal fees.
2. **Choose the right number for your use case.** Three main types of phone numbers can send and receive SMS messages: long codes, short codes, and alphanumeric sender IDs, and their capabilities and availability in different regions vary. Think in advance if your business is served better with a vanity code.
3. **Pay attention to timing.** Keep in mind that customers are more responsive to materials that are addressed directly to them. A little personalization goes a long way, such as using the recipient's first name or adding a conversational touch that reflects your customers' interests.
4. **Engage in two-way conversations.** SMS is such an effective channel for engaging with customers that it's important to anticipate and effectively handle responses to your messages. 85% of consumers not only want to be able to receive information but also reply to businesses or engage in a conversation.
5. **Measure what works.** Are you reaching customers at the right time, with the best frequency, and using the most effective calls to action? Using the right tracking tools can offer direct and measurable metrics that prove their ROI. 

## High-volume sending

Plan on doing some high-volume sending? We have some best practices for you to ensure it runs smoothly.

- Adjust the delivery speed rate limiting for your campaign or Canvases as needed, based on target audience size. This ensures that you reach the send volume that you need and that Braze sends messages at the rate your SMS or RCS provider expects and can handle.
- Ensure you stick to the 160-character limit, and be aware of special characters double-counting (for example, forward-slashes `\`, carets `^`, and tildes `~`). 

## Comply with SMS sending times {#comply-with-sms-sending-times}

Many markets restrict when you can send marketing SMS, MMS, and RCS messages. Those windows are measured in each recipient's local time, and they can differ by country and by US state. Braze applies one quiet hours window per channel and cannot vary that window by day of week. Set the **SMS/MMS/RCS** window to the strictest rules that apply to your audience.

**Warning:**


This section is not intended to provide, nor may it be relied upon as providing legal advice. Time-of-day rules change and can differ by message type. Work with your legal counsel to confirm the hours that apply to your program.



### Recommended window

For a US national audience, set [workspace quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) for **SMS/MMS/RCS** from 8 pm–12 pm. That allows sending from 12 pm–8 pm in each user's local time.

This is the strictest window you can set in Braze:

- Texas Senate Bill 140 (SB 140) starts Sunday sending at 12 pm (noon)
- Several US states end sending at 8 pm rather than 9 pm

If you only send to Texas, a 9 pm–12 pm quiet window covers SB 140: Sunday sending is 12 pm–9 pm, and Monday through Saturday sending is 9 am–9 pm. Because Braze can't set Sunday-only hours, the 9 pm–12 pm quiet window is the correct Texas mapping. However, the 8 pm–12 pm workspace default is stricter and also covers 8 pm evening cutoffs.

### Regulations by market and state

The following examples show how common rules map to a quiet hours window. This table is not exhaustive. Confirm current requirements with your legal counsel.

| Market or rule | Allowed sending hours (recipient local time) | Quiet hours window that covers it |
| --- | --- | --- |
| US federal (Telephone Consumer Protection Act, or TCPA) | 8 am–9 pm | 9 pm–8 am |
| Texas (SB 140) | Monday–Saturday 9 am–9 pm; Sunday 12 pm–9 pm | 9 pm–12 pm (covers the Sunday noon start every day) |
| Several US states (for example, Florida) | 8 am–8 pm | 8 pm–8 am |
| Brazil | 9 am–9 pm | 9 pm–9 am |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS sending time regulations by market and state" }

Use 8 pm–12 pm quiet hours (sending 12 pm–8 pm) as the workspace default when one window must cover these examples together.

### Set up SMS quiet hours

Use [workspace quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) to apply the window to every SMS, MMS, and RCS campaign and Canvas in the workspace.

1. Go to **Settings** > **Quiet Hours**.
2. Select **Add quiet hours**.
3. Select **SMS/MMS/RCS**, then set the start time to 8 pm and the end time to 12 pm.
4. Save your changes.

Workspace quiet hours is currently in early access. If you don't have access, set the same 8 pm–12 pm window on each campaign or Canvas. For permissions, precedence, held-message behavior, and API campaigns, see [Workspace quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours).

### Abort or hold by delivery type

Workspace quiet hours don't always hold a message for later delivery. The outcome depends on how the message is sent. For the full rules, see [What happens to a held message](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours#what-happens-to-a-held-message).

| Delivery type | During the quiet hours window |
| --- | --- |
| Scheduled campaign (fixed send time) | Aborted. A scheduled SMS set for 9 am under the recommended 8 pm–12 pm window is discarded. Braze doesn't deliver it at noon when the window ends. |
| API campaign | Aborted. |
| Action-based campaign | Held and sent at the next available time, by default. |
| Canvas | Held and sent at the next available time, by default. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quiet hours abort or hold by delivery type" }

### Optional Liquid abort

You can add a Liquid check in a Content Block as an additional safeguard. This aborts the send before carrier handoff, which cancels the message.

Include the following snippet at the top of your SMS message body. This example aborts the send outside a 12 pm–8 pm window in the user's [local time zone](https://www.braze.com/docs/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer).


```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour >= 20 or hour < 12 %}
  {% abort_message("Outside allowed time window") %}
{% endif %}
```


- `time_zone: ${time_zone}` evaluates the window against each user's local time, not a fixed global time, as explained in the [Campaigns FAQ](https://www.braze.com/docs/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer).
- Messages suppressed by `abort_message()` are canceled. Workspace quiet hours abort or hold the send depending on delivery type. For details, see [Abort or hold by delivery type](#abort-or-hold-by-delivery-type).
- By default, aborted messages are not visible in standard campaign reporting. When Liquid aborts a send with `{% abort_message %}`, review the send in [Messaging Observability](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder/messaging_observability). These aborts use the **Liquid abort** outcome. You can pass a reason string, such as `{% abort_message('language was nil') %}`.

### Considerations

- Quiet hours apply in each user's local time zone, not your company's time zone.
- A campaign or Canvas-level quiet hours window always takes precedence over the workspace default. A looser custom window can send outside the compliance hours you configured at the workspace.
- Time-of-day rules typically apply to marketing and solicitation messages. Workspace quiet hours apply to all SMS on the channel except auto-responses, test sends, and seed groups. If your legal counsel says transactional campaigns should send overnight, opt those campaigns out of quiet hours.
- Quiet hours control when Braze hands the message to the carrier, not the moment it arrives on the device. For example, a message handed off at 7:59 pm may land after 8 pm. Starting quiet hours at 8 pm provides a buffer before 9 pm cutoffs such as TCPA and Texas SB 140.
