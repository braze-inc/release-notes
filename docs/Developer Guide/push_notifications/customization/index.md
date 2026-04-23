# Customize push notifications

> Learn how to customize push notifications for the Braze SDK.



## Prerequisites

Before you can use this feature, you'll need to [integrate the Android Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=android).

## Using a callback for push events {#push-callback}

Braze provides a [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) callback for when push notifications are received, opened, or dismissed. It is recommended to place this callback in your `Application.onCreate()` in order to not miss any events occurring while your application is not running.

**Note:**


If previously using a Custom Broadcast Receiver for this functionality in your application, you can safely remove it in favor of this integration option.






```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```




```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```




**Tip:**


With notification action buttons, `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` intents fire when buttons with `opens app` or `deep link` actions are clicked. Deep link and extras handling remains the same. Buttons with `close` actions don't fire `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` intents and dismiss the notification automatically.



**Important:**


Create your push notification listener in `Application.onCreate` to ensure your listener is triggered after an end-user taps a notification while your app is in a terminated state.



## Customizing notification display {#customization-display}

### Step 1: Create your custom notification factory

In some scenarios, you may wish to customize push notifications in ways that would be cumbersome or unavailable server side. To give you complete control of notification display, we've added the ability to define your own [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) to create notification objects for display by Braze.

If a custom `IBrazeNotificationFactory` is set, Braze will call your factory's `createNotification()` method upon push receipt before the notification is displayed to the user. Braze will pass in a `Bundle` containing Braze push data and another `Bundle` containing custom key-value pairs sent either via the dashboard or the messaging APIs:

Braze will pass in a [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) containing data from the Braze push notification.




```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```




```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```




You can return `null` from your custom `createNotification()` method to not show the notification at all, use `BrazeNotificationFactory.getInstance().createNotification()` to obtain our default `notification` object for that data and modify it before display, or generate a completely separate `notification` object for display.

**Note:**


For documentation on Braze push data keys, refer to the [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).



### Step 2: Set your custom notification factory

To instruct Braze to use your custom notification factory, use the `setCustomBrazeNotificationFactory` method to set your [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html):





```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```




```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```




The recommended place to set your custom `IBrazeNotificationFactory` is in the `Application.onCreate()` application lifecycle method (not activity). This will allow the notification factory to be set correctly whenever your app process is active.

**Important:**


Creating your own notification from scratch is an advanced use case and should be done only with thorough testing and a deep understanding of the Braze push functionality. For example, you must make sure your notification logs push opens correctly.



To unset your custom [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) and return to default Braze handling for push, pass in `null` to our custom notification factory setter:





```java
setCustomBrazeNotificationFactory(null);
```




```kotlin
setCustomBrazeNotificationFactory(null)
```




## Rendering multicolor text

In Braze SDK version 3.1.1, HTML can be sent to a device to render multicolor text in push notifications.

