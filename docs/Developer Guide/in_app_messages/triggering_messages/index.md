# Trigger in-app messages

> Learn how to trigger in-app messages through the Braze SDK.

## Message triggers and delivery

In-app messages are triggered when the SDK logs one of the following custom event types: `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase`,and `Custom Event` (the last two containing robust property filters).

At the start of a user's session, Braze will deliver all eligible in-app messages to their device, while simultaneously prefetching assets to minimize display latency. If the trigger event has more than one eligible in-app message, only the message with the highest priority will be delivered. For more information, see [Session Lifecycle](https://www.braze.com/docs/developer_guide/analytics/tracking_sessions/#about-the-session-lifecycle).

**Note:**


In-app messages can't be triggered through the API or by API events&#8212;only custom events logged by the SDK. To learn more about logging, see [Logging Custom Events](https://www.braze.com/docs/developer_guide/analytics/logging_events/).



## Types of in-app messages

Braze sends the following types of in-app messages to user devices upon session start: `inapp` and `templated_iam`. As a dashboard user, you don't see the different types, but Braze handles them differently depending on the setup and content.

### `inapp` (standard)

An `inapp` (or "[standard](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/#standard-message-types)") in-app message is already templated with the necessary information, such as custom attributes that Braze already knows. Generally, when the in-app message downloads to the device, the trigger event causes the SDK to display the `inapp` in-app message even when the device is offline or on airplane mode.

### `templated_iam` (templated)

A `templated_iam` (or "templated") in-app message isn't yet templated with the necessary information. Braze must make another request to pull in the information before the message can appear.

In-app messages are delivered as templated in-app messages when **Re-evaluate campaign eligibility before displaying** is selected or if any of the following Liquid tags exist in the message:

- `canvas_entry_properties`
- `connected_content`
- SMS variables such as `{sms.${*}}`
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

This means that during session start, the device will receive the trigger of that in-app message instead of the entire message. When the user triggers the in-app message, the user's device will make a network request to fetch the actual message.

**Note:**


The message will not be delivered if the device doesn't have access to the internet. The message might not be delivered if the Liquid logic takes too long to resolve.



## Key-value pairs

When you create a campaign in Braze, you can set key-value pairs as `extras`, which the in-app messaging object can use to send data to your app.



```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```





```java
Map<String, String> getExtras()
```


```kotlin
extras: Map<String, String>
```



**Tip:**


For more information, refer to the [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).





The following example uses custom logic to set the presentation of an in-app message based on it's key-value pairs in `extras`. For a full customization example, check out [our sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).




```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```



```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```





## Disabling automatic triggers

By default, in-app messages are triggered automatically. To disable this:




Remove the call to `braze.automaticallyShowInAppMessages()` within your loading snippet, then create custom logic to handle showing or not showing an in-app message.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

**Important:**


If you call `braze.showInAppMessage` without removing `braze.automaticallyShowInAppMessages()`, messages may display twice.



