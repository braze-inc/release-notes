# Stripo

> [Stripo](https://stripo.email/) is a drag-and-drop email template builder for designing responsive emails with interactive elements. Stripo users can also edit in HTML and decide which elements to display or hide on various devices through the Stripo editor.

_This integration is maintained by Stripo._

## About the integration

The Braze and Stripo integration allows you to export your customized Stripo emails and upload them as templates within Braze.

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Stripo account | A Stripo account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance](https://www.braze.com/docs/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

## Integration

### Step 1: Create Stripo email

Create a Stripo email in the Stripo platform and click **Export**. 

![Stripo Export](https://www.braze.com/docs/assets/img_archive/stripo_export.png?43a34126e448e95f9e77f94d2d99ebaf)

### Step 2: Export template to Braze

In the dialogue that appears, select **Braze** as your method of export 

Next, enter your **account name** (such as workspace name), **API key**, and your **cluster instance**.

![Stripo Form](https://www.braze.com/docs/assets/img_archive/stripo_form.png?88df0b4fbb604cbad7edfba03fe24a47)

**Important:**


This is a one-time setup, and any exports in the future will automatically utilize this API key.



## Usage

Find your uploaded Stripo template in your Braze account's **Templates & Media > Email Templates** section. You can now use this email template to start sending engaging email messages to your customers!


