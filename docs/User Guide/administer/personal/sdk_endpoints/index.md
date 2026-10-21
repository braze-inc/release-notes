# API and SDK endpoints

> Look up the correct dashboard URL, REST API endpoint, and SDK endpoint for your Braze instance. You need these URLs to log in, make API calls, and integrate the SDK.

Braze manages a number of different instances for our dashboard, SDK, and REST endpoints, which we call "clusters." Your Braze onboarding manager will let you know which cluster you're on. To learn more about the Braze SDK, check out the [Braze 101](https://learning.braze.com/braze-101) Braze Learning course.

Logging in at [dashboard.braze.com](https://dashboard.braze.com) automatically sends you to the correct cluster address.















<!--The following section is the list of IPs for IP allowlisting-->




**Important:**


When integrating your SDK, use the SDK endpoint. When making calls to our REST API, use the REST endpoint.



For details about accessing the API, see our [API overview article](https://www.braze.com/docs/api/basics). 

## Custom URLs

Instead of the standard SDK endpoint for your cluster, you can configure the Braze SDK to send its network requests to a custom URL, such as a proxy or a custom domain. The following SDKs support custom URLs:

- [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk): Version 11.8.0 and later
- [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk): Version 2.11 and later

### Configuring a custom URL

Set your custom URL where you set your SDK endpoint when you initialize the SDK. For the full integration steps, see [Integrate the Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration).




Pass your custom URL as the `endpoint` when you create your `Braze.Configuration` object. For the full initialization steps, see [Step 3: Update your app delegate](https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=swift#swift_step-3-update-your-app-delegate).



```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR_APP_IDENTIFIER_API_KEY",
  endpoint: "YOUR_CUSTOM_URL"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```


```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"YOUR_APP_IDENTIFIER_API_KEY"
                                                                  endpoint:@"YOUR_CUSTOM_URL"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```



Replace the following:

- `YOUR_APP_IDENTIFIER_API_KEY`: The app identifier API key from the **App Settings** page in the Braze dashboard.
- `YOUR_CUSTOM_URL`: Your proxy or custom domain URL.

In Swift SDK version 11.8.0 and later, your custom URL can include a base path (for example, `example.com/mockServer`) and can use the `http` scheme. For more information, see the [Swift SDK changelog](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md).




You can set your custom URL in your `braze.xml` file or in code. For the full integration steps, see [Step 2: Configure your `braze.xml`](https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=android#android_step-2-configure-your-brazexml).

**Option 1: In your `braze.xml` file**

Set the `com_braze_custom_endpoint` string to your custom URL.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_URL</string>
</resources>
```

**Option 2: In code**

Call `setCustomEndpoint()` on your `BrazeConfig.Builder`, and then pass the result to `Braze.configure()`.



```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setApiKey("YOUR_APP_IDENTIFIER_API_KEY")
  .setCustomEndpoint("YOUR_CUSTOM_URL")
  .build();
Braze.configure(this, brazeConfig);
```


```kotlin
val brazeConfig = BrazeConfig.Builder()
  .setApiKey("YOUR_APP_IDENTIFIER_API_KEY")
  .setCustomEndpoint("YOUR_CUSTOM_URL")
  .build()
Braze.configure(this, brazeConfig)
```



Replace the following:

- `YOUR_APP_IDENTIFIER_API_KEY`: The app identifier API key from the **App Settings** page in the Braze dashboard.
- `YOUR_CUSTOM_URL`: Your proxy or custom domain URL.

In Android SDK version 9.0.1 and later, your custom URL can include a scheme and a base path.

If you set a custom `IBrazeEndpointProvider` on the Braze instance after you configure the SDK, it overrides the endpoint you set in `BrazeConfig`. For more information, see [`setEndpointProvider()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/set-endpoint-provider.html).




### Testing your proxy configuration

Test that your proxy works as you expect before you release your app to production. To confirm that the SDK sends requests to your custom URL, use verbose logging:

1. Enable verbose logging in your development build before you initialize the SDK. For the code for each SDK, see [Verbose logging](https://www.braze.com/docs/developer_guide/sdk_integration/verbose_logging#enabling-verbose-logging).
2. Run your app on a test device or simulator. The SDK sends a request when a session starts.
3. In your logs, find the request entries and confirm the request URL matches your custom URL.
4. Confirm your proxy receives the requests from the SDK.

If you don't see any requests to your custom URL on Android, verify your API key and endpoint configuration. For examples of what request entries look like in the logs, see [Reading verbose logs](https://www.braze.com/docs/developer_guide/sdk_integration/reading_verbose_logs#network-requests).

**Important:**


Disable verbose logging before you release your app to production.


