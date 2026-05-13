# AppsFlyer

<iframe width="560" height="315" src="https://www.youtube.com/embed/" title="Video" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen class="media_embed "></iframe>



> [AppsFlyer](https://www.appsflyer.com/) is a mobile marketing analytics and attribution platform that helps you analyze and optimize your apps through marketing analytics, mobile attribution, and deep linking.

The Braze and AppsFlyer integration allows you to better understand how to optimize and build more holistic campaigns by leveraging mobile install attribution data from AppsFlyer. 

You can also pass your AppsFlyer audiences (cohorts) directly to Braze with the [AppsFlyer Audiences](https://www.braze.com/docs/partners/data_and_analytics/cohort_import/appsflyer_audiences/) integration, allowing you to create powerful customer engagement campaigns targeted toward just the right users at just the right time. 

## Prerequisites

| Requirement | Description |
|---|---|
| AppsFlyer account | An AppsFlyer account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| AppsFlyer SDK | In addition to the required Braze SDK, you must install the [AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started).
| Email domain setup complete | You must have completed the [IP and domain setup step](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains/) of setting up your email during Braze onboarding. |
| SSL certificate | Your [SSL certificate](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) must be configured. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Map device ID



If you have an Android app, you must pass a unique Braze device ID to AppsFlyer. 

Ensure the following lines of code are inserted at the correct place—after the Braze SDK is launched and before the initialization code for the AppsFlyer SDK. See the AppsFlyer [Android SDK integration guide](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) for more information.

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```



**Important:**


Prior to February 2023, our AppsFlyer attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze `device_id` and send it to AppsFlyer upon install because there is no disruption of service. 



For those using the Swift SDK v5.7.0+, if you want to continue using IDFV as the mutual identifier, you must confirm that the `useUUIDAsDeviceId` field is set to `false` to avoid a disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to AppsFlyer upon app install in order for Braze to appropriately match iOS attributions.




```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```



```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```





To map the device ID in Unity, use the following:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```



### Step 2: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **AppsFlyer**. 

Here, you find the REST endpoint and generate your Braze data import key. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in AppsFlyer's dashboard.<br><br>![The "Data Import for Install Attribution" box available on the AppsFlyer Technology page. Included in this box is the data import key and the REST endpoint.](https://www.braze.com/docs/assets/img/attribution/appsflyer.png?2f1e0c52e6ef93f2684593d0dde70c53){: style="max-width:70%;"}

### Step 3: Configure Braze in AppsFlyer's dashboard

1. In AppsFlyer, navigate to the **Integrated Partners** page on the left bar. Next, search for **Braze** and select the Braze logo to open a configuration window.
2. Within the **Integration** tab, switch on **Activate Partner**.
3. Provide the data import key and REST endpoint that you found in the Braze dashboard. 
4. Toggle **Advanced Privacy** off and save your configuration.

Additional information on these instructions is available in [AppsFlyer's documentation](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Step 4: Confirm the integration

After Braze receives attribution data from AppsFlyer, the status connection indicator on the AppsFlyer technology partners page in Braze changes from "Not Connected" to "Connected" and includes a timestamp of the last successful request.

This status changes only after Braze receives data about an attributed install. Braze ignores organic installs (excludes them from the AppsFlyer postback) and does not count them when determining if the connection is successful.

### Step 5: Viewing user attribution data

#### Available data fields

If your integration was successful, Braze maps all non-organic install data to segment filters.

| AppsFlyer data field | Braze segment filter |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Available data fields" }

You can segment your user base by attribution data in the Braze dashboard using the Install Attribution filters.

![Four available filters. The first is "Install Attribution Source is network_val_0". The second is "Install Attribution Source is campaign_val_0". The third is "Install Attribution Source is adgroup_val_0". The fourth is "Install Attribution Source is creative_val_0". Beside the listed filters, you can see how these attribution sources will be added to the user profile. In the "Install Attribution" box on a user's information page, Install Source is listed as network_val_0, campaign is listed as campaign_val_0, etc.](https://www.braze.com/docs/assets/img/braze_attribution.png?9cdbad34ced6d33136fd667bc65019b9)

Additionally, attribution data for a particular user is available on each user's profile in the Braze dashboard.

**Note:**


Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties, and, therefore, our partners cannot send that data to Braze.



## Integrate AppsFlyer with Braze for deep linking

Deep links&#8212;links that direct users toward a specific page or place within an app or website&#8212;are used to create a tailored user experience. 

While widely used, issues can arise when using emailed deep links with click tracking#8212another important feature used in collecting user data. These issues are due to Email Service Providers (ESPs) wrapping deep links in a click-recording domain, breaking the original link. As such, supporting deep links requires additional setup.

AppsFlyer provides a [service](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer) that avoids these issues, enabling AppsFlyer to serve as an intermediary between the ESP server and your domain name.  Its role as a proxy enables the provision of association files (AASA/asset links), which facilitates deep linking. 

## Step 1 - Create a Click Tracking Domain 

Following the initial elements of [Braze’s Email set-up guidance](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate), create an email sending domain and a click tracking domain. For support, you can raise a ticket via the Braze Dashboard to initiate setup for the new CTD with the Braze Email team.

![Braze UI showing the “Get Help” button, found under the “Support” button on the top right corner](https://www.braze.com/docs/assets/img/attribution/appsflyer/1.png?9f8b32829abc0d7d8880d47683799dfa)

Creating a new CTD is mandatory, even if you already use an existing one. This ensures that there is no impact on the traffic of current live email campaigns. 

**Important:**

 
AppsFlyers creates the SSL certificate. At this stage, email links are likely not secured, meaning the URL prefix is HTTP instead of HTTPS. This is resolved in later steps.	



## Step 2 - Create a OneLink Template in AppsFlyer
Create a [OneLink template](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) and configure Universal Links/App Links under "When app is installed". This template is used later to create OneLink links for your email campaigns.

**Note:**

 If you already have an existing OneLink template configured that enables Universal Links/App Links, you can use it.



## Step 3 - Set up your Braze Integration in Appsflyer
Now it's time to set your Braze integration in AppsFlyer. This step and the following one ("Configure your app") can be set up at the same time.
To set your Braze integration in AppsFlyer:

### 1. In AppsFlyer, from the side menu, select Engage > ESP integration.
![Appsflyer UI showing the “ESP Integration” button, found in the left hand menu](https://www.braze.com/docs/assets/img/attribution/appsflyer/2.png?fec4b42d98499e8203e0a489e38d2e67)

 
### 2. Select Braze.
![Appsflyer UI showing the list of ESP Integrations, including Braze.](https://www.braze.com/docs/assets/img/attribution/appsflyer/3.png?f4237f9a6567abe24db1cfbdba664a9a)

 
### 3. Select the OneLink template you want to use for email campaigns, then click Next.
![Appsflyer UI showing the drop down allowing users to select their template.](https://www.braze.com/docs/assets/img/attribution/appsflyer/4.png?fd881a98f9e9dd75b0e0d7ee976f3a02)

 
### 4. Enter your click tracking domain and “Braze endpoint” value, which was provided with the new CTD created in step 1, then click Validate connection.

This validates that the click-tracking domain points to the endpoint you entered.

![Appsflyer UI highlighting where customers should add their click tracking domain and associated details.](https://www.braze.com/docs/assets/img/attribution/appsflyer/5.png?79835af261988caf34c570c38857d9d8)

By “Braze Endpoint”, AppsFlyer is asking for the details provided by Braze in Step 1 of this guide, specifically the new CTD. 

Then click **Validate connection**, which validates that the click-tracking domain points to the endpoint you entered.
When done, click **Next**.

### 5. Route link traffic to AppsFlyer:

#### a. Copy and send the customized pre-fabricated instructions in AppsFlyer to your IT or domain administrator. 

Your administrator must reroute your email campaign traffic from the ESP servers to the AppsFlyer servers by updating your DNS CNAME records with the new domain that AppsFlyer provided.

As a result, every time a link is clicked, the click is redirected to AppsFlyer, which in turn redirects it to the ESP endpoint.

![Diagram illustrating how click data passed from your domain, to AppsFlyer, to your esp endpoint](https://www.braze.com/docs/assets/img/attribution/appsflyer/6.png?f03253203991a9e8cbb3f17b0f5821b4)

#### b. After copying and sending the instructions, click Done.
Your Braze integration has been created.

**Important:**

 
Your Braze integration status is pending and starts working only after the CNAME record is mapped. It can take up to 24 hours after mapping for a new integration to start working and become active.



## Step 4: Configure your App (Developer-Task)
Appsflyer [offers guidance](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task) on correct app configuration, which should be followed by your web or app teams in order to support universal linking. 

## Step 5: Confirm SSL Click-tracking is enabled with Braze

At this stage, after you share and validate the CTD details in Appsflyer, we recommend performing a test send to confirm if your Onelink sending domain has an SSL certificate. This is in line with our [Email Setup](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate) guide.

You can perform quality assurance and troubleshooting by sending a deep link using OneLink. See the [AppsFlyer documentation](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) for details on using OneLink.

If CTD links are identified as HTTP, contact Braze's Email Ops team to enable SSL click-tracking. This ensures that all HTTP links are automatically converted to HTTPS.
You can use the following sample message text when contacting your Customer Success Manager, or by raising a ticket in the Braze Dashboard again, like in step 1: 

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS. 
```

### AppsFlyer click tracking URLs in Braze (optional)

You can use AppsFlyer's [OneLink attribution links](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) in Braze campaigns across push, email, and more. This allows you to send back install or re-engagement attribution data from your Braze campaigns into AppsFlyer. As a result, you can measure your marketing efforts more effectively and make data-driven decisions.

You can simply create your OneLink tracking URL in AppsFlyer and directly insert it into your Braze campaigns. AppsFlyer then uses their [probabilistic attribution methodologies](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) to attribute the user that has clicked on the link. We recommend appending your AppsFlyer tracking links with a device identifier to improve the accuracy of attributions from your Braze campaigns. This deterministically attributes the user that has clicked on the link.



For Android, Braze allows customers to opt in to [Google Advertising ID collection (GAID)](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The AppsFlyer SDK integration also collects the GAID. You can include the GAID in your AppsFlyer click-tracking links by using the following Liquid logic:

```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```




For iOS, both Braze and AppsFlyer automatically collect the IDFV natively through our SDK integrations. You can use the IDFC as the device identifier. You can include the IDFV in your AppsFlyer click-tracking links by using the following Liquid logic:


```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```



