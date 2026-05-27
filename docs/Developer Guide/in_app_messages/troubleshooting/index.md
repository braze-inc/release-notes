# Troubleshooting

> Need help troubleshooting in-app messages for the Braze SDK? Start here!



## Basic Checks

### My in-app message wasn't shown for one user

1. Was the user in the segment at session start, when the SDK requests new in-app messages?
2. Was the user eligible or re-eligible to receive the in-app message per campaign targeting rules?
3. Was the user affected by a frequency cap?
4. Was the user in a control group? Check whether your campaign is configured is configured for AB Testing.
5. Was a different, higher priority in-app message displayed in place of the expected message?
6. Was my device in the correct orientation specified by the campaign?
7. Was my message suppressed by the default 30-second minimum time interval between triggers, enforced by the SDK?

### My in-app message wasn't shown to all users on this platform

1. Is your campaign configured to target either Mobile Apps or Web Browsers as appropriate? As an example, if your campaign only targets Web Browsers, it will not send to Android devices.
2. Did you implement a custom UI, and is it working as intended? Is there other app-side custom handling or suppression that could be interfering with display? 
3. Has this particular platform and app version ever shown in-app messages successfully?
4. Did the trigger take place locally on the device? Note that a REST call can't be used to trigger an in-app message in the SDK.

### My in-app message wasn't shown for all users

1. Was the Trigger Action set up properly in the dashboard, as well as in the app integration?
2. Was a different, higher priority in-app message displayed in place of the expected message?
3. Are you on a recent version of the SDK? Some in-app message types have SDK version requirements.
4. Have sessions been integrated properly in your integration? Are session analytics working for this app?
5. Are you using a customized components library, which may interfere with how in-app messages display?

### My in-app message took a lot of time to appear

1. If you are serving large image or video files from your CDN to an HTML based in-app message, verify that your files are optimized to be as small as possible and that your CDN is performant.
2. Verify whether you have configured a `delay` for your in-app message on the dashboard.


For more in-depth discussion of these scenarios, visit <a id="troubleshooting-in-app-advanced">the advanced troubleshooting section</a>.

## Issues with Impressions and Click Analytics



### _Impressions_ are greater than _Unique Impressions_

This is expected behavior and can happen when:

- Even if re-eligibility is turned off, users who received the campaign may have more than one device. The campaign trigger updates on the next session start, so a device won't know if another device has already triggered the campaign until the user starts a new session.
- If your in-app message has a scheduled delay for a few minutes after the trigger event occurs, users may have received the message more than once.

