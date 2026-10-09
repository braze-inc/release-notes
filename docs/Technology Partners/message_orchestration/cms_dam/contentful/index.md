# Contentful

> [Contentful](https://www.contentful.com/) is a headless content management system that lets teams create, manage, and distribute structured content to any channel. The Braze app for Contentful connects that content directly to your Braze messaging: you can pull Contentful entries into messages dynamically at send time with Connected Content, or sync selected fields into Braze Content Blocks for reuse across campaigns and Canvases.

_This integration is maintained by Contentful._

## About this integration

This page covers how to configure the Braze app in Contentful and how to use Contentful assets in Braze. With this integration, you can:

* Generate a ready-to-paste Braze Connected Content call for a published entry, along with the Liquid tags needed to reference each field in a Braze message.
* Sync selected fields from an entry into a Braze Content Block, with a chosen locale, so the content is available natively in the Braze dashboard.

The result is a single source of truth for content. Content editors keep working in Contentful with their existing review and localization workflows, and marketers build campaigns in Braze against content that is already approved and current.

## Prerequisites

Before you start, you need the following:

| Requirement | Description |
| --- | --- |
| A Contentful account | A Contentful account with Space Admin access to the space where you install the app. |
| A Contentful API key | A Contentful Content Delivery API (CDA) key with read access. Create this in Contentful from **Settings** > **API keys**. |
| A Braze REST API key | A Braze REST API key with the `content_blocks.create`, `content_blocks.update`, `content_blocks.info`, and `content_blocks.list` permissions. Create this key in the Braze dashboard from **Settings** > **API Keys**. Required for Content Block syncing only. |
| A Braze REST endpoint | [Your Braze REST endpoint URL](https://www.braze.com/docs/api/basics#endpoints). Your endpoint depends on the Braze URL for your instance. Required for Content Block syncing only. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Install the Braze app in Contentful

1. Log in to the Contentful web app.
2. Select **Apps** > **Marketplace**.
3. Locate the **Braze** app and select it.
4. Select **Install**. The **Manage app access** window appears.
5. Under **Environments**, select the environments you want the app installed in.
6. Select **Authorize access**. The app configuration screen appears.
7. In **Contentful API key**, enter your Content Delivery API key.
8. To enable Content Block syncing, enter your Braze REST API key and select your Braze REST endpoint.
9. Select **Install to selected environments**.

**Note:**


If you see an error stating that a valid Contentful API key is required, check that the key has read access to the Content Delivery API (CDA).



### Step 2: Add the Braze app to a content type

1. In the Contentful web app, go to the **Content model** tab.
2. Select an existing content type, or create a new one.
3. Scroll to the **Sidebar** section.
4. Add **Braze** from the list of available items.
5. Select **Save**.

Repeat this for each content type you want to make available to Braze.

### Step 3: Connect an entry to Braze

1. Go to the **Content** tab and select **Add entry**, choosing a content type that has the Braze app in its sidebar. You can also open an existing entry.
2. Populate the entry fields and **publish** the entry. Braze can only retrieve published content.
3. In the entry sidebar, select **Generate Braze Connected Content** to produce a Connected Content call and Liquid tags to paste into a Braze message, or **Create Content Block** to push selected fields into Braze as a Content Block.

## Sync Content Blocks

### Step 1: Sync an entry to a Braze Content Block

1. Open a published entry that has the Braze app in its sidebar.
2. In the sidebar, select **Create Content Block**.
3. Select the **locale** to use. One Content Block is created per selected locale.
4. Select the **fields** to include in the Content Block.
5. Select **Send to Braze**. The Content Block is created in your Braze workspace and is available under **Content** > **Content Block**.

### Step 2: Keep synced content up to date

Choose the method that matches how often the content changes:

* Content Block syncing suits content that is stable at send time and reused across many messages. It renders without an external call.
* Connected Content suits content that may change between the time a campaign is built and the time it is delivered, because the content is fetched at delivery.

For more information on how the Braze app in Contentful works, see [Contentful's Braze app documentation](https://www.contentful.com/help/apps/braze-app/).

## Use Connected Content

### Step 1: Add the Connected Content call to a Braze message

1. In Contentful, open a published entry and select **Generate Braze Connected Content** in the sidebar.
2. Select the fields to include, then select **Next**.
3. If the entry has multiple locales, select the locales to include, then select **Next**.
4. Copy the generated Connected Content call.
5. In Braze, create or open a campaign or Canvas message.
6. Paste the Connected Content call at the top of the message body.
7. Paste the Liquid tags where the content should appear.

### Step 2: Reference fields with Liquid

JSON dot notation lets you specify what part of the response body from Contentful to include in your message. This varies based on your use case. The app generates the correct Liquid tag for each field. Tags are namespaced by locale when the entry is localized, and by content type when it is not.

| Scenario | Example Liquid tag |
| --- | --- |
| Localized entry (en-US) | `{{response.data.enUS.body}}` |
| Localized entry (es-AR) | `{{response.data.esAR.body}}` |
| Non-localized entry | `{{response.data.blogPost.body}}` |
| Short text list, joined | {::nomarkdown}<code>{{response.data.recipe.ingredients | join: ', '}}</code>{:/} |
| Short text list, single item | `{{response.data.recipe.ingredients[0]}}` |
| Location field | `{{response.data.venue.address.lat}}` and `{{response.data.venue.address.lon}}` |
| Single media file | `{{response.data.blogPost.image.url}}` |
| Asset collection, single item | `{{response.data.blogPost.imagesCollection.items[0].url}}` |
| Multiple references, single item | `{{response.data.event.contactList[0].name}}` |
| Multiple references, looped | `{% for contact in response.data.event.contactList %} {{contact.name}} {% endfor %}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid tag examples" }

Media fields also expose `title`, `description`, `contentType`, `fileName`, `size`, `width`, and `height` in addition to `url`.

### Step 3: Preview and send

1. Use the Braze **Preview & Test** tab to confirm the Connected Content call resolves and the Liquid tags render the expected values.
2. Send a test message to yourself or a test user.
3. Launch the campaign or Canvas after the content renders correctly.

## Considerations

* Entries must be published. Braze retrieves content through the Content Delivery API, which only returns published entries. Draft or changed-but-unpublished entries do not render.
* Connected Content adds a request at send time. Content is fetched when each message is delivered. Follow the guidance in [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content) on caching, timeouts, and aborting messages if the request fails, and make sure your Contentful plan's API rate limits can absorb your send volume. For Contentful's rate limits, see [Contentful technical limits](https://www.contentful.com/developers/docs/platform/technical-limits/).
* Content Blocks are workspace-specific. Content Blocks synced from Contentful are created in the Braze workspace tied to the REST API key you configured. To use the same content in another workspace, configure the app for that workspace as well.
* Locales create separate outputs. Selecting multiple locales generates separate Liquid tags (Connected Content) or separate Content Blocks (syncing), one per locale.

## Troubleshooting

| Issue | Resolution |
| --- | --- |
| "A valid Contentful API key is required" during installation | Confirm the key is a Content Delivery API (CDA) key with read access, and that it belongs to the space you are installing into. |
| Liquid tags render as blank in a Braze preview | Check that the entry is published, that the field has content, and that the locale in the tag matches a locale configured on the entry. |
| Connected Content call returns an error in Braze | Verify the Space ID, environment, and access token in the generated call, and test the endpoint directly. Braze logs Connected Content errors in the message activity log. |
| Content Block does not appear in Braze | Confirm the Braze REST API key has the required Content Block permissions and that the REST endpoint matches your Braze instance. |
| Fields in a reference list return empty values | Check whether the list contains multiple content types; loop over the list rather than accessing by index. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

## Additional resources

- [Braze app guide in the Contentful Help Center](https://www.contentful.com/help/apps/braze-app/)
- [Braze app listing on the Contentful Marketplace](https://www.contentful.com/marketplace/braze/)
- [Contentful Content Delivery API documentation](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Braze Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Braze Content Blocks](https://www.braze.com/docs/user_guide/messaging/design_and_edit/content_blocks)
