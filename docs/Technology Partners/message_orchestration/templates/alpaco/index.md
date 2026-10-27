# Alpaco

> [Alpaco](https://alpaco.email/) is an online creative management tool that offers a drag-and-drop editor for building reusable, brand-safe content for Braze. The Alpaco and Braze integration allows you to export Email Templates (including AMP) and Content Blocks, schedule sends and A/B split tests to your Braze segments, and follow the results of your Braze campaigns and Canvases directly in Alpaco.

_This integration is maintained by Alpaco._

**Note:**


Alpaco supports [full Liquid](https://shopify.github.io/liquid/) variables, and as such also fully supports any Liquid variables used in your Braze configurations. Segments and content variants built in Alpaco are exported as native Braze Liquid conditions.



## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Alpaco account | An Alpaco account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions, plus the permissions for any other features you want to use (listed in the API key permissions table). <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance](https://www.braze.com/docs/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint. <br><br> For example, if your dashboard URL is `https://dashboard-03.braze.com`, your endpoint will be `dashboard-03`. |
| App identifier (optional) | Required for scheduled sends and A/B split tests. This can be found in the Braze dashboard from **Settings** > **APIs and Identifiers** > **App Identifiers**. |
| Reporting campaign (optional) | An empty API campaign in Braze, set up once. Scheduled sends and A/B split tests are sent under this campaign, so Braze reports each variant separately. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

The API key needs the following permissions, depending on the features you use. If a permission is missing, Alpaco tells you which one to add.

| Feature | Permissions |
| ------- | ----------- |
| Export email templates | `templates.email.create`, `templates.email.update` |
| Export Content Blocks | `content_blocks.create`, `content_blocks.update` |
| Scheduled sends and A/B split tests | `segments.list`, `messages.schedule.create`, `messages.schedule.delete` |
| Results of scheduled sends and A/B split tests | `campaigns.details`, `sends.id.create`, `sends.data_series` |
| Results of campaigns | `campaigns.list`, `campaigns.details`, `campaigns.data_series` |
| Results of Canvases | `canvas.list`, `canvas.details`, `canvas.data_series` |
| Custom attributes for segments and merge tags | `custom_attributes.get` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API key permissions" }

## Use cases

- Maintain **brand consistency** by centralizing creative design in Alpaco and pushing updates to Braze with a single export.
- Export fully designed **email templates**, including their **AMP for Email** version, for use in Braze campaigns, Canvases, and transactional messaging.
- Create and manage **modular content blocks** (such as headers, footers, and promotions) that can be reused across multiple channels, including **in-app messages**.
- Enable **personalization** by including Braze-supported Liquid tags, and build **segments** on your Braze custom attributes, which Alpaco syncs daily or on demand.
- **Schedule sends** to your Braze segments directly from Alpaco, optionally in each recipient's local time.
- Run **A/B split tests** with two or more email variants, each with its own subject line, preheader, and content, without any per-test setup in Braze.
- Follow **results** in Alpaco, such as opens, clicks, click-to-open rate, unsubscribes, bounces, spam reports, conversions, and revenue per variant. This covers scheduled sends and every Braze campaign and Canvas that uses an Alpaco template or Content Block.

## Integration

Add your Braze REST API key and cluster instance as a Braze connection in Alpaco under **ESP Connections**, or provide them to the Alpaco customer success team, who will set up the initial integration for you. For scheduled sends and reporting, also add a from address, your app identifier, and your reporting campaign ID.

**Note:**


This is a one-time setup, and all future exports, scheduled sends, and results will automatically use this API key.



## Exporting Alpaco messages to Braze

### Step 1: Create a template in Alpaco

In Alpaco, create a template that expresses your brand identity. When you're ready, select **Save**.

![Alpaco Create template](https://www.braze.com/docs/assets/img/alpaco/alpaco_1.png?40800d78d576cba214b172eaaef8354b)

### Step 2: Draft a message using the template

Next, go to the Alpaco lobby and use your template to create an email, in-app message, or content block. To double-check your message before exporting, select **Review**.

![Alpaco Create email](https://www.braze.com/docs/assets/img/alpaco/alpaco_2.png?01530eb7f429ca0d244b968aeda6aaaf)

### Step 3: Export your message to Braze

Select **Export**, then choose the Braze integration and specify whether you're exporting an email template or a content block. If your email has an AMP version, it's exported together with the HTML.

If you make changes after export, you can re-export the content from Alpaco to update it in Braze.

To send directly from Alpaco, select **Scheduled**, then pick a Braze segment and a send time. If your email has A/B variants, choose how the segment is split between them. Each recipient gets exactly one variant: Alpaco schedules one message per variant and uses Braze's random bucket number with `abort_message` to keep recipients in their share. You can cancel scheduled sends from Alpaco until they go out.

![Alpaco Export email](https://www.braze.com/docs/assets/img/alpaco/alpaco_3.png?20386acb2bc8a9fc25ab5c78703d04e4)

## Using Alpaco templates and blocks in Braze

Depending on the type of content you export, your template will appear in one of the following sections:

- **Templates & Media > Email Templates**
- **Templates & Media > Content Blocks**

Alpaco templates are ideal for organizations looking to centrally manage brand consistency. They also support Braze's built-in tags for easy categorization and content management.
