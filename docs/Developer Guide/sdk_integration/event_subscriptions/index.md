# Event subscriptions

> Learn how Braze SDK event subscriptions work for Banners, Content Cards, and Feature Flags. This article explains when each event fires and what your integration should do about it.

## Prerequisites

These are the minimum SDK versions needed to use event subscriptions:

<div id='sdk-versions'><a href='/docs/developer_guide/platforms/swift/changelog/#1900' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 19.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/web/changelog/#700' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: 7.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/android/changelog/#4400' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 44.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

## About event subscriptions

Each channel has an event subscription method. You register one callback, and the SDK calls it every time something happens on that channel, such as a cache replay, a completed refresh, an analytics event, or an error. Each event tells you which kind of event you received.

The event subscription methods replace the older update subscription methods. The older methods deliver only the current data. The event methods also tell you why the data changed, when analytics events are logged and sent, and when a request fails.




| Channel | Event subscription method | Replaces | Guide |
|---|---|---|---|
| Banners | [`subscribeToBannersEvents`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersevents) | `subscribeToBannersUpdates` | [Manage Banner placements](https://www.braze.com/docs/developer_guide/banners/placements?tab=web#subscribeToBannersUpdates) |
| Content Cards | [`subscribeToContentCardsEvents`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsevents) | `subscribeToContentCardsUpdates` | [Create Content Cards](https://www.braze.com/docs/developer_guide/content_cards/creating_cards?tab=web#step-2-subscribe-to-card-updates) |
| Feature Flags | [`subscribeToFeatureFlagsEvents`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetofeatureflagsevents) | `subscribeToFeatureFlagsUpdates` | [Create feature flags](https://www.braze.com/docs/developer_guide/feature_flags/create?tab=web#updates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Web event subscription methods" }

**Important:**


`subscribeToBannersUpdates`, `subscribeToContentCardsUpdates`, and `subscribeToFeatureFlagsUpdates` are deprecated and will be removed in a future major version. Use the matching event subscription method instead.






| Channel | Event subscription method | Replaces | Guide |
|---|---|---|---|
| Banners | [`braze.banners.subscribeToEvents(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banners-swift.class/subscribetoevents(_:)) | `subscribeToUpdates(_:)` | [Manage Banner placements](https://www.braze.com/docs/developer_guide/banners/placements?tab=swift#subscribeToBannersUpdates) |
| Content Cards | [`braze.contentCards.subscribeToEvents(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoevents(_:)) | `subscribeToUpdates(_:)` | [Create Content Cards](https://www.braze.com/docs/developer_guide/content_cards/creating_cards?tab=swift#step-2-subscribe-to-card-updates) |
| Feature Flags | [`braze.featureFlags.subscribeToEvents(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoevents(_:)) | `subscribeToUpdates(_:)` | [Create feature flags](https://www.braze.com/docs/developer_guide/feature_flags/create?tab=swift#updates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Swift event subscription methods" }

For the full API reference, see the [BrazeKit documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit).

Each channel also has an `eventsStream` property that delivers the same events as an `AsyncStream`. Objective-C apps use the `subscribeToEvents:` method on the same channel objects.

**Important:**


The older `subscribeToUpdates(_:)` method and the per-channel update streams, such as `bannersStream`, are deprecated. Use `subscribeToEvents(_:)` or `eventsStream` instead.






| Channel | Event subscription method | Event class | Replaces | Guide |
|---|---|---|---|---|
| Banners | [`subscribeToBannersEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-banners-events.html) | [`BannersEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-banners-event/index.html) | `subscribeToBannersUpdates` | [Manage Banner placements](https://www.braze.com/docs/developer_guide/banners/placements?tab=android#subscribeToBannersUpdates) |
| Content Cards | [`subscribeToContentCardsEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-content-cards-events.html) | [`ContentCardsEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-event/index.html) | `subscribeToContentCardsUpdates` | [Create Content Cards](https://www.braze.com/docs/developer_guide/content_cards/creating_cards?tab=android#step-2-subscribe-to-card-updates) |
| Feature Flags | [`subscribeToFeatureFlagsEvents`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-feature-flags-events.html) | [`FeatureFlagsEvent`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feature-flags-event/index.html) | `subscribeToFeatureFlagsUpdates` | [Create feature flags](https://www.braze.com/docs/developer_guide/feature_flags/create?tab=android#updates) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Android event subscription methods" }

For the full API reference, see the [Braze Android SDK KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html).

**Important:**


`subscribeToBannersUpdates`, `subscribeToContentCardsUpdates`, `subscribeToFeatureFlagsUpdates`, and `subscribeToBannersErrors` are deprecated. Use the matching event subscription method instead.






### Names by platform

This article uses the Web names for event types, update reasons, retry states, analytics actions, and error reasons. Swift and Android use the same concepts with names that follow each platform's conventions.

| Web | Swift | Android |
|---|---|---|
| `CACHE_REPLAY` | `cacheReplay` | `CacheReplay` |
| `CACHE_LOAD` | `cacheLoad` | `CacheLoad` |
| `DATA_UPDATED` | `dataUpdated` | `DataUpdated` |
| `IMPRESSION` | `impressionEvent` | `ImpressionEvent` |
| `CLICK` | `clickEvent` | `ClickEvent` |
| `DISMISS` | `dismissEvent` | `DismissEvent` |
| `ERROR` | `error` | `ErrorEvent` |
| `AUTO_SERVER_REFRESH` | `autoServerRefresh` | `AUTO_SERVER_REFRESH` |
| `SDK_WILL_RETRY` | `sdkWillRetry` | `SDK_WILL_RETRY` |
| `ENQUEUED` | `enqueued` | `ENQUEUED` |
| `SERVER_ERROR` | `.common(.serverError)` | `Common(ErrorReason.ServerError)` |
| `FEATURE_DISABLED` | `.featureDisabled` | `FeatureDisabled` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Event names by platform" }

The remaining update reasons, retry states, analytics actions, and error reasons follow the same pattern. On Swift, the update reason type is `Braze.ChannelUpdateReason`. On Android, each channel has its own update reason type, such as `BannersUpdateReason`.

### How events are delivered

The SDK delivers events in this order:

1. **When you subscribe:** The SDK calls your callback right away with a `CACHE_REPLAY` event that contains the cached data. If the channel is disabled, it sends an `ERROR` event with the `FEATURE_DISABLED` reason instead. In both cases, your subscription stays active.
2. **When the cache changes:** The SDK sends a `CACHE_LOAD` event if the cache changed without a server refresh, or a `DATA_UPDATED` event if a refresh finished or you changed the data locally.
3. **When you or the SDK log analytics:** The SDK sends an `IMPRESSION`, `CLICK`, or `DISMISS` event with the `ENQUEUED` action, and sends it again with the `FLUSHED` action after Braze accepts it.
4. **When something fails:** The SDK sends an `ERROR` event.

Your callback receives the event as its only argument. Handle each kind of event with a switch on the event type. On Web, the SDK logs an error that your callback throws and still delivers the event to other subscribers.




```javascript
import * as braze from "@braze/web-sdk";

// Register the subscription
const subscriptionId = braze.subscribeToBannersEvents((event) => {
  switch (event.type) {
    case braze.ChannelEventType.CACHE_REPLAY:
      // Sent once, right away, with the cached data
      break;
    case braze.ChannelEventType.DATA_UPDATED:
      // A refresh finished or the data changed locally
      break;
    case braze.ChannelEventType.ERROR:
      // A request or analytics operation failed
      break;
  }
});

// Remove the subscription when you no longer need it
braze.removeSubscription(subscriptionId);
```

**Note:**


Call the event subscription method after you initialize the SDK. Call it before `openSession()` so your callback receives the events from the first session. If the SDK is disabled, the method returns `undefined`.






```swift
// Register the subscription and keep a strong reference to it
let cancellable = AppDelegate.braze?.banners.subscribeToEvents { event in
  switch event {
  case .cacheReplay(let cacheSnapshot):
    // Sent once, right away, with the cached data
    break
  case .dataUpdated(let cacheSnapshot, let reason):
    // A refresh finished or the data changed locally
    break
  case .error(let reason, let retryState):
    // A request or analytics operation failed
    break
  default:
    break
  }
}

// Remove the subscription when you no longer need it
cancellable?.cancel()
```

**Note:**


Keep a strong reference to the returned cancellable. The SDK cancels the subscription when the cancellable is deallocated. The SDK calls your handler on the main thread.






```kotlin
// Register the subscription
val subscriber = IEventSubscriber<BannersEvent> { event ->
  when (event) {
    is BannersEvent.CacheReplay -> {
      // Sent once, right away, with the cached data
    }
    is BannersEvent.DataUpdated -> {
      // A refresh finished or the data changed locally
    }
    is BannersEvent.ErrorEvent -> {
      // A request or analytics operation failed
    }
    else -> Unit
  }
}
Braze.getInstance(context).subscribeToBannersEvents(subscriber)

// Remove the subscription when you no longer need it
Braze.getInstance(context).removeSingleSubscription(subscriber, BannersEvent::class.java)
```

**Note:**


The SDK calls your subscriber from a background thread. Switch to the main thread before you update your UI.






### Cache snapshots

`CACHE_REPLAY`, `CACHE_LOAD`, and `DATA_UPDATED` events include a `cacheSnapshot` property with the data the SDK has cached for the current user.

| Channel | Data in `cacheSnapshot` |
|---|---|
| Banners | `banners`: a map of each placement ID to its cached Banner. Placements without a Banner aren't in the map. |
| Content Cards | Web: `contentCards`, a `ContentCards` object. Use `contentCards.cards` to get the list of cards. Swift and Android: `cards`, the list of cards. |
| Feature Flags | `featureFlags`: the list of feature flags. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cache snapshot data by channel" }

Every snapshot also includes `lastSyncAt`, the time of the last successful sync for the current user as a Unix timestamp in seconds. The value is `0` if no sync has succeeded and `null` (`nil` on Swift) if the channel is disabled.

## Migrate from update subscriptions {#migrate-from-update-subscriptions}

The update subscription methods still work, but they're deprecated. To migrate each subscription, after you meet the [prerequisites](#prerequisites):

1. Replace the deprecated method with the event subscription method for that channel. The tables in [About event subscriptions](#about-event-subscriptions) list each pair.
2. Update your callback. The old callback received only the current data. The new callback receives an event, so check the event type. For `CACHE_REPLAY`, `CACHE_LOAD`, and `DATA_UPDATED` events, read the data from `cacheSnapshot` and re-render.
3. (Optional) Handle `ERROR` events to find out when a refresh or an analytics operation fails. On Android, they replace `subscribeToBannersErrors`. For details, see [Error reasons](#error-reasons).
4. Remove the subscription. On Android, pass the new event class (`BannersEvent`, `ContentCardsEvent`, or `FeatureFlagsEvent`) to `removeSingleSubscription`, not the legacy `…UpdatedEvent` class.

For before-and-after code, see the guide for each channel in the tables in [About event subscriptions](#about-event-subscriptions).

## Event types

Every event is one of the event types in this table. On Web, the event has a `type` property with one of the [`ChannelEventType`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#channeleventtype) values. On Swift and Android, each event type is its own case or class. Not every channel sends every event type.

| Event type | Sent by | When it fires | What to do |
|---|---|---|---|
| `CACHE_REPLAY` | Banners, Content Cards, Feature Flags | Once, right away, each time you subscribe. It has a `cacheSnapshot` with the current cache. | Render the cached data so your UI has content without waiting for the network. |
| `CACHE_LOAD` | Banners, Content Cards, Feature Flags | The cache changed without a server refresh. This happens when the user changes, when you wipe SDK data, or when the channel is turned off. On Web, Content Cards also send it when cards arrive from the service worker. On Swift and Android, it also fires when the SDK loads the cache from local storage before any network sync. It has a `cacheSnapshot` with the new cache. | Re-render from the snapshot. After a user change or when the channel is turned off, the snapshot can be empty, so clear content from the previous user. |
| `DATA_UPDATED` | Banners, Content Cards, Feature Flags | The cache changed. The SDK sends it for every completed refresh, even if nothing changed, and for local changes such as a dismissal. It has a `cacheSnapshot` and a `reason`. | Re-render from the snapshot. Check `reason` to decide whether the change came from a refresh or from your own action. |
| `IMPRESSION` | Banners, Content Cards, Feature Flags | An impression was logged. It has an `action` and the item that was logged (`banner`, `card`, or `flag`). | Optional. Use it to mirror impressions in your own analytics. |
| `CLICK` | Banners, Content Cards | A click was logged. It has an `action` and the item that was clicked (`banner` or `card`). Banner clicks also include a button ID if the click came from a button with an ID. | Optional. Use it to mirror clicks in your own analytics. |
| `DISMISS` | Banners, Content Cards | A dismissal was logged. It has an `action` and the item that was dismissed (`banner` or `card`). | Optional. `DISMISS` is the analytics event, so update your UI from the `DATA_UPDATED` event that follows a dismissal. |
| `ERROR` | Banners, Content Cards, Feature Flags | A request or an operation failed. It has a `reason` and a `retryState`. On Web, it sometimes has `rateLimitedUntil`. On Swift and Android, the rate limit time is part of the `RATE_LIMITED` reason. | Check `retryState` to decide whether to retry, and check `reason` to find the cause. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Event types" }

## Update reasons

`DATA_UPDATED` events include a `reason` with one of the [`ChannelUpdateReason`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#channelupdatereason) values.

| Value | Meaning | What to do |
|---|---|---|
| `AUTO_SERVER_REFRESH` | A refresh that the SDK started finished, such as a refresh on a new session, including its retries. | Re-render from the snapshot. |
| `MANUAL_SERVER_REFRESH` | A refresh that you requested finished, including its retries. Examples are `requestBannersRefresh()`, `requestContentCardsRefresh()`, and `refreshFeatureFlags()` on Web and Android, or `requestRefresh()` on Swift. | Re-render from the snapshot. Use this to hide a loading indicator that you showed when you requested the refresh. |
| `CLIENT_ACTION` | The cache changed because of a local action instead of a server response, such as dismissing a Banner or a Content Card. | Re-render from the snapshot without showing a loading or error state. Feature Flags doesn't currently send this reason, but handle it so your code keeps working if it does. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Update reasons" }

## Retry states

`ERROR` events include a `retryState` with one of the [`RetryState`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#retrystate) values. It tells you whether the SDK will retry the failed operation and what you should do.

| Value | Meaning | What to do |
|---|---|---|
| `SDK_WILL_RETRY` | The SDK is retrying automatically, or is waiting for a rate limit to clear and will then retry. | Keep showing the cached content. Don't request another refresh, because the SDK sends a `DATA_UPDATED` or another `ERROR` event when the retry finishes. |
| `INTEGRATOR_MAY_RETRY` | The SDK has stopped retrying. | Keep showing the cached content. You can call the refresh method again after a delay. If the event includes `rateLimitedUntil`, wait until that time. |
| `DO_NOT_RETRY` | The failure is final for this operation. Retrying won't help. | Don't retry. Fix the cause instead, such as the API key or workspace settings. If the reason is `FEATURE_DISABLED`, stop showing content from the channel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Retry states" }

**Note:**


Refreshes don't retry automatically after a client error (an HTTP 4xx response other than 429). The SDK reports these errors with the `DO_NOT_RETRY` retry state. It still retries HTTP 429, HTTP 5xx, and network failures.



## Analytics actions

`IMPRESSION`, `CLICK`, and `DISMISS` events include an `action` with one of the `AnalyticsAction` values. Each analytics event is sent twice: first with `ENQUEUED`, then with `FLUSHED`.

| Value | Meaning | What to do |
|---|---|---|
| `ENQUEUED` | The SDK saved the analytics event locally. Braze hasn't received it yet. | Use it to update your UI or your own logging right away. |
| `FLUSHED` | The SDK flushed the analytics event to Braze with a successful network response. | Use it as confirmation that the event was flushed. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics actions" }

## Error reasons

`ERROR` events include a `reason` with one of the `ChannelErrorReason` values. Every reason can apply to every channel.

| Value | Meaning | What to do |
|---|---|---|
| `SERVER_ERROR` | Braze returned a server-side failure (such as an HTTP 5xx response, or an HTTP 429 response without a usable `Retry-After` header), or the request didn't reach Braze. | Follow the `retryState`. The SDK retries first, then reports `INTEGRATOR_MAY_RETRY`. Keep showing the cached content. |
| `CLIENT_ERROR` | Braze rejected the request (such as an HTTP 4xx response other than 429, or an SDK Authentication error). On Web, for Feature Flags, it can also mean the SDK couldn't save an impression locally. | Follow the `retryState`. An HTTP 4xx response is `DO_NOT_RETRY` right away. For an SDK Authentication error, the SDK retries first and then reports `DO_NOT_RETRY`. Check your API key, SDK endpoint, and [SDK Authentication](https://www.braze.com/docs/developer_guide/sdk_integration/authentication) setup. |
| `RATE_LIMITED` | The request was rate limited. The event includes `rateLimitedUntil`, a date for the earliest time another attempt can succeed. | If the `retryState` is `SDK_WILL_RETRY`, wait. If it is `INTEGRATOR_MAY_RETRY`, wait until `rateLimitedUntil` before you refresh again, because an earlier request fails again. For more information, see [Rate limits](https://www.braze.com/docs/developer_guide/sdk_integration/rate_limits). |
| `SDK_DISABLED` | The SDK is disabled locally, so it makes no network requests. | Treat it as final and don't retry. |
| `INVALID_SERVER_DATA` | Braze returned data that the SDK couldn't interpret. | Don't retry. The `retryState` is `DO_NOT_RETRY`. Keep showing the cached content, and contact [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support) if it persists. |
| `FEATURE_DISABLED` | The channel is disabled for this workspace. The SDK also reports the channel as disabled until it receives its first configuration from Braze. | Hide the UI for the channel. This isn't the same as an empty list of content. Keep your subscription: if Braze then enables the channel, the SDK refreshes and sends a `DATA_UPDATED` event. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Error reasons" }

**Tip:**


You can receive a `FEATURE_DISABLED` error when you subscribe before the SDK has received its first configuration from Braze, even if the channel is enabled for your workspace. Keep your subscription active and handle the `DATA_UPDATED` event that follows.


