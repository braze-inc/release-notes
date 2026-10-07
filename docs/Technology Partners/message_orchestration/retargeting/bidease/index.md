# Bidease

> [Bidease](https://www.bidease.com/) is a mobile demand-side platform (DSP) for app user acquisition and retargeting. The Braze and Bidease integration lets you use your Braze segments as audiences in Bidease campaigns, so you can re-engage lapsed users, reach high-value users, or exclude existing users from acquisition campaigns, with audiences kept in sync with your segments automatically.

_This integration is maintained by Bidease._

## About this integration

Braze holds the most complete picture of who your users are and how they engage with your app. Bidease buys mobile in-app inventory across major exchanges. The integration connects the two: Bidease regularly exports the members of the Braze segments you choose, reads their mobile advertising IDs (IDFA on iOS, GAID on Android), and replaces the matching Bidease audience with the current list.

Because each sync is a full export, users who leave a segment in Braze are also removed from the Bidease audience on the next sync. You keep defining audiences in Braze, and Bidease campaigns always target the current version of each segment. Nothing needs to be configured in Braze beyond creating a REST API key.

## Use cases

- Re-engage lapsed users: Retarget users who have not opened the app in N days, or who churned after onboarding, with paid in-app ads.
- Win back payers: Reach users who purchased before but have not converted recently.
- Suppress existing users: Exclude current or recently active users from acquisition campaigns, so your budget goes to new users only.
- Lifecycle-driven bidding: Run separate campaigns and creatives for segments built on Braze lifecycle stages, engagement scores, or custom attributes.

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A Bidease account | A Bidease advertiser account and an active relationship with your Bidease account team is required to take advantage of this partnership. |
| A Braze REST API key | A Braze REST API key with `segments.list` and `users.export.segment` permissions. <br><br> Create this key in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL](https://www.braze.com/docs/api/basics#endpoints). Your endpoint depends on the Braze URL for your instance. |
| Advertising IDs on user profiles | Bidease matches users by mobile advertising ID. Your app must pass IDFA (iOS) and/or GAID (Android) to Braze, either through the Braze SDK (stored on the user profile's devices) or as a custom attribute. On iOS, IDFA is only available for users who granted App Tracking Transparency permission. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integrate Bidease

### Step 1: Create a Braze REST API key

1. In Braze, go to **Settings** > **API Keys** and select **Create API Key**.
2. Name the key, for example `Bidease`.
3. Under permissions, select `segments.list` and `users.export.segment`. No other permissions are needed.
4. Save the key and copy its value.

### Step 2: Choose the segments to sync

1. In Braze, create or open each segment you want to use in Bidease.
2. Create a separate segment for each platform: one limited to your iOS app and one limited to your Android app. Each Braze segment maps to exactly one Bidease audience for one platform.
3. Copy each segment's API identifier from the segment details page and note its platform (iOS or Android).

### Step 3: Connect your workspace with Bidease

1. Send your Bidease account team the REST API key, your REST endpoint, and the list of segment API identifiers with the platform of each segment.
2. If your app stores advertising IDs in a custom attribute instead of through the SDK, include the attribute name.
3. Bidease connects your workspace, runs the first export, and creates one Bidease audience per segment.
4. Your account team confirms the audience sizes once the first sync completes.

## Customize Bidease

### Sync frequency

By default, Bidease re-exports each segment once a day. Hourly syncs are available on request. Each sync replaces the audience with the segment's current members.

### Advertising ID source

Bidease reads IDFA and GAID from the user's devices (the standard method, collected by the Braze SDK) and, optionally, from a custom attribute you specify. Pass advertising IDs through the Braze SDK when possible.

For setup details, see [IDFA collection for iOS](https://www.braze.com/docs/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) and [Google advertising ID for Android](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).

## Use Bidease with Braze

### Step 1: Target or exclude a Braze audience

1. Tell your Bidease account team which campaigns should use the audience. The Bidease ad operations team attaches it to those campaigns as a targeting audience or as an exclusion list.
2. Use iOS segments for iOS campaigns and Android segments for Android campaigns.

### Step 2: Update your audience in Braze

1. Edit the segment filters in Braze as needed. The next scheduled sync picks up the change automatically.
2. To add a new segment, share its API identifier with your account team.

## Considerations

- Matched audience size: Only users with an advertising ID can be reached. A Bidease audience is usually smaller than the Braze segment, especially on iOS, where IDFA depends on ATT consent.
- One platform per segment: Each Braze segment must contain users of a single platform. To reach the same audience on iOS and Android, create two segments with the same filters, one per app.
- Full replacement: Every sync replaces the whole audience. Users who left the segment are removed on the next sync. If an export returns no valid advertising IDs, Bidease keeps the previous audience instead of emptying it.
- Braze API limits: Exports use the [Users by segment export](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_segment/) endpoint and count toward your workspace's API rate limits. Braze allows one concurrent export per segment.
- Access: Bidease only reads segment lists and segment members. It does not write data to Braze. To stop the integration, delete or revoke the API key in Braze and let your account team know.

## Troubleshooting

- The Bidease audience is much smaller than the segment: Check that your app passes IDFA/GAID to Braze. Users without an advertising ID cannot be matched.
- The sync fails with an authorization error: Confirm the API key is active and has both `segments.list` and `users.export.segment` permissions, and that the REST endpoint matches your instance.
- A segment is not found: Confirm the segment API identifier and that the segment belongs to the workspace the API key was created in.
- For any other issue: Contact your Bidease account team.
