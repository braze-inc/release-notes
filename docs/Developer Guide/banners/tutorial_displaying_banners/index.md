# Tutorial: Displaying a Banner by Placement ID

> Follow along with the sample code in this tutorial to display Banners using their placement ID. For more general information, see [Banners](https://www.braze.com/docs/developer_guide/banners).



## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

<div id='sdk-versions'><a href='/docs/developer_guide/changelogs/?sdktab=swift#swift_1130' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 11.3.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=web#web_700' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: 7.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=android#android_3310' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 33.1.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=flutter#flutter_1300' class='sdk-versions--chip flutter-sdk' target='_blank'>Flutter: 13.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=react%20native#reactnative_1400' class='sdk-versions--chip reactnative-sdk' target='_blank'>React Native: 14.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## Displaying banners for the Web SDK

**Important:**


We're piloting this new tutorial format. [Tell us what you think](https://docs.google.com/forms/d/e/1FAIpQLSe_5uhWM7eXXk9F_gviO_pvA4rkYO3WA9B6tNJZ3TY91md5bw/viewform?usp=pp_url&entry.569173304=General+Feedback) — your feedback helps us improve future guides.





```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersEvents((event) => {
  const container = document.getElementById("global-banner-container");

  switch (event.type) {
    case braze.ChannelEventType.CACHE_REPLAY:
    case braze.ChannelEventType.CACHE_LOAD:
    case braze.ChannelEventType.DATA_UPDATED: {
      // Get this placement's banner. If it's missing, the user did not qualify for any banners.
      const globalBanner = event.cacheSnapshot.banners["global_banner"];
      if (!globalBanner) {
        return;
      }

      braze.insertBanner(globalBanner, container);

      if (globalBanner.isControl) {
        // Hide or collapse the container
        container.style.display = "none";
      }
      break;
    }
    case braze.ChannelEventType.ERROR:
      if (event.reason === braze.ChannelErrorReason.FEATURE_DISABLED) {
        // Banners are disabled, so hide the container
        container.style.display = "none";
      }
      break;
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

```html file=main.html
<!-- your html -->

<div id="global-banner-container" style="width: 100%; height: 450px;"></div>

<!-- ...the rest of your html -->
```

!!step
lines-index.js=5

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-index.js=8-36

### 2. Subscribe to Banner events

Use `subscribeToBannersEvents()` on Web SDK 7.0.0 and later to register a handler. The handler runs when the Banner cache is replayed, reloaded, or updated, or when an error occurs. Inside the handler, read the placement from `event.cacheSnapshot.banners`. `subscribeToBannersUpdates()` is the earlier pattern, deprecated as of 7.0.0. For the full list of events, see [Event subscriptions](https://www.braze.com/docs/developer_guide/sdk_integration/event_subscriptions).

!!step
lines-index.js=21-26

### 3. Insert the Banner and handle control groups

Use `braze.insertBanner(banner, container)` to insert a Banner when it's returned. To ensure keep your layout clean, hide or collapse Banners that are apart of a control group (for example, when `isControl` is `true`).

!!step
lines-index.js=38

### 4. Refresh your Banners

After initializing the SDK, call `requestBannersRefresh(["global_banner", ...])` to ensure that Banners are refreshed at the start of each session.

You can also call this function at any time to refresh Banner placements later.

!!step
lines-main.html=3

### 5. Add a container for your Banner

In your HTML, add a new `<div>` element and give it a short, Banner-related `id`, such as `global-banner-container`. Braze will use this `<div>` to insert your Banner into the page.





## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

<div id='sdk-versions'><a href='/docs/developer_guide/changelogs/?sdktab=swift#swift_1130' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 11.3.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=web#web_581' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: 5.8.1+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=android#android_3310' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 33.1.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=flutter#flutter_1300' class='sdk-versions--chip flutter-sdk' target='_blank'>Flutter: 13.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=react%20native#reactnative_1400' class='sdk-versions--chip reactnative-sdk' target='_blank'>React Native: 14.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## Displaying banners for the Android SDK

**Important:**


We're piloting this new tutorial format. [Tell us what you think](https://docs.google.com/forms/d/e/1FAIpQLSe_5uhWM7eXXk9F_gviO_pvA4rkYO3WA9B6tNJZ3TY91md5bw/viewform?usp=pp_url&entry.569173304=General+Feedback) — your feedback helps us improve future guides.







```kotlin file=MainApplication.kt
import android.app.Application
import android.util.Log
import com.braze.Braze
import com.braze.configuration.BrazeConfig
import com.braze.events.BannersEvent
import com.braze.events.ChannelErrorReason
import com.braze.support.BrazeLogger

public class MainApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.logLevel = Log.VERBOSE

        // Configure Braze with your SDK key and endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, config)

        // Subscribe to Banner events
        Braze.getInstance(this)
            .subscribeToBannersEvents { event ->
                when (event) {
                    is BannersEvent.CacheReplay -> {
                        for ((_, banner) in event.cacheSnapshot.banners) {
                            Log.d("brazeBanners", "Received banner for placement: ${banner.placementId}")
                        }
                    }
                    is BannersEvent.CacheLoad -> {
                        for ((_, banner) in event.cacheSnapshot.banners) {
                            Log.d("brazeBanners", "Received banner for placement: ${banner.placementId}")
                        }
                    }
                    is BannersEvent.DataUpdated -> {
                        for ((_, banner) in event.cacheSnapshot.banners) {
                            Log.d("brazeBanners", "Received banner for placement: ${banner.placementId}")
                        }
                    }
                    is BannersEvent.ErrorEvent -> {
                        if (event.reason is ChannelErrorReason.FeatureDisabled) {
                            Log.d("brazeBanners", "Banners is disabled for this app or user.")
                        }
                    }
                    else -> {}
                }
            }
    }
}
```

```kotlin file=MainActivity.kt
import android.os.Bundle
import android.util.TypedValue
import androidx.activity.ComponentActivity
import com.braze.Braze
import com.braze.ui.banners.BannerView
import kotlin.math.min

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.banners)

        val bannerView = findViewById<BannerView>(R.id.banner_view_1)
        bannerView.heightCallback = { heightDp ->
            bannerView.post {
                val cappedHeightDp = min(heightDp, 80.0)
                val heightPx = TypedValue.applyDimension(
                    TypedValue.COMPLEX_UNIT_DIP,
                    cappedHeightDp.toFloat(),
                    bannerView.resources.displayMetrics
                ).toInt()
                bannerView.layoutParams = bannerView.layoutParams.apply {
                    height = heightPx
                }
            }
        }

        // Refresh placements
        Braze.getInstance(this)
            .requestBannersRefresh(
                listOf("top-1")
            )
    }
}
```

```xml file=banners.xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <LinearLayout
        android:orientation="vertical"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_horizontal">

        <!-- Banner placement -->
        <com.braze.ui.banners.BannerView
            android:id="@+id/banner_view_1"
            android:layout_width="match_parent"
            android:layout_height="0dp"
            app:placementId="top-1" />

        <!-- ...the rest of your activity layout -->

    </LinearLayout>