For more advanced control over message timing, including deferring and restoring triggered messages, refer to our [Tutorial: Deferring and restoring triggered messages](https://www.braze.com/docs/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).



1. Implement the [`IInAppMessageManagerListener`](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?sdktab=android&tab=global%20listener#android_step-1-implement-the-custom-manager-listener) to set a custom listener.
2. Update your [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) method to return [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html).

For more advanced control over message timing, including displaying later and re-enqueuing, refer to our [Customizing Messages](https://www.braze.com/docs/developer_guide/in_app_messages/customization/?tab=global%20listener&subtab=kotlin#android_step-2-instruct-braze-to-use-the-custom-manager-listener) page.



1. Implement the `BrazeInAppMessageUIDelegate` delegate in your app. For a full walkthrough, refer to [Tutorial: In-App Message UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Update your `inAppMessage(_:displayChoiceForMessage:)` delegate method to return `.discard`.

For more advanced control over message timing, including deferring and restoring triggered messages, refer to our [Tutorial: Deferring and restoring triggered messages](https://www.braze.com/docs/developer_guide/in_app_messages/tutorials/deferring_triggered_messages).



1. Verify you're using the automatic integration initializer, which is enabled by default in versions `2.2.0` and later.
2. Set the in-app message operation default to `DISCARD` by adding the following line to your `braze.xml` file.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```





For Android, deselect **Automatically Display In-App Messages** in the Braze configuration editor. Alternatively, you can set `com_braze_inapp_show_inapp_messages_automatically` to `false` in your Unity project's `braze.xml`.

The initial in-app message display operation can be set in Braze config using the "In App Message Manager Initial Display Operation".



For iOS,  set game object listeners in the Braze configuration editor and ensure **Braze Displays In-App Messages** is not selected.

The initial in-app message display operation can be set in Braze config using the "In App Message Manager Initial Display Operation".





## Chaining two in-app messages in one session

You can trigger an in-app message from session start, then trigger a second in-app message after a button is pressed in the first. To do this, log a custom event for the button click that will trigger the second message. The trigger for the second message must already be on the device (the user must already be eligible for the second message), and occur on the device side (the Braze SDK won't pick up custom attribute changes that occur on Braze servers). The default 30-second cooldown between in-app message triggers must be altered to show multiple in-app messages in quick succession. For platform-specific configuration, see [Overriding the default rate limit](#overriding-the-default-rate-limit).

## Overriding the default rate limit

By default, the SDK rate-limits triggered in-app messages to once every 30 seconds. To override this, add the following property to your configuration file before the Braze instance is initialized. This value is used as the new rate limit in seconds.

For production apps, don't set this value lower than 10 seconds, so users aren't overwhelmed with back-to-back in-app messages. For testing and sample app flows, 5 seconds is a common setting.

You can set this interval to `0` for testing. However, a `0`-second interval doesn't force multiple in-app messages to appear at the same time. If one in-app message is already visible, another triggered message isn't displayed until the current message is dismissed.



```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```



```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```





```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```


```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```





## Manually triggering messages

By default, in-app messages are automatically triggered when the SDK logs a custom event. However, in addition to this, you can manually trigger messages using the following methods.

### Using a server-side event



At this time, the Web Braze SDK does not support manually triggering messages using server-side events.



To trigger an in-app message using a server-sent event, send a silent push notification to the device, which allows a custom push callback to log an SDK-based event. This event will then trigger the user-facing in-app message.

#### Step 1: Create a push callback to receive the silent push

Register your custom push callback to listen for a specific silent push notification. For more information, refer to [Setting up push notifications](https://www.braze.com/docs/developer_guide/push_notifications#android_setting-up-push-notifications).

Two events will be logged for the in-app message to be delivered, one by the server and one from within your custom push callback. To make sure the same event is not duplicated, the event logged from within your push callback should follow a generic naming convention, for example, "in-app message trigger event," and not the same name as the server sent event. If this is not done, segmentation and user data may be affected by duplicate events being logged for a single user action.




```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```




```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```




#### Step 2: Create a push campaign

Create a [silent push campaign](https://www.braze.com/docs/developer_guide/push_notifications/silent/?sdktab=android) triggered via the server sent event.

![](https://www.braze.com/docs/assets/img_archive/serverSentPush.png?ba3ed6cdbb6033f36d1e824f9ac5c350)

The push campaign must include key-value pair extras that indicate that this push campaign is sent to log an SDK custom event. This event will be used to trigger the in-app message.

![Two sets of key-value pairs: IS_SERVER_EVENT set to "true", and CAMPAIGN_NAME set to "example campaign name".](https://www.braze.com/docs/assets/img_archive/kvpConfiguration.png?2bd106b4fee497321c428fe8b8a6ccbe){: style="max-width:70%;" }

The earlier push callback sample code recognizes the key-value pairs and logs the appropriate SDK custom event.

Should you want to include any event properties to attach to your "in-app message trigger" event, you can achieve this by passing these in the key-value pairs of the push payload. In this example, the campaign name of the subsequent in-app message has been included. Your custom push callback can then pass the value as the parameter of the event property when logging the custom event.

#### Step 3: Create an in-app message campaign

Create your user-visible in-app message campaign in the Braze dashboard. This campaign should have an action-based delivery and be triggered from the custom event logged from within your custom push callback.

In the following example, the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![An action-based delivery campaign where an in-app message will trigger when "campaign_name" equals "IAM campaign name example."](https://www.braze.com/docs/assets/img_archive/iam_event_trigger.png?131d09d4b7d8389dca24630f1e3ad054)

If a server-sent event is logged while the app is not in the foreground, the event will log, but the in-app message will not be displayed. Should you want the event to be delayed until the application is in the foreground, a check must be included in your custom push receiver to dismiss or delay the event until the app has entered the foreground.



#### Step 1: Handle silent push and key-value pairs

Implement the following function and call it within the [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`: method](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/):




```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```




```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```




When the silent push is received, an SDK recorded event "in-app message trigger" will be logged against the user profile. 

**Important:**


Due to a push message being used to record an SDK logged custom event, Braze will need to store a push token for each user to enable this solution. For iOS users, Braze will only store a token from the point that a user has been served the OS's push prompt. Before this, the user will not be reachable using push, and the preceding solution will not be possible.



#### Step 2: Create a silent push campaign

Create a [silent push campaign](https://www.braze.com/docs/developer_guide/push_notifications/silent/?sdktab=swift) that is triggered via the server-sent event. 

![An action-based delivery in-app message campaign that will be delivered to users whose user profiles have the custom event "server_event".](https://www.braze.com/docs/assets/img_archive/iosServerSentPush.png?f2398c5efce1eef517dc7eabe0b5801b)

The push campaign must include key-value pair extras, which indicate that this push campaign is sent to log an SDK custom event. This event will be used to trigger the in-app message.

![An action-based delivery in-app message campaign that has two key-value pairs. "CAMPAIGN_NAME" set as "In-app message name example", and "IS_SERVER_EVENT" set to "true".](https://www.braze.com/docs/assets/img_archive/iOSServerPush.png?e84dc261f2b58bc43d35748e9c7db7f7)

The code within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method checks for key `IS_SERVER_EVENT` and will log an SDK custom event if this is present.

You can alter either the event name or event properties by sending the desired value within the key-value pair extras of the push payload. When logging the custom event, these extras can be used as the parameter of either the event name or as an event property.

#### Step 3: Create an in-app message campaign

Create your user-visible in-app message campaign in the Braze dashboard. This campaign should have an action-based delivery and be triggered from the custom event logged from within the `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` method.

In the following example, the specific in-app message to be triggered has been configured by sending the event property as part of the initial silent push.

![An action-based delivery in-app message campaign that will be delivered to users who perform the custom event "In-app message trigger" where "campaign_name" equals "IAM Campaign Name Example".](https://www.braze.com/docs/assets/img_archive/iosIAMeventTrigger.png?2f425e73fa63c23e0270be6007c72cbe)

**Note:**


Note that these in-app messages will only trigger if the silent push is received while the application is in the foreground.





### Displaying a pre-defined message

To manually display a pre-defined in-app message, use the following method:



For the Web SDK, use `braze.showInAppMessage(inAppMessage)` to display any in-app message. For details and an example, see [Displaying a message in real-time](#displaying-a-message-in-real-time).






```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```




```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```






```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```



### Displaying a message in real-time 

You can also create and display local in-app messages in real-time, using the same customization options available on the dashboard. To do so:



```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```






```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```




```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```




**Important:**


Do not display in-app messages when the soft keyboard is displayed on the screen as rendering is undefined in this circumstance.





Manually call the [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) method on your `inAppMessagePresenter`. For example:




```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```




```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```




**Note:**


Creating your own in-app message, you opt out of any analytics tracking and will have to manually handle click and impression logging using your `message.context`.





To display the next message in the stack, use the `DisplayNextInAppMessage()` method. Messages will be saved to this stack if `DISPLAY_LATER` or `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` is chosen as the in-app message display action.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```



## Causes of in-app message delays

If you receive an in-app message campaign a few seconds after session start, the delay may have been caused by:

- A delay in the campaign trigger
- Customizations
- The trigger event recording later than you expected (such as with a `templated_iam`)

## Exit-intent messages for Web

Exit-intent messages are non-disruptive in-app messages used to communicate important information to visitors before they leave your web site.

To set up triggers for these message types in the Web SDK, implement an exit-intent library in your website (such as [ouibounce's open-source library](https://github.com/carlsednaoui/ouibounce)), then use the following code to log `'exit intent'` as a custom event in Braze. Now your future in-app message campaigns can use this message type as a custom event trigger.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
