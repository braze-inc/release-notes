# Manage data collection

> Learn how to manage data collection for the Braze SDK, so you can comply with any data-privacy regulations as needed.



## Disabling data tracking

**Note:**


This guide uses code samples from the Braze Web SDK 4.0.0+. To upgrade to the latest Web SDK version, see [SDK Upgrade Guide](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).






To disable data-tracking activity on the Web SDK, use the method [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). This will sync any data logged before `disableSDK()` was called, and will cause all subsequent calls to the Braze Web SDK for this page and future page loads to be ignored.



Use the **Disable Tracking** or **Resume Tracking** tag type to disable or re-enable web tracking, respectively. These two options call [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) and [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).



### Best practices

To provide users with the option to stop tracking, we recommend building a simple page with two links or buttons: one that calls `disableSDK()` when clicked, and another that calls `enableSDK()` to allow users to opt back in. You can use these controls to start or stop tracking via other data sub-processors as well.

**Note:**


The Braze SDK does not need to be initialized to call `disableSDK()`, allowing you to disable tracking for fully anonymous users. Conversely,`enableSDK()` does not initialize the Braze SDK so you must also call `initialize()` afterward to enable tracking.



## Resuming data tracking

To resume data collection, you can use the [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) method.




## Google Play privacy questionnaire {#privacy-questionnaire}

Starting in April 2022, Android developers must complete Google Play's [Data safety form](https://support.google.com/googleplay/android-developer/answer/10787469) to disclose privacy and security practices. This guide provides instructions on how to fill out this new form with information on how Braze handles your app data. 

As the app developer, you are in control of what data you send to Braze. Data received by Braze is processed according to your instructions. This is what Google classifies as a [service provider](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform). 

**Important:**


This article provides information related to the data the Braze SDK processes as related to the Google safety section questionnaire. This article is not providing legal advice, so we recommend consulting with your legal team before submitting any information to Google.



### Questions

|Questions|Answers for Braze SDK|
|---|---|
|Does your app collect or share any of the required user data types?|Yes, the Braze Android SDK collects data as configured by the app developer. |
|Is all of the user data collected by your app encrypted in transit?|Yes.|
|Do you provide a way for users to request that their data be deleted?|Yes.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Questions" }

