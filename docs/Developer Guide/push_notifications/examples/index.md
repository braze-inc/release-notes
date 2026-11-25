# Advanced push notification examples

> The following guide covers some advanced push notifications examples for the Braze SDK.



## Prerequisites

Before you can use this feature, you'll need to [integrate the Android Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=android). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications?sdktab=android).

## Custom notification layout

Braze notifications are sent as [data messages](https://firebase.google.com/docs/cloud-messaging/concept-options), which means that your application will always have a chance to respond and perform behavior accordingly, even in the background (in contrast to notification messages, which can be handled automatically by the system when your app is in the background). As such, your application will have a chance to customize the experience by, for example displaying personalized UI elements within the notification delivered to the notification tray. While implementing push in this way may be unfamiliar to some, one of our well-known features at Braze, [Push Stories](https://www.braze.com/docs/user_guide/channels/push/create_a_push_message/push_stories), are a prime example of using custom view components to create an engaging experience!

**Important:**


Android imposes some limitations on what components can be used to implement custom notification views. Notification view layouts must _only_ contain View objects compatible with the [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) framework.



You can use the [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) interface to customize how Braze push notifications are displayed. By extending `BrazeNotificationFactory`, Braze will call your factory's `createNotification()` method before the notification is displayed to the user. It will then pass a payload containing custom key-value pairs sent through the Braze dashboard or REST API.

In this section, you'll partner with Superb Owl, the host of a new game show where wildlife rescue teams compete to see who can save the most owls. They're looking to leverage live updating notifications in their Android app, so they can display the status of an on-going match and make dynamic updates to the notification in realtime.

![The Live Update that Superb Owl wants to show, displaying an on-going match between 'Wild Bird Fund' and 'Owl Rescue'. It's currently the fourth quarter and the score is 2-4 with OWL in the lead.](https://www.braze.com/docs/assets/img/android/android-live-activity-superb-owl-example.jpg?b7c1563bedc808b7a9aba3771231ddc4){: style="max-width:65%;"}

### Step 1: Add a custom layout

You can add one or more custom notification RemoteView layouts to your project. These are helpful for handling how notifications are displayed when collapsed or expanded. Your directory structure should be similar to the following:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

In each XML file, create a custom layout. Superb Owl created the following layouts for their collapsed and expanded RemoteView layouts:



```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/notification_title"
        style="@style/TextAppearance.Compat.Notification.Title"
        android:layout_width="wrap_content"
        android:layout_height="0dp"
        android:layout_weight="1" />
</LinearLayout>
```



**Show the sample code**


```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"

        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team1logo"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:layout_gravity="center"
            android:src="@drawable/team_default1"/>

        <TextView
            android:id="@+id/team1name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1.6"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/score"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="2-4"
            android:textColor="#555555"
            android:textAlignment="center"
            android:textSize="32sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/timeInfo"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>


    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team2logo"
            android:layout_gravity="center"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:src="@drawable/team_default2"/>

        <TextView
            android:id="@+id/team2name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>
</LinearLayout>
```





### Step 2: Create a custom notification factory

In your application, create a new file named `MyCustomNotificationFactory.kt` that extends [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) to handle how custom RemoteView layouts are displayed.

In the following example, Superb Owl created a custom notification factory to display a RemoteView layout for on-going matches. In the [next step](#android_step-3-map-custom-data), they'll create a new method called `getTeamInfo` to map a team's data to the activity.

**Show the sample code**


```kotlin
import android.app.Notification
import android.widget.RemoteViews
import androidx.core.app.NotificationCompat
import com.braze.models.push.BrazeNotificationPayload
import com.braze.push.BrazeNotificationFactory
import com.braze.push.BrazeNotificationUtils.getOrCreateNotificationChannelId
import com.braze.support.BrazeLogger.brazelog

class MyCustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        if (payload.extras.containsKey("live_update")) {
            val kvp = payload.extras
            val notificationChannelId = getOrCreateNotificationChannelId(payload)
            val context = payload.context

            if (context == null) {
                brazelog { "BrazeNotificationPayload has null context. Not creating notification" }
                return null
            }

            val team1 = kvp["team1"]
            val team2 = kvp["team2"]
            val score1 = kvp["score1"]
            val score2 = kvp["score2"]
            val time = kvp["time"]
            val quarter = kvp["quarter"]

            // Superb Owl will define the 'getTeamInfo' method in the next step.
            val (team1name, team1icon) = getTeamInfo(team1)
            val (team2name, team2icon) = getTeamInfo(team2)

            // Get the layouts to use in the custom notification.
            val notificationLayoutCollapsed = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_collapsed)
            val notificationLayoutExpanded = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_expanded)

            // Very simple notification for the small layout
            notificationLayoutCollapsed.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $quarter"
            )

            notificationLayoutExpanded.setTextViewText(R.id.score, "$score1 - $score2")
            notificationLayoutExpanded.setTextViewText(R.id.team1name, team1name)
            notificationLayoutExpanded.setTextViewText(R.id.team2name, team2name)
            notificationLayoutExpanded.setTextViewText(R.id.timeInfo, "$time - $quarter")
            notificationLayoutExpanded.setImageViewResource(R.id.team1logo, team1icon)
            notificationLayoutExpanded.setImageViewResource(R.id.team2logo, team2icon)

            val customNotification = NotificationCompat.Builder(context, notificationChannelId)
                .setSmallIcon(R.drawable.notification_small_icon)
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(notificationLayout)
                .setCustomBigContentView(notificationLayoutExpanded)
                .build()
            return customNotification
        } else {
            // Use the BrazeNotificationFactory for all other notifications
            return super.createNotification(payload)
        }
    }
}
```



### Step 3: Map custom data

In `MyCustomNotificationFactory.kt`, create a new method for handling data when Live Updates are displayed.

Superb Owl created the following method to map each team's name and logo to expanded Live Updates:

```kotlin
class CustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Your existing code
        return super.createNotification(payload)
    }

    // Your new method
    private fun getTeamInfo(team: String?): Pair<String, Int> {
        return when (team) {
            "WBF" -> Pair("Wild Bird Fund", R.drawable.team_wbf)
            "OWL" -> Pair("Owl Rehab", R.drawable.team_owl)
            else  -> Pair("Unknown", R.drawable.notification_small_icon)
        }
    }
}
```

### Step 4: Set the custom notification factory

In your application class, use [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?)to set your custom notification factory.

```kotlin
import com.braze.Braze

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Step 5: Send the activity

You can use the [`/messages/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages) REST API endpoint to send a push notification to a user's Android device.

#### Example curl command

Superb Owl sent their request using the following curl command:

```
curl -X POST "https://BRAZE_REST_ENDPOINT/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["USER_ID"],
    "messages": {
      "android_push": {
        "title": "WBF vs OWL",
        "alert": "2 to 4 1:33 Q4",
        "extra": {
          "live_update": "true",
          "team1": "WBF",
          "team2": "OWL",
          "score1": "2",
          "score2": "4",
          "time": "1:33",
          "quarter": "Q4"
        },
        "notification_id": "ASSIGNED_NOTIFICATION_ID"
      }
    }
  }'
```

**Tip:**


While curl commands are helpful for testing, we recommend handling this call in your backend where you're already handling your [iOS Live Activities](https://www.braze.com/docs/developer_guide/push_notifications/live_notifications?sdktab=swift).



#### Request parameters

| Key                           | Description                                                                                                                                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY`                | A Braze REST API key with `messages.send` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**.                                                                                                     |
| `BRAZE_REST_ENDPOINT`         | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance](https://www.braze.com/docs/api/basics#endpoints).                                                                                                                  |
| `USER_ID`                     | The ID of the user you are sending the notification to.                                                                                                                                                                                          |
| `messages.android_push.title` | The message's title. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback.                                                                                                    |
| `messages.android_push.alert` | The message's body. By default, this is not used for the custom notification factory's live notifications, but it may be used as a fallback.                                                                                                     |
| `messages.extra`              | Key-value pairs that the custom notification factory uses for live notifications. You can assign any string to this value&#8212;however, in this example, `live_updates` is used to determine if it's a default or live push notification.  |
| `ASSIGNED_NOTIFICATION_ID`    | The notification ID you want to assign to the chosen user's live notification. The ID must be unique to this game, and must be used in order to [update their existing notification](#android_step-4-update-data-with-the-braze-rest-api) later. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Request parameters" }

### Step 6: Update the activity

To update the existing RemoteView notification with new data, modify the relevant key-value pairs assigned to `messages.extra`, then use the same `notification_id` and call the `/messages/send` endpoint again.

## Personalized push notifications

Push notifications can display user-specific information inside a custom view hierarchy. In the following example, an API-trigger is used to send personalized push notification to a user so they can track check their current progress after completing a specific task in the app.

![Personalized Push dashboard Example](https://www.braze.com/docs/assets/img/push_implementation_guide/android_push_custom_layout.png?42a0a3df3a4069479bfb1db1bd65bde1){: style="max-width:65%;border:0"}

To set up a personalized push in the dashboard, register the specific category you want to be displayed, then set any relevant user attributes you'd like to display using Liquid.

![Personalized Push dashboard Example](https://www.braze.com/docs/assets/img/push_implementation_guide/push5.png?199277e2adf2d1ded48e5dba4c2d7b4a){: style="max-width:60%;"}




## Prerequisites

Before you can use this feature, you'll need to [integrate the Swift Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=swift). You'll also need to [set up push notifications](https://www.braze.com/docs/developer_guide/push_notifications?sdktab=swift).

**Note:**


This implementation guide is centered around a Swift implementation, but Objective-C snippets are provided for those interested.



## Notification content app extensions

![Two push messages shown side-by side. The message on the left shows what a push looks like with the default UI. The message on the right shows a coffee punch card push made by implementing a custom push UI.](https://www.braze.com/docs/assets/img/push_implementation_guide/push1.png?d04035fb11637f7db51f24a1afab9e8f){: style="max-width:65%;border:0;margin-top:10px"}

Notification content app extensions provide you a great option for push notification customization. Notification content app extensions display a custom interface for your app’s notifications when a push notification is expanded.

Push notifications can be expanded in three different ways:
- A long press on the push banner
- Swiping down on the push banner
- Swiping the banner horizontally and selecting "View"

These custom views offer smart ways to engage customers by displaying distinct types of content, including interactive notifications, notifications populated with user data, and even push messages that can capture information like phone numbers and email. One of our well-known features at Braze, [Push Stories](https://www.braze.com/docs/user_guide/channels/push/create_a_push_message/push_stories), are a prime example of what a push notification content app extension can look like!

### Requirements

![Xcode's 'Choose a template for your new target' screen with 'Notification Content Extension' selected under Application Extension.](https://www.braze.com/docs/assets/img/push_implementation_guide/push15.png?64059ffe5c16313ee6377e0a79405812){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Push notifications](https://www.braze.com/docs/developer_guide/push_notifications?sdktab=swift) successfully integrated in your app
- The following files generated by Xcode based on your coding language:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Interactive push notification

Push notifications can respond to user actions inside a content app extension. For users running iOS 12 or later, this means you can turn your push notifications into fully interactive messages! This provides an exciting option to introduce interactivity to your promotions and applications. For example, your push notification can include a game for users to play, a spin-to-win wheel for discounts, or a "like" button to save a listing or song.

The following example shows a push notification where users are able to play a match game inside the expanded notification.

![A diagram of what the phases of a interactive push notification could look like. A sequence shows a user pressing into a push notification that displays an interactive matching game.](https://www.braze.com/docs/assets/img/push_implementation_guide/push12.png?e32579b6de7f5aec62265828724d6657){: style="border:0"}

### Dashboard configuration

To create an interactive push notification, you must set a custom view in your dashboard. 

1. From the **Campaigns** page, click  **Create Campaign** to start a new push notification campaign.
2. On the **Compose** tab, toggle on **Notification Buttons**. 
3. Enter a custom iOS category in the **iOS Notification Category** field. 
4. In the `.plist` of your Notification Content Extension Target, set the `UNNotificationExtensionCategory` attribute to your custom iOS category. The value given here must match what is set in the Braze dashboard under **iOS Notification Category**. 
5. Set the `UNNotificationExtensionInteractionEnabled` key to `true` to enable user interactions in a push notification.

![The notification button options found in the push message composer settings.](https://www.braze.com/docs/assets/img/push_implementation_guide/push16.png?be40aad198215645c3ef4ac2553267f4){: style="max-width:75%;border:0;margin-top:10px"}
![A plist showing NSExtension with UNNotificationExtensionCategory set to "your_custom_category", UNNotificationExtensionDefaultContentHidden set to 1, and UNNotificationExtensionInitialContentSizeRatio set to 1.](https://www.braze.com/docs/assets/img/push_implementation_guide/push17.png?42f5ff77b6402aade26b936b5c78dbc7){: style="max-width:75%;border:0;margin-top:10px"}

## Personalized push notifications

![Two iPhones displayed side-by-side. The first iPhone shows the unexpanded view of the push message. The second iPhone shows the expanded version of the push message displaying a "progress" shot of how far they are through a course, the name of the next session, and when the next session must be completed.](https://www.braze.com/docs/assets/img/push_implementation_guide/push6.png?438d9acc8285244397d14467a8a63d3a){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Push notifications can display user-specific information inside a content extension. This allows you to create user-focused push content, such as adding the option to share your progress across different platforms, show unlocked achievements, or display onboarding checklists. This example shows a push notification displayed to a user after they have completed a specific task in the Braze Learning course. By expanding the notification, the user can see their progress through their learning path. The information provided here is user-specific and can be fired off as a session is completed or a specific user action is taken by leveraging an API trigger. 

### Dashboard configuration

To create a personalized push notification, you must set a custom view in your dashboard. 

1. From the **Campaigns** page, click  **Create Campaign** to start a new push notification campaign.
2. On the **Compose** tab, toggle on **Notification Buttons**. 
3. Enter a custom iOS category in the **iOS Notification Category** field. 
4. In the **Settings** tab, create key-value pairs using standard Liquid. Set the appropriate user attributes you want the message to show. These views can be personalized based on specific user attributes of a specific user profile.
5. In the `.plist` of your Notification Content Extension Target, set the `UNNotificationExtensionCategory` attribute to your custom iOS category. The value given here must match what is set in the Braze dashboard under **iOS Notification Category**. 

![Four sets of key-value pairs, where "next_session_name" and "next_session_complete_date" are set as an API trigger property using Liquid, and "completed_session count" and "total_session_count" are set as a custom user attribute using Liquid.](https://www.braze.com/docs/assets/img/push_implementation_guide/push5.png?199277e2adf2d1ded48e5dba4c2d7b4a){: style="max-width:60%;"}

### Handling key-value pairs

The method `didReceive` is called when the notification content app extension has received a notification. This method can be found within the `NotificationViewController`. The key-value pairs provided in the dashboard are represented in the code through the use of a `userInfo` dictionary.

#### Parsing Key-Value Pairs from Push Notifications



``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo
     
  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}
 
  ...
}
```


```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;
   
  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {
 
  ...
 
  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```



## Information capture push notification

Push notifications can capture user information inside a content app extension, pushing the limits of what is possible with a push. Requesting user input through push notifications allows you to not only request basic information like name or email, but also prompt users to submit feedback or complete an unfinished user profile. 

**Tip:**


For more information, see [Logging push notification data](https://www.braze.com/docs/developer_guide/analytics/logging_channel_data/push_notifications).



In the following flow, the custom view is able to respond to state changes. Those state change components are represented in each image. 

1. User receives a push notification.
2. Push is opened. After expanded, the push prompts the user for information. In this example, the user's email address is requested, but you could request any sort of information.
3. Information is provided, and if in the expected format, the registration button is shown.
3. Confirmation view is displayed, and push gets dismissed. 


### Dashboard configuration

To create an information capture push notification, you must set a custom view in your dashboard. 

1. From the **Campaigns** page, click  **Create Campaign** to start a new push notification campaign.
2. On the **Compose** tab, toggle on **Notification Buttons**. 
3. Enter a custom iOS category in the **iOS Notification Category** field. 
4. In the **Settings** tab, create key-value pairs using standard Liquid. Set the appropriate user attributes you want the message to show. 
5. In the `.plist` of your Notification Content Extension Target, set the `UNNotificationExtensionCategory` attribute to your custom iOS category. The value given here must match what is set in the Braze dashboard under **iOS Notification Category**. 

As seen in the example, you may also include an image in your push notification. To do this, you must integrate [rich notifications](https://www.braze.com/docs/developer_guide/push_notifications/rich?sdktab=swift), set the notification style in your campaign to Rich Notification, and include a rich push image.

![A push message with three sets of key-value pairs. 1. "Braze_id" set as a Liquid call to retrieve Braze ID. 2. "cert_title" set as "Braze Marketer Certification". 3. "Cert_description" set as "Certified Braze marketers drive...".](https://www.braze.com/docs/assets/img/push_implementation_guide/push9.png?4f1d1fc129e7f564d006e649dc0ef582)

### Handling button actions

Each action button is uniquely identified. The code checks if your response identifier is equal to the `actionIdentifier`, and if so, knows that the user clicked the action button.

**Handling Push Notification Action Button Responses**<br>



``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```


```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```



### Dismissing pushes

Push notifications can be automatically dismissed from an action button press. There are three pre-built push dismissal options that we recommend:

1. `completion(.dismiss)` - Dismisses the notification
2. `completion(.doNotDismiss)` - Notification stays open
3. `completion(.dismissAndForward)` - Push dismisses and the user gets forwarded into the application