![An Android push message "Multicolor Push test message" where the letters are different colors, italicized and given a background color.](https://www.braze.com/docs/assets/img/multicolor_android_push.png?5a515501661c5953a76737951378e789){: style="max-width:40%;"}

This example is rendered with the following HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Keep in mind that, Android limits which HTML elements and tags are valid in your push notifications. For example, `marquee` is not allowed.

**Important:**


Multicolor text rendering is device-specific and may not display based on Android device or version.



To render multicolor text in a push notification, you can update your `braze.xml` or `BrazeConfig`:



Add the following in your `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```



Add the following in your [`BrazeConfig`](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):




```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 



```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```





### Supported HTML tags

Currently, Google doesn't list their supported HTML tags for Android directly in their documentation&#8212;this information can only be found in their [Git repository's `Html.java` file](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java). Keep this in mind when referencing the following table, as this information was pulled from this file, and their supported HTML tags could be subject to change.

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>HTML Tag</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Basic Text Styling</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Bold text</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Italic text</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Underline text</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Strikethrough text</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Superscript text</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Subscript text</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Monospace text</td>
    </tr>
    <tr>
      <td rowspan="3">Size/Font</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Relative text size changes</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Sets foreground color</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (with inline CSS)</td>
      <td>Inline styles (e.g., color, background)</td>
    </tr>
    <tr>
      <td rowspan="4">Paragraph &amp; Block</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Block-level sections</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Line break</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Quoted block</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Unordered list with bullets</td>
    </tr>
    <tr>
      <td>Headings</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Headings (various sizes)</td>
    </tr>
    <tr>
      <td rowspan="2">Links &amp; Images</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Clickable link</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Inline image</td>
    </tr>
    <tr>
      <td>Other Inline</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Synonyms for italic or bold</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Rendering inline images

### How it works

You can showcase a larger image within your Android push notification using inline image push. With this design, users won't have to manually expand the push to enlarge the image. Unlike regular Android push notifications, inline image push images are in a 3:2 aspect ratio.

![](https://www.braze.com/docs/assets/img/android/push/inline_image_push_android_1.png?bf2ba99d9b6423b4d8d94e5d8d9c5908){: style="max-width:50%;"}

### Compatibility

While you can send inline images to any device, devices and SDKs that don't meet the minimum versions will display a standard image instead. For inline images to display properly, both the Android Braze SDK v10.0.0+ and a device running Android M+ are required. The SDK must also be enabled for the image to render.

**Note:**


Devices running Android 12 will render differently due to changes in custom push notification styles.



### Sending an inline image push

When creating an Android push message, this feature is available in the **Notification Type** dropdown.

![The push campaign editor showing the location of the "Notification Type" dropdown (above the standard push preview).](https://www.braze.com/docs/assets/img/android/push/android_inline_image_notification_type.png?fc31f4cadbcef37649e3b980d03ce868)

## Settings

There are many advanced settings available for Android push notifications sent through the Braze dashboard. This article will describe these features and how to use them successfully.

![](https://www.braze.com/docs/assets/img_archive/android_advanced_settings.png?8131f34243617db90fdf5780cbc3cf33)

### Notification ID {#notification-id}

A **Notification ID** is a unique identifier for a message category of your choosing that informs the messaging service to only respect the most recent message from that ID. Setting a notification ID allows you to send just the most recent and relevant message, rather than a stack of outdated, irrelevant ones.

### Firebase Messaging Delivery priority {#fcm-priority}

The [Firebase Messaging Delivery Priority](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) field lets you control whether a push is sent with "normal" or "high" priority to Firebase Cloud Messaging.

### Time to live (TTL) {#ttl}

The **Time to Live** (TTL) field allows you to set a custom length of time to store messages with the push messaging service. The default values for time to live are four weeks for FCM and 31 days for ADM.

### Summary text {#summary-text}

The summary text allows you to set additional text in the expanded notification view. It also serves as a caption for notifications with images.

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."](https://www.braze.com/docs/assets/img/android/push/collapsed-android-notification.png?fd42100702f714bd5cb65f742509c9b7){: style="max-width:65%;"}

The summary text will display under the body of the message in the expanded view. 

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."](https://www.braze.com/docs/assets/img/android/push/expanded-android-notification.png?18786f441d0d9d6b65bfcce34c43198d){: style="max-width:65%;"}

For push notifications that include images, the message text will be shown in the collapsed view, while the summary text will be displayed as the image caption when the notification is expanded. 

### Custom URIs {#custom-uri}

The **Custom URI** feature allows you to specify a Web URL or an Android resource to navigate to when the notification is clicked. If no custom URI is specified, clicking on the notification brings users into your app. You can use the custom URI to deep link inside your app and direct users to resources that exist outside of your app. This can be specified via the [Messaging API](https://www.braze.com/docs/api/endpoints/messaging/) or our dashboard under **Advanced Settings** in the push composer as pictured:

![The deep linking advanced setting in the Braze push composer.](https://www.braze.com/docs/assets/img_archive/deep_link.png?30080909d43633ac9ca7ac8d115a686a)

### Notification display priority {#notification-priority}

**Important:**


The Notification Display Priority setting is no longer used on devices running Android O or newer. For newer devices, set the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance).



The priority level of a push notification affects how your notification is displayed in the notification tray relative to other notifications. It can also affect the speed and manner of delivery, as normal and lower priority messages may be sent with slightly higher latency or batched to preserve battery life, whereas high priority messages are always sent immediately.

In Android O, notification priority became a property of notification channels. You will need to work with your developer to define the priority for a channel during its configuration and then use the dashboard to select the proper channel when sending your notification sounds. For devices running versions of Android before O, specifying a priority level for Android notifications is possible via the Braze dashboard and messaging API. 

To message your full user base with a specific priority, we recommend that you indirectly specify the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance) (to target O+ devices) *and* send the individual priority from the dashboard (to target &#60;O devices).

The priority levels that you can set on Android or Fire OS push notifications are:

| Priority | Description/Intended Use | `priority` value (for API messages) |
|----------|--------------------------|-------------------------------------|
| Max      | Urgent or time-critical messages | `2` |
| High     | Important communication, such as a new message from a friend | `1` |
| Default  | Most notifications - use if your message doesn't explicitly fall under any of the other priority types | `0` |
| Low      | Information that you want users to know about but does not require immediate action | `-1` |
| Min      | Contextual or background information. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For more information, refer to Google's [Android notification](http://developer.android.com/design/patterns/notifications.html) documentation.

### Sounds {#sounds}

In Android O, notification sounds became a property of notification channels. You will need to work with your developer to define the sound for a channel during its configuration and then use the dashboard to select the proper channel when sending your notifications.

For devices running versions of Android before O, Braze allows you to set the sound of an individual push message through the dashboard composer. You can do so by specifying a local sound resource on the device (for example, `android.resource://com.mycompany.myapp/raw/mysound`). Specifying "default" in this field will play the default notification sound on the device. This can be specified via the [Messaging API](https://www.braze.com/docs/api/endpoints/messaging/) or the dashboard under **Advanced Settings** in the push composer.

![The sound advanced setting in the Braze push composer.](https://www.braze.com/docs/assets/img_archive/sound_android.png?70e53c2fdff6155d172b0399de090593)

Enter the full sound resource URI (for example, `android.resource://com.mycompany.myapp/raw/mysound`) into the dashboard prompt.

To message your full user base with a specific sound, we recommend that you indirectly specify the sound through [notification channel configuration](https://developer.android.com/training/notify-user/channels) (to target O+ devices) *and* send the individual sound from the dashboard (to target &#60;O devices).




## Prerequisites

Before you can use this feature, you'll need to [integrate the Swift Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=swift).

## Customizing action buttons {#push-action-buttons-integration}

The Braze Swift SDK provides URL handling support for push action buttons. There are four sets of default push action buttons for Braze default push categories: `Accept/Decline`, `Yes/No`, `Confirm/Cancel`, and `More`.

![A GIF of a push message being pulled down to display two customizable action buttons.](https://www.braze.com/docs/assets/img_archive/iOS8Action.gif?d3553a68ae1aa0c3a58da9e65174f404){: style="max-width:60%"}

### Manually registering action buttons

**Important:**


Manually registering push action buttons are not recommended.



If you [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=swift) using the `configuration.push.automation` configuration option, Braze automatically registers the action buttons for the default push categories and handles the push action button click analytics and URL routing.

However, you can choose to manually register push action buttons instead.

#### Step 1: Adding Braze default push categories {#registering}

Use the following code to register for the default push categories when you [register for push](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze):



a
```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```




```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```




**Note:**


Clicking on push action buttons with background activation mode will only dismiss the notification and not open the app. The next time the user opens the app, the button click analytics for these actions will be flushed to the server.



#### Step 2: Enable interactive push handling {#enable-push-handling}

To enable our push action button handling, including click analytics and URL routing, add the following code to your app's `didReceive(_:completionHandler:)` delegate method:




```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```




```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```




If you use the `UNNotification` framework and have implemented the Braze [notification methods](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling), you should already have this method integrated. 

## Customizing push categories {#customizing-push-categories}

In addition to providing a set of default push categories, Braze supports custom notification categories and actions. After you register categories in your application, you can use the Braze dashboard to send these custom notification categories to your users.

Here's an example that leverages the `LIKE_CATEGORY` displayed on the device:

![A push message displaying two push action buttons "unlike" and "like".](https://www.braze.com/docs/assets/img_archive/push_example_category.png?342eb7b8bc6d24142ee32606e22f8eee)

### Step 1: Register a category

To register a category in your app, use a similar approach to the following:




```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```




```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```




**Note:**


When you create a `UNNotificationAction`, you can specify a list of action options. For example, `.foreground` lets your users open your app after tapping the action button. This is necessary for navigational on-click behaviors, such as "Open App" and "Deep Link into Application". If you want an action button that simply dismisses the notification without opening the app, leave `.foreground` out of the action's `options` array. For more information, see [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).



### Step 2: Select your categories

After you register a category, use the Braze dashboard to send notifications of that type to users.

**Tip:**


You only need to define action buttons on the Braze dashboard for behaviors that can't be created locally in your Swift code, such as deep linking into your app or redirecting to a web URL. These actions need to be configured on the dashboard so they can define what URL or deep link to open. For action buttons that simply dismiss the notification without opening the app, you don't need to configure them on the dashboard—dismissal behavior is handled automatically by iOS. Just register your custom category and its actions in your app code, then enter the matching category name on the dashboard.



1. In the Braze dashboard, select **Messaging** > **Push Notifications**, then choose your iOS [push campaign](https://www.braze.com/docs/user_guide/message_building_by_channel/push/creating_a_push_message).
2. Under **Compose push notification**, turn on **Action Buttons**.
3. In the **iOS Notification Category** dropdown, select **Enter pre-registered custom iOS Category**.
4. Finally, enter one of the categories you created earlier. The following example, uses the custom category: `LIKE_CATEGORY`.

![The push notification campaign dashboard with the setup for custom categories.](https://www.braze.com/docs/assets/img_archive/ios-notification-category.png?3773374b98a8bfab3549164f0b8eedd1)

### Example: Custom push category {#example-custom-push-category}

Suppose you want to create a push notification with two action buttons: **Manage**, which deep links into your app, and **Keep**, which simply dismisses the notification.

In the following example, the `MANAGE_IDENTIFIER` action includes the `.foreground` option, which opens the app when tapped—this is necessary because it will deep link into a specific part of the app. The `KEEP_IDENTIFIER` action uses an empty options array, meaning it will dismiss the notification without opening the app.




```swift
Braze.Notifications.categories.insert(
  .init(identifier: "YOUR_CATEGORY",
        actions: [
          .init(identifier: "KEEP_IDENTIFIER", title: "Keep", options: []),
          .init(identifier: "MANAGE_IDENTIFIER", title: "Manage", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```




Because `MANAGE_IDENTIFIER` deep links into the app, you would set up that action button on the Braze dashboard with the associated deep link URL. However, you don't need to define a button on the dashboard for `KEEP_IDENTIFIER` because it only dismisses the notification. On the dashboard, you only need to enter the category name (for example, `YOUR_CATEGORY`) to match what you registered in your app code.

## Customizing badges

Badges are small icons that are ideal for getting a user's attention. You can specify a badge count in the [**Settings**](https://www.braze.com/docs/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) tab when you compose a push notification using the Braze dashboard. You may also update your badge count manually through your application's [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) property or the [remote notification payload](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). 

Braze will automatically clear the badge count when a Braze notification is received while the app is in the foreground. Manually setting the badge number to 0 will also clear notifications in the notification center. 

If you do not have a plan for clearing badges as part of normal app operation or by sending pushes that clear the badge, you should clear the badge when the app becomes active by adding the following code to your app's `applicationDidBecomeActive:` delegate method:




```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```




```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```




## Customizing sounds

### Step 1: Host the sound in your app

Custom push notification sounds must be hosted locally within the main bundle of your app. The following audio data formats are accepted:

- Linear PCM
- MA4
- µLaw
- aLaw

You can package the audio data in an AIFF, WAV, or CAF file. In Xcode, add the sound file to your project as a non-localized resource of the application bundle.

**Note:**


Custom sounds must be under 30 seconds when played. If a custom sound is over that limit, the default system sound is played instead.



#### Converting sound files

You can use the afconvert tool to convert sounds. For example, to convert the 16-bit linear PCM system sound Submarine.aiff to IMA4 audio in a CAF file, use the following command in the terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

**Tip:**


You can inspect a sound to determine its data format by opening it in QuickTime Player and choosing **Show Movie Inspector** from the **Movie** menu. 



### Step 2: Provide a protocol URL for the sound

You must specify a protocol URL that directs to the location of the sound file in your app. There are two methods for doing this:

* Use the `sound` parameter of the [Apple push object](https://www.braze.com/docs/api/objects_filters/messaging/apple_object#apple-push-object) to pass the URL to Braze.
* Specify the URL in the dashboard. In the [push composer](https://www.braze.com/docs/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android), select **Settings** and enter the protocol URL in the **Sound** field. 

![The push composer in the Braze dashboard](https://www.braze.com/docs/assets/img_archive/sound_push_ios.png?c035b34ffb6c0f720f6d2c08ca1ba2b2)

If the specified sound file doesn't exist or the keyword "default" is entered, Braze will use the default device alert sound. Aside from our dashboard, sound can also be configured via our [messaging API][12].

See the Apple Developer Documentation regarding [preparing custom alert sounds](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) for additional information.

## Settings

When creating a push campaign through the dashboard, click the **Settings** tab on the **Compose** step to view the advanced settings available.

![](https://www.braze.com/docs/assets/img_archive/ios_advanced_settings.png?16f142abe70d854830708b0cb21d9465)

### Key-value pairs

Braze allows you to send custom-defined string key-value pairs, known as `extras`, along with a push notification to your application. Extras can be defined via the dashboard or API and will be available as key-value pairs within the `notification` dictionary passed to your push delegate implementations.

### Alert options

Select the **Alert Options** checkbox to see a dropdown of key-values available to adjust how the notification appears on devices.

### Adding content-available flag

Check the **Add Content-Available Flag** checkbox to instruct devices to download new content in the background. Most commonly, this can be checked if you are interested in sending [silent notifications](https://www.braze.com/docs/developer_guide/push_notifications/silent/?sdktab=swift).

### Adding mutable-content flag

Check the **Add Mutable-Content Flag** checkbox to enable advanced receiver customization. This flag will automatically be sent when composing a [rich notification](https://www.braze.com/docs/developer_guide/push_notifications/rich/?sdktab=swift), regardless of the value of this checkbox.

### Collapse ID

Specify a collapse ID to coalesce similar notifications. If you send multiple notifications with the same collapse ID, the device will only show the most recently received notification. Refer to Apple's documentation on [coalesced notifications](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

### Expiry

Checking the **Expiry** checkbox will allow setting an expiration time for your message. Should a user's device lose connectivity, Braze will continue to try and send the message until the specified time. If this is not set, the platform will default to an expiration of 30 days. Note that push notifications that expire before delivery are not considered failed and will not be recorded as a bounce.




## Prerequisites

Before you can use this feature, you'll need to [integrate the Android Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=android).

## Settings

There are many advanced settings available for FireOS push notifications sent through the Braze dashboard. This article will describe these features and how to use them successfully.

![](https://www.braze.com/docs/assets/img_archive/android_advanced_settings.png?8131f34243617db90fdf5780cbc3cf33)

### Time to live (TTL) {#ttl}

The **Time to Live** (TTL) field allows you to set a custom length of time to store messages with the push messaging service. The default values for time to live are four weeks for FCM and 31 days for ADM.

### Summary text {#summary-text}

The summary text allows you to set additional text in the expanded notification view. It also serves as a caption for notifications with images.

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."](https://www.braze.com/docs/assets/img/android/push/collapsed-android-notification.png?fd42100702f714bd5cb65f742509c9b7){: style="max-width:65%;"}

The summary text will display under the body of the message in the expanded view. 

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."](https://www.braze.com/docs/assets/img/android/push/expanded-android-notification.png?18786f441d0d9d6b65bfcce34c43198d){: style="max-width:65%;"}

For push notifications that include images, the message text will be shown in the collapsed view, while the summary text will be displayed as the image caption when the notification is expanded. 

### Custom URIs {#custom-uri}

The **Custom URI** feature allows you to specify a Web URL or an Android resource to navigate to when the notification is clicked. If no custom URI is specified, clicking on the notification brings users into your app. You can use the custom URI to deep link inside your app and direct users to resources that exist outside of your app. This can be specified via the [Messaging API](https://www.braze.com/docs/api/endpoints/messaging) or our dashboard under **Advanced Settings** in the push composer as pictured:

![The deep linking advanced setting in the Braze push composer.](https://www.braze.com/docs/assets/img_archive/deep_link.png?30080909d43633ac9ca7ac8d115a686a)

### Notification display priority

**Important:**


The Notification Display Priority setting is no longer used on devices running Android O or newer. For newer devices, set the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance).



The priority level of a push notification affects how your notification is displayed in the notification tray relative to other notifications. It can also affect the speed and manner of delivery, as normal and lower priority messages may be sent with slightly higher latency or batched to preserve battery life whereas high priority messages are always sent immediately.

In Android O, notification priority became a property of notification channels. You will need to work with your developer to define the priority for a channel during its configuration and then use the dashboard to select the proper channel when sending your notification sounds. For devices running versions of Android before O, specifying a priority level for FireOS notifications is possible via the Braze dashboard and messaging API. 

To message your full user base with a specific priority, we recommend that you indirectly specify the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance) (to target O+ devices) *and* send the individual priority from the dashboard (to target &#60;O devices).

The priority levels that you can set on Fire OS push notifications are:

| Priority | Description/Intended Use | `priority` value (for API messages) |
|----------|--------------------------|-------------------------------------|
| Max      | Urgent or time-critical messages | `2` |
| High     | Important communication, such as a new message from a friend | `1` |
| Default  | Most notifications - use if your message doesn't explicitly fall under any of the other priority types | `0` |
| Low      | Information that you want users to know about but does not require immediate action | `-1` |
| Min      | Contextual or background information. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For more information, refer to Google's [Android notification](http://developer.android.com/design/patterns/notifications.html) documentation.

### Sounds {#sounds}

In Android O, notification sounds became a property of notification channels. You will need to work with your developer to define the sound for a channel during its configuration and then use the dashboard to select the proper channel when sending your notifications.

For devices running versions of Android before O, Braze allows you to set the sound of an individual push message through the dashboard composer. You can do so by specifying a local sound resource on the device (for example, `android.resource://com.mycompany.myapp/raw/mysound`). Specifying "default" in this field will play the default notification sound on the device. This can be specified via the [Messaging API](https://www.braze.com/docs/api/endpoints/messaging) or the dashboard under **Settings** in the push composer.

![The sound advanced setting in the Braze push composer.](https://www.braze.com/docs/assets/img_archive/sound_android.png?70e53c2fdff6155d172b0399de090593)

Enter the full sound resource URI (for example, `android.resource://com.mycompany.myapp/raw/mysound`) into the dashboard prompt.

To message your full user base with a specific sound, we recommend that you indirectly specify the sound through [notification channel configuration](https://developer.android.com/training/notify-user/channels) (to target O+ devices) *and* send the individual sound from the dashboard (to target &#60;O devices).




## Prerequisites

Before you can use this feature, you'll need to [integrate the React Native Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native). You must also [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=react%20native).

## Push customization in React Native

The Braze React Native SDK does not expose push notification customization (action buttons, categories, custom notification factories) through its JavaScript API. These features require native configuration in your iOS and Android projects.

The following table shows which features require native configuration:

| Feature | iOS | Android |
| --- | --- | --- |
| Action buttons | Configure in native Swift/Objective-C | Configure in native Java/Kotlin |
| Push categories | Configure in native Swift/Objective-C | Configure in native Java/Kotlin |
| Custom notification factory | N/A | Configure in native Java/Kotlin |
| Badge customization | Configure in native Swift/Objective-C | N/A |
| Custom sounds | Configure in native Swift/Objective-C | Configure in native Java/Kotlin |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### iOS customization

To add push action buttons, categories, badges, or custom sounds on iOS, implement the native configuration in your `AppDelegate` (Swift or Objective-C). See [Customize push notifications – Swift](https://www.braze.com/docs/developer_guide/push_notifications/customization/?sdktab=swift) for step-by-step instructions.

### Android customization

To add push action buttons, categories, or a custom notification factory on Android, implement the native configuration in your Android project. See [Customize push notifications – Android](https://www.braze.com/docs/developer_guide/push_notifications/customization/?sdktab=android) for step-by-step instructions.