For more information on re-eligibility, see [Re-eligibility for campaigns and Canvas](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

### Impressions are lower than expected

1. Triggers take time to sync to the device on session start, so there can be a race condition if users log an event or purchase right after they start a session. One potential workaround could be changing the campaign to trigger off of session start, then segmenting off the intended event or purchase. Note that this would deliver the in-app message on the next session start after the event has occurred.

2. If the campaign is triggered by a session start or a custom event, you want to ensure that this event or session is happening frequently enough to trigger the message. Check this data on the [Overview](https://www.braze.com/docs/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (for session data) or [Custom Events](https://www.braze.com/docs/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting) pages:

![Custom Events page showing a graph for the number of times the custom event Added to Favorites occurred over a one month period](https://www.braze.com/docs/assets/img_archive/trouble5.png?26aef03f1c01c7a0c23330a709d2f5cc)

Other reasons include:

- Users haven't viewed the in-app message, so impressions aren't logged.
- Multiple in-app messages are intercepting each other (such as multiple high-priority messages).
- If the message is in a Canvas, users may be entering a Delay step that is longer than the session timeout before receiving the in-app message.

### Impressions are lower than they used to be

1. Ensure no one unintentionally altered the segment or campaign since launch. Our segment and campaign changelogs will give you insight into changes that have been made, who made the change, and when it happened.

![Link to view changelog on the Campaign Details page with seven changes since the user has last viewed the campaign](https://www.braze.com/docs/assets/img_archive/trouble4.png?d1b004eed1ccaf74f475397ebbae7958)

{: start="2"}
2. Ensure you didn't reuse your trigger event in a separate in-app message campaign with a higher priority.

## Advanced Troubleshooting {#troubleshooting-in-app-advanced}

Most in-app message issues can be broken down into two main categories: delivery and display. To troubleshoot why an expected in-app message did not display on your device, confirm that the <a id="troubleshooting-in-app-message-delivery">in-app message was delivered to the device</a>, then <a id="troubleshooting-in-app-message-display">troubleshoot message display</a>.

### Troubleshooting delivery {#troubleshooting-in-app-message-delivery}

The SDK requests in-app messages from Braze servers on session start. To check if in-app messages are being delivered to your device, you'll need to make sure that in-app messages are being both requested by the SDK and returned by Braze servers.

#### Check if messages are requested and returned

1. Add yourself as a [test user](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) on the dashboard.
2. Set up an in-app message campaign targeted at your user.
3. Ensure that a new session occurs in your application.
4. Use the [event user logs](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check that your device is requesting in-app messages on session start. Find the SDK Request associated with your test user's session start event.
  - If your app was meant to request triggered in-app messages, you should see `trigger` in the **Requested Responses** field under **Response Data**.
  - If your app was meant to request original in-app messages, you should see  `in_app` in the **Requested Responses** field under **Response Data**.
5. Use the [event user logs](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check if the correct in-app messages are being returned in the response data.<br>![](https://www.braze.com/docs/assets/img_archive/event_user_log_iams.png?fd8f7c0f05a549b6a529b92744f37f96)

##### Troubleshoot messages not being requested

If your in-app messages are not being requested, your app might not be tracking sessions correctly, as in-app messages are refreshed upon session start. Also, be sure that your app is actually starting a session based on your app's session timeout semantics:

![The SDK request found in the event user logs displaying a successful session start event.](https://www.braze.com/docs/assets/img_archive/event_user_log_session_start.png?972201c9c20f018bc85d97167638f04e)

##### Troubleshoot messages not being returned

If your in-app messages are not being returned, you're likely experiencing a campaign targeting issue:

1. Your segment does not contain your user.
  - Check your user's [**Engagement**](https://www.braze.com/docs/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) tab to see if the correct segment appears under **Segments**.
2. Your user has previously received the in-app message and was not re-eligible to receive it again.
  - Check the [campaign re-eligibility settings](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) under the **Delivery** step of the **Campaign Composer** and make sure the re-eligibility settings align with your testing setup.
3. Your user hit the frequency cap for the campaign.
  - Check the campaign [frequency cap settings](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) and ensure they align with your testing setup.
4. If there was a control group on the campaign, your user may have fallen into the control group.
  - You can check if this has happened by creating a segment with a received campaign variant filter, where the campaign variant is set to **Control**, and checking if your user fell into that segment.
  - When creating campaigns for integration testing purposes, make sure to opt out of adding a control group.


### Troubleshooting display {#troubleshooting-in-app-message-display}

If your app is successfully requesting and receiving in-app messages, but they are not being shown, device-side logic may be preventing display:

1. Is the trigger event firing as expected? To test for this, try configuring the message to trigger using a different action (like session start) and verify whether it displays.

3. Failed image downloads will prevent in-app messages with images from displaying. Check your device logs to ensure that image downloads are not failing. Try removing your image temporarily from your message to see if that causes it to display.


7. If your in-app message is triggered by session start and you've set an extended session timeout, this will affect how quickly you can show messages. For instance, if your session timeout is set to 300 seconds, closing and re-opening the app in less than that time will not refresh the session, so an in-app message triggered by a session start will not display.





## Basic Checks

### My in-app message wasn't shown for one user

1. Was the user in the segment at session start, when the SDK requests new in-app messages?
2. Was the user eligible or re-eligible to receive the in-app message per campaign targeting rules?
3. Was the user affected by a frequency cap?
4. Was the user in a control group? Check whether your campaign is configured is configured for AB Testing.
5. Was a different, higher priority in-app message displayed in place of the expected message?
6. Was my device in the correct orientation specified by the campaign?
7. Was my message suppressed by the default 30-second minimum time interval between triggers, enforced by the SDK?

### My in-app message wasn't shown to all users on this platform

1. Is your campaign configured to target either Mobile Apps or Web Browsers as appropriate? As an example, if your campaign only targets Web Browsers, it will not send to Android devices.
2. Did you implement a custom UI, and is it working as intended? Is there other app-side custom handling or suppression that could be interfering with display? 
3. Has this particular platform and app version ever shown in-app messages successfully?
4. Did the trigger take place locally on the device? Note that a REST call can't be used to trigger an in-app message in the SDK.

### My in-app message wasn't shown for all users

1. Was the Trigger Action set up properly in the dashboard, as well as in the app integration?
2. Was a different, higher priority in-app message displayed in place of the expected message?
3. Are you on a recent version of the SDK? Some in-app message types have SDK version requirements.
4. Have sessions been integrated properly in your integration? Are session analytics working for this app?
5. Are you using a customized components library, which may interfere with how in-app messages display?

### My in-app message took a lot of time to appear

1. If you are serving large image or video files from your CDN to an HTML based in-app message, verify that your files are optimized to be as small as possible and that your CDN is performant.
2. Verify whether you have configured a `delay` for your in-app message on the dashboard.


For more in-depth discussion of these scenarios, visit <a id="troubleshooting-in-app-advanced">the advanced troubleshooting section</a>.

## Issues with Impressions and Click Analytics



### _Impressions_ are greater than _Unique Impressions_

This is expected behavior and can happen when:

- Even if re-eligibility is turned off, users who received the campaign may have more than one device. The campaign trigger updates on the next session start, so a device won't know if another device has already triggered the campaign until the user starts a new session.
- If your in-app message has a scheduled delay for a few minutes after the trigger event occurs, users may have received the message more than once.

For more information on re-eligibility, see [Re-eligibility for campaigns and Canvas](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

### Impressions are lower than expected

1. Triggers take time to sync to the device on session start, so there can be a race condition if users log an event or purchase right after they start a session. One potential workaround could be changing the campaign to trigger off of session start, then segmenting off the intended event or purchase. Note that this would deliver the in-app message on the next session start after the event has occurred.

2. If the campaign is triggered by a session start or a custom event, you want to ensure that this event or session is happening frequently enough to trigger the message. Check this data on the [Overview](https://www.braze.com/docs/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (for session data) or [Custom Events](https://www.braze.com/docs/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting) pages:

![Custom Events page showing a graph for the number of times the custom event Added to Favorites occurred over a one month period](https://www.braze.com/docs/assets/img_archive/trouble5.png?26aef03f1c01c7a0c23330a709d2f5cc)

Other reasons include:

- Users haven't viewed the in-app message, so impressions aren't logged.
- Multiple in-app messages are intercepting each other (such as multiple high-priority messages).
- If the message is in a Canvas, users may be entering a Delay step that is longer than the session timeout before receiving the in-app message.

### Impressions are lower than they used to be

1. Ensure no one unintentionally altered the segment or campaign since launch. Our segment and campaign changelogs will give you insight into changes that have been made, who made the change, and when it happened.

![Link to view changelog on the Campaign Details page with seven changes since the user has last viewed the campaign](https://www.braze.com/docs/assets/img_archive/trouble4.png?d1b004eed1ccaf74f475397ebbae7958)

{: start="2"}
2. Ensure you didn't reuse your trigger event in a separate in-app message campaign with a higher priority.

## Advanced Troubleshooting {#troubleshooting-in-app-advanced}

Most in-app message issues can be broken down into two main categories: delivery and display. To troubleshoot why an expected in-app message did not display on your device, confirm that the <a id="troubleshooting-in-app-message-delivery">in-app message was delivered to the device</a>, then <a id="troubleshooting-in-app-message-display">troubleshoot message display</a>.

### Troubleshooting delivery {#troubleshooting-in-app-message-delivery}

The SDK requests in-app messages from Braze servers on session start. To check if in-app messages are being delivered to your device, you'll need to make sure that in-app messages are being both requested by the SDK and returned by Braze servers.

#### Check if messages are requested and returned

1. Add yourself as a [test user](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) on the dashboard.
2. Set up an in-app message campaign targeted at your user.
3. Ensure that a new session occurs in your application.
4. Use the [event user logs](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check that your device is requesting in-app messages on session start. Find the SDK Request associated with your test user's session start event.
  - If your app was meant to request triggered in-app messages, you should see `trigger` in the **Requested Responses** field under **Response Data**.
  - If your app was meant to request original in-app messages, you should see  `in_app` in the **Requested Responses** field under **Response Data**.
5. Use the [event user logs](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check if the correct in-app messages are being returned in the response data.<br>![](https://www.braze.com/docs/assets/img_archive/event_user_log_iams.png?fd8f7c0f05a549b6a529b92744f37f96)

##### Troubleshoot messages not being requested

If your in-app messages are not being requested, your app might not be tracking sessions correctly, as in-app messages are refreshed upon session start. Also, be sure that your app is actually starting a session based on your app's session timeout semantics:

![The SDK request found in the event user logs displaying a successful session start event.](https://www.braze.com/docs/assets/img_archive/event_user_log_session_start.png?972201c9c20f018bc85d97167638f04e)

##### Troubleshoot messages not being returned

If your in-app messages are not being returned, you're likely experiencing a campaign targeting issue:

1. Your segment does not contain your user.
  - Check your user's [**Engagement**](https://www.braze.com/docs/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) tab to see if the correct segment appears under **Segments**.
2. Your user has previously received the in-app message and was not re-eligible to receive it again.
  - Check the [campaign re-eligibility settings](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) under the **Delivery** step of the **Campaign Composer** and make sure the re-eligibility settings align with your testing setup.
3. Your user hit the frequency cap for the campaign.
  - Check the campaign [frequency cap settings](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) and ensure they align with your testing setup.
4. If there was a control group on the campaign, your user may have fallen into the control group.
  - You can check if this has happened by creating a segment with a received campaign variant filter, where the campaign variant is set to **Control**, and checking if your user fell into that segment.
  - When creating campaigns for integration testing purposes, make sure to opt out of adding a control group.


### Troubleshooting display {#troubleshooting-in-app-message-display}

If your app is successfully requesting and receiving in-app messages, but they are not being shown, device-side logic may be preventing display:

1. Is the trigger event firing as expected? To test for this, try configuring the message to trigger using a different action (like session start) and verify whether it displays.

3. Failed image downloads will prevent in-app messages with images from displaying. Check your device logs to ensure that image downloads are not failing. Try removing your image temporarily from your message to see if that causes it to display.


7. If your in-app message is triggered by session start and you've set an extended session timeout, this will affect how quickly you can show messages. For instance, if your session timeout is set to 300 seconds, closing and re-opening the app in less than that time will not refresh the session, so an in-app message triggered by a session start will not display.





## Basic Checks

### My in-app message wasn't shown for one user

1. Was the user in the segment at session start, when the SDK requests new in-app messages?
2. Was the user eligible or re-eligible to receive the in-app message per campaign targeting rules?
3. Was the user affected by a frequency cap?
4. Was the user in a control group? Check whether your campaign is configured is configured for AB Testing.
5. Was a different, higher priority in-app message displayed in place of the expected message?
6. Was my device in the correct orientation specified by the campaign?
7. Was my message suppressed by the default 30-second minimum time interval between triggers, enforced by the SDK?

### My in-app message wasn't shown to all users on this platform

1. Is your campaign configured to target either Mobile Apps or Web Browsers as appropriate? As an example, if your campaign only targets Web Browsers, it will not send to Android devices.
2. Did you implement a custom UI, and is it working as intended? Is there other app-side custom handling or suppression that could be interfering with display? 
3. Has this particular platform and app version ever shown in-app messages successfully?
4. Did the trigger take place locally on the device? Note that a REST call can't be used to trigger an in-app message in the SDK.

### My in-app message wasn't shown for all users

1. Was the Trigger Action set up properly in the dashboard, as well as in the app integration?
2. Was a different, higher priority in-app message displayed in place of the expected message?
3. Are you on a recent version of the SDK? Some in-app message types have SDK version requirements.
4. Have sessions been integrated properly in your integration? Are session analytics working for this app?
5. Are you using a customized components library, which may interfere with how in-app messages display?

### My in-app message took a lot of time to appear

1. If you are serving large image or video files from your CDN to an HTML based in-app message, verify that your files are optimized to be as small as possible and that your CDN is performant.
2. Verify whether you have configured a `delay` for your in-app message on the dashboard.


For more in-depth discussion of these scenarios, visit <a id="troubleshooting-in-app-advanced">the advanced troubleshooting section</a>.

## Issues with Impressions and Click Analytics



### _Impressions_ are greater than _Unique Impressions_

This is expected behavior and can happen when:

- Even if re-eligibility is turned off, users who received the campaign may have more than one device. The campaign trigger updates on the next session start, so a device won't know if another device has already triggered the campaign until the user starts a new session.
- If your in-app message has a scheduled delay for a few minutes after the trigger event occurs, users may have received the message more than once.

For more information on re-eligibility, see [Re-eligibility for campaigns and Canvas](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

### Impressions are lower than expected

1. Triggers take time to sync to the device on session start, so there can be a race condition if users log an event or purchase right after they start a session. One potential workaround could be changing the campaign to trigger off of session start, then segmenting off the intended event or purchase. Note that this would deliver the in-app message on the next session start after the event has occurred.

2. If the campaign is triggered by a session start or a custom event, you want to ensure that this event or session is happening frequently enough to trigger the message. Check this data on the [Overview](https://www.braze.com/docs/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (for session data) or [Custom Events](https://www.braze.com/docs/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting) pages:

![Custom Events page showing a graph for the number of times the custom event Added to Favorites occurred over a one month period](https://www.braze.com/docs/assets/img_archive/trouble5.png?26aef03f1c01c7a0c23330a709d2f5cc)

Other reasons include:

- Users haven't viewed the in-app message, so impressions aren't logged.
- Multiple in-app messages are intercepting each other (such as multiple high-priority messages).
- If the message is in a Canvas, users may be entering a Delay step that is longer than the session timeout before receiving the in-app message.

### Impressions are lower than they used to be

1. Ensure no one unintentionally altered the segment or campaign since launch. Our segment and campaign changelogs will give you insight into changes that have been made, who made the change, and when it happened.

![Link to view changelog on the Campaign Details page with seven changes since the user has last viewed the campaign](https://www.braze.com/docs/assets/img_archive/trouble4.png?d1b004eed1ccaf74f475397ebbae7958)

{: start="2"}
2. Ensure you didn't reuse your trigger event in a separate in-app message campaign with a higher priority.

## Advanced Troubleshooting {#troubleshooting-in-app-advanced}

Most in-app message issues can be broken down into two main categories: delivery and display. To troubleshoot why an expected in-app message did not display on your device, confirm that the <a id="troubleshooting-in-app-message-delivery">in-app message was delivered to the device</a>, then <a id="troubleshooting-in-app-message-display">troubleshoot message display</a>.

### Troubleshooting delivery {#troubleshooting-in-app-message-delivery}

The SDK requests in-app messages from Braze servers on session start. To check if in-app messages are being delivered to your device, you'll need to make sure that in-app messages are being both requested by the SDK and returned by Braze servers.

#### Check if messages are requested and returned

1. Add yourself as a [test user](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) on the dashboard.
2. Set up an in-app message campaign targeted at your user.
3. Ensure that a new session occurs in your application.
4. Use the [event user logs](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check that your device is requesting in-app messages on session start. Find the SDK Request associated with your test user's session start event.
  - If your app was meant to request triggered in-app messages, you should see `trigger` in the **Requested Responses** field under **Response Data**.
  - If your app was meant to request original in-app messages, you should see  `in_app` in the **Requested Responses** field under **Response Data**.
5. Use the [event user logs](https://www.braze.com/docs/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) to check if the correct in-app messages are being returned in the response data.<br>![](https://www.braze.com/docs/assets/img_archive/event_user_log_iams.png?fd8f7c0f05a549b6a529b92744f37f96)

##### Troubleshoot messages not being requested

If your in-app messages are not being requested, your app might not be tracking sessions correctly, as in-app messages are refreshed upon session start. Also, be sure that your app is actually starting a session based on your app's session timeout semantics:

![The SDK request found in the event user logs displaying a successful session start event.](https://www.braze.com/docs/assets/img_archive/event_user_log_session_start.png?972201c9c20f018bc85d97167638f04e)

##### Troubleshoot messages not being returned

If your in-app messages are not being returned, you're likely experiencing a campaign targeting issue:

1. Your segment does not contain your user.
  - Check your user's [**Engagement**](https://www.braze.com/docs/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) tab to see if the correct segment appears under **Segments**.
2. Your user has previously received the in-app message and was not re-eligible to receive it again.
  - Check the [campaign re-eligibility settings](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) under the **Delivery** step of the **Campaign Composer** and make sure the re-eligibility settings align with your testing setup.
3. Your user hit the frequency cap for the campaign.
  - Check the campaign [frequency cap settings](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) and ensure they align with your testing setup.
4. If there was a control group on the campaign, your user may have fallen into the control group.
  - You can check if this has happened by creating a segment with a received campaign variant filter, where the campaign variant is set to **Control**, and checking if your user fell into that segment.
  - When creating campaigns for integration testing purposes, make sure to opt out of adding a control group.


### Troubleshooting display {#troubleshooting-in-app-message-display}

If your app is successfully requesting and receiving in-app messages, but they are not being shown, device-side logic may be preventing display:

1. Is the trigger event firing as expected? To test for this, try configuring the message to trigger using a different action (like session start) and verify whether it displays.

3. Failed image downloads will prevent in-app messages with images from displaying. Check your device logs to ensure that image downloads are not failing. Try removing your image temporarily from your message to see if that causes it to display.


7. If your in-app message is triggered by session start and you've set an extended session timeout, this will affect how quickly you can show messages. For instance, if your session timeout is set to 300 seconds, closing and re-opening the app in less than that time will not refresh the session, so an in-app message triggered by a session start will not display.



### Troubleshooting asset loading (`NSURLError` code `-1008`)

When integrating Braze alongside third-party network logging libraries, developers can commonly run into an `NSURLError` with the domain code `-1008`. This error indicates that assets like images and fonts could not be retrieved or failed to cache. To work around such cases, you will need to register Braze CDN URLs to the list of domains that should be ignored by these libraries.

#### Domains

The full list of CDN domains is as listed below:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Examples

Below are libraries that are known to conflict with Braze asset caching, along with example code to work around the issue. If your project uses a library that causes an unavailable resource error and is not listed below, consult the documentation of that library for similar usage APIs.

##### Netfox



```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```


```objc
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];
```



##### NetGuard



```swift
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])
```


```objc
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;
```



##### XNLogger



```swift
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])
```


```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```







