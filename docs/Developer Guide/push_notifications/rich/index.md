# Rich push notifications

> Learn how to set up rich push notifications for the Braze SDK.



## Prerequisites

Before you can use this feature, you'll need to [integrate the Swift Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=swift).

## Setting up rich push notifications

### Step 1: Creating a service extension

To create a [notification service extension](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), navigate to **File > New > Target** in Xcode and select **Notification Service Extension**.

![](https://www.braze.com/docs/assets/img_archive/ios10_se_at.png?ad077697c9a4c7c7bc3ca07a6405c05d){: style="max-width:90%"}

Ensure that **Embed In Application** is set to embed the extension in your application.

### Step 2: Setting up the notification service extension

A notification service extension is its own binary that is bundled with your app. It must be set up in the [Apple Developer Portal](https://developer.apple.com) with its own app ID and provisioning profile.

The notification service extension's bundle ID must be distinct from your main app target's bundle ID. For example, if your app's bundle ID is `com.company.appname`, you can use `com.company.appname.AppNameServiceExtension` for your service extension.

### Step 3: Adding an App Group

In Xcode, add the App Groups capability from the **Signing & Capabilities** pane to your main app target as well as the Notification Service Extension target. Then, click the **+** button. Use your app's bundle ID to create the app group. For example, if your app's bundle ID is `com.company.appname`, you can name your app group `group.com.company.appname.xyz`.

**Important:**


App Groups in this context refer to Apple's [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) and not your Braze workspace (previously app group) ID.



You need a shared App Group so your main app and the Notification Service Extension can access shared data. If you do not add your app to an app group, your app may fail to populate certain fields from the push payload and will not work fully as expected.

### Step 4: Integrating rich push notifications

For a step-by-step guide on integrating rich push notifications with `BrazeNotificationService`, refer to our [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

To see a sample, refer to the usage in [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) of our Examples app.

#### Adding the rich push framework to your app




After following the [Swift Package Manager integration guide](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), add `BrazeNotificationService` to your `Notification Service Extension` by doing the following:

1. In Xcode, under frameworks and libraries, select the <i class="fas fa-plus"></i> add icon to add a framework. <br><br>![The plus icon is located under frameworks and libraries in Xcode.](https://www.braze.com/docs/assets/img_archive/rich_notification.png?aacc2bc0878ec1e3bf74e346f2cd7132)<br><br>

2. Select the "BrazeNotificationService" framework. <br><br>![The "BrazeNotificationService framework can be selected in the modal that opens.](https://www.braze.com/docs/assets/img_archive/rich_notification2.png?13b077cd5a0a9723eff10fc48a6bc70c)




Add the following to your Podfile:

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

**Note:**


For instructions to implement Push Stories, see the [documentation](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).



After updating the Podfile, navigate to the directory of your Xcode app project within your terminal and run `pod install`.





To add `BrazeNotificationService.xcframework` to your `Notification Service Extension`, see [Manual integration](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![](https://www.braze.com/docs/assets/img/swift/rich_push/manual1.png?43f3a21a35ff7bd8ba2e787947a860b3)




#### Using your own UNNotificationServiceExtension

If you need to use your own UNNotificationServiceExtension, you can instead call [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) in your `didReceive` method.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### Step 5: Configuring the App Group in Braze

Before initializing Braze, assign the name of your app group to your Braze configuration's [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) property.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### Step 6: Creating a rich notification in your dashboard

Your marketing team can also create rich notifications from the dashboard. Create a push notification through the push composer and attach an image or GIF, or provide a URL that hosts an image, GIF, or video. Note that assets are downloaded on the receipt of push notifications, so you should plan for large, synchronous spikes in requests if you are hosting your content.




## Prerequisites

Before you can use this feature, you'll need to [integrate the Cordova Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=cordova).

## Setting up rich push notifications

### Step 1: Create a notification service extension

In your Xcode project, create a notification service extension. For a full walkthrough, see [iOS Rich Push Notifications Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

### Step 2: Add a new target

Open your Podfile and add `BrazeNotificationService` to the notification service extension target [you just created](#cordova_step-1-create-a-notification-service-extension). If `BrazeNotificationService` is already added to a target, remove it before continuing. To avoid duplicate symbol errors, use static linking.

```ruby
target 'NOTIFICATION_SERVICE_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

Replace `NOTIFICATION_SERVICE_EXTENSION` with the name of your notification service extension. Your Podfile should be similar to the following:

```ruby
target 'MyAppRichNotificationService' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

### Step 3: Reinstall your CocoaPods dependencies

In the terminal, go to your project's iOS directory and reinstall your CocoaPod dependencies.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```




## Prerequisites

Before you can use this feature, you'll need to [integrate the React Native Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=react%20native).

## Using Expo to enable rich push notifications

For the React Native SDK, **rich push notifications are available for Android by default**.

To enable rich push notifications on iOS using Expo, configure the `enableBrazeIosRichPush` property to `true` in your `expo.plugins` object in `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Lastly, add the bundle identifier for this app extension to your project's credentials configuration: `<your-app-bundle-id>.BrazeExpoRichPush`. For further details on this process, refer to [Using app extensions with Expo Application Services](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).