</ScrollView>
```

!!step
lines-MainApplication.kt=14

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-MainApplication.kt=23-49

### 2. Subscribe to Banner events

Use `subscribeToBannersEvents()` to register a handler that runs when the Banner cache is replayed or updated. `BannersCacheSnapshot.banners` is a map of placement ID to `Banner`.

For the full list of events you can receive, see [Event subscriptions](https://www.braze.com/docs/developer_guide/sdk_integration/event_subscriptions).

!!step
lines-banners.xml=15-19

### 3. Define `BannerView` in your `banners.xml`

In `banners.xml`, declare a `<com.braze.ui.banners.BannerView>` with `app:placementId="PLACEMENT_ID"` and set `android:layout_height` to `0dp`. The view stays in the layout with no height until the Banner reports its content height, so the screen does not reserve empty space before a Banner loads.

After a refresh, the SDK updates a `BannerView` only when that placement's content changes. Unchanged displayed Banners stay as-is.

!!step
lines-MainActivity.kt=13-26

### 4. Update the Banner height

Set `heightCallback` on the `BannerView`. The callback receives the Banner height in dp. Apply that height to the view yourself: convert dp to pixels, then set the layout height.

Banner HTML reports its height through a JavaScript interface, so `heightCallback` can run off the main thread. Update the view inside `bannerView.post` so the change runs on the main thread.

A height of `0.0` means there is no content to show. The SDK reports `0.0` when the placement has no Banner, the Banner is in a control group, or the Banner was dismissed. Apply `0.0` as well, so the view collapses and stays in the layout for the next Banner.

!!step
lines-MainActivity.kt=16

### 5. Limit the Banner height

Cap the height you apply. In this example, `min(heightDp, 80.0)` keeps the Banner at 80&nbsp;dp or less.

!!step
lines-MainActivity.kt=28-32

### 6. Refresh your placements

After initializing the Braze SDK, call `requestBannersRefresh(["PLACEMENT_ID"])` to fetch the latest Banner content for that placement.

This call merges into the existing Banner cache. Only the placement IDs you request are added, updated, or removed. Cached Banners for other placements stay in the cache and expire at their original expiry time. If the server returns no Banner for a requested placement, that placement is dropped from the cache.





To use Jetpack Compose, add the `com.braze:android-sdk-jetpack-compose` artifact to your app module. Use the same version as your other Braze Android SDK dependencies.



```kotlin file=MainApplication.kt
import android.app.Application
import android.util.Log
import com.braze.Braze
import com.braze.configuration.BrazeConfig
import com.braze.support.BrazeLogger

