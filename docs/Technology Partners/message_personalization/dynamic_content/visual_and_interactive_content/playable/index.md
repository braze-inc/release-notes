# Playable

> [Playable](https://playable.video) allows you to add auto-play video content to your Braze email campaigns through reusable Braze Content Blocks.

_This integration is maintained by Playable._

## About the integration

The Braze and Playable integration allows you to deliver high-quality video content that plays automatically within the inbox. Playable automatically optimizes video delivery based on the recipient's email client, device, screen size, and network conditions.

Videos are exported directly to Braze as **Content Blocks**, making them reusable across multiple email campaigns.

**Important:**


Embedded videos are not natively supported by many email clients and can significantly increase email size, which may cause messages to be marked as spam. Playable addresses this by delivering optimized video content with appropriate fallbacks for different email clients. For more details about video in email, see [Can I embed videos in emails?](https://www.braze.com/docs/user_guide/channels/email/faq/#can-i-embed-videos-in-emails)



## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Playable Account | A Playable account is required. If you don't have one, [sign up for a Playable account](https://playable.video). |
| Braze API Key | A Braze REST API key with `content_blocks.create` and `content_blocks.update` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST Endpoint | Your Braze instance REST endpoint, such as `https://rest.iad-01.braze.com`. <br><br> Your endpoint will depend on the [Braze URL for your instance](https://www.braze.com/docs/api/basics/#endpoints). |
| Video Content | Videos uploaded to Playable or imported from supported sources such as Facebook, Instagram, YouTube, X (formerly Twitter), and TikTok. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Implementation

### Step 1: Connect your Braze account

1. Log in to [Playable](https://playable.video).
2. Select **Braze** as the integration platform.
3. Enter your Braze credentials:
   - **API Key:** Your Braze REST API key.
   - **REST Endpoint:** Your Braze instance REST endpoint.

![Enter your Braze API Key and REST Endpoint in Playable][1]{: style="max-width:50%;"}

{:start="4"}
4. Click **Continue to Dashboard**.

**Tip:**


Create a dedicated Braze API key for the integration and grant only the required `content_blocks.create` and `content_blocks.update` permissions.



### Step 2: Select a video

After connecting your Braze account, you'll see the videos available in your Playable library.

![Select a video from your Playable library][2]{: style="max-width:50%;"}

1. Preview a video using the **Play** button.
2. Select the video you want to export.
3. Click **Export**.

### Step 3: Export the video to Braze

When exporting a video for the first time:

1. Enter a **Video Title** for the Braze Content Block.
2. Use only alphanumeric characters, hyphens, and underscores in the name.
3. Optionally select **Export as Draft** if you want to review the Content Block before making it active.
4. Click **Confirm**.

![Enter a Video Title for your Content Block][3]{: style="max-width:50%;"}

Playable creates the Content Block directly in your connected Braze account.

**Tip:**


Use descriptive Content Block names that identify the video or campaign, such as `summer_sale_hero_2026`.



### Step 4: Update an existing Content Block

If a video has already been exported to Braze, it is marked with an **Active** badge in Playable.

When exporting it again, you can:

- **Override Existing:** Update the existing Content Block with the latest version of the video.
![Select Override Existing to update an existing Content Block][4]{: style="max-width:50%;"}
- **Create New:** Create a separate Content Block with a new name.
![Select Create New to create a separate Content Block][5]{: style="max-width:50%;"}

Use **Override Existing** when you want to update an existing video without creating duplicates. Use **Create New** when you need a separate version, such as for A/B testing.

### Step 5: Use the Content Block in Braze

1. Log in to your Braze dashboard.
2. Navigate to **Templates** > **Content Blocks**.

![Navigate to Templates then Content Blocks in Braze][6]{: style="max-width:35%;"}

{:start="3"}
3. Find the Content Block created by Playable.
4. Add the Content Block to your Braze email campaign.

Content Blocks can be reused across multiple email campaigns.

## Video compatibility

Playable videos autoplay in 98%+ of inboxes, including:

- iPhone Mail
- Gmail
- Apple Mail
- Outlook for iOS
- Outlook for Android
- Outlook for Mac
- Newer versions of Outlook 365 for Windows
- Yahoo Mail
- AOL Mail

Legacy Outlook for Windows and other clients that do not support autoplay receive an optimized static image or video thumbnail with a play button instead.

**Tip:**


Always test your email across the email clients used by your audience before sending a large campaign.



## Best practices

### Content Block naming

- Use concise, descriptive names.
- Include campaign or date identifiers when useful.
- Use only alphanumeric characters, hyphens, and underscores.
- Avoid creating duplicate Content Blocks when an existing block can be updated.

### Video selection

- Use videos optimized for email; 15–60 seconds is a recommended range.
- Choose a clear thumbnail for fallback scenarios.
- Preview the video before exporting.
- Test the final email across major email clients.

### Content Block management

- Use **Draft** mode when a video requires review before going live.
- Use **Override Existing** to update an existing Content Block.
- Use **Create New** when maintaining separate video variations or A/B tests.
- Regularly review and archive unused Content Blocks in Braze.

### Campaign integration

- Place video content where it is visible early in the email when appropriate.
- Include a clear call to action after the video.
- Test email rendering before launching the campaign.
- Monitor engagement metrics to optimize video placement and content.

[1]: /docs/assets/img/playable/image1.png?9023f891ce979db00d9765711a1a6b02
[2]: /docs/assets/img/playable/image2.png?71c1f092906106639d2ef97d187b3a6a
[3]: /docs/assets/img/playable/image3.png?03d42f8c5248c3e06a89c56152e311d1
[4]: /docs/assets/img/playable/image4.png?1dd72f7b1a76323ac64282a5d2829340
[5]: /docs/assets/img/playable/image5.png?d08e47a1228ea8d17ea6d70c0986baf1
[6]: /docs/assets/img/playable/image6.png?da3d8751a070088356a6feaac97f0fc9
