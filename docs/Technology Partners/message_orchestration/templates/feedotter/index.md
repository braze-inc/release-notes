# FeedOtter

> [FeedOtter](https://www.feedotter.com) is a content-to-email automation platform that turns content from CMSs, websites, feeds, APIs, databases, and spreadsheets into polished emails. FeedOtter collects content and builds the email; Braze manages the audience and delivery, so you can run recurring newsletters without rebuilding each issue. Publish each issue to a Braze email template, send it to the segment you choose, and optionally link the send to a Braze campaign for reporting.

_This integration is maintained by FeedOtter._

## Use cases

- **Automated newsletters and blog digests:** Transform newly published WordPress, Drupal, or CMS content into branded Braze emails.
- **Personalized content notifications:** Match newly published articles, research, or other content to Braze segments.
- **Data-driven emails and alerts:** Turn information from APIs, databases, XML, JSON, spreadsheets, or secure data feeds into recurring Braze communications.
- **Editorial newsletters:** Create complete, ready-to-review newsletters in Braze while allowing editors to curate articles, advertising, and other content before sending.
- **RSS-to-email automation:** Automate traditional RSS and content-feed emails in Braze, with support for multi-source workflows when needed.

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A FeedOtter account | A [FeedOtter account](https://www.feedotter.com) is required to take advantage of this partnership. |
| A Braze REST API key | A Braze REST API key with the following permissions:<br>- `campaigns.list`<br>- `campaigns.details`<br>- `segments.list`<br>- `templates.email.create`<br>- `templates.email.update`<br>- `messages.send`<br>- `messages.schedule.create`<br><br>Create this key in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL](https://www.braze.com/docs/api/basics#endpoints). Your endpoint depends on the Braze URL for your instance. For example, `https://rest.iad-01.braze.com`. |
| A Braze App ID | Any [App ID](https://www.braze.com/docs/api/identifier_types/#app-identifier) in your workspace. Find it under **Settings** > **APIs and Identifiers** > **App Identifiers**. |
| A Braze segment | The audience that receives your newsletter. |
| A Braze campaign (optional) | An API-triggered campaign with an email message. Braze reports metrics for sends linked to a campaign. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integrating FeedOtter

### Step 1: Add a Braze connection in FeedOtter

1. In FeedOtter, go to **Settings** > **Integrations**.
2. Select **Add Integration**, then select **Braze**.

### Step 2: Enter your Braze API credentials

1. Enter a **Connection Label** (optional).
2. Enter your **REST Endpoint**, **API Key**, and **App ID**.
3. Select **Save**.

### Step 3: Confirm the connection to Braze

Select **Test** and confirm the indicator turns green. This confirms FeedOtter can communicate with your Braze account.

## Using FeedOtter with Braze

### Step 1: Configure the send

1. When publishing a newsletter in FeedOtter, select **Braze** and choose your Braze connection.
2. Choose a **Publishing Action**:
   - **Create a new campaign and schedule a send**, or
   - **Create a new template only** to finish sending in Braze.
3. Select a **Segment**.
4. (Optional) Select a **Campaign** to track metrics in Braze.
5. Choose **Send Now**, or **Schedule** with a date, time, and timezone.

### Step 2: Publish and view in Braze

1. Select **Publish**.
2. In Braze, go to **Campaigns** to view your campaign and the sends you orchestrated through FeedOtter.

## Support

For more information, see the [FeedOtter Braze integration documentation](https://docs.feedotter.com/integrations/braze) or contact [support@feedotter.com](mailto:support@feedotter.com).