public class MainApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Turn on verbose Braze logging
        BrazeLogger.logLevel = Log.VERBOSE

        val config = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, config)
    }
}
```

```kotlin file=BannerSlot.kt
import android.os.Handler
import android.os.Looper
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.braze.Braze
import com.braze.events.BannersEvent
import com.braze.events.ChannelErrorReason
import com.braze.events.IEventSubscriber
import com.braze.jetpackcompose.banners.Banner
import kotlin.math.min

private const val BANNER_PLACEMENT_ID = "top-1"

@Composable
fun BannerSlot() {
    val context = LocalContext.current
    val mainHandler = remember { Handler(Looper.getMainLooper()) }
    var hasBannerForPlacement by remember { mutableStateOf(false) }
    var contentHeight by remember { mutableStateOf(0.0) }

    DisposableEffect(context) {
        val subscriber = IEventSubscriber<BannersEvent> { event ->
            val hasBanner: Boolean? = when (event) {
                is BannersEvent.CacheReplay ->
                    event.cacheSnapshot.banners.containsKey(BANNER_PLACEMENT_ID)
                is BannersEvent.CacheLoad ->
                    event.cacheSnapshot.banners.containsKey(BANNER_PLACEMENT_ID)
                is BannersEvent.DataUpdated ->
                    event.cacheSnapshot.banners.containsKey(BANNER_PLACEMENT_ID)
                is BannersEvent.ErrorEvent ->
                    if (event.reason is ChannelErrorReason.FeatureDisabled) false else null
                else -> null
            }
            if (hasBanner != null) {
                val present = hasBanner
                mainHandler.post { hasBannerForPlacement = present }
            }
        }
        val braze = Braze.getInstance(context)
        braze.subscribeToBannersEvents(subscriber)
        braze.requestBannersRefresh(listOf(BANNER_PLACEMENT_ID))
        onDispose {
            braze.removeSingleSubscription(subscriber, BannersEvent::class.java)
        }
    }

    if (hasBannerForPlacement) {
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(min(contentHeight, 80.0).dp)
        ) {
            Banner(
                placementId = BANNER_PLACEMENT_ID,
                heightCallback = { heightDp ->
                    mainHandler.post { contentHeight = heightDp }
                }
            )
        }
    }
}
```

!!step
lines-MainApplication.kt=12

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-BannerSlot.kt=31-50

### 2. Subscribe to Banner events

Call `subscribeToBannersEvents` and keep the subscriber so you can remove it when the composable leaves the screen. Set `hasBannerForPlacement` when `CacheReplay`, `CacheLoad`, or `DataUpdated` contains this placement. On `ErrorEvent` with `FeatureDisabled`, set `hasBannerForPlacement` to `false`.

Banner events arrive on a background thread. Post UI updates to the main thread.

For when each event fires, see [Event subscriptions](https://www.braze.com/docs/developer_guide/sdk_integration/event_subscriptions).

!!step
lines-BannerSlot.kt=51-54

### 3. Refresh your placements

After you register the subscriber, call `requestBannersRefresh(["PLACEMENT_ID"])` to fetch the latest Banner content for that placement. Remove the subscriber with `removeSingleSubscription` when you no longer need it.

!!step
lines-BannerSlot.kt=57-70

### 4. Only show the Banner after it is in the cache

Show `Banner` only when `hasBannerForPlacement` is true. The placement stays out of your layout until the cache contains a Banner for it.

Import `com.braze.jetpackcompose.banners.Banner`. Other Compose libraries define their own `Banner` composable.

!!step
lines-BannerSlot.kt=65-67

### 5. Update the Banner height

Pass `heightCallback` to `Banner`. The callback receives the Banner height in dp. Store it in `contentHeight` and apply it with `Modifier.height`. `Banner` leaves sizing to your layout.

`heightCallback` can run off the main thread. Post the state update to the main thread before you change `contentHeight`.

A height of `0.0` means there is no content to show and prevents empty spaces in your UI. The SDK reports `0.0` when the placement has no Banner, the Banner is in a control group, or the Banner was dismissed.

!!step
lines-BannerSlot.kt=61

### 6. Limit the Banner height

Cap the height you apply. In this example, `min(contentHeight, 80.0)` keeps the Banner at 80&nbsp;dp or less.







## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

<div id='sdk-versions'><a href='/docs/developer_guide/changelogs/?sdktab=swift#swift_1130' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 11.3.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=web#web_581' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: 5.8.1+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=android#android_3310' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 33.1.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=flutter#flutter_1300' class='sdk-versions--chip flutter-sdk' target='_blank'>Flutter: 13.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/changelogs/?sdktab=react%20native#reactnative_1400' class='sdk-versions--chip reactnative-sdk' target='_blank'>React Native: 14.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## Displaying banners for the Swift SDK

**Important:**


We're piloting this new tutorial format. [Tell us what you think](https://docs.google.com/forms/d/e/1FAIpQLSe_5uhWM7eXXk9F_gviO_pvA4rkYO3WA9B6tNJZ3TY91md5bw/viewform?usp=pp_url&entry.569173304=General+Feedback) — your feedback helps us improve future guides.







```swift file=AppDelegate.swift
import UIKit
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze? = nil
    static var bannersSubscription: Braze.Cancellable? = nil

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR-API-TOKEN", endpoint: "YOUR-ENDPOINT")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        // Subscribe to Banner events
        AppDelegate.bannersSubscription = AppDelegate.braze?.banners.subscribeToEvents { event in
            switch event {
            case .cacheReplay(let cacheSnapshot), .cacheLoad(let cacheSnapshot), .dataUpdated(let cacheSnapshot, _):
                for (placementId, banner) in cacheSnapshot.banners {
                    print("Received banner: \(banner) with placement ID: \(placementId)")
                }
            case .error(let reason, _) where reason == .featureDisabled:
                print("Banners is disabled for this app or user.")
            default:
                break
            }
        }

        // Request a banners refresh
        AppDelegate.braze?.banners.requestBannersRefresh(placementIds: ["top-1"])

        return true
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
    // Bind the AppDelegate into the SwiftUI lifecycle
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift file=BannerViewController.swift
import UIKit
import BrazeKit
import BrazeUI

