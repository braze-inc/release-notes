# User phone numbers

> This article covers different topics around your users' or customers' phone numbers.

Phone numbers are shown in the user profile in local formats, but will not be in the format you use to import the number (`(724) 123 4567`).

## Importing phone numbers

You can import phone numbers by [uploading a CSV](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users#constructing-your-csv) or [via API](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) to create a user.

<a id="formatting"></a>
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


If Braze cannot coerce a number into a valid E.164 value, it cannot send WhatsApp messages to that number. Users with phone numbers that are not formattable automatically exit a Canvas step that includes WhatsApp.

### Adding users to WhatsApp a subscription group

For a customer to receive an WhatsApp message, they must have a valid phone number and be opted-in to a subscription group. For more information, refer to [WhatsApp subscription groups](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).


### Multiple users with the same phone number

#### Outbound sends

If multiple users have the same phone number within a segment of a single campaign or Canvas step, Braze deduplicates the sending and sends only one message to that phone number.

#### Inbound messages

When multiple user profiles share the same phone number, Braze uses the following tiebreak logic to determine which profile receives attribution for an inbound WhatsApp message:

1. If the message is attributed to a campaign, Braze attributes the inbound WhatsApp message to the profile that most recently received that campaign on WhatsApp. If no profile received that campaign on WhatsApp, Braze uses the profile that most recently received that same campaign on another channel (such as email or SMS).
2. Otherwise, Braze attributes the message to the profile that most recently received a campaign from the associated WhatsApp subscription group that sent anything in the last seven days on WhatsApp. If no profile received one of those campaigns on WhatsApp, Braze uses the profile that most recently received one of those same campaigns on another channel.
3. Otherwise, Braze attributes the message to the profile with the `phone` user alias for the sender's phone number—the first profile to have sent an inbound WhatsApp message from that number.
4. Otherwise, Braze attributes the message to the first matching profile Braze finds. This choice may not be consistent across inbound WhatsApp messages from the same phone number.

To prevent duplicate profiles from forming when users share phone numbers, use the [users/merge endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_users_merge) to consolidate user data.


