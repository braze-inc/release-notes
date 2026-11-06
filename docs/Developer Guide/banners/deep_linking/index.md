# Deep linking in Banners

> A Banner deep link is a custom-scheme or web URL on the Banner.

On iOS, Banner clicks are routed through `BrazeDelegate.braze(_:shouldOpenURL:)` with the Banner channel on the URL context. On Android, they are routed through `IBrazeDeeplinkHandler` with the Banner channel.

Push notifications open from the notification, including when the app is not running. Banner clicks happen while the app is open. A Content Card click listener or an in-app message click listener does not run for Banners.

For implementation details and guidance on choosing the right link type for your use case, see the deep linking documentation for your platform:

- [iOS](https://www.braze.com/docs/developer_guide/push_notifications/ios_deep_linking_guide)
- [Android](https://www.braze.com/docs/developer_guide/push_notifications/deep_linking)

For troubleshooting, see [Deep linking troubleshooting](https://www.braze.com/docs/developer_guide/push_notifications/deep_linking_troubleshooting).