final class BannerViewController: UIViewController {

  static let bannerPlacementID = "top-1"
  var bannerHeightConstraint: NSLayoutConstraint?

  lazy var contentView: UILabel = {
    let contentView = UILabel()
    contentView.text = "Your Content Here"
    contentView.textAlignment = .center
    contentView.translatesAutoresizingMaskIntoConstraints = false
    return contentView
  }()

  lazy var bannerView: BrazeBannerUI.BannerUIView = {
    var bannerView = BrazeBannerUI.BannerUIView(
      placementId: BannerViewController.bannerPlacementID,
      braze: AppDelegate.braze!,
      processContentUpdates: { [weak self] result in
        // Update layout properties when banner content has finished loading.
        DispatchQueue.main.async {
          guard let self else { return }
          switch result {
          case .success(let updates):
            if let height = updates.height {
              self.bannerView.isHidden = false
              self.bannerHeightConstraint?.constant = min(height, 80)
            }
          case .failure(let error):
            return
          }
        }
      }
    )
    bannerView.translatesAutoresizingMaskIntoConstraints = false
    bannerView.isHidden = true
    return bannerView
  }()

  override func viewDidLoad() {
    super.viewDidLoad()
    self.view.addSubview(contentView)
    self.view.addSubview(bannerView)
    bannerHeightConstraint = bannerView.heightAnchor.constraint(equalToConstant: 0)
    NSLayoutConstraint.activate([
      contentView.topAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.topAnchor),
      contentView.leadingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.leadingAnchor),
      contentView.trailingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.trailingAnchor),
      bannerView.topAnchor.constraint(equalTo: self.contentView.bottomAnchor),
      bannerView.leadingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.leadingAnchor),
      bannerView.trailingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.trailingAnchor),
      bannerView.bottomAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.bottomAnchor),
      bannerHeightConstraint!,
    ])
  }
}
```

!!step
lines-AppDelegate.swift=15

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-AppDelegate.swift=20-32

### 2. Subscribe to Banner events

Use `subscribeToEvents` to register a handler that runs when the Banner cache is replayed, reloaded, or updated, or when an error occurs. `cacheSnapshot.banners` is a dictionary of placement ID to `Banner`. Keep a strong reference to the returned `Braze.Cancellable`, because the SDK cancels the subscription when it is deallocated.

For when each event fires, see [Event subscriptions](https://www.braze.com/docs/developer_guide/sdk_integration/event_subscriptions).

!!step
lines-AppDelegate.swift=35

### 3. Refresh your placements

After you register your subscription, call `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` to refresh Banner content at the start of each session.

!!step
lines-BannerViewController.swift=19-37

### 4. Initialize the Banner and provide a callback

Create a `BrazeBannerUI.BannerUIView` instance with your Braze object and placement ID, and provide a `processContentUpdates` callback to unhide the Banner and update its height constraint based on the provided content height.

!!step
lines-BannerViewController.swift=38-40

### 5. Enable Auto Layout constraints

Hide the Banner view by default, then disable autoresizing mask translation to enable Auto Layout constraints.

!!step
lines-BannerViewController.swift=43-58

### 6. Anchor content and set height constraints

Anchor your main content to the top using Auto Layout, and place the Banner view after it. Pin the Banner’s leading, trailing, and bottom edges to the safe area, and set an initial height constraint of `0` that will be updated when content loads.






```swift file=AppDelegate.swift
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze? = nil

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR-API-TOKEN", endpoint: "YOUR-ENDPOINT")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        // Request a banners refresh
        AppDelegate.braze?.banners.requestBannersRefresh(placementIds: ["top-1"])

        return true
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
    // Bind the AppDelegate into the SwiftUI lifecycle
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            BannerSwiftUIView()
        }
    }
}
```

```swift file=BannerSwiftUIView.swift
import BrazeKit
import BrazeUI
import SwiftUI

