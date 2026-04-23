# November 12, 2024 release
 
## Data flexibility
 
### Speed limit for `/users/track`

The speed limit for the [`/users/track` endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) has been updated to 3,000 per 3 seconds.
 
## Unlocking creativity

### Canvas Use Cases

We've put together some use cases showcasing the different ways you can leverage a Braze Canvas. If you're looking for inspiration, choose a use case below to get started.

- [Abandoned Cart](https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/abandoned_cart/)
- [Back In Stock](https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/back_in_stock/)
- [Feature Adoption](https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/feature_adoption/)
- [Lapsed User](https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/lapsed_user/)
- [Onboarding](https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/onboarding/)
- [Post-Purchase Feedback](https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/post_purchase_feedback/)

## Robust channels

### LINE



Braze's LINE integration is now generally available! LINE  is the most popular messaging app in Japan, with over 95 million monthly active users. In addition to messaging, LINE offers its users an “all-in-one” platform for social media, gaming, shopping, and payments.

To get started, see our [LINE documentation](https://www.braze.com/docs/user_guide/channels/line/).
 
### LinkedIn Audience Sync



You can now use LinkedIn with [Braze Audience Sync](https://www.braze.com/docs/partners/canvas_audience_sync/), a tool that helps you extend the reach of your campaigns to many of the top social and advertising technologies. To join the beta, contact your Braze Success Manager.
 
## Improving the developer guide
 
We're in the process of making major improvements to the [Braze Developer Guide](https://www.braze.com/docs/developer_guide/home/). As a first step, we simplified the navigation and reduced the number of nested sections.

|Before|After|
|------|-----|
|!["The old navigation for the Braze Developer Guide."](https://www.braze.com/docs/assets/img/release_notes/developer_guide_improvements/old_navigation.png?f5b618cf308132401f7d8ba69c96b055)|!["The new navigation for the Braze Developer Guide."](https://www.braze.com/docs/assets/img/release_notes/developer_guide_improvements/new_navigation.png?814af51ddb6336e5c479f6b5f7f25dba)|

## New Braze partnerships
 
### MyPostcard

[MyPostcard](https://www.mypostcard.com/), a leading global postcard app, empowers you to execute direct mail campaigns with ease, providing a seamless and profitable way to connect with your customers. To get started, see [Integrating MyPostcard with Braze](https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/direct_mail/mypostcard/).
 
## SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Expo Plugin 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - This version requires 13.1.0 of the Braze React Native SDK.
    - Replaces the iOS BrazeAppDelegate method call of BrazeReactUtils.populateInitialUrl with BrazeReactUtils.populateInitialPayload.
        - This update resolves an issue where push opened events would not be triggered when clicking on a notification while the application is in a terminated state.
        - To fully leverage this update, replace all calls of Braze.getInitialURL with Braze.getInitialPushPayload in your JavaScript code. The initial URL can now be accessed via the url property of the initial push payload.
- [Braze Segment Swift Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Updates the Braze Swift SDK bindings to require releases from the 11.1.1+ SemVer denomination.
    - This allows compatibility with any version of the Braze SDK from 11.1.1 up to, but not including, 12.0.0.
    - Refer to the changelog entry for 11.1.1 for more information on potential breaking changes.
