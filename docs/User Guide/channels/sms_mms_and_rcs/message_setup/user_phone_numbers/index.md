# User phone numbers

> This article covers different topics around your users' or customers' phone numbers. If you're looking for information about your own numbers, go to our article on [sending phone numbers](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup).

## Recommended format

Import phone numbers in [`E.164`](https://en.wikipedia.org/wiki/e.164) format (`+`, country code, then subscriber number). That format keeps numbers accurate when you send to more than one country—even for U.S. numbers.

- **U.S. numbers:** Use a valid 10-digit number with a valid area code. You can omit `+1` for valid U.S. numbers; Braze maps them as U.S. Puerto Rican numbers still require a `+` and country code, even though they use 10-digit formatting with U.S.-style area codes.
- **Non-U.S. numbers:** Always include a leading `+` and the country code. For example, `+442079460100` or `+6591234567`.

### How Braze normalizes numbers without a country code

When you import a phone number onto a user profile without a leading `+`, Braze coerces it to E.164 with Google's [libphonenumber](https://github.com/google/libphonenumber). By default, Braze first tries to parse the number as a United States number. If that parse is valid, Braze stores the number with country code `+1`.

Braze does not use your workspace country, the user's `country` attribute, or other profile fields when deciding to treat the number as a U.S. number. A local number from another country that also looks like a valid 10-digit U.S. number can therefore be stored as `+1…` instead of the intended country.

If the number is not a valid U.S. number, Braze attempts a more general parse (for example, a value that already includes a country code but is missing `+`).

**Important:**


To avoid incorrect country codes, always import non-U.S. numbers in E.164 with `+` and the country code.



![Example of a valid E.164 phone number.](https://www.braze.com/docs/assets/img/sms/e164.png?76830497cb02adfbc8c4b8f89ac642ad){: style="max-width:50%;border: 0;"}

Here are a few examples showing the differences between local and `E.164` formatting:

| Country | Local | Country Code | `E.164` |
|---|---|---|---|
| USA | `4155550100` | 1 | `+14155550100` |
| UK | `2079460100` | 44 | `+442079460100` |
| Brazil | `1155256325` | 55 | `+551155256325` |
| Singapore | `91234567` | 65 | `+6591234567` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="E.164 phone number format examples" }


## Import phone numbers

When importing phone numbers, it's important that you follow the [recommended format](#recommended-format). To import phone numbers, use one of the following methods:

- [Uploading a CSV to Braze](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users#constructing-your-csv)
- [Using the `/users/track` endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track)

**Important:**


User phone numbers appear in Braze as a string of digits. If you import a number that contains non-digits (such as `,`, `-`, or `(`) other than the leading `+`, the non-digits are removed when rendered in Braze. For example, importing `+1 (724) 123-4567` appears as `+17241234567`.



## Phone number validation

Braze uses Google's [libphonenumber](https://github.com/google/libphonenumber) library to validate phone numbers. When new mobile number prefixes are introduced, support is added as the upstream library is updated. Braze does not maintain a separate list of valid prefixes.

### Handling invalid phone numbers

When a phone number is deemed invalid, Braze marks the user's phone number as invalid and does not attempt to send further communications to that phone number. An invalid phone number is marked in the **Engagement Tab** of a user profile.

![Example error message for invalid phone numbers in Braze.](https://www.braze.com/docs/assets/img/sms/invalid_banner.png?acd136e17bd69df65880b93bb7d0dd74){: style="max-width:50%;border: 0;"}

A phone number is considered invalid for the following reasons:

- **Provider Error**: a permanent error was received from the SMS and RCS provider. This indicates that the phone number supplied is incorrectly formatted or permanently unable to receive SMS or RCS messages.
- **Deactivated**: the phone number has been deactivated due to a mobile subscriber terminating their service and releasing their number from their carrier (and may eventually be recycled and assigned to a new user). A deactivated phone number can be marked invalid even if you have not sent any SMS or RCS messages to that phone number.
- **Invalid Format**: the number failed formatting validation, such as a non-E.164 value (`invalid_format`).

These invalid phone numbers can be managed through [SMS and RCS endpoints](https://www.braze.com/docs/api/endpoints/sms). To return numbers by reason, use the `reason` filter on the [Query invalid phone numbers](https://www.braze.com/docs/api/endpoints/sms/get_query_invalid_numbers) endpoint.

**Note:**


If multiple user profiles have the same phone number and that phone number is marked invalid, then all existing User Profiles with that number will display as invalid. Newly created user profiles will never initially be marked as invalid.



You can also include or exclude any users with invalid phone numbers when [creating a segment](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment#step-4-add-filters-to-your-segment).

## Exclude rejected SMS sends from segmentation

**Important:**


SMS rejections may count toward your SMS allotment depending on your Braze contract and SMS provider. For billing outcomes, see [Reporting](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/reporting).



To exclude users with rejected SMS sends from your segments, use [SQL Segment Extensions](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments), do the following:

1. Go to **Audience** > **Segment Extensions**.
2. Select **Create New Extension** > **Full refresh** or **Incremental refresh**.
3. Write a SQL query that identifies users with SMS rejections. For example, you can query the `USERS_MESSAGES_SMS_REJECTION_SHARED` event to find users who have received SMS rejections.
4. Save your Segment Extension.
5. When creating your SMS segment, add a filter to exclude users in this Segment Extension.

## Add users to SMS and RCS subscription groups

For a user to receive an SMS or RCS message, they must have a valid phone number and be opted-in to a subscription group. Subscription groups are tied to the SMS or RCS program you are running (make sure you follow the [legal requirements for SMS, MMS, and RCS](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) and have recorded consent for each customer). For more information, refer to [SMS and RCS subscription groups](https://www.braze.com/docs/sms_rcs_subscription_groups).

## Third-party sourcing and verification

Braze relies on third-party tools to source invalid numbers. Braze is not responsible for any outages or misinformation of these services. Thus, this tool should not be relied upon as your sole method of compliance for verifying invalid numbers.

## Phone number capture

To capture phone numbers through in-app messages, refer to [SMS, RCS, and WhatsApp sign-up form](https://www.braze.com/docs/phone_number_capture).
