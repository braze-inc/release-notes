

**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





## How our translation endpoints work

Our translation endpoints work with [multi-language composition](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/multi_language_settings/), where a message can have different versions that can be rendered depending on the user receiving the message.

### Prerequisites

Before using these endpoints, you must [add your locales](https://www.braze.com/docs/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).

### How to test your translations

There are two ways you can validate translation support using the API and the Braze dashboard across campaigns, Canvases (including individual steps), Content Blocks, and email templates:

- During composition (before launch)
- After launch (using post-launch drafts)

Before testing updating translations, you must:

1. [Add your locales](https://www.braze.com/docs/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. Create a message and use translation tags where appropriate.
3. Save the message.
4. Select the locales to be included.
