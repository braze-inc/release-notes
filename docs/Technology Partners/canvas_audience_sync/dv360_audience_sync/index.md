# Audience Sync to Google DV360

> The Braze Audience Sync to Google Display & Video 360 (DV360) feature extends the reach of your cross-channel customer journeys to DV360 placements across display, video, connected TV (CTV), and audio. Use your first-party customer data to securely deliver ads based on dynamic behavioral triggers, segmentation, and more.

Braze sends audience updates to DV360 through Google's Data Manager API with Customer Match.

**Note:**


Audience Sync to DV360 differs from [Audience Sync to Google](https://www.braze.com/docs/partners/canvas_audience_sync/google_audience_sync/) in two ways:
<br><br>
- Every DV360 connection uses Data Manager, so there is no legacy Ads API option like there can be for Google Ads.
- DV360 uses a separate Technology Partners connection from Google Ads, so you can select DV360 advertisers in Canvas.



## Common use cases for Audience Syncing

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand


## Prerequisites




**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





Make sure the following items are created, completed, or accepted before setting up your Google DV360 Audience Sync step in Canvas.

| Requirement | Origin | Description |
| --- | --- | --- |
| DV360 advertiser access | [Google DV360](https://support.google.com/displayvideo/) | An active DV360 advertiser (or partner access to one) tied to your brand. Your Google account must have permission to view advertisers in DV360. Braze discovers advertisers through the Display & Video 360 API. |
| Google Customer Match eligibility | [Google](https://support.google.com/google-ads/answer/6299717) | DV360 audience syncing uses Customer Match through the Data Manager API. Your Google account must meet Google's Customer Match requirements, including policy compliance, payment history, and spend thresholds. |
| Google Terms & Policies | Google | Agree to comply with applicable Google advertising terms and policies, including the [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/) when syncing EEA, UK, and Switzerland users. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

For consent attributes (`$google_ad_user_data` and `$google_ad_personalization`), EU User Consent Policy requirements, and SDK minimum versions, see [Audience Sync to Google](https://www.braze.com/docs/partners/canvas_audience_sync/google_audience_sync/#collecting-consent-for-eea-uk-and-switzerland-end-users).

## Integration

### Step 1: Connect Google Display & Video 360

**Important:**


You must have the ["Admin" permission](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/#admin) to connect Google Display & Video 360 to your Braze account.



1. In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** > **Google Display & Video 360**. 
2. In the **Google Display & Video 360 Audience Sync** section, select **Connect Google Display & Video 360**.
3. After you're redirected to Google OAuth to authorize Braze, grant both permissions when prompted:
- **Send audience data** (Data Manager API)
- **Read advertiser list** (Display & Video 360 API)
4. After authorization, select the DV360 advertisers you want to sync from in this workspace, then save your selection.

**Note:**


DV360 advertisers are listed by **Advertiser** name and **Advertiser ID**. You can filter by advertiser name or ID. If both permissions are granted and no advertisers appear, confirm your DV360 account role and access—reconnecting alone cannot fix a missing DV360 role.



To introduce new DV360 advertisers later, select **Refresh Accounts** on the partner page. Refreshing may disrupt active Canvases that use a Google Display & Video 360 Audience Sync step.

#### Export iOS IDFA or Google Advertising IDs

If you plan to export mobile advertising IDs in your audience sync, enable **Add Mobile Advertising IDs** on the Google Display & Video 360 partner page and enter your iOS app ID and Android app ID (app package name). For setup details, see [Export iOS IDFA or Google Advertising IDs](https://www.braze.com/docs/partners/canvas_audience_sync/google_audience_sync/#export-ios-idfa-or-google-advertising-ids) in the Google Audience Sync guide.

### Step 2: Add a Google DV360 Audience step in Canvas

Add a component in your Canvas, then select **Audience Sync**. Select **Google DV360** as the Audience Sync partner.

### Step 3: Sync setup

1. Select the DV360 advertiser to sync to.
2. In the **Choose a New or Existing Audience** dropdown, enter the name of a new or existing audience.
3. Select whether to add users to or remove users from the audience.
4. Select a field to match: **Customer Contact Info** (email, phone, or both) or **Mobile Advertiser ID** (iOS IDFA or Android GAID).

**Important:**


You cannot combine customer contact information and mobile advertiser IDs in the same Customer Match audience. For more details, see [Google Customer Match requirements](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).



For step-by-step screenshots of creating or syncing to an existing audience, see [Sync setup](https://www.braze.com/docs/partners/canvas_audience_sync/google_audience_sync/#step-3-sync-setup) in the Google Audience Sync guide—the Canvas workflow is the same, except you select **Google DV360** and a DV360 advertiser.

### Step 4: Launch Canvas

After you configure your Google DV360 Audience Sync step, complete the remainder of your Canvas and launch. Users sync as they enter the Audience Sync step.

## Frequently asked questions

### How long does it take for audiences to populate in DV360?

Audience updates are typically processed within 6 to 12 hours, similar to [Audience Sync to Google](https://www.braze.com/docs/partners/canvas_audience_sync/overview/).

### Can I use the same Google account for Google Ads and DV360?

Yes. DV360 uses the same Google OAuth application as Google Ads, but you connect it from the separate **Google Display & Video 360** Technology Partners page. Each connection maintains its own advertiser allowlist for the workspace. Consent is incremental: if you already granted Google Ads scopes, those grants are kept when you authorize DV360.

### What if I only granted one Google permission?

Braze requires both **Send audience data** and **Read advertiser list** to discover advertisers and sync audiences. Use **Grant permissions** on the Google Display & Video 360 partner page to complete OAuth consent. Audience syncs also require the Display & Video 360 scope on the DV360 connection.
