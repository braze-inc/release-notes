# TransPerfect

> [TransPerfect](https://www.transperfect.com/) provides language and localization technology through GlobalLink. [GlobalLink Connect](https://glconnect.transperfect.com/docs/braze/26.1.0/) integrates with Braze so you can browse supported Braze content, submit it for translation in GlobalLink, and write completed translations back to Braze through the Braze Translations API.

_This integration is maintained by TransPerfect._

## About the integration

After you configure GlobalLink Connect for your Braze instance, users browse supported Braze content in GlobalLink Connect and submit it for translation through the GlobalLink platform. The connector:

1. Requests translatable content from Braze through the Translations API
2. Extracts content enclosed in Braze translation tags
3. Submits a translation request to GlobalLink TMS
4. Updates Braze with translated content after the GlobalLink workflow completes

Only content exposed through the Braze Translations API is available for translation.

## Supported content

In the current release, GlobalLink Connect supports translation of:

- Email templates
- Content Blocks
- Campaigns (email channel only)

The connector does not extract content from push, in-app messages, or SMS.

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A TransPerfect GlobalLink account | A GlobalLink Connect account is required to use this integration. Contact [TransPerfect](https://www.transperfect.com/) to get started. |
| A Braze REST API key | A Braze REST API key with the following permissions:<br>- `campaigns.list`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `content_blocks.info`<br>- `content_blocks.list`<br>- `content_blocks.translations.get`<br>- `content_blocks.translations.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.get`<br>- `templates.translations.update`<br><br>Create this key in the Braze dashboard from **Settings** > **APIs and Identifiers** > **API Keys**. For more information, see [Creating REST API keys](https://www.braze.com/docs/api/basics#creating-rest-api-keys). |
| A Braze REST endpoint | [Your REST endpoint URL](https://www.braze.com/docs/api/basics#endpoints). Your endpoint depends on the Braze URL for your instance. |
| Braze multi-language settings | Source and target locales must be configured in Braze under **Settings** > **Localization Settings**. For more information, see [Multi-language settings](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/multi_language_settings/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Create a Braze REST API key

1. In Braze, go to **Settings** > **APIs and Identifiers** > **API Keys**.
2. Select **Create API Key**.
3. Enter a name for the key (for example, `GlobalLink`).
4. Select the permissions listed in [Prerequisites](#prerequisites).
5. Create the key, then copy the API key identifier and your instance REST endpoint URL (for example, `https://rest.iad-03.braze.com`).

GlobalLink Connect uses the REST endpoint for the `rest-api-url` field and the API key for the `braze-api-key` field.

### Step 2: Configure localization settings in Braze

1. In Braze, go to **Settings** > **Localization Settings**.
2. Select **Add locale** and add each source and target language you want to support. For more information, see [Multi-language settings](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/multi_language_settings/).
3. Note the language name and locale identifier for each locale. You provide these values to TransPerfect so GlobalLink Connect can map source and target locales.

### Step 3: Configure the GlobalLink Connect connector

Provide the following values to your TransPerfect or GlobalLink team so they can complete the Braze connector configuration:

| Configuration field | Description |
| --- | --- |
| `rest-api-url` | REST API endpoint of your Braze instance. |
| `braze-api-key` | REST API key created in [Step 1](#step-1-create-a-braze-rest-api-key). |
| `source-locale` | Source locale name, code, and identifier from Braze localization settings. |
| `target-locale` | Target locale names, codes, and identifiers from Braze localization settings. |
| `filename-configuration` | How GlobalLink names files sent for translation: `name_id` (name and ID), `name` (name only), or `ID` (ID only). |
| `preview-enabled` | `true` or `false` to enable or disable preview. |
| `include-archived-campaigns` | `true` or `false` to include or exclude archived campaigns. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Connector configuration fields" }

For full connector configuration details, see the [GlobalLink Connect Braze documentation](https://glconnect.transperfect.com/docs/braze/26.1.0/).

### Step 4: Mark content for translation in Braze

Enclose the content you want to translate in Braze translation tags so the Translations API can expose it to GlobalLink Connect. For more information, see [Multi-language messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/).

Enable the matching locales on the email template, Content Block, or campaign message before you submit content for translation.

### Step 5: Submit content and return translations

1. In GlobalLink Connect, browse supported Braze content (email templates, Content Blocks, and campaign email messages).
2. Submit the content for translation through the GlobalLink platform.
3. After GlobalLink TMS completes translation and review, GlobalLink Connect updates Braze through the Translations API.
4. In Braze, open the message, go to **Preview and Test**, and select **Multi-language user** to confirm the translations. For more information, see [Preview personalization](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/preview_personalization/).

## Considerations

- The connector supports the email channel only. Push, in-app messages, and SMS are not available for extraction in the current release.
- Only content wrapped in translation tags and exposed through the Braze Translations API appears in GlobalLink Connect.

## Additional resources

- [GlobalLink Connect Braze documentation](https://glconnect.transperfect.com/docs/braze/26.1.0/)
- [TransPerfect](https://www.transperfect.com/)
