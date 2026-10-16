# Auto-insert Banners with Web Targeting

> For web placements, you can optionally configure Web Targeting in the placement settings to specify where the Banner should appear on the page. When Web Targeting is configured, the Braze Web SDK inserts Banners at the specified location automatically rather than through an explicit call to `insertBanner()`. For more information, see [Web Targeting for Banners](https://www.braze.com/docs/user_guide/channels/banners/web_targeting). For background information on Banners and Banner placements, see [About Banners](https://www.braze.com/docs/developer_guide/banners) and [Manage placements](https://www.braze.com/docs/developer_guide/banners/placements).




**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





## Prerequisites

Because Web Targeting insertion adds HTML into your page, it requires the same opt-in as [`insertBanner`](https://www.braze.com/docs/developer_guide/banners/placements#insertBanner):

```javascript
braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  allowUserSuppliedJavascript: true, // required for Web Targeting auto-insert
});
```

Without `allowUserSuppliedJavascript: true`, auto-insertion is a no-op and the SDK logs an error.

## Triggering Web Targeting insertion

When called, the `insertWebTargetingBanners()` method attempts to use each Banner's Web Targeting information, if present, to find the intended spot for that Banner on the page and automatically insert it there. Call this method shortly after SDK initialization and after each completed Banner sync performed through the Web SDK.

If the Web SDK fails to find the targeted insertion spot for a Banner with Web Targeting information, it continuously retries to insert it. This allows Web Targeting to target portions of your page that may only appear after the initial page load. This retry behavior can be disabled when initializing the SDK using the `initialize()` method's `enableWebTargetingBannerRetryLoop` parameter.

```javascript
braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  allowUserSuppliedJavascript: true,
  enableWebTargetingBannerRetryLoop: false, // don't retry if the target isn't in the DOM yet
});
```

## Enable Web Targeting insertion upon Banner refreshes

If desired, you may call `automaticallyInsertWebTargetingBanners()` following SDK initialization. Invoking this method establishes a subscription that immediately performs Web Targeting insertion for the Banners present after the Web SDK completes a Banners sync. This resolves the need to call `insertWebTargetingBanners()`, but you can stick to just that method if you want finer-grained control over when Web Targeting insertion occurs. This method will not insert any Banners when called.

## Single-Page Apps (SPA) {#spa-considerations}

Note the following details if your website uses single-page app (SPA) architecture or similar systems (such as React Router or Vue) to handle page routing and navigation or if your website manually removes inserted Banners:

- If a Banner is inserted into the DOM with Web Targeting but later removed due to re-rendering upon routing, the Web SDK does not automatically attempt to re-insert it on the new page. Likewise, if the Banner remains after re-render but is URL-scoped to the previous route, the Web SDK does not automatically remove it from the DOM.
- Call `insertWebTargetingBanners()` after every client-side route render to invoke all the various bookkeeping logic orchestrated by the SDK. It only reinserts Banners that have a changed state, so it's safe to call on every navigation.

## Troubleshooting

Common reasons a Banner doesn't auto-insert, logged through the SDK's logger (`enableLogging: true`):

| Symptom | Likely cause |
|---|---|
| Nothing inserts anywhere, and the SDK logs "`allowUserSuppliedJavascript` is required" | `initialize()` was called without `allowUserSuppliedJavascript: true`. |
| The SDK logs "target element not found for selector" | The CSS selector doesn't match any element yet. If the element renders later, this resolves itself through the retry loop; otherwise, double-check the selector configured for the placement. |
| The SDK logs "cannot insert inside" an element | The Banner's Web Targeting information would have inserted it into an unsupported element, such as `video` or `img`. See [Web Targeting for Banners](https://www.braze.com/docs/user_guide/channels/banners/web_targeting). |
| A Banner inserts once but doesn't update on route changes | See [SPA considerations](#spa-considerations)—call `insertWebTargetingBanners()` after each client-side route render. |
| A Banner disappears after a framework re-render | See [SPA considerations](#spa-considerations). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web Targeting troubleshooting" }

## Next steps

- [Web Targeting for Banners](https://www.braze.com/docs/user_guide/channels/banners/web_targeting) — how company users configure CSS selector, insertion position, and URL targeting for a placement in the dashboard.
- [Manage placements](https://www.braze.com/docs/developer_guide/banners/placements) — create placements, refresh them, and display Banners manually with `insertBanner`.
- [Banners: Frequently Asked Questions](https://www.braze.com/docs/developer_guide/banners/faq)

**Tip:**


Want to help prioritize what's next for Web Targeting? Contact [banners-feedback@braze.com](mailto:banners-feedback@braze.com).


