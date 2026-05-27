# September 16, 2025 release

## Data flexibility

### Braze Data Platform

Braze Data Platform is a set of comprehensive, composable set of data capabilities and partner integrations that empowers you to create personalized, impactful experiences across the customer lifecycle. Learn more about the three data related jobs to be done: 

- [Data unification](https://www.braze.com/docs/user_guide/data/unification)
- [Data activation](https://www.braze.com/docs/user_guide/data/activation)
- [Data distribution](https://www.braze.com/docs/user_guide/data/distribution)

### Custom Banner properties



You can use custom properties from your Banner campaign to retrieve key–value data through the SDK and modify your app’s behavior or appearance. To learn more, see [Custom Banner properties](https://www.braze.com/docs/developer_guide/banners/placements/#custom-properties).

### Token authentication



When using Braze Connected Content, you may find that certain APIs require a token instead of a username and password. Braze can store credentials that hold [token authentication header values](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication).

### Promotion codes

You can save promotion codes to a user’s profile through a User Update step. For more information, refer to [Saving promotion codes to user profiles](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes#save-to-profile).

## Unlocking creativity

### Braze Pilot

[Braze Pilot](https://www.braze.com/docs/user_guide/get_started/braze_pilot/) is a publicly available app for Android and iOS that allows you to launch messages from your Braze dashboard to your phone. Check out [Getting started with Braze Pilot](https://www.braze.com/docs/user_guide/get_started/braze_pilot/getting_started/) for a walkthrough of downloading the app, initializing the connection to your Braze dashboard, and completing the setup.

## New Braze partnerships

### Blings - Visual and interactive content

[Blings](https://www.braze.com/docs/partners/blings/) is a next-generation personalized video platform that enables you to deliver real-time, interactive, and data-driven video experiences across channels at scale.

### Shopify standard integration with third-party tool

For Shopify online stores, we recommend using Braze’s standard integration method to support the Braze SDKs on your site.

However, we understand that you may prefer using a third-party tool, like Google Tag Manager, so we put together a guide on how you can. To get started, see [Shopify: Third-party tagging](https://www.braze.com/docs/shopify_standard_integration_third_party_tagging/).

## SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Updates the native Android bridge from Braze Android SDK `36.0.0` to `39.0.0`.
    - Updates the native iOS bridge from Braze Swift SDK `12.0.0` to `13.2.0`. This includes Xcode 26 support.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Updates the Braze Swift SDK bindings to require releases from the `13.0.0+` SemVer denomination. This allows compatibility with any version of the Braze SDK from `13.0.0` up to, but not including, `14.0.0`.
