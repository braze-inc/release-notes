# Set up user language and locale

> Decide which signal determines the language a consumer receives, then set that value on the user profile so localized campaigns and Canvases target the right audience.

## About this example

UponVoyage, a fictional travel brand, personalizes messages for consumers across twelve markets. Marketing derives language from a `market` custom attribute set to the country a consumer books outbound travel from. That attribute maps to a region rather than a language, so consumers who book from a multilingual country—or from a country outside their own—can receive the wrong language.

This example compares three signals for a consumer's language and shows how to set each one on the profile:

- **SDK-collected language:** The `language` [standard attribute](https://www.braze.com/docs/user_guide/data/activation/attributes/standard_attributes), captured from the device or browser locale
- **Explicit language preference:** A value the consumer chooses in your app or on your site, set through the SDK or REST API
- **Market or region custom attribute:** A business attribute such as `market`, used when your content varies by region rather than by language

`language` and `country` are separate standard attributes in Braze. When regional variants matter (for example, European Spanish compared to Latin American Spanish), target both attributes rather than storing a combined locale string.

This example shows how to choose a language signal and set it on the profile. For storing and sending translated copy, see [Compare translation approaches](https://www.braze.com/docs/user_guide/example_library/localization/compare_translation_approaches).

## Considerations

- Country comes from IP geolocation first. Braze identifies `country` by IP address geolocation. If geolocation isn't available, Braze identifies `country` by the device locale. Don't treat `country` as a device-reported value. For more information, see [SDK data collection](https://www.braze.com/docs/user_guide/data/unification/user_data/sdk_data_collection#minimum-integration).
- Language collection is optional and can be turned off. `language` is optional data collected by default, so a minimum integration or a device property allowlist can exclude it. Confirm your integration still collects it before you rely on it. For more information, see [Storage](https://www.braze.com/docs/developer_guide/storage#device-properties).
- Most recent device locale may be absent. Not every consumer has a value, so plan a fallback language for messages that use it.
- Setting a value explicitly stops automatic collection. After you set `language` or `country` through the SDK, REST API, or CSV import, Braze stops automatically updating that field for that consumer. Plan for how a consumer changes their preference later.
- Explicit values consume data points. SDK and API attribute updates log data points, while automatic collection doesn't. For more information, see [Data points](https://www.braze.com/docs/user_guide/data/infrastructure/data_points).
- `language` must be an ISO 639-1 code. Use two-letter codes such as `en` or `nl`. For the supported set, see [Language codes](https://www.braze.com/docs/user_guide/data/unification/user_data/language_codes). `country` uses ISO 3166-1 alpha-2 codes such as `GB` or `BE`.
- Changing your language model affects existing assets. When you move from a custom attribute to standard attributes, audit the campaigns, Canvases, segments, and Liquid that reference the old attribute before you retire it.

## Setup

### Step 1: Choose the signal that determines language

| Signal | Use it when | Tradeoff |
| --- | --- | --- |
| SDK-collected `language` | You want coverage for every consumer with an SDK session and no engineering work beyond the existing integration | Reflects the device setting, which may differ from the language a consumer wants marketing in |
| Explicit language preference | Consumers can choose a language in your app, on your site, or in an account settings page | Requires an interface for the choice and a call to Braze when it changes |
| Market or region custom attribute | Content, pricing, or legal copy varies by market rather than by language | A `market` attribute maps to a language only when each market has one language |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Choose the signal that determines language" }

Where you can collect an explicit preference, use it as your primary signal and fall back to SDK-collected `language`. A `market` attribute is a poor substitute to infer language in multilingual countries such as Belgium, Canada, and Switzerland.

### Step 2: Confirm what your integration already collects

1. Go to **Audience** > **User Search**, open a consumer profile, and check the **Language** and **Country** fields.
2. If **Language** is empty across profiles, confirm your SDK integration doesn't exclude it from device property collection.
3. Note whether **Most Recent Device Locale** is populated. Use it for diagnostics, and don't target on it without a fallback.

### Step 3: Set an explicit language preference

Use this step only when you chose an explicit language preference in Step 1. For SDK-collected `language`, confirm collection in Step 2 and skip to targeting. For a `market` or region custom attribute, set that attribute through the SDK or REST API, then continue with Steps 4 through 6 as needed.

When a consumer chooses a language, send that choice to Braze so it takes precedence over automatic collection.

Set the value through the SDK when the choice happens in your app or on your site. For method names on each platform, see [Setting user attributes](https://www.braze.com/docs/developer_guide/analytics/setting_user_attributes).

For preferences stored in your own systems, send the standard attributes through the [`/users/track` endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track):

```json
{
  "attributes": [
    {
      "external_id": "{YOUR_EXTERNAL_ID}",
      "language": "nl",
      "country": "BE"
    }
  ]
}
```

Replace `YOUR_EXTERNAL_ID` with the identifier for the consumer whose preference changed.

### Step 4: Set country when a consumer signals a region

Set `country` explicitly when a consumer tells you their region—for example, when they browse a country-specific site or select a market at signup. Use the same `/users/track` request or SDK method as the previous step.

If you want IP-based country to keep updating, don't set `country` explicitly. Choose one source per consumer and apply it consistently.

### Step 5: Target messages on language and country

1. Build segments with the **Language** and **Country** filters rather than a combined locale attribute.
2. For messages that vary by region within a language, filter on both attributes—for example, `language` is `es` and `country` is `ES`.
3. To send one message that renders per locale, [add locales](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/multi_language_settings) using the default language and country attributes, then see [Multi-language messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).
4. If you keep a `market` attribute for regional content, [add a locale based on custom attributes](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/multi_language_settings#add-a-locale) instead of mapping that attribute to a language.

### Step 6: Migrate away from a market-based language model

1. Search your workspace for campaigns, Canvases, segments, and Content Blocks that reference the `market` attribute.
2. Backfill `language` for existing profiles through [CSV import](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users/csv_import) or the API where you already know a consumer's preference.
3. Update assets to filter on **Language**, keeping the `market` attribute only where content varies by region.
4. Confirm each locale renders as expected with **Preview message as user** before you retire the old attribute.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/data/activation/attributes/standard_attributes"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Standard attributes</span></span></div></a></li><li><a href="/docs/user_guide/data/unification/user_data/sdk_data_collection"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">SDK data collection</span></span></div></a></li><li><a href="/docs/user_guide/data/unification/user_data/language_codes"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Language codes</span></span></div></a></li><li><a href="/docs/developer_guide/analytics/setting_user_attributes"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Setting user attributes</span></span></div></a></li><li><a href="/docs/api/objects_filters/user_attributes_object"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">User attributes object</span></span></div></a></li><li><a href="/docs/user_guide/administer/global/workspace_settings/multi_language_settings"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Localization settings</span></span></div></a></li><li><a href="/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Multi-language messages</span></span></div></a></li><li><a href="/docs/user_guide/example_library/localization/compare_translation_approaches"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Compare translation approaches</span></span></div></a></li></ul>
