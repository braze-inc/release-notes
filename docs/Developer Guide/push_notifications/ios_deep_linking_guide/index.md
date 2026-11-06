# iOS deep linking guide

> This guide helps you choose the right deep linking strategy for your iOS app. Your choice depends on which messaging channel you're using and whether you use a third-party linking provider like Branch.

For implementation details, see [Deep linking](https://www.braze.com/docs/developer_guide/push_notifications/deep_linking?sdktab=swift). For troubleshooting, see [Deep linking troubleshooting](https://www.braze.com/docs/developer_guide/push_notifications/deep_linking_troubleshooting).

## Choosing a link type

There are three ways to handle links from Braze messages in your iOS app. Each one works differently and is suited for different channels and use cases.

| Link type | Example | Best for | Opens without app installed? |
|---|---|---|---|
| **Custom scheme** | `myapp://products/123` | Push, in-app messages, Content Cards, and Banners | No — link fails |
| **Universal link** | `https://myapp.com/products/123` | Email, SMS, channels with click tracking | Yes — falls back to web |
| **Open Web URL Inside App** | Any `https://` URL | Displaying web content in a modal WebView | N/A — displays in WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Choosing a link type" }

### Custom scheme deep links

Custom scheme deep links (for example, `myapp://products/123`) open your app directly to a specific screen. They are the simplest option for channels where links aren't modified by a third party.

**Use custom scheme deep links when:**
- Sending push notifications, in-app messages, Content Cards, or Banners
- You don't need the link to work if the app isn't installed
- You don't need click tracking (email ESP link wrapping)

**Don't use custom scheme deep links when:**
- Sending emails — ESPs wrap links for click tracking, which breaks custom schemes
- You need the link to fall back to a web page if the app isn't installed

### Universal links

Universal links (for example, `https://myapp.com/products/123`) are standard HTTPS URLs that iOS can route to your app instead of opening in a browser. They require server-side configuration (an AASA file) and app-side setup (Associated Domains entitlement).

**Use universal links when:**
- Sending emails. Your ESP wraps links for click tracking, so links must be HTTPS.
- Sending SMS or other channels where links are wrapped or shortened.
- You need the link to fall back to a web page when the app isn't installed.
- You're using a third-party linking provider like Branch or AppsFlyer.

**Don't use universal links when:**
- You only need deep links from push, in-app messages, Banners, or Content Cards. Custom schemes are simpler.

### "Open Web URL Inside App"

This option opens a web page inside a modal WebView within your app. It's handled entirely by the Braze SDK using `Braze.WebViewController` — you don't need to write any URL handling code.

**Use "Open Web URL Inside App" when:**
- You want to display a web page (such as a promotion or article) without leaving your app.
- The URL is a standard HTTPS web page, not a deep link to a specific app screen.

**Don't use "Open Web URL Inside App" when:**
- You need to navigate to a specific view in your app. Instead, use a custom scheme or universal link.
- The web page requires authentication or has Content Security Policy headers that block embedding.

## What you need for each link type

### Custom scheme deep links

| Requirement | Details |
|---|---|
| AASA file | Not required |
| `Info.plist` | Register your scheme under `CFBundleURLTypes` and add it to `LSApplicationQueriesSchemes` |
| App delegate method | Implement `application(_:open:options:)`, or `scene(_:openURLContexts:)` if your app uses scenes, to handle custom scheme links. This includes custom scheme links opened from Braze messages |
| Braze SDK configuration | None. The SDK opens custom scheme URLs by default unless `braze(_:shouldOpenURL:)` returns `false` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom scheme deep links" }

### Universal links

| Requirement | Details |
|---|---|
| AASA file | Required — host at `https://yourdomain.com/.well-known/apple-app-site-association` |
| Associated Domains | Add `applinks:yourdomain.com` in Xcode under **Signing & Capabilities** |
| App delegate method | Implement `application(_:continue:restorationHandler:)` to handle `NSUserActivity` |
| Braze SDK configuration | Set `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (optional) | Implement `braze(_:shouldOpenURL:)` for custom routing (for example, Branch) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Universal links" }

**Important:**


If you send emails through Braze, your ESP (SendGrid, SparkPost, or Amazon SES) wraps links in a click-tracking domain. You must host the AASA file on your click-tracking domain as well, not only on your primary domain. For complete setup, see [Universal links and App Links](https://www.braze.com/docs/user_guide/channels/email/customize/universal_links_and_app_links). If every email link opens the app, see [Every email link opens the app](https://www.braze.com/docs/developer_guide/push_notifications/deep_linking_troubleshooting#every-email-link-opens-the-app).



### "Open Web URL Inside App"

| Requirement | Details |
|---|---|
| AASA file | Not required |
| App delegate method | Not required — the SDK handles this automatically |
| Braze SDK configuration | None — select **Open Web URL Inside App** in the campaign composer |
{: .reset-td-br-1 .reset-td-br-2 aria-label=""Open Web URL Inside App"" }

## When you need an AASA file {#when-aasa}

An Apple App Site Association (AASA) file is only required when you use **universal links**. It tells iOS which URLs your app can handle.

You need an AASA file when:

- You send deep links in email campaigns (because ESPs wrap links in HTTPS click-tracking URLs).
- You send deep links in SMS campaigns (because links may be shortened to HTTPS URLs).
- You use Branch, AppsFlyer, or another linking provider (because they use their own HTTPS domains).
- You use universal links from push, in-app messages, or Content Cards (less common, but possible with `forwardUniversalLinks = true`).

You don't need an AASA file when:

- You only use custom scheme deep links (for example, `myapp://`) from push, in-app messages, Content Cards, or Banners.
- You use the **Open Web URL Inside App** option.

For AASA setup instructions, see [Universal links and App Links](https://www.braze.com/docs/user_guide/channels/email/customize/universal_links_and_app_links).

## When you need app code to handle links {#when-app-code}

Which delegate method you implement depends on the type of link you're using and whether you need custom routing logic:

| Delegate method | Handles | When to implement |
|---|---|---|
| `BrazeDelegate.braze(_:shouldOpenURL:)` | All URLs opened by the Braze SDK | You need custom routing logic (for example, Branch, conditional handling, analytics) for Braze messages |
| `application(_:open:options:)` or `scene(_:openURLContexts:)` | Custom scheme deep links (`myapp://`) | You use custom scheme deep links from any channel, including Braze messages |
| `application(_:continue:restorationHandler:)` | Universal links (`https://`) | You use universal links from email, SMS, or with `forwardUniversalLinks = true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="When you need app code to handle links #when-app-code" }

### BrazeDelegate.shouldOpenURL versus application open URL methods

For push notifications, in-app messages, Content Cards, and Banners, the Braze SDK calls `BrazeDelegate.braze(_:shouldOpenURL:)` before it opens the URL. The URL context includes the source channel. Use this method to:

- Route the URL to a third-party provider (for example, Branch or AppsFlyer) before Braze opens it
- Log analytics
- Return `false` so Braze does not open the URL

If you don't implement `shouldOpenURL`, the SDK default returns `true`, and Braze opens the URL. Custom scheme links open through the system, which calls your app's `scene(_:openURLContexts:)` or `application(_:open:options:)`. Web links open in a WebView or the browser, depending on the message settings.

If you implement `shouldOpenURL` and return `false`, handle the URL in that method. Braze does not open it and does not forward the URL to your application or scene delegate methods.

When Braze opens a custom scheme link, iOS calls `application(_:open:options:)`, or `scene(_:openURLContexts:)` if your app uses scenes. When `forwardUniversalLinks = true`, Braze passes universal links directly to `scene(_:continue:)` or `application(_:continue:restorationHandler:)`. If both are implemented, Braze calls only the scene delegate method.

## Using Branch with Braze {#branch}

If you use [Branch](https://www.braze.com/docs/partners/message_orchestration/deeplinking/branch_for_deeplinking) as your linking provider, your setup requires a few additional steps beyond a standard universal link configuration:

1. **Branch SDK**: Integrate the Branch SDK following [Branch's documentation](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Associated Domains**: Add your Branch domain (for example, `applinks:yourapp.app.link`) in Xcode under **Signing & Capabilities**.
3. **BrazeDelegate**: Implement `braze(_:shouldOpenURL:)` to route Branch links to the Branch SDK. Return `false` so Braze does not open the URL after you route it.
4. **Forward universal links**: Set `configuration.forwardUniversalLinks = true` in your Braze SDK configuration.

For implementation details and debugging guidance, see [Branch for deep linking](https://www.braze.com/docs/partners/message_orchestration/deeplinking/branch_for_deeplinking).

