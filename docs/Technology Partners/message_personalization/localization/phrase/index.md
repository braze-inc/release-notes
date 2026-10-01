# Phrase

> [Phrase](https://phrase.com/) is a localization platform. It translates content, automates translation workflows, and reports on that content so you can reach people across languages and cultures.

_This integration is maintained by Phrase._

## About the integration

Translate campaign and Canvas content from Braze, then return completed translations to the same message. Phrase reports that sending email for translation from Braze can [reduce preparation work by up to 98%](https://phrase.com/integrations/braze/) compared with other integrations.

In Phrase, automated workflows, AI translations that follow your brand, and collaboration with translation providers bring content back to Braze. For HTML email, translators see a visual preview so the translation matches the layout.

The integration helps you:

- Skip manual imports, exports, and project setup
- Shorten the time from draft to launch
- Keep translations aligned with your brand voice
- Check that translations fit the message layout

## Supported channels

The integration translates the following content in campaigns and Canvases, in the drag-and-drop editor or the traditional HTML editor:

- Email
- Push
- In-app messages
- Banners

## Demo

For a walkthrough, watch the [Phrase and Braze integration demo](https://youtu.be/VN8SCD1Dgwg).

## Prerequisites

| Requirement | Description |
| --- | --- |
| Phrase account | A Phrase account with the Braze integration add-on. |
| Braze REST API key | A Braze REST API key with the following permissions:<br>- `templates.translations.get`<br>- `templates.translations.update`<br>- `templates.email.list`<br>- `campaigns.list`<br>- `campaigns.details`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `canvas.list`<br>- `canvas.details`<br>- `canvas.translations.get`<br>- `canvas.translations.update`<br><br>Create this key in the Braze dashboard from **Settings** > **APIs and Identifiers** > **API Keys**. For more information, see [Creating REST API keys](https://www.braze.com/docs/api/basics#creating-rest-api-keys). |
| Braze REST endpoint | [Your REST endpoint URL](https://www.braze.com/docs/api/basics#endpoints). Your endpoint depends on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Add locales in Braze

Before you connect Phrase, add the locales you want to translate.

1. In Braze, go to **Settings** > **Localization Settings**.
2. Select **Add locale** and add each language you want to support. For more information, see [Localization Settings](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/multi_language_settings/).
3. Name each locale with the same code you use in Phrase, and use underscores (for example, `en_US`, `de_DE`, or `fr_FR`).

**Important:**


Braze stores the locale key as the lowercase locale name. A locale named `en_US` is stored as `en_us`. Use that locale key in Phrase.



### Step 2: Create a Braze REST API key

Phrase uses a REST API key to read your messages and write translations back.

1. In Braze, go to **Settings** > **APIs and Identifiers** > **API Keys**.
2. Select **Create API Key**.
3. Enter a name for the key (for example, `Phrase integration`).
4. Select the permissions listed in [Prerequisites](#prerequisites).
5. Copy the API key and your REST endpoint URL (for example, `https://rest.iad-03.braze.com`).

### Step 3: Configure the connector in Phrase TMS

1. In Phrase, go to **Phrase TMS** > **Settings** > **Connectors** and select **New**.
2. Select **Braze** as the connector type.
3. Enter a name for the connector.
4. Paste the REST endpoint URL and REST API key from [Step 2](#step-2-create-a-braze-rest-api-key).
5. Select **Test connection**. A check mark appears when the connection succeeds.
6. (Optional) Under **Show optional settings**, enter translation tag IDs if you want to import only Braze content that uses those IDs.
7. Select **Save**.

### Step 4: Mark content for translation

Phrase identifies translatable content with Liquid translation tags. Each tag ID must be unique in the message. For more information, see [Multi-language messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/).

#### HTML editor

Wrap the content you want to translate. This applies to email, push, and in-app messages composed in the HTML editor.

For body content:


```liquid
{% translation body %}
Your email content here...
{% endtranslation %}
```


For the subject and preheader:


```liquid
{% translation subject %}Your subject{% endtranslation %}
{% translation preheader %}Your preheader{% endtranslation %}
```


#### Drag-and-drop editor

Add the drag-and-drop message to a campaign or Canvas before you import it. Phrase imports drag-and-drop messages from campaigns and Canvases.

1. Open the campaign or Canvas message.
2. Add a **Paragraph** block at the top of the message that contains `{% translation body %}`.
3. Add a **Paragraph** block at the bottom of the message that contains `{% endtranslation %}`.

#### Choose locales on the message

1. Save the message.
2. Open the message again. Select **Manage languages** (**Languages** in the drag-and-drop editor) and add the locales that match your Phrase project.

### Step 5: Import content and export translations

#### Import

In Phrase TMS, go to **Jobs** > **New** > **Import from online repository**. Select your Braze connector, then select the templates, campaigns, or Canvases to translate. Use this import to test the connection. After you validate it, you can import content with [Automated Project Creation](https://support.phrase.com/hc/en-us/articles/5709647363356).

#### Translate

For a test, translate in the Phrase computer-assisted translation (CAT) editor. For HTML email, use **Live Preview**. You can add AI translation, quality scoring, and a human review step to the workflow.

#### Export

To send translations back to Braze, select **Export to online repository**, or configure automation to deliver translations when they are ready.

#### Preview in Braze

Open the message, go to **Preview and Test**, and select **Multi-language user**. Switch locales to check the translations. For more information, see [Preview personalization](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/preview_personalization/).

## Troubleshooting

### Why isn't my template listed in Phrase TMS?

- Add at least one pair of translation tags. Phrase lists messages that include those tags.
- Use a different translation ID for each tag pair in the message. If the same ID appears twice (for example, in the subject and the body), Braze returns an error and Phrase omits the message.
- If you entered a translation tag ID in the connector settings, Phrase imports content that uses that ID.