@available(iOS 13.0, *)
struct BannerSwiftUIView: View {

  static let bannerPlacementID = "top-1"

  @State var hasBannerForPlacement: Bool = false
  @State var contentHeight: CGFloat = 0
  @State var bannersSubscription: Braze.Cancellable?

  var body: some View {
    VStack {
      Text("Your Content Here")
        .frame(maxWidth: .infinity, maxHeight: .infinity)
      if let braze = AppDelegate.braze,
        hasBannerForPlacement
      {
        BrazeBannerUI.BannerView(
          placementId: BannerSwiftUIView.bannerPlacementID,
          braze: braze,
          processContentUpdates: { result in
            switch result {
            case .success(let updates):
              if let height = updates.height {
                self.contentHeight = height
              }
            case .failure:
              return
            }
          }
        )
        .frame(height: min(contentHeight, 80))
      }
    }.onAppear {
      bannersSubscription = AppDelegate.braze?.banners.subscribeToEvents { event in
        switch event {
        case .cacheReplay(let cacheSnapshot), .cacheLoad(let cacheSnapshot), .dataUpdated(let cacheSnapshot, _):
          hasBannerForPlacement = cacheSnapshot.banners[BannerSwiftUIView.bannerPlacementID] != nil
        case .error(let reason, _) where reason == .featureDisabled:
          hasBannerForPlacement = false
        default:
          break
        }
      }
    }
  }
}

```

!!step
lines-AppDelegate.swift=13

### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-AppDelegate.swift=19

### 2. Refresh your placements

After initializing the Braze SDK, call `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` to refresh Banner content at the start of each session.

!!step
lines-BannerSwiftUIView.swift=1-50

### 3. Create a view component

Create a reusable SwiftUI view component that displays available Banners and contains your main app content if needed.

!!step
lines-BannerSwiftUIView.swift=37-48

### 4. Subscribe to Banner events

In `.onAppear`, use `subscribeToEvents` to register a handler that sets `hasBannerForPlacement` whenever the Banner cache is replayed, reloaded, or updated. Keep a strong reference to the returned `Braze.Cancellable` in your state, because the SDK cancels the subscription when it is deallocated.

For when each event fires, see [Event subscriptions](https://www.braze.com/docs/developer_guide/sdk_integration/event_subscriptions).

!!step
lines-BannerSwiftUIView.swift=18-36

### 5. Only show `BannerView` after it loads

To avoid blank space in your UI, only show `BrazeBannerUI.BannerView` if a Banner is present and the SDK is initialized.

!!step
lines-BannerSwiftUIView.swift=24-33

### 6. Dynamically update Banner height

Use the `processContentUpdates` callback to fetch the Banner’s content height as soon as it loads. Update your SwiftUI state (`contentHeight`) and apply a `.frame(height:)` constraint using the provided height.

!!step
lines-BannerSwiftUIView.swift=35

### 7. Limit the Banner height

To ensure your Banner never exceeds the maximum height, apply a `.frame(height: min(contentHeight, 80))` modifier. This will keep your UI visually balanced regardless of the Banner's content.