For more information about handling user requests for their data and deletion, see [Braze Data Retention Information](https://www.braze.com/docs/api/data_retention/).

### Data collection

The data collected by Braze is determined by your specific integration and the user data you choose to collect. To learn more about what data Braze collects by default and how to disable certain attributes, see our [SDK data collection options](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration).

<table aria-label="Data collection" id="datatypes">
    <thead>
        <tr>
            <th width="25%">Category</th>
            <th width="25%">Data type</th>
            <th width="50%">Braze Usage</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Location</td>
            <td>Approximate location</td>
            <td rowspan="15">Not collected by default.</td>
        </tr>
        <tr>
            <td>Precise location</td>
        </tr>
        <tr>
            <td rowspan="9">Personal Info</td>
            <td>Name</td>
        </tr>
        <tr>
            <td>Email address</td>
        </tr>
        <tr>
            <td>User IDs</td>
        </tr>
        <tr>
            <td>Address</td>
        </tr>
        <tr>
            <td>Phone number</td>
        </tr>
        <tr>
            <td>Race and ethnicity</td>
        </tr>
        <tr>
            <td>Political or religious beliefs</td>
        </tr>
        <tr>
            <td>Sexual orientation</td>
        </tr>
        <tr>
            <td>Other info</td>
        </tr>
        <tr>
            <td rowspan="4">Financial info</td>
            <td>User payment info</td>
        </tr>
        <tr>
            <td>Purchase history</td>
        </tr>
        <tr>
            <td>Credit score</td>
        </tr>
        <tr>
            <td>Other financial info</td>      
        </tr>
        <tr>
            <td rowspan="2">Health and fitness</td>
            <td>Health info</td>
            <td rowspan="2">Not collected by default.</td>
        </tr>
        <tr>
            <td>Fitness info</td>     
        </tr>
        <tr>
            <td rowspan="3">Messages</td>
            <td>Emails</td>
            <td rowspan="2">Not collected by default.</td>
        </tr>
        <tr>
            <td>SMS or MMS</td>          
        </tr>
        <tr>
            <td>Other in-app messages</td>
            <td>If you send In-app messages or push notifications through Braze, we collect information on when users have opened or read these messages.</td>
        </tr>
        <tr>
            <td rowspan="2">Photos and videos</td>
            <td>Photos</td>
            <td rowspan="8">Not collected.</td>
        </tr>
        <tr>
            <td>Videos</td>
        </tr>
        <tr>
            <td rowspan="3">Audio files</td>
            <td>Voice or sound recordings</td>
        </tr>        
        <tr>
            <td>Music files</td>
        </tr>
        <tr>
            <td>Other audio files</td>
        </tr>
        <tr>
            <td>Files and docs</td>
            <td>Files and docs</td>
        </tr>
        <tr>
            <td>Calendar</td>
            <td>Calendar events</td>
        </tr>
        <tr>
            <td>Contacts</td>
            <td>Contacts</td>
        </tr>
        <tr>
            <td rowspan="5">App activity</td>
            <td>App interactions</td>
            <td>Braze collects session activity data by default. All other interactions and activity is determined by your app's custom integration.</td>
        </tr>
        <tr>
            <td>In-app search history</td>
            <td>Not collected.</td>            
        </tr>
        <tr>
            <td>Installed apps</td>
            <td>Not collected.</td>            
        </tr>
        <tr>
            <td>Other user-generated content</td>
            <td rowspan="2">Not collected by default.</td>            
        </tr>
        <tr>
            <td>Other actions</td>
        </tr>
        <tr>
            <td>Web browsing</td>
            <td>Web browsing history</td>
            <td>Not collected.</td>
        </tr>
        <tr>
            <td rowspan="3">App information and performance</td>
            <td>Crash logs</td>
            <td>Braze collects crash logs for errors that occur within the SDK. This contains the user's phone model and OS level, along with a Braze specific user ID.</td>
        </tr>
        <tr>
            <td>Diagnostics</td>
            <td>Not collected.</td>            
        </tr>
        <tr>
            <td>Other app performance data</td>
            <td>Not collected.</td>
        </tr>
        <tr>
            <td>Device or other IDs</td>
            <td>Device or other IDs</td>
            <td>Braze generates a device ID to differentiate users' devices, and checks if messages are sent to the correct intended device.</td>
        </tr>
    </tbody>
</table>

To learn more about other device data that Braze collects which may fall outside the scope of Google Play's data safety guidelines, see our [Android storage overview](https://www.braze.com/docs/developer_guide/storage/?tab=android) and our [SDK data collection options](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration).

## Disabling data tracking

To disable data-tracking activity on the Android SDK, use the method [`disableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html). This will cause all network connections to be canceled, meaning the Braze SDK will no longer pass any data to Braze servers.

## Wiping previously-stored data

You can use the method [`wipeData()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/wipe-data.html) to fully clear all client-side data stored on the device.

## Resuming data tracking

To resume data collection, you can use the [`enableSDK()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-sdk.html) method. Keep in mind, this will not restore any previously wiped data.




## Apple's privacy manifest {#privacy-manifest}

### What is tracking data?

Apple defines "tracking data" as data collected in your app about an end-user or device that's linked to third-party data (such as targeted advertising), or a data broker. For a complete definition with examples, see [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

By default, the Braze SDK does not collect tracking data. However, depending on your Braze SDK configuration, you may be required to list Braze-specific data in your app's privacy manifest.

### What is a privacy manifest?

A privacy manifest is a file in your Xcode project that describes the reason your app and third-party SDKs collect data, along with their data-collection methods. Each of your third-party SDKs that track data require its own privacy manifest. When you [create your app's privacy report](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), these privacy manifest files are automatically aggregated into a single report.

### API tracking-data domains

Starting with iOS 17.2, Apple will block all declared tracking endpoints in your app until the end-user accepts an [Ad Tracking Transparency (ATT) prompt](https://support.apple.com/en-us/HT212025). Braze provides tracking endpoints to route your tracking data, while still allowing you to route non-tracking first-party data to the original endpoint. 

## Declaring Braze tracking data

**Tip:**


For a full walkthrough, see the [Privacy Tracking Data tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).



### Prerequisites

The following Braze SDK version is required to implement this feature:

<div id='sdk-versions'><a href='/docs/developer_guide/platforms/swift/changelog/#900' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 9.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

### Step 1: Review your current policies

Review your Braze SDK's current data-collection policies with your legal team to determine whether your app collects tracking data [as defined by Apple](#what-is-tracking-data). If you're not collecting any tracking data, you don't need to customize your privacy manifest for the Braze SDK at this time. For more information about the Braze SDK's data-collection policies, see [SDK data collection](https://www.braze.com/docs/user_guide/data/user_data_collection/sdk_data_collection/).

**Important:**


If any of your non-Braze SDKs collect tracking data, you'll need to review those policies separately.



### Step 2: Create a privacy manifest

First, check if you already have a privacy manifest by searching for a `PrivacyInfo.xcprivacy` file in your Xcode project. If you already have this file, you can continue to the next step. Otherwise, see [Apple: Create a privacy manifest](sdk-tracking.iad-01.braze.com).

### Step 3: Add your endpoint to the privacy manifest

In your Xcode project, open your app's `PrivacyInfo.xcprivacy` file, then right-click the table and check **Raw Keys and Values**.



![An Xcode project with the context menu open and "Raw Keys and Values" highlighted.](https://www.braze.com/docs/assets/img/apple/privacy_manifest/check_raw_keys_and_values.png?670eead9e29da0d52e7ae1a6d6205194)

Under **App Privacy Configuration**, choose **NSPrivacyTracking** and set its value to **YES**.

![The 'PrivacyInfo.xcprivacy' file open with "NSPrivacyTracking" set to "YES".](https://www.braze.com/docs/assets/img/apple/privacy_manifest/add_nsprivacytracking.png?02325a36076d8716d2d1e340f7a8ecd7)

Under **App Privacy Configuration**, choose **NSPrivacyTrackingDomains**. In the domains array, add a new element and set its value to the endpoint you [previously added to your `AppDelegate`](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate) prefixed with `sdk-tracking`.

![The 'PrivacyInfo.xcprivacy' file open with a Braze tracking endpoint listed under "NSPrivacyTrackingDomains".](https://www.braze.com/docs/assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png?eb07fc3447c9380e0a20b912f9b22630)

### Step 4: Declare your tracking data

Next, open `AppDelegate.swift` then list each [tracking property](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) you want to declare by creating a static or dynamic tracking list. Keep in mind, Apple will block these properties until the end-user accepts their ATT prompt, so only list the properties you and your legal team consider tracking. For example:



In the following example, `dateOfBirth`, `customEvent`, and `customAttribute` are declared as tracking data within a static list. 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```



In the following example, the tracking list is automatically updated after the end-user accepts the ATT prompt.

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```



### Step 5: Prevent infinite retry loops

To prevent the SDK from entering an infinite retry loop, use the `set(adTrackingEnabled: enableAdTracking)` method to handle ATT permissions. The `adTrackingEnabled` property in your method should be handled similar to the following:

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Disabling data tracking

To disable data-tracking activity on the Swift SDK, set the [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) property to `false` on your Braze instance. When `enabled` is set to `false`, the Braze SDK ignores any calls to the public API. The SDK also cancels all in-flight actions, such as network requests, event processing, etc. 

## Wiping previously-stored data

You can use the [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) method to fully clear locally-stored SDK data on a user's device.

For Braze Swift versions 7.0.0 and later, the SDK and the `wipeData()` method randomly generates a UUID for their device ID. However, if your `useUUIDAsDeviceId` is set to `false` _or_ you're using Swift SDK version 5.7.0 or earlier, you'll also need to make a post request to [`/users/delete`](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/) since your Identifier for Vendors (IDFV) will automatically be used as that user's device ID.

If you use manual push integration, and your app calls `wipeData()` and later re-enables the SDK in the same app run, call `registerForRemoteNotifications()` again so Braze can receive a refreshed device token. For more information, see [setting up push notifications](https://www.braze.com/docs/developer_guide/push_notifications/?sdktab=swift).

## Resuming data tracking

To resume data collection, set [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) to `true`. Keep in mind, this will not restore any previously wiped data.

## IDFV collection

In previous versions of the Braze iOS SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user's device ID. Beginning in Swift SDK `v5.7.0`, the IDFV field was optionally disabled, and instead, Braze would set a random UUID as the device ID. Starting in Swift SDK `v7.0.0`, the IDFV field will not be collected by default, and a UUID will be set as the device ID instead.

The `useUUIDAsDeviceId` feature configures the [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) to set the device ID as a UUID. Traditionally, the iOS SDK would assign the device ID equal to the Apple-generated IDFV value. With this feature enabled by default on your iOS app, all new users created via the SDK would be assigned a device ID equal to a UUID.

If you still want to collect IDFV separately, you can use [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

### Considerations

#### SDK Version

In Swift SDK `v7.0.0+`, when `useUUIDAsDeviceId` is enabled (default), all new users created will be assigned a random device ID. All previously existing users will maintain their same device ID value, which may have been IDFV.

When this feature is not enabled, devices will continue to be assigned IDFV upon creation.

#### Downstream 

**Technology partners**: When this feature is enabled, any technology partners that derive the IDFV value from the Braze device ID will no longer have access to this data. If the IDFV value derived from the device is needed for your partner integration, we recommend that you set this feature to `false`.

**Currents**: `useUUIDAsDeviceId` set to true means the device ID sent in Currents will no longer equal the IDFV value.

### Frequently asked questions

#### Will this change impact my existing users in Braze?

No. When enabled, this feature will not overwrite any user data in Braze. New UUID device IDs will only be created for new devices or when `wipedata()` is called.

#### Can I turn this feature off after turning it on?

Yes, this feature can be toggled on and off at your discretion. Previously stored device IDs will never be overwritten.

#### Can I still capture the IDFV value via Braze elsewhere?

Yes, you can still optionally collect the IDFV via the Swift SDK (collection is disabled by default). 




## Prerequisites

Before you can use this feature, you'll need to [integrate the React Native Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native).

## Disabling data tracking

To disable data collection, use the `disableSDK` method. After calling this method, the Braze SDK stops sending data to Braze servers.

```javascript
Braze.disableSDK();
```

## Resuming data tracking

To resume data collection after disabling it, use the `enableSDK` method.

```javascript
Braze.enableSDK();
```

## Wiping data

To delete all locally stored Braze SDK data on the device, use the `wipeData` method. After calling this method, the SDK is disabled and must be re-enabled with `enableSDK`.

```javascript
Braze.wipeData();
```

## Flushing data

To request an immediate flush of any pending data to Braze servers, use `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Setting ad-tracking enabled

To inform Braze whether ad-tracking is enabled for this device, use the `setAdTrackingEnabled` method. The SDK does not automatically collect this data.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

The second parameter is the Google Advertising ID and is only used on Android.

## Updating the tracking property allow list (iOS only)

To update the list of data types declared for tracking, use `updateTrackingPropertyAllowList`. This is a no-op on Android.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

For more information, refer to [Privacy Manifest](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/).




