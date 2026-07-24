# Track uninstalls

> Learn how to set up uninstall tracking through the Braze SDK. For general information, see [User Guide: Uninstall tracking](https://www.braze.com/docs/user_guide/analytics/tracking/uninstall_tracking).



## Setting up uninstall tracking

### Step 1: Set up FCM

The Android Braze SDK uses Firebase Cloud Messaging (FCM) to send silent push notifications, which are used to collect uninstall tracking analytics. If you haven't already, [set up](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=android#android_setting-up-push-notifications) or [migrate to](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=android) the Firebase Cloud Messaging API for push notifications.

### Step 2: Manually detect uninstall tracking (optional)

By default, the Android Braze SDK automatically detects and ignores silent push notifications related to uninstall tracking. However, you choose to manually detect uninstall tracking using the [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) method.

**Important:**


Because silent notifications for uninstall tracking are not forwarded to any Braze push callbacks, you can only use this method before you pass a push notification to Braze.



### Step 3: Remove automatic server pings

A silent push notification wakes your app and instantiates the `Application` component if the app isn't already running. So, if you have a custom [`Application`](https://developer.android.com/reference/android/app/Application) subclass, remove any logic that automatically pings your servers during your [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) lifecycle method.

### Step 4: Enable uninstall tracking

Finally, enable uninstall tracking in Braze. For a full walkthrough, see [Turning on uninstall tracking](https://www.braze.com/docs/user_guide/analytics/tracking/uninstall_tracking/#turning-on-uninstall-tracking).

**Important:**


Tracking uninstalls can be imprecise. The metrics you see on Braze may be delayed or inaccurate.






## Setting up uninstall tracking

### Step 1: Enable background push

In your Xcode project, go to **Capabilities** and ensure you have **Background Modes** enabled. For more information, see [silent push notification](https://www.braze.com/docs/developer_guide/push_notifications/silent/?sdktab=swift).

### Step 2: Ignore internal push notifications

The Swift Braze SDK uses background push notifications to collect uninstall tracking analytics. Make sure your app [ignores internal push notifications](https://www.braze.com/docs/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications) so it doesn't take unwanted actions when these are sent.

### Step 3: Send a test push (optional)

Next, send yourself a test push notification from the Braze dashboard (don't worry&#8212;it doesn't update your user profile).

1. Go to **Messaging** > **Campaigns** and create a push notification campaign using the relevant platform.
2. Go to **Settings** > **App Settings** and add the `appboy_uninstall_tracking` key with relevant `true` value, then check **Add Content-Available Flag**.
3. Use the **Preview** page to send yourself a test uninstall tracking push.
4. Check that your app does not make any unwanted automatic actions when it receives a push notification.

**Note:**


A badge number is sent along with the test push notification&#8212;however a real uninstall tracking push doesn't send any badge numbers.



### Step 4: Enable uninstall tracking

Finally, enable uninstall tracking in Braze. For a full walkthrough, see [Turning on uninstall tracking](https://www.braze.com/docs/user_guide/analytics/tracking/uninstall_tracking/#turning-on-uninstall-tracking).

**Important:**


Tracking uninstalls can be imprecise. The metrics you see on Braze may be delayed or inaccurate.





