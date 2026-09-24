# Kochava

> [Kochava](https://www.kochava.com/) offers mobile attribution and analytics to help you harness your data for growth. The Kochava Audience Platform enables you to plan, target, activate, measure, and optimize your app campaigns.

_This integration is maintained by Kochava._

## About the integration

The Braze and Kochava integration helps power a more holistic understanding of your campaigns by sending attribution data to Braze to better understand what campaigns are driving installs, in-app activity, and more.

## Prerequisites

| Requirement | Description |
|---|---|
| Kochava account | A Kochava account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| Kochava SDK | In addition to the required Braze SDK, you must install the [Kochava SDK](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Map user IDs

Depending on your platform, your app may need to pass the Braze device identifier (`device_id`) to Kochava so that when Kochava sends attribution data back to Braze, Braze can match that data to the correct user profile. See the Android and iOS sections for when mapping is required.

#### Android

The Braze SDK generates a device identifier (`device_id`). Your app should retrieve this identifier and pass it to Kochava's `IdentityLink` method. This allows Kochava to include the `device_id` in the attribution data it sends back to Braze, so Braze can match attribution events to the correct user profile.

Retrieve the Braze `device_id` with the following method:

```java
Braze.getInstance(context).getDeviceId();
```

#### iOS

**Important:**


Prior to February 2023, our Kochava attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. Braze customers using Objective-C don't need to fetch the Braze `device_id` and send it to Kochava upon install, because there is no disruption of service.



Starting in Swift SDK v5.7.0, you can configure whether Braze uses IDFV or a randomly generated UUID as the device ID. In Swift SDK v7.0.0+, `useUUIDAsDeviceId` defaults to `true`, so new users get a UUID `device_id` unless you set this field to `false`. For more information, see [Collecting IDFV](https://www.braze.com/docs/developer_guide/analytics/managing_data_collection/?sdktab=swift).

- To keep IDFV as the mutual identifier with Kochava, set `useUUIDAsDeviceId` to `false`.
- If `useUUIDAsDeviceId` is `true` (the default in v7.0.0+), pass the Braze `device_id` to Kochava upon app install so Braze can match iOS attributions.

Use one of the following non-blocking APIs to retrieve the Braze `device_id`, then pass that value into Kochava per Kochava's [iOS SDK](https://support.kochava.com/sdk-integration/ios-sdk-integration/) instructions. For additional help, contact Kochava support.

##### Completion handler
```swift
AppDelegate.braze?.getDeviceId { deviceId in
  // Pass `deviceId` to Kochava
}
```
##### Swift concurrency
```swift
let deviceId = await AppDelegate.braze?.getDeviceId()
```

### Step 2: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Kochava**. 

Here, you can find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Kochava's dashboard.<br><br>![This image shows the "Data Import for Install Attribution" box found in the Kochava technology page. In this box, you are shown the data import key and the REST endpoint.](https://www.braze.com/docs/assets/img/attribution/kochava.png?114afae6905e00785adb4acb0c51d6c5){: style="max-width:90%;"}

### Step 3: Set up a postback from Kochava

[Add a postback](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback) in your Kochava dashboard. You're prompted for the data import key and REST endpoint that you found in the Braze dashboard.

### Step 4: Confirm the integration

After Braze receives attribution data from Kochava, the status connection indicator on the Kochava technology partners page in Braze changes from "Not Connected" to "Connected on" followed by a timestamp of the last successful request.

This status changes only after Braze receives data about an attributed install. Organic installs don't update the connection status.

## Facebook and X (formerly Twitter) attribution data

Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties and, therefore, our partners cannot send that data to Braze.

## Kochava click tracking URLs in Braze (optional)

Click tracking links in your Braze campaigns let you see which campaigns are driving app installs and re-engagement. As a result, you can measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Kochava click tracking links, visit their [documentation](https://support.kochava.com/reference-information/attribution-overview/). You can insert the Kochava click tracking links into your Braze campaigns directly. Kochava then uses their [probabilistic attribution methodologies](https://www.kochava.com/getting-prepared-for-ios-14/) to attribute the user that has clicked on the link. We recommend appending your Kochava tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This deterministically attributes the user that has clicked on the link.



For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id). The GAID is also collected natively through the Kochava SDK integration. You can include the GAID in your Kochava click tracking links by using the following Liquid logic:

```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```




For iOS, append the Braze device identifier to improve deterministic attribution. In Liquid, `most_recently_used_device.${id}` is the Braze device ID, which may be the IDFV or a UUID depending on your Swift SDK `useUUIDAsDeviceId` setting. Kochava's click-tracking URLs commonly use an `idfv` query parameter for this value:


```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```




**Note:**


**This recommendation is purely optional**<br>
If you currently don't use any device identifiers—such as the Braze device ID or GAID—in your click tracking links, or don't plan to in the future, Kochava can still attribute these clicks through their probabilistic modeling.




