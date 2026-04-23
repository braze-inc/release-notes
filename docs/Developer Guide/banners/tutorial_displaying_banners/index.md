# Tutorial: Displaying a Banner by Placement ID

> Follow along with the sample code in this tutorial to display Banners using their placement ID. For more general information, see [Banners](https://www.braze.com/docs/developer_guide/banners/).



## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

<div id='sdk-versions'><a href='/docs/developer_guide/platforms/swift/changelog/#1130' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 11.3.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/web/changelog/#581' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: 5.8.1+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/android/changelog/#3310' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 33.1.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/flutter/changelog/#1300' class='sdk-versions--chip flutter-sdk' target='_blank'>Flutter: 13.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/react_native/changelog/#1400' class='sdk-versions--chip reactnative-sdk' target='_blank'>React Native: 14.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## Displaying banners for the Web SDK

**Important:**


We're piloting this new tutorial format. [Tell us what you think](https://docs.google.com/forms/d/e/1FAIpQLSe_5uhWM7eXXk9F_gviO_pvA4rkYO3WA9B6tNJZ3TY91md5bw/viewform?usp=pp_url&entry.569173304=General+Feedback) — your feedback helps us improve future guides.





```js file=index.js
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToBannersUpdates((banners) => {
  // Get this placement's banner. If it's `null`, the user did not qualify for any banners.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    // Hide or collapse the container
    container.style.display = "none";
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

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-index.js=8-23

#### 2. Subscribe to Banner updates

Use `subscribeToBannersUpdates()` to register a handler that runs whenever a Banner is updated. Inside the handler, call `braze.getBanner("global_banner")` to get the latest placement.

!!step
lines-index.js=15-22

#### 3. Insert the Banner and handle control groups

Use `braze.insertBanner(banner, container)` to insert a Banner when it's returned. To ensure keep your layout clean, hide or collapse Banners that are apart of a control group (for example, when `isControl` is `true`).

!!step
lines-index.js=25

#### 4. Refresh your Banners

After initializing the SDK, call `requestBannersRefresh(["global_banner", ...])` to ensure that Banners are refreshed at the start of each session.

You can also call this function at any time to refresh Banner placements later.

!!step
lines-main.html=3

#### 5. Add a container for your Banner

In your HTML, add a new `<div>` element and give it a short, Banner-related `id`, such as `global-banner-container`. Braze will use this `<div>` to insert your Banner into the page.





## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

<div id='sdk-versions'><a href='/docs/developer_guide/platforms/swift/changelog/#1130' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 11.3.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/web/changelog/#581' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: 5.8.1+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/android/changelog/#3310' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 33.1.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/flutter/changelog/#1300' class='sdk-versions--chip flutter-sdk' target='_blank'>Flutter: 13.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/react_native/changelog/#1400' class='sdk-versions--chip reactnative-sdk' target='_blank'>React Native: 14.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## Displaying banners for the Android SDK

**Important:**


We're piloting this new tutorial format. [Tell us what you think](https://docs.google.com/forms/d/e/1FAIpQLSe_5uhWM7eXXk9F_gviO_pvA4rkYO3WA9B6tNJZ3TY91md5bw/viewform?usp=pp_url&entry.569173304=General+Feedback) — your feedback helps us improve future guides.





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

        // Configure Braze with your SDK key and endpoint
        val config = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, config)

        // Subscribe to Banner updates
        Braze.getInstance(this)
            .subscribeToBannersUpdates { update ->
                for (banner in update.banners) {
                    Log.d("brazeBanners", "Received banner for placement: ${banner.placementId}")
                    // Add any custom banner logic you'd like
                }
            }
    }
}
```

```kotlin file=MainActivity.kt
import android.os.Bundle
import androidx.activity.ComponentActivity

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Inflate the XML layout
        setContentView(R.layout.banners)

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
            android:layout_height="wrap_content"
            app:placementId="top-1" />

        <!-- ...the rest of your activity layout -->

    </LinearLayout>
</ScrollView>
```

!!step
lines-MainApplication.kt=12

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-MainApplication.kt=21-28

#### 2. Subscribe to Banner updates

Use `subscribeToBannersUpdates()` to register a handler that runs whenever a Banner is updated.

!!step
lines-MainActivity.kt=10-14

#### 3. Refresh your placements

After initializing the Braze SDK, call `requestBannersRefresh(["PLACEMENT_ID"])`  to fetch the latest Banner content for that placement.

!!step
lines-banners.xml=15-19

#### 4. Define `BannerView` in your `banners.xml`

In `banners.xml`, declare a `<com.braze.ui.banners.BannerView>` element with `app:placementId="PLACEMENT_ID"`. Braze will use this element to insert your Banner into your UI.





## Prerequisites

Before you can start this tutorial, verify that your Braze SDK meets the minimum version requirements:

<div id='sdk-versions'><a href='/docs/developer_guide/platforms/swift/changelog/#1130' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 11.3.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/web/changelog/#581' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: 5.8.1+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/android/changelog/#3310' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 33.1.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/flutter/changelog/#1300' class='sdk-versions--chip flutter-sdk' target='_blank'>Flutter: 13.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/react_native/changelog/#1400' class='sdk-versions--chip reactnative-sdk' target='_blank'>React Native: 14.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## Displaying banners for the Swift SDK

**Important:**


We're piloting this new tutorial format. [Tell us what you think](https://docs.google.com/forms/d/e/1FAIpQLSe_5uhWM7eXXk9F_gviO_pvA4rkYO3WA9B6tNJZ3TY91md5bw/viewform?usp=pp_url&entry.569173304=General+Feedback) — your feedback helps us improve future guides.







```swift file=AppDelegate.swift
import UIKit
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
  var bannerHeightConstraints: NSLayoutConstraint?

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
lines-AppDelegate.swift=14

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-AppDelegate.swift=20

#### 2. Refresh your placements

After initializing the Braze SDK, `call requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` to refresh Banner content at the start of each session.

!!step
lines-BannerViewController.swift=19-37

#### 3. Initialize the Banner and provide a callback

Create a `BrazeBannerUI.BannerUIView` instance with your Braze object and placement ID, and provide a `processContentUpdates` callback to unhide the Banner and update its height constraint based on the provided content height.

!!step
lines-BannerViewController.swift=38-40

#### 4. Enable Auto Layout constraints

Hide the Banner view by default, then disable autoresizing mask translation to enable Auto Layout constraints.

!!step
lines-BannerViewController.swift=43-58

#### 5. Anchor content and set height constraints

Anchor your main content to the top using Auto Layout, and place the Banner view directly below it. Pin the Banner’s leading, trailing, and bottom edges to the safe area, and set an initial height constraint of `0` that will be updated when content loads.






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
      AppDelegate.braze?.banners.getBanner(
        for: BannerSwiftUIView.bannerPlacementID,
        { banner in
          hasBannerForPlacement = banner != nil
        }
      )
    }
  }
}

```

!!step
lines-AppDelegate.swift=13

#### 1. Enable debugging (optional)

To make troubleshooting easier while developing, consider enabling debugging.

!!step
lines-AppDelegate.swift=19

#### 2. Refresh your placements

After initializing the Braze SDK, call `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` to refresh Banner content at the start of each session.

!!step
lines-BannerSwiftUIView.swift=1-46

#### 3. Create a view component

Create a reusable SwiftUI view component that displays available Banners and contains your main app content if needed.

!!step
lines-BannerSwiftUIView.swift=36-43

#### 4. Only display available Banners

Only attempt to show `BrazeBannerUI.BannerView` if the SDK is initialized and Banner content exists for that user. In `.onAppear`, call `getBanner(for:placementID)` to set the state of `hasBannerForPlacement`.

!!step
lines-BannerSwiftUIView.swift=17-32

#### 5. Only show `BannerView` after it loads

To avoid blank space in your UI, only show `BrazeBannerUI.BannerView` if a Banner is present and the SDK is initialized.

!!step
lines-BannerSwiftUIView.swift=23-32

#### 6. Dynamically update Banner height

Use the `processContentUpdates` callback to fetch the Banner’s content height as soon as it loads. Update your SwiftUI state (`contentHeight`) and apply a `.frame(height:)` constraint using the provided height.

!!step
lines-BannerSwiftUIView.swift=34

#### 7. Limit the Banner height

To ensure your Banner never exceeds the maximum height, apply a `.frame(height: min(contentHeight, 80))` modifier. This will keep your UI visually balanced regardless of the Banner's content.







