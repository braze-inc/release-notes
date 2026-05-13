# Push stories

> Learn how to set up push stories for the Braze SDK.



## Prerequisites

Before you can use this feature, you'll need to [integrate the Swift Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=swift), which includes implementing the `UNNotification` framework.

The following minimum SDK version is required to receive Push Stories:

<div id='sdk-versions'><a href='/docs/developer_guide/platforms/swift/changelog/#500' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 5.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## Setting up Push Stories

### Step 1: Adding the Notification Content Extension target {#notification-content-extension}

In your app project, go to menu **File > New > Target** and add a new `Notification Content Extension` target and activate it.

![](https://www.braze.com/docs/assets/img/swift/push_story/add_content_extension.png?ad9e5d8cc83d88d9e26dbd2c4c8dba67)

Xcode should generate a new target for you and create files automatically for you including:

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### Step 2: Enable capabilities {#enable-capabilities}

In Xcode, add the Background Modes capability using the **Signing & Capabilities** pane to the main app target. Select both the **Background fetch** and **Remote notifications** checkboxes.

![](https://www.braze.com/docs/assets/img/swift/push_story/enable_background_mode.png?37d0c9c4c59fb04aa930729a5539ed59)

#### Adding an App Group

Additionally, from the **Signing & Capabilities** pane in Xcode, add the App Groups capability to your main app target as well as the Notification Content Extension targets. Then, click the **+** button. Use your app's bundle ID to create the app group. For example, if your app's bundle ID is `com.company.appname`, you can name your app group `group.com.company.appname.xyz`.

**Important:**


App Groups in this context refer to Apple's [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) and not your Braze workspace (previously app group) ID.



If you do not add your app to an App Group, your app may fail to populate certain fields from the push payload and will not work fully as expected.

### Step 3: Adding the Push Story framework to your app {#enable-capabilities}




After following the [Swift Package Manager integration guide](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), add `BrazePushStory` to your `Notification Content Extension`:

![In Xcode, under frameworks and libraries, select the "+" icon to add a framework.](https://www.braze.com/docs/assets/img/swift/push_story/spm1.png?00b81a1ac272e7247a67cd7c176a79f8)

![](https://www.braze.com/docs/assets/img/swift/push_story/spm2.png?9df11322d50bd385f7151ba062c0319c)




Add the following line to your Podfile:

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```

**Note:**


For instructions to implement Rich Push, see [Rich notifications](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager).



After updating the Podfile, navigate to the directory of your Xcode app project within your terminal and run `pod install`.




Download the latest `BrazePushStory.zip` from the [GitHub release page](https://github.com/braze-inc/braze-swift-sdk/releases), extract it, and add the `BrazePushStory.xcframework` to your project's `Notification Content Extension`.

![](https://www.braze.com/docs/assets/img/swift/push_story/manual1.png?cdc5b6905a824611c983facc8b541026)

**Important:**


Make sure that **Do Not Embed** is selected for **BrazePushStory.xcframework** under the **Embed** column.






### Step 4: Updating your notification view controller {#enable-capabilities}

In `NotificationViewController.swift`, add the following line to import the header files:

```swift
import BrazePushStory
```

Next, replace the default implementation by inheriting [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/):

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### Custom handling push story events

If you want to implement your own custom logic to handle push story notification events, inherit `BrazePushStory.NotificationViewController` as above and override the [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:)) methods as below.

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)
    
    // Custom handling logic
  }
  
  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)
    
    // Custom handling logic
  }
}
```

### Step 5: Setting the Notification Content Extension plist {#notification-content-extension}

Open the `Info.plist` file of the `Notification Content Extension`, then add and change the following keys under `NSExtension \ NSExtensionAttributes`:

| Key                                              | Type    | Value                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | String  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Boolean | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Number  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Boolean | `YES`                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 5: Setting the Notification Content Extension plist #notification-content-extension" }

Additionally, add the following top-level `Braze` dictionary to the same `Info.plist` file, replacing `REPLACE_WITH_APPGROUP` with the App Group you created in [Step 2](#enable-capabilities):

| Key              | Type   | Value                    |
|------------------|--------|--------------------------|
| `Braze.AppGroup` | String | `REPLACE_WITH_APPGROUP`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 5: Setting the Notification Content Extension plist #notification-content-extension" }

Your `Info.plist` file should match the following image:

![](https://www.braze.com/docs/assets/img/swift/push_story/notificationcontentextension_plist.png?781099250e344b0bfbf448d47af7a25c)

### Step 6: Updating the Braze integration in your main app {#update-braze}

Before initializing Braze, assign the name of your app group to your Braze configuration's [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) property.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```




## Prerequisites

Before you can use this feature, you'll need to [integrate the Cordova Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=cordova).

## Setting up push stories

### Step 1: Create a notification content extension

In your Xcode project, create a notification content extension. For a full walkthrough, see [iOS Push Stories Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

### Step 2: Configure your push app group

In your project's `config.xml` file, configure the push app group [you just created](#cordova_step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Replace `PUSH_APP_GROUP` with the name of your push app group. Your `config.xml` should be similar to the following:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### Step 3: Add a new target

Open your Podfile and add `BrazePushStory` to the notification content extension target [you created previously](#cordova_step-1-create-a-notification-content-extension). To avoid duplicate symbol errors, use static linking.

```ruby
target 'NOTIFICATION_CONTENT_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

Replace `NOTIFICATION_CONTENT_EXTENSION` with the name of your notification content extension. Your Podfile should be similar to the following:

```ruby
target 'MyAppNotificationContentExtension' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

### Step 4: Reinstall your CocoaPods dependencies

In the terminal, go to your iOS directory and reinstall your CocoaPod dependencies.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```




## Prerequisites

Before you can use this feature, you'll need to [integrate the React Native Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=react%20native).

## Enabling push stories

For the React Native SDK, **push stories are available for Android by default**.

To enable Push Stories on iOS using Expo, ensure you have an app group defined for your application. For more information, see [Adding an App Group](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Next, configure the `enableBrazeIosPushStories` property to `true` and assign your app group ID to `iosPushStoryAppGroup` in your `expo.plugins` object in `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Lastly, add the bundle identifier for this app extension to your project's credentials configuration: `<your-app-bundle-id>.BrazeExpoPushStories`. For further details on this process, refer to [Using app extensions with Expo Application Services](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).

**Warning:**


If you are using Push Stories with Expo Application Services, be sure to use the `EXPO_NO_CAPABILITY_SYNC=1` flag when running `eas build`. There is a known issue in the command line which removes the App Groups capability from your extension's provisioning profile.





