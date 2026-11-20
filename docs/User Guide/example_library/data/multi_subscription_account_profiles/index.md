# Model multi-subscription accounts with subscription-level profiles

> Give each subscription under a shared customer account its own Braze user profile, linked by an account ID custom attribute, so you can message and report at the subscription level while still grouping profiles that belong to the same account.

## About this example

StyleRyde is a fictional on-demand ridesharing brand where one customer account can hold multiple subscriptions. For example, a household plan can cover several riders, each with a unique phone number. Consumers log in once at the account level, then choose which subscription (phone line) to manage.

StyleRyde needs to do the following:

- Send service SMS to the phone number on a specific subscription.
- Send marketing push and Content Cards to the device session for the active subscription.
- Keep push and SMS marketing preferences, push and SMS engagement history, and Currents data at the individual subscription level.
- Group related subscriptions for account-level reporting and journeys.

Braze models engagement around the [user profile](https://www.braze.com/docs/user_guide/data/unification/user_data/user_profile_lifecycle). Email, phone, preference attributes, and channel history live on that profile. For multi-subscription accounts, treat each subscription as its own user profile, then group profiles with a shared `account_id` custom attribute. Think of users grouped by account ID, rather than a single account object that contains users.

This example covers the subscription-level profiles pattern. Use it when each subscription has (or can have) a stable unique ID that your app can pass to `changeUser()`.

## Considerations

- **Active user ID:** Call [`changeUser()`](https://www.braze.com/docs/developer_guide/analytics/setting_user_ids) with the subscription ID when a consumer logs in or switches subscriptions. The SDK associates one active user ID per session.
- **Shared account IDs:** Don't call `changeUser()` with a shared account ID for all subscriptions on a device. That mixes engagement across people and breaks logout and re-engagement. See [How changeUser() works](https://www.braze.com/docs/developer_guide/analytics/setting_user_ids#how-changeuser-works).
- **Shared email addresses:** Multiple profiles can share one address. Before you rely on shared inboxes, review the [email FAQ](https://www.braze.com/docs/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address) and [email subscription state](https://www.braze.com/docs/user_guide/channels/email/subscriptions#checking-email-subscription-state).
  - **Email opt-in:** Opt-in follows the address. A change on one profile copies to up to 100 other profiles with the same address. Push and SMS preferences can still differ by subscription when phone numbers are unique.
  - **Email deduplication:** Braze deduplicates segment-based scheduled sends to a shared address. Named-recipient and later Canvas steps can still send to that address more than once.
  - **Email engagement:** Deliveries, opens, clicks, and spam reports are recorded on each matching profile (up to 100), and Braze personalizes the send for the one profile it selects.

**Important:**


Don't put content that's specific to one subscription (such as a phone line or plan details) in an email to a shared address. Braze personalizes that email for the one profile it selects. Send that content through push, SMS, or Content Cards, or give each subscription its own email address.



- **SMS phone numbers:** Use a unique phone number on each subscription profile when SMS is your service channel. Phone is stored on the profile you target for SMS.
- **Push tokens:** Push tokens belong to one profile per device. See [Step 3](#step-3-identify-the-active-subscription-in-the-sdk) for what happens when a consumer switches subscriptions.
- **Account rollups:** Account-level rollups (for example, "any subscription on this account purchased a monthly pass") need a warehouse or Currents join on `account_id`. An `account_id` segment filter returns each profile with that value.
- **Billing:** Each subscription profile counts as a separate profile toward your monthly active users (MAU) and data point usage, as described in [Billing](https://www.braze.com/docs/user_guide/administer/global/billing) and [Data points (Legacy)](https://www.braze.com/docs/user_guide/data/infrastructure/data_points).

## Setup

### Step 1: Define identifiers

Map your CRM identifiers to Braze as follows.

| Concept | StyleRyde example | Braze field |
| --- | --- | --- |
| Account (login and billing) | Household account `acct_12345` | Custom attribute `account_id` (string) on every related profile |
| Subscription (individual line) | Rider subscription `sub_12345_1` | Profile `external_id` |
| Contact email | Shared household email | Profile `email` (may repeat across profiles) |
| Contact phone | Unique per subscription | Profile `phone` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Map account and subscription identifiers to Braze" }

Use a stable, unique subscription ID as `external_id`. Keep the account ID as a custom attribute so you can segment and join related profiles without collapsing them into one Braze user.

### Step 2: Create one profile per subscription

Create or update each subscription through the SDK or the [`/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) endpoint. Include at least the following:

| Field | What to store |
| --- | --- |
| `external_id` | Subscription ID |
| `email` and `phone` | Contact fields when captured |
| `account_id` | Shared account identifier |
| Role or ownership attributes | For example, `is_account_owner` |
| Push and SMS marketing preference attributes | Values you need for segmentation. Email opt-in is managed with [email subscription states and groups](https://www.braze.com/docs/user_guide/channels/email/subscriptions), which apply per address. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fields to include on each subscription profile" }

Example profile layout for two StyleRyde accounts:

| Attribute | Profile A | Profile B | Profile C | Profile D |
| --- | --- | --- | --- | --- |
| `external_id` (subscription) | `sub_12345_1` | `sub_12345_2` | `sub_12345_3` | `sub_789_1` |
| `account_id` | `acct_12345` | `acct_12345` | `acct_12345` | `acct_789` |
| `email` | `alex@example.com` | `alex@example.com` | `alex@example.com` | `riley@example.com` |
| `phone` | `+15555550101` | `+15555550102` | `+15555550103` | `+15555550901` |
| `is_account_owner` | `false` | `true` | `false` | `true` |
| `marketing_sms_opt_in` | `true` | `true` | `false` | `false` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Example subscription-level profiles for two accounts" }

Each column is a separate Braze user. Profiles A to C share `account_id` `acct_12345` but keep distinct phones, SMS preferences, and SMS and push engagement history. Because they share `alex@example.com`, they also share one email subscription state and email engagement.

Example `/users/track` attribute payload for one subscription:

```json
{
  "attributes": [
    {
      "external_id": "sub_12345_2",
      "email": "alex@example.com",
      "phone": "+15555550102",
      "account_id": "acct_12345",
      "is_account_owner": true,
      "marketing_sms_opt_in": true
    }
  ]
}
```

### Step 3: Identify the active subscription in the SDK

When the consumer logs in or switches which subscription they are managing, call `changeUser()` with that subscription's `external_id`.

```javascript
// After the consumer selects subscription sub_12345_2 in the StyleRyde app
braze.changeUser("sub_12345_2");
```

Push tokens, Content Cards, and in-app messages then follow the active subscription profile for that session. If the consumer switches to another subscription in-app, call `changeUser()` again with the new subscription ID.

When a profile registers a device's push token, Braze removes that token from every other profile on the same device. In practice, an account owner who switches between subscriptions on one phone receives push only for the subscription they selected last. Push messages aimed at the other subscriptions don't reach that phone.

### Step 4: Align channels with profile fields

| Channel | Target using |
| --- | --- |
| SMS (service) | `phone` on the subscription profile you intend to reach |
| Email | Use `email` on the profile. Profiles that share an address also share email subscription state, and some sends are deduplicated, as described in [Considerations](#considerations). |
| Push and Content Cards | The profile currently set with `changeUser()` on the device. The device's push token belongs only to the profile that registered it last. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Align messaging channels with subscription profile fields" }

For account-owner-only journeys (for example, billing reminders), filter where `is_account_owner` is `true` and the relevant `account_id` or subscription attributes.

### Step 5: Segment and report with account and subscription attributes

- Build subscription-level segments with phone, push and SMS marketing preferences, and subscription-specific custom attributes.
- Build account-scoped audiences with the `account_id` filter (for example, all subscriptions where `account_id` equals `acct_12345`). This filter selects each profile with that value.
- Use Currents and user-level analytics on each subscription profile for engagement reporting. Join on `account_id` in your warehouse when you need household rollups, such as "account X has a profile that purchased a monthly pass".
- Email deliveries, opens, clicks, and spam reports can be stored on more than one profile that shares an address, so account for that when you join on `account_id`, as described in [Considerations](#considerations).

## Related articles

<ul class="guide_tiles"><li><a href="/docs/developer_guide/analytics/setting_user_ids"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Set user IDs</span></span></div></a></li><li><a href="/docs/user_guide/data/unification/user_data/user_profile_lifecycle"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">User profile lifecycle</span></span></div></a></li><li><a href="/docs/api/endpoints/user_data/post_user_track"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">POST: Create and update users</span></span></div></a></li><li><a href="/docs/user_guide/data/activation/attributes/custom_attributes"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Custom attributes</span></span></div></a></li><li><a href="/docs/user_guide/channels/email/faq"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Email FAQ</span></span></div></a></li></ul>
