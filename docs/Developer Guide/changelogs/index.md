# Braze SDK changelogs

> This reference page includes the changelogs for each Braze SDK and a link to the changelog in their public GitHub repository. For the full list of resources, see [References, Repositories, and Sample Apps](https://www.braze.com/docs/developer_guide/references/).



**Tip:**


You can also find a copy of the [Web Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).



<h2 id="671">6.7.1</h2>

<h5 id="fixed">Fixed</h5>
<ul>
  <li>Fixed an issue where Braze pushes were not displayed properly.</li>
</ul>

<h2 id="670---deprecated">6.7.0 - DEPRECATED</h2>

<h5 id="added">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">brazeBridge.closeMessage()</code> support for Banners. Calling this method will remove the Banner from the page and log a dismissal event.</li>
  <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh"><code class="language-plaintext highlighter-rouge">braze.requestBannersRefresh()</code></a> no longer requires the <code class="language-plaintext highlighter-rouge">allowUserSuppliedJavascript</code> initialization option to be enabled.</li>
</ul>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Fixed an issue with the CDN integration on Safari 26+ that could cause messaging sync requests to fail in certain scenarios.</li>
  <li>Fixed an issue where the Braze SDK would attempt to display push notifications sent from other push providers</li>
</ul>

<h2 id="660">6.6.0</h2>

<h5 id="added-1">Added</h5>
<ul>
  <li>Added a <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions"><code class="language-plaintext highlighter-rouge">cookieExpiryInDays</code></a> initialization option to configure cookie duration from the default of 400 days.</li>
</ul>

<h2 id="650">6.5.0</h2>

<h5 id="added-2">Added</h5>
<ul>
  <li>Added the <code class="language-plaintext highlighter-rouge">Banner.html</code> property to support manually injecting HTML for cases where <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner"><code class="language-plaintext highlighter-rouge">insertBanner</code></a> is not appropriate.</li>
</ul>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Improved request retry timing to prefer server-configurable values for resiliency and consistency with other Braze SDKs</li>
</ul>

<h2 id="640">6.4.0</h2>

<h5 id="added-3">Added</h5>
<ul>
  <li>Added methods <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerimpressions"><code class="language-plaintext highlighter-rouge">braze.logBannerImpressions()</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerclick"><code class="language-plaintext highlighter-rouge">braze.logBannerClick()</code></a> to allow integrators to manually log both the banner impression and click events. These methods should only be called if you’re bypassing <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner"><code class="language-plaintext highlighter-rouge">insertBanner</code></a> and building custom UI for banners similar to other channels.</li>
</ul>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Fixed an issue where In-App Messages for the previous user were still displayed after changing users.</li>
</ul>

<h2 id="631">6.3.1</h2>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Fixed an issue where banner impressions were not cleared from local storage when a new session was opened.</li>
</ul>

<h2 id="630">6.3.0</h2>

<h5 id="added-4">Added</h5>
<ul>
  <li>Exposed <code class="language-plaintext highlighter-rouge">NotificationSubscriptionTypes</code> in <code class="language-plaintext highlighter-rouge">brazeBridge</code>.</li>
  <li>Added support for detection of ChatGPT Atlas browser.</li>
  <li>Improved crawler bot detection.</li>
</ul>

<h2 id="620">6.2.0</h2>

<h5 id="added-5">Added</h5>
<ul>
  <li>Updated platform detection for the <code class="language-plaintext highlighter-rouge">Coolita</code> and <code class="language-plaintext highlighter-rouge">WhaleTV</code> Smart TV platforms, which are now classified as <code class="language-plaintext highlighter-rouge">Other Smart TV</code>.</li>
</ul>

<h2 id="610">6.1.0</h2>

<h5 id="added-6">Added</h5>
<ul>
  <li>Added support for <a href="https://js.appboycdn.com/web-sdk-develop/latest/doc/classes/braze.banner.html"><code class="language-plaintext highlighter-rouge">Banner</code></a> properties.</li>
</ul>

<h5 id="changed">Changed</h5>
<ul>
  <li>The default client-side rate limiting value for Banners refresh has been increased. For more information on SDK rate limiting, please refer to the <a href="https://www.braze.com/docs/developer_guide/sdk_integration/rate_limits#braze-sdk-rate-limits">Braze Developer Guide</a></li>
</ul>

<h5 id="fixed-5">Fixed</h5>
<ul>
  <li>Fixed an issue where Banner serialization keys were inconsistent between SDK versions, which could cause Banners to display incorrectly until the first Banners refresh after a version upgrade.</li>
  <li>Fixed an issue where PetalBot and Meta web crawlers were not properly detected.</li>
</ul>

<h2 id="600">6.0.0</h2>

<h5 id="️-breaking">⚠️ Breaking</h5>
<ul>
  <li>Removed the <code class="language-plaintext highlighter-rouge">Banner.html</code> property, <code class="language-plaintext highlighter-rouge">logBannerClick</code>, and <code class="language-plaintext highlighter-rouge">logBannerImpressions</code> methods. Instead, use <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner"><code class="language-plaintext highlighter-rouge">insertBanner</code></a> which automatically handles impression and click tracking.</li>
  <li>Removed support for the legacy News Feed feature.
This includes removal of the <code class="language-plaintext highlighter-rouge">Feed</code> class, and the following associated methods:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">destroyFeed()</code></li>
      <li><code class="language-plaintext highlighter-rouge">getCachedFeed()</code></li>
      <li><code class="language-plaintext highlighter-rouge">logFeedDisplayed()</code></li>
      <li><code class="language-plaintext highlighter-rouge">requestFeedRefresh()</code></li>
      <li><code class="language-plaintext highlighter-rouge">showFeed()</code></li>
      <li><code class="language-plaintext highlighter-rouge">subscribeToFeedUpdates()</code></li>
      <li><code class="language-plaintext highlighter-rouge">toggleFeed()</code></li>
      <li><code class="language-plaintext highlighter-rouge">logCardClick()</code> (replaced by <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick"><code class="language-plaintext highlighter-rouge">logContentCardClick()</code></a>)</li>
      <li><code class="language-plaintext highlighter-rouge">logCardImpressions()</code> (replaced by <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions"><code class="language-plaintext highlighter-rouge">logContentCardImpressions()</code></a>)</li>
    </ul>
  </li>
  <li>The <code class="language-plaintext highlighter-rouge">created</code> and <code class="language-plaintext highlighter-rouge">categories</code> fields that were used by legacy News Feed cards have been removed from <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html"><code class="language-plaintext highlighter-rouge">Card</code></a> subclasses.</li>
  <li>The <code class="language-plaintext highlighter-rouge">linkText</code> field was also removed from the <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html"><code class="language-plaintext highlighter-rouge">ImageOnly</code></a> Card subclass and its constructor.</li>
  <li>Clarified definitions and updated types to note that certain SDK methods explicitly return <code class="language-plaintext highlighter-rouge">undefined</code> when the SDK is not initialized, aligning the typings with actual runtime behavior. This could introduce new TypeScript errors in projects that relied on the previous (incomplete) typings.</li>
  <li>The images of In-App Messages with <code class="language-plaintext highlighter-rouge">cropType</code> of <code class="language-plaintext highlighter-rouge">CENTER_CROP</code> (e.g. <code class="language-plaintext highlighter-rouge">FullScreenMessage</code> by default) are now rendered via an <code class="language-plaintext highlighter-rouge">&lt;img&gt;</code> tag instead of <code class="language-plaintext highlighter-rouge">&lt;span&gt;</code> for improved accessibility. This may break existing CSS customizations for the <code class="language-plaintext highlighter-rouge">.ab-center-cropped-img</code> class or its children.</li>
</ul>

<h5 id="added-7">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">imageAltText</code> and <code class="language-plaintext highlighter-rouge">language</code> fields to the following classes:
    <ul>
      <li>Cards: <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html"><code class="language-plaintext highlighter-rouge">CaptionedImage</code></a>, <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html"><code class="language-plaintext highlighter-rouge">ImageOnly</code></a>, and [<code class="language-plaintext highlighter-rouge">ClassicCard</code>]</li>
      <li>In-App Messages: <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html"><code class="language-plaintext highlighter-rouge">ModalMessage</code></a>, <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html"><code class="language-plaintext highlighter-rouge">FullScreenMessage</code></a>, and <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html"><code class="language-plaintext highlighter-rouge">SlideUpMessage</code></a></li>
    </ul>
  </li>
  <li>When available, the default UI will use these fields to set the alternate text of images and the <code class="language-plaintext highlighter-rouge">lang</code> attribute, respectively, of In-App Messages and Cards.</li>
  <li>Improved the accessibility of In-App Messages and Content Cards when displayed by the default UI.</li>
</ul>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>Any new session subscriptions now immediately invoke the callback if a new session has already started.</li>
</ul>

<h5 id="fixed-6">Fixed</h5>
<ul>
  <li>Subscription methods now correctly trigger refreshes when <code class="language-plaintext highlighter-rouge">openSession()</code> is called, even if <code class="language-plaintext highlighter-rouge">changeUser()</code> was called first.</li>
  <li>Fixed an issue where Banners could display with a small amount of whitespace at the bottom.</li>
  <li>Fixed an issue where the <code class="language-plaintext highlighter-rouge">messageExtras</code> field was missing from the type definitions of InAppMessage classes.</li>
</ul>

<h2 id="591">5.9.1</h2>

<h5 id="fixed-7">Fixed</h5>
<ul>
  <li>Fixed an issue where rate limit state persisted across users and sessions causing requests to be incorrectly rate limited at session start.</li>
</ul>

<h2 id="590">5.9.0</h2>

<h5 id="added-8">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">brazeBridge.setBannerHeight()</code> to allow Banners to resize dynamically.</li>
</ul>

<h5 id="fixed-8">Fixed</h5>
<ul>
  <li>Fixed an edge case with retry logic for Feature Flags, Content Cards and Banners network requests.</li>
</ul>

<h2 id="581">5.8.1</h2>

<h5 id="fixed-9">Fixed</h5>
<ul>
  <li>Fixed an issue with the npm version of the Web SDK that prevented Banner clicks from being logged.</li>
</ul>

<h2 id="580">5.8.0</h2>

<h5 id="changed-2">Changed</h5>
<ul>
  <li>The <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner"><code class="language-plaintext highlighter-rouge">insertBanner</code></a> method now accepts a <code class="language-plaintext highlighter-rouge">null</code> or <code class="language-plaintext highlighter-rouge">undefined</code> banner argument.</li>
  <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh"><code class="language-plaintext highlighter-rouge">requestBannersRefresh</code></a> now waits for the initial response from the backend and tries again if Banners are enabled.</li>
</ul>

<h5 id="fixed-10">Fixed</h5>
<ul>
  <li>Fixed a race condition causing “not enabled” messages to be logged for Banners and Feature Flags methods on the user’s first session.</li>
</ul>

<h2 id="570">5.7.0</h2>

<h5 id="added-9">Added</h5>
<ul>
  <li>Added a method <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlineid"><code class="language-plaintext highlighter-rouge">User.setLineId</code></a> used to set the user’s <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/line">LINE</a> User ID.</li>
</ul>

<h5 id="fixed-11">Fixed</h5>
<ul>
  <li>Fixed an issue where the chevron icon pointed in the wrong direction on SlideUp in-app messages when using RTL languages.</li>
</ul>

<h5 id="changed-3">Changed</h5>
<ul>
  <li>The SDK now respects the <code class="language-plaintext highlighter-rouge">retry-after</code> header returned by the Braze platform when determining how long to wait before retrying a request.</li>
</ul>

<h2 id="561">5.6.1</h2>

<h5 id="fixed-12">Fixed</h5>
<ul>
  <li>Fixed an issue where the Tizen operating system was not accurately reported in device properties.</li>
</ul>

<h2 id="560">5.6.0</h2>

<h5 id="added-10">Added</h5>
<ul>
  <li>Added support for the Banners campaign type.</li>
</ul>

<h5 id="fixed-13">Fixed</h5>
<ul>
  <li>Fixed an issue where the SDK could erroneously request a triggers refresh even if no session is started.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">ControlMessage</code> instances would allow multiple impressions.</li>
</ul>

<h2 id="550">5.5.0</h2>

<h5 id="changed-4">Changed</h5>
<ul>
  <li>The SDK now rate limits Content Cards impressions to correspond to expected human behavior.</li>
</ul>

<h2 id="540">5.4.0</h2>

<h5 id="added-11">Added</h5>
<ul>
  <li>Added support for right-to-left languages to the built-in UI for In-App Messages and Content Cards.</li>
  <li>Introduced a new initialization option <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions"><code class="language-plaintext highlighter-rouge">serviceWorkerScope</code></a> that can be used to override the default scope of the service worker.</li>
  <li>Added a method <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#isinitialized"><code class="language-plaintext highlighter-rouge">braze.isInitialized()</code></a> that returns whether the SDK has been initialized.</li>
  <li>Added a new custom event named <code class="language-plaintext highlighter-rouge">braze.initialized</code> that is dispatched on the <code class="language-plaintext highlighter-rouge">window</code> object when the Braze initialization completes.</li>
</ul>

<h2 id="532">5.3.2</h2>

<h5 id="fixed-14">Fixed</h5>
<ul>
  <li>Fixed a regression introduced in 5.2.0 that could cause HTML In-App Messages to render incorrectly when an external script is loaded synchronously.</li>
</ul>

<h2 id="531">5.3.1</h2>

<h5 id="fixed-15">Fixed</h5>
<ul>
  <li>Fixed an issue where a custom <code class="language-plaintext highlighter-rouge">serviceWorkerLocation</code> was not used when calling <code class="language-plaintext highlighter-rouge">unregisterPush</code>.</li>
</ul>

<h2 id="530">5.3.0</h2>

<h5 id="added-12">Added</h5>
<ul>
  <li>Added the following methods to the <code class="language-plaintext highlighter-rouge">FeatureFlag</code> class to support the upcoming expansion of feature flag property types:
    <ul>
      <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.featureflag.html#getjsonproperty"><code class="language-plaintext highlighter-rouge">getJsonProperty()</code></a></li>
      <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.featureflag.html#getimageproperty"><code class="language-plaintext highlighter-rouge">getImageProperty()</code></a></li>
      <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.featureflag.html#gettimestampproperty"><code class="language-plaintext highlighter-rouge">getTimestampProperty()</code></a></li>
    </ul>
  </li>
</ul>

<h5 id="fixed-16">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">e.preventDefault()</code> could be called on events that were not cancelable.</li>
</ul>

<h2 id="520">5.2.0</h2>

<h5 id="added-13">Added</h5>
<ul>
  <li>Added a <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions"><code class="language-plaintext highlighter-rouge">deviceId</code></a> initialization option. This can be used to set device ID of the user that would be used after initialization.</li>
  <li>Added support for the <code class="language-plaintext highlighter-rouge">message_extras</code> liquid tag for in-app messages.</li>
</ul>

<h5 id="changed-5">Changed</h5>
<ul>
  <li>The SDK will now persist and send the user’s alias in all backend requests if it has been set, until the user is identified via an external ID. This alias will no longer be sent in requests once the user is identified and is not compatible with SDK authentication.</li>
  <li>The SDK will now check for existing permissions before requesting push permissions.</li>
</ul>

<h5 id="fixed-17">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">unregisterPush()</code> failed to invoke the <code class="language-plaintext highlighter-rouge">successCallback()</code> function in some cases where the user has already unsubscribed to push.</li>
  <li>Fixed an issue where characters <code class="language-plaintext highlighter-rouge">|</code> and <code class="language-plaintext highlighter-rouge">:</code> were not supported in the <code class="language-plaintext highlighter-rouge">userId</code>.</li>
  <li>Fixed an issue where HTML In-App Messages that used module script tags were not supported.</li>
</ul>

<h2 id="511">5.1.1</h2>

<h5 id="fixed-18">Fixed</h5>
<ul>
  <li>Fixed an issue where content cards sync request count persisted across users causing requests to be incorrectly rate limited.</li>
</ul>

<h2 id="510">5.1.0</h2>

<h5 id="changed-6">Changed</h5>
<ul>
  <li>The <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetofeatureflagsupdates"><code class="language-plaintext highlighter-rouge">subscribeToFeatureFlagsUpdates()</code></a> callback will be triggered first with cached feature flags only if this cache is from the current session.</li>
</ul>

<h5 id="fixed-19">Fixed</h5>
<ul>
  <li>Fixed an issue where in-app messages failed to render a transparent background when using color-scheme.</li>
  <li>Fixed an issue where impressions for a given feature flag ID were limited to once-per-user instead of once-per-session.</li>
</ul>

<h2 id="501">5.0.1</h2>

<h5 id="fixed-20">Fixed</h5>
<ul>
  <li>Fixed a bug where toggling <code class="language-plaintext highlighter-rouge">noCookies</code> initialization option from true to false did not create all the necessary cookies.</li>
  <li>Fixed an issue where user attributes could not be nulled out by setting a specific null value.</li>
</ul>

<h2 id="500">5.0.0</h2>

<h5 id="️-breaking-1">⚠️ Breaking</h5>
<ul>
  <li>The <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetofeatureflagsupdates"><code class="language-plaintext highlighter-rouge">subscribeToFeatureFlagsUpdates()</code></a> callback will now always be called, regardless of refresh success/failure. If there is a failure in receiving updates, the callback will be called with currently cached feature flags.</li>
  <li>The <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getfeatureflag"><code class="language-plaintext highlighter-rouge">getFeatureFlag()</code></a> method now returns a null if the feature flag does not exist, or if feature flags are disabled.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">logContentCardsDisplayed()</code> method that was previously deprecated in 4.0.4.</li>
  <li>Removed the deprecated initialization option <code class="language-plaintext highlighter-rouge">enableHtmlInAppMessages</code>. This should be replaced with the <code class="language-plaintext highlighter-rouge">allowUserSuppliedJavascript</code> option instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">Banner</code> class that was previously deprecated in 4.9.0 in favor of <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html"><code class="language-plaintext highlighter-rouge">ImageOnly</code></a>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">ab-banner</code> CSS classname as part of <code class="language-plaintext highlighter-rouge">Banner</code> class removal. CSS customizations should instead target the <code class="language-plaintext highlighter-rouge">ab-image-only</code> class.</li>
  <li>The SDK no longer throws runtime errors anywhere. If Braze methods are called prior to initialization, a warning will be logged to the console instead.</li>
  <li>The SDK no longer adds default Braze in-app message styles to custom HTML in-app messages. These styles were previously used by legacy in-app message types.</li>
</ul>

<h2 id="4102">4.10.2</h2>

<h5 id="fixed-21">Fixed</h5>
<ul>
  <li>Fixed a CSS templating issue in the npm version of the SDK introduced in 4.10.1 that caused in-app messages to display without the expected styles when using Braze built-in UI.</li>
</ul>

<h2 id="4101">4.10.1</h2>

<h5 id="fixed-22">Fixed</h5>
<ul>
  <li>Fixed an issue where user attributes could not be nulled out by setting a specific null value.</li>
</ul>

<h2 id="4100">4.10.0</h2>

<h5 id="added-14">Added</h5>
<ul>
  <li>Added a new <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions"><code class="language-plaintext highlighter-rouge">appVersionNumber</code></a> initialization option for <a href="https://www.braze.com/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/">targeting via numerical comparison</a>.</li>
</ul>

<h5 id="changed-7">Changed</h5>
<ul>
  <li>The SDK now ensures that cached messages for user (content cards, deferred in-app message, and feature flags) are cleared upon <code class="language-plaintext highlighter-rouge">changeUser()</code>.</li>
  <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeviceid"><code class="language-plaintext highlighter-rouge">getDeviceId</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#getuserid"><code class="language-plaintext highlighter-rouge">getUserId</code></a> now return results directly. Their callback parameters are deprecated and will be removed in a future major version.</li>
</ul>

<h2 id="490">4.9.0</h2>

<h5 id="added-15">Added</h5>
<ul>
  <li>Introduced a new <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html"><code class="language-plaintext highlighter-rouge">ImageOnly</code></a> Card subclass, which has the same functionality as the <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.banner.html"><code class="language-plaintext highlighter-rouge">Banner</code></a> class.</li>
  <li>Added a new <code class="language-plaintext highlighter-rouge">ab-image-only</code> CSS class to <code class="language-plaintext highlighter-rouge">Banner</code> and <code class="language-plaintext highlighter-rouge">ImageOnly</code> cards when displayed through the built-in UI. New CSS customizations should target this class. The <code class="language-plaintext highlighter-rouge">ab-banner</code> classname will remain on both card types until the <code class="language-plaintext highlighter-rouge">Banner</code> class is removed in a future release.</li>
  <li>Introduced two new methods <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage"><code class="language-plaintext highlighter-rouge">deferInAppMessage()</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage"><code class="language-plaintext highlighter-rouge">getDeferredInAppMessage()</code></a> that can be used together to delay the display of an in-app message for a future pageload.
    <ul>
      <li>[<code class="language-plaintext highlighter-rouge">deferInAppMessage()</code>] method defers the given in-app message.</li>
      <li>The deferred in-app message can be retrieved by calling the  [<code class="language-plaintext highlighter-rouge">getDeferredInAppMessage</code>] method.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-8">Changed</h5>
<ul>
  <li>Deprecated the <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.banner.html"><code class="language-plaintext highlighter-rouge">Banner</code></a> class.</li>
</ul>

<h5 id="fixed-23">Fixed</h5>
<ul>
  <li>Fixed an issue where in-app messages with images would fail to display when a parent node is supplied to <code class="language-plaintext highlighter-rouge">showInAppMessage()</code> and the parent node has not been attached to the DOM before the display callback is invoked.</li>
  <li>Fixed an issue where the callbacks passed to <code class="language-plaintext highlighter-rouge">requestContentCardsRefresh()</code> were sometimes not triggered when this call was queued behind another <code class="language-plaintext highlighter-rouge">requestContentCardsRefresh()</code> or <code class="language-plaintext highlighter-rouge">subscribeToContentCardsUpdates()</code> request.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">dismissCard()</code> did not work as expected on cached content cards.</li>
  <li>Fixed an issue where calling <code class="language-plaintext highlighter-rouge">destroy()</code> soonafter <code class="language-plaintext highlighter-rouge">wipeData()</code> incorrectly created a device ID cookie.</li>
</ul>

<h2 id="483">4.8.3</h2>

<h5 id="fixed-24">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">manageServiceWorkerExternally</code> initialization option failed to register service-worker when trying to register from a path higher than the service-worker location.</li>
</ul>

<h2 id="482">4.8.2</h2>

<h5 id="fixed-25">Fixed</h5>
<ul>
  <li>Fixed an issue where slow / failed image loading prevents subsequent in-app messages from displaying.</li>
  <li>Fixed a regression introduced in 4.8.0 where push notifications failed to display in Safari versions &lt;= 15.</li>
</ul>

<h2 id="481">4.8.1</h2>

<h5 id="fixed-26">Fixed</h5>
<ul>
  <li>Fixed an issue where content cards were sometimes not marked as read upon card impression.</li>
  <li>Improved the typings for the <code class="language-plaintext highlighter-rouge">isControl</code> field on In-App Message and Card classes.</li>
</ul>

<h2 id="480">4.8.0</h2>

<h5 id="changed-9">Changed</h5>
<ul>
  <li>The <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetofeatureflagsupdates"><code class="language-plaintext highlighter-rouge">subscribeToFeatureFlagsUpdates</code></a> callback will now always be called first with the currently cached feature flags, and when feature flag updates are available.</li>
</ul>

<h5 id="fixed-27">Fixed</h5>
<ul>
  <li>Fixed the return type for <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates"><code class="language-plaintext highlighter-rouge">subscribeToContentCardsUpdates()</code></a>.</li>
  <li>Fixed the return type for <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetofeatureflagsupdates"><code class="language-plaintext highlighter-rouge">subscribeToFeatureFlagsUpdates()</code></a>.</li>
  <li>Improved type definitions in Card, InAppMessage and InAppMessageButton classes:
    <ul>
      <li>Fixed return types for <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#subscribetoclickedevent"><code class="language-plaintext highlighter-rouge">Card.subscribeToClickedEvent()</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#subscribetodismissedevent"><code class="language-plaintext highlighter-rouge">Card.subscribeToDismissedEvent()</code></a>.</li>
      <li>Fixed return types for <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html#subscribetoclickedevent"><code class="language-plaintext highlighter-rouge">InAppMessage.subscribeToClickedEvent()</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html#subscribetodismissedevent"><code class="language-plaintext highlighter-rouge">InAppMessage.subscribeToDismissedEvent()</code></a>.</li>
      <li>Fixed return type for <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessagebutton.html#subscribetoclickedevent"><code class="language-plaintext highlighter-rouge">InAppMessageButton.subscribeToClickedEvent()</code></a>.</li>
      <li>Fixed type definition of <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html#extras"><code class="language-plaintext highlighter-rouge">InAppMessage.extras</code></a>.</li>
    </ul>
  </li>
</ul>

<h2 id="472">4.7.2</h2>

<h5 id="fixed-28">Fixed</h5>
<ul>
  <li>Fixed a regression with the noCookies option which caused some localStorage keys to be persisted in cookie storage.</li>
</ul>

<h2 id="471">4.7.1</h2>

<h5 id="fixed-29">Fixed</h5>
<ul>
  <li>Improved the type definition of <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html"><code class="language-plaintext highlighter-rouge">Card.extras</code></a>.</li>
  <li>Fixed a regression introduced in 4.0.0 where the <code class="language-plaintext highlighter-rouge">manageServiceWorkerExternally</code> and <code class="language-plaintext highlighter-rouge">disablePushTokenMaintenance</code> initialization options could not work as expected.</li>
</ul>

<h2 id="470">4.7.0</h2>

<h5 id="added-16">Added</h5>
<ul>
  <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setcustomuserattribute"><code class="language-plaintext highlighter-rouge">User.setCustomUserAttribute</code></a> now accepts nested custom attributes and arrays of objects.
    <ul>
      <li>Adds a <code class="language-plaintext highlighter-rouge">merge</code> parameter that specifies whether the value should be merged with the existing value on the backend. If <code class="language-plaintext highlighter-rouge">false</code> (default), any existing attribute will be overwritten. If <code class="language-plaintext highlighter-rouge">true</code>, existing objects and arrays of objects will be merged. To update an array of objects, follow the guidelines in our <a href="https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/#usage-examples">public docs</a>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-30">Fixed</h5>
<ul>
  <li>Fixed an issue where <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission"><code class="language-plaintext highlighter-rouge">requestPushPermission</code></a> did not call the <code class="language-plaintext highlighter-rouge">deniedCallback</code> if the SDK encountered certain errors when registering push.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">requestPushPermission</code> did not log a message if push is not supported on the user’s browser.</li>
  <li>Fixed an incorrect typing in <code class="language-plaintext highlighter-rouge">subscribeToSdkAuthenticationFailures</code>.</li>
</ul>

<h2 id="463">4.6.3</h2>

<h5 id="fixed-31">Fixed</h5>
<ul>
  <li>Fixed an issue preventing Feature Flags refreshes when SDK Authentication errors occur.</li>
</ul>

<h2 id="462">4.6.2</h2>

<h5 id="changed-10">Changed</h5>
<ul>
  <li>Removed legacy email capture CSS. This is not a breaking change, as all existing web email capture campaigns have been migrated to the new universal email capture type on the Braze backend. This change results in ~1KB size reduction for those using the built-in In-App Message UI.</li>
</ul>

<h2 id="461">4.6.1</h2>

<h5 id="fixed-32">Fixed</h5>
<ul>
  <li>Improved the type definition of <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.featureflag.html"><code class="language-plaintext highlighter-rouge">FeatureFlag.properties</code></a>.</li>
</ul>

<h2 id="460">4.6.0</h2>

<h5 id="added-17">Added</h5>
<ul>
  <li>Added a method <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick"><code class="language-plaintext highlighter-rouge">braze.logContentCardClick()</code></a> to log that the user clicked on the given Content Card. This method is equivalent to calling <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcardclick"><code class="language-plaintext highlighter-rouge">braze.logCardClick()</code></a> with parameter <code class="language-plaintext highlighter-rouge">forContentCards = true</code>.</li>
  <li>Added support for the upcoming Braze Feature Flags product.</li>
</ul>

<h5 id="changed-11">Changed</h5>
<ul>
  <li>Improved the check for duplicate in-app messages at display time.</li>
</ul>

<h2 id="451">4.5.1</h2>

<h5 id="fixed-33">Fixed</h5>
<ul>
  <li>Fixed an issue where sites with globally-scoped <code class="language-plaintext highlighter-rouge">svg</code> and <code class="language-plaintext highlighter-rouge">img</code> CSS caused certain elements of the built-in UI to display incorrectly.</li>
</ul>

<h2 id="450">4.5.0</h2>

<h5 id="added-18">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">isControl</code> property to <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html"><code class="language-plaintext highlighter-rouge">ContentCard</code></a> base model, to easily determine whether the card is a control card.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">isControl</code> property to <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html"><code class="language-plaintext highlighter-rouge">InAppMessage</code></a> base model, to easily determine whether the message is a control in-app-message.</li>
</ul>

<h5 id="changed-12">Changed</h5>
<ul>
  <li>Improved the reliability of in-app message impression logging in edge cases.</li>
</ul>

<h2 id="440">4.4.0</h2>

<h5 id="added-19">Added</h5>
<ul>
  <li>A message is now logged if an IAM is triggered but not displayed because neither <code class="language-plaintext highlighter-rouge">automaticallyShowInAppMessages()</code> nor <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage()</code> were called.</li>
</ul>

<h5 id="changed-13">Changed</h5>
<ul>
  <li>IndexedDB connections now close after a transaction has been completed.</li>
</ul>

<h5 id="fixed-34">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 4.0.0 where In-App Message closing animations did not work as expected.</li>
</ul>

<h2 id="430">4.3.0</h2>

<h5 id="added-20">Added</h5>
<ul>
  <li>Added <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages/#bridge"><code class="language-plaintext highlighter-rouge">brazeBridge.changeUser(id: string, sdkAuthSignature?: string)</code></a> to HTML In-App Messages.</li>
  <li>Added the ability to include a custom pathname in the <code class="language-plaintext highlighter-rouge">baseUrl</code> <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions">initialization option</a>.</li>
</ul>

<h2 id="421">4.2.1</h2>

<h5 id="fixed-35">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 4.0.3, where IAM displays could sometimes fail due to an internal race condition.</li>
</ul>

<h2 id="420">4.2.0</h2>

<h5 id="added-21">Added</h5>
<ul>
  <li>Added support for Content Cards to evaluate Retry-After headers.</li>
</ul>

<h2 id="410">4.1.0</h2>

<h5 id="added-22">Added</h5>
<ul>
  <li>Added a method <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions"><code class="language-plaintext highlighter-rouge">braze.logContentCardImpressions()</code></a> to log that the user saw the given Content Cards. This method is equivalent to calling <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcardimpressions"><code class="language-plaintext highlighter-rouge">braze.logCardImpressions()</code></a> with parameter <code class="language-plaintext highlighter-rouge">forContentCards = true</code>.</li>
</ul>

<h5 id="fixed-36">Fixed</h5>
<ul>
  <li>Fixed an issue where calling <code class="language-plaintext highlighter-rouge">unregisterPush()</code> when the user is already unregistered would fail to execute the success callback function.</li>
</ul>

<h2 id="406">4.0.6</h2>

<h5 id="fixed-37">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 4.0.0 that incorrectly failed to display valid IAMs with an unknown Braze Action type error.</li>
</ul>

<h2 id="405">4.0.5</h2>

<h5 id="fixed-38">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 4.0.0 that prevented the SDK from running with certain rollup.js configurations.</li>
</ul>

<h2 id="404">4.0.4</h2>

<h5 id="changed-14">Changed</h5>
<ul>
  <li>Deprecated and changed the obsolete <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardsdisplayed">logContentCardsDisplayed</a> method to a no-op. Card impressions should be logged using <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcardimpressions">logCardImpressions</a>.</li>
</ul>

<h5 id="fixed-39">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 4.0.0 that prevented control in-app message impressions from being logged.</li>
</ul>

<h2 id="403">4.0.3</h2>

<h5 id="fixed-40">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 4.0.0 where Safari push did not work unless the full <code class="language-plaintext highlighter-rouge">baseUrl</code> (e.g. <code class="language-plaintext highlighter-rouge">https://sdk.iad-01.braze.com/api/v3</code>) was specified in the initialization options.</li>
  <li>The SDK will now ignore In-App Messages containing a push prompt Braze Action for users who have already registered for push or whose browser does not support push.</li>
</ul>

<h2 id="402">4.0.2</h2>

<h5 id="changed-15">Changed</h5>
<ul>
  <li>Cookies set by the Braze Web SDK now expire after 400 days per the recommendation of the <a href="https://httpwg.org/http-extensions/draft-ietf-httpbis-rfc6265bis.html#section-4.1.2.2">HTTP Working Group’s draft RFC 6265</a></li>
</ul>

<h5 id="fixed-41">Fixed</h5>
<ul>
  <li>Removed usages of the nullish coalescing operator for better compatibility with various webpack configurations.</li>
</ul>

<h2 id="401">4.0.1</h2>

<h5 id="fixed-42">Fixed</h5>
<ul>
  <li>The <code class="language-plaintext highlighter-rouge">created</code> field is now set for <code class="language-plaintext highlighter-rouge">Card</code> objects when using Content Cards.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">"type": "module"</code> to the package.json so frameworks like Next.js recognize the SDK as an ES Module.</li>
</ul>

<h2 id="400">4.0.0</h2>

<h5 id="️-breaking-2">⚠️ Breaking</h5>
<ul>
  <li>See our <a href="https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md">upgrade guide</a> for more information on how to migrate from v3.</li>
  <li>The <code class="language-plaintext highlighter-rouge">appboy-web-sdk</code>, <code class="language-plaintext highlighter-rouge">@braze/web-sdk-core</code>, and <code class="language-plaintext highlighter-rouge">@braze/web-sdk-no-amd</code> npm packages are deprecated in favor of the <code class="language-plaintext highlighter-rouge">@braze/web-sdk</code> package and will no longer receive updates.</li>
  <li>The SDK’s exported object has been renamed from <code class="language-plaintext highlighter-rouge">appboy</code> to <code class="language-plaintext highlighter-rouge">braze</code>. CDN users must update their loading snippet when upgrading to 4.0.</li>
  <li>The file name for the bundled version of the SDK has changed to <code class="language-plaintext highlighter-rouge">braze.min.js</code>. CDN users must ensure that the URL points to this new file name when upgrading to 4.0.</li>
  <li>The Braze Web SDK now supports importing individual features and methods as native ES Modules that can be tree-shaken. For example, if you only use In-App Messages with a custom UI, you can now import our <code class="language-plaintext highlighter-rouge">InAppMessage</code> classes and <code class="language-plaintext highlighter-rouge">subscribeToInAppMesssage()</code> and Javascript module bundlers such as webpack will remove any unused code. If you prefer to continue using a compiled version of the SDK, it can be found through our CDN.</li>
  <li>The prefix for SDK logs has changed from <code class="language-plaintext highlighter-rouge">Appboy</code> to <code class="language-plaintext highlighter-rouge">Braze</code>. If you use the <code class="language-plaintext highlighter-rouge">Appboy</code> prefix as a filter in your logging tools, you should update it to include <code class="language-plaintext highlighter-rouge">Braze</code>.</li>
  <li>As a result of the above changes, many of our method signatures have changed. See our <a href="https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md">upgrade guide</a> for more information on how to migrate.</li>
  <li>Dropped support for Internet Explorer.</li>
</ul>

<h5 id="changed-16">Changed</h5>
<ul>
  <li>Updated default z-index of <code class="language-plaintext highlighter-rouge">InAppMessage</code> to 9001. This can be still be overwritten using the <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions">inAppMessageZIndex</a> initialization option.</li>
</ul>

<h5 id="added-23">Added</h5>
<ul>
  <li>Introduced support for the new Braze Actions feature. When displaying In-App Messages and Content Cards through our built-in UI, this feature requires no additional code.</li>
  <li>Added <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction"><code class="language-plaintext highlighter-rouge">braze.handleBrazeAction()</code></a> to handle Braze Action URLs when using a custom UI.</li>
</ul>

<h2 id="351">3.5.1</h2>

<h5 id="changed-17">Changed</h5>
<ul>
  <li>Added Shopify to <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.brazesdkmetadata.html"><code class="language-plaintext highlighter-rouge">BrazeSdkMetadata</code></a></li>
</ul>

<h2 id="350">3.5.0</h2>

<h5 id="added-24">Added</h5>
<ul>
  <li>Added <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#addsdkmetadata"><code class="language-plaintext highlighter-rouge">appboy.addSdkMetadata()</code></a> to allow self reporting of SDK Metadata fields via the <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.brazesdkmetadata.html"><code class="language-plaintext highlighter-rouge">appboy.BrazeSdkMetadata</code></a> enum.</li>
  <li>Deprecated the <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#stopWebTracking"><code class="language-plaintext highlighter-rouge">appboy.stopWebTracking()</code></a> method in favor of using <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#disableSDK"><code class="language-plaintext highlighter-rouge">appboy.disableSDK()</code></a>, which has the same functionality.</li>
  <li>Deprecated the <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#resumeWebTracking"><code class="language-plaintext highlighter-rouge">appboy.resumeWebTracking()</code></a> method in favor of using <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#enableSDK"><code class="language-plaintext highlighter-rouge">appboy.enableSDK()</code></a>, which has the same functionality.</li>
  <li>Added getter method <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#isDisabled"><code class="language-plaintext highlighter-rouge">appboy.isDisabled()</code></a> to determine if SDK has been disabled via <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#disableSDK"><code class="language-plaintext highlighter-rouge">appboy.disableSDK()</code></a>.</li>
  <li>Accessibility improvements to in-app messages with scrollable text.</li>
</ul>

<h5 id="changed-18">Changed</h5>
<ul>
  <li>Calling <code class="language-plaintext highlighter-rouge">changeUser()</code> with an SDK Authentication signature will now update the signature when it is called with the current user’s ID.</li>
</ul>

<h5 id="fixed-43">Fixed</h5>
<ul>
  <li>Fixed an issue where removing the <code class="language-plaintext highlighter-rouge">ab-pause-scrolling</code> class was not sufficient to allow scrolling on touchscreen devices during the display of an in-app message.</li>
</ul>

<h2 id="341">3.4.1</h2>

<h5 id="fixed-44">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 3.3.0 where event timestamps could become incorrect when a network request fails and the event is placed back in the queue.</li>
</ul>

<h2 id="340">3.4.0</h2>

<h5 id="added-25">Added</h5>
<ul>
  <li>Added <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html#addtosubscriptiongroup"><code class="language-plaintext highlighter-rouge">User.addToSubscriptionGroup()</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html#removefromsubscriptiongroup"><code class="language-plaintext highlighter-rouge">User.removeFromSubscriptionGroup()</code></a> to manage SMS/Email Subscription Groups.</li>
</ul>

<h5 id="changed-19">Changed</h5>
<ul>
  <li>Cards with subclass <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.controlcard.html"><code class="language-plaintext highlighter-rouge">ControlCard</code></a> are no longer counted in <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.feed.html#getunreadcardcount"><code class="language-plaintext highlighter-rouge">Feed.getUnreadCardCount</code></a> or <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.contentcards.html#getunviewedcardcount"><code class="language-plaintext highlighter-rouge">ContentCards.getUnviewedCardCount</code></a>.</li>
</ul>

<h5 id="fixed-45">Fixed</h5>
<ul>
  <li>Fixed an issue where globally-scoped CSS could cause the text and close button of In-App Messages to display incorrectly when using the built-in UI.</li>
  <li>Fixed an accessibility issue with Content Cards where some feed children did not have the <code class="language-plaintext highlighter-rouge">article</code> role.</li>
  <li>Fixed an issue where service worker network requests, including push click analytics, could not be made when SDK Authentication is enabled. If SDK Authentication is enabled and the service worker does not have a valid authentication signature, push click analytics will now be sent to the backend on the user’s next session.</li>
  <li>Fixed an issue where network requests that failed due to SDK Authentication errors did not use exponential backoff for retries.</li>
  <li>Fixed an issue where iPads would be detected as Mac devices when using the “Request Desktop Site” iOS feature.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">aspectRatio</code> had an incorrect type in <code class="language-plaintext highlighter-rouge">Card</code> subclasses.</li>
</ul>

<h2 id="330">3.3.0</h2>

<h5 id="added-26">Added</h5>
<ul>
  <li>Introduced support for new SDK Authentication feature.</li>
  <li>Introduced an <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions.__type.inappmessagezindex"><code class="language-plaintext highlighter-rouge">inAppMessageZIndex</code></a> initialization option that allows you to easily customize the z-index of In-App Messages displayed by the built-in UI.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">successCallback</code> and <code class="language-plaintext highlighter-rouge">errorCallback</code> parameters to <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#requestcontentcardsrefresh"><code class="language-plaintext highlighter-rouge">requestContentCardsRefresh</code></a>.</li>
  <li>The SDK now logs deprecation warnings for deprecated methods and initialization options when logging is enabled.</li>
  <li>Added support for <code class="language-plaintext highlighter-rouge">brazeBridge</code>, which has the same API as <code class="language-plaintext highlighter-rouge">appboyBridge</code>. <code class="language-plaintext highlighter-rouge">appboyBridge</code> is now deprecated but will continue to function.</li>
  <li>Introduced support for the upcoming nested properties feature in <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logcustomevent"><code class="language-plaintext highlighter-rouge">appboy.logCustomEvent</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logpurchase"><code class="language-plaintext highlighter-rouge">appboy.logPurchase</code></a>.</li>
</ul>

<h5 id="changed-20">Changed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">appboyQueue</code> replay snippet from the <code class="language-plaintext highlighter-rouge">npm</code> publication of the SDK. This avoids possible race conditions when referencing the SDK simultaneously from <code class="language-plaintext highlighter-rouge">npm</code> and the CDN, and removes use of <code class="language-plaintext highlighter-rouge">eval</code> from the <code class="language-plaintext highlighter-rouge">npm</code> package</li>
  <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logcustomevent"><code class="language-plaintext highlighter-rouge">appboy.logCustomEvent</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#logpurchase"><code class="language-plaintext highlighter-rouge">appboy.logPurchase</code></a> now impose a 50KB limit on custom properties. If the supplied properties are too large, the event is not logged.</li>
  <li>Deprecated the <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#tracklocation"><code class="language-plaintext highlighter-rouge">trackLocation</code></a> method in favor of using the native Geolocation API and passing the location data to <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html#setlastknownlocation">‘User.setLastKnownLocation`</a>. See our <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/location_tracking/">public docs</a> for more information.</li>
  <li>Deprecated the <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions.__type.enablehtmlinappmessages"><code class="language-plaintext highlighter-rouge">enableHtmlInAppMessages</code></a> initialization option in favor of <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions.__type.enablehtmlinappmessages"><code class="language-plaintext highlighter-rouge">allowUserSuppliedJavascript</code></a>. These options are functionally equivalent and no other changes are required.</li>
</ul>

<h5 id="fixed-46">Fixed</h5>
<ul>
  <li>Fixed incorrect typing for <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/appboy.user.html#setcountry"><code class="language-plaintext highlighter-rouge">User.setCountry</code></a>.</li>
  <li>Added missing <code class="language-plaintext highlighter-rouge">dismissed</code> property to TypeScript definition and docs for <code class="language-plaintext highlighter-rouge">Card</code> subclasses.</li>
</ul>

<h2 id="320">3.2.0</h2>

<h5 id="added-27">Added</h5>
<ul>
  <li>Added an optional <code class="language-plaintext highlighter-rouge">parentNode</code> parameter to <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.display.html#hidecontentcards"><code class="language-plaintext highlighter-rouge">appboy.display.hideContentCards</code></a> that allows you to specify a particular Content Cards feed to hide.</li>
</ul>

<h5 id="changed-21">Changed</h5>
<ul>
  <li>Cookies set by the SDK are now renewed when a new session is started. This fixes an issue where the SDK would stop setting cookies that had been deleted or expired when identification information existed in localStorage, preventing cross-subdomain identification from functioning in certain circumstances.</li>
  <li>Increased clickable area of all buttons in the built-in UI to be at least 45x45px to comply with mobile accessibility best-practices. This includes some minor changes to the Content Cards and News Feed UI to accommodate the larger buttons.</li>
</ul>

<h5 id="fixed-47">Fixed</h5>
<ul>
  <li>Fixed an issue where some network requests fail on websites using certain libraries that overwrite the native Promise object.</li>
</ul>

<h2 id="312">3.1.2</h2>

<h5 id="fixed-48">Fixed</h5>
<ul>
  <li>Added default <code class="language-plaintext highlighter-rouge">alt</code> text to In-App Message and Content Card images to improve screen-reader experience.</li>
  <li>Improved the display of different aspect ratios for <code class="language-plaintext highlighter-rouge">ClassicCard</code> images when using the built-in UI.</li>
  <li>Fixed a regression introduced in 3.1.0 where the SDK would sometimes make multiple network requests when starting a new session.</li>
  <li>Fixed an issue where globally-scoped <code class="language-plaintext highlighter-rouge">float</code> CSS caused certain elements of the built-in UI to display incorrectly.</li>
  <li>Fixed an incorrect TypeScript definition for <code class="language-plaintext highlighter-rouge">DeviceProperties</code>.</li>
</ul>

<h2 id="311">3.1.1</h2>

<h5 id="fixed-49">Fixed</h5>
<ul>
  <li>Fixed an issue where a javascript error could be thrown when showing Content Cards or In-App Messages in certain environments where <code class="language-plaintext highlighter-rouge">this</code> is undefined.</li>
</ul>

<h2 id="310">3.1.0</h2>

<h5 id="added-28">Added</h5>
<ul>
  <li>Added a <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions.__type.devicepropertyallowlist"><code class="language-plaintext highlighter-rouge">devicePropertyAllowlist</code></a> initialization option. This new initialization option has the same functionality as <code class="language-plaintext highlighter-rouge">devicePropertyWhitelist</code>, which is now deprecated and will be removed in a future release.</li>
</ul>

<h5 id="changed-22">Changed</h5>
<ul>
  <li>Relaxed the email address validation used by the SDK in favor of the more accurate Braze backend validation. Valid addresses with unusual structures or international characters which were previously rejected will now be accepted.</li>
</ul>

<h5 id="fixed-50">Fixed</h5>
<ul>
  <li>Fixed an issue where the SDK was improperly handling session starts when switching between subdomains, causing a short delay in triggering in-app messages.</li>
</ul>

<h2 id="301">3.0.1</h2>

<h5 id="fixed-51">Fixed</h5>
<ul>
  <li>Fixed incorrect type definitions for the <code class="language-plaintext highlighter-rouge">extras</code> property of Card and In-App Message classes.</li>
  <li>Fixed a regression introduced in 2.5.0 where the functionality of the <code class="language-plaintext highlighter-rouge">manageServiceWorkerExternally</code> and <code class="language-plaintext highlighter-rouge">disablePushTokenMaintenance</code> initialization options were swapped.</li>
</ul>

<h2 id="300">3.0.0</h2>

<h5 id="️-breaking-3">⚠️ Breaking</h5>
<ul>
  <li>The Braze Web SDK now comes bundled with TypeScript definitions in the <code class="language-plaintext highlighter-rouge">@braze</code> NPM packages. The TypeScript defintions include documentation and autocomplete in IDEs that support it, even if your project does not use TypeScript.</li>
  <li>The following breaking changes have been made to allow for a better TypeScript experience:
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">ab</code> namespace has been removed. To migrate from previous integrations, you can simply find and replace all references to <code class="language-plaintext highlighter-rouge">appboy.ab</code> with <code class="language-plaintext highlighter-rouge">appboy</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">InAppMessage.Button</code> has been renamed to <code class="language-plaintext highlighter-rouge">InAppMessageButton</code>. To migrate from previous integrations, you can simply find and replace all references to <code class="language-plaintext highlighter-rouge">InAppMessage.Button</code> with <code class="language-plaintext highlighter-rouge">InAppMessageButton</code>.</li>
    </ul>
  </li>
  <li>Due to the above changes, the SDK loading snippet has been updated. If you integrate the Braze Web SDK using the CDN, you must <a href="https://github.com/Appboy/appboy-web-sdk#Alternative-CDN-installation">update the loading snippet</a> when upgrading to 3.0.</li>
  <li>The <code class="language-plaintext highlighter-rouge">baseUrl</code> option to <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initialize"><code class="language-plaintext highlighter-rouge">appboy.initialize</code></a> is now required to initialize the SDK. If your integration did not already provide the <code class="language-plaintext highlighter-rouge">baseUrl</code> option, it should now be set to the previous default value of <code class="language-plaintext highlighter-rouge">sdk.iad-01.braze.com</code> (e.g, <code class="language-plaintext highlighter-rouge">appboy.initialize('YOUR-API-KEY', { baseUrl: 'sdk.iad-01.braze.com' });</code>).</li>
  <li>Removed the <code class="language-plaintext highlighter-rouge">messagingReadyCallback</code> from <code class="language-plaintext highlighter-rouge">openSession</code> and <code class="language-plaintext highlighter-rouge">changeUser</code>. Since 2.3.1, the SDK handles events that occur during the asynchronous portion of these calls gracefully, and ensures internally that only the latest messaging will be triggered. Any code previously being invoked inside this callback may be safely placed directly after the openSession or changeUser call.</li>
</ul>

<h5 id="changed-23">Changed</h5>
<ul>
  <li>The Braze Web SDK has brand new docs, which can be found <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html">here</a>. Any URLs from the previous docs will redirect to the appropriate location.</li>
</ul>

<h5 id="fixed-52">Fixed</h5>
<ul>
  <li>Fixed an issue where browser version was incorrectly reported in Android Webview.</li>
</ul>

<h2 id="271">2.7.1</h2>

<h5 id="fixed-53">Fixed</h5>
<ul>
  <li>Fixed a regression introduced in 2.5.0 where the functionality of the <code class="language-plaintext highlighter-rouge">manageServiceWorkerExternally</code> and <code class="language-plaintext highlighter-rouge">disablePushTokenMaintenance</code> initialization options were swapped.</li>
</ul>

<h2 id="270">2.7.0</h2>

<h5 id="added-29">Added</h5>
<ul>
  <li>Added <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge"><code class="language-plaintext highlighter-rouge">appboyBridge.getUser().addAlias(alias, label)</code></a> to HTML In-App Messages.</li>
</ul>

<h5 id="changed-24">Changed</h5>
<ul>
  <li>The Braze Web SDK now uses <a href="https://wicg.github.io/ua-client-hints/#interface">User-Agent Client Hints</a> for device detection when available. When using User-Agent Client Hints, browser version detection is limited to the significant version (e.g., 85 instead of 85.0.123.0). Note that this upgrade will be necessary to ensure accurate operating system detection in upcoming versions of Chromium-based browsers.</li>
  <li>Cards received from the Content Cards test send feature of the Braze dashboard are no longer removed when the SDK receives an update to the user’s Content Cards.</li>
</ul>

<h5 id="fixed-54">Fixed</h5>
<ul>
  <li>Removed code that could result in javascript errors in certain webpack configurations where the <code class="language-plaintext highlighter-rouge">global</code> object is not accessible by the SDK.</li>
  <li>Fixed an issue where the <code class="language-plaintext highlighter-rouge">ab.Card</code> methods <code class="language-plaintext highlighter-rouge">removeAllSubscriptions</code>, <code class="language-plaintext highlighter-rouge">removeSubscription</code>, <code class="language-plaintext highlighter-rouge">subscribeToClickedEvent</code>, and <code class="language-plaintext highlighter-rouge">subscribeToDismissedEvent</code> were minified, resulting in <code class="language-plaintext highlighter-rouge">undefined</code> when called.</li>
</ul>

<h2 id="260">2.6.0</h2>

<h5 id="added-30">Added</h5>
<ul>
  <li>Introduced new NPM packages under the <code class="language-plaintext highlighter-rouge">@braze</code> scope. The core and full versions of the SDK as well as the service worker are now published in their own packages, resulting in a drastically reduced install size compared to the <code class="language-plaintext highlighter-rouge">appboy-web-sdk</code> package. This is not a breaking change for existing NPM integrations and we will continue to publish the <code class="language-plaintext highlighter-rouge">appboy-web-sdk</code> package to maintain backwards compatibility. See the README for integration details.</li>
  <li>Added <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge"><code class="language-plaintext highlighter-rouge">appboyBridge.getUser().setLanguage(language)</code></a> to HTML In-App Messages.</li>
</ul>

<h5 id="changed-25">Changed</h5>
<ul>
  <li>The new HTML In-App Message type now allows multiple clicks to be logged for a given message.</li>
</ul>

<h5 id="fixed-55">Fixed</h5>
<ul>
  <li>Made push-related methods more defensive against edge-cases where <code class="language-plaintext highlighter-rouge">Notification</code> is not defined.</li>
  <li>Fixed an issue where unexpected backend responses could result in a javascript error.</li>
  <li>Fixed an issue in recent versions of Safari where calling <code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code> would throw a javascript error if the user did not allow websites to ask for permission to send notifications.</li>
</ul>

<h2 id="252">2.5.2</h2>

<h5 id="fixed-56">Fixed</h5>
<ul>
  <li>Fixed an issue that could cause some prerender user agents to fail to be appropriately recognized as a web crawler.</li>
</ul>

<h5 id="changed-26">Changed</h5>
<ul>
  <li>Data will now be flushed to the Braze backend every 3 seconds on Safari (down from 10 seconds) due to new privacy features that clear localStorage after 7 days of inactivity.</li>
</ul>

<h2 id="251">2.5.1</h2>

<h5 id="fixed-57">Fixed</h5>
<ul>
  <li>Fixed an issue in Content Cards where <code class="language-plaintext highlighter-rouge">getUnviewedCardCount()</code> returns <code class="language-plaintext highlighter-rouge">undefined</code>. This issue was introduced in 2.5.0.</li>
</ul>

<h2 id="250">2.5.0</h2>

<h5 id="added-31">Added</h5>
<ul>
  <li>Introduced support for upcoming HTML In-App Message templates.</li>
  <li>Added <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge"><code class="language-plaintext highlighter-rouge">appboyBridge.logClick()</code></a> to HTML In-App Messages.</li>
  <li>Expanded browser detection to include UC Browser and newer versions of Microsoft Edge that are based on Chromium.</li>
  <li>Added a new variant of the SDK that allows sites using RequireJS to load the SDK through another method, such as NPM or a <code class="language-plaintext highlighter-rouge">&lt;script&gt;</code> tag. See the <a href="https://github.com/Appboy/appboy-web-sdk#alternative-no-amd-installation">README</a> for more information.</li>
  <li>Added an optional callback to <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.requestImmediateDataFlush"><code class="language-plaintext highlighter-rouge">appboy.requestImmediateDataFlush</code></a> that is invoked when the flush is complete.</li>
  <li>Added Czech and Ukrainian language support for Braze UI elements.</li>
</ul>

<h5 id="changed-27">Changed</h5>
<ul>
  <li>Decreased the size of the service worker by 20%.</li>
</ul>

<h5 id="fixed-58">Fixed</h5>
<ul>
  <li>Fixed an issue where refreshing Content Cards or News Feed while the feed is showing could cause multiple impressions to be logged for the same card.</li>
  <li>Fixed a bug where calling <code class="language-plaintext highlighter-rouge">setEmail</code> with an email address containing capital letters could sometimes be incorrectly rejected.</li>
  <li>Fixed a bug where refreshing Content Cards would incorrectly set the <code class="language-plaintext highlighter-rouge">clicked</code> attribute of the cards to <code class="language-plaintext highlighter-rouge">false</code>.</li>
  <li>Fixed a bug where providing <code class="language-plaintext highlighter-rouge">serviceWorkerLocation</code> with an absolute URL containing a protocol and hostname would result in an error being logged when calling <code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code>.</li>
  <li>Fixed an issue where calling <code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code> in recent versions of Firefox would not show the notification prompt.</li>
  <li>Fixed a timing issue where creating a reference to <code class="language-plaintext highlighter-rouge">window.appboy</code> and then using that reference asynchronously could sometimes cause javascript errors when using the default integration snippet.</li>
</ul>

<h2 id="243">2.4.3</h2>

<h5 id="fixed-59">Fixed</h5>
<ul>
  <li>Fixed a bug that would cause <code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code> to fail when called immediately on a user’s first session.</li>
  <li>Fixed an issue where using both the <code class="language-plaintext highlighter-rouge">manageServiceWorkerExternally</code> and <code class="language-plaintext highlighter-rouge">serviceWorkerLocation</code> initialization options would cause the SDK to not register for push if the provided service worker location was in a sub-directory.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code> could throw an exception if an error occured while updating a previously registered service worker.</li>
</ul>

<h2 id="242">2.4.2</h2>

<h5 id="fixed-60">Fixed</h5>
<ul>
  <li>Fixed a bug introduced in 2.4.1 that would focus inline feeds, causing the page to scroll when content cards are shown out of view.</li>
</ul>

<h2 id="241">2.4.1</h2>

<h4 id="breaking">Breaking</h4>
<ul>
  <li>Accessibility updates in this release have changed headers to use <code class="language-plaintext highlighter-rouge">h1</code> tags and close buttons to use <code class="language-plaintext highlighter-rouge">button</code> tags (instead of <code class="language-plaintext highlighter-rouge">div</code> and <code class="language-plaintext highlighter-rouge">span</code> respectively). As a result, any CSS customizations which rely upon <code class="language-plaintext highlighter-rouge">div</code> or <code class="language-plaintext highlighter-rouge">span</code> elements within <code class="language-plaintext highlighter-rouge">.ab-feed</code> or <code class="language-plaintext highlighter-rouge">.ab-in-app-message</code> should be updated to use classes instead.</li>
</ul>

<h5 id="added-32">Added</h5>
<ul>
  <li>Introduced a <a href="https://js.appboycdn.com/web-sdk/latest/doc/ab.Card.html#dismissCard"><code class="language-plaintext highlighter-rouge">dismissCard</code></a> method that can be used to dismiss a card programmatically.</li>
  <li>Improved accessibility throughout the SDK:
    <ul>
      <li>Used <code class="language-plaintext highlighter-rouge">h1</code> tags for headers and <code class="language-plaintext highlighter-rouge">button</code> tags for close buttons</li>
      <li>Added ARIA attributes</li>
      <li>Improved the experience when tabbing through elements</li>
      <li>We now restore the user’s previously focused element after closing In-App Messages</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-61">Fixed</h5>
<ul>
  <li>Fixed a bug introduced in 2.4.0 that could cause a javascript error in integrations that only include the core library. This error would occur when a Content Card with a URL is received.</li>
</ul>

<h2 id="240">2.4.0</h2>

<h5 id="breaking-1">Breaking</h5>
<ul>
  <li>Removed the Feedback feature and <code class="language-plaintext highlighter-rouge">appboy.submitFeedback</code> method from the SDK.</li>
</ul>

<h5 id="added-33">Added</h5>
<ul>
  <li>Improved browser detection to account for the Smart TV landscape.</li>
  <li>Added logic to automatically renew push subscriptions when they are expired or older than 6 months.</li>
  <li>Introduced a <code class="language-plaintext highlighter-rouge">contentSecurityNonce</code> initialization option for sites with a Content Security Policy. See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize"><code class="language-plaintext highlighter-rouge">appboy.initialize</code></a> documentation for more info.</li>
  <li>Introduced a <code class="language-plaintext highlighter-rouge">disablePushTokenMaintenance</code> initialization option for sites that have users with Web Push permission granted, but do not wish to use Web Push with Braze. See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize"><code class="language-plaintext highlighter-rouge">appboy.initialize</code></a> documentation for more info.</li>
  <li>Introduced a <code class="language-plaintext highlighter-rouge">manageServiceWorkerExternally</code> initialization option for sites that have their own service worker already. See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize"><code class="language-plaintext highlighter-rouge">appboy.initialize</code></a> documentation for more info.</li>
  <li>Deprecated the <code class="language-plaintext highlighter-rouge">subscribeToNewInAppMessages</code> method in favor of the new <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.subscribeToInAppMessage"><code class="language-plaintext highlighter-rouge">subscribeToInAppMessage</code></a> method, which has a simpler interface.</li>
</ul>

<h5 id="fixed-62">Fixed</h5>
<ul>
  <li>Improved support for In-App Messages on “notched” devices (for example, iPhone X, Pixel 3XL).</li>
  <li>The logic that prevents the page behind a modal or fullscreen In-App Message from scrolling now functions correctly on iOS.</li>
  <li>Fixed a caching bug that could cause In-App Messages, Content Cards, and News Feed Cards received by one instance of the Braze SDK to not be seen by another simultaneously running instance of the Braze SDK.</li>
  <li>Fixed a bug that would cause redundant network activity for new users on their first session ever.</li>
  <li>Fixed a bug that would cause push registration that occurs immediately on a user’s first session to fail.</li>
  <li>Introduced the <code class="language-plaintext highlighter-rouge">allowUserSuppliedJavascript</code> initialization option, which is an alias for the existing <code class="language-plaintext highlighter-rouge">enableHtmlInAppMessages</code> option, and disabled the ability to use <code class="language-plaintext highlighter-rouge">javascript:</code> URIs in In-App Message and Content Card click actions unless one of these options is provided.</li>
</ul>

<h5 id="changed-28">Changed</h5>
<ul>
  <li>Improved the look and feel of Content Card dismissals and Content Card and News Feed animations to match the latest In-App Message styles.</li>
  <li>The <code class="language-plaintext highlighter-rouge">baseUrl</code> configuration option for <code class="language-plaintext highlighter-rouge">appboy.initialize</code> is now more flexible in the values that it can accept.</li>
  <li>Cookies set by the Braze Web SDK now expire after 1 year.</li>
</ul>

<h2 id="234">2.3.4</h2>

<h5 id="fixed-63">Fixed</h5>
<ul>
  <li>Fix regression introduced in 2.3.3 that could prevent analytics from being logged from the service worker.</li>
</ul>

<h2 id="233">2.3.3</h2>

<h5 id="fixed-64">Fixed</h5>
<ul>
  <li>Improved some In-App Message CSS styles to be more resilient against conflicts with any page-wide CSS.</li>
  <li>Improved the resiliency of the code that allows body content to scroll again when modal or fullscreen in-app messages are dismissed.</li>
</ul>

<h2 id="232">2.3.2</h2>

<h5 id="added-34">Added</h5>
<ul>
  <li>Added support for an improved integration snippet which is capable of stubbing the interface before the SDK loads in Google Tag Manager.</li>
</ul>

<h2 id="231">2.3.1</h2>

<h5 id="added-35">Added</h5>
<ul>
  <li>Introduced new <code class="language-plaintext highlighter-rouge">closeMessage</code> method on <code class="language-plaintext highlighter-rouge">ab.InAppMessage</code> objects to enable integrations to programmatically close messages if desired.</li>
  <li>The Braze Web SDK now automatically enqueues trigger events that occur while triggers are being synced with the Braze backend, and replays them when the sync is complete. This fixes a race condition that could cause users to inadvertantly miss messages when trigger events occur directly after calling <code class="language-plaintext highlighter-rouge">openSession</code> or <code class="language-plaintext highlighter-rouge">changeUser</code>. This change obsoletes usage of the <code class="language-plaintext highlighter-rouge">messagingReadyCallback</code>, which is now deprecated (but will continue to function).</li>
</ul>

<h5 id="fixed-65">Fixed</h5>
<ul>
  <li>Fixed an issue which prevented tall <code class="language-plaintext highlighter-rouge">ab.HtmlMessage</code> objects from scrolling on iOS.</li>
  <li>Fixed “Object doesn’t support this action” error in Internet Explorer 11 or older when showing <code class="language-plaintext highlighter-rouge">ab.HtmlMessage</code> objects.</li>
</ul>

<h2 id="230">2.3.0</h2>

<h5 id="added-36">Added</h5>
<ul>
  <li>Improved the look and feel of In-App Messages to adhere to the latest UX and UI best practices. Changes affect font sizes, padding, and responsiveness across all message types. Now supports button border styling.</li>
</ul>

<h5 id="fixed-66">Fixed</h5>
<ul>
  <li>This feature, which regressed in 2.1.0, has been restored: when you call <code class="language-plaintext highlighter-rouge">appboy.openSession</code>, if the user has previously granted the site permission to send push, Braze will now automatically send the user’s push token to Braze backend. This will allow users to continue to receive push messages if they manually remove push permission and then subsequently manually reenable it - and will also cause user push tokens to automatically migrate to Braze over time when moving to Braze from a previously-integrated third-party push provider.</li>
</ul>

<h2 id="227">2.2.7</h2>

<h5 id="added-37">Added</h5>
<ul>
  <li>HTML In-App Messages now emit an <code class="language-plaintext highlighter-rouge">ab.BridgeReady</code> event when the <code class="language-plaintext highlighter-rouge">appboyBridge</code> variable is available for use inside your HTML, allowing you to use <code class="language-plaintext highlighter-rouge">appboyBridge</code> immediately when an in-app message is shown. To utilize this event in your HTML In-App Messages, use <code class="language-plaintext highlighter-rouge">window.addEventListener('ab.BridgeReady', function() {/*Use appboyBridge here*/}, false);</code>.</li>
</ul>

<h5 id="changed-29">Changed</h5>
<ul>
  <li>Changed usages of <code class="language-plaintext highlighter-rouge">Date.now()</code> to <code class="language-plaintext highlighter-rouge">new Date().valueOf()</code> to allow the Braze SDK to sit side-by-side with legacy 3rd party libraries that monkey-patched <code class="language-plaintext highlighter-rouge">Date.now()</code> before ECMASCRIPT 5 defined it.</li>
</ul>

<h2 id="226">2.2.6</h2>

<h5 id="added-38">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">clicked</code> property to Content Cards which returns true if this card has ever been clicked on this device.</li>
</ul>

<h5 id="changed-30">Changed</h5>
<ul>
  <li>Improved in-app message triggering logic to fall back to lower priority messages when the Braze server aborts templating (e.g. from a Connected Content abort in the message body, or because the user is no longer in the correct Segment for the message)</li>
  <li>Improved in-app message triggering logic to retry user personalization when communication with the Braze server fails due to network connectivity issues.</li>
  <li>The Braze Web SDK now only stores cookies for the most recently-used API Key (app). This reduces cookie storage usage for domains that are configured against many Braze apps.</li>
</ul>

<h2 id="225">2.2.5</h2>

<h5 id="added-39">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">devicePropertyWhitelist</code> property to the options for <code class="language-plaintext highlighter-rouge">appboy.initialize()</code>, which can be used to filter what device properties get collected.</li>
</ul>

<h2 id="224">2.2.4</h2>

<h5 id="added-40">Added</h5>
<ul>
  <li>Added support for richer custom styling through CSS in in-app messages.</li>
</ul>

<h5 id="changed-31">Changed</h5>
<ul>
  <li>Subtle visual polish to the News Feed and Content Cards</li>
</ul>

<h2 id="223">2.2.3</h2>

<h5 id="added-41">Added</h5>
<ul>
  <li>Added support for tracking custom location attributes. See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setCustomLocationAttribute"><code class="language-plaintext highlighter-rouge">ab.User.setCustomLocationAttribute</code></a> documentation for more information.</li>
  <li>When calling <code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code> with a <code class="language-plaintext highlighter-rouge">deniedCallback</code>, that <code class="language-plaintext highlighter-rouge">deniedCallback</code> will now be invoked (with a <code class="language-plaintext highlighter-rouge">temporary</code> parameter of <code class="language-plaintext highlighter-rouge">true</code>) for temporary denials, where the browser has automatically denied permission on behalf of the user after multiple ignored attempts to register for push, but will allow attempts again in the future - probably in about a week.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">appboyBridge.web.trackLocation()</code> in HTML in-app messages. This enables HTML in-app message soft location tracking prompts.</li>
</ul>

<h5 id="fixed-67">Fixed</h5>
<ul>
  <li>News Feed and Content Cards clicks and impressions will now be logged multiple times for a given card (if they in fact occur multiple times). Impressions will still only be logged for a given card once per viewing of the feed (regardless of how many times it scrolls in and out of view).</li>
  <li>Improved logic around IndexedDB to better catch and log errors (prevents security errors with disabled cookies on certain browsers, or from Safari’s “Intelligent Tracking Prevention” when integrated in an iFrame).</li>
  <li>Worked around <a href="https://bugs.chromium.org/p/chromium/issues/detail?id=811403">this Chrome Bug</a> which could cause device detection to throw “Unsupported time zone specified undefined” on Linux-based systems with certain settings.</li>
  <li>Fixed an issue where the messagingReadyCallback would not get fired if changeUser was called with an empty ID.</li>
</ul>

<h5 id="changed-32">Changed</h5>
<ul>
  <li>Data will now be flushed to the Braze backend every three seconds when localStorage is not available.</li>
  <li>Improved triggered in-app message re-eligibility logic to better handle templating failures.</li>
</ul>

<h2 id="222">2.2.2</h2>

<h5 id="added-42">Added</h5>
<ul>
  <li>Updated push token handling to automatically remove blocked users from the pushable audience on session start.</li>
</ul>

<h5 id="fixed-68">Fixed</h5>
<ul>
  <li>Fixed issue in Content Cards where the <code class="language-plaintext highlighter-rouge">getUnviewedCardCount</code> method on <code class="language-plaintext highlighter-rouge">ab.ContentCards</code> could not be invoked properly.</li>
  <li>Fixed a bug where the <a href="https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#addAlias"><code class="language-plaintext highlighter-rouge">addAlias</code> method</a> was returning an object instead of a boolean value.</li>
  <li>Fixed issue which could prevent Content Cards from syncing properly on IE 11 and Safari.</li>
</ul>

<h5 id="changed-33">Changed</h5>
<ul>
  <li>Various user attribute methods now support setting null (<code class="language-plaintext highlighter-rouge">setFirstName</code>, <code class="language-plaintext highlighter-rouge">setLastName</code>, <code class="language-plaintext highlighter-rouge">setCountry</code>, <code class="language-plaintext highlighter-rouge">setHomeCity</code>, <code class="language-plaintext highlighter-rouge">setPhoneNumber</code>, <code class="language-plaintext highlighter-rouge">setEmail</code>, <code class="language-plaintext highlighter-rouge">setGender</code>, <code class="language-plaintext highlighter-rouge">setLanguage</code>, and <code class="language-plaintext highlighter-rouge">setDateOfBirth</code>) by passing in an explicit null value.</li>
</ul>

<h2 id="221">2.2.1</h2>

<h5 id="fixed-69">Fixed</h5>
<ul>
  <li>Prevent push received/clicked analytics from being sent to the Braze backend when <code class="language-plaintext highlighter-rouge">appboy.stopWebTracking</code> has been called.</li>
</ul>

<h2 id="220">2.2.0</h2>

<h5 id="added-43">Added</h5>
<ul>
  <li>Introduced support for Content Cards, which will eventually replace the existing News Feed feature and adds significant capability.</li>
  <li>Added support for web push on Accelerated Mobile Pages (AMP). See https://www.braze.com/documentation/Web/#amp-support for setup information.</li>
</ul>

<h5 id="fixed-70">Fixed</h5>
<ul>
  <li>Fixed an issue where in-app messages triggered on session start could potentially be templated with the old user’s attributes.</li>
</ul>

<h5 id="removed">Removed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">appboy.requestInAppMessageRefresh()</code> and support for legacy in-app messages - these were long-deprecated and have been supplanted by <a href="https://www.braze.com/documentation/Web/#in-app-messages-triggered">triggered in-app messages</a>.</li>
</ul>

<h2 id="211">2.1.1</h2>

<h5 id="fixed-71">Fixed</h5>
<ul>
  <li>Prevent push received/clicked analytics from being sent to the Braze backend when <code class="language-plaintext highlighter-rouge">appboy.stopWebTracking</code> has been called.</li>
</ul>

<h2 id="210">2.1.0</h2>

<h5 id="added-44">Added</h5>
<ul>
  <li>Added <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#wipeData"><code class="language-plaintext highlighter-rouge">appboy.wipeData()</code></a> to allow deletion of locally stored SDK data. After calling this method, users will appear as a new anonymous user on a new device.</li>
</ul>

<h5 id="fixed-72">Fixed</h5>
<ul>
  <li>Improved push registration and unregistration
    <ul>
      <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#registerAppboyPushMessages"><code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code></a> will now set the user’s subscription status to “OPTED_IN” only at times when they’ve just accepted the permission prompt.</li>
      <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#unregisterAppboyPushMessages"><code class="language-plaintext highlighter-rouge">appboy.unregisterAppboyPushMessages</code></a> will now persist across sessions and user changes (until <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#registerAppboyPushMessages"><code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code></a> is called again).</li>
      <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#registerAppboyPushMessages"><code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code></a> will cause push prompts to be shown shown more reliably in situations where the user has ignored them in the past. Logging around dismissing (as opposed to accepting or blocking) push prompts has been improved.</li>
    </ul>
  </li>
  <li>Fixed a bug with <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#changeUser"><code class="language-plaintext highlighter-rouge">appboy.changeUser</code></a> where <code class="language-plaintext highlighter-rouge">messagingReadyCallback</code> would not fire when the supplied <code class="language-plaintext highlighter-rouge">userId</code> was the current user.</li>
</ul>

<h5 id="changed-34">Changed</h5>
<ul>
  <li>Updated from FontAwesome 4.3.0 to FontAwesome 4.7.0. Integrations that wish to maintain older versions should pass in <code class="language-plaintext highlighter-rouge">doNotLoadFontAwesome</code> as <code class="language-plaintext highlighter-rouge">true</code> during initialization and load their desired version.</li>
  <li>The Braze SDK will automatically load FontAwesome unless <code class="language-plaintext highlighter-rouge">doNotLoadFontAwesome</code> is explicitly passed in as <code class="language-plaintext highlighter-rouge">true</code> during initialization, regardless of whether fontawesome.css or fontawesome.min.css are already on the page.</li>
</ul>

<h2 id="209">2.0.9</h2>

<h5 id="fixed-73">Fixed</h5>
<ul>
  <li>Prevent push received/clicked analytics from being sent to the Braze backend when <code class="language-plaintext highlighter-rouge">appboy.stopWebTracking</code> has been called.</li>
</ul>

<h2 id="208">2.0.8</h2>

<h5 id="added-45">Added</h5>
<ul>
  <li>Added defensive guards against any possibility of sessions expiring in less than 1 second or of creating multiple session events in rapid succession if scripted in parallel across many open tabs.</li>
</ul>

<h2 id="207">2.0.7</h2>

<h5 id="added-46">Added</h5>
<ul>
  <li>Added support for <a href="https://tools.ietf.org/html/rfc8292">Voluntary Application Server Identification (VAPID) for Web Push</a>:
    <ul>
      <li>Will be required for Microsoft Edge’s upcoming Web Push support, and possibly other browsers in the future.</li>
      <li>Allows importing of VAPID-enabled push tokens generated by other push providers, given the corresponding keypair (support@braze.com).</li>
      <li>Happens transparently in the background and does not require an integration update.</li>
      <li>Once the browser landscape has sufficiently matured, this will eventually obviate the need to supply a <code class="language-plaintext highlighter-rouge">gcm_sender_id</code> in your site’s <code class="language-plaintext highlighter-rouge">manifest.json</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-35">Changed</h5>
<ul>
  <li><a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#unregisterAppboyPushMessages"><code class="language-plaintext highlighter-rouge">appboy.unregisterAppboyPushMessages</code></a> now accepts optional <code class="language-plaintext highlighter-rouge">successCallback</code> and <code class="language-plaintext highlighter-rouge">errorCallback</code> arguments to signal completion, as it functions asynchronously.</li>
</ul>

<h2 id="206">2.0.6</h2>

<h5 id="fixed-74">Fixed</h5>
<ul>
  <li>Fixed a javascript error introduced in 2.0.5 when logging in the service worker.</li>
</ul>

<h2 id="205">2.0.5</h2>

<h5 id="added-47">Added</h5>
<ul>
  <li>Added Location Tracking - See <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#trackLocation"><code class="language-plaintext highlighter-rouge">appboy.trackLocation()</code></a> for more information.</li>
  <li><code class="language-plaintext highlighter-rouge">appboy.user.setGender</code> now supports more gender options. See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#toc4"><code class="language-plaintext highlighter-rouge">Genders</code> enum documentation</a> for more information.</li>
  <li>Added <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#stopWebTracking"><code class="language-plaintext highlighter-rouge">appboy.stopWebTracking()</code></a> and <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#resumeWebTracking"><code class="language-plaintext highlighter-rouge">appboy.resumeWebTracking()</code></a> to allow user opt-outs.</li>
  <li>Improved accessibility for in-app messages and news feed by focusing on elements where appropriate, allowing users to tab through various buttons, and adding labels where appropriate.</li>
</ul>

<h5 id="fixed-75">Fixed</h5>
<ul>
  <li>Fixed a bug that caused <code class="language-plaintext highlighter-rouge">appboy.display.automaticallyShowNewInAppMessages()</code> not to function correctly when called after calling <code class="language-plaintext highlighter-rouge">appboy.destroy()</code> and then calling <code class="language-plaintext highlighter-rouge">appboy.initialize()</code> a second time.</li>
  <li>The <code class="language-plaintext highlighter-rouge">openSession</code> and <code class="language-plaintext highlighter-rouge">changeUser</code> methods now take a <code class="language-plaintext highlighter-rouge">messagingReadyCallback</code> that executes when the Braze Web SDK is ready to show messaging data to this user. This fixes a race condition where custom events could be logged before in-app messages had been fetched from the Braze backend and users would not see intended messaging.</li>
</ul>

<h5 id="changed-36">Changed</h5>
<ul>
  <li>Deprecated the <code class="language-plaintext highlighter-rouge">submitFeedback</code> method. The feedback feature is disabled for new accounts, and will be removed in a future SDK release.</li>
</ul>

<h2 id="204">2.0.4</h2>

<h5 id="changed-37">Changed</h5>
<ul>
  <li>Renamed documentation references from Appboy to Braze. This is not a breaking change.</li>
</ul>

<h2 id="203">2.0.3</h2>

<h5 id="fixed-76">Fixed</h5>
<ul>
  <li>Fixed a null reference error when replaying calls made using the new integration snippet on IE 11.</li>
</ul>

<h2 id="202">2.0.2</h2>

<h5 id="fixed-77">Fixed</h5>
<ul>
  <li>Fixed an issue with our minification that would cause the Braze Web SDK to leak polyfill functions into the global namespace.</li>
</ul>

<h2 id="201">2.0.1</h2>

<h5 id="fixed-78">Fixed</h5>
<ul>
  <li>Fixed automatic css loading when used in combination with the doNotLoadFontAwesome initialization option.</li>
</ul>

<h2 id="200">2.0.0</h2>

<h5 id="breaking-2">Breaking</h5>
<ul>
  <li>Braze now automatically loads required CSS styles. You must remove all references to appboy.min.css from your site.</li>
  <li>The <code class="language-plaintext highlighter-rouge">getUserId</code> method now takes a callback which it invokes with the userId, instead of returning a value directly. This is necessary to ensure the proper replaying of calls made to <code class="language-plaintext highlighter-rouge">appboy</code> before the SDK has fully loaded. Where before, you would do <code class="language-plaintext highlighter-rouge">var userId = appboy.getUser().getUserId();</code>, now do <code class="language-plaintext highlighter-rouge">appboy.getUser().getUserId(function(userId) { console.log(userId); })</code>  See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#getUserId"><code class="language-plaintext highlighter-rouge">getUserId method documentation</code></a> for more information.</li>
  <li>The <code class="language-plaintext highlighter-rouge">getDeviceId</code> method now takes a callback which it invokes with the deviceId, instead of returning a value directly. This is necessary to ensure the proper replaying of calls made to <code class="language-plaintext highlighter-rouge">appboy</code> before the SDK has fully loaded. See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#getDeviceId"><code class="language-plaintext highlighter-rouge">getDeviceId method documentation</code></a> for more information.</li>
</ul>

<h5 id="changed-38">Changed</h5>
<ul>
  <li><a href="https://github.com/Appboy/appboy-web-sdk#getting-started">The default Braze integration snippet</a> has been updated for best-practices compliance, resilience, and performance. Using this new snippet, calls may be made to <code class="language-plaintext highlighter-rouge">appboy</code> before the SDK has fully loaded, and will be replayed automatically when the SDK loads. We recommend that you update your site’s integration to the new snippet for optimal behavior, but this is not a breaking change, and is not required.</li>
</ul>

<h5 id="added-48">Added</h5>
<ul>
  <li>If you are using a front-end packager such as <a href="http://browserify.org/">Browserify</a> or <a href="https://webpack.github.io/">Webpack</a>, <a href="https://github.com/Appboy/appboy-web-sdk#Alternative-NPM-installation">the NPM integration instructions</a> have been updated to meet your use-case.</li>
</ul>

<h2 id="1614">1.6.14</h2>

<h5 id="added-49">Added</h5>
<ul>
  <li>Added the user agent for the https://prerender.io/ crawler to the list of known web crawlers.</li>
  <li>Added <a href="https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setLanguage"><code class="language-plaintext highlighter-rouge">ab.User.setLanguage</code></a> method to allow explicit control over the language you use in the Braze dashboard to localize your messaging content.</li>
</ul>

<h5 id="fixed-79">Fixed</h5>
<ul>
  <li>Fixed array validation on pages where the Array type has been modified by other scripts.</li>
</ul>

<h5 id="changed-39">Changed</h5>
<ul>
  <li>Marked the ‘touchstart’ listener in in-app messages as ‘passive’ for performance and PWA compliance.</li>
</ul>

<h2 id="1613">1.6.13</h2>

<h5 id="added-50">Added</h5>
<ul>
  <li>Contains service-worker support for Web Push notifications that require user interaction to be dismissed.</li>
</ul>

<h5 id="fixed-80">Fixed</h5>
<ul>
  <li>Improved time zone recognition on modern browsers to prevent possible ambiguity between different zones with similar UTC offsets.</li>
  <li>Broadened detection of the Android OS to better recognize newer hardware and as-of-yet unreleased hardware on an ongoing basis.</li>
  <li>Fixed data-formation error when pending additions or removals to a custom attribute array were re-enqueued following a Braze backend outage or otherwise failed data flush.</li>
</ul>

<h5 id="changed-40">Changed</h5>
<ul>
  <li>We now allow a value of 0 for the <code class="language-plaintext highlighter-rouge">minimumIntervalBetweenTriggerActionsInSeconds</code> option for <code class="language-plaintext highlighter-rouge">appboy.initialize</code></li>
</ul>

<h2 id="1612">1.6.12</h2>

<h5 id="added-51">Added</h5>
<ul>
  <li>Introduced <code class="language-plaintext highlighter-rouge">noCookies</code> option. By default, the Braze SDK will store small amounts of data (user ids, session ids), in cookies. This is done to allow Braze to recognize users and sessions across different subdomains of your site. If this presents a problem for you, pass <code class="language-plaintext highlighter-rouge">true</code> for this option to disable cookie storage and rely entirely on HTML 5 localStorage to identify users and sessions. The downside of this configuration is that you will be unable to recognize users across subdomains of your site.</li>
  <li>Added user aliasing capability. Aliases can be used in the API and dashboard to identify users in addition to their ID.  See the <a href="https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#addAlias"><code class="language-plaintext highlighter-rouge">addAlias method documentation</code></a> for more information.</li>
</ul>

<h5 id="fixed-81">Fixed</h5>
<ul>
  <li>Fixed issue in which the local cache of seen in-app messages and news feed cards was being cleared when the anonymous user was identified, allowing certain items to be retriggered or appear unread.</li>
</ul>

<h2 id="1611">1.6.11</h2>

<h5 id="added-52">Added</h5>
<ul>
  <li>When you call <code class="language-plaintext highlighter-rouge">appboy.openSession</code>, if the user has previously granted the site permission to send push, Braze will now automatically send the user’s push token to Braze backend. This will allow users to continue to receive push messages if they manually remove push permission and then subsequently manually reenable it - and will also cause user push tokens to automatically migrate to Braze over time when moving to Braze from a previously-integrated third-party push provider.</li>
</ul>

<h5 id="fixed-82">Fixed</h5>
<ul>
  <li>IMPORTANT: Due to a behavioral change in Chrome 59, to reliably receive notifications, you must update the service worker from https://js.appboycdn.com/web-sdk/1.6/service-worker.js.</li>
  <li><code class="language-plaintext highlighter-rouge">appboy.display.automaticallyShowNewInAppMessages()</code> may now be safely called multiple times on the same <code class="language-plaintext highlighter-rouge">appboy</code> instance.</li>
</ul>

<h2 id="1610">1.6.10</h2>

<h5 id="fixed-83">Fixed</h5>
<ul>
  <li>A bug in our documentation for soft push prompts could cause Control Group stats to fail. If you previously implemented soft push prompts, please refer to the latest version of our documentation: https://www.braze.com/documentation/Web/#soft-push-prompts</li>
</ul>

<h2 id="169">1.6.9</h2>

<h5 id="added-53">Added</h5>
<ul>
  <li>Added support for <code class="language-plaintext highlighter-rouge">appboyBridge.web.registerAppboyPushMessages</code> to allow HTML in-app messages to request push permission from the user.</li>
</ul>

<h2 id="168">1.6.8</h2>

<h5 id="fixed-84">Fixed</h5>
<ul>
  <li>Fixed “Notification is not defined” error when calling <code class="language-plaintext highlighter-rouge">appboy.isPushPermissionGranted</code>/<code class="language-plaintext highlighter-rouge">appboy.isPushBlocked</code> on Chrome versions prior to 46.</li>
</ul>

<h2 id="167">1.6.7</h2>

<h5 id="added-54">Added</h5>
<ul>
  <li>The Braze Web SDK now supports HTML content in-app messages. For your security, these must be enabled by supplying the <code class="language-plaintext highlighter-rouge">enableHtmlInAppMessages</code> configuration option when calling <code class="language-plaintext highlighter-rouge">appboy.initialize</code>.</li>
</ul>

<h5 id="fixed-85">Fixed</h5>
<ul>
  <li>The News Feed css is now defensive against any global box-sizing css rules that may exist on your site, and handles classic card image styling more gracefully.</li>
  <li>On mobile devices, Fullscreen in-app messages’ close buttons are sized relative to the entire device - this ensures touchable targets on high-resolution phones.</li>
  <li>Improved positioning of Modal in-app messages to ensure visibility and attractive positioning across all browsers.</li>
</ul>

<h2 id="166">1.6.6</h2>

<h5 id="fixed-86">Fixed</h5>
<ul>
  <li>Fixed a data-storage issue where a small number of users impacted by the issue fixed in 1.6.5 may record a new session on page load after upgrading to 1.6.5.</li>
</ul>

<h2 id="165">1.6.5</h2>

<h5 id="fixed-87">Fixed</h5>
<ul>
  <li>Cookies are now stored with path=/ for sitewide accessibility, ensuring that identification persists sitewide in all situations. This fixes an issue introduced in 1.6.0.</li>
</ul>

<h2 id="164">1.6.4</h2>

<h5 id="added-55">Added</h5>
<ul>
  <li>The Braze Web SDK now ignores web crawler activity by default - this saves datapoints, makes analytics more accurate, and may improve page rank (this change can be reversed with the <code class="language-plaintext highlighter-rouge">allowCrawlerActivity</code> initialization option).</li>
</ul>

<h5 id="fixed-88">Fixed</h5>
<ul>
  <li>Fixed an issue where in-app messages triggered off of push clicks wouldn’t fire because the push click happened before the in-app message configuration was synced to the device.</li>
  <li>Increased defensiveness against corrupted localStorage or cookie data.</li>
</ul>

<h5 id="changed-41">Changed</h5>
<ul>
  <li>Increased the size of in-app message close buttons on mobile browsers slightly to make an easier touch target.</li>
  <li>Updated <code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code> to flush subscriptions to the server immediately.</li>
</ul>

<h2 id="163">1.6.3</h2>

<h5 id="changed-42">Changed</h5>
<ul>
  <li>Further improved the layout of Fullscreen in-app messages on short desktop screens.</li>
</ul>

<h2 id="162">1.6.2</h2>

<h5 id="changed-43">Changed</h5>
<ul>
  <li>Deprecated the <code class="language-plaintext highlighter-rouge">appboy.isPushGranted</code> method in favor of the new <code class="language-plaintext highlighter-rouge">appboy.isPushPermissionGranted</code>. The old method was inappropriately testing whether the browser has an active push subscription, and not doing the intended test of whether the user has granted push <strong>permission</strong>. The old method will be removed in an upcoming release.</li>
</ul>

<h2 id="161">1.6.1</h2>

<h5 id="fixed-89">Fixed</h5>
<ul>
  <li>Improved Modal in-app message layout to prevent text-view scrolling until necessary.</li>
</ul>

<h5 id="changed-44">Changed</h5>
<ul>
  <li>Deprecated the <code class="language-plaintext highlighter-rouge">safariWebsitePushId</code> parameter to <code class="language-plaintext highlighter-rouge">appboy.registerAppboyPushMessages</code> and <code class="language-plaintext highlighter-rouge">appboy.isPushGranted</code> in favor of the new <code class="language-plaintext highlighter-rouge">safariWebsitePushId</code> option to <code class="language-plaintext highlighter-rouge">appboy.initialize</code>. If you implement Safari push, you should convert your integration to use the new initialization option - support for the parameters will be removed in a future release. This is not yet a breaking change.</li>
  <li>Polished Fullscreen in-app message display on desktop browsers to reduce unused whitespace when the content is small enough not to scroll.</li>
</ul>

<h2 id="160">1.6.0</h2>

<h5 id="fixed-90">Fixed</h5>
<ul>
  <li>Fixed an edge-case that could cause SlideUp in-app messages to appear offscreen if many were triggered in rapid succession.</li>
</ul>

<h5 id="changed-45">Changed</h5>
<ul>
  <li>Improved ability to consistently identify users, devices, and sessions across subdomains by preferring domain-wide cookies for ID storage (over the previously-preferred localStorage).</li>
</ul>

<h2 id="151">1.5.1</h2>

<h5 id="fixed-91">Fixed</h5>
<ul>
  <li>Fixed a rendering issue that could cause FullScreen in-app messages to appear partially off-screen on very short browser windows.</li>
</ul>

<h2 id="150">1.5.0</h2>

<h5 id="added-56">Added</h5>
<ul>
  <li>Added support for upgraded in-app messages including image-only messages, improved image sizing/cropping, text scrolling, text alignment, configurable orientation, and configurable frame color.</li>
  <li>Added support for in-app messages triggered on custom event properties, purchase properties, and in-app message clicks.</li>
  <li>Improved support for templated in-app messages.</li>
  <li>Added appboy.isPushGranted() method, useful for migrating existing push subscriptions from another third-party provider to Braze.</li>
  <li>Added language localization - language is detected automatically from the browser or can be specified explicitly via the <code class="language-plaintext highlighter-rouge">language</code> initialization option.</li>
</ul>

<h2 id="142">1.4.2</h2>

<h5 id="added-57">Added</h5>
<ul>
  <li>Added additional logging information for Safari push.</li>
</ul>

<h2 id="141">1.4.1</h2>

<h5 id="added-58">Added</h5>
<ul>
  <li>Added a more explicit error when attempting to call registerAppboyPushMessages on Safari without supplying a safariWebsitePushID.</li>
</ul>

<h2 id="140">1.4.0</h2>

<h5 id="added-59">Added</h5>
<ul>
  <li>Added support for Safari push messages.</li>
  <li>If you version your website, you may now optionally pass the version to Braze via the new <code class="language-plaintext highlighter-rouge">appVersion</code> initialization option.</li>
  <li>The News Feed now displays a timed-out message to users if the refresh fails (due to network or back end outages).</li>
  <li>Browser version will now be reported as part of the user’s device information along with browser.</li>
  <li>Added ability to specify on a message-by-message basis whether in-app message clicks should open in a new tab or same tab.</li>
</ul>

<h5 id="fixed-92">Fixed</h5>
<ul>
  <li>Fixed an issue which caused emoji in web push messages to be broken on Firefox.</li>
</ul>

<h5 id="changed-46">Changed</h5>
<ul>
  <li>Overhauled the browser detection code for improved reliability.</li>
</ul>

<h2 id="133">1.3.3</h2>

<h5 id="added-60">Added</h5>
<ul>
  <li>Added a new <code class="language-plaintext highlighter-rouge">serviceWorkerLocation</code> initialization option. See JSDocs for more information.</li>
</ul>

<h2 id="132">1.3.2</h2>

<h5 id="added-61">Added</h5>
<ul>
  <li>Added support for Braze Feedback through the new appboy.submitFeedback method.</li>
</ul>

<h5 id="fixed-93">Fixed</h5>
<ul>
  <li>In-App Messages now track click analytics even when the click action is “None.”</li>
  <li>Prevent Mobile Safari in Private Browsing mode from throwing an exception. This issue was introduced in 1.3.0.</li>
</ul>

<h2 id="131">1.3.1</h2>

<h5 id="fixed-94">Fixed</h5>
<ul>
  <li>Prevent Firefox from throwing an exception when in Private Browsing mode. This issue was introduced in 1.3.0.</li>
</ul>

<h2 id="130">1.3.0</h2>

<h5 id="breaking-3">Breaking</h5>
<ul>
  <li>The <code class="language-plaintext highlighter-rouge">inAppMessages</code> parameter to <code class="language-plaintext highlighter-rouge">appboy.subscribeToNewInAppMessages</code> subscribers may now contain <code class="language-plaintext highlighter-rouge">ab.ControlMessage</code> objects.</li>
</ul>

<h5 id="added-62">Added</h5>
<ul>
  <li>Adds support for triggered in-app messages.</li>
</ul>

<h5 id="fixed-95">Fixed</h5>
<ul>
  <li>Fixed a bug where news feed cards weren’t always immediately being marked as read during scrolling.</li>
</ul>

<h5 id="changed-47">Changed</h5>
<ul>
  <li>All iOS devices will now report their OS as “iOS” instead of “iPhone/iPod” or “iPad”.</li>
</ul>

<h2 id="122">1.2.2</h2>

<h5 id="fixed-96">Fixed</h5>
<ul>
  <li>Fixed a javascript error that could occur when attempting to showFeed before the body has loaded.</li>
  <li>Made in-app message buttons explicitly display:inline-block so that they still display correctly if the site is styling buttons as display:block.</li>
</ul>

<h2 id="121">1.2.1</h2>

<h5 id="fixed-97">Fixed</h5>
<ul>
  <li>The service worker now reads Braze’s backend URL from IndexedDB, which allows web push to function for clients with custom Braze endpoints.</li>
  <li>isPushBlocked now returns false when isPushSupported is false instead of erroring.</li>
</ul>

<h2 id="120">1.2.0</h2>

<h5 id="breaking-4">Breaking</h5>
<ul>
  <li>Restyled the news feed for improved legibility with a wider variety of card content. If you have existing news feed css customization this may be a breaking change.</li>
</ul>

<h5 id="added-63">Added</h5>
<ul>
  <li>Supports web push (on browsers implementing the w3c spec, with or without payloads - i.e. Chrome, Firefox).</li>
  <li>Introduced appboy.toggleFeed as a convenience method - it simply calls appboy.showFeed or appboy.destroyFeed based on whether there’s currently a feed showing.</li>
</ul>

<h5 id="fixed-98">Fixed</h5>
<ul>
  <li>Buttonless FullScreen and Modal messages now respect body click actions from the dashboard.</li>
</ul>

<h5 id="changed-48">Changed</h5>
<ul>
  <li>To reduce the datapoint impact of the high number of anonymous users on the web, in-app messages are no longer. automatically refreshed for new, anonymous users on their first openSession call. You can override this behavior and force an in-app message refresh by manually calling appboy.requestInAppMessageRefresh.</li>
  <li>In-App Messages may now be dismissed with a click on the greyed-out background of the page. This behavior may be prevented by passing requireExplicitInAppMessageDismissal:true to <code class="language-plaintext highlighter-rouge">appboy.initialize</code>.</li>
</ul>

<h2 id="111">1.1.1</h2>

<h5 id="added-64">Added</h5>
<ul>
  <li>Expanded browser detection to recognize more niche browsers.</li>
</ul>

<h5 id="fixed-99">Fixed</h5>
<ul>
  <li>Fixed an issue which would cause some Android devices to be detected as Linux.</li>
</ul>

<h2 id="110">1.1.0</h2>

<h5 id="added-65">Added</h5>
<ul>
  <li>Introduced <code class="language-plaintext highlighter-rouge">appboy.logFeedDisplayed</code>, which is called automatically when using <code class="language-plaintext highlighter-rouge">appboy.display.showFeed</code>.</li>
</ul>

<h5 id="fixed-100">Fixed</h5>
<ul>
  <li>Fixed a race condition which could cause events to be double-counted if the user had the site open in very many tabs at once.</li>
</ul>

<h5 id="changed-49">Changed</h5>
<ul>
  <li>News feed and in-app message links now open in the same tab.</li>
</ul>

<h2 id="101">1.0.1</h2>

<h5 id="fixed-101">Fixed</h5>
<ul>
  <li>The SDK now logs correctly to the console when enableLogging is true (or toggleAppboyLogging has been called) and no custom logger has been specified.</li>
</ul>

<h2 id="100">1.0.0</h2>

<h5 id="added-66">Added</h5>
<ul>
  <li>Respect blacklisted custom events, attributes, and purchases.</li>
</ul>

<h5 id="removed-1">Removed</h5>
<ul>
  <li>Removed the setBio method on ab.User in accordance with the deprecation of that user property across the Braze platform.</li>
</ul>

<h2 id="024">0.2.4</h2>

<h5 id="fixed-102">Fixed</h5>
<ul>
  <li>Fixed an issue which was causing the in-app message refresh throttle not to persist beyond a single page load.</li>
</ul>

<h2 id="023">0.2.3</h2>

<h5 id="added-67">Added</h5>
<ul>
  <li>Introduce <code class="language-plaintext highlighter-rouge">appboy.display.destroyFeed</code> method to allow integrators to implement a toggle feed button or otherwise hide the feed from code.</li>
</ul>

<h5 id="fixed-103">Fixed</h5>
<ul>
  <li>Prevent potential race condition which could cause news feed cards to not be marked as read for a short amount of time.</li>
</ul>

<h5 id="removed-2">Removed</h5>
<ul>
  <li>Remove the news feed z-index. If necessary, the z-index can be set manually via CSS: <code class="language-plaintext highlighter-rouge">.ab-feed { z-index: }</code>.</li>
</ul>

<h2 id="022">0.2.2</h2>

<h5 id="fixed-104">Fixed</h5>
<ul>
  <li>Fix issue where already-cached news feed cards were not properly having impressions logged when the news feed was first shown.</li>
</ul>

<h5 id="changed-50">Changed</h5>
<ul>
  <li>Minor improvements to In-App Message styling.</li>
</ul>

<h2 id="021">0.2.1</h2>

<h5 id="added-68">Added</h5>
<ul>
  <li>Give the news feed a z-index just below bootstrap modal backdrops.</li>
</ul>

<h5 id="fixed-105">Fixed</h5>
<ul>
  <li>Support legacy Internet Explorer (complete IE9 support, generally functional IE8 support).</li>
</ul>

<h5 id="changed-51">Changed</h5>
<ul>
  <li>Ignore in-app messages with an unknown type (prevents future message types from be inappropriately displayed on versions of the sdk which don’t yet support them).</li>
</ul>

<h2 id="020">0.2.0</h2>

<h5 id="added-69">Added</h5>
<ul>
  <li>Added Braze news feed support.</li>
</ul>

<h2 id="015">0.1.5</h2>

<h5 id="fixed-106">Fixed</h5>
<ul>
  <li>Correctly identify IE11.</li>
</ul>

<h2 id="014">0.1.4</h2>

<h5 id="fixed-107">Fixed</h5>
<ul>
  <li>Fixed issue where SlideUp message clicks with a clickAction of URI were not being respected.</li>
  <li>Fixed issue where Date custom attributes, custom event properties, and purchase properties were not being recognized as Dates by the Braze platform.</li>
</ul>

<h2 id="013">0.1.3</h2>

<h5 id="added-70">Added</h5>
<ul>
  <li>Add support for more purchase currencies, allow lowercase currencies.</li>
</ul>

<h5 id="changed-52">Changed</h5>
<ul>
  <li>Use millisecond precision when logging events.</li>
</ul>

<h2 id="012">0.1.2</h2>

<h5 id="changed-53">Changed</h5>
<ul>
  <li>Introduce optional doNotLoadFontAwesome initialization option and additionally don’t load FontAwesome if fontawesome.css or fontawesome.min.css are already on the page.</li>
  <li>More minor improvements to In-App Message styling.</li>
</ul>

<h2 id="011">0.1.1</h2>

<h5 id="changed-54">Changed</h5>
<ul>
  <li>Various minor improvements to SlideUp styling.</li>
</ul>

<h2 id="010">0.1.0</h2>

<h5 id="added-71">Added</h5>
<ul>
  <li>Support in-app messages.</li>
</ul>

<h2 id="005">0.0.5</h2>

<h5 id="fixed-108">Fixed</h5>
<ul>
  <li>Fixed critical issue which caused browser tabs to become unresponsive with no network connection.</li>
</ul>

<h2 id="004">0.0.4</h2>

<h5 id="fixed-109">Fixed</h5>
<ul>
  <li>Defend against NS_ERROR_FILE_CORRUPTED (corrupted browser SQLite database) and more generally against inability to use localStorage.</li>
</ul>

<h2 id="003">0.0.3</h2>

<h5 id="changed-55">Changed</h5>
<ul>
  <li>Provide better backend error messages.</li>
</ul>

<h2 id="002">0.0.2</h2>

<h5 id="fixed-110">Fixed</h5>
<ul>
  <li>Fixed a bug where due to minification, locally stored data was version-specific.</li>
</ul>

<h2 id="001">0.0.1</h2>

<h5 id="fixed-111">Fixed</h5>
<ul>
  <li>Fixed bug where multibyte UTF-8 characters were being rejected for various attributes.</li>
  <li>Harden usage of localStorage slightly.</li>
</ul>

<h5 id="changed-56">Changed</h5>
<ul>
  <li>Allow setLogger to be called before initialize.</li>
</ul>

<h2 id="000">0.0.0</h2>

<ul>
  <li>Initial release with core functionality.</li>
</ul>




**Tip:**


You can also find a copy of the [Android Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md).



<h2 id="4210">42.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.1.0">Release Date</a></p>

<h5 id="added">Added</h5>
<ul>
  <li>Added support for Android 17 (API 37).</li>
  <li>Added <code class="language-plaintext highlighter-rouge">BannerView.onDismissCallback</code> for integrators to run custom logic when a Banner is dismissed.</li>
</ul>

<h2 id="4200">42.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v42.0.0">Release Date</a></p>

<h4 id="breaking">Breaking</h4>
<ul>
  <li>Updated Kotlin from 2.0.20 to 2.2.20.
    <ul>
      <li>Updated Kotlin Coroutines from 1.8.1 to 1.10.2.</li>
      <li>Updated Kotlin Serialization from 1.8.0 to 1.9.0.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed">Fixed</h5>
<ul>
  <li>Fixed an issue where non-HTML In-App Message view creation was dispatched to a background thread, causing an <code class="language-plaintext highlighter-rouge">IllegalArgumentException</code> when image loaders like Glide require the main thread. See <a href="https://github.com/braze-inc/braze-android-sdk/issues/102">#102</a> for details.</li>
  <li>Fixed an issue where in-app messages from a previous user session could be presented after <code class="language-plaintext highlighter-rouge">changeUser()</code> is called. On user change, the in-app message stack, event map, and any carryover or unregistered messages are now unconditionally cleared.</li>
  <li>Fixed an issue on API 36+ where pressing the Back button to dismiss an in-app message could also close the app or navigate back.</li>
  <li>Fixed an issue where expired Banners would be returned in <code class="language-plaintext highlighter-rouge">Braze.subscribeToBannersUpdates()</code>.</li>
  <li>Fixed R8 optimized resource shrinking stripping custom <code class="language-plaintext highlighter-rouge">res/values</code> that Braze requires to operate when <code class="language-plaintext highlighter-rouge">android.r8.optimizedResourceShrinking</code> is enabled (Gradle 9.x). See <a href="https://github.com/braze-inc/braze-android-sdk/issues/84">#84</a> for details.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">setDateOfBirth</code> accepted out-of-range or negative date values instead of rejecting them.</li>
  <li>Fixed a potential ANR when registering for Braze updates during <code class="language-plaintext highlighter-rouge">Activity</code> lifecycle (for example when using <code class="language-plaintext highlighter-rouge">BrazeActivityLifecycleCallbackListener</code>). That registration no longer blocks the UI thread.</li>
</ul>

<h5 id="added-1">Added</h5>
<ul>
  <li>Added a config field <code class="language-plaintext highlighter-rouge">BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled()</code> to configure the SDK to automatically apply window insets to HTML In-App messages.
    <ul>
      <li>By default, this value is true.</li>
    </ul>
  </li>
  <li>Added support for dismissing slideup in-app messages by vertical swipes. Slideups from the bottom can be dismissed by swiping down and slideups from the top can be dismissed by swiping up.</li>
</ul>

<h2 id="4111">41.1.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.1.1">Release Date</a></p>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Fixed an issue where calling <code class="language-plaintext highlighter-rouge">wipeData()</code> could result in SDK read/writes not working until the app was restarted.
    <ul>
      <li>All data would still be properly wiped from storage after calls to <code class="language-plaintext highlighter-rouge">wipeData()</code>.</li>
      <li>This issue would manifest as <code class="language-plaintext highlighter-rouge">CancellationException</code> or <code class="language-plaintext highlighter-rouge">StorageException</code> in logs and would not result in an app crash.</li>
    </ul>
  </li>
</ul>

<h2 id="4110">41.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.1.0">Release Date</a></p>

<h5 id="changed">Changed</h5>
<ul>
  <li>Updated the Coil library from 3.1.0 to 3.2.0.</li>
</ul>

<h2 id="4100">41.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0">Release Date</a></p>

<h4 id="breaking-1">Breaking</h4>
<ul>
  <li>Renamed <code class="language-plaintext highlighter-rouge">BrazeConfig.Builder.setIsLocationCollectionEnabled()</code> to <code class="language-plaintext highlighter-rouge">setIsAutomaticLocationCollectionEnabled()</code>.</li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">BrazeConfig.isLocationCollectionEnabled</code> to <code class="language-plaintext highlighter-rouge">isAutomaticLocationCollectionEnabled</code>.</li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">BrazeConfigurationProvider.isLocationCollectionEnabled</code> to <code class="language-plaintext highlighter-rouge">isAutomaticLocationCollectionEnabled</code>.</li>
</ul>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Fixed an issue where manual location tracking was being blocked by automatic location tracking.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazeUser.setLastKnownLocation()</code> now works independently of the automatic location collection setting. Customers can use automatic collection, manual tracking, both, or neither.</li>
    </ul>
  </li>
  <li>Fixed a memory leak in the data persistence layer.</li>
</ul>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>Updated Coil library to Coil3.</li>
</ul>

<h2 id="4020">40.2.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v40.2.0">Release Date</a></p>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Fixed a potential memory leak in the activity lifecycle. See <a href="https://github.com/braze-inc/braze-android-sdk/issues/86">#86</a> for details.</li>
  <li>Fixed an issue when pressing the Back button from the Accessibility menu to dismiss an in-app message, occurring on Samsung devices running on Android 16 or higher.</li>
</ul>

<h2 id="4011">40.1.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v40.1.1">Release Date</a></p>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Fixed a potential memory leak in session management. See <a href="https://github.com/braze-inc/braze-android-sdk/issues/86">#86</a> for details.</li>
  <li>Fixed an issue with multiple sessions being opened when transparent activities are present.</li>
</ul>

<h2 id="4010">40.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v40.1.0">Release Date</a></p>

<h5 id="fixed-5">Fixed</h5>
<ul>
  <li>Fixed an error that could occur when a WebView failed to render correctly.</li>
  <li>Fixed an issue with location collection on pre-Android 11 devices.</li>
  <li>Fixed an issue that could cause an IAM with a deeplink click action to become unresponsive after being clicked.</li>
</ul>

<h5 id="added-2">Added</h5>
<ul>
  <li>Added the ability to call <code class="language-plaintext highlighter-rouge">setGoogleAdvertisingId</code> with <code class="language-plaintext highlighter-rouge">null</code> or a blank string in order to completely opt out users from ad tracking.</li>
</ul>

<h2 id="4002">40.0.2</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v40.0.2">Release Date</a></p>

<h5 id="fixed-6">Fixed</h5>
<ul>
  <li>Fixed an issue with <code class="language-plaintext highlighter-rouge">com.braze.Braze.Companion#disableDelayedInitialization</code> on low end devices.</li>
</ul>

<h2 id="4001">40.0.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v40.0.1">Release Date</a></p>

<h5 id="changed-2">Changed</h5>
<ul>
  <li>Improved state management of the networking stack to be more efficient with requests after the app is resumed.</li>
</ul>

<h2 id="4000">40.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v40.0.0">Release Date</a></p>

<h4 id="breaking-2">Breaking</h4>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">InAppMessageCloser</code>.
    <ul>
      <li>Use <code class="language-plaintext highlighter-rouge">BrazeInAppMessageManager.hideCurrentlyDisplayingInAppMessage()</code> to hide in-app messages and <code class="language-plaintext highlighter-rouge">IInAppMessage#setAnimateOut()</code> for controlling exit animations.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-7">Fixed</h5>
<ul>
  <li>Fixed an issue where calls to <code class="language-plaintext highlighter-rouge">wipeData()</code> followed by <code class="language-plaintext highlighter-rouge">enableSdk()</code> could result in certain SDK data being unusable until the app was restarted.
    <ul>
      <li>All data would still be properly wiped from storage after calls to <code class="language-plaintext highlighter-rouge">wipeData()</code>.</li>
      <li>This issue would manifest as <code class="language-plaintext highlighter-rouge">IllegalStateException: There are multiple DataStores active for the same file</code> in logcat and would not result in an app crash.</li>
      <li>This issue does not result in any data loss.</li>
    </ul>
  </li>
  <li>Fixed an issue where anonymous user transitions to identified users could cause SDK Auth errors when push token data was present.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">BrazeInAppMessageManager</code> could misreport incoming in-app messages as not belonging to the current user after disabling and re-enabling the SDK.</li>
</ul>

<h5 id="added-3">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">IBraze.subscribeToChangeUserEvents()</code>.</li>
</ul>

<h5 id="changed-3">Changed</h5>
<ul>
  <li>Removes <code class="language-plaintext highlighter-rouge">DeviceKey.RESOLUTION</code>.</li>
</ul>

<h2 id="3900">39.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v39.0.0">Release Date</a></p>

<h4 id="breaking-3">Breaking</h4>
<ul>
  <li>Changed the behavior of <code class="language-plaintext highlighter-rouge">Braze.subscribeToContentCardsUpdates()</code> to immediately return cached Content Cards after registering the subscriber.</li>
</ul>

<h5 id="fixed-8">Fixed</h5>
<ul>
  <li>Fixed a race condition in <code class="language-plaintext highlighter-rouge">BrazeBootReceiver</code> which could cause a crash upon SDK initialization.</li>
</ul>

<h5 id="changed-4">Changed</h5>
<ul>
  <li>Increased the socket read timeout for all network requests to 25 seconds.</li>
</ul>

<h2 id="3800">38.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0">Release Date</a></p>

<h4 id="breaking-4">Breaking</h4>
<ul>
  <li>Removed News Feed.
    <ul>
      <li>Removed <code class="language-plaintext highlighter-rouge">BrazeImageSwitcher</code>, <code class="language-plaintext highlighter-rouge">CardKey.Provider</code>, and <code class="language-plaintext highlighter-rouge">CardCategory</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">Card</code> objects now only represent Content Cards.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">Card.updated</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">IBraze.logFeedDisplayed()</code>, <code class="language-plaintext highlighter-rouge">IBraze.requestFeedRefreshFromCache()</code>, <code class="language-plaintext highlighter-rouge">IBraze.requestFeedRefresh()</code>, <code class="language-plaintext highlighter-rouge">IBraze.subscribeToFeedUpdates(subscriber)</code>, <code class="language-plaintext highlighter-rouge">IBraze.logFeedCardImpression(cardId)</code>, and <code class="language-plaintext highlighter-rouge">IBraze.logFeedCardClick(cardId)</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">BrazeConfig.isNewsFeedVisualIndicatorOn</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-4">Added</h5>
<ul>
  <li>Added support for delayed SDK initialization.
    <ul>
      <li>To enable delayed initialization, call <code class="language-plaintext highlighter-rouge">Braze.enableDelayedInitialization(context, analyticsBehavior)</code>.</li>
      <li>To disable delayed initialization, call <code class="language-plaintext highlighter-rouge">Braze.disableDelayedInitialization(context)</code>.</li>
    </ul>
  </li>
  <li>Added predictive back animations to full view in-app messages on gesture navigation modes on API 34+, and 3-button navigation modes on API 36+. See the <a href="https://developer.android.com/about/versions/16/behavior-changes-all">Android 16 Documentation</a> for more details.</li>
  <li>Moved the method internals of <code class="language-plaintext highlighter-rouge">BrazeFirebaseMessagingService.onNewToken()</code> to the companion object for easier behavior overriding.</li>
  <li>Added support for new <code class="language-plaintext highlighter-rouge">Banner</code> properties by adding the following methods:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">banner.getStringProperty(key)</code> for accessing <code class="language-plaintext highlighter-rouge">String</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getNumberProperty(key)</code> for accessing <code class="language-plaintext highlighter-rouge">Number</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getBooleanProperty(key)</code> for accessing <code class="language-plaintext highlighter-rouge">Boolean</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getJSONProperty(key)</code> for accessing <code class="language-plaintext highlighter-rouge">JSONObject</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getImageProperty(key)</code> for accessing image URL properties as <code class="language-plaintext highlighter-rouge">String</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getTimestampProperty(key)</code> for accessing Unix UTC millisecond timestamp properties as <code class="language-plaintext highlighter-rouge">Long</code>s.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-5">Changed</h5>
<ul>
  <li>Changed the behavior of templated In-App Messages to not automatically retry on endpoint errors to match the behavior of the iOS and Web SDKs.</li>
  <li>The default client-side rate limiting values for Banners refresh has been increased. For more information on SDK rate limiting, please refer to the <a href="https://www.braze.com/docs/developer_guide/sdk_integration/rate_limits#braze-sdk-rate-limits">Braze Developer Guide</a>.</li>
</ul>

<h2 id="3700">37.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v37.0.0">Release Date</a></p>

<h4 id="breaking-5">Breaking</h4>
<ul>
  <li>Removed the config field <code class="language-plaintext highlighter-rouge">BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled()</code> and defaulted its behavior to true. The SDK will now unconditionally apply window insets to all HTML In-App Messages.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">IBraze.requestContentCardsRefresh(boolean)</code>. Please instead use <code class="language-plaintext highlighter-rouge">IBraze.requestContentCardsRefresh()</code> and <code class="language-plaintext highlighter-rouge">IBraze.requestContentCardsRefreshFromCache()</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">BrazeConfig.Builder.setDeviceObjectWhitelist()</code>. Please use <code class="language-plaintext highlighter-rouge">BrazeConfig.Builder.setDeviceObjectAllowlist()</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">BrazeConfig.Builder.setDeviceObjectWhitelistEnabled()</code>. Please use <code class="language-plaintext highlighter-rouge">BrazeConfig.Builder.setDeviceObjectAllowlistEnabled()</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">ContentCardsUpdatedEvent.getLastUpdatedInSecondsFromEpoch</code>. Please instead use <code class="language-plaintext highlighter-rouge">getTimestampSeconds()</code>(Java) or <code class="language-plaintext highlighter-rouge">timestampSeconds</code>(Kotlin).</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">FeatureFlag.getTimestamp(key)</code>. Please use <code class="language-plaintext highlighter-rouge">FeatureFlag.getTimestampProperty(key)</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">BrazeWebViewClient.shouldInterceptRequest(view, url)</code>. Please use <code class="language-plaintext highlighter-rouge">BrazeWebViewClient.shouldInterceptRequest(view, request)</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">IBraze.getInstallTrackingId()</code>. Please use <code class="language-plaintext highlighter-rouge">IBraze.deviceId</code> instead.</li>
</ul>

<h5 id="fixed-9">Fixed</h5>
<ul>
  <li>Fixed an issue where a <code class="language-plaintext highlighter-rouge">LeakedClosableViolation</code> would occur when disabling and re-enabling the SDK.</li>
  <li>Fixed an issue with Android TalkBack announcing “double tap to activate” on header and body text in In-App Messages.</li>
</ul>

<h5 id="added-5">Added</h5>
<ul>
  <li>Added support for Android 16 (API 36).
    <ul>
      <li>Note that apps targeting API 36 should update to this SDK version.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">shutdown()</code> to <code class="language-plaintext highlighter-rouge">IBrazeImageLoader</code> to allow for cleanup of resources.</li>
  <li>Improved accessibility support across In-App Messages and Content Cards by introducing alt text for images (by setting their content description).</li>
  <li>Added the ability to pass <code class="language-plaintext highlighter-rouge">null</code> to <code class="language-plaintext highlighter-rouge">BrazeUser.setGender(gender)</code> in order to unset the gender value.</li>
</ul>

<h5 id="changed-6">Changed</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">UriAction.openUriWithActionViewFromPush</code>, <code class="language-plaintext highlighter-rouge">UriAction.openUriWithWebViewActivity</code>, and <code class="language-plaintext highlighter-rouge">UriAction.openUriWithWebViewActivityFromPush</code> are marked as <code class="language-plaintext highlighter-rouge">open</code> and can now be overridden.</li>
</ul>

<h2 id="3600">36.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v36.0.0">Release Date</a></p>

<blockquote>
  <p>[!IMPORTANT]
This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. Note that while we are re-introducing the ability to compile, we are not reintroducing formal support for &lt;API 25, and cannot guarantee that the SDK will work as intended on devices running those versions.</p>

  <p>If your app supports those versions, you should:</p>
  <ul>
    <li>Validate your integration of the SDK works as intended on physical devices (not just emulators) for those API versions.</li>
    <li>If you cannot validate expected behavior, you must either call <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html">disableSDK</a>, or not initialize the SDK on those versions. Otherwise, you may cause unintended side effects or degraded performance on your end users’ devices.</li>
  </ul>
</blockquote>

<h4 id="breaking-6">Breaking</h4>
<ul>
  <li>Fixed an issue where In-App Messages would cause a read on the main thread.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazeInAppMessageManager.displayInAppMessage</code> is now a Kotlin suspend function.</li>
      <li>If you do not call this function directly, you do not need to make any changes.</li>
    </ul>
  </li>
  <li>AndroidX Compose BOM updated to 2025.04.01 to handle updates in the Jetpack Compose APIs.</li>
</ul>

<h5 id="fixed-10">Fixed</h5>
<ul>
  <li>Fixed a potential issue where the SDK could incorrectly calculate in-flight In-App Message requests and prevent new In-App Messages from being triggered.</li>
  <li>Ensured that Content Cards, In-App Messages, Feature Flags, and Banners are cleared when calling <code class="language-plaintext highlighter-rouge">Braze.wipeData()</code>.</li>
  <li>Set default background of <code class="language-plaintext highlighter-rouge">BannerView</code> to transparent.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">BrazeInAppMessageManager.activity</code> would point to the previous activity when an Activity on the blocklist was active.</li>
  <li>Fixed an issue where In-App Messages would continue consuming predictive back callbacks after the message was dismissed/closed.
    <ul>
      <li>For more detail: The predictive back callback not removed when the In-App Message was closed via the close button (or any other non-back dismissal method). This caused two back button invocations to be needed to trigger the host Activity/Fragment’s predictive back callback.</li>
    </ul>
  </li>
</ul>

<h5 id="added-6">Added</h5>
<ul>
  <li>Added a parameter <code class="language-plaintext highlighter-rouge">enablePullToRefresh</code> to <code class="language-plaintext highlighter-rouge">ContentCardsList</code> in Jetpack Compose to allow for disabling pull-to-refresh behavior.</li>
</ul>

<h5 id="changed-7">Changed</h5>
<ul>
  <li>Removed the deprecated <code class="language-plaintext highlighter-rouge">announceForAccessibility</code> in favor of <code class="language-plaintext highlighter-rouge">accessibilityLiveRegion</code> and <code class="language-plaintext highlighter-rouge">contentDescription</code> for accessibility TalkBack.</li>
  <li>Removed any displayed In-App Messages when calling <code class="language-plaintext highlighter-rouge">Braze.changeUser()</code>.</li>
  <li>Modified <code class="language-plaintext highlighter-rouge">BrazeActivityLifecycleCallbackListener</code> to keep track of the latest activity in use.
    <ul>
      <li>This is used to handle push permission prompts for various channels (ie. In-App Messages, Banners, etc).</li>
      <li>If you plan on using push permission prompts from a channel other than In-App Messages, you should make sure you’re registering <code class="language-plaintext highlighter-rouge">BrazeActivityLifecycleCallbackListener</code> in your Application class.</li>
    </ul>
  </li>
  <li>Set <code class="language-plaintext highlighter-rouge">allowFileAccess</code> to <code class="language-plaintext highlighter-rouge">false</code> in <code class="language-plaintext highlighter-rouge">BannerView</code>.</li>
</ul>

<h2 id="3500">35.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v35.0.0">Release Date</a></p>

<h4 id="breaking-7">Breaking</h4>
<ul>
  <li>HTML In-App Messages will now persist the WebView when the app is put in the background.
    <ul>
      <li>To disable this feature, use <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_persist_webview_when_backgrounding_app"&gt;false&lt;/bool&gt;</code> in your <code class="language-plaintext highlighter-rouge">braze.xml</code> file.</li>
    </ul>
  </li>
  <li>Removes the ability to control whether the SDK prevents showing In-App Messages to different users in certain edge cases.
    <ul>
      <li>Removes the option to configure via <code class="language-plaintext highlighter-rouge">braze.xml</code> through <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_prevent_in_app_message_display_for_different_user"&gt;true&lt;/bool&gt;</code>.</li>
      <li>Removes the option to configure via runtime configuration through <code class="language-plaintext highlighter-rouge">BrazeConfig.setShouldPreventInAppMessageDisplayForDifferentUsers()</code>.</li>
      <li>The SDK will now always behave as if this configuration option were set to true.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-11">Fixed</h5>
<ul>
  <li>Control banners will invoke <code class="language-plaintext highlighter-rouge">bannerView.heightCallback</code> with a value of 0.0. Previously it was not being called for control banners.</li>
  <li>Fixed an issue where sending a test banner from the dashboard would not update immediately.</li>
</ul>

<h5 id="added-7">Added</h5>
<ul>
  <li>Added the ability to get success and failure callbacks for <code class="language-plaintext highlighter-rouge">BrazeUser.requestBannersRefresh()</code>.</li>
  <li>Allows user to subscribe to Banner update errors with <code class="language-plaintext highlighter-rouge">Braze.subscribeToBannersErrors()</code>.</li>
</ul>

<h2 id="3400">34.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v34.0.0">Release Date</a></p>

<h4 id="breaking-8">Breaking</h4>
<ul>
  <li>Updated the minimum SDK version from 21 (Lollipop) to 25 (Nougat).</li>
</ul>

<h5 id="added-8">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazeNotificationPayload.isSilentPush</code> to check if a notification payload is a silent push.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazeUser.setLineId(String)</code> to set the <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/line">LINE</a> ID of a user.
    <ul>
      <li>Adds <code class="language-plaintext highlighter-rouge">brazeBridge.getUser().setLineId(String)</code> to the javascript interface for HTML In-App Messages and Banners.</li>
    </ul>
  </li>
  <li>Added the ability to forcibly pad In-App Messages with the height of the status bar.
    <ul>
      <li>Configured via <code class="language-plaintext highlighter-rouge">braze.xml</code> through <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_in_app_message_add_status_bar_padding"&gt;true&lt;/bool&gt;</code>.</li>
      <li>Can also be configured via runtime configuration through <code class="language-plaintext highlighter-rouge">BrazeConfig.setShouldAddStatusBarPaddingToInAppMessages()</code>.</li>
      <li>Defaults to false. You should not change this value unless you’re seeing issues with In-App Messages close button being obscured by the status bar when using a cross-platform framework like React Native or Flutter.</li>
    </ul>
  </li>
  <li>Added a callback in <code class="language-plaintext highlighter-rouge">BannerJavascriptInterface</code> for dynamically setting the height of a Banner.</li>
</ul>

<h4 id="fixed-12">Fixed</h4>
<ul>
  <li>Fixed an issue where automatic location collection being disabled would also disable Geofences.</li>
</ul>

<h2 id="3310">33.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v33.1.0">Release Date</a></p>

<h5 id="fixed-13">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">ContentCardsFragment</code> would not show the empty state if the user had only control cards.</li>
</ul>

<h5 id="added-9">Added</h5>
<ul>
  <li>Adds support for the Braze Banner Cards product.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazeWebViewClient</code> to facilitate the creation of <code class="language-plaintext highlighter-rouge">WebViewClient</code>s in Banners and In-App Messages.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">BannerWebViewClient</code>, which extends <code class="language-plaintext highlighter-rouge">BrazeWebViewClient</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">InAppMessageWebViewClient</code> now extends <code class="language-plaintext highlighter-rouge">BrazeWebViewClient</code>.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">JavascriptInterfaceBase</code> to simplify the creation of JavaScript interfaces for Banners and In-App Messages.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">BannerJavascriptInterface</code>, which extends <code class="language-plaintext highlighter-rouge">JavascriptInterfaceBase</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">InAppMessageJavascriptInterface</code> now extends <code class="language-plaintext highlighter-rouge">JavascriptInterfaceBase</code>.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">IBannerWebViewClientListener</code> interface for Banner WebViewClient listeners.</li>
  <li>Added an optional button id parameter to <code class="language-plaintext highlighter-rouge">IInAppMessage.logClick</code>.</li>
</ul>

<h5 id="changed-8">Changed</h5>
<ul>
  <li>Changed the location of <code class="language-plaintext highlighter-rouge">brazeBridge</code> to be located in file <code class="language-plaintext highlighter-rouge">braze-html-bridge.js</code>. <code class="language-plaintext highlighter-rouge">brazeBridge</code> is now accessible in both Banners and In-App Messages.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">braze-html-in-app-message-bridge.js</code> is now deprecated and will be removed in a future version of the SDK, in favor of <code class="language-plaintext highlighter-rouge">braze-html-bridge.js</code>.</li>
    </ul>
  </li>
  <li>Changed properties in <code class="language-plaintext highlighter-rouge">AttributionData</code> from non-nullable to nullable to allow for optional values.</li>
</ul>

<h2 id="3300">33.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v33.0.0">Release Date</a></p>

<h5 id="breaking-9">Breaking</h5>
<ul>
  <li>Updated Kotlin from 1.8 to Kotlin 2.0.</li>
</ul>

<h5 id="fixed-14">Fixed</h5>
<ul>
  <li>Braze HTML In-App Message bridge method <code class="language-plaintext highlighter-rouge">incrementCustomUserAttribute()</code> will use the provided value as the increment amount instead of always incrementing by 1.</li>
  <li>Fixed an issue where In-App Message text alignments would not match what was set in the dashboard in some cases.
    <ul>
      <li>Removed <code class="language-plaintext highlighter-rouge">android:supportsRtl="true"</code> from android-sdk-ui <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code>. You should have this in your application <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">android:textAlignment="viewStart"</code> from the In-App Message layouts, since this is sent by the server.</li>
    </ul>
  </li>
  <li>Fixed an issue where Content Cards and Feature Flags were not refreshing after a session started due to a session timeout.</li>
  <li>Fixed an issue with SDK Authentication where tokens that expired and refreshed mid session would be treated as failed.</li>
</ul>

<h5 id="changed-9">Changed</h5>
<ul>
  <li>Braze HTML In-App Message bridge method will now also accept strings for <code class="language-plaintext highlighter-rouge">incrementCustomUserAttribute()</code>, <code class="language-plaintext highlighter-rouge">setDateOfBirth()</code>, <code class="language-plaintext highlighter-rouge">setCustomLocationAttribute()</code>, and <code class="language-plaintext highlighter-rouge">logPurchase()</code>.</li>
</ul>

<h2 id="3210">32.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v32.1.0">Release Date</a></p>

<h5 id="fixed-15">Fixed</h5>
<ul>
  <li>Fixed an issue where geofence events could not be sent when the app is in the background.</li>
  <li>Fixed an issue where In-App Messages would fail to be dismissed when the host app is using the predictive back gesture.</li>
</ul>

<h5 id="added-10">Added</h5>
<ul>
  <li>Added support for an upcoming Braze SDK Debugging tool.</li>
  <li>Added the ability to prevent certain edge cases where the SDK could show In-App Messages to different users than the one that triggered the In-App Message.
    <ul>
      <li>Configured via <code class="language-plaintext highlighter-rouge">braze.xml</code> through <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_prevent_in_app_message_display_for_different_user"&gt;true&lt;/bool&gt;</code>.</li>
      <li>Can also be configured via runtime configuration through <code class="language-plaintext highlighter-rouge">BrazeConfig.setShouldPreventInAppMessageDisplayForDifferentUsers()</code>.</li>
      <li>Defaults to false. Note that even when false, the SDK will still prevent most cases of showing In-App Messages to different users. This configuration option is designed to prevent edge cases such as when the user changes while on a <code class="language-plaintext highlighter-rouge">BrazeActivityLifecycleCallbackListener</code> blocked Activity or when a mismatched message is still in the stack.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-10">Changed</h5>
<ul>
  <li>Changed the behavior of the <code class="language-plaintext highlighter-rouge">Braze.getDeviceId()</code> method to return a different device ID based on the API key used to initialize the SDK.</li>
</ul>

<h2 id="3200">32.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v32.0.0">Release Date</a></p>

<h5 id="breaking-10">Breaking</h5>
<ul>
  <li>Fixed issue where cards with duplicate IDs would cause a crash in Jetpack Compose Content Cards.
    <ul>
      <li>If you manually add cards, please ensure that they have unique IDs.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-16">Fixed</h5>
<ul>
  <li>Fixed an issue where closing an In-App Message could throw an error if the previously focused <code class="language-plaintext highlighter-rouge">View</code> was removed.</li>
  <li>Fixed an issue where some In-App Messages could display after their expiration time.</li>
  <li>Fixed an issue with In-App Message and Content Cards not displaying RTL language properly.</li>
  <li>Fixed an issue where logging In-App Message impression or clicks could result in blocking the main thread.</li>
</ul>

<h5 id="added-11">Added</h5>
<ul>
  <li>Added support for Android 15 (API 35).
    <ul>
      <li>Note that apps targeting API 35 should update to this SDK version.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-11">Changed</h5>
<ul>
  <li>Changed the behavior of <code class="language-plaintext highlighter-rouge">Braze.wipeData()</code> to retain external subscriptions (like <code class="language-plaintext highlighter-rouge">Braze.subscribeToContentCardsUpdates()</code>) after being called.</li>
</ul>

<h2 id="3110">31.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v31.1.0">Release Date</a></p>

<h5 id="fixed-17">Fixed</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">getTimestampProperty(key)</code> to <code class="language-plaintext highlighter-rouge">FeatureFlag</code> and deprecated <code class="language-plaintext highlighter-rouge">getTimestamp(key)</code> for consistency.</li>
</ul>

<h5 id="added-12">Added</h5>
<ul>
  <li>Added Azerbaijani language translations for Braze UI elements.</li>
</ul>

<h2 id="3100">31.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v31.0.0">Release Date</a></p>

<h4 id="breaking-11">Breaking</h4>
<ul>
  <li><code class="language-plaintext highlighter-rouge">BrazeImageUtils::getBitmap</code> now returns a <code class="language-plaintext highlighter-rouge">BitmapAndHeaders</code> object instead of just a <code class="language-plaintext highlighter-rouge">Bitmap</code>. This object contains the <code class="language-plaintext highlighter-rouge">Bitmap</code> and headers from the image download network request.
    <ul>
      <li>Custom Image Loaders that have used code from <code class="language-plaintext highlighter-rouge">DefaultBrazeImageLoader</code> may need to update their code to handle the new return type.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-18">Fixed</h5>
<ul>
  <li>Fixed the potential for <code class="language-plaintext highlighter-rouge">ViewUtils.removeViewFromParent</code> to cause a crash.</li>
  <li>Fixed an issue where an HTML In-App Message could crash if a bad external link had a query parameter of <code class="language-plaintext highlighter-rouge">target="_blank"</code>. Thanks to <code class="language-plaintext highlighter-rouge">@chenxiangcxc</code> for finding the issue.</li>
  <li>Fixed an issue where images would be cached when the HTTP headers indicated they shouldn’t be cached.</li>
  <li>Fixed an issue where some liquid templated images would not have the proper aspect ratio.</li>
</ul>

<h5 id="added-13">Added</h5>
<ul>
  <li>Added support for new Feature Flag property types by adding <code class="language-plaintext highlighter-rouge">getJsonProperty(key)</code>, <code class="language-plaintext highlighter-rouge">getImageProperty(key)</code>, and <code class="language-plaintext highlighter-rouge">getTimestampProperty(key)</code> to <code class="language-plaintext highlighter-rouge">FeatureFlag</code>.</li>
</ul>

<h5 id="changed-12">Changed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">@Synchronized</code> from Brazelogger in order to eliminate noisy thread deadlock logs.</li>
</ul>

<h2 id="3040">30.4.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v30.4.0">Release Date</a></p>

<h5 id="fixed-19">Fixed</h5>
<ul>
  <li>Fixed an issue with <code class="language-plaintext highlighter-rouge">com.braze.support.DateTimeUtils.nowInMilliseconds()</code> where, in the event of the device network time clock not being available, the SDK would continually log about the error.</li>
</ul>

<h5 id="added-14">Added</h5>
<ul>
  <li>Adds support for the <code class="language-plaintext highlighter-rouge">message_extras</code> Liquid tag for in-app messages.</li>
</ul>

<h2 id="3030">30.3.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v30.3.0">Release Date</a></p>

<h5 id="added-15">Added</h5>
<ul>
  <li>Added the fields <code class="language-plaintext highlighter-rouge">responseCode, responseHeaders, requestUrl</code> to <code class="language-plaintext highlighter-rouge">BrazeNetworkFailureEvent</code>.</li>
</ul>

<h2 id="3020">30.2.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v30.2.0">Release Date</a></p>

<h5 id="added-16">Added</h5>
<ul>
  <li>Introduces out-of-the-box <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/android/content_cards/jetpackcompose/">Jetpack Compose support</a> for Content Cards. Add the <code class="language-plaintext highlighter-rouge">com.braze:android-sdk-jetpack-compose</code> module to your <code class="language-plaintext highlighter-rouge">build.gradle</code> if you would like to use this feature.</li>
</ul>

<h2 id="3011">30.1.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v30.1.1">Release Date</a></p>

<h5 id="fixed-20">Fixed</h5>
<ul>
  <li>Fixed an issue where the SDK would fail to unregister session seal broadcast receivers.
    <ul>
      <li>The intent action is suffixed with <code class="language-plaintext highlighter-rouge">.intent.BRAZE_SESSION_SHOULD_SEAL</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="3010">30.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v30.1.0">Release Date</a></p>

<h5 id="added-17">Added</h5>
<ul>
  <li>Added the ability to configure whether SDK created Activities (such as <code class="language-plaintext highlighter-rouge">ContentCardsActivity</code>, <code class="language-plaintext highlighter-rouge">BrazeWebViewActivity</code>, etc.) use the <code class="language-plaintext highlighter-rouge">WindowManager.LayoutParams.FLAG_SECURE</code> to prevent screen capturing.
    <ul>
      <li>Configured via <code class="language-plaintext highlighter-rouge">braze.xml</code> through <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_use_activity_window_flag_secure"&gt;true&lt;/bool&gt;</code>.</li>
      <li>Can also be configured via runtime configuration through <code class="language-plaintext highlighter-rouge">BrazeConfig.setShouldUseWindowFlagSecureInActivities()</code>.</li>
      <li>Defaults to false.</li>
    </ul>
  </li>
</ul>

<h2 id="3000">30.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v30.0.0">Release Date</a></p>

<h4 id="breaking-12">Breaking</h4>
<ul>
  <li>WebViews used for In-App Messages have been updated to use <code class="language-plaintext highlighter-rouge">WebViewAssetLoader</code>.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">WebSettings.allowFileAccess</code> is now set to <code class="language-plaintext highlighter-rouge">false</code> in <code class="language-plaintext highlighter-rouge">InAppMessageHtmlBaseView</code> and <code class="language-plaintext highlighter-rouge">BrazeWebViewActivity</code>.</li>
      <li>If you are overriding <code class="language-plaintext highlighter-rouge">InAppMessageWebViewClient</code> and/or <code class="language-plaintext highlighter-rouge">InAppMessageHtmlBaseView</code>, please compare against the original classes to make sure your implementation is correctly loading the assets.</li>
      <li>If you are not overriding <code class="language-plaintext highlighter-rouge">InAppMessageWebViewClient</code> or <code class="language-plaintext highlighter-rouge">InAppMessageHtmlBaseView</code>, everything will work as before.</li>
      <li>If you are not using custom classes, everything will work as before.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-21">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">ImageView.setBitmap</code> was being called on a non-UI thread, causing <code class="language-plaintext highlighter-rouge">CalledFromWrongThreadException</code>.</li>
  <li>Fixed an issue where a StrictMode <code class="language-plaintext highlighter-rouge">DiskReadViolation</code> would occur when displaying an In-app Message. Thanks to @auxDK for finding the issue.</li>
</ul>

<h5 id="added-18">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(Context, BrazePushEvent)</code> to process events when using <code class="language-plaintext highlighter-rouge">Braze.subscribeToPushNotificationEvents</code>.
    <ul>
      <li>See <code class="language-plaintext highlighter-rouge">/samples/firebase-push</code>.</li>
    </ul>
  </li>
  <li>Added the ability to configure whether a user’s notification subscription state should automatically be set to <code class="language-plaintext highlighter-rouge">OPTED_IN</code> when push permissions are granted.
    <ul>
      <li>Configured via <code class="language-plaintext highlighter-rouge">braze.xml</code> through <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_optin_when_push_authorized"&gt;true&lt;/bool&gt;</code>.</li>
      <li>Can also be configured via runtime configuration through <code class="language-plaintext highlighter-rouge">BrazeConfig.setOptInWhenPushAuthorized()</code>.</li>
      <li>Defaults to true. This was the previous behavior.</li>
    </ul>
  </li>
</ul>

<h2 id="2901">29.0.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v29.0.1">Release Date</a></p>

<h5 id="fixed-22">Fixed</h5>
<ul>
  <li>Fixed an issue where Content Cards saved directly to storage via API triggered campaigns could be purged after syncs.</li>
  <li>Fixed an issue with the default Content Card feed where images provided without default aspect ratios would display with the wrong dynamic aspect ratio.</li>
</ul>

<h2 id="2900">29.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v29.0.0">Release Date</a></p>

<h5 id="breaking-13">Breaking</h5>
<ul>
  <li>Renamed <code class="language-plaintext highlighter-rouge">BannerImageCard</code>, <code class="language-plaintext highlighter-rouge">BannerImageCardView</code>, and <code class="language-plaintext highlighter-rouge">BannerImageContentCardView</code> to <code class="language-plaintext highlighter-rouge">ImageOnlyCard</code>, <code class="language-plaintext highlighter-rouge">ImageOnlyCardView</code>, and <code class="language-plaintext highlighter-rouge">ImageOnlyContentCardView</code>.</li>
  <li>All styles used for Banner Cards have been updated to Image Only Cards. All keys with the word <code class="language-plaintext highlighter-rouge">banner</code> should be replaced with <code class="language-plaintext highlighter-rouge">image_only</code>.</li>
  <li>Device brand information is now sent. If you want to block this, see <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/sdk_primer#blocking-data-collection">Blocking data collection</a>.</li>
</ul>

<h5 id="fixed-23">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">NotificationTrampolineActivity</code> would sometimes appear in the list of recent tasks.</li>
</ul>

<h5 id="added-19">Added</h5>
<ul>
  <li>Braze HTML In-App Message bridge method <code class="language-plaintext highlighter-rouge">setCustomUserAttribute()</code> will now accept a JSON Object as the value.
    <ul>
      <li>When passing a JSON Object, you can pass a third parameter of ‘true’ that will merge the JSON Object with the existing value.</li>
    </ul>
  </li>
  <li>Adds a new option <code class="language-plaintext highlighter-rouge">REENQUEUE</code> to enum <code class="language-plaintext highlighter-rouge">InAppMessageOperation</code>.
    <ul>
      <li>Return this option in <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener.beforeInAppMessageDisplayed</code> to ensure that an in-app message is not displayed and is simply re-enqueued.</li>
      <li>This option will reset any trigger times and re-eligibility rules as if it was never triggered. It will not add the message to the In-App Message stack.</li>
    </ul>
  </li>
</ul>

<h2 id="2800">28.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v28.0.0">Release Date</a></p>

<h4 id="breaking-14">Breaking</h4>
<ul>
  <li>Updated minimum SDK version to 21 (Lollipop).</li>
  <li>Feature Flags functions have been modified.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlag(id)</code> will now return null if the feature flag doesn’t exist.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.subscribeToFeatureFlagsUpdates()</code> will only callback when a refresh request completes, and initially if previously cached data exists. It will also be called with cached feature flags for any refresh failures.
        <ul>
          <li>If you want the cached value immediately at app startup, use <code class="language-plaintext highlighter-rouge">Braze.getFeatureFlag(id)</code>.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Refactored <code class="language-plaintext highlighter-rouge">DefaultInAppMessageViewWrapper.createButtonClickListener()</code> into <code class="language-plaintext highlighter-rouge">DefaultInAppMessageViewWrapper.createButtonClickListeners()</code>.</li>
</ul>

<h5 id="fixed-24">Fixed</h5>
<ul>
  <li>Fixed an issue where Firebase fallback service had a null <code class="language-plaintext highlighter-rouge">Context</code>.</li>
  <li>Fixed an issue where calling <code class="language-plaintext highlighter-rouge">requestPushPermission()</code> before <code class="language-plaintext highlighter-rouge">closeMessage()</code> in the HTML bridge could result in the HTML IAM remaining in the view hierarchy.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">Braze.removeSingleSubscription()</code> wouldn’t remove synchronous subscriptions, resulting in memory leaks with <code class="language-plaintext highlighter-rouge">ContentCardsFragment</code>.</li>
</ul>

<h5 id="changed-13">Changed</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">DefaultContentCardHandler</code> will sort by <code class="language-plaintext highlighter-rouge">Card.id</code> if both <code class="language-plaintext highlighter-rouge">Card.isPinned</code> and <code class="language-plaintext highlighter-rouge">Card.created</code> are equal.</li>
</ul>

<h2 id="2701">27.0.1</h2>

<h5 id="fixed-25">Fixed</h5>
<ul>
  <li>Fixed a bug introduced in version 26.1.0 where additional empty network requests were sent on <code class="language-plaintext highlighter-rouge">openSession</code> calls. Customers on v27.0.0 are strongly encouraged to upgrade.</li>
</ul>

<h2 id="2700">27.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v27.0.0">Release Date</a></p>

<p>⚠️ This version has a known issue. Please upgrade to v33.0.0.</p>

<h4 id="breaking-15">Breaking</h4>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">IInAppMessage.logDisplayFailure()</code>.</li>
</ul>

<h5 id="fixed-26">Fixed</h5>
<ul>
  <li>Fixed the behavior of HTML In-App messages to restrict remote navigation inputs to their display WebView during message display on non touch-mode devices.</li>
</ul>

<h2 id="2632">26.3.2</h2>

<h5 id="fixed-27">Fixed</h5>
<ul>
  <li>Fixed a bug introduced in version 26.1.0 where additional empty network requests were sent on <code class="language-plaintext highlighter-rouge">openSession</code> calls. Customers on v26.3.0 and v26.3.1 are strongly encouraged to upgrade.</li>
</ul>

<h2 id="2631">26.3.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v26.3.1">Release Date</a></p>

<p>⚠️ This version has a known issue. Please upgrade to v33.0.0.</p>

<h5 id="fixed-28">Fixed</h5>
<ul>
  <li>Internal bug fixes for an upcoming Braze push feature.</li>
</ul>

<h2 id="2630">26.3.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v26.3.0">Release Date</a></p>

<p>⚠️ This version has a known issue. Please upgrade to v33.0.0.</p>

<h5 id="added-20">Added</h5>
<ul>
  <li>Added the ability to forward Firebase push notifications to <code class="language-plaintext highlighter-rouge">FirebaseMessagingService</code> implementations if that push notification is not a Braze notification.
    <ul>
      <li>Configured via runtime configuration through <code class="language-plaintext highlighter-rouge">BrazeConfig.setFallbackFirebaseMessagingServiceEnabled()</code> and <code class="language-plaintext highlighter-rouge">BrazeConfig.setFallbackFirebaseMessagingServiceClasspath()</code></li>
      <li>Can also be configured via <code class="language-plaintext highlighter-rouge">braze.xml</code> through <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled"&gt;true&lt;/bool&gt;</code> and <code class="language-plaintext highlighter-rouge">&lt;string name="com_braze_fallback_firebase_cloud_messaging_service_classpath"&gt;com.company.OurFirebaseMessagingService&lt;/string&gt;</code>.</li>
      <li>Defaults to false.</li>
    </ul>
  </li>
</ul>

<h2 id="2621">26.2.1</h2>

<p>⚠️ This version has a known issue. Please upgrade to v33.0.0.</p>

<h5 id="fixed-29">Fixed</h5>
<ul>
  <li>Fixed a bug introduced in version 26.1.0 where additional empty network requests were sent on <code class="language-plaintext highlighter-rouge">openSession</code> calls. Customers on v26.2.0 are strongly encouraged to upgrade.</li>
</ul>

<h2 id="2620">26.2.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v26.2.0">Release Date</a></p>

<p>⚠️ This version has a known issue. Please upgrade to v33.0.0.</p>

<h5 id="fixed-30">Fixed</h5>
<ul>
  <li>Fixed an issue with Unity not properly forwarding messages to the Braze Unity internal layer for In-App Message events.</li>
  <li>Fixed an issue on Android 13+ devices where push subscriptions would be set to <code class="language-plaintext highlighter-rouge">OPTED_IN</code> on every session after the user granted push permissions. Now, the SDK sets the user to <code class="language-plaintext highlighter-rouge">OPTED_IN</code> only once immediately after the user grants push permissions.</li>
</ul>

<h5 id="changed-14">Changed</h5>
<ul>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">IBraze.requestContentCardsRefresh(boolean)</code> in favor of <code class="language-plaintext highlighter-rouge">IBraze.requestContentCardsRefresh()</code> and <code class="language-plaintext highlighter-rouge">IBraze.requestContentCardsRefreshFromCache()</code>.</li>
</ul>

<h2 id="2611">26.1.1</h2>

<p>⚠️ This version has a known issue. Please upgrade to v33.0.0.</p>

<h5 id="fixed-31">Fixed</h5>
<ul>
  <li>Fixed a bug introduced in version 26.1.0 where additional empty network requests were sent on <code class="language-plaintext highlighter-rouge">openSession</code> calls. Customers on v26.1.0 are strongly encouraged to upgrade.</li>
</ul>

<h2 id="2610">26.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v26.1.0">Release Date</a></p>

<p>⚠️ This version has a known issue. Please upgrade to v33.0.0.</p>

<h5 id="important">Important</h5>
<ul>
  <li>This release includes support for Android 14 (Upside Down Cake / API 34).</li>
</ul>

<h5 id="added-21">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">verticalAccuracy</code> to location information.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazeUser.setLastKnownLocation</code> now accepts verticalAccuracy.</li>
      <li>Updates through Braze location APIs will automatically include verticalAccuracy if the device supports it.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-15">Changed</h5>
<ul>
  <li>Changed target API for the SDK to 34.</li>
</ul>

<h2 id="2600">26.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v26.0.0">Release Date</a></p>

<h4 id="breaking-16">Breaking</h4>
<ul>
  <li>Added the ability to configure link target behavior for HTML In-App Messages through <code class="language-plaintext highlighter-rouge">BrazeConfig.setIsHtmlInAppMessageHtmlLinkTargetEnabled()</code> or via adding <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_html_in_app_message_enable_html_link_target"&gt;true&lt;/bool&gt;</code> to your <code class="language-plaintext highlighter-rouge">braze.xml</code>. Defaults to enabled.
    <ul>
      <li>When enabled, a link in an In-App Message that has the link target set (e.g. <code class="language-plaintext highlighter-rouge">&lt;a HREF="https://www.braze.com" target="_blank"&gt;Please Read&lt;/a&gt;</code>) will open the link in a browser, but will not close the In-App Message.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-32">Fixed</h5>
<ul>
  <li>Fixed an issue where a slideup In-App Message would not be auto-dismissed if the user interacted with it.</li>
  <li>Fixed an issue where a user’s push subscription state changed to “subscribed” instead of “opted in” upon accepting the Android 13+ push prompt.</li>
</ul>

<h2 id="2500">25.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v25.0.0">Release Date</a></p>

<h3 id="important-1">Important</h3>

<p>Our SDK is now hosted in Maven Central. You can remove <code class="language-plaintext highlighter-rouge">https://braze-inc.github.io/braze-android-sdk/sdk</code> from your build.gradle and make sure you have <code class="language-plaintext highlighter-rouge">mavenCentral()</code> as a repository.</p>

<h5 id="added-22">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazeLogger.enableVerboseLogging()</code> to more easily enable verbose logs.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Braze.getDeviceIdAsync()</code> which allows for asynchronously retrieving the Braze device identifier.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">com.braze.events.IFireOnceEventSubscriber</code> to provide the ability to listen to Braze updates with a fire-only-once guarantee.
    <div class="language-kotlin highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="nc">Braze</span><span class="p">.</span><span class="nf">getInstance</span><span class="p">(</span><span class="n">context</span><span class="p">).</span><span class="nf">subscribeToContentCardsUpdates</span><span class="p">(</span><span class="nc">IFireOnceEventSubscriber</span> <span class="p">{</span>
    <span class="c1">// Only fires once</span>
<span class="p">})</span>
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
  <li>Updated <code class="language-plaintext highlighter-rouge">BrazeUser.setCustomUserAttribute()</code> to now accept nested custom attributes and arrays of objects. Please see our <a href="https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/#usage-examples">public docs</a> for more information.</li>
</ul>

<h2 id="2430">24.3.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v24.3.0">Release Date</a></p>

<h5 id="fixed-33">Fixed</h5>
<ul>
  <li>Fixed an issue where the SDK would attempt to to access the visual service WindowManager from non-visual contexts, resulting in benign StrictMode errors.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">@JvmStatic</code> to <code class="language-plaintext highlighter-rouge">com.braze.push.BrazeHuaweiPushHandler.handleHmsRemoteMessageData()</code>.</li>
  <li>Fixed an issue where notification extra data was not being passed along in Push Story main image clicks.</li>
  <li>Fixed an issue where ContentCardAdapter was not properly handling bad indexes being passed in.</li>
  <li>Fixed an issue where a user’s push subscription state would not change to “opted in” upon accepting the Android 13+ push prompt.</li>
</ul>

<h5 id="added-23">Added</h5>
<ul>
  <li>Added the ability to configure dismissal of Push Stories on click by adding <code class="language-plaintext highlighter-rouge">BrazeConfig.setDoesPushStoryDismissOnClick()</code> or <code class="language-plaintext highlighter-rouge">&lt;bool name="com_braze_does_push_story_dismiss_on_click"&gt;true&lt;/bool&gt;</code> to your <code class="language-plaintext highlighter-rouge">braze.xml</code>. Defaults to true.</li>
</ul>

<h2 id="2420">24.2.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v24.2.0">Release Date</a></p>

<h5 id="added-24">Added</h5>
<ul>
  <li>Added support for the upcoming Braze Feature Flags product.</li>
</ul>

<h5 id="changed-16">Changed</h5>
<ul>
  <li>Changed the default behavior for images to more aggressively sample large images.
    <ul>
      <li>Images will be sampled until their effective bitmap size (i.e. W x H x 4 bytes) is below 16 MB.</li>
      <li>Images will be sampled until both (and not either) the half-width and half-height of the image is less than or equal to the image destination dimensions.</li>
    </ul>
  </li>
  <li>Changed the behavior of failed Content Card requests to automatically retry on server 500 errors and SDK Authentication errors.</li>
</ul>

<h2 id="2410">24.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v24.1.0">Release Date</a></p>

<h5 id="added-25">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazeActivityLifecycleCallbackListener.registerOnApplication()</code> which allows for registering the lifecycle callback listener from any <code class="language-plaintext highlighter-rouge">Context</code>.</li>
</ul>

<h2 id="2400">24.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v24.0.0">Release Date</a></p>

<h4 id="breaking-17">Breaking</h4>
<ul>
  <li>Location and geofence functionality has moved to a new module called <code class="language-plaintext highlighter-rouge">com.braze:android-sdk-location</code>. Add this module to your <code class="language-plaintext highlighter-rouge">build.gradle</code> if you are using Braze location functionality.</li>
  <li>Deprecated classes starting with <code class="language-plaintext highlighter-rouge">Appboy</code> have now been removed.</li>
  <li>Moved <code class="language-plaintext highlighter-rouge">com.appboy</code> packages to <code class="language-plaintext highlighter-rouge">com.braze</code>.</li>
  <li>All xml classes and values in them have been changed from <code class="language-plaintext highlighter-rouge">appboy</code> to <code class="language-plaintext highlighter-rouge">braze</code>. All custom code should be updated accordingly.</li>
  <li><code class="language-plaintext highlighter-rouge">BrazeNotificationUtils.isAppboyPushMessage()</code> removed. Please use instead:
    <ul>
      <li>Java: <code class="language-plaintext highlighter-rouge">BrazeNotificationUtils.isBrazePushMessage(Intent)</code></li>
      <li>Kotlin: <code class="language-plaintext highlighter-rouge">Intent.isBrazePushMessage()</code></li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">APPBOY_NOTIFICATION_OPENED_SUFFIX</code>, <code class="language-plaintext highlighter-rouge">APPBOY_NOTIFICATION_RECEIVED_SUFFIX</code>, and <code class="language-plaintext highlighter-rouge">APPBOY_NOTIFICATION_DELETED_SUFFIX</code> are removed.
    <ul>
      <li>Instead, please use <code class="language-plaintext highlighter-rouge">Braze.getInstance(context).subscribeToPushNotificationEvents()</code></li>
    </ul>
  </li>
  <li>Updated the minimum version of <code class="language-plaintext highlighter-rouge">com.google.android.gms:play-services-location</code> required for Braze Geofences to <code class="language-plaintext highlighter-rouge">20.0.0</code>.</li>
</ul>

<h5 id="added-26">Added</h5>
<ul>
  <li>Added the ability to optionally pipe Braze logcat from <code class="language-plaintext highlighter-rouge">BrazeLogger</code> to a custom callback via <code class="language-plaintext highlighter-rouge">BrazeLogger.onLoggedCallback</code>.
    <div class="language-kotlin highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>  <span class="nc">BrazeLogger</span><span class="p">.</span><span class="n">onLoggedCallback</span> <span class="p">=</span> <span class="k">fun</span><span class="p">(</span><span class="n">priority</span><span class="p">:</span> <span class="nc">BrazeLogger</span><span class="p">.</span><span class="nc">Priority</span><span class="p">,</span> <span class="n">message</span><span class="p">:</span> <span class="nc">String</span><span class="p">,</span> <span class="n">throwable</span><span class="p">:</span> <span class="nc">Throwable</span><span class="p">?)</span> <span class="p">{</span>
    <span class="c1">// Custom callback logic here</span>
  <span class="p">}</span>
</pre></td></tr></tbody></table></code></pre></div>    </div>
    <div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>  <span class="nc">BrazeLogger</span><span class="o">.</span><span class="na">setOnLoggedCallback</span><span class="o">((</span><span class="n">priority</span><span class="o">,</span> <span class="n">s</span><span class="o">,</span> <span class="n">throwable</span><span class="o">)</span> <span class="o">-&gt;</span> <span class="o">{</span>
    <span class="c1">// Custom logic here</span>
    <span class="k">return</span> <span class="kc">null</span><span class="o">;</span>
  <span class="o">});</span>
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
</ul>

<h5 id="changed-17">Changed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">BrazeUser.setFacebookData()</code> and <code class="language-plaintext highlighter-rouge">BrazeUser.setTwitterData()</code>.</li>
  <li>Changed the default behavior of <code class="language-plaintext highlighter-rouge">DefaultContentCardsUpdateHandler</code> to use the creation time vs last update time when sorting Content Cards.</li>
</ul>

<h2 id="2330">23.3.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.3.0">Release Date</a></p>

<h5 id="fixed-34">Fixed</h5>
<ul>
  <li>Fixed the behavior of the Braze HTML In-App Message bridge method <code class="language-plaintext highlighter-rouge">requestPushPermission()</code> to not cause the in-app message to reload.</li>
  <li>Fixed <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.views.InAppMessageImageView</code> to guard against null values of <code class="language-plaintext highlighter-rouge">InAppMessageImageView.inAppRadii</code>.</li>
</ul>

<h5 id="changed-18">Changed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.IInAppMessageViewWrapperFactory</code>. Please use <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.IInAppMessageViewWrapperFactory</code>.</li>
  <li>Changed <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.views.InAppMessageFullView.getMessageClickableView</code> to be nullable.</li>
</ul>

<h2 id="2321">23.2.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.2.1">Release Date</a></p>

<h5 id="fixed-35">Fixed</h5>
<ul>
  <li>Fixed the fields of <code class="language-plaintext highlighter-rouge">DefaultInAppMessageViewWrapper</code> to be <code class="language-plaintext highlighter-rouge">open</code>, allowing them to be subclassed in Kotlin properly.</li>
</ul>

<h2 id="2320">23.2.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.2.0">Release Date</a></p>

<h5 id="fixed-36">Fixed</h5>
<ul>
  <li>Fixed the fields of <code class="language-plaintext highlighter-rouge">DefaultInAppMessageViewWrapper</code> to be <code class="language-plaintext highlighter-rouge">protected</code>, allowing them to be subclassed.</li>
  <li>Fixed <code class="language-plaintext highlighter-rouge">BrazeNotificationPayload</code> and <code class="language-plaintext highlighter-rouge">BrazePushReceiver</code> to not hold onto an Activity context for longer than needed.</li>
</ul>

<h5 id="added-27">Added</h5>
<ul>
  <li>Added a config field <code class="language-plaintext highlighter-rouge">BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled()</code> to configure the SDK to automatically apply window insets to HTML In-App messages.
    <ul>
      <li>By default, this value is false.</li>
    </ul>
  </li>
  <li>Added <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/subscribe-to-no-matching-trigger-for-event.html"><code class="language-plaintext highlighter-rouge">subscribeToNoMatchingTriggerForEvent</code></a> which is called if no Braze in-app message was triggered for a given event.</li>
</ul>

<h5 id="changed-19">Changed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.listeners.IInAppMessageWebViewClientListener</code>. Please use <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.listeners.IInAppMessageWebViewClientListener</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyInAppMessageHtmlBaseView.APPBOY_BRIDGE_PREFIX</code>. Please use <code class="language-plaintext highlighter-rouge">InAppMessageHtmlBaseView.BRAZE_BRIDGE_PREFIX</code>.</li>
</ul>

<h2 id="2312">23.1.2</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.1.2">Release Date</a></p>

<h5 id="changed-20">Changed</h5>
<ul>
  <li>Removed the use of the Kotlin Coroutines method <code class="language-plaintext highlighter-rouge">limitedParallelism()</code>.</li>
</ul>

<h2 id="2311">23.1.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.1.1">Release Date</a></p>

<h5 id="fixed-37">Fixed</h5>
<ul>
  <li>Fixed the <code class="language-plaintext highlighter-rouge">DefaultInAppMessageViewWrapper</code> to be Kotlin open, allowing it to be subclassed.</li>
</ul>

<h2 id="2310">23.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.1.0">Release Date</a></p>

<h5 id="added-28">Added</h5>
<ul>
  <li>Added more reliable HTML In-App Message focusing specifically for TV environments. To use this behavior please set <code class="language-plaintext highlighter-rouge">com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages</code> to <code class="language-plaintext highlighter-rouge">false</code>.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazeNotificationPayload.extras</code> as a <code class="language-plaintext highlighter-rouge">Map&lt;String, String&gt;</code> to easily retrieve dashboard provided KVPs for push notification data.</li>
  <li>Added support for Content Cards to evaluate Retry-After headers.</li>
</ul>

<h2 id="2301">23.0.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.0.1">Release Date</a></p>

<h5 id="fixed-38">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">BaseCardView</code> would sometimes have the wrong size for a given image.</li>
</ul>

<h5 id="changed-21">Changed</h5>
<ul>
  <li>Added proguard rules to keep <code class="language-plaintext highlighter-rouge">enum.values()</code> and <code class="language-plaintext highlighter-rouge">enum.valueOf(String)</code> for users who don’t use the default Android proguard rules.</li>
</ul>

<h2 id="2300">23.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.0.0">Release Date</a></p>

<h4 id="breaking-18">Breaking</h4>
<ul>
  <li><code class="language-plaintext highlighter-rouge">BaseContentCardView.bindViewHolder()</code> now takes <code class="language-plaintext highlighter-rouge">Card</code> instead of generic type.</li>
</ul>

<h5 id="fixed-39">Fixed</h5>
<ul>
  <li>Fixed an issue where apps with a target of Android 12 running on Android 13 devices would not automatically create a default notification channel upon a push notification being received.</li>
</ul>

<h5 id="added-29">Added</h5>
<ul>
  <li>Added ability to retrieve deeplinks from <code class="language-plaintext highlighter-rouge">BrazeNotificationPayload</code> objects via <code class="language-plaintext highlighter-rouge">BrazeNotificationPayload().deeplink</code>.</li>
</ul>

<h2 id="2200">22.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v22.0.0">Release Date</a></p>

<h4 id="breaking-19">Breaking</h4>
<ul>
  <li><code class="language-plaintext highlighter-rouge">Appboy.java</code> is now <code class="language-plaintext highlighter-rouge">Braze.kt</code>. Kotlin clients will need to update their code to support the use of Kotlin properties on the Braze singleton where needed.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.registerPushToken()</code>/<code class="language-plaintext highlighter-rouge">Braze.getRegisteredPushToken()</code> is now <code class="language-plaintext highlighter-rouge">Braze.setRegisteredPushToken()</code>/<code class="language-plaintext highlighter-rouge">Braze.getRegisteredPushToken()</code>. If using Kotlin, use the property <code class="language-plaintext highlighter-rouge">Braze.registeredPushToken</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getDeviceId</code> is now just <code class="language-plaintext highlighter-rouge">Braze.deviceId</code> for Kotlin.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.enableMockNetworkAppboyRequestsAndDropEventsMode</code> is now <code class="language-plaintext highlighter-rouge">Braze.enableMockNetworkRequestsAndDropEventsMode()</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">Appboy.java</code> has been removed. For example, calls like <code class="language-plaintext highlighter-rouge">Appboy.getInstance()</code> will need to be <code class="language-plaintext highlighter-rouge">Braze.getInstance()</code> moving forward.</li>
      <li>Replaced <code class="language-plaintext highlighter-rouge">setCustomAppboyNotificationFactory()</code> with <code class="language-plaintext highlighter-rouge">setCustomBrazeNotificationFactory() / customBrazeNotificationFactory</code>.</li>
      <li>Renamed <code class="language-plaintext highlighter-rouge">enableMockAppboyNetworkRequestsAndDropEventsMode</code> to <code class="language-plaintext highlighter-rouge">enableMockNetworkRequestsAndDropEventsMode</code>.</li>
    </ul>
  </li>
  <li>Moved <code class="language-plaintext highlighter-rouge">com.appboy.IBrazeEndpointProvider</code> to <code class="language-plaintext highlighter-rouge">com.braze.IBrazeEndpointProvider</code>.</li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">com.appboy.events.IEventSubscriber</code> to <code class="language-plaintext highlighter-rouge">com.braze.events.IEventSubscriber</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">Appboy.registerAppboyPushMessages() / Appboy.getAppboyPushMessageRegistrationId()</code>. Replaced with <code class="language-plaintext highlighter-rouge">getRegisteredPushToken() / setRegisteredPushToken()</code>.</li>
  <li>Replaced <code class="language-plaintext highlighter-rouge">IAppboyNotificationFactory</code> with <code class="language-plaintext highlighter-rouge">IBrazeNotificationFactory</code>.</li>
</ul>

<h5 id="fixed-40">Fixed</h5>
<ul>
  <li>Fixed an issue in <code class="language-plaintext highlighter-rouge">BrazePushReceiver</code> where eager In-App Message test displays and Content Card serializations from push notifications wouldn’t work unless notifications were enabled on the device.</li>
  <li>Fixed an issue where devices between the API 19 up to API 29 would not perform automatic data syncs in some cases.</li>
  <li>Fixed an issue where carryover in-app messages wouldn’t display on subsequent Views on new Activities.</li>
  <li>Fixed an issue where some long running In-App Message HTML WebViews would call View methods on non UI threads.</li>
</ul>

<h5 id="added-30">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">IBraze.subscribeToPushNotificationEvents()</code> to allow for subscriptions to push notification events without the use of a <code class="language-plaintext highlighter-rouge">BroadcastReceiver</code>.
    <ul>
      <li>Recommended to be placed in your <code class="language-plaintext highlighter-rouge">Application.onCreate()</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-22">Changed</h5>
<ul>
  <li>Changed <code class="language-plaintext highlighter-rouge">com.braze.models.outgoing.BrazeProperties.clone()</code> to return <code class="language-plaintext highlighter-rouge">BrazeProperties?</code>.</li>
</ul>

<h2 id="2100">21.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v21.0.0">Release Date</a></p>

<h5 id="important-2">Important</h5>
<ul>
  <li>This release includes support for Android 13 (Tiramisu / API 33).</li>
</ul>

<h4 id="breaking-20">Breaking</h4>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">IAppboy.logContentCardsDisplayed</code>. This method was not part of the recommended Content Cards integration and can be safely removed.</li>
</ul>

<h5 id="changed-23">Changed</h5>
<ul>
  <li>Changed target API for the SDK to 33.</li>
</ul>

<h2 id="2000">20.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v20.0.0">Release Date</a></p>

<h4 id="breaking-21">Breaking</h4>
<ul>
  <li>Changed <code class="language-plaintext highlighter-rouge">BrazeNotificationStyleFactory</code> to remove deprecated functions.
    <ul>
      <li>Removed <code class="language-plaintext highlighter-rouge">BrazeNotificationStyleFactory.getBigNotificationStyle(Context, Bundle, Bundle, NotificationCompat.Builder)</code>. Use <code class="language-plaintext highlighter-rouge">BrazeNotificationStyleFactory.getNotificationStyle(NotificationCompat.Builder, BrazeNotificationPayload)</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">BrazeNotificationStyleFactory.getBigTextNotificationStyle(BrazeConfigurationProvider, Bundle)</code>. Use <code class="language-plaintext highlighter-rouge">BrazeNotificationStyleFactory.getBigTextNotificationStyle(BrazeNotificationPayload)</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">BrazeNotificationStyleFactory.getStoryStyle(Context, Bundle, Bundle, NotificationCompat.Builder)</code>. Use <code class="language-plaintext highlighter-rouge">BrazeNotificationStyleFactory.getStoryStyle(NotificationCompat.Builder, BrazeNotificationPayload)</code> instead.</li>
    </ul>
  </li>
  <li>Changed <code class="language-plaintext highlighter-rouge">BrazeNotificationActionUtils</code> to remove deprecated functions.
    <ul>
      <li>Removed <code class="language-plaintext highlighter-rouge">BrazeNotificationActionUtils.addNotificationActions(Context, NotificationCompat.Builder, Bundle)</code>. Use <code class="language-plaintext highlighter-rouge">BrazeNotificationActionUtils.addNotificationActions(NotificationCompat.Builder, BrazeNotificationPayload)</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">BrazeNotificationActionUtils.addNotificationAction(Context, NotificationCompat.Builder, Bundle, Int)</code>. Use <code class="language-plaintext highlighter-rouge">BrazeNotificationActionUtils.addNotificationAction(BrazeNotificationPayload.ActionButton)</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">AppboyNotificationActionUtils</code>. Use <code class="language-plaintext highlighter-rouge">BrazeNotificationActionUtils</code> instead.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyHuaweiPushHandler</code>. Use <code class="language-plaintext highlighter-rouge">BrazeHuaweiPushHandler</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code>. Use <code class="language-plaintext highlighter-rouge">BrazeFirebaseMessagingService</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyAdmReceiver</code>. Use <code class="language-plaintext highlighter-rouge">BrazeAmazonDeviceMessagingReceiver</code> instead.</li>
  <li><code class="language-plaintext highlighter-rouge">BrazeFirebaseMessagingService.handleBrazeRemoteMessage()</code> and <code class="language-plaintext highlighter-rouge">BrazeFirebaseMessagingService.isBrazePushNotification()</code> now require non-null parameters.</li>
  <li><code class="language-plaintext highlighter-rouge">UriAction.channel</code> is now <code class="language-plaintext highlighter-rouge">Channel.CONTENT_CARD</code> for actions that originate from a Content Card instead of <code class="language-plaintext highlighter-rouge">Channel.NEWS_FEED</code>.</li>
</ul>

<h5 id="fixed-41">Fixed</h5>
<ul>
  <li>Fixed an issue that would prevent SDK Authentication errors from being retried.</li>
</ul>

<h5 id="added-31">Added</h5>
<ul>
  <li>Modified <code class="language-plaintext highlighter-rouge">BrazeProperties.addProperties()</code> to allow adding nested properties via <code class="language-plaintext highlighter-rouge">JSONObject</code> or <code class="language-plaintext highlighter-rouge">Map&lt;String, *&gt;</code>.</li>
  <li>Added support for Braze Action Deeplink Click Actions.</li>
</ul>

<h5 id="changed-24">Changed</h5>
<ul>
  <li>Slideup messages now have a maximum width of 450dp. This can be adjusted by modifying <code class="language-plaintext highlighter-rouge">@dimen/com_braze_inappmessage_slideup_max_width</code>.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">com.braze.Constants</code> with constants starting with “BRAZE_” that replace the corresponding “APPBOY_” constants in <code class="language-plaintext highlighter-rouge">com.appboy.Constants</code>. The “APPBOY_” constants are deprecated and will be removed in a future release.</li>
</ul>

<h2 id="1900">19.0.0</h2>

<h5 id="important-3">Important</h5>
<ul>
  <li>It is highly recommended to include the compiler flag <code class="language-plaintext highlighter-rouge">-Xjvm-default=all</code> in your Gradle build options due to the new use of default arguments in the SDK. Without this flag, you may see a compiler warning about “Inheritance from an interface with ‘@JvmDefault’ members”. An example is included below:</li>
</ul>

<div class="language-groovy highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre>  <span class="n">android</span> <span class="o">{</span>
    <span class="n">kotlinOptions</span> <span class="o">{</span>
      <span class="n">freeCompilerArgs</span> <span class="o">=</span> <span class="o">[</span><span class="s1">'-Xjvm-default=all'</span><span class="o">]</span>
      <span class="n">jvmTarget</span> <span class="o">=</span> <span class="s2">"1.8"</span>
    <span class="o">}</span>
  <span class="o">}</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v19.0.0">Release Date</a></p>

<h5 id="-breaking">⚠ Breaking</h5>
<ul>
  <li>Modified behavior of <code class="language-plaintext highlighter-rouge">BrazeProperties(JSONObject)</code> when <code class="language-plaintext highlighter-rouge">Date</code> is part of JSONObject.
    <ul>
      <li>Previously, Date objects in the JSONObject would be converted with the <code class="language-plaintext highlighter-rouge">Date.toString()</code> (e.g. “Thu Jan 01 03:15:33 CST 1970”).</li>
      <li>Date objects in the JSONObject are now converted to <code class="language-plaintext highlighter-rouge">BrazeDateFormat.LONG</code> (e.g. “1970-01-01 09:15:33”). This behavior is consistent with <code class="language-plaintext highlighter-rouge">BrazeProperties.addProperty(Date)</code>.</li>
    </ul>
  </li>
  <li>Converted <code class="language-plaintext highlighter-rouge">IInAppMessage</code> to Kotlin and changed several methods to no longer allow for null inputs or return boolean statuses on field setters.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">IInAppMessage.setClickAction()</code> is renamed to <code class="language-plaintext highlighter-rouge">setClickBehavior()</code> and now returns void.</li>
      <li><code class="language-plaintext highlighter-rouge">MessageButton.setClickAction()</code> is renamed to <code class="language-plaintext highlighter-rouge">setClickBehavior()</code> and now returns void.</li>
      <li><code class="language-plaintext highlighter-rouge">InAppMessageImmersiveBase.setMessageButtons()</code> no longer accepts null. Pass in an empty list to clear.</li>
    </ul>
  </li>
  <li>Converted <code class="language-plaintext highlighter-rouge">Card</code> to Kotlin, so JVM signatures may have changed.
    <ul>
      <li>Removed <code class="language-plaintext highlighter-rouge">Card.isEqualToCard()</code>. Please use <code class="language-plaintext highlighter-rouge">card.equals(otherCard)</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">Card.isRead()</code> and <code class="language-plaintext highlighter-rouge">Card.setIsRead()</code>. Please use <code class="language-plaintext highlighter-rouge">Card.isIndicatorHighlighted</code> (Kotlin) or <code class="language-plaintext highlighter-rouge">Card.isIndicatorHighlighted()</code> and <code class="language-plaintext highlighter-rouge">Card.setIndicatorHighlighted()</code> (Java).</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.AnimationUtils</code>, <code class="language-plaintext highlighter-rouge">com.appboy.ViewUtils</code>, <code class="language-plaintext highlighter-rouge">com.appboy.UriUtils</code>, <code class="language-plaintext highlighter-rouge">com.appboy.IAction</code>, <code class="language-plaintext highlighter-rouge">com.appboy.NewsfeedAction</code> and <code class="language-plaintext highlighter-rouge">com.appboy.UriAction</code> classes. The Braze namespaced classes remain.</li>
  <li><code class="language-plaintext highlighter-rouge">BrazeDeeplinkHandler.createUriActionFromUrlString()</code> and <code class="language-plaintext highlighter-rouge">BrazeDeeplinkHandler.createUriActionFromUri()</code> now require non-null values for uri/url and channel.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">AppboyNavigator</code> has been removed in favor of <code class="language-plaintext highlighter-rouge">BrazeDeeplinkHandler</code>.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils</code> in favor of <code class="language-plaintext highlighter-rouge">BrazeNotificationUtils</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener</code>. Please use <code class="language-plaintext highlighter-rouge">BrazeActivityLifecycleCallbackListener</code>.
    <ul>
      <li>Removed <code class="language-plaintext highlighter-rouge">BrazeLifecycleCallbackListener.setInAppMessagingRegistrationBlacklist()</code> in favor of <code class="language-plaintext highlighter-rouge">BrazeLifecycleCallbackListener.setInAppMessagingRegistrationBlocklist()</code>. Removed <code class="language-plaintext highlighter-rouge">BrazeLifecycleCallbackListener.setSessionHandlingBlacklist()</code> in favor of <code class="language-plaintext highlighter-rouge">BrazeLifecycleCallbackListener.setSessionHandlingBlocklist()</code>.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyContentCardsManager</code>. Please use <code class="language-plaintext highlighter-rouge">BrazeContentCardsManager</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyEmptyContentCardsAdapter</code>. Please use <code class="language-plaintext highlighter-rouge">EmptyContentCardsAdapter</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">BrazeUser.setAvatarImageUrl(String)</code>.</li>
</ul>

<h5 id="fixed-42">Fixed</h5>
<ul>
  <li>Fixed the startup behavior of the SDK to not perform caller thread blocking operations when setting up SharedPreferences and other disk reading I/O.</li>
  <li>Fixed a potential issue where the default implementation of <code class="language-plaintext highlighter-rouge">Webview.onRenderProcessGone()</code> could lead to app crashes. Thanks to @ankitsingh08 for finding the issue.</li>
</ul>

<h5 id="changed-25">Changed</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazeProperties(Map&lt;String, *&gt;)</code> constructor.</li>
  <li>Changed <code class="language-plaintext highlighter-rouge">Appboy.getConfiguredApiKey()</code> to accept a <code class="language-plaintext highlighter-rouge">BrazeConfigurationProvider</code> instead of a <code class="language-plaintext highlighter-rouge">Context</code> object.</li>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">AppboyBootReceiver</code>. Please use <code class="language-plaintext highlighter-rouge">BrazeBootReceiver</code> instead.</li>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">APPBOY_WEBVIEW_URL_EXTRA</code>. Please use <code class="language-plaintext highlighter-rouge">BRAZE_WEBVIEW_URL_EXTRA</code> instead.</li>
  <li>Changed the SDK to not wake the screens of <code class="language-plaintext highlighter-rouge">Configuration.UI_MODE_TYPE_TELEVISION</code> devices when receiving push notifications.
    <ul>
      <li>These screen types will not be awoken even if <code class="language-plaintext highlighter-rouge">isPushWakeScreenForNotificationEnabled()</code> is true and the permission <code class="language-plaintext highlighter-rouge">Manifest.permission.WAKE_LOCK</code> is granted.</li>
      <li>Special thanks to @IanGClifton for https://github.com/braze-inc/braze-android-sdk/pull/213.</li>
    </ul>
  </li>
</ul>

<h2 id="1801">18.0.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v18.0.1">Release Date</a></p>

<h5 id="fixed-43">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 17.0.0 where some HTML In-App Message zip asset files containing hidden <code class="language-plaintext highlighter-rouge">__MACOSX</code> folders without a corresponding entry for that folder would cause the in-app message to fail to display.</li>
</ul>

<h2 id="1800">18.0.0</h2>

<h5 id="important-4">Important</h5>
<ul>
  <li>It is highly recommended to include the compiler flag <code class="language-plaintext highlighter-rouge">-Xjvm-default=all</code> in your Gradle build options due to the new use of default arguments in the SDK. Without this flag, you may see a compiler warning about “Inheritance from an interface with ‘@JvmDefault’ members”. An example is included below:</li>
</ul>

<div class="language-groovy highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre>  <span class="n">android</span> <span class="o">{</span>
    <span class="n">kotlinOptions</span> <span class="o">{</span>
      <span class="n">freeCompilerArgs</span> <span class="o">=</span> <span class="o">[</span><span class="s1">'-Xjvm-default=all'</span><span class="o">]</span>
      <span class="n">jvmTarget</span> <span class="o">=</span> <span class="s2">"1.8"</span>
    <span class="o">}</span>
  <span class="o">}</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v18.0.0">Release Date</a></p>

<blockquote>
  <p>This version has a known issue with HTML In-App Message which was fixed in v18.0.1</p>
</blockquote>

<h5 id="-breaking-1">⚠ Breaking</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyLruImageLoader</code> in favor of <code class="language-plaintext highlighter-rouge">DefaultBrazeImageLoader</code>.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.lrucache.AppboyLruImageLoader</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.images.DefaultBrazeImageLoader</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.Appboy.getAppboyImageLoader</code> -&gt; <code class="language-plaintext highlighter-rouge">com.appboy.Appboy.getImageLoader</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.Appboy.setAppboyImageLoader</code> -&gt; <code class="language-plaintext highlighter-rouge">com.appboy.Appboy.setImageLoader</code>.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">IAppboyEndpointProvider</code> in favor of <code class="language-plaintext highlighter-rouge">IBrazeEndpointProvider</code>.
    <ul>
      <li>If using <code class="language-plaintext highlighter-rouge">Braze.setAppboyEndpointProvider()</code> please use <code class="language-plaintext highlighter-rouge">Braze.setEndpointProvider()</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-44">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 15.0.0 where Full in-app messages on tablets may have had an incorrect background color.</li>
</ul>

<h5 id="added-32">Added</h5>
<ul>
  <li>Added the ability to change SDK authentication signature with <code class="language-plaintext highlighter-rouge">Braze.changeUser()</code> when the current user id and a new signature is passed in.
    <ul>
      <li>Previously, <code class="language-plaintext highlighter-rouge">Braze.changeUser()</code> would not change the SDK authentication signature if the current user id was used.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-26">Changed</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">InAppMessageCloser</code> is deprecated.
    <ul>
      <li>Use <code class="language-plaintext highlighter-rouge">BrazeInAppMessageManager.hideCurrentlyDisplayingInAppMessage()</code> to hide currently displayed in-app messages.</li>
      <li>Use <code class="language-plaintext highlighter-rouge">IInAppMessage.setAnimateOut()</code> to set whether your in-app message should animate on close.</li>
      <li>New version of <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener.onInAppMessageClicked()</code> and <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener.onInAppMessageButtonClicked()</code> that don’t use <code class="language-plaintext highlighter-rouge">InAppMessageCloser</code> have been added.
        <ul>
          <li>If you override the deprecated functions that use <code class="language-plaintext highlighter-rouge">InAppMessageCloser</code>, those will be called.</li>
          <li>If you override the new functions and don’t override the deprecated functions, the new functions will be called.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">ContentCardsUpdatedEvent.getLastUpdatedInSecondsFromEpoch</code>.
    <ul>
      <li>Use <code class="language-plaintext highlighter-rouge">getTimestampSeconds()</code> (Java) or <code class="language-plaintext highlighter-rouge">timestampSeconds</code> (Kotlin).</li>
    </ul>
  </li>
</ul>

<h2 id="1700">17.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v17.0.0">Release Date</a></p>

<p>:warning: This version has a known issue with HTML In-App Message which was fixed in v18.0.1</p>

<h5 id="-breaking-2">⚠ Breaking</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">BrazeLogger.setLogLevel()</code> replaced with direct property setter <code class="language-plaintext highlighter-rouge">BrazeLogger.logLevel</code> for Kotlin.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyLogger, com.appboy.IntentUtils, com.appboy.StringUtils</code> class. The Braze namespaced classes remain.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">com_braze_locale_api_key_map</code> as a configuration option and <code class="language-plaintext highlighter-rouge">BrazeConfig.setLocaleToApiMapping()</code>. If you need to change your API key based on locale, please use <code class="language-plaintext highlighter-rouge">BrazeConfig</code> at runtime instead.</li>
</ul>

<h5 id="added-33">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">Braze.isDisabled()</code> to determine whether the SDK is disabled.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Braze.addSdkMetadata()</code> to allow self reporting of SDK Metadata fields via the <code class="language-plaintext highlighter-rouge">BrazeSdkMetadata</code> enum.
    <ul>
      <li>Fields may also be added via a <code class="language-plaintext highlighter-rouge">string-array</code> to your <code class="language-plaintext highlighter-rouge">braze.xml</code> with the key <code class="language-plaintext highlighter-rouge">com_braze_sdk_metadata</code>. The allowed items are the same as the keys found in the <code class="language-plaintext highlighter-rouge">BrazeSdkMetadata</code> enum. For example when using Branch:
        <div class="language-xml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="nt">&lt;string-array</span> <span class="na">name=</span><span class="s">"com_braze_sdk_metadata"</span><span class="nt">&gt;</span>
 <span class="nt">&lt;item&gt;</span>BRANCH<span class="nt">&lt;/item&gt;</span>
<span class="nt">&lt;/string-array&gt;</span>
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>Fields are additive across all reporting methods.</li>
    </ul>
  </li>
</ul>

<h2 id="1600">16.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v16.0.0">Release Date</a></p>

<h5 id="-breaking-3">⚠ Breaking</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyConfigurationProvider</code> in favor of <code class="language-plaintext highlighter-rouge">BrazeConfigurationProvider</code>.
    <ul>
      <li>Any deprecated usages, such as in the <code class="language-plaintext highlighter-rouge">IBrazeNotificationFactory</code> have also been removed.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-45">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 13.1.0 where session start location updates would fail to update on pre API 30 devices.</li>
  <li>Fixed an issue introduced in 13.1.0 where geofence update events would fail to update properly.</li>
</ul>

<h5 id="added-34">Added</h5>
<ul>
  <li>Added the ability to namespace all <code class="language-plaintext highlighter-rouge">braze.xml</code> configurations to be able to use <code class="language-plaintext highlighter-rouge">braze</code> in place of <code class="language-plaintext highlighter-rouge">appboy</code>. The Braze namespaced configuration keys will take precedence over the <code class="language-plaintext highlighter-rouge">appboy</code> keys.
    <ul>
      <li>For example, <code class="language-plaintext highlighter-rouge">com_appboy_api_key</code> can be replaced with <code class="language-plaintext highlighter-rouge">com_braze_api_key</code>.</li>
      <li>Be sure to look for and update any API keys in your build variants as the <code class="language-plaintext highlighter-rouge">com_braze_api_key</code> from your default variant might take precedence unexpectedly.</li>
      <li>All <code class="language-plaintext highlighter-rouge">com_appboy_*</code> configuration keys in XML will be removed in a future release so it is advised to migrate these configuration keys to their <code class="language-plaintext highlighter-rouge">com_braze_*</code> counterparts.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-27">Changed</h5>
<ul>
  <li>Changed target API for the SDK to 31.</li>
</ul>

<h2 id="1500">15.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v15.0.0">Release Date</a></p>

<h5 id="important-5">Important</h5>
<ul>
  <li>It is highly recommended to do extensive QA after updating to this release, especially for clients doing any amount of Content Card or In-App Message customizations.</li>
</ul>

<h5 id="-breaking-4">⚠ Breaking</h5>
<ul>
  <li>All Content Cards layout/drawables/colors/dimens identifiers containing <code class="language-plaintext highlighter-rouge">com_appboy_content_cards</code>/<code class="language-plaintext highlighter-rouge">com_appboy_content_card</code> were replaced with <code class="language-plaintext highlighter-rouge">com_braze_content_cards</code>/<code class="language-plaintext highlighter-rouge">com_braze_content_card</code> respectively.
    <ul>
      <li>Content Card drawables <code class="language-plaintext highlighter-rouge">icon_pinned, icon_read, icon_unread</code> are now <code class="language-plaintext highlighter-rouge">com_braze_content_card_icon_pinned, com_braze_content_card_icon_read, com_braze_content_card_icon_unread</code>.</li>
    </ul>
  </li>
  <li>All In-App Message layout/drawables/colors/dimens identifiers containing <code class="language-plaintext highlighter-rouge">com_appboy_inappmessage</code>/<code class="language-plaintext highlighter-rouge">com_appboy_in_app_message</code> replaced with <code class="language-plaintext highlighter-rouge">com_braze_inappmessage</code>.</li>
  <li>All styles under namespace <code class="language-plaintext highlighter-rouge">Appboy.*</code> moved to <code class="language-plaintext highlighter-rouge">Braze.*</code>.
    <ul>
      <li>Any <code class="language-plaintext highlighter-rouge">Appboy.*</code> style overrides must be migrated to <code class="language-plaintext highlighter-rouge">Braze.*</code> as there is no backwards compatibility.</li>
      <li>For example, a style override for <code class="language-plaintext highlighter-rouge">Appboy.Cards.ImageSwitcher</code> must be renamed to <code class="language-plaintext highlighter-rouge">Braze.Cards.ImageSwitcher</code>.</li>
    </ul>
  </li>
  <li>Several classes/interfaces have been moved to a Braze namespace/package.
    <ul>
      <li>In-App Messages
        <ul>
          <li>In-App Message classes under <code class="language-plaintext highlighter-rouge">com.appboy.models.*</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.models.inappmessage</code></li>
          <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.InAppMessageCloser</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.InAppMessageCloser</code></li>
          <li>Enum <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.InAppMessageOperation</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.InAppMessageOperation</code></li>
          <li>Enums in package <code class="language-plaintext highlighter-rouge">com.appboy.enums.inappmessage.*</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.enums.inappmessage</code></li>
        </ul>
      </li>
      <li>Content Cards
        <ul>
          <li>Interface <code class="language-plaintext highlighter-rouge">IContentCardsUpdateHandler</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.ui.contentcards.handlers.IContentCardsUpdateHandler</code></li>
          <li>Interface <code class="language-plaintext highlighter-rouge">IContentCardsViewBindingHandler</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.ui.contentcards.handlers.IContentCardsViewBindingHandler</code></li>
          <li>Interface <code class="language-plaintext highlighter-rouge">AppboyContentCardsActionListener</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.ui.contentcards.listeners.DefaultContentCardsActionListener</code></li>
          <li>Classes in package <code class="language-plaintext highlighter-rouge">com.appboy.ui.contentcards.view.*</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.ui.contentcards.view.*</code>
            <ul>
              <li>This is the package containing all Content Card default views.</li>
            </ul>
          </li>
          <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.events.ContentCardsUpdatedEvent</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.events.ContentCardsUpdatedEvent</code></li>
        </ul>
      </li>
      <li>Miscellaneous
        <ul>
          <li>Class <code class="language-plaintext highlighter-rouge">AppboyBaseFragmentActivity</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.ui.activities.BrazeBaseFragmentActivity</code></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Removed deprecated <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener#onInAppMessageReceived</code> from <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyUser</code> in favor of <code class="language-plaintext highlighter-rouge">BrazeUser</code>.
    <ul>
      <li>Note that for Kotlin consumers, <code class="language-plaintext highlighter-rouge">Appboy.currentUser?</code> and <code class="language-plaintext highlighter-rouge">Braze.currentUser?</code> are valid due to the removal of generics on the <code class="language-plaintext highlighter-rouge">Braze.getCurrentUser()</code> method.</li>
    </ul>
  </li>
</ul>

<h5 id="added-35">Added</h5>
<ul>
  <li>Added support for Conversational Push.</li>
  <li>Added the ability for custom broadcast receivers to not require the host package name as a prefix when declaring intent filters in your app manifest.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">&lt;action android:name="${applicationId}.intent.APPBOY_PUSH_RECEIVED" /&gt;</code> should be replaced with <code class="language-plaintext highlighter-rouge">&lt;action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" /&gt;</code></li>
      <li><code class="language-plaintext highlighter-rouge">&lt;action android:name="${applicationId}.intent.APPBOY_NOTIFICATION_OPENED" /&gt;</code> should be replaced with <code class="language-plaintext highlighter-rouge">&lt;action android:name="com.braze.push.intent.NOTIFICATION_OPENED" /&gt;</code></li>
      <li><code class="language-plaintext highlighter-rouge">&lt;action android:name="${applicationId}.intent.APPBOY_PUSH_DELETED" /&gt;</code> should be replaced with <code class="language-plaintext highlighter-rouge">&lt;action android:name="com.braze.push.intent.NOTIFICATION_DELETED" /&gt;</code></li>
      <li>The <code class="language-plaintext highlighter-rouge">appboy</code> intents have been deprecated but are still available. They will be removed in a future release so migrating early is highly recommended.</li>
      <li>Both the <code class="language-plaintext highlighter-rouge">appboy</code> and <code class="language-plaintext highlighter-rouge">braze</code> intents are sent for backwards compatibility so only one set should be registered at a time.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazeUser.addToSubscriptionGroup()</code> and <code class="language-plaintext highlighter-rouge">BrazeUser.removeFromSubscriptionGroup()</code> to add or remove a user from an email or SMS subscription group.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">brazeBridge.getUser().addToSubscriptionGroup()</code> and <code class="language-plaintext highlighter-rouge">brazeBridge.getUser().removeFromSubscriptionGroup()</code> to the javascript interface for HTML In-App Messages.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-28">Changed</h5>
<ul>
  <li>Several classes in the android-sdk-ui artifact have been renamed to the Braze namespace/package. Whenever possible, the original classes are still available. However, they will be removed in a future release so migrating early is highly recommended.
    <ul>
      <li>Classes in package <code class="language-plaintext highlighter-rouge">com.appboy.push.*</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.push.*</code></li>
      <li>Classes in package <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.views</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.views</code></li>
      <li>Classes in package <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.listeners</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.listeners</code></li>
      <li>Interfaces in <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.*</code> moved to <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.*</code></li>
      <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.AppboyFirebaseMessagingService</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.push.BrazeFirebaseMessagingService</code></li>
      <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.AppboyAdmReceiver</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.push.BrazeAmazonDeviceMessagingReceiver</code></li>
      <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.ui.AppboyContentCardsFragment</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.ui.contentcards.ContentCardsFragment</code></li>
      <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.ui.activities.AppboyContentCardsActivity</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.ui.activities.ContentCardsActivity</code></li>
      <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.ui.AppboyWebViewActivity</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.ui.BrazeWebViewActivity</code></li>
      <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.AppboyInAppMessageManager</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.BrazeInAppMessageManager</code></li>
      <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.DefaultInAppMessageViewWrapper</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.ui.inappmessage.DefaultInAppMessageViewWrapper</code></li>
      <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.AppboyLifecycleCallbackListener</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.BrazeActivityLifecycleCallbackListener</code></li>
    </ul>
  </li>
  <li>Changed the <code class="language-plaintext highlighter-rouge">ContentCardsFragment</code> and <code class="language-plaintext highlighter-rouge">BrazeInAppMessageManager</code> to clear their respective caches of messages after <code class="language-plaintext highlighter-rouge">wipeData()</code> is called.</li>
</ul>

<h2 id="1401">14.0.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v14.0.1">Release Date</a></p>

<h5 id="fixed-46">Fixed</h5>
<ul>
  <li>Fixed an issue with <code class="language-plaintext highlighter-rouge">BrazeProperties</code> not being kept via proguard rules.</li>
  <li>Fixed an issue on TV integrations where in app messages wouldn’t properly be given focus when visible.</li>
</ul>

<h5 id="added-36">Added</h5>
<ul>
  <li>Added close icon highlighting for TV integrations when selecting the close button in In App Messages.</li>
</ul>

<h2 id="1400">14.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v14.0.0">Release Date</a></p>

<h5 id="-breaking-5">⚠ Breaking</h5>
<ul>
  <li>Interface <code class="language-plaintext highlighter-rouge">IInAppMessageViewWrapperFactory</code> changed to use <code class="language-plaintext highlighter-rouge">BrazeConfigurationProvider</code>.</li>
  <li>Interface <code class="language-plaintext highlighter-rouge">IAppboyImageLoader/IBrazeImageLoader</code> changed to use <code class="language-plaintext highlighter-rouge">com.braze.enums.BrazeViewBounds</code>.</li>
  <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.configuration.AppboyConfig</code> is now <code class="language-plaintext highlighter-rouge">com.braze.configuration.BrazeConfig</code>. The original class has been removed and old usages should be updated.</li>
  <li>Class <code class="language-plaintext highlighter-rouge">com.appboy.enums.AppboyViewBounds</code> is now <code class="language-plaintext highlighter-rouge">com.braze.enums.BrazeViewBounds</code>. The original class has been removed and old usages should be updated.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.push.AppboyNotificationUtils#bundleOptString</code>.</li>
  <li><code class="language-plaintext highlighter-rouge">Braze.logPurchase()</code> and <code class="language-plaintext highlighter-rouge">Braze.logEvent()</code> now impose a 50KB limit on event properties. If the supplied properties are too large, the event is not logged.
    <ul>
      <li>See <code class="language-plaintext highlighter-rouge">BrazeProperties.isInvalid()</code>.</li>
    </ul>
  </li>
  <li>HTML In-App Messages rendered via the default <code class="language-plaintext highlighter-rouge">AppboyHtmlViewFactory</code> now require the device to be in touch mode to display.
    <ul>
      <li>See <code class="language-plaintext highlighter-rouge">getIsTouchModeRequiredForHtmlInAppMessages()</code> in the #added section for configuration on disabling this behavior.</li>
    </ul>
  </li>
  <li>For Kotlin consumers, <code class="language-plaintext highlighter-rouge">Appboy.currentUser?</code> calls must be migrated to <code class="language-plaintext highlighter-rouge">Braze.getCurrentUser&lt;BrazeUser&gt;()</code> due to updated generics resolution.</li>
</ul>

<h5 id="changed-29">Changed</h5>
<ul>
  <li>Several classes in the base artifact have been renamed to the Braze namespace/packages. Whenever possible, the original classes are still available. However, they will be removed in a future release so migrating early is highly recommended.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.Appboy</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.Braze</code></li>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.configuration.AppboyConfig</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.configuration.BrazeConfig</code></li>
      <li><code class="language-plaintext highlighter-rouge">com.braze.AppboyUser</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.BrazeUser</code></li>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.lrucache.AppboyLruImageLoader</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.images.DefaultBrazeImageLoader</code></li>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.configuration.AppboyConfigurationProvider</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.configuration.BrazeConfigurationProvider</code></li>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.models.outgoing.AppboyProperties</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.models.outgoing.BrazeProperties</code></li>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.support.AppboyImageUtils</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.support.BrazeImageUtils</code></li>
      <li><code class="language-plaintext highlighter-rouge">com.appboy.support.AppboyFileUtils</code> -&gt; <code class="language-plaintext highlighter-rouge">com.braze.support.BrazeFileUtils</code></li>
    </ul>
  </li>
  <li>Changed the behavior of In-App Message Accessibility Exclusive mode to save and reset the accessibility flags of views after display.</li>
  <li>Changed the <code class="language-plaintext highlighter-rouge">AppboyInAppMessageWebViewClientListener</code> to use an Activity context when following a deeplink in <code class="language-plaintext highlighter-rouge">IInAppMessageWebViewClientListener.onOtherUrlAction</code>.</li>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">AppboyInAppMessageHtmlBaseView.APPBOY_BRIDGE_PREFIX</code>.</li>
</ul>

<h5 id="added-37">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">Braze.registerPushToken()</code> and <code class="language-plaintext highlighter-rouge">Braze.getRegisteredPushToken()</code>.
    <ul>
      <li>Note that these methods are the functional equivalents of <code class="language-plaintext highlighter-rouge">Appboy.registerAppboyPushMessages()</code> and <code class="language-plaintext highlighter-rouge">Appboy.getAppboyPushMessageRegistrationId()</code>.</li>
    </ul>
  </li>
  <li>Exposed <code class="language-plaintext highlighter-rouge">brazeBridge</code> which replaces <code class="language-plaintext highlighter-rouge">appboyBridge</code> to be used as the javascript interface for HTML In-App Messages. <code class="language-plaintext highlighter-rouge">appboyBridge</code> is deprecated and will be removed in a future version of the SDK.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyInAppMessageHtmlBaseView.BRAZE_BRIDGE_PREFIX</code>.</li>
  <li>Added the ability to configure whether <code class="language-plaintext highlighter-rouge">View#isInTouchMode()</code> is required to show HTML In-App Messages via <code class="language-plaintext highlighter-rouge">BrazeConfig.setIsTouchModeRequiredForHtmlInAppMessages()</code>.
    <ul>
      <li>Can also be configured via boolean <code class="language-plaintext highlighter-rouge">com_braze_require_touch_mode_for_html_in_app_messages</code> in your <code class="language-plaintext highlighter-rouge">braze.xml</code>.</li>
      <li>Defaults to true.</li>
    </ul>
  </li>
  <li>Added support for new SDK Authentication feature.</li>
</ul>

<h5 id="fixed-47">Fixed</h5>
<ul>
  <li>Fixed an issue with <code class="language-plaintext highlighter-rouge">setIsInAppMessageAccessibilityExclusiveModeEnabled()</code> not being respected if set via runtime configuration. Setting this value via XML was unaffected.</li>
  <li>Fixed an issue with the SDK repeatedly failing to initialize when not properly setting a Braze API key.</li>
</ul>

<h2 id="1312">13.1.2</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v13.1.2">Release Date</a></p>

<h5 id="changed-30">Changed</h5>
<ul>
  <li>Changed the <code class="language-plaintext highlighter-rouge">NotificationTrampolineActivity</code> to always call <code class="language-plaintext highlighter-rouge">finish()</code> regardless of any eventual deeplink handling by the host app or SDK.</li>
</ul>

<h2 id="1311">13.1.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v13.1.1">Release Date</a></p>

<h5 id="fixed-48">Fixed</h5>
<ul>
  <li>Fixed an issue with the <code class="language-plaintext highlighter-rouge">NotificationTrampolineActivity</code> being opened on notification delete intents.</li>
</ul>

<h2 id="1310">13.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v13.1.0">Release Date</a></p>

<h5 id="changed-31">Changed</h5>
<ul>
  <li>All notifications now route through <code class="language-plaintext highlighter-rouge">NotificationTrampolineActivity</code> to comply with Android 12 notification trampoline restrictions.</li>
  <li>Inline Image push is now compatible with the Android 12 notification area changes.</li>
  <li>Automatic Firebase Messaging registration will now use <code class="language-plaintext highlighter-rouge">FirebaseMessaging.getInstance().getToken()</code> directly if available.</li>
  <li>Removed usage of <code class="language-plaintext highlighter-rouge">Intent.ACTION_CLOSE_SYSTEM_DIALOGS</code> with push notifications.</li>
</ul>

<h5 id="added-38">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">getInAppMessageStack()</code>, <code class="language-plaintext highlighter-rouge">getCarryoverInAppMessage()</code>, and <code class="language-plaintext highlighter-rouge">getUnregisteredInAppMessage()</code> to <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager</code>.</li>
</ul>

<h2 id="1300">13.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v13.0.0">Release Date</a></p>

<h5 id="-breaking-6">⚠ Breaking</h5>
<ul>
  <li>Moved all In-App Message buttons from <code class="language-plaintext highlighter-rouge">Button</code> to <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.views.InAppMessageButton</code>.
    <ul>
      <li>This ensures that the <code class="language-plaintext highlighter-rouge">MaterialComponentsViewInflater</code> does not interfere with standard In-App Message display when using a <code class="language-plaintext highlighter-rouge">MaterialComponents</code> theme.</li>
      <li>Apps extending a <code class="language-plaintext highlighter-rouge">Material</code> theme should test to ensure their In-App Messages appear as expected.</li>
    </ul>
  </li>
  <li>Moved <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.AppboyInAppMessageImageView</code> to <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.views.InAppMessageImageView</code>.</li>
  <li>Removed all getter methods from <code class="language-plaintext highlighter-rouge">AppboyConfig</code>. Access to the underlying data is now directly possible via the variables of the object, e.g. <code class="language-plaintext highlighter-rouge">appboyConfig.getApiKey()</code> is now <code class="language-plaintext highlighter-rouge">appboyConfig.mApiKey</code>.</li>
</ul>

<h5 id="added-39">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">getEmptyCardsAdapter(), getContentCardUpdateRunnable(), getNetworkUnavailableRunnable()</code> to protected methods in <code class="language-plaintext highlighter-rouge">AppboyContentCardsFragment</code> for easier customizability.</li>
  <li>Changed the max content line length to 2 lines for Inline Image Push.
    <ul>
      <li>This style can be found via <code class="language-plaintext highlighter-rouge">"Appboy.Push.InlineImage.TextArea.TitleContent.ContentText"</code></li>
    </ul>
  </li>
</ul>

<h5 id="fixed-49">Fixed</h5>
<ul>
  <li>Changed the <code class="language-plaintext highlighter-rouge">AppboyContentCardsFragment.ContentCardsUpdateRunnable</code> to determine network unavailability and feed emptiness based on the filtered list of cards and not the original input list of cards.</li>
  <li>Fixed an issue with IAM display where a deleted local image would result in a failed image display.</li>
</ul>

<h2 id="1200">12.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v12.0.0">Release Date</a></p>

<h5 id="-breaking-7">⚠ Breaking</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">getIntentFlags</code> to the <code class="language-plaintext highlighter-rouge">IAppboyNavigator</code> interface to more easily allow for customizing Activity launch behavior.
    <ul>
      <li>A default implementation is available below:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>@Override
public int getIntentFlags(IntentFlagPurpose intentFlagPurpose) {
  return new AppboyNavigator().getIntentFlags(intentFlagPurpose);
}
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">firebase_messaging_service_automatically_register_on_new_token</code> to <code class="language-plaintext highlighter-rouge">com_appboy_firebase_messaging_service_automatically_register_on_new_token</code> in <code class="language-plaintext highlighter-rouge">appboy.xml</code> configuration.</li>
</ul>

<h5 id="fixed-50">Fixed</h5>
<ul>
  <li>Fixed an issue with the default image loader not properly setting image bitmaps on API 23 and below devices.</li>
  <li>Fixed an issue where the <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.ensureSubscribedToInAppMessageEvents()</code> method wouldn’t properly resubscribe after disabling and re-enabling the SDK.</li>
</ul>

<h5 id="changed-32">Changed</h5>
<ul>
  <li>Changed Push Stories in <code class="language-plaintext highlighter-rouge">AppboyNotificationStyleFactory</code> to use <code class="language-plaintext highlighter-rouge">BrazeNotificationPayload</code>.</li>
</ul>

<h2 id="1100">11.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v11.0.0">Release Date</a></p>

<h5 id="-breaking-8">⚠ Breaking</h5>
<ul>
  <li>Changed the behavior of new beta HTML In-App Messages with dashboard preview support (i.e. those with <code class="language-plaintext highlighter-rouge">MessageType.HTML</code> and not <code class="language-plaintext highlighter-rouge">MessageType.HTML_FULL</code>) to not automatically log analytics clicks on url follows in <code class="language-plaintext highlighter-rouge">IInAppMessageWebViewClientListener</code>.
    <ul>
      <li>Body click analytics will no longer automatically be collected. To continue to receive body click analytics, you must log body clicks explicitly from your message via Javascript using <code class="language-plaintext highlighter-rouge">appboyBridge.logClick()</code>.</li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">IContentCardsUpdateHandler</code> and <code class="language-plaintext highlighter-rouge">IContentCardsViewBindingHandler</code> interfaces now extend <code class="language-plaintext highlighter-rouge">android.os.Parcelable</code>.
    <ul>
      <li>This ensures that these handlers properly transition across instance state saves and reads.</li>
      <li>Examples on how to extend <code class="language-plaintext highlighter-rouge">Parcelable</code> can be found in <code class="language-plaintext highlighter-rouge">DefaultContentCardsUpdateHandler</code> and <code class="language-plaintext highlighter-rouge">DefaultContentCardsViewBindingHandler</code>.</li>
    </ul>
  </li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> to <code class="language-plaintext highlighter-rouge">BrazePushReceiver</code>.</li>
</ul>

<h5 id="added-40">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.getIsCurrentlyDisplayingInAppMessage()</code>.</li>
  <li>Added ability to configure whether the <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> will automatically register tokens in its <code class="language-plaintext highlighter-rouge">onNewToken</code> method.
    <ul>
      <li>Defaults to whether FCM automatic registration is enabled. Note that FCM automatic registration is a separate configuration option and is not enabled by default.</li>
      <li>Configured by changing the boolean value for <code class="language-plaintext highlighter-rouge">firebase_messaging_service_automatically_register_on_new_token</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>, or at runtime by setting <code class="language-plaintext highlighter-rouge">AppboyConfig.setIsFirebaseMessagingServiceOnNewTokenRegistrationEnabled()</code>.</li>
      <li>Note that the Sender ID used to configure tokens received in <code class="language-plaintext highlighter-rouge">onNewToken()</code> is based on the app’s default Firebase Project rather than the explicitly configured Sender ID on the Braze SDK. These should generally be the same value.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-33">Changed</h5>
<ul>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener.setInAppMessagingRegistrationBlacklist()</code> in favor of <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener.setInAppMessagingRegistrationBlocklist()</code>.</li>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setDeviceObjectWhitelist()</code> in favor of <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setDeviceObjectAllowlist()</code>.</li>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setDeviceObjectWhitelistEnabled()</code> in favor of <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setDeviceObjectAllowlistEnabled()</code>.</li>
</ul>

<h5 id="fixed-51">Fixed</h5>
<ul>
  <li>Fixed an issue where the <code class="language-plaintext highlighter-rouge">AppboyContentCardsFragment</code> would not transition a custom <code class="language-plaintext highlighter-rouge">IContentCardsUpdateHandler</code> or <code class="language-plaintext highlighter-rouge">IContentCardsViewBindingHandler</code> implementation in <code class="language-plaintext highlighter-rouge">onSaveInstanceState()</code>, which caused the defaults for both to be used instead.</li>
  <li>Fixed an issue with deeplink handling where push action button deeplinks would only work once throughout the lifetime of the application.</li>
</ul>

<h2 id="1010">10.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v10.1.0">Release Date</a></p>

<h5 id="changed-34">Changed</h5>
<ul>
  <li>Changed <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code> to extend <code class="language-plaintext highlighter-rouge">FragmentActivity</code> for better fragment management.
    <ul>
      <li>Note that <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code> now no longer performs session and in-app message registration on its own.</li>
      <li>Clients using <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener</code> will see no effect.</li>
      <li>Clients performing manual session integration should override <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code> to add back this registration and set the new Activity via <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder#setCustomWebViewActivityClass()</code> or <code class="language-plaintext highlighter-rouge">com_appboy_custom_html_webview_activity_class_name</code> in the <code class="language-plaintext highlighter-rouge">appboy.xml</code> file.</li>
    </ul>
  </li>
</ul>

<h5 id="added-41">Added</h5>
<ul>
  <li>Added support for receiving messages via the Huawei Messaging Service.</li>
</ul>

<h5 id="fixed-52">Fixed</h5>
<ul>
  <li>Fixed minor display issues with Inline Image Push.</li>
</ul>

<h2 id="1000">10.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v10.0.0">Release Date</a></p>

<h5 id="-breaking-9">⚠ Breaking</h5>
<ul>
  <li>The Android SDK has now fully migrated to AndroidX dependencies. No backwards compatibility is possible with the no longer maintained Android Support Library.
    <ul>
      <li>See https://developer.android.com/jetpack/androidx for more information on AndroidX, including migration steps.</li>
      <li>Braze Android 9.0.0 is the last SDK version compatible with the Android Support Library.</li>
    </ul>
  </li>
  <li>Added a new interface method, <code class="language-plaintext highlighter-rouge">IAppboyNotificationFactory.createNotification(BrazeNotificationPayload)</code>.
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">BrazeNotificationPayload</code> is a data object that performs the task of extracting and surfacing values from the Braze push payload in a far more convenient way.</li>
      <li>Integrations without a custom <code class="language-plaintext highlighter-rouge">IAppboyNotificationFactory</code> will have no breaking changes.</li>
      <li>Integrations with a custom <code class="language-plaintext highlighter-rouge">IAppboyNotificationFactory</code> are recommended to switchover to their non-deprecated counterparts in <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.java</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-42">Added</h5>
<ul>
  <li>Added support for <code class="language-plaintext highlighter-rouge">com_appboy_inapp_show_inapp_messages_automatically</code> boolean configuration for Unity.</li>
</ul>

<h5 id="fixed-53">Fixed</h5>
<ul>
  <li>Fixed support for dark mode in HTML in-app messages and remote urls opened in <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code> for deeplinks via the <code class="language-plaintext highlighter-rouge">prefers-color-scheme: dark</code> css style.
    <ul>
      <li>The decision to display content in dark mode will still be determined at display time based on the device’s state.</li>
    </ul>
  </li>
  <li>Fixed an issue where the card parameter in <code class="language-plaintext highlighter-rouge">com.appboy.IAppboyImageLoader.renderUrlIntoCardView()</code> was null for Content Cards.</li>
</ul>

<h5 id="removed">Removed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.push.AppboyNotificationUtils.handleContentCardsSerializedCardIfPresent()</code>.</li>
</ul>

<h2 id="900">9.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v9.0.0">Release Date</a></p>

<h5 id="-breaking-10">⚠ Breaking</h5>
<ul>
  <li>The Android SDK now has a source and target build compatibility set to Java 8.</li>
</ul>

<h5 id="changed-35">Changed</h5>
<ul>
  <li>Simplified the email regex used in the SDK to centralize most validation on the server.
    <ul>
      <li>The original email validation used is reproduced below:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>(?:[a-z0-9!#$%&amp;'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&amp;'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
</ul>

<h5 id="fixed-54">Fixed</h5>
<ul>
  <li>Fixed an issue where in-app message icon TextViews could throw a <code class="language-plaintext highlighter-rouge">ClassCastException</code> on certain devices and prevent display.</li>
</ul>

<h5 id="removed-1">Removed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.support.AppboyImageUtils.getBitmap(android.net.Uri)</code> in favor of <code class="language-plaintext highlighter-rouge">com.appboy.support.AppboyImageUtils.getBitmap(android.content.Context, android.net.Uri, com.appboy.enums.AppboyViewBounds)</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.AppboyAdmReceiver.CAMPAIGN_ID_KEY</code>.
    <ul>
      <li>Use <code class="language-plaintext highlighter-rouge">Constants.APPBOY_PUSH_CAMPAIGN_ID_KEY</code> instead.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.push.AppboyNotificationUtils.isValidNotificationPriority()</code>.</li>
</ul>

<h2 id="810">8.1.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v8.1.0">Release Date</a></p>

<h5 id="added-support-for-android-11-r-api-30">Added support for Android 11 R (API 30).</h5>
<ul>
  <li>Note that apps targeting API 30 should update to this SDK version.</li>
</ul>

<h5 id="changed-36">Changed</h5>
<ul>
  <li>Changed Content Card subscriptions to automatically re-fire when silent push syncs or test send cards are received via push.</li>
  <li>Improved several accessibility features of In-App Messages and Content Cards as per <a href="https://developer.android.com/guide/topics/ui/accessibility/principles">Principles for improving app accessibility</a>.
    <ul>
      <li>Changed non-informative accessibility content descriptions for in-app message and Content Card images to <code class="language-plaintext highlighter-rouge">@null</code>.</li>
      <li>Content Cards now have content descriptions on their views that incorporate the title and description.</li>
    </ul>
  </li>
  <li>Changed the <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to override the <code class="language-plaintext highlighter-rouge">onNewToken()</code> method to register a Firebase push token when automatic Firebase registration enabled.</li>
</ul>

<h5 id="added-43">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">appboyBridge.getUser().addAlias()</code> to the javascript interface for HTML In-App Messages.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.getConfiguredApiKey()</code> to aid in determining if the SDK has an API key properly configured.</li>
  <li>Added an overload for <code class="language-plaintext highlighter-rouge">IAppboy.getCurrentUser()</code> that adds an asynchronous callback for when the current user is available instead of blocking on the caller thread.
    <ul>
      <li>The following is an example of the full interface:</li>
      <li>
        <div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre><span class="nc">Appboy</span><span class="o">.</span><span class="na">getInstance</span><span class="o">(</span><span class="n">mContext</span><span class="o">).</span><span class="na">getCurrentUser</span><span class="o">(</span><span class="k">new</span> <span class="nc">IValueCallback</span><span class="o">&lt;</span><span class="nc">AppboyUser</span><span class="o">&gt;()</span> <span class="o">{</span>
  <span class="nd">@Override</span>
  <span class="kd">public</span> <span class="kt">void</span> <span class="nf">onSuccess</span><span class="o">(</span><span class="nd">@NonNull</span> <span class="nc">AppboyUser</span> <span class="n">currentUser</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">currentUser</span><span class="o">.</span><span class="na">setFirstName</span><span class="o">(</span><span class="s">"Jared"</span><span class="o">);</span>
  <span class="o">}</span>

  <span class="nd">@Override</span>
  <span class="kd">public</span> <span class="kt">void</span> <span class="nf">onError</span><span class="o">()</span> <span class="o">{}</span>
<span class="o">});</span>
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>A convenience class is also provided with <code class="language-plaintext highlighter-rouge">SimpleValueCallback</code>:</li>
      <li>
        <div class="language-java highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="nc">Appboy</span><span class="o">.</span><span class="na">getInstance</span><span class="o">(</span><span class="n">mContext</span><span class="o">).</span><span class="na">getCurrentUser</span><span class="o">(</span><span class="k">new</span> <span class="nc">SimpleValueCallback</span><span class="o">&lt;</span><span class="nc">AppboyUser</span><span class="o">&gt;()</span> <span class="o">{</span>
  <span class="nd">@Override</span>
  <span class="kd">public</span> <span class="kt">void</span> <span class="nf">onSuccess</span><span class="o">(</span><span class="nd">@NonNull</span> <span class="nc">AppboyUser</span> <span class="n">currentUser</span><span class="o">)</span> <span class="o">{</span>
    <span class="n">currentUser</span><span class="o">.</span><span class="na">setFirstName</span><span class="o">(</span><span class="s">"Julian"</span><span class="o">);</span>
  <span class="o">}</span>
<span class="o">});</span>
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.setClickOutsideModalViewDismissInAppMessageView()</code> allow for the dismissal of a Modal In-App Message when tapping on the frame behind the message itself.
    <ul>
      <li>The default (and historical) value is false, meaning that clicks outside the modal do not close the modal.</li>
      <li>To toggle the feature on, call: <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)</code></li>
    </ul>
  </li>
</ul>

<h5 id="fixed-55">Fixed</h5>
<ul>
  <li>Fixed behavior of the <code class="language-plaintext highlighter-rouge">com.appboy.ui.AppboyContentCardsFragment</code> to not assign margin of the first card in the feed from the top of the feed.</li>
  <li>Fixed an issue with Content Card test sends where the test send wouldn’t be visible in some conditions.</li>
  <li>Fixed an issue with regex based event property triggers not working as expected. Previously they had to match the entire string, now they will search for matches as expected. The regex is now also case-insensitive.</li>
  <li>Fixed an issue with <code class="language-plaintext highlighter-rouge">resolveActivity()</code> in the default <code class="language-plaintext highlighter-rouge">UriAction</code> logic not returning a valid <code class="language-plaintext highlighter-rouge">Activity</code> to handle external deeplinks on Android 11 devices without the <code class="language-plaintext highlighter-rouge">QUERY_ALL_PACKAGES</code> permission.</li>
  <li>Fixed an issue introduced in 4.0.1 where upgrading the SDK could result in server configuration values getting removed until the next session start.</li>
</ul>

<h5 id="removed-2">Removed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setNotificationsEnabledTrackingOn()</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyImageUtils.getPixelsFromDp()</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">ViewUtils.getDisplayHeight()</code>.</li>
</ul>

<h2 id="801">8.0.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v8.0.1">Release Date</a></p>

<h5 id="fixed-56">Fixed</h5>
<ul>
  <li>Fixed an Activity resolution issue in <code class="language-plaintext highlighter-rouge">com.appboy.ui.AppboyWebViewActivity</code> by removing a call to <code class="language-plaintext highlighter-rouge">setDownloadListener()</code>.</li>
  <li>Fixed an implementation issue in 8.0.0 related to setting runtime configuration after stopping the SDK.</li>
</ul>

<h2 id="800">8.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v8.0.0">Release Date</a></p>

<h5 id="-breaking-11">⚠ Breaking</h5>
<ul>
  <li>Integrators note: most of the changes listed below are on lightly used interfaces that do no affect most clients.</li>
  <li>Moved <code class="language-plaintext highlighter-rouge">InAppMessageHtmlBase.getAssetsZipRemoteUrl(), InAppMessageHtmlBase.setAssetsZipRemoteUrl()</code> to <code class="language-plaintext highlighter-rouge">InAppMessageZippedAssetHtmlBase.java</code>.</li>
  <li>Moved <code class="language-plaintext highlighter-rouge">AppboyInAppMessageHtmlFullView.APPBOY_BRIDGE_PREFIX</code> to <code class="language-plaintext highlighter-rouge">AppboyInAppMessageHtmlBaseView.APPBOY_BRIDGE_PREFIX</code></li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">IInAppMessage.getRemoteAssetPathForPrefetch</code> to <code class="language-plaintext highlighter-rouge">IInAppMessage.getRemoteAssetPathsForPrefetch</code> and changed signature to List<String>.</String></li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">IInAppMessage.setLocalAssetPathForPrefetch</code> to <code class="language-plaintext highlighter-rouge">IInAppMessage.setLocalAssetPathsForPrefetch</code> and changed signature to Map&lt;String, String&gt;.</li>
  <li>Created In-App Message interface <code class="language-plaintext highlighter-rouge">IInAppMessageWithImage</code> for slideup, modal, and fulls to hold image based methods. These methods have been refactored out of the <code class="language-plaintext highlighter-rouge">IInAppMessage</code> interface.
    <ul>
      <li>These methods are <code class="language-plaintext highlighter-rouge">getImageUrl(), getRemoteImageUrl(), getLocalImageUrl(), getBitmap(), getImageDownloadSuccessful(), setImageUrl(), setLocalImageUrl(), setImageDownloadSuccessful(), setRemoteImageUrl()</code>, and <code class="language-plaintext highlighter-rouge">setBitmap()</code>.</li>
    </ul>
  </li>
  <li>Content Card backgrounds (in the default UI), now have their colors set via <code class="language-plaintext highlighter-rouge">/android-sdk-ui/src/main/res/drawable-nodpi/com_appboy_content_card_background.xml</code>.</li>
  <li>Several Content Cards related style values are now fully decoupled from News Feed values and are enumerated below.</li>
  <li>The color <code class="language-plaintext highlighter-rouge">@color/com_appboy_card_background_border</code> is now <code class="language-plaintext highlighter-rouge">@color/com_appboy_content_card_background_border</code> for Content Cards.</li>
  <li>The color <code class="language-plaintext highlighter-rouge">@color/com_appboy_card_background_shadow</code> is now <code class="language-plaintext highlighter-rouge">@color/com_appboy_content_card_background_shadow</code> for Content Cards.</li>
  <li>The color <code class="language-plaintext highlighter-rouge">@color/com_appboy_card_background</code> is now <code class="language-plaintext highlighter-rouge">@color/com_appboy_content_card_background</code> for Content Cards.</li>
  <li>The color used for the text in the empty <code class="language-plaintext highlighter-rouge">AppboyContentCardsFragment</code>, <code class="language-plaintext highlighter-rouge">@color/com_appboy_title</code> is now <code class="language-plaintext highlighter-rouge">@color/com_appboy_content_card_empty_text_color</code>.</li>
  <li>Several News Feed dimensions values also used in Content Card styles now have Content Card specific values, enumerated below. Note that if these values were overridden in your styles for use in Content Cards, they will have to be updated to the new keys.</li>
  <li>The dimension <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_card_background_border_left</code> is now <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_content_card_background_border_left</code>.</li>
  <li>The dimension <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_card_background_border_right</code> is now <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_content_card_background_border_right</code>.</li>
  <li>The dimension <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_card_background_border_top</code> is now <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_content_card_background_border_top</code>.</li>
  <li>The dimension <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_card_background_border_bottom</code> is now <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_content_card_background_border_bottom</code>.</li>
  <li>The dimension <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_card_background_shadow_bottom</code> is now <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_content_card_background_shadow_bottom</code>.</li>
  <li>The dimension <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_card_background_corner_radius</code> is now <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_content_card_background_corner_radius</code>.</li>
  <li>The dimension <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_card_background_shadow_radius</code> is now <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_content_card_background_shadow_radius</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyInAppMessageHtmlJavascriptInterface(Context)</code> in favor of <code class="language-plaintext highlighter-rouge">AppboyInAppMessageHtmlJavascriptInterface(Context, IInAppMessageHtml)</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">IAppboy.logPushDeliveryEvent()</code> and <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.logPushDeliveryEvent()</code>.</li>
</ul>

<h5 id="added-44">Added</h5>
<ul>
  <li>Added support for upcoming HTML In-App Message templates.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">appboyBridge.logClick(String), appboyBridge.logClick()</code> and <code class="language-plaintext highlighter-rouge">appboyBridge.getUser().setLanguage()</code> to the javascript interface for HTML In-App Messages.</li>
  <li>Added support for dark mode in HTML in-app messages and remote urls opened in <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code> for deeplinks via the <code class="language-plaintext highlighter-rouge">prefers-color-scheme: dark</code> css style.
    <ul>
      <li>The decision to display content in dark mode will be determined at display time based on the device’s state.</li>
    </ul>
  </li>
  <li>Added support for dark mode in the default Content Cards UI.
    <ul>
      <li>This feature is enabled by default. To disable or change, override the values present in <code class="language-plaintext highlighter-rouge">android-sdk-ui/src/main/res/values-night/colors.xml</code> and <code class="language-plaintext highlighter-rouge">android-sdk-ui/src/main/res/values-night/dimens.xml</code>.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">IAppboy.subscribeToSessionUpdates()</code> which allows for the host app to be notified when a session is started or ended.</li>
  <li>Added the ability to optionally set a custom list of location providers when obtaining a single location, such as on session start. See <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setCustomLocationProviderNames()</code> for more information.
    <ul>
      <li>The following example showcases instructing the SDK to use <code class="language-plaintext highlighter-rouge">LocationManager.GPS_PROVIDER</code> and <code class="language-plaintext highlighter-rouge">LocationManager.NETWORK_PROVIDER</code>.
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>  new AppboyConfig.Builder()
      .setCustomLocationProviderNames(EnumSet.of(LocationProviderName.GPS, LocationProviderName.NETWORK));
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>In xml:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>  &lt;string-array translatable="false" name="com_appboy_custom_location_providers_list"&gt;
    &lt;item&gt;GPS&lt;/item&gt;
    &lt;item&gt;NETWORK&lt;/item&gt;
  &lt;/string-array&gt;
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>By default, only the passive and network providers are used when obtaining a single location from the system.</li>
      <li>This change does not affect Braze Geofences.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-57">Fixed</h5>
<ul>
  <li>Fixed an issue where the pending intent flags on a push story only allowed for the main deeplink to be fired once.</li>
  <li>Fixed behavior of the <code class="language-plaintext highlighter-rouge">com.appboy.ui.AppboyContentCardsFragment</code> to not double the margin of the first card in the feed from the top of the feed.</li>
  <li>Fixed an issue where calling <code class="language-plaintext highlighter-rouge">wipeData()</code> or <code class="language-plaintext highlighter-rouge">disableSdk()</code> could result in not being able to set runtime configuration afterwards.</li>
</ul>

<h5 id="changed-37">Changed</h5>
<ul>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">com.appboy.models.IInAppMessageWithImage#setImageUrl()</code> in favor of <code class="language-plaintext highlighter-rouge">com.appboy.models.IInAppMessageWithImage#setRemoteImageUrl(String)</code>.</li>
</ul>

<h2 id="700">7.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v7.0.0">Release Date</a></p>

<h5 id="-breaking-12">⚠ Breaking</h5>
<ul>
  <li>Made several changes to the default Content Card views to more easily customize and apply ImageView styling.
    <ul>
      <li>Changed <code class="language-plaintext highlighter-rouge">Appboy.ContentCards.BannerImage.ImageContainer.Image</code> to <code class="language-plaintext highlighter-rouge">Appboy.ContentCards.BannerImage.Image</code>.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.ui.contentcards.view.ContentCardViewHolder.createCardImageWithStyle()</code>.</li>
</ul>

<h5 id="added-45">Added</h5>
<ul>
  <li>Added Czech and Ukrainian language translations for Braze UI elements.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">android-sdk-base-jetified</code> and <code class="language-plaintext highlighter-rouge">android-sdk-ui-jetified</code> to reference jetified SDK AAR artifacts from the artifact repository.
    <ul>
      <li>This is a direct replacement for <code class="language-plaintext highlighter-rouge">android-sdk-ui-x</code> and is a more complete integration path for using the Braze SDK with AndroidX.</li>
      <li>Usage as follows:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>dependencies {
implementation "com.appboy:android-sdk-ui-jetified:${BRAZE_SDK_VERSION}"
}
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>If previously using the <code class="language-plaintext highlighter-rouge">android-sdk-ui-x</code> module, you must replace any imports under the <code class="language-plaintext highlighter-rouge">com.appboy.uix.push</code> package to be under <code class="language-plaintext highlighter-rouge">com.appboy.ui.push</code>.</li>
      <li>The gradle properties <code class="language-plaintext highlighter-rouge">android.enableJetifier=true</code> and <code class="language-plaintext highlighter-rouge">android.useAndroidX=true</code> are no longer required when using androidX libraries with the Braze SDK.</li>
    </ul>
  </li>
  <li>Added Material Design Button class names to exported consumer proguard rules.
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>-keepnames class android.support.design.button.MaterialButton
-keepnames class com.google.android.material.button.MaterialButton
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
</ul>

<h5 id="fixed-58">Fixed</h5>
<ul>
  <li>Fixed issue in <code class="language-plaintext highlighter-rouge">AppboyCardAdapter</code> where a card index could be out of bounds when marking a card as seen.</li>
</ul>

<h5 id="changed-38">Changed</h5>
<ul>
  <li>In-App Message “test sends” from the dashboard now display automatically if your app is in the foreground.
    <ul>
      <li>Backgrounded apps will continue to receive a push notification to display the message.</li>
      <li>You can disable this feature by changing the boolean value for <code class="language-plaintext highlighter-rouge">com_appboy_in_app_message_push_test_eager_display_enabled</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>, or at runtime by setting <code class="language-plaintext highlighter-rouge">AppboyConfig.setInAppMessageTestPushEagerDisplayEnabled()</code> to false.</li>
    </ul>
  </li>
  <li>Changed <code class="language-plaintext highlighter-rouge">UriAction</code> to be more easily customizable.</li>
</ul>

<h5 id="removed-3">Removed</h5>
<ul>
  <li>Removed the <code class="language-plaintext highlighter-rouge">android-sdk-ui-x</code> module. See the <code class="language-plaintext highlighter-rouge">Added</code> section for more information.</li>
  <li>Removed the China Push Sample app.</li>
</ul>

<h2 id="600">6.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v6.0.0">Release Date</a></p>

<h5 id="-breaking-13">⚠ Breaking</h5>
<ul>
  <li>Slideup and HTML Full In-App Messages now require the device to be in touch mode at the time of display. This is enforced in their respective <code class="language-plaintext highlighter-rouge">IInAppMessageViewFactory</code> default implementations.
    <ul>
      <li>See https://developer.android.com/reference/android/view/View.html#isInTouchMode().</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">ViewUtils.setFocusableInTouchModeAndRequestFocus()</code>.</li>
  <li><code class="language-plaintext highlighter-rouge">AppboyUnityPlayerNativeActivity</code>, <code class="language-plaintext highlighter-rouge">AppboyOverlayActivity</code>, <code class="language-plaintext highlighter-rouge">AppboyUnityNativeInAppMessageManagerListener</code>, <code class="language-plaintext highlighter-rouge">AppboyUnityPlayerNativeActivity</code>, <code class="language-plaintext highlighter-rouge">AppboyUnityPlayerNativeActivity</code>, and <code class="language-plaintext highlighter-rouge">IAppboyUnityInAppMessageListener</code> have been removed from the <code class="language-plaintext highlighter-rouge">android-sdk-unity</code> project.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">UnityPlayerNativeActivity</code> was deprecated in 2015. See https://unity3d.com/unity/beta/unity5.4.0b1.</li>
    </ul>
  </li>
</ul>

<h5 id="added-46">Added</h5>
<ul>
  <li>Added proper support for navigating and closing Braze In-App Messages with directional-pads/TV remote input devices.</li>
  <li>Added the ability to customize the in-app message button border radius via <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_in_app_message_button_corner_radius</code>.</li>
  <li>Added the ability to customize the in-app message button border color stroke width via <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_in_app_message_button_border_stroke</code>.
    <ul>
      <li>The stroke width used when an in-app message button border is focused is set via <code class="language-plaintext highlighter-rouge">@dimen/com_appboy_in_app_message_button_border_stroke_focused</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-59">Fixed</h5>
<ul>
  <li>Fixed an issue where Content Cards syncs were suppressed too often.</li>
  <li>Fixed an issue where in-app messages could not be closed on TVs or other devices without touch interactions.</li>
</ul>

<h5 id="changed-39">Changed</h5>
<ul>
  <li>Changed in-app messages to return focus back to the view that previously held focus before a message is displayed as given via <code class="language-plaintext highlighter-rouge">Activity#getCurrentFocus()</code>.</li>
</ul>

<h2 id="500">5.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v5.0.0">Release Date</a></p>

<h5 id="-breaking-14">⚠ Breaking</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">IInAppMessageView.hasAppliedWindowInsets()</code>.</li>
</ul>

<h5 id="added-47">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">appboyBridge.logClick()</code> and <code class="language-plaintext highlighter-rouge">appboyBridge.getUser().setLanguage()</code> to the javascript interface for HTML In-App Messages.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.requestGeofences()</code> to request a Braze Geofences update for a manually provided GPS coordinate. Automatic Braze Geofence requests must be disabled to properly use this method.
    <ul>
      <li>Braze Geofences can only be requested once per session, either automatically by the SDK or manually with the above method.</li>
    </ul>
  </li>
  <li>Added the ability to disable Braze Geofences from being requested automatically at session start.
    <ul>
      <li>You can do this by configuring the boolean value for <code class="language-plaintext highlighter-rouge">com_appboy_automatic_geofence_requests_enabled</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
      <li>You can also configure this at runtime by setting <code class="language-plaintext highlighter-rouge">AppboyConfig.setAutomaticGeofenceRequestEnabled()</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-60">Fixed</h5>
<ul>
  <li>Fixed an issue where multiple calls to <code class="language-plaintext highlighter-rouge">ViewCompat.setOnApplyWindowInsetsListener()</code> could result in in-app messages margins getting applied multiple times instead of exactly once.</li>
  <li>Fixed an issue where pure white <code class="language-plaintext highlighter-rouge">#ffffffff</code> in a dark theme in-app message would not be used when the device was in dark mode.
    <ul>
      <li>In this case, the original non-dark theme color would be used by the in-app message instead.</li>
    </ul>
  </li>
</ul>

<h2 id="402">4.0.2</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v4.0.2">Release Date</a></p>

<h5 id="fixed-61">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 4.0.0 where Content Card clicks wouldn’t get forwarded to the parent RecyclerView based on its View’s <code class="language-plaintext highlighter-rouge">clickable</code> status.
    <ul>
      <li>This would result in clicks not being handled or logged for Content Cards.</li>
    </ul>
  </li>
</ul>

<h2 id="401">4.0.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v4.0.1">Release Date</a></p>

<h5 id="fixed-62">Fixed</h5>
<ul>
  <li>Fixed an issue where in-app messages could display behind translucent status and navigation bars.</li>
</ul>

<h2 id="400">4.0.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v4.0.0">Release Date</a></p>

<h5 id="known-issues-with-version-400">Known Issues with version 4.0.0</h5>
<ul>
  <li>Content Card clicks are not handled or logged for Content Cards due to the <code class="language-plaintext highlighter-rouge">"Appboy.ContentCards"</code> style containing the <code class="language-plaintext highlighter-rouge">"clickable=true"</code> style. This is fixed in SDK version 4.0.2.</li>
</ul>

<h5 id="-breaking-15">⚠ Breaking</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">beforeInAppMessageViewOpened(), afterInAppMessageViewOpened(), beforeInAppMessageViewClosed(), afterInAppMessageViewClosed()</code> to the <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener</code> interface.
    <ul>
      <li>These methods are intended to help instrument each stage of the In-App Message View gaining and losing visibility status.</li>
    </ul>
  </li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">Card.getIsDismissible()</code> to <code class="language-plaintext highlighter-rouge">Card.getIsDismissibleByUser()</code>.</li>
</ul>

<h5 id="added-48">Added</h5>
<ul>
  <li>Added the ability to more easily test In-App Messages from the dashboard when sending a test push by bypassing the need to click the test push notification and instead directly display the test In-App Message when the app is in the foreground.
    <ul>
      <li>A push notification will still display if a test In-App Message push is received and the app is in the background.</li>
      <li>You can enable this feature by configuring the boolean value for <code class="language-plaintext highlighter-rouge">com_appboy_in_app_message_push_test_eager_display_enabled</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>. The default value is false.</li>
      <li>You can also enable this feature at runtime by setting <code class="language-plaintext highlighter-rouge">AppboyConfig.setInAppMessageTestPushEagerDisplayEnabled()</code> to true. The default value is false.</li>
    </ul>
  </li>
  <li>Added the ability to customize how In-App Messages views are added to the view hierarchy with a custom <code class="language-plaintext highlighter-rouge">IInAppMessageViewWrapperFactory</code>.
    <ul>
      <li>See <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.setCustomInAppMessageViewWrapperFactory()</code>.</li>
      <li>For lightweight customizations, consider extending <code class="language-plaintext highlighter-rouge">DefaultInAppMessageViewWrapper</code> and overriding <code class="language-plaintext highlighter-rouge">getParentViewGroup()</code>, <code class="language-plaintext highlighter-rouge">getLayoutParams()</code>, and <code class="language-plaintext highlighter-rouge">addInAppMessageViewToViewGroup()</code>.</li>
      <li>Addresses https://github.com/braze-inc/braze-android-sdk/issues/138.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">Card.setIsDismissibleByUser()</code> to allow for integrators to disable the default swipe-to-dismiss behavior on a per-card basis.</li>
  <li>Added the ability to set the initial <code class="language-plaintext highlighter-rouge">AppboyLogger</code> log level via <code class="language-plaintext highlighter-rouge">appboy.xml</code>.
    <ul>
      <li>In your <code class="language-plaintext highlighter-rouge">appboy.xml</code>, set an integer value for <code class="language-plaintext highlighter-rouge">com_appboy_logger_initial_log_level</code>. The integer should correspond to a constant in <code class="language-plaintext highlighter-rouge">Log</code>, such as <code class="language-plaintext highlighter-rouge">Log.VERBOSE</code> which is 2.</li>
      <li>Values set via <code class="language-plaintext highlighter-rouge">AppboyLogger.setLogLevel()</code> take precedence over values set in <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
    </ul>
  </li>
  <li>Added the ability to use a custom Activity when opening deeplinks inside the app via a WebView. This Activity will be used in place of the default <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code>.
    <ul>
      <li>You can do this by configuring the string value for <code class="language-plaintext highlighter-rouge">com_appboy_custom_html_webview_activity_class_name</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>. Note that the class name used <code class="language-plaintext highlighter-rouge">appboy.xml</code> must be the exact class name string as returned from <code class="language-plaintext highlighter-rouge">YourClass.class.getName()</code>.</li>
      <li>You can also configure this at runtime by setting <code class="language-plaintext highlighter-rouge">AppboyConfig.setCustomWebViewActivityClass()</code>.</li>
      <li>To retrieve the url in your custom WebView:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>final Bundle extras = getIntent().getExtras();
if (extras.containsKey(Constants.APPBOY_WEBVIEW_URL_EXTRA)) {
String url = extras.getString(Constants.APPBOY_WEBVIEW_URL_EXTRA);
}
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
</ul>

<h5 id="fixed-63">Fixed</h5>
<ul>
  <li>Fixed the inability to scroll through Content Cards when not using standard input mechanisms, aiding accessibility.
    <ul>
      <li>All Content Card views now have <code class="language-plaintext highlighter-rouge">selectable</code> and <code class="language-plaintext highlighter-rouge">focusable</code> attributes set to true.</li>
      <li>Amazon Fire TV integrators should update to this version.</li>
    </ul>
  </li>
  <li>Changed <code class="language-plaintext highlighter-rouge">AppboyInAppMessageHtmlUserJavascriptInterface.setCustomAttribute()</code> in the HTML javascript bridge to not coerce <code class="language-plaintext highlighter-rouge">Double</code> into <code class="language-plaintext highlighter-rouge">Float</code>.</li>
  <li>Fixed default Content Card rendering on low screen density devices. Previously, Content Cards could render without a margin and overflow off screen.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">@dimens/com_appboy_content_cards_max_width</code> now accurately sets the maximum possible width of a Content Card.</li>
      <li><code class="language-plaintext highlighter-rouge">@dimens/com_appboy_content_cards_divider_left_margin</code> and <code class="language-plaintext highlighter-rouge">@dimens/com_appboy_content_cards_divider_right_margin</code> are now used to provide a margin for Content Cards when the width of the Content Card does not exceed the max width of <code class="language-plaintext highlighter-rouge">@dimens/com_appboy_content_cards_max_width</code>.</li>
    </ul>
  </li>
  <li>Fixed an issue where images in Content Cards could be resized before they had finished a layout, resulting in an 0 width/height ImageView.</li>
</ul>

<h5 id="changed-40">Changed</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">InAppMessageImmersiveBase.getMessageButtons()</code> is now guaranteed to be non-null. When buttons are not set on the message, this list will be non-null and empty.
    <ul>
      <li>Calling <code class="language-plaintext highlighter-rouge">InAppMessageImmersiveBase.setMessageButtons()</code> with null will instead clear the <code class="language-plaintext highlighter-rouge">MessageButton</code> list</li>
    </ul>
  </li>
  <li>Changed the SDK to compile against the 18.0.0 version of the Firebase Cloud Messaging dependency.</li>
  <li>Updated the exported <code class="language-plaintext highlighter-rouge">android-sdk-ui</code> consumer proguard rules to keep javascript interface methods.</li>
  <li>Changed the WebView used in HTML In-App Messages to have DOM storage enabled via <code class="language-plaintext highlighter-rouge">setDomStorageEnabled(true)</code>.</li>
  <li>Changed Content Cards to allow for blank or empty values for the title or description. In these situations, the <code class="language-plaintext highlighter-rouge">TextView</code>’s visibility is changed to <code class="language-plaintext highlighter-rouge">GONE</code> in the view hierarchy.</li>
</ul>

<h5 id="removed-4">Removed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">Constants.APPBOY_WEBVIEW_URL_KEY</code>.</li>
</ul>

<h2 id="380">3.8.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v3.8.0">Release Date</a></p>

<h5 id="-breaking-16">⚠ Breaking</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">renderUrlIntoInAppMessageView()</code>, <code class="language-plaintext highlighter-rouge">renderUrlIntoCardView()</code>, <code class="language-plaintext highlighter-rouge">getPushBitmapFromUrl()</code>, and <code class="language-plaintext highlighter-rouge">getInAppMessageBitmapFromUrl()</code> to the <code class="language-plaintext highlighter-rouge">IAppboyImageLoader</code> interface. These methods provide more information about the rendered object. For example, <code class="language-plaintext highlighter-rouge">renderUrlIntoCardView()</code> provides the <code class="language-plaintext highlighter-rouge">Card</code> object being rendered in the feed.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">IAppboyImageLoader.renderUrlIntoView()</code> and <code class="language-plaintext highlighter-rouge">IAppboyImageLoader.getBitmapFromUrl()</code> have been removed.</li>
      <li>For maintaining behavioral parity, <code class="language-plaintext highlighter-rouge">renderUrlIntoInAppMessageView()</code> and <code class="language-plaintext highlighter-rouge">renderUrlIntoCardView()</code> can reuse your previous <code class="language-plaintext highlighter-rouge">IAppboyImageLoader.renderUrlIntoView()</code> implementation while <code class="language-plaintext highlighter-rouge">getPushBitmapFromUrl()</code> and <code class="language-plaintext highlighter-rouge">getInAppMessageBitmapFromUrl()</code> can reuse your previous <code class="language-plaintext highlighter-rouge">IAppboyImageLoader.getBitmapFromUrl()</code> implementation.</li>
      <li>The Glide <code class="language-plaintext highlighter-rouge">IAppboyImageLoader</code> implementation has been updated and can be found <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/samples/glide-image-integration/src/main/java/com/appboy/glideimageintegration/GlideAppboyImageLoader.java">here</a>.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">MessageButton#getIsSecondaryButton()</code> and <code class="language-plaintext highlighter-rouge">MessageButton#setIsSecondaryButton()</code>.</li>
</ul>

<h5 id="added-49">Added</h5>
<ul>
  <li>Added support for the upcoming feature, In-App Messages in Dark Mode.
    <ul>
      <li>Dark Mode enabled messages must be created from the dashboard. Braze does not dynamically theme In-App Messages for Dark Mode.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">IInAppMessageThemeable</code> interface to In-App Messages, which adds <code class="language-plaintext highlighter-rouge">enableDarkTheme()</code> to In-App Messages.</li>
      <li>To configure/disable Braze from automatically applying a Dark Theme (when available from Braze’s servers), use a custom <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener</code>.
        <ul>
          <li>
            <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>  if (inAppMessage instanceof IInAppMessageThemeable &amp;&amp; ViewUtils.isDeviceInNightMode(AppboyInAppMessageManager.getInstance().getApplicationContext())) {
    ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
  }
</pre></td></tr></tbody></table></code></pre></div>            </div>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">Card.isContentCard()</code>.</li>
  <li>Added the ability to use an existing color resource for <code class="language-plaintext highlighter-rouge">com_appboy_default_notification_accent_color</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.
    <ul>
      <li>For example: <code class="language-plaintext highlighter-rouge">&lt;color name="com_appboy_default_notification_accent_color"&gt;@color/my_color_here&lt;/color&gt;</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-64">Fixed</h5>
<ul>
  <li>Fixed an edge case where the <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager</code> could throw an <code class="language-plaintext highlighter-rouge">NullPointerException</code> if an in-app message was in the process of animating out while <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.unregisterInAppMessageManager()</code> was called.</li>
  <li>Fixed an issue where multiple subscribers to Content Cards updates could cause a <code class="language-plaintext highlighter-rouge">ConcurrentModificationException</code> if they simultaneously attempted to mutate the list returned in <code class="language-plaintext highlighter-rouge">ContentCardsUpdatedEvent.getAllCards()</code>.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">ContentCardsUpdatedEvent.getAllCards()</code> now returns a shallow copy of the list of Content Cards model objects.</li>
    </ul>
  </li>
  <li>Fixed an issue (introduced in 3.7.0) where the background color for fullscreen in-app messages was not set.</li>
  <li>Fixed an issue (introduced in 3.7.0) were images for fullscreen in-app messages would not appear on API 21 and below devices.</li>
</ul>

<h2 id="371">3.7.1</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v3.7.1">Release Date</a></p>

<h5 id="added-50">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">IInAppMessage.setExtras()</code> to set extras on In-App Messages.</li>
</ul>

<h5 id="fixed-65">Fixed</h5>
<ul>
  <li>Fixed an issue where a slow loading HTML In-App Message could throw an exception if the Activity changed before <code class="language-plaintext highlighter-rouge">onPageFinished()</code> was called.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">FEATURE_INDETERMINATE_PROGRESS</code> and <code class="language-plaintext highlighter-rouge">FEATURE_PROGRESS</code> from <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code>.</li>
</ul>

<h2 id="370">3.7.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v3.7.0">Release Date</a></p>

<h5 id="known-issues">Known Issues</h5>
<ul>
  <li>This release introduced issues with in-app message unregistration (<code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.unregisterInAppMessageManager()</code>) and fullscreen in-app messages. These issues have been fixed in version 3.8.0 of the SDK.</li>
</ul>

<h5 id="breaking-22">Breaking</h5>
<ul>
  <li>Added the <code class="language-plaintext highlighter-rouge">applyWindowInsets()</code> method to <code class="language-plaintext highlighter-rouge">IInAppMessageView</code> interface. This allows for granular customization at the in-app message view level with respect to device notches.</li>
  <li>The old configuration key used in <code class="language-plaintext highlighter-rouge">appboy.xml</code> for disabling location collection <code class="language-plaintext highlighter-rouge">com_appboy_disable_location_collection</code> is now deleted. This key is replaced by <code class="language-plaintext highlighter-rouge">com_appboy_enable_location_collection</code>. The default value of <code class="language-plaintext highlighter-rouge">com_appboy_disable_location_collection</code> is false. Braze location collection is disabled by default starting with Braze SDK version 3.6.0.</li>
  <li>Removes the Feedback feature from the SDK. All Feedback methods on the SDK, including <code class="language-plaintext highlighter-rouge">Appboy.submitFeedback()</code> and <code class="language-plaintext highlighter-rouge">Appboy.logFeedbackDisplayed()</code>, are removed.</li>
</ul>

<h5 id="fixed-66">Fixed</h5>
<ul>
  <li>Changed the behavior of In-App Messages to allow analytics to be logged again when the same In-App Message is displaying a new time.</li>
</ul>

<h5 id="changed-41">Changed</h5>
<ul>
  <li>Improves support for in-app messages on “notched” devices (for example, iPhone X, Pixel 3XL). Full-screen messages now expand to fill the entire screen of any phone, while covering the status bar.</li>
  <li>Changed the behavior of HTML In-App Messages to not display until the content has finished loading as determined via <code class="language-plaintext highlighter-rouge">WebViewClient#onPageFinished()</code> on the in-app message’s <code class="language-plaintext highlighter-rouge">WebView</code>.</li>
</ul>

<h2 id="360">3.6.0</h2>

<p><a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v3.6.0">Release Date</a></p>

<h5 id="breaking-23">Breaking</h5>
<ul>
  <li>External user ids (provided via <code class="language-plaintext highlighter-rouge">Appboy.changeUser()</code>), are now limited to 997 bytes in UTF-8 encoding.
    <ul>
      <li>Existing user IDs will be truncated to 997 bytes in UTF-8 encoding.</li>
      <li>New user IDs (via <code class="language-plaintext highlighter-rouge">Appboy.changeUser()</code>) will be rejected if too long.</li>
      <li>This byte limit can be read in code via <code class="language-plaintext highlighter-rouge">Constants#USER_ID_MAX_LENGTH_BYTES</code>.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">IInAppMessage.getMessageType()</code> to return the <code class="language-plaintext highlighter-rouge">MessageType</code> enum for easier in-app message type checking.</li>
  <li>Braze location collection is disabled by default. If you choose to use our location services, you must explicitly enable location services.
    <ul>
      <li>You can do this by configuring the boolean value for <code class="language-plaintext highlighter-rouge">com_appboy_enable_location_collection</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>. The default value is false.</li>
      <li>You can also enable location collection at runtime by setting <code class="language-plaintext highlighter-rouge">AppboyConfig.setIsLocationCollectionEnabled()</code> to true.</li>
      <li>The old configuration value <code class="language-plaintext highlighter-rouge">com_appboy_disable_location_collection</code> in appboy.xml is deprecated. It should be replaced with new configuration value of <code class="language-plaintext highlighter-rouge">com_appboy_enable_location_collection</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-51">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyContentCardsFragment.getContentCardsRecyclerView()</code> to obtain the RecyclerView associated with the Content Cards fragment.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.getDefaultInAppMessageViewFactory()</code> to simplify most custom implementations of <code class="language-plaintext highlighter-rouge">IInAppMessageViewFactory</code>.</li>
</ul>

<h5 id="changed-42">Changed</h5>
<ul>
  <li>Changed the click target area of in-app message close buttons to 48dp. The close button drawable was increased to <code class="language-plaintext highlighter-rouge">20dp</code> from <code class="language-plaintext highlighter-rouge">14dp</code>.
    <ul>
      <li>The width/height in dp of this click target can be configured with a <code class="language-plaintext highlighter-rouge">dimens</code> override for <code class="language-plaintext highlighter-rouge">com_appboy_in_app_message_close_button_click_area_width</code> and <code class="language-plaintext highlighter-rouge">com_appboy_in_app_message_close_button_click_area_height</code> respectively.</li>
    </ul>
  </li>
  <li>Changed <code class="language-plaintext highlighter-rouge">UriUtils.getQueryParameters()</code> to handle the parsing of an opaque/non-hierarchical Uri such as <code class="language-plaintext highlighter-rouge">mailto:</code> or <code class="language-plaintext highlighter-rouge">tel:</code>.</li>
</ul>

<h2 id="350">3.5.0</h2>

<h5 id="breaking-24">Breaking</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">IAppboyUnitySupport</code> interface from Appboy singleton object. Its methods have been added to the <code class="language-plaintext highlighter-rouge">IAppboy</code> interface.</li>
  <li>The <code class="language-plaintext highlighter-rouge">IAction</code> in <code class="language-plaintext highlighter-rouge">IContentCardsActionListener.onContentCardClicked()</code> is now annotated as <code class="language-plaintext highlighter-rouge">@Nullable</code>. Previously, this field was always non-null.</li>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">FLAG_ACTIVITY_NEW_TASK</code> was not added to configured back stack Activities when opening push. This resulted in push notifications failing to open deep links in that situation.
    <ul>
      <li>Custom push back stack Activities are set via <code class="language-plaintext highlighter-rouge">AppboyConfig.setPushDeepLinkBackStackActivityClass()</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-52">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.getCachedContentCards()</code> to provide an easier way to obtain the cached/offline list of Content Cards on the device.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.deserializeContentCard()</code> to allow for the deserialization of a Content Card. Useful for custom integrations that store the Content Cards data models in their own storage and recreate the Content Card afterwards.</li>
</ul>

<h5 id="changed-43">Changed</h5>
<ul>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">Card.isEqualTo()</code> in favor of using <code class="language-plaintext highlighter-rouge">Card.equals()</code>.</li>
</ul>

<h5 id="fixed-67">Fixed</h5>
<ul>
  <li>Fixed behavior in Content Cards and News Feed where cards without a click action wouldn’t have their client click listeners called.</li>
</ul>

<h2 id="340">3.4.0</h2>

<h5 id="added-53">Added</h5>
<ul>
  <li>Added support for Android 10 Q (API 29).
    <ul>
      <li>With the addition of the <code class="language-plaintext highlighter-rouge">android.permission.ACCESS_BACKGROUND_LOCATION</code> permission in Android Q, this permission is now required for Braze Geofences to work on Android Q+ devices. Please see the documentation for more information.</li>
      <li>The <code class="language-plaintext highlighter-rouge">AppboyNotificationRoutingActivity</code> class is now sent with the <code class="language-plaintext highlighter-rouge">Intent.FLAG_ACTIVITY_NO_HISTORY</code> Intent flag. This is not expected to be a user visible change nor will require any integration changes.</li>
    </ul>
  </li>
  <li>Added the ability to enable Braze Geofences without enabling Braze location collection. Set <code class="language-plaintext highlighter-rouge">AppboyConfig.setGeofencesEnabled()</code> or <code class="language-plaintext highlighter-rouge">com_appboy_geofences_enabled</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code> to enable Braze Geofences.
    <ul>
      <li>Note that Braze Geofences will continue to work on existing integrations if location collection is enabled and this new configuration is not present. This new configuration is intended for integrations that want Braze Geofences, but not location collection enabled as well.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.setGoogleAdvertisingId()</code> to pass a Google Advertising ID and Ad Tracking Limiting enabled flag back to Braze. Note that the SDK will not automatically collect either field.</li>
</ul>

<h5 id="fixed-68">Fixed</h5>
<ul>
  <li>Fixed in-app message buttons not properly respecting colors when using a Material Design style theme.</li>
</ul>

<h5 id="breaking-25">Breaking</h5>
<ul>
  <li>Geofences on Android Q+ devices will not work without the <code class="language-plaintext highlighter-rouge">android.permission.ACCESS_BACKGROUND_LOCATION</code> permission.</li>
  <li>Changed the signature of <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener.onInAppMessageButtonClicked()</code> to include the in-app message of the clicked button.</li>
  <li>Removed the deprecated <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity.URL_EXTRA</code>. Please use <code class="language-plaintext highlighter-rouge">Constants.APPBOY_WEBVIEW_URL_EXTRA</code> instead.</li>
</ul>

<h2 id="330">3.3.0</h2>

<h5 id="known-issues-1">Known Issues</h5>
<ul>
  <li>If using a defined back stack Activity (set via <code class="language-plaintext highlighter-rouge">AppboyConfig.setPushDeepLinkBackStackActivityClass()</code>), then push notifications containing deep links won’t be opened. This behavior is fixed in 3.4.1.</li>
</ul>

<h5 id="changed-44">Changed</h5>
<ul>
  <li>Changed the behavior of push deep links to not restart the launcher activity of the app when clicked.</li>
  <li>Changed the broadcast receiver responsible for sealing sessions after the session timeout to use <code class="language-plaintext highlighter-rouge">goAsync</code> to lower the occurrence of ANRs on certain devices.
    <ul>
      <li>This ANR would contain the constant <code class="language-plaintext highlighter-rouge">APPBOY_SESSION_SHOULD_SEAL</code> in the Google Play Console.</li>
    </ul>
  </li>
  <li>Changed the default video poster (the large black &amp; white play icon) used by default in HTML in-app messages to be transparent.</li>
</ul>

<h5 id="added-54">Added</h5>
<ul>
  <li>Added support for <code class="language-plaintext highlighter-rouge">long</code> type event properties.</li>
</ul>

<h5 id="fixed-69">Fixed</h5>
<ul>
  <li>Fixed fullscreen in-app messages on notched devices rendering with a gap at the top of the in-app message.</li>
  <li>Fixed behavior of in-app messages where modal display would take up the entire screen after successive rotations on older devices.</li>
</ul>

<h2 id="322">3.2.2</h2>

<h5 id="changed-45">Changed</h5>
<ul>
  <li>Improved the reliability of the session start location logic when location collection is enabled.</li>
  <li>Changed the in-app message trigger behavior to not perform custom event triggering until any pending server trigger requests have finished.</li>
</ul>

<h5 id="fixed-70">Fixed</h5>
<ul>
  <li>Fixed a bug in <code class="language-plaintext highlighter-rouge">AppboyInAppMessageImageView</code> that made images loaded with Glide appear blurry or not appear when setting an aspect ratio.</li>
</ul>

<h2 id="321">3.2.1</h2>

<h5 id="added-55">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService.handleBrazeRemoteMessage()</code> to facilitate forwarding a Firebase <code class="language-plaintext highlighter-rouge">RemoteMessage</code> from your <code class="language-plaintext highlighter-rouge">FirebaseMessagingService</code> to the <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code>.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService.handleBrazeRemoteMessage()</code> will return false if the argument <code class="language-plaintext highlighter-rouge">RemoteMessage</code> did not originate from Braze. In that case, the <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> will do nothing.</li>
      <li>A helper method <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService.isBrazePushNotification()</code> will also return true if the <code class="language-plaintext highlighter-rouge">RemoteMessage</code> originated from Braze.</li>
    </ul>
  </li>
</ul>

<h4 id="fixed-71">Fixed</h4>
<ul>
  <li>Fixed an issue with <code class="language-plaintext highlighter-rouge">AppboyInAppMessageBoundedLayout</code> having a custom styleable attribute that collided with a preset Android attribute.</li>
</ul>

<h2 id="320">3.2.0</h2>

<h5 id="important-6">Important</h5>
<ul>
  <li>Please note the breaking push changes in release 3.1.1 regarding the <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> before upgrading to this version.</li>
</ul>

<h5 id="fixed-72">Fixed</h5>
<ul>
  <li>Fixed an issue where a filename’s canonical path was not validated during zip file extraction.</li>
  <li>Fixed an issue where the SDK setup verification would erroneously always log a warning that the <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> was registered using the old <code class="language-plaintext highlighter-rouge">com.google.android.c2dm.intent.RECEIVE</code> intent-filter.</li>
</ul>

<h5 id="changed-46">Changed</h5>
<ul>
  <li>Improved the look and feel of in-app messages to adhere to the latest UX and UI best practices. Changes affect font sizes, padding, and responsiveness across all message types. Now supports button border styling.</li>
</ul>

<h5 id="added-56">Added</h5>
<ul>
  <li>Added collection of <code class="language-plaintext highlighter-rouge">ActivityManager.isBackgroundRestricted()</code> to device collection information.</li>
</ul>

<h2 id="311">3.1.1</h2>

<h5 id="breaking-26">Breaking</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to directly use the Firebase messaging event <code class="language-plaintext highlighter-rouge">com.google.firebase.MESSAGING_EVENT</code>. This is now the required way to integrate Firebase push with Braze. The <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> should be removed from your <code class="language-plaintext highlighter-rouge">AndroidManifest</code> and replaced with the following:
    <ul>
      <li>
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre>&lt;service android:name="com.appboy.AppboyFirebaseMessagingService"&gt;
  &lt;intent-filter&gt;
    &lt;action android:name="com.google.firebase.MESSAGING_EVENT" /&gt;
  &lt;/intent-filter&gt;
&lt;/service&gt;
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>Also note that any <code class="language-plaintext highlighter-rouge">c2dm</code> related permissions should be removed from your manifest as Braze does not require any extra permissions for <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to work correctly.</li>
    </ul>
  </li>
  <li>Changed signature of <code class="language-plaintext highlighter-rouge">Appboy.logPushNotificationActionClicked()</code>.</li>
</ul>

<h5 id="added-57">Added</h5>
<ul>
  <li>Added ability to render HTML elements in push notifications via <code class="language-plaintext highlighter-rouge">AppboyConfig.setPushHtmlRenderingEnabled()</code> and also <code class="language-plaintext highlighter-rouge">com_appboy_push_notification_html_rendering_enabled</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.
    <ul>
      <li>This allows the ability to use “multicolor” text in your push notifications.</li>
      <li>Note that html rendering be used on all push notification text fields when this feature is enabled.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-73">Fixed</h5>
<ul>
  <li>Fixed behavior where the app would be reopened after clicking notification action buttons with a “close” button.</li>
  <li>Fixed behavior where in-app messages would not apply proper margins on devices with notched displays and would appear obscured by the notch.</li>
  <li>Fixed an issue that caused the enum <code class="language-plaintext highlighter-rouge">DeviceKey</code> to be unavailable in our public API.</li>
  <li>Fixed an issue in the <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> where the “is uninstall tracking push” method was looking for the extras bundle before its preprocessing into a bundle. This would result in uninstall tracking push being forwarded to your broadcast receiver as a silent push when it should not.</li>
  <li>Fixed an issue in the <code class="language-plaintext highlighter-rouge">AppboyLruImageLoader</code> where very large bitmaps stored in the cache could throw <code class="language-plaintext highlighter-rouge">OutOfMemoryError</code> when retrieving them from the cache.</li>
</ul>

<h5 id="changed-47">Changed</h5>
<ul>
  <li>Changed behavior of the Feed and Content Cards image loader to always resize images to their true source aspect ratio after download.</li>
</ul>

<h2 id="310">3.1.0</h2>

<h5 id="breaking-27">Breaking</h5>
<ul>
  <li>Renamed <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.wakeScreenIfHasPermission()</code> to <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.wakeScreenIfAppropriate()</code>. Wakelocks can now be configured to not wake the device screen for push notifications.
    <ul>
      <li>This can be set via <code class="language-plaintext highlighter-rouge">AppboyConfig.setIsPushWakeScreenForNotificationEnabled()</code> and also <code class="language-plaintext highlighter-rouge">com_appboy_push_wake_screen_for_notification_enabled</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-58">Added</h5>
<ul>
  <li>A drop-in <code class="language-plaintext highlighter-rouge">AppboyContentCardsActivity</code> class has been added which can be used to display Braze Content Cards.</li>
  <li>Added an appboyBridge ready event to know precisely when the appboyBridge has finished loading in the context of an HTML in-app message.
    <ul>
      <li>Example below:
        <div class="language-javascript highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre> <span class="o">&lt;</span><span class="nx">script</span> <span class="nx">type</span><span class="o">=</span><span class="dl">"</span><span class="s2">text/javascript</span><span class="dl">"</span><span class="o">&gt;</span>
   <span class="kd">function</span> <span class="nf">logMyCustomEvent</span><span class="p">()</span> <span class="p">{</span>
     <span class="nx">appboyBridge</span><span class="p">.</span><span class="nf">logCustomEvent</span><span class="p">(</span><span class="dl">'</span><span class="s1">My Custom Event</span><span class="dl">'</span><span class="p">);</span>
   <span class="p">}</span>
   <span class="nb">window</span><span class="p">.</span><span class="nf">addEventListener</span><span class="p">(</span><span class="dl">'</span><span class="s1">ab.BridgeReady</span><span class="dl">'</span><span class="p">,</span> <span class="nx">logMyCustomEvent</span><span class="p">,</span> <span class="kc">false</span><span class="p">);</span>
 <span class="o">&lt;</span><span class="sr">/script</span><span class="err">&gt;
</span></pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">Constants.TRAFFIC_STATS_THREAD_TAG</code> to identify the Braze network traffic with the <code class="language-plaintext highlighter-rouge">TrafficStats</code> API.</li>
  <li>Added the ability to configure a blacklist of Activity classes to disable automatic session handling and in-app message registration in the AppboyLifecycleCallbackListener. See <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener.setActivityClassInAppMessagingRegistrationBlacklist()</code>, <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener.setActivityClassSessionHandlingBlacklist()</code>, and constructor <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener(boolean, boolean, Set&lt;Class&gt;, Set&lt;Class&gt;)</code>.</li>
</ul>

<h5 id="changed-48">Changed</h5>
<ul>
  <li>Deprecated the Feedback feature. This feature is disabled for new accounts, and will be removed in a future SDK release.</li>
  <li>Changed the deprecated status of the <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.isUninstallTrackingPush()</code> method. Note that uninstall tracking notifications will not be forwarded to registered receivers.</li>
  <li>Improved in-app message triggering logic to fall back to lower priority messages when the Braze server aborts templating (e.g. from a Connected Content abort in the message body, or because the user is no longer in the correct segment for the message)</li>
</ul>

<h2 id="301">3.0.1</h2>

<h5 id="changed-49">Changed</h5>
<ul>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">Card.isRead()</code> and <code class="language-plaintext highlighter-rouge">Card.setIsRead()</code>. Please use <code class="language-plaintext highlighter-rouge">Card.isIndicatorHighlighted()</code> and <code class="language-plaintext highlighter-rouge">Card.setIndicatorHighlighted()</code> instead.</li>
</ul>

<h5 id="added-59">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">Card.isClicked()</code>. Clicks made through <code class="language-plaintext highlighter-rouge">Card.logClick()</code> are now saved locally on the device for Content Cards.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyConfig.setIsInAppMessageAccessibilityExclusiveModeEnabled()</code> which forces accessibility readers to only be able to read currently displaying in-app messages and no other screen contents.
    <ul>
      <li>This can also be set via <code class="language-plaintext highlighter-rouge">com_appboy_device_in_app_message_accessibility_exclusive_mode_enabled</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="300">3.0.0</h2>

<h5 id="breaking-28">Breaking</h5>
<ul>
  <li>From <code class="language-plaintext highlighter-rouge">AppboyConfig</code>, removed <code class="language-plaintext highlighter-rouge">getEnableBackgroundLocationCollection()</code>, <code class="language-plaintext highlighter-rouge">getLocationUpdateTimeIntervalSeconds()</code>, and <code class="language-plaintext highlighter-rouge">getLocationUpdateDistance()</code> and their respective setters in <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyInAppMessageImmersiveBaseView.getMessageButtonsView()</code>.</li>
  <li>Removed the Fresco image library from the SDK. To displaying GIFs, you must use a custom image library. Please see <code class="language-plaintext highlighter-rouge">IAppboy#setAppboyImageLoader(IAppboyImageLoader)</code>.
    <ul>
      <li>We recommend the <a href="https://bumptech.github.io/glide/">Glide Image Library</a> as a Fresco replacement.</li>
      <li><code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setFrescoLibraryEnabled()</code> has been removed.</li>
      <li><code class="language-plaintext highlighter-rouge">AppboyConfigurationProvider.getIsFrescoLibraryUseEnabled()</code> has been removed.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-74">Fixed</h5>
<ul>
  <li>Fixed a NPE issue with the RecyclerView while saving the instance state in the <code class="language-plaintext highlighter-rouge">AppboyContentCardsFragment</code>.</li>
</ul>

<h5 id="added-60">Added</h5>
<ul>
  <li>Added the ability to set location custom attributes on the html in-app message javascript interface.</li>
  <li>Added compatibility with androidX dependencies.
    <ul>
      <li>This initial release adds direct compatibility for classes found under the <code class="language-plaintext highlighter-rouge">com.appboy.push</code> package. These classes are commonly used in conjunction with an <code class="language-plaintext highlighter-rouge">IAppboyNotificationFactory</code>. To use these compatible classes, add the following gradle import: <code class="language-plaintext highlighter-rouge">implementation 'com.appboy:android-sdk-ui-x:VERSION'</code> and replace your imports to fall under the <code class="language-plaintext highlighter-rouge">com.appboy.uix.push</code> package.</li>
      <li>The gradle properties <code class="language-plaintext highlighter-rouge">android.enableJetifier=true</code> and <code class="language-plaintext highlighter-rouge">android.useAndroidX=true</code> are required when using androidX libraries with the Braze SDK.</li>
    </ul>
  </li>
  <li>Added nullability annotation to <code class="language-plaintext highlighter-rouge">Appboy</code> and <code class="language-plaintext highlighter-rouge">AppboyUser</code> for better Kotlin interoperability.</li>
  <li>Added the ability to optionally whitelist keys in the device object. See <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setDeviceObjectWhitelistEnabled()</code> and <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setDeviceObjectWhitelist()</code> for more information.
    <ul>
      <li>The following example showcases whitelisting the device object to only include the Android OS version and device locale in the device object.
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>  new AppboyConfig.Builder()
      .setDeviceObjectWhitelistEnabled(true)
      .setDeviceObjectWhitelist(EnumSet.of(DeviceKey.ANDROID_VERSION, DeviceKey.LOCALE));
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
</ul>

<h5 id="removed-5">Removed</h5>
<ul>
  <li>Removed the ability to optionally track locations in the background.</li>
  <li>Removed Cross Promotion cards from the News Feed.
    <ul>
      <li>Cross Promotion cards have also been removed as a card model and will thus no longer be returned.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-50">Changed</h5>
<ul>
  <li>Updated the Baidu China Push sample to use the version 2.9 Baidu JNI libraries and version 6.1.1.21 of the Baidu jar.</li>
</ul>

<h2 id="270">2.7.0</h2>

<h5 id="breaking-29">Breaking</h5>
<ul>
  <li>Renamed <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code> to <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code>. This receiver is intended to be used for Firebase integrations and thus the <code class="language-plaintext highlighter-rouge">com.google.android.c2dm.intent.REGISTRATION</code> intent-filter action in your <code class="language-plaintext highlighter-rouge">AndroidManifest</code> should be removed.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyConfigurationProvider.isGcmMessagingRegistrationEnabled()</code>, <code class="language-plaintext highlighter-rouge">AppboyConfigurationProvider.getGcmSenderId()</code>, <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setGcmSenderId()</code>, and <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setGcmMessagingRegistrationEnabled()</code>.</li>
</ul>

<h5 id="changed-51">Changed</h5>
<ul>
  <li>Changed custom event property values validation to allow for empty strings.</li>
</ul>

<h2 id="260">2.6.0</h2>

<h5 id="added-61">Added</h5>
<ul>
  <li>Introduced support for the Content Cards feature, which will eventually replace the existing News Feed feature and adds significant capability.</li>
</ul>

<h5 id="breaking-30">Breaking</h5>
<ul>
  <li>Updated the minimum SDK version from 14 (Ice Cream Sandwich) to 16 (Jelly Bean).</li>
</ul>

<h5 id="added-62">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyUser.setLocationCustomAttribute()</code> and <code class="language-plaintext highlighter-rouge">AppboyUser.unsetLocationCustomAttribute()</code>.</li>
</ul>

<h2 id="251">2.5.1</h2>

<h5 id="changed-52">Changed</h5>
<ul>
  <li>Changed the behavior of push stories to ensure that after the story initially appears in the notification tray, subsequent page traversal clicks don’t alert the user again.</li>
</ul>

<h5 id="added-63">Added</h5>
<ul>
  <li>The Braze SDK now automatically records when the user has disabled notifications at the app level.
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">appboy.xml</code> <code class="language-plaintext highlighter-rouge">com_appboy_notifications_enabled_tracking_on</code> boolean attribute and <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setNotificationsEnabledTrackingOn()</code> have been deprecated and are no longer used.</li>
      <li>This allows users to more effectively opt-out of push and leads to a more accurate push notification reachable audience.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-75">Fixed</h5>
<ul>
  <li>Fixed an issue where, when the lock screen was present, notification action button and push story body clicks would not open the application immediately. Added <code class="language-plaintext highlighter-rouge">AppboyNotificationRoutingActivity</code> for handling notification action button and push story body clicks.</li>
  <li>Fixed an issue where, for non fullscreen activities targeting API 27, requesting an orientation on activities would throw an exception.</li>
</ul>

<h2 id="250">2.5.0</h2>

<h5 id="breaking-31">Breaking</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">isControl()</code> to the <code class="language-plaintext highlighter-rouge">IInAppMessage</code> interface.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">logDisplayFailure()</code> to the <code class="language-plaintext highlighter-rouge">IInAppMessage</code> interface. In-app message display failures may affect campaign statistics so care should be taken when logging display failures.</li>
  <li>Added the <code class="language-plaintext highlighter-rouge">InAppMessageControl</code> class to represent control in-app messages. Control in-app messages should not be displayed to users and should only call <code class="language-plaintext highlighter-rouge">logImpression()</code> at render time.
    <ul>
      <li>Requesting in-app message display, even if the stack is non-empty, may potentially lead to no in-app message displaying if the in-app message is a control in-app message.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.setCustomControlInAppMessageManagerListener()</code> to modify the lifecycle behavior for control in-app messages.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">logInAppMessageClick</code>, <code class="language-plaintext highlighter-rouge">logInAppMessageButtonClick</code>, and <code class="language-plaintext highlighter-rouge">logInAppMessageImpression</code> from Appboy Unity player subclasses and <code class="language-plaintext highlighter-rouge">AppboyUnityActivityWrapper</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyConfigurationProvider.getIsUilImageCacheDisabled()</code> and <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setDisableUilImageCache()</code>.</li>
</ul>

<h5 id="fixed-76">Fixed</h5>
<ul>
  <li>Fixed the issue where in-app messages triggered on session start could potentially be templated with the old user’s attributes.</li>
  <li>Fixed a bug where calling <code class="language-plaintext highlighter-rouge">Appboy.wipeData()</code> or <code class="language-plaintext highlighter-rouge">Appboy.disableSdk()</code> could potentially lead to null instances being returned from <code class="language-plaintext highlighter-rouge">Appboy.getInstance()</code>.</li>
  <li>Fixed the issue where push deep links did not respect the back stack behavior when instructed to open inside the app’s WebView.</li>
  <li>Fixed a bug where the push received broadcast action contained the host package name twice.</li>
</ul>

<h2 id="240">2.4.0</h2>

<h5 id="fixed-77">Fixed</h5>
<ul>
  <li>Fixed a bug where calling <code class="language-plaintext highlighter-rouge">Appboy.wipeData()</code> would throw an uncaught exception when the Google Play location services library was not present.</li>
</ul>

<h5 id="added-64">Added</h5>
<ul>
  <li>Added the ability to listen for notification deleted intents from the <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code> via the action suffix <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.APPBOY_NOTIFICATION_DELETED_SUFFIX</code>.</li>
  <li>Added a notification creation timestamp to notifications built from the <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code>. This allows for calculating the duration of a notification. Intents will contain <code class="language-plaintext highlighter-rouge">Constants.APPBOY_PUSH_RECEIVED_TIMESTAMP_MILLIS</code> in the intent extras bundle.</li>
</ul>

<h5 id="changed-53">Changed</h5>
<ul>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.isUninstallTrackingPush()</code> to always return false. Uninstall tracking no longer requires sending a silent push notification to devices.</li>
</ul>

<h2 id="230">2.3.0</h2>

<h5 id="known-issues-with-version-230">Known Issues with version 2.3.0</h5>
<ul>
  <li>If the Google Play location services library is not present, calls to <code class="language-plaintext highlighter-rouge">Appboy.wipeData()</code> will throw an uncaught exception.</li>
</ul>

<h5 id="breaking-32">Breaking</h5>
<ul>
  <li>Removed the <code class="language-plaintext highlighter-rouge">appboyInAppMessageCustomFontFile</code> custom xml attribute. Custom font typefaces must now be located in the <code class="language-plaintext highlighter-rouge">res/font</code> directory.
    <ul>
      <li>To override a Braze style, both <code class="language-plaintext highlighter-rouge">android:fontFamily</code> and <code class="language-plaintext highlighter-rouge">fontFamily</code> style attributes must be set to maintain compatibility across all SDK versions. Example below:
```</li>
    </ul>
    <item name="android:fontFamily">@font/YOUR_CUSTOM_FONT_FAMILY</item>
    <item name="fontFamily">@font/YOUR_CUSTOM_FONT_FAMILY</item>
    <p>```</p>
    <ul>
      <li>See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html for more information.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyInAppMessageButtonView.java</code> and <code class="language-plaintext highlighter-rouge">AppboyInAppMessageTextView.java</code>.</li>
  <li>Removed the <code class="language-plaintext highlighter-rouge">AppboyGeofenceService</code>. Geofence integration no longer requires a manifest registration. Any reference to <code class="language-plaintext highlighter-rouge">AppboyGeofenceService</code> can safely be removed from your manifest.</li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">AppboyUnityPlayerNativeActivityWrapper</code> to <code class="language-plaintext highlighter-rouge">AppboyUnityActivityWrapper</code>.</li>
</ul>

<h5 id="fixed-78">Fixed</h5>
<ul>
  <li>Fixed a bug where sessions could be opened and closed with a null activity.</li>
</ul>

<h5 id="added-65">Added</h5>
<ul>
  <li>Added the ability to have the Braze SDK automatically register for Firebase Cloud Messaging.
    <ul>
      <li>Enabled via <code class="language-plaintext highlighter-rouge">com_appboy_firebase_cloud_messaging_registration_enabled</code> boolean attribute in XML or via <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setIsFirebaseCloudMessagingRegistrationEnabled()</code>.</li>
      <li>The Firebase Cloud Messaging Sender ID is set via <code class="language-plaintext highlighter-rouge">com_appboy_firebase_cloud_messaging_sender_id</code> string attribute in XML or via <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setFirebaseCloudMessagingSenderIdKey()</code>.</li>
      <li>The Firebase Cloud Messaging dependencies must still be compiled into your project. The Braze SDK does not compile any Firebase Cloud Messaging dependencies as part of this release.</li>
    </ul>
  </li>
  <li>Added UnityPlayerActivity support to AppboyUnityActivityWrapper. Previously only UnityPlayerNativeActivity was supported.</li>
  <li>Added a AppboyUnityPlayerActivity class for the UnityPlayerActivity for both prime31 and non-prime31 integrations.</li>
</ul>

<h2 id="225">2.2.5</h2>

<h5 id="added-66">Added</h5>
<ul>
  <li>Added support for wiping all customer data created by the Braze SDK via <code class="language-plaintext highlighter-rouge">Appboy.wipeData()</code>.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.disableSdk()</code> to disable the Braze SDK.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.enableSdk()</code> to re-enable the SDK after a call to <code class="language-plaintext highlighter-rouge">Appboy.disableSdk()</code>.</li>
</ul>

<h5 id="changed-54">Changed</h5>
<ul>
  <li>Changed <code class="language-plaintext highlighter-rouge">AppboyInAppMessageWebViewClientListener</code> to call <code class="language-plaintext highlighter-rouge">onDismissed()</code> when <code class="language-plaintext highlighter-rouge">onCloseAction()</code> gets called for HTML in-app messages.</li>
</ul>

<h5 id="fixed-79">Fixed</h5>
<ul>
  <li>Fixed an issue where internal thread pool executors could get blocked on a long running task and throw <code class="language-plaintext highlighter-rouge">RejectedExecutionException</code>.</li>
</ul>

<h2 id="224">2.2.4</h2>

<h5 id="added-67">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setIsSessionStartBasedTimeoutEnabled()</code> which optionally sets the session timeout behavior to be either session-start or session-end based. The default behavior is to be session-end based.
    <ul>
      <li>The use of this flag is recommended for long (30 minutes or longer) session timeout values.</li>
      <li>This value can also be configured via <code class="language-plaintext highlighter-rouge">appboy.xml</code> with the boolean <code class="language-plaintext highlighter-rouge">com_appboy_session_start_based_timeout_enabled</code> set to true.</li>
    </ul>
  </li>
</ul>

<h2 id="223">2.2.3</h2>

<h5 id="added-68">Added</h5>
<ul>
  <li>Added support for any custom image library to work with in-app messages and the news feed, including the <a href="https://bumptech.github.io/glide/">Glide Image Library</a>.
    <ul>
      <li>Please see <code class="language-plaintext highlighter-rouge">IAppboy#setAppboyImageLoader(IAppboyImageLoader)</code> for how to set a custom image library.</li>
    </ul>
  </li>
  <li>Added the <code class="language-plaintext highlighter-rouge">Glide Image Integration</code> sample app, showcasing how to use the Glide Library.</li>
</ul>

<h4 id="changed-55">Changed</h4>
<ul>
  <li>Updated the proguard rules for Fresco and Notification Enabled Tracking.</li>
</ul>

<h2 id="222">2.2.2</h2>

<h5 id="added-69">Added</h5>
<ul>
  <li>The Braze SDK may now optionally record when the user has disabled notifications at the app level.
    <ul>
      <li>Enabled via <code class="language-plaintext highlighter-rouge">appboy.xml</code> using the <code class="language-plaintext highlighter-rouge">com_appboy_notifications_enabled_tracking_on</code> boolean attribute or via <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setNotificationsEnabledTrackingOn()</code>.</li>
      <li>If using proguard in your app and Braze SDK v2.2.2 or below, please add <code class="language-plaintext highlighter-rouge">-keep class android.support.v4.app.NotificationManagerCompat { *; }</code> to your proguard rules.</li>
      <li>(Update) Note that starting with Braze Android SDK Version <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#251"><code class="language-plaintext highlighter-rouge">2.5.1</code></a>, this feature is now automatically enabled.</li>
    </ul>
  </li>
</ul>

<h2 id="221">2.2.1</h2>

<h5 id="added-70">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">Other</code>, <code class="language-plaintext highlighter-rouge">Unknown</code>, <code class="language-plaintext highlighter-rouge">Not Applicable</code>, and <code class="language-plaintext highlighter-rouge">Prefer not to Say</code> options for user gender.</li>
</ul>

<h2 id="220">2.2.0</h2>

<h5 id="breaking-33">Breaking</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">Appboy.requestInAppMessageRefresh()</code> and removed support for Original in-app messages. Note that all customers on version 2.2.0 and newer should use triggered in-app messages.</li>
  <li>Changed the signature of most methods on the <code class="language-plaintext highlighter-rouge">IAppboy</code> interface. Methods that logged values now return void instead of boolean.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.openSession()</code> now returns void.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.closeSession</code> now returns void.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.changeUser()</code> now returns void. To get the current user, please call <code class="language-plaintext highlighter-rouge">IAppboy.getCurrentUser()</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.logCustomEvent()</code> and all method overloads now return void.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.logPurchase()</code> and all method overloads now return void.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.submitFeedback()</code> now returns void.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.logPushNotificationOpened()</code> now returns void.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.logPushNotificationActionClicked()</code> now returns void.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.logFeedDisplayed()</code> now returns void.</li>
      <li><code class="language-plaintext highlighter-rouge">IAppboy.logFeedbackDisplayed()</code> now returns void.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyFeedbackFragment.FeedbackResult.ERROR</code>.</li>
  <li>Changed <code class="language-plaintext highlighter-rouge">AppboyFeedbackFragment.FeedbackFinishedListener</code> to <code class="language-plaintext highlighter-rouge">AppboyFeedbackFragment.IFeedbackFinishedListener</code>.</li>
  <li>Changed <code class="language-plaintext highlighter-rouge">AppboyFeedbackFragment.FeedbackResult.SENT</code> to <code class="language-plaintext highlighter-rouge">AppboyFeedbackFragment.FeedbackResult.SUBMITTED</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">Appboy.fetchAndRenderImage()</code>. Please use <code class="language-plaintext highlighter-rouge">getAppboyImageLoader().renderUrlIntoView()</code> instead.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyFileUtils.getExternalStorage()</code>.</li>
</ul>

<h5 id="added-71">Added</h5>
<ul>
  <li>Added Push Stories, a new push type that uses <code class="language-plaintext highlighter-rouge">DecoratedCustomViewStyle</code> to display multiple images in a single notification. We recommend posting push stories to a notification channel with vibration disabled to avoid repeated vibrations as the user navigates through the story.</li>
</ul>

<h5 id="changed-56">Changed</h5>
<ul>
  <li>The Braze singleton now internally performs most actions on a background thread, giving a very substantial performance boost to all actions on the <code class="language-plaintext highlighter-rouge">Appboy</code> singleton.</li>
</ul>

<h4 id="fixed-80">Fixed</h4>
<ul>
  <li>Reduced the number of connections made when the Braze SDK downloads files and images. Note that the amount of data downloaded has not changed.</li>
</ul>

<h2 id="214">2.1.4</h2>

<h5 id="added-72">Added</h5>
<ul>
  <li>Added a check on Braze initialization for the “Calypso AppCrawler” indexing bot that disables all Braze network requests when found. This prevents erroneous Braze data from being sent for Firebase app indexing crawlers.</li>
  <li>Added the ability to disable adding an activity to the back stack when automatically following push deep links. Previously, the app’s main activity would automatically be added to the back stack.
    <ul>
      <li>Enabled via <code class="language-plaintext highlighter-rouge">appboy.xml</code> using the <code class="language-plaintext highlighter-rouge">com_appboy_push_deep_link_back_stack_activity_enabled</code> boolean attribute or via <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setPushDeepLinkBackStackActivityEnabled()</code>.</li>
    </ul>
  </li>
  <li>Added the ability to specify a custom activity to open on the back stack when automatically following push deep links. Previously, only the app’s main activity could be used.
    <ul>
      <li>The custom activity is set via <code class="language-plaintext highlighter-rouge">appboy.xml</code> using the <code class="language-plaintext highlighter-rouge">com_appboy_push_deep_link_back_stack_activity_class_name</code> string attribute or via <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setPushDeepLinkBackStackActivityClass()</code>. Note that the class name used in the <code class="language-plaintext highlighter-rouge">appboy.xml</code> must be the exact class name string as returned from <code class="language-plaintext highlighter-rouge">YourClass.class.getName()</code>.</li>
    </ul>
  </li>
  <li>Added the <code class="language-plaintext highlighter-rouge">setLanguage()</code> method to <code class="language-plaintext highlighter-rouge">AppboyUser</code> to allow explicit control over the language you use in the Braze dashboard to localize your messaging content.</li>
</ul>

<h5 id="changed-57">Changed</h5>
<ul>
  <li>Added support for acquiring wake locks on Android O using the notification channel importance instead of the individual notification’s priority.</li>
</ul>

<h2 id="213">2.1.3</h2>

<h5 id="fixed-81">Fixed</h5>
<ul>
  <li>Fixed a bug where implicit intents for custom push broadcast receivers would be suppressed in devices running Android O.</li>
  <li>Updated the Braze ProGuard configuration to ensure Google Play Services classes required by Geofencing aren’t renamed.</li>
</ul>

<h2 id="212">2.1.2</h2>

<h5 id="fixed-82">Fixed</h5>
<ul>
  <li>Fixed a bug where sealed session flushes would not be sent on apps with long session timeouts due to Android O background service limitations.</li>
</ul>

<h2 id="211">2.1.1</h2>

<h5 id="added-73">Added</h5>
<ul>
  <li>Added the ability to set a custom API endpoint via <code class="language-plaintext highlighter-rouge">appboy.xml</code> using the <code class="language-plaintext highlighter-rouge">com_appboy_custom_endpoint</code> string attribute or via <code class="language-plaintext highlighter-rouge">AppboyConfig.Builder.setCustomEndpoint()</code>.</li>
</ul>

<h5 id="fixed-83">Fixed</h5>
<ul>
  <li>Fixed a bug where date custom attributes were formatted in the device’s locale, which could result in incorrectly formatted dates. Date custom attributes are now always formatted in <code class="language-plaintext highlighter-rouge">Locale.US</code>.</li>
</ul>

<h2 id="210">2.1.0</h2>

<h5 id="breaking-34">Breaking</h5>
<ul>
  <li>Updated the minimum SDK version from 9 (Gingerbread) to 14 (Ice Cream Sandwich).
    <ul>
      <li>We recommend that session tracking and in-app messages registration be done via an <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener</code> instance using <a href="https://developer.android.com/reference/android/app/Application.html#registerActivityLifecycleCallbacks(android.app.Application.ActivityLifecycleCallbacks)"><code class="language-plaintext highlighter-rouge">Application.registerActivityLifecycleCallbacks()</code></a>.</li>
    </ul>
  </li>
  <li>Removed the deprecated field: <code class="language-plaintext highlighter-rouge">AppboyLogger.LogLevel</code>. Please use <code class="language-plaintext highlighter-rouge">AppboyLogger.setLogLevel()</code> and <code class="language-plaintext highlighter-rouge">AppboyLogger.getLogLevel()</code> instead.</li>
  <li>Updated the v4 support library dependency to version 26.0.0. To download Android Support Libraries versions 26.0.0 and above, you must add the following line to your top-level <code class="language-plaintext highlighter-rouge">build.gradle</code> repositories block:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>maven {
  url "https://maven.google.com"
}
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
</ul>

<h5 id="added-74">Added</h5>
<ul>
  <li>Added support for Android O notification channels. In the case that a Braze notification does not contain the id for a notification channel, Braze will fallback to a default notification channel. Other than the default notification channel, Braze will not create any channels. All other channels must be programatically defined by the host app.
    <ul>
      <li>Note that default notification channel creation will occur even if your app does not target Android O. If you would like to avoid default channel creation until your app targets Android O, do not upgrade to this version.</li>
      <li>To set the user facing name of the default Braze notification channel, please use <code class="language-plaintext highlighter-rouge">AppboyConfig.setDefaultNotificationChannelName()</code>.</li>
      <li>To set the user facing description of the default Braze notification channel, please use <code class="language-plaintext highlighter-rouge">AppboyConfig.setDefaultNotificationChannelDescription()</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-58">Changed</h5>
<ul>
  <li>Updated the target SDK version to 26.</li>
</ul>

<h2 id="205">2.0.5</h2>

<h5 id="fixed-84">Fixed</h5>
<ul>
  <li>Fixed a bug where relative links in <code class="language-plaintext highlighter-rouge">href</code> tags in HTML in-app messages would get passed as file Uris to the <code class="language-plaintext highlighter-rouge">AppboyNavigator</code>.</li>
</ul>

<h5 id="added-75">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">Double</code> as a valid value type on <code class="language-plaintext highlighter-rouge">AppboyUser.setCustomUserAttribute()</code>.</li>
  <li>Added user aliasing capability. Aliases can be used in the API and dashboard to identify users in addition to their ID.  See the <code class="language-plaintext highlighter-rouge">addAlias</code> method on <a href="https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/AppboyUser.html"><code class="language-plaintext highlighter-rouge">AppboyUser</code></a> for more information.</li>
</ul>

<h2 id="204">2.0.4</h2>

<h5 id="changed-59">Changed</h5>
<ul>
  <li>Made further improvements to Braze singleton initialization performance.</li>
</ul>

<h2 id="203">2.0.3</h2>

<h5 id="changed-60">Changed</h5>
<ul>
  <li>Enabled TLS 1.2 for Braze HTTPS connections running on API 16+ devices. Previously, for devices running on API 16-20, only TLS 1.0 was enabled by default.</li>
  <li>Improved Braze singleton initialization performance.</li>
</ul>

<h2 id="202">2.0.2</h2>

<h5 id="fixed-85">Fixed</h5>
<ul>
  <li>Fixed a bug where identifying a user while a request was in flight could cause newly written attributes on the old user to be orphaned in local storage.</li>
</ul>

<h2 id="201">2.0.1</h2>

<h5 id="added-76">Added</h5>
<ul>
  <li>Added support for displaying Youtube videos inside of HTML in-app messages and the Braze Webview. For HTML in-app messages, this requires hardware acceleration to be enabled in the Activity where the in-app message is being displayed, please see https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling. Please note that hardware acceleration is only available on API versions 11 and above.</li>
  <li>Added the ability to access Braze’s default notification builder instance from custom <code class="language-plaintext highlighter-rouge">IAppboyNotificationFactory</code> instances. This simplifies making small changes to Appboy’s default notification handling.</li>
  <li>Improved <code class="language-plaintext highlighter-rouge">AppboyImageUtils.getBitmap()</code> by adding the ability to sample images using preset view bounds.</li>
</ul>

<h2 id="200">2.0.0</h2>

<h5 id="breaking-35">Breaking</h5>
<ul>
  <li>Removed the following deprecated methods and fields:
    <ul>
      <li>Removed the unsupported method <code class="language-plaintext highlighter-rouge">Appboy.logShare()</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">Appboy.logPurchase(String, int)</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">Appboy.logFeedCardImpression()</code> and <code class="language-plaintext highlighter-rouge">Appboy.logFeedCardClick()</code>. Please use <code class="language-plaintext highlighter-rouge">Card.logClick()</code> and <code class="language-plaintext highlighter-rouge">Card.logImpression()</code> instead.</li>
      <li>Removed the unsupported method <code class="language-plaintext highlighter-rouge">Appboy.getAppboyResourceEndpoint()</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">IAppboyEndpointProvider.getResourceEndpoint()</code>. Please update your interface implementation if applicable.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">Appboy.registerAppboyGcmMessages()</code>. Please use <code class="language-plaintext highlighter-rouge">Appboy.registerAppboyPushMessages()</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">AppboyInAppMessageBaseView.resetMessageMargins()</code>. Please use <code class="language-plaintext highlighter-rouge">AppboyInAppMessageBaseView.resetMessageMargins(boolean)</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.unity.AppboyUnityGcmReceiver</code>. To open Braze push deep links automatically in Unity, set the boolean configuration parameter <code class="language-plaintext highlighter-rouge">com_appboy_inapp_show_inapp_messages_automatically</code> to true in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
      <li>Removed the unsupported method <code class="language-plaintext highlighter-rouge">AppboyUser.setBio()</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">AppboyUser.setIsSubscribedToEmails()</code>. Please use <code class="language-plaintext highlighter-rouge">AppboyUser.setEmailNotificationSubscriptionType()</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">Constants.APPBOY_PUSH_CUSTOM_URI_KEY</code>. Please use <code class="language-plaintext highlighter-rouge">Constants.APPBOY_PUSH_DEEP_LINK_KEY</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">Constants.APPBOY_CANCEL_NOTIFICATION_TAG</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.ui.actions.ViewAction</code> and <code class="language-plaintext highlighter-rouge">com.appboy.ui.actions.WebAction</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">CardCategory.ALL_CATEGORIES</code>. Please use <code class="language-plaintext highlighter-rouge">CardCategory.getAllCategories()</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">AppboyImageUtils.storePushBitmapInExternalStorage()</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">AppboyFileUtils.canStoreAssetsLocally()</code> and <code class="language-plaintext highlighter-rouge">AppboyFileUtils.getApplicationCacheDir()</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">InAppMessageModal.getModalFrameColor()</code> and <code class="language-plaintext highlighter-rouge">InAppMessageModal.setModalFrameColor()</code>. Please use <code class="language-plaintext highlighter-rouge">InAppMessageModal.getFrameColor()</code> and <code class="language-plaintext highlighter-rouge">InAppMessageModal.setFrameColor()</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">com.appboy.enums.SocialNetwork</code>.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.getAppboyExtras()</code>. Please use <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.getAppboyExtrasWithoutPreprocessing()</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.setLargeIconIfPresentAndSupported(Context, AppboyConfigurationProvider, NotificationCompat.Builder)</code>. Please use <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.setLargeIconIfPresentAndSupported(Context, AppboyConfigurationProvider, NotificationCompat.Builder, Bundle)</code> instead.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.hideCurrentInAppMessage()</code>. Please use <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.hideCurrentlyDisplayingInAppMessage()</code> instead.</li>
    </ul>
  </li>
  <li>Changed method signatures for <code class="language-plaintext highlighter-rouge">gotoNewsFeed()</code> and <code class="language-plaintext highlighter-rouge">gotoURI()</code> in <code class="language-plaintext highlighter-rouge">IAppboyNavigator</code>. Please update your interface implementation if applicable.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">Appboy.unregisterAppboyPushMessages()</code>. Please use <code class="language-plaintext highlighter-rouge">AppboyUser.setPushNotificationSubscriptionType()</code> instead.</li>
  <li>Moved <code class="language-plaintext highlighter-rouge">getAppboyNavigator()</code> and <code class="language-plaintext highlighter-rouge">setAppboyNavigator()</code> from <code class="language-plaintext highlighter-rouge">Appboy.java</code> to <code class="language-plaintext highlighter-rouge">AppboyNavigator.java</code>.</li>
  <li>The Braze Baidu China Push integration now uses the Baidu <code class="language-plaintext highlighter-rouge">channelId</code> as the push token. Please update your push token registration code to pass <code class="language-plaintext highlighter-rouge">channelId</code> instead of <code class="language-plaintext highlighter-rouge">userId</code> into <code class="language-plaintext highlighter-rouge">Appboy.registerAppboyPushMessages()</code>. The China Push sample has been updated.</li>
  <li>Removed the <code class="language-plaintext highlighter-rouge">wearboy</code> and <code class="language-plaintext highlighter-rouge">wear-library</code> modules. Android Wear 1.0 is no longer supported. Please remove <code class="language-plaintext highlighter-rouge">AppboyWearableListenerService</code> from your <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code> if applicable.</li>
</ul>

<h5 id="added-77">Added</h5>
<ul>
  <li>Added a javascript interface to HTML in-app messages	with ability to	log custom events, purchases, user attributes, navigate users, and close the messaage.</li>
  <li>Added the ability to set a single delegate object to custom handle all Uris opened by Braze across in-app messages, push, and the news feed. Your delegate object should implement the <code class="language-plaintext highlighter-rouge">IAppboyNavigator</code> interface and be set using <code class="language-plaintext highlighter-rouge">AppboyNavigator.setAppboyNavigator()</code>.
    <ul>
      <li>See https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/CustomAppboyNavigator.java for an example implementation.</li>
      <li>You must also provide instructions for Braze to navigate to your app’s (optional) news feed implementation. To use Braze’s default handling, call <code class="language-plaintext highlighter-rouge">AppboyNavigator.executeNewsFeedAction(context, uriAction);</code>.</li>
      <li>Note: Previously, <code class="language-plaintext highlighter-rouge">AppboyNavigator</code> was only used when opening in-app messages.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-61">Changed</h5>
<ul>
  <li>Removed the need to manually add declarations for Braze’s news feed and in-app message activities (<code class="language-plaintext highlighter-rouge">AppboyFeedActivity</code> and <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code>) to the app <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code>. If you have these declarations in your manifest, they can be safely removed.</li>
  <li>Push notifications with web url click actions now open in an in-app webview instead of the external mobile web browser when clicked.</li>
</ul>

<h2 id="1190">1.19.0</h2>

<h5 id="added-78">Added</h5>
<ul>
  <li>Added support for registering geofences with Google Play Services and messaging on geofence events. Please reach out to success@braze.com for more information about this feature.</li>
</ul>

<h5 id="removed-6">Removed</h5>
<ul>
  <li>Support for share type notification action buttons and custom notification action buttons was removed.</li>
</ul>

<h5 id="changed-62">Changed</h5>
<ul>
  <li>Push deep links that can be handled by the current app are automatically opened using the current app. Previously, if another app could handle the deep link as well, a chooser dialog would open.
    <ul>
      <li>Thanks to <a href="https://github.com/catacom">catacom</a></li>
      <li>See https://github.com/braze-inc/braze-android-sdk/pull/71</li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">AppboyImageUtils.storePushBitmapInExternalStorage()</code> has been deprecated.</li>
</ul>

<h2 id="1180">1.18.0</h2>

<h5 id="breaking-36">Breaking</h5>
<ul>
  <li>Renamed the <code class="language-plaintext highlighter-rouge">android-sdk-jar</code> artifact in the <code class="language-plaintext highlighter-rouge">gh-pages</code> branch to <code class="language-plaintext highlighter-rouge">android-sdk-base</code> and changed its format from <code class="language-plaintext highlighter-rouge">jar</code> to <code class="language-plaintext highlighter-rouge">aar</code>. Most integrations depend on <code class="language-plaintext highlighter-rouge">android-sdk-ui</code> and won’t need to take any action.
    <ul>
      <li>Note: If you were compiling <code class="language-plaintext highlighter-rouge">android-sdk-jar</code> in your <code class="language-plaintext highlighter-rouge">build.gradle</code>, you must now compile <code class="language-plaintext highlighter-rouge">android-sdk-base</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-79">Added</h5>
<ul>
  <li>Added the ability to set custom read and unread icons for News Feed cards. To do so, override the <code class="language-plaintext highlighter-rouge">Appboy.Cards.ImageSwitcher</code> style in your <code class="language-plaintext highlighter-rouge">styles.xml</code> and add <code class="language-plaintext highlighter-rouge">appboyFeedCustomReadIcon</code> and <code class="language-plaintext highlighter-rouge">appboyFeedCustomUnReadIcon</code> drawable attributes.</li>
  <li>Added a sample app showcasing the FCM + Braze push integration. See <code class="language-plaintext highlighter-rouge">/samples/firebase-push</code>.</li>
  <li>Added a sample app for manual session integration. See <code class="language-plaintext highlighter-rouge">/samples/manual-session-integration</code>.</li>
</ul>

<h5 id="removed-7">Removed</h5>
<ul>
  <li>Removed the <code class="language-plaintext highlighter-rouge">-dontoptimize</code> flag from Braze’s UI consumer proguard rules. See https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/appboy-proguard-rules.pro for the latest Proguard config.
    <ul>
      <li>Thanks to <a href="https://github.com/mnonnenmacher">mnonnenmacher</a></li>
      <li>See https://github.com/braze-inc/braze-android-sdk/pull/69</li>
    </ul>
  </li>
</ul>

<h5 id="changed-63">Changed</h5>
<ul>
  <li>Updated the Droidboy project to use the conventional Android Build System folder structure.</li>
</ul>

<h2 id="1170">1.17.0</h2>

<h5 id="breaking-37">Breaking</h5>
<ul>
  <li>Added the ability to configure Braze completely at runtime using <code class="language-plaintext highlighter-rouge">Appboy.configure()</code>. Values set at runtime take precedence over their counterparts in <code class="language-plaintext highlighter-rouge">appboy.xml</code>. A complete example of Braze runtime configuration is available in our Hello Appboy sample app’s <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/hello-appboy/src/main/java/com/appboy/helloworld/HelloAppboyApplication.java">application class</a>.
    <ul>
      <li>Renamed <code class="language-plaintext highlighter-rouge">com.appboy.configuration.XmlAppConfigurationProvider</code> to <code class="language-plaintext highlighter-rouge">com.appboy.configuration.AppboyConfigurationProvider</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">Appboy.configure(String)</code> changed to <code class="language-plaintext highlighter-rouge">Appboy.configure(Context, AppboyConfig)</code>.  To maintain parity, replace your current usage with the following equivalent snippit:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>AppboyConfig appboyConfig = new AppboyConfig.Builder()
      .setApiKey("your-api-key")
      .build();
Appboy.configure(this, appboyConfig);
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
</ul>

<h5 id="fixed-86">Fixed</h5>
<ul>
  <li>Fixed an issue where in-app messages triggered off of push clicks wouldn’t fire because the push click happened before the in-app message configuration was synced to the device.</li>
</ul>

<h5 id="changed-64">Changed</h5>
<ul>
  <li>Updated <code class="language-plaintext highlighter-rouge">Appboy.registerAppboyPushMessages()</code> to flush the subscription to the server immediately.</li>
  <li>Improved the accessibility-mode behavior of in-app messages.</li>
</ul>

<h2 id="1160">1.16.0</h2>

<h5 id="added-80">Added</h5>
<ul>
  <li>Added the ability to toggle outbound network requests from the Braze SDK online/offline. See <code class="language-plaintext highlighter-rouge">Appboy.setOutboundNetworkRequestsOffline()</code> for more details.</li>
</ul>

<h5 id="fixed-87">Fixed</h5>
<ul>
  <li>Fixed a bug that caused session sealed automatic data flushes to not occur.</li>
</ul>

<h5 id="removed-8">Removed</h5>
<ul>
  <li>Removed Braze notification action button icons and icon constants.</li>
</ul>

<h2 id="1153">1.15.3</h2>

<h5 id="fixed-88">Fixed</h5>
<ul>
  <li>Fixed a bug where in-app messages triggered while no activity was registered with <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager</code> would be dropped.</li>
</ul>

<h2 id="1152">1.15.2</h2>

<h5 id="fixed-89">Fixed</h5>
<ul>
  <li>Fixed a bug where in-app messages triggered while no activity was registered with <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager</code> would be displayed without assets.</li>
</ul>

<h2 id="1151">1.15.1</h2>

<h5 id="added-81">Added</h5>
<ul>
  <li>Added Hebrew localization strings.</li>
</ul>

<h5 id="changed-65">Changed</h5>
<ul>
  <li>Improved the initialization time of the Braze SDK.</li>
</ul>

<h5 id="removed-9">Removed</h5>
<ul>
  <li>Removed fetching of the device hardware serial number as part of device metadata collection.</li>
</ul>

<h2 id="1150">1.15.0</h2>

<h5 id="breaking-38">Breaking</h5>
<ul>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.hideCurrentInAppMessage()</code>. Please use <code class="language-plaintext highlighter-rouge">AppboyInAppMessageManager.hideCurrentlyDisplayingInAppMessage()</code> instead.</li>
</ul>

<h5 id="added-82">Added</h5>
<ul>
  <li>Added the option to handle session tracking and <code class="language-plaintext highlighter-rouge">InAppMessageManager</code> registration automatically on apps with a minimum supported SDK of API level 14 or above. This is done by registering an <code class="language-plaintext highlighter-rouge">AppboyLifecycleCallbackListener</code> instance using <a href="https://developer.android.com/reference/android/app/Application.html#registerActivityLifecycleCallbacks(android.app.Application.ActivityLifecycleCallbacks)"><code class="language-plaintext highlighter-rouge">Application.registerActivityLifecycleCallbacks()</code></a>. See the Hello Appboy sample app’s <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/hello-appboy/src/main/java/com/appboy/helloworld/HelloAppboyApplication.java">application class</a> for an example.</li>
  <li>Added support for upgraded in-app messages including image-only messages, improved image sizing/cropping, text scrolling, text alignment, configurable orientation, and configurable frame color.</li>
  <li>Added support for in-app messages triggered on custom event properties, purchase properties, and in-app message clicks.</li>
  <li>Added support for templating event properties within in-app messages.</li>
  <li>Added the ability to optionally open deep links and the main activity of the app automatically when a user clicks a push notification, eliminating the need to write a custom <code class="language-plaintext highlighter-rouge">BroadcastReceiver</code> for Braze push. To activate, set the boolean property <code class="language-plaintext highlighter-rouge">com_appboy_handle_push_deep_links_automatically</code> to <code class="language-plaintext highlighter-rouge">true</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>. Note that even when automatic deep link opening is enabled, Braze push opened and received intents will still be sent. To avoid double opening, remove your custom <code class="language-plaintext highlighter-rouge">BroadcastReceiver</code> or modify it to not open deep links.</li>
</ul>

<h2 id="1141">1.14.1</h2>

<h5 id="fixed-90">Fixed</h5>
<ul>
  <li>Fixed a bug where images in short news and cross promotion News Feed cards would appear too small on high resolution devices. This bug did not affect Fresco users.</li>
</ul>

<h5 id="changed-66">Changed</h5>
<ul>
  <li>Updated Baidu push service jar from v4.6.2.38 to v5.1.0.48.</li>
</ul>

<h2 id="1140">1.14.0</h2>

<h5 id="breaking-39">Breaking</h5>
<ul>
  <li>Renamed <code class="language-plaintext highlighter-rouge">disableAllAppboyNetworkRequests()</code> to <code class="language-plaintext highlighter-rouge">enableMockAppboyNetworkRequestsAndDropEventsMode()</code> and fixes a bug where calling <code class="language-plaintext highlighter-rouge">Appboy.changeUser()</code> would cause a network request even in disabled/mocked mode. Note that <code class="language-plaintext highlighter-rouge">enableMockAppboyNetworkRequestsAndDropEventsMode</code> should only be used in testing environments.</li>
</ul>

<h5 id="added-83">Added</h5>
<ul>
  <li>Added the ability to log negatively-priced purchases.</li>
  <li>Added the option to sort News Feed cards based on read/unread status.</li>
  <li>Added a custom News Feed click delegate. To handle News Feed clicks manually, implement <code class="language-plaintext highlighter-rouge">IFeedClickActionListener</code> and register an instance using <code class="language-plaintext highlighter-rouge">AppboyFeedManager.getInstance().setFeedCardClickActionListener()</code>.  This enables use-cases such as selectively using the native browser to open web links.</li>
</ul>

<h5 id="changed-67">Changed</h5>
<ul>
  <li>Added the ability to include file separators in User Ids.</li>
  <li>Changes Braze’s default Log Level from VERBOSE to INFO. Previously disabled debug log statements are enabled and available for debugging. To change Braze’s Log Level, update the value of <code class="language-plaintext highlighter-rouge">AppboyLogger.LogLevel</code>, e.g. <code class="language-plaintext highlighter-rouge">AppboyLogger.LogLevel = Log.VERBOSE</code>.</li>
</ul>

<h5 id="removed-10">Removed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">keep</code> rules from <code class="language-plaintext highlighter-rouge">consumerProguardFiles</code> automatic Proguard configuration for potentially improved optimization for client apps. Note that client apps that Proguard Braze code must now store release mapping files for Braze to interpret stack traces. If you would like to continue to <code class="language-plaintext highlighter-rouge">keep</code> all Braze code, add <code class="language-plaintext highlighter-rouge">-keep class bo.app.** { *; }</code> and <code class="language-plaintext highlighter-rouge">-keep class com.appboy.** { *; }</code> to your Proguard configuration.
    <ul>
      <li>See https://github.com/braze-inc/braze-android-sdk/issues/54</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">onRetainInstance()</code> from the Braze News Feed fragment. As a result, the News Feed may be used in nested fragments.</li>
</ul>

<h2 id="1135">1.13.5</h2>

<h5 id="added-84">Added</h5>
<ul>
  <li>Defined <code class="language-plaintext highlighter-rouge">com_appboy_card_background</code> to provide simpler control of news feed card background color.</li>
  <li>Added a convenience method to <code class="language-plaintext highlighter-rouge">Month</code> to allow direct instantiation from a month integer.</li>
</ul>

<h5 id="fixed-91">Fixed</h5>
<ul>
  <li>Fixed a database access race condition in changeUser code.
    <ul>
      <li>See https://github.com/braze-inc/braze-android-sdk/issues/52 and https://github.com/braze-inc/braze-android-sdk/issues/39</li>
    </ul>
  </li>
</ul>

<h5 id="removed-11">Removed</h5>
<ul>
  <li>Removed optimizations from the private library’s Proguard configuration to allow dexing Braze with Jack and Android Gradle Plugin 2.2.0+.</li>
</ul>

<h2 id="1134">1.13.4</h2>

<h5 id="added-85">Added</h5>
<ul>
  <li>Added ability to set push and email subscription state from Droidboy.</li>
</ul>

<h5 id="changed-68">Changed</h5>
<ul>
  <li>Open sourced Braze’s Unity plugin library code.</li>
</ul>

<h2 id="1133">1.13.3</h2>

<h5 id="added-86">Added</h5>
<ul>
  <li>Added the ability to set the large notification icon from within the GCM payload.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">consumerProguardFiles</code> automatic Proguard configuration.</li>
</ul>

<h5 id="fixed-92">Fixed</h5>
<ul>
  <li>Fixed a bug where triggered HTML in-app messages would not always send button analytics.</li>
</ul>

<h5 id="changed-69">Changed</h5>
<ul>
  <li>Updated Baidu push service jar from v4.3.0.4 to v4.6.2.38.</li>
  <li>Updated to log analytics for in-app messages and in-app message buttons with ‘NONE’ click actions.</li>
  <li>Updated the Droidboy sample app to use material design.</li>
  <li>Updated the Hello Appboy sample app to use Proguard.</li>
</ul>

<h2 id="1132">1.13.2</h2>

<h5 id="fixed-93">Fixed</h5>
<ul>
  <li>Fixed bug where passing a <code class="language-plaintext highlighter-rouge">JSONObject</code> with multiple invalid keys or values to the <code class="language-plaintext highlighter-rouge">AppboyProperties</code> constructor would cause a <code class="language-plaintext highlighter-rouge">ConcurrentModificationException</code>.</li>
</ul>

<h2 id="1131">1.13.1</h2>

<h5 id="fixed-94">Fixed</h5>
<ul>
  <li>Added handling to a case where certain devices were returning null Resources for GCM BroadcastReceiver onReceive contexts.</li>
</ul>

<h2 id="1130">1.13.0</h2>

<h5 id="added-87">Added</h5>
<ul>
  <li>Added support for action-based, locally triggered in-app messages. In-app messages are now sent to the device at session start with associated trigger events. The SDK will display in-app messages in near real-time when the trigger event associated with a message occurs. Trigger events can be app opens, push opens, purchases, and custom events.</li>
</ul>

<h5 id="changed-70">Changed</h5>
<ul>
  <li>Deprecated the old system of requesting in-app message display, now collectively known as ‘original’ in-app messaging, where messages were limited to displaying at app start.</li>
</ul>

<h5 id="removed-12">Removed</h5>
<ul>
  <li>Removed Iab billing example code from Droidboy.</li>
</ul>

<h2 id="1120">1.12.0</h2>

<h5 id="breaking-40">Breaking</h5>
<ul>
  <li>Removed the deprecated method <code class="language-plaintext highlighter-rouge">Appboy.requestSlideupRefresh()</code>.  Please use <code class="language-plaintext highlighter-rouge">Appboy.requestInAppMessageRefresh()</code> instead.</li>
  <li>Removed the deprecated class AppboySlideupManager.  Please use AppboyInAppMessageManager instead.</li>
</ul>

<h5 id="changed-71">Changed</h5>
<ul>
  <li>HTML in-app message WebViews now use wide viewport mode and load pages in overview mode.</li>
  <li>Moved <code class="language-plaintext highlighter-rouge">AppboyImageUtils</code> to the private library with an updated api.</li>
  <li>Moved <code class="language-plaintext highlighter-rouge">WebContentUtils</code> to the private library.</li>
  <li>Renamed <code class="language-plaintext highlighter-rouge">IInAppMessageHtmlBase</code> to <code class="language-plaintext highlighter-rouge">InAppMessageHtmlBase</code>.</li>
  <li>Method count of the private Braze library has decreased by over 600 since version 1.11.0.</li>
</ul>

<h5 id="removed-13">Removed</h5>
<ul>
  <li>Removed the partial duplicate of the private library’s StringUtils from the ui project.</li>
</ul>

<h2 id="1112">1.11.2</h2>

<h5 id="fixed-95">Fixed</h5>
<ul>
  <li>Fixed bug where large and small icons both rendered at full size in notification remoteviews for Honeycomb/ICS.  Now, if a large icon is available, only the large icon is shown.  Otherwise, the small icon is used.</li>
  <li>Fixed bug where push open logs were under-reported under certain device conditions.</li>
</ul>

<h2 id="1111">1.11.1</h2>
<ul>
  <li>Placeholder for Unity release.</li>
</ul>

<h2 id="1110">1.11.0</h2>

<h5 id="added-88">Added</h5>
<ul>
  <li>Creates Activity based Unity in-app messages (fixing an issue where touches on in-app messages were hitting the game behind the in-app message) and removes redundant Unity permissions.</li>
  <li>Added a method for setting modal frame color on in-app messages, no longer displays in-app messages on asset download failure and adds robustness.</li>
  <li>Added deep link support to <code class="language-plaintext highlighter-rouge">AppboyUnityGcmReceiver</code>.</li>
</ul>

<h5 id="changed-72">Changed</h5>
<ul>
  <li>Makes the WebView background for HTML in-app messages transparent.  Ensure your HTML in-app messages expect a transparent background.</li>
  <li>Updated Google Play Services from to 7.5.0 to 8.3.0 and Play Services Support from 1.2.0 to 1.3.0.
    <ul>
      <li>See https://github.com/braze-inc/braze-android-sdk/issues/45</li>
    </ul>
  </li>
  <li>Updated Braze WebView to support redirects to deep links and enables DOM storage.</li>
</ul>

<h2 id="1103">1.10.3</h2>

<h5 id="added-89">Added</h5>
<ul>
  <li>Added Android M Support.  Under the runtime permissions model introduced in Android M, location permission must be explicitly obtained from the end user by the integrating app.  Once location permission is granted, Braze will resume location data collection on the subsequent session.</li>
</ul>

<h2 id="1102">1.10.2</h2>

<h5 id="added-90">Added</h5>
<ul>
  <li>Added the ability to log a custom event from an HTML in-app message. To log a custom event from an HTML in-app message, navigate a user to a url of the form <code class="language-plaintext highlighter-rouge">appboy://customEvent?name=customEventName&amp;p1=v2</code>, where the <code class="language-plaintext highlighter-rouge">name</code> URL parameter is the name of the event, and the remaining parameters are logged as String properties on the event.</li>
</ul>

<h2 id="1101">1.10.1</h2>

<h5 id="changed-73">Changed</h5>
<ul>
  <li>Enabled javascript in HTML in-app messages.</li>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">logShare()</code> and <code class="language-plaintext highlighter-rouge">setBio()</code> in the public interface as support in the Braze dashboard has been removed.</li>
</ul>

<h2 id="1100-1">1.10.0</h2>

<h5 id="fixed-96">Fixed</h5>
<ul>
  <li>Fixed an issue where applications in extremely resource starved environments were seeing ANRs from the periodic dispatch <code class="language-plaintext highlighter-rouge">BroadcastReceiver</code>.  This was not a bug in the Braze code, but a symptom of a failing application.  This updates our periodic dispatch mechanism so it won’t have this symptomatic behavior, which in some cases should help developers track down the source of the actual issue (depending on the bug).  Apps that only use the Braze jar file will now have to register <code class="language-plaintext highlighter-rouge">&lt;service android:name="com.appboy.services.AppboyDataSyncService"/&gt;</code> in their <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code> to enable Braze to periodically flush data.</li>
  <li>Fixed a very rare issue where calling <code class="language-plaintext highlighter-rouge">Context.checkCallingOrSelfPermission()</code> would cause an exception to be thrown on certain custom Android builds.</li>
</ul>

<h5 id="changed-74">Changed</h5>
<ul>
  <li>Updated the News Feed to not show cards in the local cache that have expired.</li>
</ul>

<h2 id="192">1.9.2</h2>

<h5 id="fixed-97">Fixed</h5>
<ul>
  <li>Fixed bug triggered when <code class="language-plaintext highlighter-rouge">AppboyWearableListenerService</code> was not registered.</li>
</ul>

<h2 id="190">1.9.0</h2>

<h5 id="breaking-41">Breaking</h5>
<ul>
  <li>All users must add the line <code class="language-plaintext highlighter-rouge">-dontwarn com.google.android.gms.**</code> to their proguard config file if using proguard.
    <ul>
      <li>See https://github.com/braze-inc/braze-android-sdk/issues/43</li>
    </ul>
  </li>
</ul>

<h5 id="added-91">Added</h5>
<ul>
  <li>Added support for analytics from Android Wear devices.</li>
  <li>Added support for displaying notification action buttons sent from the Braze dashboard.  To allow image sharing on social networks, add the <code class="language-plaintext highlighter-rouge">&lt;uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" /&gt;</code> permission to your <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code>.</li>
  <li>Added delegate to <code class="language-plaintext highlighter-rouge">FeedbackFinishedListener</code> enabling modification of feedback messages before they are sent to Appboy.  Also adds a disposition parameter to <code class="language-plaintext highlighter-rouge">onFeedbackFinished()</code>.</li>
  <li>Added support for GIF images in the News Feed and in in-app messages via the Facebook Fresco image library (version 0.6.1) as a provided library. If found in the parent app (your app), images and GIFs will be loaded using views from the Fresco library. In order to display GIFs, Fresco must be added as a dependency in the parent app. If not found in the parent app, News Feed cards and in-app messages will not display GIFs. To disable use of the Fresco library in the UI project, set the value of <code class="language-plaintext highlighter-rouge">com_appboy_enable_fresco_library_use</code> to false (or omit it) in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>; to enable Fresco use set <code class="language-plaintext highlighter-rouge">com_appboy_enable_fresco_library_use</code> to true in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>. ImageView specific attributes for News Feed cards and in-app messages, such as <code class="language-plaintext highlighter-rouge">scaleType</code>, must now be applied programmatically instead of being applied from <code class="language-plaintext highlighter-rouge">styles.xml</code>. If using Fresco and proguarding your app, please include http://frescolib.org/docs/proguard.html with your proguard config. If you are not using Fresco, add the <code class="language-plaintext highlighter-rouge">dontwarn com.appboy.ui.**</code> directive. Note: to use Fresco with Braze it must be initialized when your application launches.</li>
  <li>Added explicit top and bottom padding values for in-app message buttons to improve button rendering on some phones.  See the <code class="language-plaintext highlighter-rouge">Appboy.InAppMessage.Button</code> style in <code class="language-plaintext highlighter-rouge">styles.xml</code>.</li>
  <li>Added HTML in-app message types. HTML in-app messages consist of html along with an included zipped assets file to locally reference images, css, etc. See <code class="language-plaintext highlighter-rouge">CustomHtmlInAppMessageActionListener</code> in our Droidboy sample app for an example listener for the callbacks on the actions inside the WebView hosting the HTML in-app message.</li>
  <li>Added a <code class="language-plaintext highlighter-rouge">setAttributionData()</code> method to AppboyUser that sets an AttributionData object for the user. Use this method with attribution provider SDKs when attribution events are fired.</li>
</ul>

<h5 id="changed-75">Changed</h5>
<ul>
  <li>Removed the need for integrating client apps to log push notifications inside their activity code.  <strong>Please remove all calls to <code class="language-plaintext highlighter-rouge">Appboy.logPushNotificationOpened()</code> from your app as they are now all handled automatically by Braze.  Otherwise, push opens will be incorrectly logged twice.</strong></li>
  <li>In-app message views are now found in the <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.views</code> package and in-app message listeners are now found in the <code class="language-plaintext highlighter-rouge">com.appboy.ui.inappmessage.listeners</code> package.</li>
</ul>

<h2 id="182">1.8.2</h2>

<h5 id="added-92">Added</h5>
<ul>
  <li>Added the ability to specify custom fonts for in-app message ui elements via the <code class="language-plaintext highlighter-rouge">appboyInAppMessageCustomFontFile</code> custom xml attribute.</li>
  <li>Increases the number of supported currency codes from 22 to 171.  All common currency codes are now supported. The full list of supported codes is available at our <a href="https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/IAppboy.html#logPurchase(java.lang.String,%20java.lang.String,%20java.math.BigDecimal,%20int,%20com.appboy.models.outgoing.AppboyProperties)">Javadoc</a>.</li>
  <li>Added the method <code class="language-plaintext highlighter-rouge">isUninstallTrackingPush()</code> to AppboyNotificationUtils to be able to detect background push sent for Braze uninstall tracking.</li>
</ul>

<h5 id="changed-76">Changed</h5>
<ul>
  <li>Updated <code class="language-plaintext highlighter-rouge">BigPictureStyle</code> to show message in expanded view if summary is not present (after 1.7.0 a summary was required in expanded view to have text appear).</li>
</ul>

<h2 id="181">1.8.1</h2>
<ul>
  <li>Internal release for Xamarin, adds <code class="language-plaintext highlighter-rouge">AppboyXamarinFormsFeedFragment</code>.</li>
</ul>

<h2 id="180">1.8.0</h2>

<h5 id="breaking-42">Breaking</h5>
<ul>
  <li>Updated the minimum sdk version from 8 (froyo) to 9 (gingerbread).</li>
</ul>

<h5 id="added-93">Added</h5>
<ul>
  <li>Added an opt-in location service that logs background location events.</li>
</ul>

<h5 id="fixed-98">Fixed</h5>
<ul>
  <li>Fixed an in-app message lifecycle listener bug where certain lifecycle events could be fired twice.</li>
</ul>

<h2 id="173">1.7.3</h2>

<h5 id="added-94">Added</h5>
<ul>
  <li>Added Braze logging configurability by setting the AppboyLogger.LogLevel.  This is intended to be used in development environments and should not be set in a released application as logging statements are essential for debugging.
    <ul>
      <li>See https://github.com/braze-inc/braze-android-sdk/issues/38</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">getAppboyPushMessageRegistrationId()</code> to the Braze interface to enable retrieval of the GCM/ADM/Baidu registration ID Braze has set for the device.</li>
</ul>

<h5 id="changed-77">Changed</h5>
<ul>
  <li>Updated our libraries to build against API level 22.</li>
  <li>Blacklisted custom attributes may no longer be incremented.</li>
</ul>

<h2 id="172">1.7.2</h2>

<h5 id="added-95">Added</h5>
<ul>
  <li>Introduced <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.getAppboyExtrasWithoutPreprocessing()</code> to parse Braze extras from GCM/ADM intent extras directly rather than requiring Braze extras to be parsed into a Bundle before being passed into <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.getAppboyExtras()</code>.</li>
  <li>Added the ability to send and retrieve extra key-value pairs via a News Feed card.</li>
  <li>Added the ability to define custom key-value properties on a custom event or purchase.  Property keys are strings and values may be strings, doubles, ints, booleans, or <code class="language-plaintext highlighter-rouge">java.util.Date</code> objects.</li>
</ul>

<h5 id="removed-14">Removed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">DownloadUtils.java</code> from <code class="language-plaintext highlighter-rouge">com.appboy.ui.support</code>.  The <code class="language-plaintext highlighter-rouge">downloadImageBitmap()</code> function has been moved to <code class="language-plaintext highlighter-rouge">com.appboy.support.AppboyImageUtils</code>.</li>
</ul>

<h2 id="171">1.7.1</h2>

<h5 id="added-96">Added</h5>
<ul>
  <li>Upgrades Droidboy’s custom user attributes and purchases capability and refactors the settings page.</li>
</ul>

<h5 id="removed-15">Removed</h5>
<ul>
  <li>Removed requirement to manually integrate Font Awesome into the client app’s /assets folder for in-app messages with icons.</li>
</ul>

<h2 id="170">1.7.0</h2>

<h5 id="breaking-43">Breaking</h5>
<ul>
  <li>Added summary subtext in <code class="language-plaintext highlighter-rouge">BigView</code> style notifications.  This is a breaking change in <code class="language-plaintext highlighter-rouge">BigView</code> style notification display.  Previously the summary text in <code class="language-plaintext highlighter-rouge">BigView</code> style notifications was set to the bundle/dashboard summary text if it was present, or the alert message otherwise.  Now the bundle/dashboard summary text is used to set the message subtext, which results in the bundle/dashboard summary text being shown in both the collapsed and expanded views.  See our updated push previews for a visualization of this change.</li>
</ul>

<h5 id="added-97">Added</h5>
<ul>
  <li>Added the ability to set a custom <code class="language-plaintext highlighter-rouge">IAppboyNotificationFactory</code> to customize push using <code class="language-plaintext highlighter-rouge">Appboy.setCustomAppboyNotificationFactory()</code>.</li>
  <li>Added the ability to override title and summary in <code class="language-plaintext highlighter-rouge">BigView</code> push notifications.</li>
  <li>Added the ability to set a default large icon for push messages by adding the <code class="language-plaintext highlighter-rouge">com_appboy_push_large_notification_icon</code> drawable resource to your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
  <li>Added support for modal and full screen style in-app messages.  Also adds support for including fontawesome icons and images with in-app messages, changing colors on in-app message UI elements, expanded customization options, and message resizing for tablets.  Please visit our documentation for more information.</li>
  <li>Added a sample application (China Sample App) which integrates Baidu Cloud Push and Braze for sending push messages through Braze to devices without Google Services installed.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils.logBaiduNotificationClick()</code>, a utility method for logging push notification opens from push messages sent via Baidu Cloud Push by Braze.</li>
</ul>

<h5 id="changed-78">Changed</h5>
<ul>
  <li>Refactors AppboyNotificationUtils into multiple classes in the com.appboy.push package and the AppboyImageUtils class in com.appboy.</li>
</ul>

<h2 id="162">1.6.2</h2>

<h5 id="added-98">Added</h5>
<ul>
  <li>Added a major performance upgrade that reduces CPU usage, memory footprint, and network traffic.</li>
  <li>Added 26 additional languages to localization support for Braze UI elements.</li>
  <li>Added local blocking for blacklisted custom attributes, events, and purchases.  However, blacklisted attributes may still be incremented (removed in release 1.7.3).</li>
  <li>Added the ability to set the accent color for notification in Android Lollipop and above.  This can be done by setting the <code class="language-plaintext highlighter-rouge">com_appboy_default_notification_accent_color</code> integer in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
  <li>Updated the News Feed to render wider on tablet screens.</li>
  <li>Added swipe handling for in-app messages on APIs &lt;= 11.</li>
</ul>

<h5 id="changed-79">Changed</h5>
<ul>
  <li>Updated our UI library to build against API level 21.</li>
</ul>

<h2 id="161">1.6.1</h2>

<h5 id="fixed-99">Fixed</h5>
<ul>
  <li>Fixed a timezone bug where short names were used for lookup, causing the default timezone (GMT) to be set in cases where the short name was not equal to the time zone Id.</li>
  <li>Fixed a bug where multiple pending push intents could override each other in the notification center.</li>
</ul>

<h2 id="160">1.6.0</h2>

<h5 id="fixed-100">Fixed</h5>
<ul>
  <li>Fixed News Feed swipe-refresh <code class="language-plaintext highlighter-rouge">CalledFromWrongThreadException</code>.</li>
</ul>

<h5 id="changed-80">Changed</h5>
<ul>
  <li>Updated the android-L preview support from version 1.5.2 to support the public release of Android 5.0.  Updates the v4 support library dependency to version 21.0.0.</li>
  <li><code class="language-plaintext highlighter-rouge">android.permission.GET_ACCOUNTS</code> is no longer required during initial GCM registration for devices running Jelly Bean and higher.  However, use of this permissions is recommended so that pre-Jelly Bean devices can register with GCM.</li>
  <li><code class="language-plaintext highlighter-rouge">android.permission.WAKE_LOCK</code> is no longer required during initial GCM registration.  However, use of this permissions is recommended to allow notifications to wake the screen and engage users when the notification arrives.</li>
  <li>No longer overwrite messages in the notification center based on collapse key (GCM) or consolidation key (ADM).  Instead, overwrite based on message title and message alert, or, if specified, a custom notification id.</li>
  <li>Updated Droidboy to use the most recent Google IAB helper classes.</li>
</ul>

<h2 id="155">1.5.5</h2>

<h5 id="added-99">Added</h5>
<ul>
  <li>Added support for displaying Kindle notifications with images.</li>
</ul>

<h5 id="changed-81">Changed</h5>
<ul>
  <li>Notifications with a minimum priority specified no longer trigger the device wakelock because Android does not display them in the status bar (they appear silently in the drawer).</li>
</ul>

<h5 id="removed-16">Removed</h5>
<ul>
  <li>Removed styleable elements from the UI project. This should have no impact on consuming projects.</li>
</ul>

<h2 id="154">1.5.4</h2>

<h5 id="added-100">Added</h5>
<ul>
  <li>Incubates a feature to allow for runtime changes to be made to the API key. Please contact android@braze.com if you want to test this feature.</li>
  <li>Added support for Big View text summaries, allowing summary text to be displayed under the main text in a notification.</li>
  <li>Added support for custom URIs to open when a notification is clicked.</li>
  <li>Added support for notification duration control.  When specified, sets an alarm to remove a notification from the notification center after the specified duration.</li>
  <li>Added support for notification sounds.  Users can specify a notification sound URI to play with the notification.</li>
  <li>Added support for changing in-app message duration from the client app.  To do this, you can modify the slideup object passed to you in the <code class="language-plaintext highlighter-rouge">onReceive()</code> delegate using the new setter method <code class="language-plaintext highlighter-rouge">IInAppMessage.setDurationInMilliseconds()</code>.</li>
</ul>

<h5 id="changed-82">Changed</h5>
<ul>
  <li>Updated <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code> to always fill the parent view.  This forces some previously problematic websites to render at the correct size.</li>
</ul>

<h2 id="153">1.5.3</h2>

<h5 id="added-101">Added</h5>
<ul>
  <li>Added the ability to turn off Braze’s automatic location collection using the <code class="language-plaintext highlighter-rouge">com_appboy_disable_location_collection</code> boolean in <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
  <li>Added the ability to send location tracking events to Braze manually using setLastKnownLocation on the AppboyUser.  This is intended to be used with <code class="language-plaintext highlighter-rouge">com_appboy_disable_location_collection</code> set to true so that locations are only being recorded from a single source.</li>
</ul>

<h2 id="152">1.5.2</h2>

<h5 id="added-102">Added</h5>
<ul>
  <li>Added support for GCM and ADM messages without collapse keys.</li>
  <li>Added support for GCM and ADM messages with notification priorities.</li>
  <li>Enabled setting a registration ID without a full push setup; <code class="language-plaintext highlighter-rouge">registerAppboyGcmMessages()</code> and <code class="language-plaintext highlighter-rouge">registerAppboyPushMessages()</code> no longer throw null pointer exceptions if Braze isn’t correctly configured to display push messages.</li>
  <li>Enabled <code class="language-plaintext highlighter-rouge">AppboyWebViewActivity</code> to download items.</li>
  <li>Added support for apps built targeting android-L. Braze’s process for registering push notifications had previously used an implicit service intent which caused a runtime error. Any apps built against android-L will need to upgrade to this version. However, apps with Braze that are/were built against any other versions of Android will run without issue on android-L. Thus, this is not an urgent upgrade unless you’re working with android-L.</li>
</ul>

<h5 id="removed-17">Removed</h5>
<ul>
  <li>Removed extraneous features from Droidboy so it’s more easily digestible as a sample application.</li>
</ul>

<h2 id="151">1.5.1</h2>

<h5 id="removed-18">Removed</h5>
<ul>
  <li>Removed obfuscation from parameter names on public models.</li>
</ul>

<h2 id="150">1.5.0</h2>

<h5 id="added-103">Added</h5>
<ul>
  <li>Added Kindle Fire support and ADM support.</li>
  <li>Added read/unread visual indicators to newsfeed cards. Use the configuration boolean com_appboy_newsfeed_unread_visual_indicator_on in appboy.xml to enabled the indicators.  Additionally, moved the <code class="language-plaintext highlighter-rouge">logFeedCardImpression()</code> and <code class="language-plaintext highlighter-rouge">logFeedCardClick()</code> methods to the card objects themselves.</li>
  <li>Added support to image loading in CaptionedImage and Banner cards for dynamic resizing after loading the image url; supports any aspect ratio.</li>
  <li>Added Hello Appboy sample project that shows a minimal use case of the Braze SDK.</li>
  <li>Added wake lock to <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code> in the UI project. When the <code class="language-plaintext highlighter-rouge">WAKE_LOCK</code> permission is set, the screen will be turned on when a notification is received.</li>
</ul>

<h5 id="changed-83">Changed</h5>
<ul>
  <li>Moved constants from <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code> (ie: <code class="language-plaintext highlighter-rouge">APPBOY_GCM_NOTIFICATION_TITLE_ID</code>, etc.) into new <code class="language-plaintext highlighter-rouge">AppboyNotificationUtils</code> class.</li>
  <li>Restricted productId to 255 characters for <code class="language-plaintext highlighter-rouge">Appboy.logPurchase()</code>.</li>
</ul>

<h2 id="143">1.4.3</h2>

<h5 id="removed-19">Removed</h5>
<ul>
  <li>Removed org.json classes from appboy.jar.</li>
</ul>

<h2 id="142">1.4.2</h2>

<h5 id="added-104">Added</h5>
<ul>
  <li>Added summary text for push image notifications.</li>
  <li>Added a new constant, <code class="language-plaintext highlighter-rouge">APPBOY_LOG_TAG_PREFIX</code>, for logging which includes the sdk version number.</li>
</ul>

<h2 id="141">1.4.1</h2>

<h5 id="added-105">Added</h5>
<ul>
  <li>Added automatic tests to verify that the sdk has integrated correctly.</li>
  <li>Added an optional quantity amount to in-app-purchases.</li>
</ul>

<h5 id="changed-84">Changed</h5>
<ul>
  <li>Changed the device identifier from the device persistent <code class="language-plaintext highlighter-rouge">ANDROID_ID</code> to a non device persistent identifier for compliance with the new Google Play Terms of Service.</li>
</ul>

<h5 id="removed-20">Removed</h5>
<ul>
  <li>Removed default max length and ellipsize properties in the <code class="language-plaintext highlighter-rouge">styles.xml</code>. The old defaults were set to 5 for maxLines for  newsfeed cards and ellipsize ‘end’.</li>
</ul>

<h2 id="140">1.4.0</h2>

<h5 id="added-106">Added</h5>
<ul>
  <li>Added categories.</li>
  <li>Added swipe to refresh functionality to the newsfeed. The swipe to refresh colors are configurable in the colors xml file.</li>
  <li>Added configurable session timeout to the <code class="language-plaintext highlighter-rouge">appboy xml</code>.</li>
  <li>Added images to GCM push notifications.</li>
  <li>Added email and push notification subscription types for a user. Subscription types are explicitly opted in, subscribed, and unsubscribed. The old email boolean subscribe method has been deprecated.</li>
</ul>

<h5 id="changed-85">Changed</h5>
<ul>
  <li>The feedback form now displays error popups to the user on invalid fields.</li>
</ul>

<h5 id="removed-21">Removed</h5>
<ul>
  <li>Removed click logging on slideups when action is <code class="language-plaintext highlighter-rouge">None</code>.</li>
</ul>

<h2 id="134">1.3.4</h2>

<h5 id="changed-86">Changed</h5>
<ul>
  <li>Minor changes to address some Lint issues in the UI project.</li>
  <li>Updated the open source AppboyGcmReceiver to use references to R.java for resource identifiers. This became possible when we moved AppboyGcmReceiver.java into the android-sdk-ui project (from the base library JAR).</li>
</ul>

<h2 id="133">1.3.3</h2>

<h5 id="fixed-101">Fixed</h5>
<ul>
  <li>Minor bug fix for a crash that occurred in certain conditions where the News Feed cards were replaced with a smaller set of cards.</li>
</ul>

<h2 id="132">1.3.2</h2>

<h5 id="fixed-102">Fixed</h5>
<ul>
  <li>Fixed a few minor style issues to be closer in line with Eclipse’s preferences.</li>
  <li>Fixed a potential synchronization issue with the AppboyListAdapter.</li>
  <li>Added the ability to set the avatar image URL for your users.</li>
  <li>Fixed support for protocol URLs and adds an ActivityAction overload that streamlines the use of deep link and web link actions.</li>
</ul>

<h5 id="changed-87">Changed</h5>
<ul>
  <li>Minor update to Chinese language translation.</li>
  <li>Moved com.appboy.AppboyGcmReceiver to the open source android-sdk-ui project. Also moves some of the constants previously available as AppboyGcmReceiver.* to com.appboy.constants.APPBOY_GCM_*. The CAMPAIGN_ID_KEY previously used in our sample app is still available in com.appboy.AppboyGcmReceiver, but if you were using other constants, you’ll have to move the references.</li>
  <li>Removed input validation on custom attribute key names so that you can use foreign characters and spaces to your heart’s desire. Just don’t go over the max character limit.</li>
</ul>

<h2 id="131">1.3.1</h2>

<h5 id="changed-88">Changed</h5>
<ul>
  <li>Updated to version 1.9.1 of Android-Universal-Image-Loader.</li>
  <li>Added Chinese language translations.</li>
  <li>Minor cleanup to imports.</li>
</ul>

<h2 id="13">1.3</h2>

<p>Braze version 1.3 provides a substantial upgrade to the slideup code and reorganization for better flexibility moving forward, but at the expense of a number of breaking changes. We’ve detailed the changes in this changelog and hope that you’ll love the added power, increased flexibility, and improved UI that the new Braze slideup provides. If you have any trouble with these changes, feel free to reach out to success@braze.com for help, but most migrations to the new code structure should be relatively painless.</p>

<h5 id="breaking-44">Breaking</h5>
<p>New AppboySlideupManager</p>
<ul>
  <li>The AppboySlideupManager has moved to <code class="language-plaintext highlighter-rouge">com.appboy.ui.slideups.AppboySlideupManager.java</code>.</li>
  <li>An <code class="language-plaintext highlighter-rouge">ISlideupManagerListener</code> has been provided to allow the developer to control which slideups are displayed, when they are displayed, as well as what action(s) to perform when a slideup is clicked or dismissed.
    <ul>
      <li>The slideup <code class="language-plaintext highlighter-rouge">YOUR-APPLICATION-PACKAGE-NAME.intent.APPBOY_SLIDEUP_CLICKED</code> event has been replaced by the <code class="language-plaintext highlighter-rouge">ISlideupManagerListener.onSlideupClicked(Slideup slideup, SlideupCloser slideupCloser)</code> method.</li>
    </ul>
  </li>
  <li>Added the ability to use a custom <code class="language-plaintext highlighter-rouge">android.view.View</code> class to display slideups by providing an <code class="language-plaintext highlighter-rouge">ISlideupViewFactory</code>.</li>
  <li>Default handling of actions assigned to the slideup from the Braze dashboard.</li>
  <li>Slideups can be dismissed by swiping away the view to either the left or the right. (Only on devices running Honeycomb Android 3.1 or higher).
    <ul>
      <li>Any slideups that are created to be dismissed by a swipe will automatically be converted to auto dismiss slideups on devices that are not running Android 3.1 or higher.</li>
    </ul>
  </li>
</ul>

<p>Slideup model</p>
<ul>
  <li>A key value <code class="language-plaintext highlighter-rouge">extras</code> java.util.Map has been added to provide additional data to the slideup. <code class="language-plaintext highlighter-rouge">Extras</code> can be on defined on a per slideup basis via the dashboard.</li>
  <li>The <code class="language-plaintext highlighter-rouge">SlideFrom</code> field defines whether the slideup originates from the top or the bottom of the screen.</li>
  <li>The <code class="language-plaintext highlighter-rouge">DismissType</code> property controls whether the slideup will dismiss automatically after a period of time has lapsed, or if it will wait for interaction with the user before disappearing.
    <ul>
      <li>The slideup will be dismissed automatically after the number of milliseconds defined by the duration field have elapsed if the slideup’s DismissType is set to AUTO_DISMISS.</li>
    </ul>
  </li>
  <li>The ClickAction field defines the behavior after the slideup is clicked: display a news feed, redirect to a uri, or nothing but dismissing the slideup. This can be changed by calling any of the following methods: <code class="language-plaintext highlighter-rouge">setClickActionToNewsFeed()</code>, <code class="language-plaintext highlighter-rouge">setClickActionToUri(Uri uri)</code>, or <code class="language-plaintext highlighter-rouge">setClickActionToNone()</code>.</li>
  <li>The uri field defines the uri string that the slide up will open when the ClickAction is set to URI. To change this value, use the <code class="language-plaintext highlighter-rouge">setClickActionToUri(Uri uri)</code> method.</li>
  <li>Convenience methods to track slideup impression and click events have been added to the <code class="language-plaintext highlighter-rouge">com.appboy.models.Slideup</code> class.
    <ul>
      <li>Impression and click tracking methods have been removed from <code class="language-plaintext highlighter-rouge">IAppboy.java</code>.</li>
    </ul>
  </li>
  <li>A static <code class="language-plaintext highlighter-rouge">createSlideup</code> method has been added to create custom slideups.</li>
</ul>

<p>IAppboyNavigator</p>
<ul>
  <li>A custom <code class="language-plaintext highlighter-rouge">IAppboyNavigator</code> can be set via <code class="language-plaintext highlighter-rouge">IAppboy.setAppboyNavigator(IAppboyNavigator appboyNavigator)</code> which can be used to direct your users to your integrated Braze news feed when certain slideups are clicked. This provides a more seamless experience for your users. Alternatively, you can choose not to provide an IAppboyNavigator, but instead register the new <code class="language-plaintext highlighter-rouge">AppboyFeedActivity</code> class in your <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code> which will open a new Braze news feed Activity when certain slideups are clicked.</li>
</ul>

<p>Other</p>
<ul>
  <li>A new base class, <code class="language-plaintext highlighter-rouge">AppboyBaseActivity</code>, has been added that extends <code class="language-plaintext highlighter-rouge">android.app.Activity</code> and integrates Braze session and slideup management.</li>
  <li>A drop-in <code class="language-plaintext highlighter-rouge">AppboyFeedActivity</code> class has been added which can be used to display the Braze News Feed.</li>
</ul>

<h2 id="121">1.2.1</h2>

<h5 id="fixed-103">Fixed</h5>
<ul>
  <li>Fixed a ProGuard issue.</li>
</ul>

<h2 id="12">1.2</h2>

<h5 id="added-107">Added</h5>
<ul>
  <li>Introduced two new card types (Banner card and Captioned Image card).</li>
  <li>Added support for sending down key/value pairs as part of a GCM message.</li>
</ul>

<h5 id="fixed-104">Fixed</h5>
<ul>
  <li>Minor bug fixes.</li>
</ul>

<h2 id="11">1.1</h2>

<h5 id="added-108">Added</h5>
<ul>
  <li>Added support for reporting purchases in multiple currencies.</li>
</ul>

<h5 id="fixed-105">Fixed</h5>
<ul>
  <li>Fixed a bug in caching custom events to a SQLite database.</li>
  <li>Fixed a validation bug when logging custom events.</li>
</ul>

<h5 id="changed-89">Changed</h5>
<ul>
  <li>Deprecated <code class="language-plaintext highlighter-rouge">IAppboy.logPurchase(String, int)</code>.</li>
</ul>

<h2 id="10">1.0</h2>
<ul>
  <li>Initial release</li>
</ul>




**Tip:**


You can also find a copy of the [Swift Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-swift-sdk/blob/master/CHANGELOG.md).



<h2 id="1410">14.1.0</h2>

<h5 id="added">Added</h5>
<ul>
  <li>Adds support for Banner dismissal events.
    <ul>
      <li>Adds an optional <code class="language-plaintext highlighter-rouge">onDismiss</code> closure to both <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazebannerui/banneruiview"><code class="language-plaintext highlighter-rouge">BrazeBannerUI.BannerUIView</code></a> (UIKit) and <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazebannerui/bannerview"><code class="language-plaintext highlighter-rouge">BrazeBannerUI.BannerView</code></a> (SwiftUI) for integrators to run custom logic when a banner is dismissed.
        <ul>
          <li>By default, this closure is a no-op.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Improves the robustness of the SDK’s internal state management.
    <ul>
      <li>This release includes an internal refactor intended to make SDK behavior more consistent. No external API changes.</li>
    </ul>
  </li>
  <li>Adds error logging for Banners operations, providing actionable diagnostics for persistence failures and invalid banner states.</li>
</ul>

<h5 id="fixed">Fixed</h5>
<ul>
  <li>Improves robustness around push notification and deep link handling during delayed SDK initialization.</li>
  <li>Fixes an issue where <code class="language-plaintext highlighter-rouge">Braze.FeatureFlags.subscribeToUpdates</code> would not trigger the update closure upon all refresh completions.
    <ul>
      <li>All refresh completions, regardless of a success or error result, will now trigger the update closure. This change brings parity with the Android and Web SDKs.</li>
      <li>Previously, the update closure would not always trigger upon the completion of a refresh request, depending on whether the cached data had previously been reported.</li>
    </ul>
  </li>
</ul>

<h2 id="1404">14.0.4</h2>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Fixes an issue where the configuration of push notification automation would be dropped upon every other re-initialization of the Braze instance.</li>
</ul>

<h2 id="1403">14.0.3</h2>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Push Stories now filter out invalid pages so users can still navigate through remaining valid pages.</li>
</ul>

<h2 id="1402">14.0.2</h2>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Fixes the SwiftUI implementation of <code class="language-plaintext highlighter-rouge">BannerView</code> to update Banner contents in-place whenever a refresh has succeeded.</li>
  <li>Re-exposes the public initializer of <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI.HtmlView</code> as a designated <code class="language-plaintext highlighter-rouge">init</code> instead of a <code class="language-plaintext highlighter-rouge">convenience init</code>, which was introduced in version <code class="language-plaintext highlighter-rouge">14.0.0</code>
    <ul>
      <li>This allows subclasses of <code class="language-plaintext highlighter-rouge">HtmlView</code> to access the public initializer.</li>
    </ul>
  </li>
  <li>Improves robustness of internal SDK logic around dictionary access to prevent potential crashes.</li>
</ul>

<h2 id="1401">14.0.1</h2>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Resolves an issue where the handling of universal links defaulted to the <code class="language-plaintext highlighter-rouge">UIApplicationDelegate</code> implementation instead of the <code class="language-plaintext highlighter-rouge">UISceneDelegate</code> implementation when the app was not in foreground.
    <ul>
      <li>This would occur even if there was no <code class="language-plaintext highlighter-rouge">UIApplicationDelegate</code> implementation, resulting in dropped universal link handling under such scenarios.</li>
    </ul>
  </li>
  <li>Fixes a memory leak where base64-encoded tracking IDs in in-app messages would accumulate on background threads.</li>
  <li>Resolves an issue where in-app messages were not dismissed when the user is changed, resulting in the user seeing incorrect content.
    <ul>
      <li>This change also adds <code class="language-plaintext highlighter-rouge">changeUser</code> dismissal reason for in-app messages.</li>
    </ul>
  </li>
</ul>

<h2 id="1400">14.0.0</h2>

<h5 id="breaking">Breaking</h5>
<ul>
  <li>Removes News Feed.
    <ul>
      <li>This fully removes all UI elements, data models, and actions associated with News Feed.</li>
    </ul>
  </li>
</ul>

<h5 id="added-1">Added</h5>
<ul>
  <li>Remote configuration now automatically refetches after SDK upgrades, keeping server defaults in sync and improving reliability after version changes.</li>
</ul>

<h5 id="fixed-5">Fixed</h5>
<ul>
  <li>Resolves an issue where long text in in-app message buttons would wrap to multiple lines.
    <ul>
      <li>These messages will now match the dashboard preview behavior of truncating long text.</li>
    </ul>
  </li>
  <li>Push Stories now fail gracefully when receiving <code class="language-plaintext highlighter-rouge">null</code>/empty deeplink values.
    <ul>
      <li>Previously, an invalid deeplink would cause the Push Story’s content to appear blank.</li>
      <li><code class="language-plaintext highlighter-rouge">StoryPage</code> safely trims and percent-encodes deeplink strings, dropping invalid values instead of throwing an error.</li>
      <li><code class="language-plaintext highlighter-rouge">StoryView</code> only scrolls when pages exist, preventing the “Next” action from crashing when the carousel is empty.</li>
    </ul>
  </li>
  <li>HTML in-app messages now reuse cached payloads to mitigate app hangs that occur in rare situations during presentation.</li>
  <li>Templated in-app messages with delayed presentation will now request templated values only after completion of the delay.
    <ul>
      <li>This ensures that templated values are most up-to-date with the display of the message.</li>
      <li>Previously, the request for templated values would occur at trigger time, prior to the delay.</li>
    </ul>
  </li>
</ul>

<h2 id="1330">13.3.0</h2>

<h5 id="added-2">Added</h5>
<ul>
  <li>Improves reliability when sending the push token and push authorization status to the backend.
    <ul>
      <li>This change ensures that push authorization status changes will be flushed immediately as soon as they are read.</li>
    </ul>
  </li>
</ul>

<h2 id="1321">13.2.1</h2>

<h5 id="fixed-6">Fixed</h5>
<ul>
  <li>Resolves an issue where an accumulation of Banners pending requests could cause the host application to hang at app startup.
    <ul>
      <li>This fix performs additional cleanup to any existing requests that were accumulated from previous versions, so you do not need to do any manual cleanup.</li>
    </ul>
  </li>
</ul>

<h2 id="1320">13.2.0</h2>

<h5 id="added-3">Added</h5>
<ul>
  <li>Adds support for compilation with Xcode 26.0 and its corresponding operating system runtimes on all platforms supported by the Braze Swift SDK.</li>
</ul>

<h2 id="1310">13.1.0</h2>

<h5 id="added-4">Added</h5>
<ul>
  <li>Adds support for Banner properties via new public methods on <code class="language-plaintext highlighter-rouge">Braze.Banner</code> instances.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">banner.stringProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">String</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.numberProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">Double</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.timestampProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">Int</code> Unix millisecond timestamp properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.booleanProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">Bool</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.imageProperty(key:)</code> for accessing image URL properties as <code class="language-plaintext highlighter-rouge">String</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.jsonProperty(key:)</code> for accessing JSON properties as <code class="language-plaintext highlighter-rouge">[String:Any]</code> dictionaries.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.jsonProperty&lt;T: Decodable&gt;(key:type:decoder:)</code> for accessing JSON properties as values of any custom <code class="language-plaintext highlighter-rouge">Decodable</code> type.</li>
    </ul>
  </li>
  <li>The default client-side rate limiting values for Banners refresh has been increased. For more information on SDK rate limiting, please refer to the <a href="https://www.braze.com/docs/developer_guide/sdk_integration/rate_limits#braze-sdk-rate-limits">Braze Developer Guide</a></li>
</ul>

<h5 id="fixed-7">Fixed</h5>
<ul>
  <li>Improves the behavior of VoiceOver for assets that are missing an <code class="language-plaintext highlighter-rouge">imageAltText</code> for Content Card and In-App Message campaigns created via the Traditional editor.
    <ul>
      <li>These assets will no longer be selectable or narrated by VoiceOver. Previously, the asset would be selectable and VoiceOver would read gibberish.</li>
      <li>Drag-and-drop campaigns are not affected by this issue.</li>
      <li>Campaigns created using the Traditional editor should always have the <code class="language-plaintext highlighter-rouge">Alt text</code> field populated for accessible users.</li>
    </ul>
  </li>
</ul>

<h2 id="1300">13.0.0</h2>

<h5 id="breaking-1">Breaking</h5>
<ul>
  <li>Extends the functionality of <code class="language-plaintext highlighter-rouge">BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)</code> to be triggered for “Optional” authentication errors.
    <ul>
      <li>The delegate method <code class="language-plaintext highlighter-rouge">BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)</code> will now be triggered for both “Required” <strong>and “Optional”</strong> authentication errors.</li>
      <li>If you want to only handle “Required” SDK authentication errors, add a check ensuring that <code class="language-plaintext highlighter-rouge">BrazeSDKAuthError.optional</code> is <code class="language-plaintext highlighter-rouge">false</code> inside your implementation of this delegate method.</li>
    </ul>
  </li>
  <li>Fixes the usage of <code class="language-plaintext highlighter-rouge">Braze.Configuration.sdkAuthentication</code> to take effect when enabled.
    <ul>
      <li>Previously, the value of this configuration was not consumed by the SDK and the token was always attached to requests if it was present.</li>
      <li>Now, the SDK will only attach the SDK authentication token to outgoing network requests when this configuration is enabled.</li>
    </ul>
  </li>
  <li>The setters for all properties of <code class="language-plaintext highlighter-rouge">Braze.FeatureFlag</code> and all properties of <code class="language-plaintext highlighter-rouge">Braze.Banner</code> have been made <code class="language-plaintext highlighter-rouge">private</code>. The properties of these classes are now read-only.</li>
  <li>Removes the <code class="language-plaintext highlighter-rouge">banner.id</code> property, which was deprecated in version <code class="language-plaintext highlighter-rouge">11.4.0</code>.
    <ul>
      <li>Instead, use <code class="language-plaintext highlighter-rouge">banner.trackingId</code> to read a banner’s campaign tracking ID.</li>
    </ul>
  </li>
</ul>

<h5 id="added-5">Added</h5>
<ul>
  <li>Adds the boolean field <code class="language-plaintext highlighter-rouge">optional</code> to <code class="language-plaintext highlighter-rouge">BrazeSDKAuthError</code> to indicate if it is an optional authentication error.</li>
</ul>

<h2 id="1210">12.1.0</h2>

<h5 id="added-6">Added</h5>
<ul>
  <li>Adds optional <code class="language-plaintext highlighter-rouge">imageAltText</code> and <code class="language-plaintext highlighter-rouge">language</code> fields to UI classes and structs associated with Content Card and In-App Message campaigns for improved accessibility.
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">imageAltText</code> field contains the image accessibility alt text (if any) for the image or icon in a given campaign. The SDK’s default UI will use this field to inform how VoiceOver narrates the image portion of a campaign</li>
      <li>The optional <code class="language-plaintext highlighter-rouge">language</code> field is a <a href="https://en.wikipedia.org/wiki/IETF_language_tag">BCP 47</a> tag. If it is present, VoiceOver will use the corresponding language narrator when reading the campaign. Otherwise, the user system default settings will be used.</li>
      <li>These are the classes and structs with <code class="language-plaintext highlighter-rouge">imageAltText</code> and <code class="language-plaintext highlighter-rouge">language</code>:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">Braze.ContentCard.ClassicImage</code></li>
          <li><code class="language-plaintext highlighter-rouge">Braze.ContentCard.ImageOnly</code></li>
          <li><code class="language-plaintext highlighter-rouge">Braze.ContentCard.CaptionedImage</code></li>
          <li><code class="language-plaintext highlighter-rouge">Braze.ContentCardRaw</code> (<code class="language-plaintext highlighter-rouge">BRZContentCardRaw</code> in Objective-C)</li>
          <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.Slideup</code></li>
          <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.Modal</code></li>
          <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.ModalImage</code></li>
          <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.Full</code></li>
          <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.FullImage</code></li>
          <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessageRaw</code> (<code class="language-plaintext highlighter-rouge">BRZInAppMessageRaw</code> in Objective-C)</li>
          <li><code class="language-plaintext highlighter-rouge">Braze.ContentCard.Classic</code> has the <code class="language-plaintext highlighter-rouge">language</code> field only</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Adds provisional support for Xcode 26 Beta via the <a href="https://github.com/braze-inc/braze-swift-sdk-xcode-26-preview"><code class="language-plaintext highlighter-rouge">braze-inc/braze-swift-sdk-xcode-26-preview</code></a> repository.
    <ul>
      <li>Full support will be added to the main repository closer to the public release of Xcode 26.</li>
      <li>For any compatibility issues discovered while using the Xcode 26 Beta, submit a GitHub issue on the <a href="https://github.com/braze-inc/braze-swift-sdk/issues">main repository</a>.</li>
    </ul>
  </li>
</ul>

<h2 id="1203">12.0.3</h2>

<h5 id="fixed-8">Fixed</h5>
<ul>
  <li>Fixes the Banner rendering incompatibility with iOS 18.5+ while maintaining the correct URL redirect behavior.
    <ul>
      <li>Banners can now successfully render on iOS 18.5+ without compromising click action functionality.</li>
      <li>See the changelog entries for versions 12.0.1 and 12.0.2 for further details.</li>
    </ul>
  </li>
</ul>

<h2 id="1202">12.0.2</h2>

<p>⚠️ Important: This version has a known issue preventing Banners from rendering on iOS 18.5+.</p>

<h5 id="fixed-9">Fixed</h5>
<ul>
  <li>Reverts Banners to the behavior found in versions <code class="language-plaintext highlighter-rouge">12.0.0</code> and prior.
    <ul>
      <li>Banners remain unusable on iOS 18.5+. A future release will address this issue.</li>
    </ul>
  </li>
</ul>

<h2 id="1201">12.0.1</h2>

<p>⚠️ Important: This version has a known issue in Drag-and-Drop in-app messages and Banners, preventing certain URLs from redirecting properly. Update to a newer version if you are using this feature.</p>

<h5 id="fixed-10">Fixed</h5>
<ul>
  <li>Fixes an issue where setting <code class="language-plaintext highlighter-rouge">configuration.forwardUniversalLinks = true</code> would not properly forward universal links to the system APIs in some cases.
    <ul>
      <li>The SDK now verifies that the system APIs are implemented (either in your <code class="language-plaintext highlighter-rouge">UIApplicationDelegate</code> or <code class="language-plaintext highlighter-rouge">SceneDelegate</code>) before forwarding the universal link.</li>
      <li>When multiple implementations are found, the SDK favors the <code class="language-plaintext highlighter-rouge">SceneDelegate</code> implementation over the <code class="language-plaintext highlighter-rouge">UIApplicationDelegate</code> implementation.</li>
    </ul>
  </li>
  <li>Fixes an issue when configuring <code class="language-plaintext highlighter-rouge">Braze.Configuration.Push.Automation.authorizationOptions</code> with the <code class="language-plaintext highlighter-rouge">.provisional</code> option.
    <ul>
      <li>Previously, the <code class="language-plaintext highlighter-rouge">.provisional</code> option was also applied for push primer in-app messages. This resulted in no push notification permission prompt being shown to the user.</li>
      <li>With this change, push primer in-app messages will request push notification permissions using only the <code class="language-plaintext highlighter-rouge">.alert</code>, <code class="language-plaintext highlighter-rouge">.badge</code>, and <code class="language-plaintext highlighter-rouge">.sound</code> options, ensuring that the system prompt is presented to the user.</li>
    </ul>
  </li>
  <li>Fixes an incompatibility with iOS 18.5 where Banners would not render.
    <ul>
      <li>Previously, the Banner view would be added to the view hierarchy with a height of 0 but never successfully load the HTML content.</li>
      <li>Banner views will no longer trigger superfluous <code class="language-plaintext highlighter-rouge">about:blank</code> URLs upon initial load.</li>
    </ul>
  </li>
</ul>

<h2 id="1200">12.0.0</h2>

<h5 id="breaking-2">Breaking</h5>
<ul>
  <li>The distributed static XCFrameworks now include their resources directly instead of relying on external resources bundles.
    <ul>
      <li>When manually integrating the static XCFrameworks, you must select the <em>Embed &amp; Sign</em> option for each XCFramework in the <em>Frameworks, Libraries, and Embedded Content</em> section of your target’s <em>General</em> settings.</li>
      <li>No changes are required for Swift Package Manager or CocoaPods integrations.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-11">Fixed</h5>
<ul>
  <li>Fixes an App Store validation issue where Braze’s libraries privacy manifests would fail to be detected when integrating the SDK as static XCFrameworks.</li>
  <li>Fixes <code class="language-plaintext highlighter-rouge">BrazeKitCompat</code> <code class="language-plaintext highlighter-rouge">ABKContentCard.expiresAt</code> to return the correct expiration date.
    <ul>
      <li>Previously, <code class="language-plaintext highlighter-rouge">ABKContentCard.expiresAt</code> would always return <code class="language-plaintext highlighter-rouge">0</code>.</li>
    </ul>
  </li>
  <li>Fixes an issue where the <code class="language-plaintext highlighter-rouge">Braze.FeatureFlags.subscribeToUpdates(_:)</code> update closure was being called immediately after calling <code class="language-plaintext highlighter-rouge">changeUser(userId:)</code> instead of waiting for the next feature flags sync result.</li>
  <li>Fixes an issue where <code class="language-plaintext highlighter-rouge">Braze.ContentCards.subscribeToUpdates(_:)</code> would not call the update closure whenever a sync occurred without any changes in the Content Cards data.
    <ul>
      <li>Previously, the update closure would only be called when the sync resulted in a change.</li>
    </ul>
  </li>
  <li>Fixes the <code class="language-plaintext highlighter-rouge">Braze.User.set(dateOfBirth:)</code> method to report dates using the Gregorian calendar instead of the device’s current calendar setting.
    <ul>
      <li>Previously, the SDK would override input dates and formats if the device’s calendar settings were non-Gregorian.</li>
      <li>With this change, you will still need to ensure that dates provided to <code class="language-plaintext highlighter-rouge">set(dateOfBirth:)</code> are generated with the Gregorian calendar, but the Braze SDK will no longer override their formats inadvertently.</li>
    </ul>
  </li>
  <li>Enhances the <code class="language-plaintext highlighter-rouge">⁠braze.wipeData()</code> function to send a final update to all registered channel subscribers, notifying them of the data wipe.
    <ul>
      <li>This update ensures that any UI components utilizing the channel’s data are properly dismissed and cleaned up.</li>
      <li>For instance, if an in-app message is currently displaying as <code class="language-plaintext highlighter-rouge">braze.wipeData()</code> is called, the message will be removed from display.</li>
    </ul>
  </li>
  <li>Fixes <code class="language-plaintext highlighter-rouge">braze.user.id</code> not resetting to <code class="language-plaintext highlighter-rouge">nil</code> after calling <code class="language-plaintext highlighter-rouge">braze.wipeData()</code>.
    <ul>
      <li>Internally, the user identifier was properly reset, but the public <code class="language-plaintext highlighter-rouge">braze.user.id</code> property was not updated to reflect this change.</li>
    </ul>
  </li>
</ul>

<h5 id="added-7">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">BrazeInAppMessagePresenter.dismiss(reason:)</code> optional protocol method.
    <ul>
      <li>This method enables the SDK to inform the in-app message presenter when an in-app message should be dismissed due to an internal SDK state change.</li>
      <li>Currently, this method is triggered only by calling <code class="language-plaintext highlighter-rouge">⁠braze.wipeData()</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI</code> implements this optional method and dismisses the in-app message when triggered.</li>
    </ul>
  </li>
</ul>

<h2 id="1190">11.9.0</h2>

<h5 id="added-8">Added</h5>
<ul>
  <li>Adds <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/pushtostarttokenupdatesstream"><code class="language-plaintext highlighter-rouge">Braze.LiveActivities.pushToStartTokenUpdatesStream: AsyncStream&lt;Braze.LiveActivities.PushToStartTokenUpdate&gt;</code></a>, an asynchronous stream which publishes updates pertaining to the Live Activities push-to-start token lifecycle.
    <ul>
      <li>See <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/pushtostarttokenupdate"><code class="language-plaintext highlighter-rouge">Braze.LiveActivities.PushToStartTokenUpdate</code></a> for all varieties of update events published by the stream.</li>
    </ul>
  </li>
  <li>Adds dSYM files to the dynamic and mergeable variants of the Braze SDK XCFrameworks.
    <ul>
      <li>This addresses an App Store submission validation warning when using Xcode 16.0 or later.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-12">Fixed</h5>
<ul>
  <li>The SDK Debugger tool will now capture logs even when <code class="language-plaintext highlighter-rouge">Braze.configuration.logger.level</code> is <code class="language-plaintext highlighter-rouge">.disabled</code> and no SDK logging occurs locally.
    <ul>
      <li>This aligns the Braze Swift SDK Debugger Tool behavior with that of the Debugger Tool on the Braze Android SDK.</li>
    </ul>
  </li>
  <li>Sets the default background of <code class="language-plaintext highlighter-rouge">BannerUIView</code> to be transparent.</li>
  <li>Renames the <code class="language-plaintext highlighter-rouge">VisibilityTracker.displayLinkTick</code> method to <code class="language-plaintext highlighter-rouge">VisibilityTracker.brazeDisplayLinkTick</code> in BrazeUI to avoid potential naming conflicts with private system methods.</li>
</ul>

<h2 id="1180">11.8.0</h2>

<h5 id="added-9">Added</h5>
<ul>
  <li>Network requests made by the SDK to the Braze Live Activities <code class="language-plaintext highlighter-rouge">/push_token_tag</code> endpoint will now be retried in the case of a request failure.</li>
  <li>Expands customizability options of custom endpoints passed when initializing a <code class="language-plaintext highlighter-rouge">Braze</code> instance.
    <ul>
      <li>You can now specify a base path to be used for SDK network requests (i.e. “example.com/mockServer”).</li>
      <li><code class="language-plaintext highlighter-rouge">http</code> schemes are now supported for use by custom endpoints (i.e. http://example.com). Previously, only <code class="language-plaintext highlighter-rouge">https</code> schemes were supported.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-13">Fixed</h5>
<ul>
  <li>Fixes an issue where in-app messages would not always be triggered when sending Braze requests to the tracking endpoint. This occurred when both of the following conditions are true:
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">Braze.Configuration.Api.trackingPropertyAllowList</code> did not include the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/everything"><code class="language-plaintext highlighter-rouge">.everything</code> type</a>.</li>
      <li>All other <code class="language-plaintext highlighter-rouge">Braze.Configuration.TrackingProperty</code> types were manually listed in the <code class="language-plaintext highlighter-rouge">trackingPropertyAllowList</code>.</li>
    </ul>
  </li>
  <li>Improves the rendering behavior of Banner Cards embedded in a scroll view on hybrid development frameworks.</li>
  <li>Fixes the Banner Card view to prevent drag gestures from exposing the background of the HTML content.</li>
  <li>Fixes an issue on the Braze web view bridge where numeric values of <code class="language-plaintext highlighter-rouge">1</code> or <code class="language-plaintext highlighter-rouge">0</code> would be incorrectly reported as <code class="language-plaintext highlighter-rouge">true</code> or <code class="language-plaintext highlighter-rouge">false</code>, respectively.</li>
</ul>

<h2 id="1170">11.7.0</h2>

<h5 id="added-10">Added</h5>
<ul>
  <li>Adds the ability for a banner container to resize when the banner content changes height.</li>
</ul>

<h2 id="1161">11.6.1</h2>

<h5 id="fixed-14">Fixed</h5>
<ul>
  <li>Improves the reliability of collecting Live Activity push-to-start tokens on calling <code class="language-plaintext highlighter-rouge">registerPushToStart</code>:
    <ul>
      <li>Push-to-start tokens will now flush to the server immediately as soon as they are retrieved.</li>
      <li>Push-to-start tokens will now be read immediately from the <code class="language-plaintext highlighter-rouge">pushToStartToken</code> property as soon as <code class="language-plaintext highlighter-rouge">registerPushToStart</code> is called, in addition to the existing behavior where an observable is set up to monitor new tokens.</li>
    </ul>
  </li>
  <li>Resolves issues with the SDK’s internal state for devices that were previously affected after restoring from another device’s iCloud or iTunes backup.
    <ul>
      <li>Previously, these devices would incorrectly inherit the device ID from the original device.</li>
      <li>With this update, the SDK now generates a unique device ID for each restored device, ensuring proper identification and functionality.</li>
      <li>This update follows up on the <code class="language-plaintext highlighter-rouge">11.6.0</code> fix, which prevented the issue from occurring on future backups.</li>
    </ul>
  </li>
</ul>

<h2 id="1160">11.6.0</h2>

<h5 id="fixed-15">Fixed</h5>
<ul>
  <li>Fixes the behavior in the Braze-provided UI for Banner Cards where content would not automatically be cleared from the UI when changing to a user that was not eligible for that campaign.</li>
  <li>Changes the behavior of <code class="language-plaintext highlighter-rouge">Braze.Banners.subscribeToUpdates(_:)</code> to match behavior of the corresponding API on the Braze Android SDK.
    <ul>
      <li>Upon calling <code class="language-plaintext highlighter-rouge">Braze.Banners.subscribeToUpdates(_:)</code>, the update handler closure will only be called if a banners sync has succeeded during the current user session.
        <ul>
          <li>Previously, calling <code class="language-plaintext highlighter-rouge">Braze.Banners.subscribeToUpdates(_:)</code> would always result in the update handler being called one time immediately.</li>
        </ul>
      </li>
      <li>Upon successfully completing a banners sync, <code class="language-plaintext highlighter-rouge">Braze.Banners.subscribeToUpdates(_:)</code> will call its registered update handler even if the sync result is identical to the last successful sync.</li>
    </ul>
  </li>
  <li>Changes the behavior of <code class="language-plaintext highlighter-rouge">Braze.Banners.bannersStream</code> to match behavior of the corresponding API on the Braze Android SDK.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.Banners.bannersStream</code> will now only emit an update immediately upon access if a banners sync has succeeded during the current user session.
        <ul>
          <li>Previously, accessing <code class="language-plaintext highlighter-rouge">Braze.Banners.bannersStream</code> would always emit one update immediately.</li>
        </ul>
      </li>
      <li>Upon successfully completing a banners sync, <code class="language-plaintext highlighter-rouge">Braze.Banners.bannersStream</code> will emit an update even if the sync result is identical to the last successful sync.</li>
    </ul>
  </li>
  <li>JavaScript bridge methods expecting number arguments now also accept string representations of numbers.
    <ul>
      <li>This change aligns the behavior of the Swift SDK with the behavior of the Web SDK.</li>
    </ul>
  </li>
</ul>

<h5 id="added-11">Added</h5>
<ul>
  <li>Adds an optional method <code class="language-plaintext highlighter-rouge">removeBannerContent</code> to the <code class="language-plaintext highlighter-rouge">BrazeBannerPlacement</code> protocol.</li>
  <li>Locally persisted Braze SDK data will no longer transfer during OS backups. This resolves an issue introduced in <code class="language-plaintext highlighter-rouge">6.2.0</code>.</li>
</ul>

<h2 id="1150">11.5.0</h2>

<h5 id="fixed-16">Fixed</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">Braze.banners.getBanner(for:_:)</code> now successfully returns a cached <code class="language-plaintext highlighter-rouge">Banner</code> object for the requested placement ID as long as a Banner Cards sync has ever succeeded for the current user.
    <ul>
      <li>Previously, it would log a warning and pass <code class="language-plaintext highlighter-rouge">nil</code> to the completion handler if a Banner Cards sync had not been completed for the current user during the current session specifically.</li>
      <li>This change aligns behavior with the Android SDK.</li>
    </ul>
  </li>
  <li>Fixes an issue where images with the <code class="language-plaintext highlighter-rouge">"JPEG"</code> image type would sometimes not display in Push Stories.</li>
  <li>Fixes an issue where an in-app message in a Braze-provided UI can be displayed for an ineligible user under rare conditions.
    <ul>
      <li>This may occur if the in-app message was in the process of being displayed in the UI at the same time that the user was changed to a different user.</li>
    </ul>
  </li>
</ul>

<h5 id="added-12">Added</h5>
<ul>
  <li>Adds <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user/id"><code class="language-plaintext highlighter-rouge">Braze.User.id</code></a> to access the current user identifier synchronously.
    <ul>
      <li>Deprecates <code class="language-plaintext highlighter-rouge">Braze.User.id() async</code> and <code class="language-plaintext highlighter-rouge">Braze.User.id(queue:completion:)</code> in favor of <code class="language-plaintext highlighter-rouge">Braze.User.id</code>.
        <ul>
          <li>These methods will be removed fully in a future update.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Adds the optional parameter <code class="language-plaintext highlighter-rouge">userIDMatchBehavior</code> to the initializers of <code class="language-plaintext highlighter-rouge">Braze.InAppMessageRaw.Context</code>. This determines the behavior in the UI when the current identified user is different from the one that triggered the in-app message.
    <ul>
      <li>The default for Braze-provided UIs (<code class="language-plaintext highlighter-rouge">.enforce</code>) will enforce that the user ID matches the user ID that triggered the in-app message. If there is a mismatch, the in-app message will not be displayed.</li>
      <li>For custom UIs, the default is <code class="language-plaintext highlighter-rouge">.ignore</code> and a mismatch will still display the in-app message.</li>
    </ul>
  </li>
</ul>

<h2 id="1140">11.4.0</h2>

<h5 id="fixed-17">Fixed</h5>
<ul>
  <li>Fixes an issue where the SDK could hang during initialization if previous sessions generated a large number of geofence refreshes. This hang could sometimes lead to a crash by blocking the main thread for an extended period.</li>
  <li>Fixes an issue where the triggering of in-app messages could be delayed in cases where requests for updated in-app message triggers are also delayed due to rate limiting.</li>
  <li>Adds additional safeguards to ensure that ongoing network requests are dropped when changing users mid-flight.</li>
</ul>

<h5 id="added-13">Added</h5>
<ul>
  <li>When Content Cards, Feature Flags, or Banner Cards go from enabled to disabled, the stored data is removed from cache.</li>
  <li>Adds <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/trackingid"><code class="language-plaintext highlighter-rouge">banner.trackingId</code></a> to distinguish between banner objects.
    <ul>
      <li>Deprecates <code class="language-plaintext highlighter-rouge">banner.id</code> in favor of <code class="language-plaintext highlighter-rouge">banner.trackingId</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="1130">11.3.0</h2>

<h5 id="fixed-18">Fixed</h5>
<ul>
  <li>Fixes a behavior where calling the <code class="language-plaintext highlighter-rouge">logClick</code> bridge method in HTML in-app messages with <code class="language-plaintext highlighter-rouge">""</code> as the button ID would log an error.
    <ul>
      <li>Instead, this would log an in-app message body click to match other platforms.</li>
    </ul>
  </li>
</ul>

<h5 id="added-14">Added</h5>
<ul>
  <li>Adds support for the Braze Banner Cards product.
    <ul>
      <li>For usage details, refer to our tutorial <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c4-bannersui">here</a>.</li>
    </ul>
  </li>
</ul>

<h2 id="1120">11.2.0</h2>

<h5 id="fixed-19">Fixed</h5>
<ul>
  <li>Fixes the Objective-C <code class="language-plaintext highlighter-rouge">Braze.delegate</code> declaration to be <code class="language-plaintext highlighter-rouge">weak</code> like the Swift variant.</li>
</ul>

<h5 id="added-15">Added</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">Braze.prepareForDelayedInitialization</code> now takes an optional parameter <code class="language-plaintext highlighter-rouge">analyticsBehavior: PushEnqueueBehavior</code>.
    <ul>
      <li>Braze uses this value to determine whether any Braze push payloads received before initialization should be processed once initialization is complete.</li>
      <li><code class="language-plaintext highlighter-rouge">PushEnqueueBehavior.queue</code> will enqueue received push payloads to be processed upon initialization. This option is selected by default.</li>
      <li><code class="language-plaintext highlighter-rouge">PushEnqueueBehavior.drop</code> will drop received push payloads, ignoring them.</li>
    </ul>
  </li>
  <li>Adds configuration properties to customize the <code class="language-plaintext highlighter-rouge">lineSpacing</code>, <code class="language-plaintext highlighter-rouge">maxLineHeight</code>, <code class="language-plaintext highlighter-rouge">minLineHeight</code>, and <code class="language-plaintext highlighter-rouge">lineHeightMultiple</code> for the header and message texts in full and modal in-app messages.</li>
  <li>Updates <code class="language-plaintext highlighter-rouge">BrazeContentCardUI.ViewController.Attributes.defaults</code> to be a <code class="language-plaintext highlighter-rouge">var</code> to allow directly editing the property for convenience.</li>
</ul>

<h2 id="1111">11.1.1</h2>

<h5 id="fixed-20">Fixed</h5>
<ul>
  <li>Fixes an issue introduced in <code class="language-plaintext highlighter-rouge">11.0.0</code> where the push subscription status would be sent to the backend with an inaccurate value at startup, causing an unexpected subscription state. The SDK now sends up the accurate subscription status at each startup.</li>
</ul>

<h2 id="1110">11.1.0</h2>

<p>⚠️ <strong>Important:</strong> This version has a known issue related to push subscription status. Upgrade to version <code class="language-plaintext highlighter-rouge">11.1.1</code> instead.</p>

<h5 id="fixed-21">Fixed</h5>
<ul>
  <li>Fixes an issue introduced in <code class="language-plaintext highlighter-rouge">11.0.0</code> where the push token status would not always be reported in all circumstances.</li>
  <li>Fixes a display bug where an in-app message would appear truncated after certain keyboard dismissal scenarios.</li>
  <li>Fixes a reference cycle in <code class="language-plaintext highlighter-rouge">Braze.NewsFeedCard.Context</code> that could prevent the card from being deallocated.</li>
</ul>

<h5 id="added-16">Added</h5>
<ul>
  <li>Adds a public initializer for <code class="language-plaintext highlighter-rouge">Braze.Notifications.Payload</code>.</li>
</ul>

<h2 id="1101">11.0.1</h2>

<h5 id="fixed-22">Fixed</h5>
<ul>
  <li>Fixes an issue introduced in <code class="language-plaintext highlighter-rouge">11.0.0</code> where the push subscription status would be sent to the backend with an inaccurate value at startup, causing an unexpected subscription state. The SDK now sends up the accurate subscription status at each startup.</li>
</ul>

<h2 id="1100">11.0.0</h2>

<p>⚠️ <strong>Important:</strong> This version has a known issue related to push subscription status. Upgrade to version <code class="language-plaintext highlighter-rouge">11.1.1</code> instead.</p>

<h5 id="breaking-3">Breaking</h5>
<ul>
  <li>Adds support for <a href="https://developer.apple.com/documentation/swift/adoptingswift6">Swift 6 strict concurrency checking</a>.
    <ul>
      <li>Relevant public Braze classes and data types now conform to the <code class="language-plaintext highlighter-rouge">Sendable</code> protocol and can be safely used across concurrency contexts.</li>
      <li>Main thread-only APIs are now marked with the <code class="language-plaintext highlighter-rouge">@MainActor</code> attribute.</li>
      <li>We recommend using Xcode 16.0 or later to take advantage of these features while minimizing the number of warnings generated by the compiler. Previous versions of Xcode may still be used, but some features may generate warnings.</li>
    </ul>
  </li>
  <li>When integrating push notification support manually, you may need to update the <code class="language-plaintext highlighter-rouge">UNUserNotificationCenterDelegate</code> conformance to use the <code class="language-plaintext highlighter-rouge">@preconcurrency</code> attribute to prevent warnings.
    <ul>
      <li>Applying the <code class="language-plaintext highlighter-rouge">@preconcurrency</code> attribute on protocol conformance is only available in Xcode 16.0 or later. Reference our sample integration code <a href="https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual">here</a>.</li>
      <li>As of Xcode 16.0, Apple has not yet audited the <code class="language-plaintext highlighter-rouge">UNUserNotificationCenterDelegate</code> protocol for Swift concurrency.
        <div class="language-swift highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="kd">extension</span> <span class="kt">AppDelegate</span><span class="p">:</span> <span class="kd">@preconcurrency</span> <span class="kt">UNUserNotificationCenterDelegate</span> <span class="p">{</span>
<span class="c1">// Your existing implementation</span>
<span class="p">}</span>
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
  <li>Updates the <code class="language-plaintext highlighter-rouge">SDWebImage</code> dependency in <code class="language-plaintext highlighter-rouge">BrazeUICompat</code> and sample apps to <code class="language-plaintext highlighter-rouge">5.19.7+</code> to support Swift 6 strict concurrency checking.</li>
</ul>

<h4 id="fixed-23">Fixed</h4>
<ul>
  <li>Fixes the push authorization status reporting to display the proper push token status on the Dashboard when a user has not explicitly accepted or declined push permissions.</li>
</ul>

<h2 id="1031">10.3.1</h2>

<h5 id="fixed-24">Fixed</h5>
<ul>
  <li>Improves the reliability of sending updates to Live Activities that were launched via a push-to-start notification to an app in the terminated state.</li>
</ul>

<h2 id="1030">10.3.0</h2>

<h5 id="fixed-25">Fixed</h5>
<ul>
  <li>Fixes the in-app message orientation validation logic, which prevented certain device classes from displaying messages under certain orientation configurations.</li>
  <li>Fixes the default behavior on full-screen in-app messages to display as modals only on tablet screen sizes.
    <ul>
      <li>Previously, full-screen messages would erroneously default to modal presentations on some larger phones.</li>
    </ul>
  </li>
  <li>Fixes a crash when dismissing a slideup in-app message before it has finished presenting.</li>
  <li>Fixes an issue on iOS 18.0+ where the in-app message UI would persist on the screen when attempting to dismiss the message before it has finished presenting.</li>
  <li>Updates custom attribute value, custom event, and purchase string validation to use a 255 character maximum instead of a 255 byte maximum.</li>
</ul>

<h5 id="added-17">Added</h5>
<ul>
  <li>The <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)"><code class="language-plaintext highlighter-rouge">Braze.set(identifierForAdvertiser:)</code></a> and <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)"><code class="language-plaintext highlighter-rouge">Braze.set(identifierForVendor:)</code></a> methods now accept a <code class="language-plaintext highlighter-rouge">nil</code> parameter value to remove the identifiers from the user profile.</li>
  <li>Adds additional safeguards to <code class="language-plaintext highlighter-rouge">Braze.Notifications.subscribeToUpdates</code> to ensure the same Push notification can’t trigger the update closure multiple times.</li>
</ul>

<h2 id="1020">10.2.0</h2>

<h5 id="fixed-26">Fixed</h5>
<ul>
  <li>Updates the content card image background color to be clear.</li>
</ul>

<h5 id="added-18">Added</h5>
<ul>
  <li>Adds support for an upcoming Braze SDK Debugging tool.</li>
</ul>

<h2 id="1010">10.1.0</h2>

<h5 id="fixed-27">Fixed</h5>
<ul>
  <li>Fixes an issue affecting the Objective-C variants of <code class="language-plaintext highlighter-rouge">BrazeDelegate</code>, <code class="language-plaintext highlighter-rouge">BrazeContentCardUIViewControllerDelegate</code> and <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUIDelegate</code>.
    <ul>
      <li>When setting these delegates in Objective-C a second time, the delegate would end up being set to <code class="language-plaintext highlighter-rouge">nil</code>.</li>
      <li>This issue has been resolved and the delegates can now be set multiple times without issue.</li>
    </ul>
  </li>
</ul>

<h5 id="added-19">Added</h5>
<ul>
  <li>Adds support for delayed SDK initialization, allowing you to create the Braze instance outside of <code class="language-plaintext highlighter-rouge">application(_:didFinishLaunchingWithOptions:)</code>.
    <ul>
      <li>The SDK can now be initialized asynchronously, while conserving the ability to process incoming Braze push notifications.</li>
      <li>Symbol documentation: <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)"><code class="language-plaintext highlighter-rouge">Braze.prepareForDelayedInitialization(pushAutomation:)</code></a></li>
      <li>Integration documentation: <a href="https://braze.com/docs/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/"><em>Delayed Initialization</em></a></li>
      <li>Sample app: <a href="https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#pushnotifications-delayedinitialization"><em>PushNotifications-DelayedInitialization</em></a>.</li>
    </ul>
  </li>
  <li>Adds the ability to prevent showing an in-app message to a different user than the one that triggered the in-app message.
    <ul>
      <li>To enable this feature, set <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/preventinappmessagedisplayfordifferentuser"><code class="language-plaintext highlighter-rouge">Braze.Configuration.preventInAppMessageDisplayForDifferentUser</code></a> to <code class="language-plaintext highlighter-rouge">true</code> (default: <code class="language-plaintext highlighter-rouge">false</code>).</li>
    </ul>
  </li>
</ul>

<h2 id="1000">10.0.0</h2>

<h5 id="breaking-4">Breaking</h5>
<ul>
  <li>The following changes have been made when subscribing to Push events with <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)"><code class="language-plaintext highlighter-rouge">Braze.Notifications.subscribeToUpdates(payloadTypes:_:)</code></a>:
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">update</code> closure will now be triggered by both “Push Opened” and “Push Received” events by default. Previously, it would only be triggered by “Push Opened” events.
        <ul>
          <li>To continue subscribing only to “Push Opened” events, pass in <code class="language-plaintext highlighter-rouge">[.opened]</code> for the parameter <code class="language-plaintext highlighter-rouge">payloadTypes</code>. Alternatively, implement your <code class="language-plaintext highlighter-rouge">update</code> closure to check that the <code class="language-plaintext highlighter-rouge">type</code> from the <code class="language-plaintext highlighter-rouge">Braze.Notifications.Payload</code> is <code class="language-plaintext highlighter-rouge">.opened</code>.</li>
        </ul>
      </li>
      <li>When receiving a push notification with <code class="language-plaintext highlighter-rouge">content-available: true</code>, the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type"><code class="language-plaintext highlighter-rouge">Braze.Notifications.Payload.type</code></a> will now be <code class="language-plaintext highlighter-rouge">.received</code> instead of <code class="language-plaintext highlighter-rouge">.opened</code>.</li>
    </ul>
  </li>
  <li>Marks the following deprecated APIs as unavailable:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.Configuration.Api.Flavor</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.Configuration.Api.flavor</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.Configuration.Api.SdkMetadata</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.Configuration.Api.addSdkMetadata(_:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.ContentCard.ClickAction.uri(_:useWebview:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.ContentCard.ClickAction.uri</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.ClickAction.uri(_:useWebview:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.ClickAction.uri</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.ModalImage.imageUri</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.Full.imageUri</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.FullImage.imageUri</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.Themes.default</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.deviceId(queue:completion:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze._objc_deviceId(completion:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.deviceId()</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.User.setCustomAttributeArray(key:array:fileID:line:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.User.addToCustomAttributeArray(key:value:fileID:line:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.User._objc_addToCustomAttributeArray(key:value:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.User._objc_removeFromCustomAttributeArray(key:value:)</code></li>
      <li><code class="language-plaintext highlighter-rouge">gifViewProvider</code></li>
      <li><code class="language-plaintext highlighter-rouge">GifViewProvider.default</code></li>
    </ul>
  </li>
  <li>Removes the deprecated APIs:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.Configuration.DeviceProperty.pushDisplayOptions</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.InAppMessageRaw.Context.Error.extraProcessClickAction</code></li>
    </ul>
  </li>
  <li>Removes the deprecated <code class="language-plaintext highlighter-rouge">BrazeLocation</code> class in favor of <code class="language-plaintext highlighter-rouge">BrazeLocationProvider</code>.</li>
</ul>

<h5 id="fixed-28">Fixed</h5>
<ul>
  <li>Fixes a crash when handling a scheme-based deep link containing a registered <code class="language-plaintext highlighter-rouge">applink</code> domain (e.g. <code class="language-plaintext highlighter-rouge">applinks:example.com</code> with a deep link to <code class="language-plaintext highlighter-rouge">app://example.com/path</code>).</li>
</ul>

<h5 id="added-20">Added</h5>
<ul>
  <li>Adds support to subscribe to “Push Received” events via <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)"><code class="language-plaintext highlighter-rouge">Braze.Notifications.subscribeToUpdates(payloadTypes:_:)</code></a>.
    <ul>
      <li>The following notifications will trigger this subscription:
        <ul>
          <li>Notifications received in the foreground</li>
          <li>Notifications with the field <code class="language-plaintext highlighter-rouge">content-available: true</code> received in the foreground or background</li>
        </ul>
      </li>
      <li>The following notifications will <em>not</em> trigger this subscription:
        <ul>
          <li>Notifications received while terminated</li>
          <li>Notifications received in the background without the field <code class="language-plaintext highlighter-rouge">content-available: true</code></li>
        </ul>
      </li>
      <li>The new parameter <code class="language-plaintext highlighter-rouge">payloadTypes</code> will allow you to subscribe to “Push Opened” events, “Push Received” events, or both. If the parameter is omitted, it will subscribe to both by default.</li>
      <li>If you are using manual push integration, you will need to first implement <code class="language-plaintext highlighter-rouge">UNUserNotificationCenter.userNotificationCenter(_:willPresent:withCompletionHandler:)</code>, and make sure to call <code class="language-plaintext highlighter-rouge">Braze.Notifications.handleForegroundNotification(notification:)</code> within your implementation. Then, use <code class="language-plaintext highlighter-rouge">subscribeToUpdates</code> as noted above. See <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-3-enable-push-handling">our guide on push notification integration</a> for more info.</li>
    </ul>
  </li>
  <li>Adds the public property <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type"><code class="language-plaintext highlighter-rouge">Braze.Notifications.Payload.type</code></a>.</li>
  <li>Adds the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler/init(braze:)"><code class="language-plaintext highlighter-rouge">Braze.WebViewBridge.ScriptMessageHandler.init(braze:)</code></a> initializer enabling a simpler way to initialize the <code class="language-plaintext highlighter-rouge">ScriptMessageHandler</code> for adding it to user-provided web views.</li>
</ul>

<h2 id="931">9.3.1</h2>

<h5 id="fixed-29">Fixed</h5>
<ul>
  <li>Fixes an issue where the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:)"><code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.subscribeToUpdates(_:)</code></a> callback was not triggered at app launch when the cached feature flags matched the remote feature flags.</li>
  <li>Fixes an issue in Objective-C projects where the return value of <code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.jsonProperty(key:)</code> would incorrectly encode any entry value equal to <code class="language-plaintext highlighter-rouge">null</code> under certain conditions.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">[String: Any]</code> dictionaries returned by the Swift API will now drop <code class="language-plaintext highlighter-rouge">null</code> values.</li>
      <li><code class="language-plaintext highlighter-rouge">NSDictionary</code> objects returned by the Objective-C API will now encode <code class="language-plaintext highlighter-rouge">null</code> values as <code class="language-plaintext highlighter-rouge">NSNull</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="930">9.3.0</h2>

<h5 id="added-21">Added</h5>
<ul>
  <li>Adds Objective-C support for the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog"><code class="language-plaintext highlighter-rouge">BrazeInAppMessageUIDelegate.inAppMessage(_:prepareWith:)</code></a> method.
    <ul>
      <li>Customization of <code class="language-plaintext highlighter-rouge">ViewAttributes</code> via the <code class="language-plaintext highlighter-rouge">attributes</code> property is not available in the Objective-C version of <code class="language-plaintext highlighter-rouge">PresentationContextRaw</code>.</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.jsonProperty(key:type:decoder:)</code> to decode <code class="language-plaintext highlighter-rouge">jsonobject</code> type Feature Flag properties into custom <code class="language-plaintext highlighter-rouge">Decodable</code> types.</li>
  <li>Deprecates the existing Feature Flag APIs, to be removed in a future version:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.jsonStringProperty(key:)</code> has been deprecated.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.jsonObjectProperty(key:)</code> has been deprecated in favor of <code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.jsonProperty(key:)</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-30">Fixed</h5>
<ul>
  <li>Fixes an issue where the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/presentationcontext/preferredorientation"><code class="language-plaintext highlighter-rouge">preferredOrientation</code></a> on the presentation context of an in-app message would not be respected.</li>
</ul>

<h2 id="920">9.2.0</h2>

<h5 id="added-22">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">openNewWindowLinksInBrowser</code> configuration (default: <code class="language-plaintext highlighter-rouge">false</code>) to <code class="language-plaintext highlighter-rouge">Braze.ModalContext</code>.
    <ul>
      <li>Set this value in the <code class="language-plaintext highlighter-rouge">braze(_:willPresentModalWithContext:)</code> method of your <code class="language-plaintext highlighter-rouge">BrazeDelegate</code> to specify whether to launch the device browser to open web view hyperlinks that normally open a new tab or window.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-31">Fixed</h5>
<ul>
  <li>Fixes an issue with the automatic push integration feature that could cause the SDK not to send the device token to Braze.</li>
  <li>Fixes an issue that prevented external links, which open in a new tab, from being activated in presented web views.</li>
</ul>

<h2 id="910">9.1.0</h2>

<h5 id="added-23">Added</h5>
<ul>
  <li>Adds support for 3 new Feature Flag property types and various APIs for accessing them:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.timestampProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">Int</code> Unix millisecond timestamps.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.imageProperty(key:)</code> for accessing image URLs as <code class="language-plaintext highlighter-rouge">String</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.jsonObjectProperty(key:)</code> for accessing JSONs as <code class="language-plaintext highlighter-rouge">[String:Any]</code> dictionaries.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.FeatureFlag.jsonStringProperty(key:)</code> for accessing JSONs as <code class="language-plaintext highlighter-rouge">String</code>s.</li>
    </ul>
  </li>
  <li>Adds safeguards when reading the device model.</li>
</ul>

<h5 id="fixed-32">Fixed</h5>
<ul>
  <li>Fixes the duplicate symbols compilation errors and runtime warnings that may occur under specific conditions when integrating <code class="language-plaintext highlighter-rouge">BrazeKit</code> and either <code class="language-plaintext highlighter-rouge">BrazeNotificationService</code> or <code class="language-plaintext highlighter-rouge">BrazePushStory</code> via CocoaPods.</li>
</ul>

<h2 id="900">9.0.0</h2>

<h5 id="breaking-5">Breaking</h5>
<ul>
  <li>Removes the default privacy tracking domains from the <code class="language-plaintext highlighter-rouge">BrazeKit</code> privacy manifest.
    <ul>
      <li>If you are using the Braze <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/">data tracking features</a>, you will need to manually add your tracking endpoint to your app-level privacy manifest.</li>
      <li>Refer to the updated <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking">tutorial</a> for integration guidance.</li>
    </ul>
  </li>
  <li>Removes the deprecated <code class="language-plaintext highlighter-rouge">BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)</code> method in favor of <code class="language-plaintext highlighter-rouge">BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError)</code>.
    <ul>
      <li>This method was originally deprecated in <a href="https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.14.0">release <code class="language-plaintext highlighter-rouge">5.14.0</code></a>.</li>
      <li>Failing to switch to the new delegate method will not trigger a compiler error; instead, the <code class="language-plaintext highlighter-rouge">BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)</code> method you define will simply not be called.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-33">Fixed</h5>
<ul>
  <li>Adds the missing <code class="language-plaintext highlighter-rouge">NSPrivacyCollectedDataTypes</code> key to the <code class="language-plaintext highlighter-rouge">BrazePushStory</code> privacy manifest.</li>
</ul>

<h2 id="840">8.4.0</h2>

<h5 id="added-24">Added</h5>
<ul>
  <li>Expands Geofences behavior in the background while “When In Use” authorization is selected:
    <ul>
      <li>Adds the <code class="language-plaintext highlighter-rouge">Braze.Location.Configuration.allowBackgroundGeofenceUpdates</code> property to toggle whether geofences should be updated in the background.
        <ul>
          <li>When using this setting, verify that you have enabled the <em>Location updates</em> background mode.</li>
        </ul>
      </li>
      <li>Adds the <code class="language-plaintext highlighter-rouge">Braze.Location.Configuration.distanceFilter</code> property to configure the minimum distance sensitivity for triggering a location update.</li>
    </ul>
  </li>
  <li>Adds support for the <code class="language-plaintext highlighter-rouge">message_extras</code> Liquid tag for in-app messages.</li>
</ul>

<h2 id="830">8.3.0</h2>

<h5 id="added-25">Added</h5>
<ul>
  <li>Adds early access for a third alternative repository which provides all Braze modules as mergeable XCFrameworks. For instructions on how to leverage it, refer to the repository README:
    <ul>
      <li><a href="https://github.com/braze-inc/braze-swift-sdk-prebuilt-mergeable">braze-inc/braze-swift-sdk-prebuilt-mergeable</a></li>
    </ul>
  </li>
</ul>

<h5 id="fixed-34">Fixed</h5>
<ul>
  <li>Adds a missing privacy manifest for <code class="language-plaintext highlighter-rouge">BrazePushStory</code>.</li>
  <li>Fixes an invalid privacy manifest warning in <code class="language-plaintext highlighter-rouge">BrazeLocation</code> when submitting to the App Store as a dynamic XCFramework.</li>
  <li>Fixes an issue where already enqueued in-app messages would not be removed from the stack after subsequent <code class="language-plaintext highlighter-rouge">.reenqueue</code> and <code class="language-plaintext highlighter-rouge">.discard</code> display actions.</li>
  <li>Fixes an issue preventing retried requests from using an updated SDK authentication token until a new request was scheduled for processing.</li>
  <li>Purchases, custom events, and nested custom user attributes can now include properties with values of any type conforming to <a href="https://developer.apple.com/documentation/swift/binaryinteger"><code class="language-plaintext highlighter-rouge">BinaryInteger</code></a> (<code class="language-plaintext highlighter-rouge">Int64</code>, <code class="language-plaintext highlighter-rouge">UInt16</code>, etc).
    <ul>
      <li>All values will be cast to <code class="language-plaintext highlighter-rouge">Int</code> before being logged.</li>
      <li>This resolves an issue with a bugfix in <code class="language-plaintext highlighter-rouge">7.6.0</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="821">8.2.1</h2>

<h5 id="fixed-35">Fixed</h5>
<ul>
  <li>Fixes App Store validation issues when archiving with Xcode 15.3.</li>
</ul>

<h2 id="820">8.2.0</h2>

<h5 id="added-26">Added</h5>
<ul>
  <li>Adds support for remotely starting Live Activities via push notifications.
    <ul>
      <li>Adds the following methods to the <code class="language-plaintext highlighter-rouge">liveActivities</code> module:
        <ul>
          <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)"><code class="language-plaintext highlighter-rouge">registerPushToStart(forType:name:) -&gt; Task&lt;Void, Never&gt;</code></a></li>
          <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/optoutpushtostart(type:)"><code class="language-plaintext highlighter-rouge">optOutPushToStart(type:)</code></a></li>
        </ul>
      </li>
      <li>This feature requires iOS 17.2 or higher.</li>
      <li>For usage details, refer to the updated Live Activities tutorial <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b4-live-activities/">here</a>.</li>
    </ul>
  </li>
  <li>Adds return values for existing <code class="language-plaintext highlighter-rouge">liveActivities</code> methods:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">launchActivity(pushTokenTag:activity:)</code> now returns a discardable <code class="language-plaintext highlighter-rouge">Task&lt;Void, Never&gt;?</code>.</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">pushToStartTokens</code> as a new <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty">tracking property</a> type.</li>
</ul>

<h2 id="810">8.1.0</h2>

<h5 id="added-27">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">is_test_send</code> boolean value in the in-app message JSON representation.</li>
  <li>Adds the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/subscribetosessionupdates(_:)"><code class="language-plaintext highlighter-rouge">Braze.subscribeToSessionUpdates(_:)</code></a> method and <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream"><code class="language-plaintext highlighter-rouge">Braze.sessionUpdatesStream</code></a> property to subscribe to the session updates events generated by the SDK.</li>
  <li>Adds public APIs to access <code class="language-plaintext highlighter-rouge">BrazeKit</code>, <code class="language-plaintext highlighter-rouge">BrazeLocation</code> and <code class="language-plaintext highlighter-rouge">BrazeUI</code> resources bundles:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.Resources.bundle</code></li>
      <li><code class="language-plaintext highlighter-rouge">BrazeLocationResources.bundle</code></li>
      <li><code class="language-plaintext highlighter-rouge">BrazeUIResources.bundle</code></li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">BrazeKit.overrideResourceBundle</code> and <code class="language-plaintext highlighter-rouge">BrazeUI.overrideResourceBundle</code> have been deprecated in favor of <code class="language-plaintext highlighter-rouge">BrazeKit.overrideResourcesBundle</code> and <code class="language-plaintext highlighter-rouge">BrazeUI.overrideResourcesBundle</code>.</li>
  <li>Re-enables visionOS sample apps requiring SDWebImage in <code class="language-plaintext highlighter-rouge">Examples-CocoaPods.xcworkspace</code>. SDWebImage for visionOS is now supported when using CocoaPods.</li>
  <li>Updated SDWebImage dependency in <code class="language-plaintext highlighter-rouge">BrazeUICompat</code> to <code class="language-plaintext highlighter-rouge">5.19.0+</code>.</li>
</ul>

<h5 id="fixed-36">Fixed</h5>
<ul>
  <li>Fixes multiple issues on visionOS:
    <ul>
      <li>Sessions now properly start as expected.</li>
      <li>The click behavior <em>Open Web URL Inside App</em> now properly opens the URL in a modal web view. Previously, the URL would always be opened using the default web browser.</li>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/targetscene">Braze.Notifications.Payload.targetScene</a> is now defined.</li>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/urlcontext/targetscene">Braze.URLContext.targetScene</a> is now properly set by the SDK for in-app messages click actions.</li>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewbridge/scriptmessagehandler/init(logclick:logerror:shownewsfeed:closemessage:braze:)-p2ki">Braze.WebViewBridge.ScriptMessageHandler.init(logClick:logError:showNewsFeed:closeMessage:braze:)</a> is now defined.</li>
      <li>[BrazeDelegate.braze(<em>:willPresentModalWithContext:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(</em>:willpresentmodalwithcontext:)-1fj41) now has a default implementation.</li>
      <li>Handling network requests and persisting data properly extend the lifetime of the application for processing.</li>
    </ul>
  </li>
</ul>

<h2 id="801">8.0.1</h2>

<h5 id="fixed-37">Fixed</h5>
<ul>
  <li>Fixes the reported SDK version, see <a href="#800">8.0.0</a>.</li>
  <li>Removes crash data from the <code class="language-plaintext highlighter-rouge">BrazeKit</code> privacy manifest. This data type is not collected by Braze.</li>
</ul>

<h2 id="800">8.0.0</h2>

<h5 id="️-warning">⚠️ Warning</h5>
<ul>
  <li>This release reports the SDK version as <code class="language-plaintext highlighter-rouge">7.7.0</code> instead of <code class="language-plaintext highlighter-rouge">8.0.0</code>.</li>
</ul>

<h5 id="breaking-6">Breaking</h5>
<ul>
  <li>Compiles the SDK using Xcode version 15.2 (15C500b).
    <ul>
      <li>This also raises the minimum deployment targets to iOS 12.0 and tvOS 12.0.</li>
    </ul>
  </li>
  <li>The <code class="language-plaintext highlighter-rouge">BrazeLocation</code> class is now marked as unavailable. It was previously deprecated in favor of <code class="language-plaintext highlighter-rouge">BrazeLocationProvider</code> in 5.8.1.</li>
</ul>

<h5 id="added-28">Added</h5>
<ul>
  <li>Adds support for visionOS 1.0.
    <ul>
      <li>⚠️ Rich push notifications and Push Stories may not display as expected on visionOS 1.0. We are monitoring the latest versions for potential fixes.</li>
      <li>⚠️ CocoaPods is not yet supported by SDWebImage for visionOS. visionOS sample apps requiring SDWebImage have been disabled in the <code class="language-plaintext highlighter-rouge">Examples-CocoaPods.xcworkspace</code>. Refer to the SwiftPM or manual integration Xcode project instead.</li>
    </ul>
  </li>
</ul>

<h2 id="770">7.7.0</h2>

<h5 id="added-29">Added</h5>
<ul>
  <li>Updates the prebuilt release assets to include the privacy manifest for manual integrations of SDWebImage.
    <ul>
      <li>Follow the <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration/?tab=static">manual integration guide</a> to add the <code class="language-plaintext highlighter-rouge">SDWebImage.bundle</code> to your project for static XCFrameworks.</li>
    </ul>
  </li>
  <li>Enhances support for language localizations.
    <ul>
      <li>Introduces a localization for Azerbaijani strings.</li>
      <li>Updates Ukrainian localization strings for accuracy.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-38">Fixed</h5>
<ul>
  <li>Fixes the default button placement for full in-app message views.</li>
  <li>Fixes an issue where setting <code class="language-plaintext highlighter-rouge">Braze.Configuration.Api.endpoint</code> to a URL with invalid characters could cause a crash.
    <ul>
      <li>If the SDK is given an invalid endpoint, it will no longer attempt to make network requests and will instead log an error.</li>
    </ul>
  </li>
  <li>Fixes an issue preventing <code class="language-plaintext highlighter-rouge">BrazeLocation</code> from working correctly when using the dynamic XCFrameworks.</li>
</ul>

<h2 id="760">7.6.0</h2>

<h5 id="added-30">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">Braze.InAppMessage.Data.isTestSend</code> property, which indicates whether an in-app message was triggered as part of a test send.</li>
  <li>Adds logic to separate Braze data into tracking and non-tracking requests.
    <ul>
      <li>Adds the following methods to set and edit the allow list for properties that will be used for tracking:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">Braze.Configuration.Api.trackingPropertyAllowList</code>: Set the initial allow list before initializing Braze.</li>
          <li><code class="language-plaintext highlighter-rouge">Braze.updateTrackingAllowList(adding:removing:)</code>: Update the existing allow list during runtime.</li>
        </ul>
      </li>
      <li>For full usage details on these configurations, refer to our tutorial <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/">here</a>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-39">Fixed</h5>
<ul>
  <li>Adds safeguards to prevent a rare race condition occuring in the SDK network layer.</li>
  <li>Prevents in-app message test sends from attempting re-display after being discarded by a custom in-app message UI delegate.</li>
  <li>Fixes an issue in the default Braze in-app message UI where some messages were not being removed from the stack after display.</li>
  <li>Fixes the compilation of <code class="language-plaintext highlighter-rouge">BrazeKitCompat</code> and <code class="language-plaintext highlighter-rouge">BrazeUICompat</code> in Objective-C++ projects.</li>
  <li>Fixes an issue in <code class="language-plaintext highlighter-rouge">BrazeUICompat</code> where the header text in Full or Modal in-app messages would be duplicated in place of the body text under certain conditions.</li>
  <li>Fixes the encoding of values of types <code class="language-plaintext highlighter-rouge">Float</code>, <code class="language-plaintext highlighter-rouge">Int8</code>, <code class="language-plaintext highlighter-rouge">Int16</code>, <code class="language-plaintext highlighter-rouge">Int32</code>, <code class="language-plaintext highlighter-rouge">Int64</code>, <code class="language-plaintext highlighter-rouge">UInt</code>, <code class="language-plaintext highlighter-rouge">UInt8</code>, <code class="language-plaintext highlighter-rouge">UInt16</code>, <code class="language-plaintext highlighter-rouge">UInt32</code> and <code class="language-plaintext highlighter-rouge">UInt64</code>. Those types were previously not supported in custom events and purchase properties.</li>
  <li>Fixes an issue preventing purchase events from being logged when the product identifier has a leading dollar sign.</li>
  <li>Fixes an issue preventing custom attributes from being logged when the attribute key has a leading dollar sign.</li>
</ul>

<h2 id="750">7.5.0</h2>

<h5 id="added-31">Added</h5>
<ul>
  <li>Adds privacy manifests for <code class="language-plaintext highlighter-rouge">BrazeKit</code> and <code class="language-plaintext highlighter-rouge">BrazeLocation</code> to describe Braze’s data collection policies. For more details, refer to <a href="https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests">Apple’s documentation</a> on privacy manifests.
    <ul>
      <li>More fine-tuned configurations to manage your data collection practices will be made available in a future release.</li>
    </ul>
  </li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">optInWhenPushAuthorized</code> configuration property to specify whether a user’s notification subscription state should automatically be set to <code class="language-plaintext highlighter-rouge">optedIn</code> when updating push permissions to authorized.</li>
  <li>The WebKit Inspector developer tool is now enabled by default for all instances of <code class="language-plaintext highlighter-rouge">BrazeInAppMessagesUI.HtmlView</code>. It can be disabled by setting <code class="language-plaintext highlighter-rouge">BrazeInAppMessagesUI.HtmlView.Attributes.allowInspector</code> to <code class="language-plaintext highlighter-rouge">false</code>.</li>
</ul>

<h5 id="fixed-40">Fixed</h5>
<ul>
  <li>Fixes an issue with the code signatures of XCFrameworks introduced in <code class="language-plaintext highlighter-rouge">7.1.0</code>.</li>
  <li>Fixes a crash on tvOS devices running versions below 16.0, caused by the absence of the <code class="language-plaintext highlighter-rouge">UIApplication.openNotificationSettingsURLString</code> symbol in those OS versions.</li>
  <li>Fixes an issue where a content card would not display if the value under “Redirect to Web URL” was an empty string.</li>
  <li>Fixes incorrect behavior in BrazeUI where tapping the body of a <code class="language-plaintext highlighter-rouge">Full</code> or <code class="language-plaintext highlighter-rouge">Modal</code> in-app message with buttons and an “Image Only” layout would dismiss that message and process the button’s click action.
    <ul>
      <li>Tapping the body will now be a no-op, bringing parity with other platforms.</li>
    </ul>
  </li>
</ul>

<h2 id="740">7.4.0</h2>

<h5 id="added-32">Added</h5>
<ul>
  <li>Adds two alternative repositories to support specialized integration options. For instructions on how to leverage them, refer to their respective READMEs:
    <ul>
      <li><a href="https://github.com/braze-inc/braze-swift-sdk-prebuilt-static">braze-inc/braze-swift-sdk-prebuilt-static</a> which provides all Braze modules as static XCFrameworks.</li>
      <li><a href="https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic">braze-inc/braze-swift-sdk-prebuilt-dynamic</a> which provides all Braze modules as dynamic XCFrameworks.</li>
    </ul>
  </li>
  <li>In-App Message assets from URLs containing the query parameter <code class="language-plaintext highlighter-rouge">cache=false</code> will not be prefetched.
    <ul>
      <li>Additionally, when presented as a part of In-App Messages or Content Cards, those URLs will be fetched using the <a href="https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy/reloadignoringlocalandremotecachedata"><code class="language-plaintext highlighter-rouge">URLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData</code></a> caching policy, which always requests a fresh version from the source and ignores any cached versions.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-41">Fixed</h5>
<ul>
  <li>Fixes XCFrameworks headers to use the <code class="language-plaintext highlighter-rouge">#import</code> syntax instead of <code class="language-plaintext highlighter-rouge">@import</code> for compatibility with Objective-C++ contexts.</li>
  <li>Fixes the push token tag validation during Live Activity registration, accepting strings up to 256 bytes instead of 255 bytes.</li>
  <li><code class="language-plaintext highlighter-rouge">Braze.ContentCards.unviewedCards</code> no longer includes Control cards to bring parity with Android and Web.</li>
  <li>Fixes an Objective-C metaclass crash that occurs when initializing a custom subclass of certain BrazeUI views.</li>
</ul>

<h2 id="730">7.3.0</h2>

<h5 id="added-33">Added</h5>
<ul>
  <li>Adds support for Expo Notifications <a href="https://docs.expo.dev/versions/latest/sdk/notifications/#notification-events-listeners">event listeners</a> when using the automatic push integration.</li>
</ul>

<h5 id="fixed-42">Fixed</h5>
<ul>
  <li>Fixes a rare concurrency issue that might result in duplicated events when logging large amount of events.</li>
  <li>Fixes an issue where <code class="language-plaintext highlighter-rouge">user.set(dateOfBirth:)</code> was not setting the date of birth accurately due to variations in the device’s timezone.</li>
</ul>

<h2 id="720">7.2.0</h2>

<h5 id="added-34">Added</h5>
<ul>
  <li>Exposes the <code class="language-plaintext highlighter-rouge">BrazePushStory.NotificationViewController.didReceive</code> methods for custom handling of push story notification events.</li>
</ul>

<h5 id="fixed-43">Fixed</h5>
<ul>
  <li>Resolves an issue for in-app messages with buttons where tapping on the body would incorrectly execute the button’s click action.
    <ul>
      <li>Now, when you tap on the body of an in-app message with buttons, no event should occur.</li>
    </ul>
  </li>
  <li>Resolves a potential deadlock under rare circumstances in BrazeUI’s In-App messages presentation.</li>
  <li>Fixes the default implementation for the Objective-C representation of <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:shouldprocess:buttonid:message:view:)-7lvld"><code class="language-plaintext highlighter-rouge">BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:url:buttonId:message:view:)</code></a> to return the proper click action URL.</li>
  <li>Resolves an issue where the body of the modal in-app message may be displayed stretched on some device models.</li>
  <li>Resolves an issue where <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI</code> could fail to detect the correct application window for presenting its post-click webview.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI</code> now prefers using the current key <code class="language-plaintext highlighter-rouge">UIWindow</code> instead of the first one in the application’s window stack.</li>
    </ul>
  </li>
</ul>

<h5 id="removed">Removed</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">Braze.Configuration.DeviceProperty.pushDisplayOptions</code> has been deprecated. Providing this value no longer has an effect.</li>
</ul>

<h2 id="710">7.1.0</h2>

<h5 id="fixed-44">Fixed</h5>
<ul>
  <li>Resolves an issue preventing templated in-app messages from triggering if a previous attempt to display the message failed within the same session.</li>
  <li>Fixes an issue that prevented custom events and nested custom attributes from logging if had a property with a value that was prefixed with a <code class="language-plaintext highlighter-rouge">$</code>.</li>
  <li>Fixes a bug in the Content Cards feed UI where the empty feed message would not display when the user only had control cards in their feed.</li>
  <li>Adds additional safeguards when reading the device model.</li>
</ul>

<h5 id="added-35">Added</h5>
<ul>
  <li>Adds a code signature to all XCFrameworks in the Braze Swift SDK, signed by <code class="language-plaintext highlighter-rouge">Braze, Inc.</code>.</li>
  <li><code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI.DisplayChoice.later</code> has been deprecated in favor of <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI.DisplayChoice.reenqueue</code>.</li>
</ul>

<h2 id="700">7.0.0</h2>

<h5 id="breaking-7">Breaking</h5>
<ul>
  <li>The <code class="language-plaintext highlighter-rouge">useUUIDAsDeviceId</code> configuration is now enabled by default.
    <ul>
      <li>For more details on the impacts, refer to this <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/">Collecting IDFV - Swift</a>.</li>
    </ul>
  </li>
  <li>The <code class="language-plaintext highlighter-rouge">Banner</code> Content Card type and corresponding UI elements have been renamed to <code class="language-plaintext highlighter-rouge">ImageOnly</code>. All member methods and properties remain the same.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.ContentCard.Banner</code> → <code class="language-plaintext highlighter-rouge">Braze.ContentCard.ImageOnly</code></li>
      <li><code class="language-plaintext highlighter-rouge">BrazeContentCardUI.BannerCell</code> → <code class="language-plaintext highlighter-rouge">BrazeContentCardUI.ImageOnlyCell</code></li>
    </ul>
  </li>
  <li>Refactors some text layout logic in BrazeUI into a new <code class="language-plaintext highlighter-rouge">Braze.ModalTextView</code> class.</li>
  <li>Updates the behavior for Feature Flags methods.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">FeatureFlags.featureFlag(id:)</code> now returns <code class="language-plaintext highlighter-rouge">nil</code> for an ID that does not exist.</li>
      <li><code class="language-plaintext highlighter-rouge">FeatureFlags.subscribeToUpdates(:)</code> will trigger the callback when any refresh request completes with a success or failure.
        <ul>
          <li>The callback will also trigger immediately upon initial subscription if previously cached data exists from the current session.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h5 id="fixed-45">Fixed</h5>
<ul>
  <li>Fixes compiler warnings about Swift 6 when compiling <code class="language-plaintext highlighter-rouge">BrazeUI</code> while using Xcode 15.</li>
  <li>Exposes public imports for <code class="language-plaintext highlighter-rouge">ABKClassicImageContentCardCell.h</code> and <code class="language-plaintext highlighter-rouge">ABKControlTableViewCell.h</code> for use in the BrazeUICompat layer.</li>
  <li>Adds additional safeguards around invalid constraint values for <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI.SlideupView</code>.</li>
  <li>Resolves a Content Cards feed UI issue displaying a placeholder image in Classic cards without an attached image.</li>
</ul>

<h5 id="added-36">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">enableDarkTheme</code> property to <code class="language-plaintext highlighter-rouge">BrazeContentCardUI.ViewController.Attributes</code>.
    <ul>
      <li>Set this field to <code class="language-plaintext highlighter-rouge">false</code> to prevent the Content Cards feed UI from adopting dark theme styling when the device is in dark mode.</li>
      <li>This field is <code class="language-plaintext highlighter-rouge">true</code> by default.</li>
    </ul>
  </li>
</ul>

<h2 id="662">6.6.2</h2>

<h5 id="fixed-46">Fixed</h5>
<ul>
  <li>Fixes an issue preventing purchase events from being logged when the product identifier has a leading dollar sign ($).</li>
  <li>Fixes an issue preventing custom attributes from being logged when the attribute key has a leading dollar sign ($).</li>
</ul>

<h2 id="661">6.6.1</h2>

<h5 id="fixed-47">Fixed</h5>
<ul>
  <li>Fixes a crash in the geofences feature that could occur when the number of monitored regions exceeded the maximum count.</li>
  <li>Fixes an issue introduced in <code class="language-plaintext highlighter-rouge">6.3.1</code> that would always update a user’s push subscription status to <code class="language-plaintext highlighter-rouge">optedIn</code> on app launch if push permissions were authorized on the device settings.
    <ul>
      <li>The SDK now will only send the subscription status at app launch if the device notification settings goes from denied to authorized.</li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">Braze.ContentCard.logClick(using braze: Braze)</code> will now log a click regardless of whether the <code class="language-plaintext highlighter-rouge">ContentCard</code> has a <code class="language-plaintext highlighter-rouge">ClickAction</code>.
    <ul>
      <li>This behavior differs from the default API <code class="language-plaintext highlighter-rouge">Braze.ContentCard.Context.logClick()</code>, which has the safeguard of requiring a <code class="language-plaintext highlighter-rouge">ClickAction</code> to log a click.</li>
    </ul>
  </li>
</ul>

<h2 id="660">6.6.0</h2>

<h5 id="fixed-48">Fixed</h5>
<ul>
  <li>Fixes an issue in HTML in-app messages where custom event and purchase properties would always convert values for <code class="language-plaintext highlighter-rouge">1</code> and <code class="language-plaintext highlighter-rouge">0</code> to become <code class="language-plaintext highlighter-rouge">true</code> and <code class="language-plaintext highlighter-rouge">false</code>, respectively.
    <ul>
      <li>These property values will now respect their original form in the HTML.</li>
    </ul>
  </li>
  <li>Prevents the default Braze UI from displaying in-app messages underneath the keyboard when Stage Manager is in use.</li>
</ul>

<h5 id="added-37">Added</h5>
<ul>
  <li>Adds the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/logfeatureflagimpression(id:)"><code class="language-plaintext highlighter-rouge">Braze.FeatureFlags.logFeatureFlagImpression(id: String)</code></a> method.</li>
  <li>Adds the optional <code class="language-plaintext highlighter-rouge">merge</code> parameter to the Objective-C representation of the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/setcustomattribute(key:dictionary:merge:fileid:line:)"><code class="language-plaintext highlighter-rouge">setCustomAttribute(key:dictionary:merge:)</code></a> method.</li>
</ul>

<h2 id="650">6.5.0</h2>

<h5 id="fixed-49">Fixed</h5>
<ul>
  <li>Content card impressions can now be logged any number of times on a single card, bringing parity with Android and Web.
    <ul>
      <li>This removes the limit introduced in 6.3.1 where a card impression could only be logged once per session.</li>
      <li>In the Braze-provided Content Cards feed UI, impressions will be logged once per feed instance.</li>
    </ul>
  </li>
</ul>

<h5 id="added-38">Added</h5>
<ul>
  <li>Adds a simplified method for integrating push notification support into your application:
    <ul>
      <li>Automatic push integration can be enabled by setting <code class="language-plaintext highlighter-rouge">configuration.push.automation = true</code> on your configuration object.
        <ul>
          <li>This eliminates the need for the manual push integration outlined in the <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications#Option-2-Implement-the-push-notification-handlers-manually"><em>Implement the push notification handlers manually</em></a> tutorial section.</li>
          <li>When enabled, the SDK will automatically implement the necessary system delegate methods for handling push notifications.</li>
          <li>Compatibility with other push providers, whether first or third party, is maintained. The SDK will automatically handle only Braze push notifications, while original system delegate methods will be executed for all other push notifications.</li>
        </ul>
      </li>
      <li>Each automation step can be independently enabled or disabled. For example, <code class="language-plaintext highlighter-rouge">configuration.push.automation.requestAuthorizationAtLaunch = false</code> can be used to prevent the automatic request for push permissions at launch.</li>
      <li>Resources:
        <ul>
          <li>Updated <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b1-standard-push-notifications"><em>Standard Push Notifications</em></a> tutorial.</li>
          <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.property"><code class="language-plaintext highlighter-rouge">Braze.Configuration.Push.automation</code></a> property.</li>
          <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class"><code class="language-plaintext highlighter-rouge">Braze.Configuration.Push.Automation</code></a> type (provides details about the behavior of each automation step).</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Adds the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks"><code class="language-plaintext highlighter-rouge">Braze.Configuration.forwardUniversalLinks</code></a> configuration. When enabled, the SDK will redirect universal links from Braze campaigns to the appropriate system methods.</li>
  <li>Adds the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(_:)"><code class="language-plaintext highlighter-rouge">Braze.Notifications.subscribeToUpdates(_:)</code></a> method to subscribe to the push notifications handled by the SDK.
    <ul>
      <li>This method runs the provided closure with a <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload"><code class="language-plaintext highlighter-rouge">Braze.Notifications.Payload</code></a> class representing the processed push notification.</li>
    </ul>
  </li>
  <li>Adds the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/devicetoken"><code class="language-plaintext highlighter-rouge">Braze.Notifications.deviceToken</code></a> property to access the most recent notification device token received by the SDK.</li>
</ul>

<h2 id="640">6.4.0</h2>

<h5 id="fixed-50">Fixed</h5>
<ul>
  <li>Fixes an issue preventing text fields from being selected in HTML IAMs for iOS 15.</li>
  <li>Fixes an issue where the device model was inaccurately reported as iPad on macOS (<em>Mac Catalyst</em> and <em>Designed for iPad</em> configurations).</li>
  <li>Fixes an issue where custom event and purchase properties would not accept an entry if its value was an empty string.</li>
  <li>Fixes a crash that occurred in the default UI for Content Cards when encountering a zero-value aspect ratio.</li>
  <li>Fixes an issue introduced in 6.0.0 where images in in-app messages would appear smaller than expected when using the compatibility UI (<code class="language-plaintext highlighter-rouge">BrazeUICompat</code>).</li>
</ul>

<h5 id="added-39">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">unviewedCards</code> convenience property to the <code class="language-plaintext highlighter-rouge">Braze.ContentCards</code> class to get the unviewed content cards for the current user.</li>
</ul>

<h2 id="631">6.3.1</h2>

<h5 id="fixed-51">Fixed</h5>
<ul>
  <li>Fixes an issue where the previous user’s data would not be flushed after calling <code class="language-plaintext highlighter-rouge">changeUser(userId:sdkAuthSignature:)</code> when the SDK authentication feature is enabled.</li>
  <li>A content card impression can now be logged once per session. Previously, the Braze-provided Content Cards UI would limit to a single impression per card at maximum, irrespective of sessions.</li>
  <li>Fixes an issue that previously caused push notification URLs with percent-encoded characters to fail during decoding.</li>
  <li>Fixes a behavior to automatically set a user’s push subscription state to <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/subscriptionstate/optedin"><code class="language-plaintext highlighter-rouge">optedIn</code></a> after push permissions have explicitly been authorized via the Settings app.</li>
  <li>Correctly hides shadows on in-app messages that are configured with a transparent background.</li>
  <li>Fixes a rare crash occurring when deinitializing the Braze instance.</li>
</ul>

<h5 id="added-40">Added</h5>
<ul>
  <li>Adds additional logging for network-related decoding errors.</li>
</ul>

<h2 id="630">6.3.0</h2>

<h5 id="fixed-52">Fixed</h5>
<ul>
  <li>“Confirm” and “Cancel” notification categories now show the correct titles on the action buttons.</li>
</ul>

<h5 id="added-41">Added</h5>
<ul>
  <li>Adds a new <code class="language-plaintext highlighter-rouge">SDKMetadata</code> option <code class="language-plaintext highlighter-rouge">.reactnativenewarch</code> for the React Native New Architecture.</li>
  <li>Adds public initializers for <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/urlcontext/"><code class="language-plaintext highlighter-rouge">Braze.URLContext</code></a> and <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/modalcontext/"><code class="language-plaintext highlighter-rouge">Braze.ModalContext</code></a>.</li>
</ul>

<h2 id="620">6.2.0</h2>

<h5 id="fixed-53">Fixed</h5>
<ul>
  <li>Fixes a crash introduced in 6.0.0 when displaying an HTML in-app message using the <code class="language-plaintext highlighter-rouge">BrazeUICompat</code> module.</li>
  <li>Removed a system call that is known to be slow on older versions of macOS. This resolves the SDK hanging during initialization on Mac Catalyst when running on affected macOS versions.</li>
</ul>

<h5 id="added-42">Added</h5>
<ul>
  <li>Adds support for <code class="language-plaintext highlighter-rouge">target</code> attributes on anchor tags in HTML in-app messages (e.g. <code class="language-plaintext highlighter-rouge">&lt;a href="..." target="_blank"&gt;&lt;/a&gt;</code>).
    <ul>
      <li>Adding the <code class="language-plaintext highlighter-rouge">target</code> attribute to links will allow them to open in a new webview without dismissing the current in-app message.</li>
      <li>This behavior can be disabled via the <code class="language-plaintext highlighter-rouge">linkTargetSupport</code> property of the <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI.HtmlView.Attributes</code> struct.</li>
      <li>See our <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/">Custom HTML in-app messages</a> documentation page for more details.</li>
    </ul>
  </li>
</ul>

<h2 id="610">6.1.0</h2>

<h5 id="fixed-54">Fixed</h5>
<ul>
  <li>Fixes an issue that led to disproportionately large close buttons on in-app messages when the user has set a large font size in the device settings.</li>
  <li>Fixes an issue that would lock the screen in a specific orientation after the dismissal of an in-app message customized to be presented in that orientation.
    <ul>
      <li>This issue only impacted iOS 16.0+ devices.</li>
    </ul>
  </li>
</ul>

<h5 id="added-43">Added</h5>
<ul>
  <li>Adds new versions of <code class="language-plaintext highlighter-rouge">setCustomAttribute</code> to the User object to support <a href="https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support">nested custom attributes</a>.
    <ul>
      <li>Renames <code class="language-plaintext highlighter-rouge">User.setCustomAttributeArray(key: String, array: [String]?)</code> to <code class="language-plaintext highlighter-rouge">setCustomAttribute(…)</code> to align it with other custom attribute setters, and adds “string” to the <code class="language-plaintext highlighter-rouge">addTo</code> and <code class="language-plaintext highlighter-rouge">removeFrom</code> attribute array methods to clarify which custom attributes they’re used for.</li>
    </ul>
  </li>
</ul>

<h2 id="600">6.0.0</h2>

<h5 id="breaking-8">Breaking</h5>
<ul>
  <li>The in-app message data models sent to <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)"><code class="language-plaintext highlighter-rouge">BrazeInAppMessagePresenter.present(message:)</code></a> now contain remote asset URLs. Previously, these data models would contain local asset URLs.
    <ul>
      <li>This change is only breaking in two situations:
        <ul>
          <li>When implementing a custom <code class="language-plaintext highlighter-rouge">BrazeInAppMessagePresenter</code>.</li>
          <li>When relying on asset URLs being local in the message provided by <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb"><code class="language-plaintext highlighter-rouge">BrazeInAppMessageUIDelegate.inAppMessage(_:displayChoiceForMessage:)</code></a></li>
        </ul>
      </li>
      <li>The in-app message data models available from the other <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate"><code class="language-plaintext highlighter-rouge">BrazeInAppMessageUIDelegate</code></a> methods remain unchanged and contain local asset URLs.</li>
    </ul>
  </li>
</ul>

<h5 id="added-44">Added</h5>
<ul>
  <li>The in-app message context now provides two additional methods:
    <ul>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessageraw/context-swift.class/getlocalassets(urls:destinationurl:completionhandler:)"><code class="language-plaintext highlighter-rouge">getLocalAssets(urls:destinationURL:completionHandler:)</code></a>: Retrieves the local assets associated with the given remote asset URLs.</li>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessageraw/context-swift.class/withlocalassets(message:destinationurl:completionhandler:)"><code class="language-plaintext highlighter-rouge">withLocalAssets(message:destinationURL:completionHandler:)</code></a>: Returns a modified in-app message with all remote asset URLs replaced with local ones.</li>
    </ul>
  </li>
</ul>

<h2 id="5140">5.14.0</h2>

<h5 id="fixed-55">Fixed</h5>
<ul>
  <li>VoiceOver now correctly focuses on in-app message views when they are presented.</li>
  <li>Fixes an issue causing in-app messages with re-eligibility disabled to display multiple times under certain conditions.</li>
  <li>Fixes an issue where modal and full in-app message headers were truncated on devices running iOS versions lower than 16 when displaying non-ASCII characters.</li>
  <li>The dynamic variant of <code class="language-plaintext highlighter-rouge">BrazeUI.framework</code> in the release artifact <code class="language-plaintext highlighter-rouge">braze-swift-sdk-prebuilt.zip</code> is now an actual dynamic framework. Previously, this specific framework was mistakenly distributed as a static framework.</li>
</ul>

<h5 id="added-45">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">BrazeSDKAuthDelegate</code> protocol as a separate protocol from <code class="language-plaintext highlighter-rouge">BrazeDelegate</code>, allowing for more flexible integrations.
    <ul>
      <li>Apps implementing <code class="language-plaintext highlighter-rouge">BrazeDelegate.braze(_:sdkAuthenticationFailedWithError:)</code> should migrate to use <code class="language-plaintext highlighter-rouge">BrazeSDKAuthDelegate</code> and remove the old implementation. The <code class="language-plaintext highlighter-rouge">BrazeDelegate</code> method will be removed in a future major release.</li>
    </ul>
  </li>
</ul>

<h2 id="5130">5.13.0</h2>

<h5 id="fixed-56">Fixed</h5>
<ul>
  <li>Fixes an issue where the SDK would automatically track body clicks on non-legacy HTML in-app messages.</li>
</ul>

<h5 id="added-46">Added</h5>
<ul>
  <li>Adds the synchronous <code class="language-plaintext highlighter-rouge">deviceId</code> property on the Braze instance.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">deviceId(queue:completion:)</code> is now deprecated.</li>
      <li><code class="language-plaintext highlighter-rouge">deviceId() async</code> is now deprecated.</li>
    </ul>
  </li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">automaticBodyClicks</code> property to the HTML in-app message view attributes. This property can be used to enable automatic body clicks tracking on non-legacy HTML in-app messages.
    <ul>
      <li>This property is <code class="language-plaintext highlighter-rouge">false</code> by default.</li>
      <li>This property is ignored for legacy HTML in-app messages.</li>
    </ul>
  </li>
</ul>

<h2 id="5120">5.12.0</h2>

<blockquote>
  <p>Starting with this release, this SDK will use <a href="https://semver.org/">Semantic Versioning</a>.</p>
</blockquote>

<h5 id="added-47">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">json()</code> and <code class="language-plaintext highlighter-rouge">decoding(json:)</code> public methods to the Feature Flag model object for JSON encoding/decoding.</li>
</ul>

<h2 id="5112">5.11.2</h2>

<h5 id="fixed-57">Fixed</h5>
<ul>
  <li>Fixes a crash occurring when the SDK is configured with a flush interval of <code class="language-plaintext highlighter-rouge">0</code> and network connectivity is poor.</li>
</ul>

<h2 id="5111">5.11.1</h2>

<h5 id="fixed-58">Fixed</h5>
<ul>
  <li>Fixes an issue preventing the correct calculation of the delay when retrying failed requests. This led to a more aggressive retry schedule than intended.</li>
  <li>Improves the performance of Live Activity tracking by de-duping push token tag requests.</li>
  <li>Fixes an issue in <code class="language-plaintext highlighter-rouge">logClick(using:)</code> where it would incorrectly open the <code class="language-plaintext highlighter-rouge">url</code> field in addition to logging a click for metrics. It now only logs a click for metrics.
    <ul>
      <li>This applies to the associated APIs for content cards, in-app messages, and news feed cards.</li>
      <li>It is still recommended to use the associated <code class="language-plaintext highlighter-rouge">Context</code> object to log interactions instead of these APIs.</li>
    </ul>
  </li>
</ul>

<h5 id="added-48">Added</h5>
<ul>
  <li>Adds <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/overrideresourcebundle"><code class="language-plaintext highlighter-rouge">BrazeKit.overrideResourceBundle</code></a> and <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/overrideresourcebundle/"><code class="language-plaintext highlighter-rouge">BrazeUI.overrideResourceBundle</code></a> to allow for custom resource bundles to be used by the SDK.
    <ul>
      <li>This feature is useful when your setup prevents you from using the default resource bundle (e.g. Tuist).</li>
    </ul>
  </li>
</ul>

<h2 id="5110">5.11.0</h2>

<h5 id="added-49">Added</h5>
<ul>
  <li>Adds support for <a href="https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities">Live Activities</a> via the <code class="language-plaintext highlighter-rouge">liveActivities</code> module on the Braze instance.
    <ul>
      <li>This feature provides the following new methods for tracking and managing Live Activities with the Braze push server:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">launchActivity(pushTokenTag:activity:)</code></li>
          <li><code class="language-plaintext highlighter-rouge">resumeActivities(ofType:)</code></li>
        </ul>
      </li>
      <li>This feature requires iOS 16.1 and up.</li>
      <li>To learn how to integrate this feature, refer to the <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b4-live-activities/">setup tutorial</a>.</li>
    </ul>
  </li>
  <li>Adds logic to re-synchronize Content Cards on SDK version changes.</li>
  <li>Adds provisional support for Xcode 14.3 Beta via the <a href="https://github.com/braze-inc/braze-swift-sdk-xcode-14-3-preview"><code class="language-plaintext highlighter-rouge">braze-inc/braze-swift-sdk-xcode-14-3-preview</code></a> repository.</li>
</ul>

<h2 id="5101">5.10.1</h2>

<h5 id="changed">Changed</h5>
<ul>
  <li>Dynamic versions of the prebuilt xcframeworks are now available in the <code class="language-plaintext highlighter-rouge">braze-swift-sdk-prebuilt.zip</code> release artifact.</li>
</ul>

<h2 id="5100">5.10.0</h2>

<h5 id="fixed-59">Fixed</h5>
<ul>
  <li>Fixes an issue where test content cards were removed before their expiration date.</li>
  <li>Fixes an issue in <code class="language-plaintext highlighter-rouge">BrazeUICompat</code> where the status bar appearance wasn’t restored to its original state after dismissing a full in-app message.</li>
  <li>Fixes an issue when decoding notification payloads where some valid boolean values weren’t correctly parsed.</li>
</ul>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>In-app modal and full-screen messages are now rendered with <code class="language-plaintext highlighter-rouge">UITextView</code>, which better supports large amounts of text and extended UTF code points.</li>
</ul>

<h2 id="591">5.9.1</h2>

<h5 id="fixed-60">Fixed</h5>
<ul>
  <li>Fixes an issue preventing local expired content cards from being removed.</li>
  <li>Fixes a behavior that could lead to background tasks extending beyond the expected time limit with inconsistent network connectivity.</li>
</ul>

<h5 id="added-50">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">logImpression(using:)</code> and <code class="language-plaintext highlighter-rouge">logClick(buttonId:using:)</code> to news feed cards.</li>
</ul>

<h2 id="590">5.9.0</h2>

<h5 id="breaking-9">Breaking</h5>
<ul>
  <li>Raises the minimum deployment target to iOS 11.0 and tvOS 11.0.</li>
  <li>Raises the Xcode version to 14.1 (14B47b).</li>
</ul>

<h5 id="fixed-61">Fixed</h5>
<ul>
  <li>Fixes an issue where the post-click webview would close automatically in some cases.</li>
  <li>Fixes a behavior where the current user messaging data would not be directly available after initializing the SDK or calling <code class="language-plaintext highlighter-rouge">changeUser(userId:)</code>.</li>
  <li>Fixes an issue preventing News Feed data models from being available offline.</li>
  <li>Fixes an issue where the release binaries could emit warnings when generating dSYMs.</li>
</ul>

<h5 id="changed-2">Changed</h5>
<ul>
  <li>SwiftPM and CocoaPods now use the same release assets.</li>
</ul>

<h5 id="added-51">Added</h5>
<ul>
  <li>Adds support for the upcoming Braze Feature Flags product.</li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">braze-swift-sdk-prebuilt.zip</code> archive to the release assets.
    <ul>
      <li>This archive contains the prebuilt xcframeworks and their associated resource bundles.</li>
      <li>The content of this archive can be used to manually integrate the SDK.</li>
    </ul>
  </li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">Examples-Manual.xcodeproj</code> showcasing how to integrate the SDK using the prebuilt release assets.</li>
  <li>Adds support for Mac Catalyst for example applications, available at <a href="./Support/Examples/README.md">Support/Examples/</a></li>
  <li>Adds support to convert from <code class="language-plaintext highlighter-rouge">Data</code> into an in-app message, content card, or news feed card via <code class="language-plaintext highlighter-rouge">decoding(json:)</code>.</li>
</ul>

<h2 id="581">5.8.1</h2>

<h5 id="fixed-62">Fixed</h5>
<ul>
  <li>Fixes a conflict with the shared instance of <a href="https://developer.apple.com/documentation/foundation/processinfo"><code class="language-plaintext highlighter-rouge">ProcessInfo</code></a>, allowing low power mode notifications to trigger correctly.</li>
</ul>

<h5 id="changed-3">Changed</h5>
<ul>
  <li>Renames the <code class="language-plaintext highlighter-rouge">BrazeLocation</code> class to <code class="language-plaintext highlighter-rouge">BrazeLocationProvider</code> to avoid shadowing the module of the same name (<a href="https://bugs.swift.org/browse/SR-14195">SR-14195</a>).</li>
</ul>

<h2 id="580">5.8.0</h2>

<p>To help migrate your app from the Appboy-iOS-SDK to our Swift SDK, this release includes the <code class="language-plaintext highlighter-rouge">Appboy-iOS-SDK</code> <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide">migration guide</a>:</p>
<ul>
  <li>Follow step-by-step instructions to migrate each feature to the new APIs.</li>
  <li>Includes instructions for a minimal migration scenario via our compatibility libraries.</li>
</ul>

<h5 id="added-52">Added</h5>
<ul>
  <li>Adds compatibility libraries <code class="language-plaintext highlighter-rouge">BrazeKitCompat</code> and <code class="language-plaintext highlighter-rouge">BrazeUICompat</code>:
    <ul>
      <li>Provides all the old APIs from <code class="language-plaintext highlighter-rouge">Appboy-iOS-SDK</code> to easily start migrating to the Swift SDK.</li>
      <li>See the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide">migration guide</a> for more details.</li>
    </ul>
  </li>
  <li>Adds support for <a href="https://www.braze.com/docs/user_guide/engagement_tools/news_feed">News Feed</a> data models and analytics.
    <ul>
      <li>News Feed UI is not supported by the Swift SDK. See the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide">migration guide</a> for instructions on using the compatibility UI.</li>
    </ul>
  </li>
</ul>

<h2 id="570">5.7.0</h2>

<h5 id="fixed-63">Fixed</h5>
<ul>
  <li>Fixes an issue where modal image in-app messages would not respect the aspect ratio of the image when the height of the image is larger than its width.</li>
</ul>

<h5 id="changed-4">Changed</h5>
<ul>
  <li>Changes modal, modal image, full, and full image in-app message view attributes to use the <code class="language-plaintext highlighter-rouge">ViewDimension</code> type for their <code class="language-plaintext highlighter-rouge">minWidth</code>, <code class="language-plaintext highlighter-rouge">maxWidth</code> and <code class="language-plaintext highlighter-rouge">maxHeight</code> attributes.
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">ViewDimension</code> type enables providing different values for regular and large size-classes.</li>
    </ul>
  </li>
</ul>

<h5 id="added-53">Added</h5>
<ul>
  <li>Adds a configuration to use a randomly generated UUID instead of IDFV as the device ID: <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/useuuidasdeviceid"><code class="language-plaintext highlighter-rouge">useUUIDAsDeviceId</code></a>.
    <ul>
      <li>This configuration defaults to <code class="language-plaintext highlighter-rouge">false</code>. To opt in to this feature, set this value to <code class="language-plaintext highlighter-rouge">true</code>.</li>
      <li>Enabling this value will only affect new devices. Existing devices will use the device identifier that was previously registered.</li>
    </ul>
  </li>
</ul>

<h2 id="564">5.6.4</h2>

<h5 id="fixed-64">Fixed</h5>
<ul>
  <li>Fixes an issue preventing the execution of <code class="language-plaintext highlighter-rouge">BrazeDelegate</code> methods when setting the delegate using Objective-C.</li>
  <li>Fixes an issue where triggering an in-app message twice with the same event did not place the message on the in-app message stack under certain conditions.</li>
</ul>

<h5 id="added-54">Added</h5>
<ul>
  <li>Adds the public <code class="language-plaintext highlighter-rouge">id</code> field to <code class="language-plaintext highlighter-rouge">Braze.InAppMessage.Data</code>.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">logImpression(using:)</code> and <code class="language-plaintext highlighter-rouge">logClick(buttonId:using:)</code> to both in-app messages and content cards, and adds <code class="language-plaintext highlighter-rouge">logDismissed(using:)</code> to content cards.
    <ul>
      <li>It is recommended to continue using the associated <code class="language-plaintext highlighter-rouge">Context</code> to log impressions, clicks, and dismissals for the majority of use cases.</li>
    </ul>
  </li>
  <li>Adds Swift concurrency to support async/await versions of the following public methods. These methods can be used as alternatives to their corresponding counterparts that use completion handlers:
    <ul>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/id()"><code class="language-plaintext highlighter-rouge">Braze.User.id()</code></a></li>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/deviceid()"><code class="language-plaintext highlighter-rouge">Braze.deviceId()</code></a></li>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/requestrefresh()"><code class="language-plaintext highlighter-rouge">ContentCards.requestRefresh()</code></a></li>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cardsstream"><code class="language-plaintext highlighter-rouge">ContentCards.cardsStream</code></a> as an alternative to <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)"><code class="language-plaintext highlighter-rouge">ContentCards.subscribeToUpdates(_:)</code></a></li>
    </ul>
  </li>
</ul>

<h2 id="563">5.6.3</h2>

<h5 id="fixed-65">Fixed</h5>
<ul>
  <li>Fixes the <code class="language-plaintext highlighter-rouge">InAppMessageRaw</code> to <code class="language-plaintext highlighter-rouge">InAppMessage</code> conversion to properly take into account the <code class="language-plaintext highlighter-rouge">extras</code> dictionary and the <code class="language-plaintext highlighter-rouge">duration</code>.</li>
  <li>Fixes an issue preventing the execution of the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:sdkauthenticationfailedwitherror:)-505pz"><code class="language-plaintext highlighter-rouge">braze(_:sdkAuthenticationFailedWithError:)</code></a> delegate method in case of an authentication error.</li>
</ul>

<h5 id="changed-5">Changed</h5>
<ul>
  <li>Improves error logging descriptions for HTTP requests and responses.</li>
</ul>

<h2 id="562">5.6.2</h2>

<h5 id="changed-6">Changed</h5>
<ul>
  <li>Corrected the version number from the previous release.</li>
</ul>

<h2 id="561">5.6.1</h2>

<h5 id="added-55">Added</h5>
<ul>
  <li>Adds the public initializers <code class="language-plaintext highlighter-rouge">Braze.ContentCard.Context(card:using:)</code> and <code class="language-plaintext highlighter-rouge">Braze.InAppMessage.Context(message:using:)</code>.</li>
</ul>

<h2 id="560">5.6.0</h2>

<h5 id="fixed-66">Fixed</h5>
<ul>
  <li>The modal webview controller presented after a click now correctly handles non-HTTP(S) URLs (e.g. App Store URLs).</li>
  <li>Fixes an issue preventing some test HTML in-app messages from displaying images.</li>
</ul>

<h5 id="added-56">Added</h5>
<ul>
  <li>Learn how to easily customize <code class="language-plaintext highlighter-rouge">BrazeUI</code> in-app message and content cards UI components with the following documentation and example code:
    <ul>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization">In-App Message UI Customization</a> article</li>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization">Content Cards UI Customization</a> article</li>
      <li><code class="language-plaintext highlighter-rouge">InAppMessageUI-Customization</code> example scheme</li>
      <li><code class="language-plaintext highlighter-rouge">ContentCardUI-Customization</code> example scheme</li>
    </ul>
  </li>
  <li>Adds new attributes to <code class="language-plaintext highlighter-rouge">BrazeUI</code> in-app message UI components:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">cornerCurve</code> to change the <a href="https://developer.apple.com/documentation/quartzcore/calayer/3152596-cornercurve"><code class="language-plaintext highlighter-rouge">cornerCurve</code></a></li>
      <li><code class="language-plaintext highlighter-rouge">buttonsAttributes</code> to change the font, spacing and corner radius of the buttons</li>
      <li><code class="language-plaintext highlighter-rouge">imageCornerRadius</code> to change the image corner radius for slideups</li>
      <li><code class="language-plaintext highlighter-rouge">imageCornerCurve</code> to change the image <a href="https://developer.apple.com/documentation/quartzcore/calayer/3152596-cornercurve"><code class="language-plaintext highlighter-rouge">cornerCurve</code></a> for slideups</li>
      <li><code class="language-plaintext highlighter-rouge">dismissible</code> to change whether slideups can be interactively dismissed</li>
    </ul>
  </li>
  <li>Adds direct accessors to the in-app message view subclass on the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/messageview"><code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI.messageView</code></a> property.
    <ul>
      <li><a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/inappmessageview/slideup"><code class="language-plaintext highlighter-rouge">slideup</code></a>, <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/inappmessageview/modal"><code class="language-plaintext highlighter-rouge">modal</code></a>, <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/inappmessageview/modalimage"><code class="language-plaintext highlighter-rouge">modalImage</code></a>, <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/inappmessageview/full"><code class="language-plaintext highlighter-rouge">full</code></a>, <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/inappmessageview/fullimage"><code class="language-plaintext highlighter-rouge">fullImage</code></a>, <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/inappmessageview/html"><code class="language-plaintext highlighter-rouge">html</code></a>, <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/inappmessageview/control"><code class="language-plaintext highlighter-rouge">control</code></a>.</li>
    </ul>
  </li>
  <li>Adds direct accessors to the content card <code class="language-plaintext highlighter-rouge">title</code>, <code class="language-plaintext highlighter-rouge">description</code> and <code class="language-plaintext highlighter-rouge">domain</code> when available.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">Braze.Notifications.isInternalNotification</code> to check if a push notification was sent by Braze for an internal feature.</li>
  <li>Adds <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages/#bridge"><code class="language-plaintext highlighter-rouge">brazeBridge.changeUser()</code></a> to the HTML in-app messages JavaScript bridge.</li>
</ul>

<h5 id="changed-7">Changed</h5>

<ul>
  <li>The <code class="language-plaintext highlighter-rouge">applyAttributes()</code> method for <code class="language-plaintext highlighter-rouge">BrazeContentCardUI</code> views now take the <code class="language-plaintext highlighter-rouge">attributes</code> explicitly as a parameter.</li>
</ul>

<h2 id="551">5.5.1</h2>

<h5 id="fixed-67">Fixed</h5>
<ul>
  <li>Fixes an issue where content cards would not be properly removed when stopping a content card campaign on the dashboard and selecting the option <em>Remove card after the next sync (e.g. session start)</em>.</li>
</ul>

<h2 id="550">5.5.0</h2>

<h5 id="added-57">Added</h5>
<ul>
  <li>Adds support for host apps written in Objective-C.
    <ul>
      <li>Braze Objective-C types start either with <code class="language-plaintext highlighter-rouge">BRZ</code> or <code class="language-plaintext highlighter-rouge">Braze</code>, e.g.:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">Braze</code></li>
          <li><code class="language-plaintext highlighter-rouge">BrazeDelegate</code></li>
          <li><code class="language-plaintext highlighter-rouge">BRZContentCardRaw</code></li>
        </ul>
      </li>
      <li>See our Objective-C <a href="Examples/">Examples</a> project.</li>
    </ul>
  </li>
  <li>Adds <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y"><code class="language-plaintext highlighter-rouge">BrazeDelegate.braze(_:noMatchingTriggerForEvent:)</code></a> which is called if no Braze in-app message is triggered for a given event.</li>
</ul>

<h5 id="changed-8">Changed</h5>
<ul>
  <li>In <code class="language-plaintext highlighter-rouge">Braze.Configuration.Api</code>:
    <ul>
      <li>Renamed <code class="language-plaintext highlighter-rouge">SdkMetadata</code> to <code class="language-plaintext highlighter-rouge">SDKMetadata</code>.</li>
      <li>Renamed <code class="language-plaintext highlighter-rouge">addSdkMetadata(_:)</code> to <code class="language-plaintext highlighter-rouge">addSDKMetadata(_:)</code>.</li>
    </ul>
  </li>
  <li>In <code class="language-plaintext highlighter-rouge">Braze.InAppMessage</code>:
    <ul>
      <li>Renamed <code class="language-plaintext highlighter-rouge">Themes.default</code> to <code class="language-plaintext highlighter-rouge">Themes.defaults</code>.</li>
      <li>Renamed <code class="language-plaintext highlighter-rouge">ClickAction.uri</code> to <code class="language-plaintext highlighter-rouge">ClickAction.url</code>.</li>
      <li>Renamed <code class="language-plaintext highlighter-rouge">ClickAction.uri(_:useWebView:)</code> to <code class="language-plaintext highlighter-rouge">ClickAction.url(_:useWebView:)</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="540">5.4.0</h2>

<h5 id="fixed-68">Fixed</h5>
<ul>
  <li>Fixes an issue where <code class="language-plaintext highlighter-rouge">brazeBridge.logClick(button_id)</code> would incorrectly accept invalid <code class="language-plaintext highlighter-rouge">button_id</code> values like <code class="language-plaintext highlighter-rouge">""</code>, <code class="language-plaintext highlighter-rouge">[]</code>, or <code class="language-plaintext highlighter-rouge">{}</code>.</li>
</ul>

<h5 id="added-58">Added</h5>
<ul>
  <li>Adds support for Braze Action Deeplink Click Actions.</li>
</ul>

<h2 id="532">5.3.2</h2>

<h5 id="fixed-69">Fixed</h5>
<ul>
  <li>Fixes an issue preventing compilation when importing <code class="language-plaintext highlighter-rouge">BrazeUI</code> via SwiftPM in specific cases.</li>
  <li>Lowers <code class="language-plaintext highlighter-rouge">BrazeUI</code> minimum deployment target to iOS 10.0.</li>
</ul>

<h2 id="531">5.3.1</h2>

<h5 id="fixed-70">Fixed</h5>
<ul>
  <li>Fixes an HTML in-app message issue where clicking a link in an iFrame would launch a separate webview and close the message, instead of redirecting within the iFrame.</li>
  <li>Fixes the rounding of In-App Message modal view top corners.</li>
  <li>Fixes the display of modals and full screen in-app messages on iPads in landscape mode.</li>
</ul>

<h5 id="added-59">Added</h5>
<ul>
  <li>Adds two Example schemes:
    <ul>
      <li>InAppMessage-Custom-UI:
        <ul>
          <li>Demonstrates how to implement your own custom In-App Message UI.</li>
          <li>Available on iOS and tvOS.</li>
        </ul>
      </li>
      <li>ContentCards-Custom-UI:
        <ul>
          <li>Demonstrates how to implement your own custom Content Card UI.</li>
          <li>Available on iOS and tvOS.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Adds <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction/uri"><code class="language-plaintext highlighter-rouge">Braze.InAppMessage.ClickAction.uri</code></a> for direct access.</li>
  <li>Adds <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction/uri/"><code class="language-plaintext highlighter-rouge">Braze.ContentCard.ClickAction.uri</code></a> for direct access.</li>
  <li>Adds <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/deviceid(queue:completion:)"><code class="language-plaintext highlighter-rouge">Braze.deviceId(queue:completion:)</code></a> to retrieve the device identifier used by Braze.</li>
</ul>

<h2 id="530">5.3.0</h2>

<h5 id="added-60">Added</h5>
<ul>
  <li>Adds support for tvOS.
    <ul>
      <li>See the schemes <em>Analytics-tvOS</em> and <em>Location-tvOS</em> in the <a href="Examples/">Examples</a> project.</li>
    </ul>
  </li>
</ul>

<h2 id="520">5.2.0</h2>

<h5 id="added-61">Added</h5>
<ul>
  <li>Adds <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards">Content Cards</a> support.
    <ul>
      <li>See the <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui"><em>Content Cards UI</em></a> tutorial to get started.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-9">Changed</h5>
<ul>
  <li>Raises <code class="language-plaintext highlighter-rouge">BrazeUI</code> minimum deployment target to iOS 11.0 to allow providing SwiftUI compatible Views.</li>
</ul>

<h2 id="510">5.1.0</h2>

<h5 id="fixed-71">Fixed</h5>
<ul>
  <li>Fixes an issue where the SDK would be unable to present a webview when the application was already presenting a modal view controller.</li>
  <li>Fixes an issue preventing a full device data update after changing the identified user.</li>
  <li>Fixes an issue preventing events and user attributes from being flushed automatically under certain conditions.</li>
  <li>Fixes an issue delaying updates to push notifications settings.</li>
</ul>

<h5 id="added-62">Added</h5>
<ul>
  <li>Adds CocoaPods support.
    <ul>
      <li>Pods:
        <ul>
          <li><a href="https://cocoapods.org/pods/BrazeKit">BrazeKit</a></li>
          <li><a href="https://cocoapods.org/pods/BrazeUI">BrazeUI</a></li>
          <li><a href="https://cocoapods.org/pods/BrazeLocation">BrazeLocation</a></li>
          <li><a href="https://cocoapods.org/pods/BrazeNotificationService">BrazeNotificationService</a></li>
          <li><a href="https://cocoapods.org/pods/BrazePushStory">BrazePushStory</a></li>
        </ul>
      </li>
      <li>See <a href="Examples/Podfile">Examples/Podfile</a> for example integration.</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">Braze.UIUtils.activeTopmostViewController</code> to get the topmost view controller that is currently being presented by the application.</li>
</ul>

<h2 id="501">5.0.1</h2>

<h5 id="fixed-72">Fixed</h5>
<ul>
  <li>Fixes a race condition when retrieving the user’s notification settings.</li>
  <li>Fixes an issue where duplicate data could be recorded after force quitting the application.</li>
</ul>

<h2 id="500-early-access">5.0.0 (Early Access)</h2>

<p>We are excited to announce the initial release of the Braze Swift SDK!</p>

<p>The Braze Swift SDK is set to replace the <a href="https://github.com/Appboy/appboy-ios-sdk/">current Braze iOS SDK</a> and provides a more modern API, simpler integration, and better performance.</p>

<h3 id="current-limitations">Current limitations</h3>

<p>The following features are not supported yet:</p>
<ul>
  <li><del>Objective-C integration</del>
    <ul>
      <li>Added in <a href="#550">5.5.0</a></li>
    </ul>
  </li>
  <li><del>tvOS integration</del>
    <ul>
      <li>Added in <a href="#530">5.3.0</a></li>
    </ul>
  </li>
  <li><del>News Feed</del>
    <ul>
      <li>Added in <a href="#570">5.7.0</a></li>
    </ul>
  </li>
  <li><del>Content Cards</del>
    <ul>
      <li>Added in <a href="#520">5.2.0</a></li>
    </ul>
  </li>
</ul>




**Tip:**


You can also find a copy of the [Cordova Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md).



<h2 id="1500">15.0.0</h2>

<h5 id="breaking">Breaking</h5>
<ul>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v41.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 39.0.0 to 41.1.1</a>.</li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 13.2.0 to 14.0.1</a>.</li>
</ul>

<h5 id="fixed">Fixed</h5>
<ul>
  <li>Fixed <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage</code> on both iOS and Android to properly invoke the success callback with in-app message data and correctly respect the <code class="language-plaintext highlighter-rouge">useBrazeUI</code> parameter. <a href="https://github.com/braze-inc/braze-cordova-sdk/issues/103">#103</a></li>
</ul>

<h2 id="1400">14.0.0</h2>

<h5 id="breaking-1">Breaking</h5>
<ul>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 37.0.0 to 39.0.0</a>.
    <ul>
      <li>The minimum required <code class="language-plaintext highlighter-rouge">GradlePluginKotlinVersion</code> is now <code class="language-plaintext highlighter-rouge">2.1.0</code>.</li>
    </ul>
  </li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 12.0.0 to 13.2.0</a>.
    <ul>
      <li>This includes Xcode 26 support.</li>
    </ul>
  </li>
  <li>Removes support for News Feed. The following APIs have been removed:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">launchNewsFeed</code></li>
      <li><code class="language-plaintext highlighter-rouge">getNewsFeed</code></li>
      <li><code class="language-plaintext highlighter-rouge">getNewsFeedUnreadCount</code></li>
      <li><code class="language-plaintext highlighter-rouge">getNewsFeedCardCount</code></li>
      <li><code class="language-plaintext highlighter-rouge">getCardCountForCategories</code></li>
      <li><code class="language-plaintext highlighter-rouge">getUnreadCardCountForCategories</code></li>
    </ul>
  </li>
</ul>

<h2 id="1300">13.0.0</h2>

<h5 id="breaking-2">Breaking</h5>
<ul>
  <li>Updated the internal iOS implementation of <code class="language-plaintext highlighter-rouge">enableSdk</code> method to use <code class="language-plaintext highlighter-rouge">setEnabled:</code> instead of <code class="language-plaintext highlighter-rouge">_requestEnableSDKOnNextAppRun</code>, which was deprecated in the Swift SDK.
    <ul>
      <li>Calling this method no longer requires the app to be re-launched to take effect. The SDK will now become enabled as soon as this method is executed.</li>
    </ul>
  </li>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 36.0.0 to 37.0.0</a>.</li>
</ul>

<h2 id="1200">12.0.0</h2>

<blockquote>
  <p>[!IMPORTANT]
This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. However, we are not reintroducing formal support for &lt; API 25. Read more <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600">here</a>.</p>
</blockquote>

<h5 id="breaking-3">Breaking</h5>
<ul>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 35.0.0 to 36.0.0</a>.</li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.6.1 to 12.0.0</a>.</li>
</ul>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Updated the internal iOS implementation of <code class="language-plaintext highlighter-rouge">getUserId</code> to <code class="language-plaintext highlighter-rouge">braze.user.identifier</code> instead of <code class="language-plaintext highlighter-rouge">[braze.user idWithCompletion:]</code>, which was deprecated in Swift SDK <a href="https://github.com/braze-inc/braze-swift-sdk/releases/tag/11.5.0">11.5.0</a>. This deprecation does not have any impact to functionality.</li>
</ul>

<h5 id="added">Added</h5>
<ul>
  <li>Added support for the <code class="language-plaintext highlighter-rouge">setSdkAuthenticationSignature</code> method on Android.</li>
</ul>

<h2 id="1100">11.0.0</h2>

<h5 id="breaking-4">Breaking</h5>
<ul>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 32.1.0 to 35.0.0</a>.
    <ul>
      <li>The minimum required Android SDK version is 25. See more details <a href="https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information">here</a>.</li>
    </ul>
  </li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.1.0...11.6.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 10.1.0 to 11.6.1</a>.</li>
</ul>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Updated automatic push integration on iOS to be fully compatible with Swift-based projects (e.g. Capacitor applications).
    <ul>
      <li>Previously, the automatic push integration would not properly register the push token in Swift-based projects.</li>
    </ul>
  </li>
</ul>

<h5 id="added-1">Added</h5>
<ul>
  <li>Added the ability to provide different API keys for Android and iOS in the <code class="language-plaintext highlighter-rouge">config.xml</code> file.
    <ul>
      <li>To set the Android API key, add <code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.android_api_key" value="your-android-api-key" /&gt;</code>.</li>
      <li>To set the iOS API key, add <code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.ios_api_key" value="your-ios-api-key" /&gt;</code>.</li>
      <li>The preference <code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.api_key" value="your-api-key" /&gt;</code> is still supported for backwards compatibility and is used if no platform-specific API key is provided.</li>
    </ul>
  </li>
</ul>

<h2 id="1000">10.0.0</h2>

<h5 id="breaking-5">Breaking</h5>
<ul>
  <li>⚠️ This version now requires Cordova Android 13.0.0. ⚠️
    <ul>
      <li>Refer to the <a href="https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html">Cordova release announcement</a> for a full list of project dependency requirements.</li>
    </ul>
  </li>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.3.0 to 32.1.0</a>.</li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 9.2.0 to 10.1.0</a>.</li>
</ul>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Fixed the native-to-JavaScript translation of in-app message strings, where nested escape characters were previously being removed.</li>
  <li>Fixed the <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage</code> method on iOS to respect the <code class="language-plaintext highlighter-rouge">useBrazeUI</code> setting.
    <ul>
      <li>Updated the Android implementation to match iOS by using the <code class="language-plaintext highlighter-rouge">DISCARD</code> option instead of <code class="language-plaintext highlighter-rouge">DISPLAY_LATER</code> if the default Braze UI is not used.</li>
    </ul>
  </li>
  <li>Fixed the <code class="language-plaintext highlighter-rouge">getContentCardsFromServer</code> method to trigger an error callback on iOS when cards have failed to refresh.</li>
</ul>

<h5 id="added-2">Added</h5>
<ul>
  <li>Added the <code class="language-plaintext highlighter-rouge">getUserId()</code> method to get the ID of the current user. This method will return <code class="language-plaintext highlighter-rouge">null</code> if the current user is anonymous.</li>
  <li>Added support for new Feature Flag property types and APIs for accessing them:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagTimestampProperty(id, key)</code> for accessing Int Unix UTC millisecond timestamps as <code class="language-plaintext highlighter-rouge">number</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagImageProperty(id, key)</code> for accessing image URLs as <code class="language-plaintext highlighter-rouge">string</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagJSONProperty(id, key)</code> for accessing JSON objects as <code class="language-plaintext highlighter-rouge">object</code> types.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">setLocationCustomAttribute(key, latitude, longitude)</code> to set a location custom attribute.</li>
</ul>

<h2 id="920">9.2.0</h2>

<h5 id="added-3">Added</h5>
<ul>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/9.1.0...9.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 9.1.0 to 9.2.0</a>.</li>
</ul>

<h2 id="910">9.1.0</h2>

<h5 id="added-4">Added</h5>
<ul>
  <li>Added the following properties to the Content Card model:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">isTest</code></li>
      <li><code class="language-plaintext highlighter-rouge">isControl</code> (Note: If you’re implementing your own UI, Control Cards should not be rendered, but you should manually log analytics for them.)</li>
    </ul>
  </li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...9.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 9.0.0 to 9.1.0</a>.</li>
</ul>

<h2 id="900">9.0.0</h2>

<h5 id="breaking-6">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.7.0 to 9.0.0</a>.</li>
</ul>

<h5 id="added-5">Added</h5>
<ul>
  <li>Added support to modify the allow list for Braze tracking properties via the following JavaScript properties and methods:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">TrackingProperty</code> string enum</li>
      <li><code class="language-plaintext highlighter-rouge">TrackingPropertyAllowList</code> object interface</li>
      <li><code class="language-plaintext highlighter-rouge">updateTrackingPropertyAllowList</code> method</li>
      <li>For details, refer to the <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/">Braze iOS Privacy Manifest</a> documentation.</li>
    </ul>
  </li>
  <li>Added the <code class="language-plaintext highlighter-rouge">setAdTrackingEnabled</code> method to set <code class="language-plaintext highlighter-rouge">adTrackingEnabled</code> flag on iOS and both the <code class="language-plaintext highlighter-rouge">adTrackingEnabled</code> flag and the Google Advertising ID on Android.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazePlugin.subscribeToInAppMessage()</code> which allows you to listen for new in-app messages from the JavaScript plugin and choose whether or not to use the default Braze UI to display in-app messages.</li>
  <li>Added support for logging analytics and functionality for in-app messages.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.logInAppMessageImpression(message)</code></li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.logInAppMessageClicked(message)</code></li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.loginAppMessageButtonClicked(message, buttonId)</code></li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.hideCurrentInAppMessage()</code></li>
    </ul>
  </li>
  <li>Added support for manually performing the action of an in-app message when using a custom UI.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.performInAppMessageAction(message)</code></li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.performInAppMessageButtonAction(message, buttonId)</code></li>
    </ul>
  </li>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.1.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.1.1 to 30.3.0</a>.</li>
</ul>

<h2 id="810">8.1.0</h2>

<h5 id="added-6">Added</h5>
<ul>
  <li>Added new Android feature support that can be added in your <code class="language-plaintext highlighter-rouge">config.xml</code>:
    <ul>
      <li>Ability to set the session timeout behavior to be based either on session start or session end events.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.is_session_start_based_timeout_enabled" value="false" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set the user-facing name as seen via <code class="language-plaintext highlighter-rouge">NotificationChannel.getName</code> for the Braze default <code class="language-plaintext highlighter-rouge">NotificationChannel</code>.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.default_notification_channel_name" value="name" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set the user-facing description as seen via <code class="language-plaintext highlighter-rouge">NotificationChannel.getDescription</code> for the Braze default <code class="language-plaintext highlighter-rouge">NotificationChannel</code>.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.default_notification_channel_description" value="description" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set whether a Push Story is automatically dismissed when clicked.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.does_push_story_dismiss_on_click" value="true" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set whether the use of a fallback Firebase Cloud Messaging Service is enabled.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set the classpath for the fallback Firebase Cloud Messaging Service.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.fallback_firebase_messaging_service_classpath" value="your-classpath" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set whether the Content Cards unread visual indication bar is enabled.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set whether the Braze will automatically register tokens in <code class="language-plaintext highlighter-rouge">com.google.firebase.messaging.FirebaseMessagingService.onNewToken</code>.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set whether Braze will add an activity to the back stack when automatically following deep links for push.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set the activity that Braze will add to the back stack when automatically following deep links for push.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="your-class-name" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set if Braze should automatically opt-in the user when push is authorized by Android.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.should_opt_in_when_push_authorized" value="true" /&gt;</code></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Added new iOS feature support that can be added in your <code class="language-plaintext highlighter-rouge">config.xml</code>:
    <ul>
      <li>Ability to set the minimum logging level for <code class="language-plaintext highlighter-rouge">Braze.Configuration.Logger</code>.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.ios_log_level" value="2" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set if a randomly generated UUID should be used as the device ID.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.ios_use_uuid_as_device_id" value="YES" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set the interval in seconds between automatic data flushes.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.ios_flush_interval_seconds" value="10" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set whether the request policy for <code class="language-plaintext highlighter-rouge">Braze.Configuration.Api</code> should be automatic or manual.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.ios_use_automatic_request_policy" value="YES" /&gt;</code></li>
        </ul>
      </li>
      <li>Ability to set if a user’s notification subscription state should automatically be set to optedIn when push permissions are authorized.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.should_opt_in_when_push_authorized" value="YES" /&gt;</code></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazePlugin.setLastKnownLocation()</code> to set the last known location for the user.</li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.6.0...7.7.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.6.0 to 7.7.0</a>.</li>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.0.0...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.0.0 to 30.1.1</a>.</li>
</ul>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Fixed the <code class="language-plaintext highlighter-rouge">getDeviceId</code> method to return the value as a success instead of an error on iOS.</li>
</ul>

<h2 id="800">8.0.0</h2>

<h5 id="breaking-7">Breaking</h5>
<ul>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v30.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 27.0.1 to 30.0.0</a>.</li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.6.0...7.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.6.0 to 7.6.0</a>.</li>
  <li>Renamed the <code class="language-plaintext highlighter-rouge">Banner</code> Content Card type to <code class="language-plaintext highlighter-rouge">ImageOnly</code>:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">ContentCardTypes.BANNER</code> → <code class="language-plaintext highlighter-rouge">ContentCardTypes.IMAGE_ONLY</code></li>
      <li>On Android, if the XML files in your project contain the word <code class="language-plaintext highlighter-rouge">banner</code> for Content Cards, it should be replaced with <code class="language-plaintext highlighter-rouge">image_only</code>.</li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">BrazePlugin.getFeatureFlag(id)</code> will now return <code class="language-plaintext highlighter-rouge">null</code> if the feature flag does not exist.</li>
  <li><code class="language-plaintext highlighter-rouge">BrazePlugin.subscribeToFeatureFlagsUpdates(function)</code> will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.</li>
  <li>Removed the deprecated method <code class="language-plaintext highlighter-rouge">registerAppboyPushMessages</code>. Use <code class="language-plaintext highlighter-rouge">setRegisteredPushToken</code> instead.</li>
</ul>

<h5 id="added-7">Added</h5>
<ul>
  <li>Added the ability to set a minimum trigger action time interval for Android and iOS.
    <ul>
      <li>To enable this feature, add the line <code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" /&gt;</code> in your <code class="language-plaintext highlighter-rouge">config.xml</code>.</li>
    </ul>
  </li>
  <li>Added the ability to configure the app group ID for iOS push extensions.
    <ul>
      <li>To enable this feature, add the line <code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.ios_push_app_group" value="your-app-group" /&gt;</code> in your <code class="language-plaintext highlighter-rouge">config.xml</code>.</li>
    </ul>
  </li>
  <li>Added support for automatically forwarding universal links in iOS.
    <ul>
      <li>To enable this feature, add the line <code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.ios_forward_universal_links" value="YES" /&gt;</code> in your <code class="language-plaintext highlighter-rouge">config.xml</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="700">7.0.0</h2>

<h5 id="breaking-8">Breaking</h5>
<ul>
  <li>Updated the native Android version <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701">from Braze Android SDK 26.3.2 to 27.0.1</a>.</li>
</ul>

<h5 id="added-8">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">logFeatureFlagImpression(id)</code>.</li>
  <li>Updated the native iOS version <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.5.0...6.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.5.0 to 6.6.0</a>.</li>
  <li>Added support for nested custom user attributes.
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">setCustomUserAttribute</code> method now accepts objects and arrays of objects.</li>
      <li>Added an optional <code class="language-plaintext highlighter-rouge">merge</code> parameter to the <code class="language-plaintext highlighter-rouge">setCustomUserAttribute</code> method. This is a non-breaking change.</li>
      <li>Please see our <a href="https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/">public docs</a> for more information.</li>
    </ul>
  </li>
  <li>Exposed the <code class="language-plaintext highlighter-rouge">braze</code> instance as a convenience static property on iOS via <code class="language-plaintext highlighter-rouge">BrazePlugin.braze</code>.
    <ul>
      <li>This makes it easier to work with tools such as Capacitor by Ionic.</li>
    </ul>
  </li>
</ul>

<h2 id="601">6.0.1</h2>

<h5 id="fixed-5">Fixed</h5>
<ul>
  <li>Updated the native Android version <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2632">from Braze Android SDK 26.3.1 to 26.3.2</a>.</li>
</ul>

<h2 id="600">6.0.0</h2>

<h5 id="breaking-9">Breaking</h5>
<ul>
  <li>Updated the native iOS version <a href="https://github.com/braze-inc/braze-swift-sdk/compare/5.13.0...6.5.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 5.13.0 to 6.5.0</a>.</li>
  <li>Updated the native Android version <a href="https://github.com/braze-inc/braze-android-sdk/compare/v25.0.0...v26.3.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 25.0.0 to 26.3.1</a>.</li>
</ul>

<h5 id="added-9">Added</h5>
<ul>
  <li>Added support for Braze SDK Authentication.
    <ul>
      <li>Enabled on Android via <code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.sdk_authentication_enabled" value="true" /&gt;</code>.</li>
      <li>Enabled on iOS via <code class="language-plaintext highlighter-rouge">&lt;preference name="com.braze.sdk_authentication_enabled" value="YES" /&gt;</code>.</li>
      <li>Updated <code class="language-plaintext highlighter-rouge">changeUser()</code> to accept an optional second parameter for an SDK Auth token, e.g. <code class="language-plaintext highlighter-rouge">changeUser("user id here", "jwt token here")</code>.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">subscribeToSdkAuthenticationFailures()</code> which listens for SDK authentication failures.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">setSdkAuthenticationSignature()</code> to set a Braze SDK Authentication signature JWT token.</li>
    </ul>
  </li>
</ul>

<h2 id="500">5.0.0</h2>

<h5 id="breaking-10">Breaking</h5>
<ul>
  <li>Updated these Feature Flag methods to return promises instead of using a callback parameter
    <ul>
      <li><code class="language-plaintext highlighter-rouge">getAllFeatureFlags()</code></li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlag(id)</code></li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagBooleanProperty(id, key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagStringProperty(id, key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagNumberProperty(id, key)</code></li>
      <li>To get a boolean property, for example, you can now use the following syntax:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("feature-flag-id", "property-key");
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
  <li>Changed <code class="language-plaintext highlighter-rouge">subscribeToFeatureFlagUpdates</code> to <code class="language-plaintext highlighter-rouge">subscribeToFeatureFlagsUpdates</code>.</li>
</ul>

<h2 id="400">4.0.0</h2>

<h5 id="breaking-11">Breaking</h5>
<ul>
  <li>Renamed instances of <code class="language-plaintext highlighter-rouge">Appboy</code> to <code class="language-plaintext highlighter-rouge">Braze</code>.
    <ul>
      <li>To ensure that your project is properly migrated to the new naming conventions, note and replace the following instances in your project:
        <ul>
          <li>The plugin has been renamed from <code class="language-plaintext highlighter-rouge">cordova-plugin-appboy</code> to <code class="language-plaintext highlighter-rouge">cordova-plugin-braze</code>.
            <ul>
              <li>Ensure that you run <code class="language-plaintext highlighter-rouge">cordova plugin remove cordova-plugin-appboy</code> and then re-add the plugin using the instructions in the <a href="./README.md">README</a>.</li>
            </ul>
          </li>
          <li>This GitHub repository has been moved to the URL <code class="language-plaintext highlighter-rouge">https://github.com/braze-inc/braze-cordova-sdk</code>.</li>
          <li>In your project’s <code class="language-plaintext highlighter-rouge">config.xml</code> file, rename instances of <code class="language-plaintext highlighter-rouge">com.appboy</code> to <code class="language-plaintext highlighter-rouge">com.braze</code> for each of your configuration property keys.</li>
          <li>The JavaScript class interface <code class="language-plaintext highlighter-rouge">AppboyPlugin</code> has been renamed to <code class="language-plaintext highlighter-rouge">BrazePlugin</code>.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2500">Braze Android SDK 25.0.0</a>.</li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.13.0">Braze Swift SDK 5.13.0</a>.
    <ul>
      <li>This update fixes the iOS behavior introduced in version <code class="language-plaintext highlighter-rouge">2.33.0</code> when logging clicks for content cards. Calling <code class="language-plaintext highlighter-rouge">logContentCardClicked</code> now only sends a click event for metrics, instead of both sending a click event as well as redirecting to the associated <code class="language-plaintext highlighter-rouge">url</code> field.
        <ul>
          <li>For instance, to log a content card click and redirect to a URL, you will need two commands:
```
BrazePlugin.logContentCardClicked(contentCardId);</li>
        </ul>

        <p>// Your own custom implementation
YourApp.openUrl(contentCard[“url”]);
```</p>
        <ul>
          <li>This brings the iOS behavior to match pre-<code class="language-plaintext highlighter-rouge">2.33.0</code> versions and bring parity with Android’s behavior.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h5 id="added-10">Added</h5>
<ul>
  <li>Added property methods for Feature Flags: <code class="language-plaintext highlighter-rouge">getFeatureFlagBooleanProperty(id, key)</code>, <code class="language-plaintext highlighter-rouge">getFeatureFlagStringProperty(id, key)</code>, <code class="language-plaintext highlighter-rouge">getFeatureFlagNumberProperty(id, key)</code></li>
</ul>

<h2 id="300">3.0.0</h2>

<h5 id="added-11">Added</h5>
<ul>
  <li>Added support for the upcoming Braze Feature Flags product with <code class="language-plaintext highlighter-rouge">getFeatureFlag()</code>, <code class="language-plaintext highlighter-rouge">getAllFeatureFlags()</code>, <code class="language-plaintext highlighter-rouge">refreshFeatureFlags()</code>, and <code class="language-plaintext highlighter-rouge">subscribeToFeatureFlagUpdates()</code>.</li>
</ul>

<h5 id="changed">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.11.0">Braze Swift SDK 5.11.0</a>.</li>
  <li>Removed automatic requests for App Tracking Transparency permissions on iOS.</li>
</ul>

<h2 id="2330">2.33.0</h2>

<h5 id="breaking-12">Breaking</h5>
<ul>
  <li>Migrated the iOS plugin to use the new <a href="https://github.com/braze-inc/braze-swift-sdk">Braze Swift SDK</a> (5.8.1).
    <ul>
      <li>News Feed UI is no longer supported on iOS.</li>
      <li>This migration requires re-identifying users. To do so, you must call the <code class="language-plaintext highlighter-rouge">changeUser</code> method on the Braze instance for non-anonymous users. You can read more about it <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/#Re-identify-users">here</a>.</li>
    </ul>
  </li>
</ul>

<h2 id="2320">2.32.0</h2>

<h5 id="breaking-13">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v24.1.0">Braze Android SDK 24.1.0</a>.</li>
  <li>Updated the Android bridge to Kotlin.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">&lt;preference name="GradlePluginKotlinEnabled" value="true" /&gt;</code> is now required in your <code class="language-plaintext highlighter-rouge">config.xml</code>.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">setAvatarImageUrl()</code>.</li>
</ul>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>Added an <code class="language-plaintext highlighter-rouge">main</code> value to <code class="language-plaintext highlighter-rouge">package.json</code>.</li>
</ul>

<h5 id="added-12">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">setRegisteredPushToken()</code> which replaces the deprecated <code class="language-plaintext highlighter-rouge">registerAppboyPushMessages()</code> method.</li>
</ul>

<h2 id="2310">2.31.0</h2>

<h5 id="breaking-14">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.0.1">Braze Android SDK 23.0.1</a>.</li>
</ul>

<h5 id="added-13">Added</h5>
<ul>
  <li>Added a method <code class="language-plaintext highlighter-rouge">requestPushPermission()</code> for Android API 33 to request push permission prompts from the system on Android 13 devices.</li>
</ul>

<h2 id="2301">2.30.1</h2>

<h5 id="added-14">Added</h5>
<ul>
  <li>Added the ability to set the session timeout for iOS (String) in seconds.
    <ul>
      <li>Add <code class="language-plaintext highlighter-rouge">&lt;preference name="com.appboy.com.appboy.ios_session_timeout" value="your_timeout" /&gt;</code> to your <code class="language-plaintext highlighter-rouge">config.xml</code>, replacing <code class="language-plaintext highlighter-rouge">your_timeout</code> with the desired number of seconds.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-6">Fixed</h5>
<ul>
  <li>Fixed a bug where a Content Card without a key-value pair could cause a crash.</li>
</ul>

<h2 id="2300">2.30.0</h2>

<h5 id="breaking-15">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v21.0.0">Braze Android SDK 21.0.0</a>.</li>
  <li>Removed “logContentCardsDisplayed” from the javascript plugin.</li>
</ul>

<h2 id="2290">2.29.0</h2>

<h5 id="breaking-16">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v19.0.0">Braze Android SDK 19.0.0</a>.</li>
</ul>

<h5 id="changed-2">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/releases/tag/4.4.2">Braze iOS SDK 4.4.2</a>.</li>
</ul>

<h2 id="2280">2.28.0</h2>

<h5 id="breaking-17">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v18.0.1">Braze Android SDK 18.0.1</a>.</li>
</ul>

<h5 id="fixed-7">Fixed</h5>
<ul>
  <li>Fixed an error around locating certain iOS resources when integrating the SDK.</li>
</ul>

<h2 id="2270">2.27.0</h2>

<h5 id="breaking-18">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v17.0.0">Braze Android SDK 17.0.0</a>.</li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/releases/tag/4.4.0">Braze iOS SDK 4.4.0</a>.</li>
</ul>

<h5 id="added-15">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">addToSubscriptionGroup()</code> and <code class="language-plaintext highlighter-rouge">removeFromSubscriptionGroup()</code>.</li>
</ul>

<h2 id="2260">2.26.0</h2>

<h5 id="breaking-19">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v16.0.0">Braze Android SDK 16.0.0</a>.</li>
</ul>

<h5 id="fixed-8">Fixed</h5>
<ul>
  <li>Fixed an issue in pre Android P WebViews where the system WebView would not properly handle view focus being returned to it.
    <ul>
      <li>https://issuetracker.google.com/issues/36915710 for more information.</li>
      <li>This fix is applied by default and can be disabled via <code class="language-plaintext highlighter-rouge">com.braze.android_apply_cordova_webview_focus_request_fix</code> in your <code class="language-plaintext highlighter-rouge">config.xml</code>.</li>
      <li>When enabled, this fix sets a custom In App Message view vrapper factory with the native Android SDK, potentially overriding any other custom set view factories.</li>
    </ul>
  </li>
</ul>

<h2 id="2250">2.25.0</h2>

<h5 id="breaking-20">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v15.0.0">Braze Android SDK 15.0.0</a>.</li>
</ul>

<h5 id="changed-3">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/releases/tag/4.3.2">Braze iOS SDK 4.3.2</a>.</li>
</ul>

<h5 id="added-16">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">Other</code>, <code class="language-plaintext highlighter-rouge">Unknown</code>, <code class="language-plaintext highlighter-rouge">Not Applicable</code>, and <code class="language-plaintext highlighter-rouge">Prefer not to Say</code> options for user gender.</li>
</ul>

<h2 id="2240">2.24.0</h2>

<h5 id="breaking-21">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v14.0.1">Braze Android SDK 14.0.1</a>.</li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/releases/tag/4.3.0">Braze iOS SDK 4.3.0</a>.</li>
</ul>

<h5 id="changed-4">Changed</h5>
<ul>
  <li>(minor) Changed logcat tag for Android plugin to be <code class="language-plaintext highlighter-rouge">BrazeCordova</code>.</li>
</ul>

<h2 id="2230">2.23.0</h2>

<h5 id="breaking-22">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312">Braze Android SDK 13.1.2</a>.</li>
</ul>

<h2 id="2220">2.22.0</h2>

<h5 id="breaking-23">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v13.0.0">Braze Android SDK 13.0.0</a>.</li>
</ul>

<h5 id="added-17">Added</h5>
<ul>
  <li>Added the ability to delay automatic session tracking for Android.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">&lt;preference name="com.appboy.android_disable_auto_session_tracking" value="true" /&gt;</code> in your <code class="language-plaintext highlighter-rouge">config.xml</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="2210">2.21.0</h2>

<h5 id="breaking-24">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3311">Braze iOS SDK 3.31.1</a>.</li>
</ul>

<h5 id="fixed-9">Fixed</h5>
<ul>
  <li>Fixed an issue on iOS where the plugin was incompatible with other Cordova plugins that have the <code class="language-plaintext highlighter-rouge">use_frameworks</code> Cocoapods setting in their <code class="language-plaintext highlighter-rouge">Podfile</code>.</li>
</ul>

<h5 id="added-18">Added</h5>
<ul>
  <li>Added the ability to disable <code class="language-plaintext highlighter-rouge">UNAuthorizationOptionProvisional</code> on iOS. Within <code class="language-plaintext highlighter-rouge">config.xml</code>, set <code class="language-plaintext highlighter-rouge">com.appboy.ios_disable_un_authorization_option_provisional</code> to <code class="language-plaintext highlighter-rouge">YES</code> to disable <code class="language-plaintext highlighter-rouge">UNAuthorizationOptionProvisional</code>.</li>
</ul>

<h2 id="2200">2.20.0</h2>

<h5 id="added-19">Added</h5>
<ul>
  <li>Added the method <code class="language-plaintext highlighter-rouge">getDeviceId()</code> to the javascript plugin.</li>
</ul>

<h2 id="2190">2.19.0</h2>

<h5 id="breaking-25">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3291">Braze iOS SDK 3.29.1</a>.</li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v11.0.0">Braze Android SDK 11.0.0</a>.</li>
</ul>

<h5 id="fixed-10">Fixed</h5>
<ul>
  <li>Fixed an issue where the plugin would automatically add the In-app Purchase capability to XCode projects.</li>
</ul>

<h5 id="added-20">Added</h5>
<ul>
  <li>Added the methods <code class="language-plaintext highlighter-rouge">addAlias()</code> and <code class="language-plaintext highlighter-rouge">setLanguage()</code> to the javascript plugin.</li>
</ul>

<h2 id="2180">2.18.0</h2>

<h5 id="breaking-26">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v10.0.0">Braze Android SDK 10.0.0</a>.</li>
</ul>

<h2 id="2170">2.17.0</h2>

<h5 id="breaking-27">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3270">Braze iOS SDK 3.27.0</a>. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.</li>
</ul>

<h2 id="2160">2.16.0</h2>

<h5 id="changed-5">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v8.1.0">Braze Android SDK 8.1.0</a>.</li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3261">Braze iOS SDK 3.26.1</a>.</li>
</ul>

<h5 id="added-21">Added</h5>
<ul>
  <li>Added the ability to display notifications while app is in the foreground in iOS. Within <code class="language-plaintext highlighter-rouge">config.xml</code> set <code class="language-plaintext highlighter-rouge">com.appboy.display_foreground_push_notifications</code> to <code class="language-plaintext highlighter-rouge">"YES"</code> to enable this.</li>
</ul>

<h2 id="2150">2.15.0</h2>

<h5 id="changed-6">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3230">Braze iOS SDK 3.23.0</a>.</li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v8.0.1">Braze Android SDK 8.0.1</a>.</li>
</ul>

<h2 id="2140">2.14.0</h2>

<h5 id="changed-7">Changed</h5>
<ul>
  <li>Reverted iOS plugin to use framework tag in <code class="language-plaintext highlighter-rouge">plugin.xml</code>.</li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v7.0.0">Braze Android SDK 7.0.0</a>.</li>
</ul>

<h2 id="2130">2.13.0</h2>

<h5 id="added-22">Added</h5>
<ul>
  <li>Added the Content Cards methods <code class="language-plaintext highlighter-rouge">requestContentCardsRefresh(), getContentCardsFromServer(), getContentCardsFromCache(), launchContentCards(), logContentCardsDisplayed(), logContentCardClicked(), logContentCardImpression(), logContentCardDismissed()</code> to the javascript plugin.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">getContentCardsFromServer(), getContentCardsFromCache()</code> both take a success and error callback to handle return values.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-8">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v4.0.2">Braze Android SDK 4.0.2</a>.</li>
</ul>

<h2 id="2120">2.12.0</h2>

<h5 id="changed-9">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v3.8.0">Braze Android SDK 3.8.0</a>.</li>
  <li>Pinned Android Gradle plugin version to 3.5.1 in <code class="language-plaintext highlighter-rouge">build-extras.gradle</code>.
    <ul>
      <li>Addresses https://github.com/braze-inc/braze-cordova-sdk/issues/46.</li>
    </ul>
  </li>
</ul>

<h2 id="2112">2.11.2</h2>

<p><strong>Important:</strong> This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md">Braze iOS SDK Changelog</a> for more information.</p>

<h5 id="changed-10">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3202">Braze iOS SDK 3.20.2</a>.</li>
</ul>

<h2 id="2111">2.11.1</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 2.11.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 2.11.2 or above if you make use of HTML in-app messages.</p>

<h5 id="changed-11">Changed</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3201">Braze iOS SDK 3.20.1</a>.</li>
</ul>

<h2 id="2110">2.11.0</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 2.11.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 2.11.2 or above if you make use of HTML in-app messages.</p>

<h5 id="breaking-28">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3200">Braze iOS SDK 3.20.0</a>.</li>
  <li><strong>Important:</strong> Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to this version as soon as possible to ensure a smooth transition as devices upgrade to iOS 13.</li>
  <li>Removes the Feedback feature.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">submitFeedback()</code> and <code class="language-plaintext highlighter-rouge">launchFeedback()</code> have been removed from the <code class="language-plaintext highlighter-rouge">AppboyPlugin</code> interface.</li>
    </ul>
  </li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v3.7.0">Braze Android SDK 3.7.0</a>.</li>
</ul>

<h5 id="added-23">Added</h5>
<ul>
  <li>Added ability to configure location collection in preferences. Braze location collection is now disabled by default.
    <ul>
      <li>Set <code class="language-plaintext highlighter-rouge">com.appboy.enable_location_collection</code> to <code class="language-plaintext highlighter-rouge">true/false</code> on Android.</li>
      <li>Set <code class="language-plaintext highlighter-rouge">com.appboy.enable_location_collection</code> to <code class="language-plaintext highlighter-rouge">YES/NO</code> on iOS.</li>
    </ul>
  </li>
  <li>Added ability to configure geofences in preferences. Note that the geofences branch is still required to use Braze Geofences out of the box.
    <ul>
      <li>Set <code class="language-plaintext highlighter-rouge">com.appboy.geofences_enabled</code> to <code class="language-plaintext highlighter-rouge">true/false</code> on Android.</li>
      <li>Set <code class="language-plaintext highlighter-rouge">com.appboy.geofences_enabled</code> to <code class="language-plaintext highlighter-rouge">YES/NO</code> on iOS.</li>
    </ul>
  </li>
</ul>

<h2 id="2101">2.10.1</h2>

<h5 id="fixed-11">Fixed</h5>
<ul>
  <li>Fixed an issue in the iOS plugin where custom endpoints were not correctly getting substituted for the actual server endpoints.</li>
</ul>

<h2 id="2100">2.10.0</h2>

<h5 id="breaking-29">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3141">Braze iOS SDK 3.14.1</a>.</li>
</ul>

<h5 id="added-24">Added</h5>
<ul>
  <li>Added ability for plugin to automatically collect the IDFA information on iOS. To enable, set <code class="language-plaintext highlighter-rouge">com.appboy.ios_enable_idfa_automatic_collection</code> to <code class="language-plaintext highlighter-rouge">YES</code> in your <code class="language-plaintext highlighter-rouge">config.xml</code> project file.
    <ul>
      <li>
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>&lt;platform name="ios"&gt;
    &lt;preference name="com.appboy.ios_enable_idfa_automatic_collection" value="YES" /&gt;
&lt;/platform&gt;
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
</ul>

<h5 id="fixed-12">Fixed</h5>
<ul>
  <li>Fixed an issue in the Android plugin where the Braze SDK could be invoked before <code class="language-plaintext highlighter-rouge">pluginInitialize</code> was called by Cordova. The plugin now explicitly initializes the SDK before any SDK or Android lifecycle methods are called.
    <ul>
      <li>Fixes https://github.com/braze-inc/braze-cordova-sdk/issues/38</li>
    </ul>
  </li>
</ul>

<h2 id="290">2.9.0</h2>

<h5 id="breaking-30">Breaking</h5>
<ul>
  <li>Updated to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3140">Braze iOS SDK 3.14.0</a>.</li>
  <li>Updated to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#322">Braze Android SDK 3.2.2</a>.</li>
</ul>

<h5 id="changed-12">Changed</h5>
<ul>
  <li>Changed the iOS plugin to use Cocoapods instead of a framework integration.</li>
  <li>Improved the look and feel of in-app messages to adhere to the latest UX and UI best practices. Changes affect font sizes, padding, and responsiveness across all message types. Now supports button border styling.</li>
</ul>

<h5 id="fixed-13">Fixed</h5>
<ul>
  <li>Fixed the Android plugin not respecting decimal purchase prices.
    <ul>
      <li>Fixes https://github.com/braze-inc/braze-cordova-sdk/issues/36.</li>
    </ul>
  </li>
</ul>

<h2 id="280">2.8.0</h2>
<ul>
  <li>Changed the iOS frameworks to be automatically embedded in the <code class="language-plaintext highlighter-rouge">plugin.xml</code>.
    <ul>
      <li>This fixes the “dyld: Library not loaded” issue raised in XCode if the frameworks were not manually embedded.</li>
    </ul>
  </li>
  <li>Adds method to immediately flush any pending data via <code class="language-plaintext highlighter-rouge">requestImmediateDataFlush()</code>.</li>
</ul>

<h2 id="271">2.7.1</h2>
<ul>
  <li>Fixes an issue where sending push on Android resulted in a crash in version 2.7.0. Past versions (before 2.7.0) are unaffected.</li>
</ul>

<h2 id="270">2.7.0</h2>
<ul>
  <li>Updates Braze Android version to 3.0.0+
    <ul>
      <li>Removes GCM push registration methods. In your config.xml <code class="language-plaintext highlighter-rouge">com.appboy.android_automatic_push_registration_enabled</code> and <code class="language-plaintext highlighter-rouge">com.appboy.android_gcm_sender_id</code> , now have no effect on push registration.</li>
    </ul>
  </li>
  <li>Updates Braze iOS version to 3.9.0.</li>
</ul>

<h2 id="260">2.6.0</h2>
<ul>
  <li>Fixes an issue where the Cordova 8.0.0+ build system would convert numeric preferences in the <code class="language-plaintext highlighter-rouge">config.xml</code> to be floating point numbers.
    <ul>
      <li>Numeric preferences, such as sender ids, now should be prefixed with <code class="language-plaintext highlighter-rouge">str_</code> for correct parsing. I.e. <code class="language-plaintext highlighter-rouge">&lt;preference name="com.appboy.android_fcm_sender_id" value="str_64422926741" /&gt;</code>.</li>
    </ul>
  </li>
  <li>Updates Braze Android version to 2.6.0+</li>
</ul>

<h2 id="251">2.5.1</h2>
<ul>
  <li>Updates Braze Android version to 2.4.0+.</li>
  <li>Adds Firebase Cloud Messaging automatic registration support. GCM automatic registration should be disabled by setting the config value “com.appboy.android_automatic_push_registration_enabled” to “false”. See the Android sample-project’s <code class="language-plaintext highlighter-rouge">config.xml</code> for an example. FCM <code class="language-plaintext highlighter-rouge">config.xml</code> keys below.
    <ul>
      <li>“com.appboy.firebase_cloud_messaging_registration_enabled” (“true”/”false”)</li>
      <li>“com.appboy.android_fcm_sender_id” (String)</li>
      <li>The Firebase dependencies <code class="language-plaintext highlighter-rouge">firebase-messaging</code> and <code class="language-plaintext highlighter-rouge">firebase-core</code> are now included automatically as part of the plugin.</li>
    </ul>
  </li>
</ul>

<h2 id="250">2.5.0</h2>
<ul>
  <li>Updates Braze Android version to 2.2.5+.</li>
  <li>Updates Braze iOS version to 3.3.4.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">wipeData()</code>, <code class="language-plaintext highlighter-rouge">enableSdk()</code>, and <code class="language-plaintext highlighter-rouge">disableSdk()</code> methods to the plugin.</li>
</ul>

<h2 id="240">2.4.0</h2>
<ul>
  <li>Fixes a subdirectory incompatibility issue with Cordova 7.1.0</li>
</ul>

<h2 id="232">2.3.2</h2>
<ul>
  <li>Adds configuration for custom API endpoints on iOS and Android using the config.xml.
    <ul>
      <li>Android preference: “com.appboy.android_api_endpoint”</li>
      <li>iOS preference: “com.appboy.ios_api_endpoint”</li>
    </ul>
  </li>
</ul>

<h2 id="231">2.3.1</h2>
<ul>
  <li>Adds getter for all News Feed cards. Thanks to @cwelk for contributing.</li>
  <li>Adds a git branch <code class="language-plaintext highlighter-rouge">geofence-branch</code> for registering geofences with Google Play Services and messaging on geofence events. Please reach out to success@appboy.com for more information about this feature. The branch has geofences integrated for both Android and iOS.</li>
</ul>

<h2 id="230">2.3.0</h2>
<ul>
  <li>Fixes in-app messages display issue on iOS.</li>
  <li>Updates Appboy iOS version to 2.29.0</li>
  <li>Updates Appboy Android version to 2.0+</li>
  <li>Fixes original in-app messages not being requested on Android.</li>
</ul>

<h2 id="220">2.2.0</h2>
<ul>
  <li>Updates Appboy Android version to 1.18+</li>
  <li>Updates Appboy iOS version to 2.25.0</li>
  <li>Adds the ability to configure the Android Cordova SDK using the config.xml. See the Android sample-project’s <code class="language-plaintext highlighter-rouge">config.xml</code> for an example.
    <ul>
      <li>Supported keys below, see <a href="https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/configuration/BrazeConfig.Builder.html">the AppboyConfig.Builder javadoc</a> for more details</li>
      <li>“com.appboy.api_key” (String)</li>
      <li>“com.appboy.android_automatic_push_registration_enabled” (“true”/”false”)</li>
      <li>“com.appboy.android_gcm_sender_id” (String)</li>
      <li>“com.appboy.android_small_notification_icon” (String)</li>
      <li>“com.appboy.android_large_notification_icon” (String)</li>
      <li>“com.appboy.android_notification_accent_color” (Integer)</li>
      <li>“com.appboy.android_default_session_timeout” (String)</li>
      <li>“com.appboy.android_handle_push_deep_links_automatically” (“true”/”false”)</li>
      <li>“com.appboy.android_log_level” (Integer) can also be configured here, for obtaining debug logs from the Appboy Android SDK</li>
    </ul>
  </li>
  <li>Updates the Android Cordova SDK to use the <a href="https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/BrazeActivityLifecycleCallbackListener.html">Appboy Lifecycle listener</a> to handle session and in-app message registration</li>
</ul>

<h2 id="210">2.1.0</h2>
<ul>
  <li>Adds support for iOS 10 push registration and handling using the UNUserNotificationCenter.</li>
  <li>Adds functionality for turning off automatic push registration on iOS. To disable, add the preference <code class="language-plaintext highlighter-rouge">com.appboy.ios_disable_automatic_push_handling</code> with a value of <code class="language-plaintext highlighter-rouge">YES</code>.</li>
</ul>

<h2 id="200">2.0.0</h2>
<ul>
  <li>Updates to add functionality for turning off automatic push registration on iOS.  If you want to turn off iOS default push registration, add the preference <code class="language-plaintext highlighter-rouge">com.appboy.ios_disable_automatic_push_registration</code> with a value of <code class="language-plaintext highlighter-rouge">YES</code>.</li>
  <li>Includes patch for iOS 10 push open bug.  See https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#2240 for more information.</li>
  <li>Updates Appboy iOS version to 2.24.2.</li>
  <li>Updates Appboy Android version to 1.15+.</li>
  <li>Updates plugin to configure Android via parameters to eliminate need for post-install modifications on Android. Ported from https://github.com/Appboy/appboy-cordova-sdk/tree/feature/android-variable-integration.</li>
</ul>

<h2 id="01">0.1</h2>
<ul>
  <li>Initial release. Adds support for Appboy Android version 1.12+ and Appboy iOS version 2.18.1.</li>
</ul>




**Tip:**


You can also find a copy of the [Flutter Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-flutter-sdk/blob/master/CHANGELOG.md).



<h2 id="1801">18.0.1</h2>

<h5 id="fixed">Fixed</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">Braze.registerPushToken()</code> now explicitly enforces that the device token is a hex-encoded string for the iOS implementation.
    <ul>
      <li>This addresses previously reported issues of tokens being improperly converted.</li>
    </ul>
  </li>
</ul>

<h2 id="1800">18.0.0</h2>

<h4 id="breaking">Breaking</h4>
<ul>
  <li>Streamlines the iOS integration process to not require writing native code to forward content cards, banners, feature flags, in-app messages, or push notification updates from the native SDK.
    <ul>
      <li>The SDK will now automatically set up these subscriptions when the Braze instance is created.</li>
      <li>This matches the existing behavior on Android.</li>
      <li>To migrate, remove any manual calls to <code class="language-plaintext highlighter-rouge">braze.contentCards.subscribeToUpdates()</code>, <code class="language-plaintext highlighter-rouge">braze.banners.subscribeToUpdates()</code>, <code class="language-plaintext highlighter-rouge">braze.notifications.subscribeToUpdates</code>, <code class="language-plaintext highlighter-rouge">braze.featureFlags.subscribeToUpdates</code> and <code class="language-plaintext highlighter-rouge">braze.inAppMessagePresenter</code> in the <code class="language-plaintext highlighter-rouge">AppDelegate</code>.</li>
      <li>By default, in-app messages will be presented. To override this, set a custom in-app message presenter using the <code class="language-plaintext highlighter-rouge">postInitialization</code> closure in <code class="language-plaintext highlighter-rouge">BrazePlugin.configure(_:postInitialization:)</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="added">Added</h5>
<ul>
  <li>Adds support for delayed SDK initialization. See full setup guide <a href="https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter">here</a>.
    <ul>
      <li>Adds <code class="language-plaintext highlighter-rouge">initialize(apiKey, endpoint)</code> method to create the Braze instance at runtime with the stored configuration. This method can be called multiple times to re-initialize the SDK with a different API key and endpoint mid-session.</li>
      <li>To enable delayed initialization on Android, add <code class="language-plaintext highlighter-rouge">com_braze_enable_delayed_initialization</code> set to <code class="language-plaintext highlighter-rouge">true</code> in your <code class="language-plaintext highlighter-rouge">braze.xml</code>.</li>
    </ul>
  </li>
  <li>For iOS integrations only, adds <code class="language-plaintext highlighter-rouge">BrazePlugin.configure(_:postInitialization:)</code> to store configurations in your <code class="language-plaintext highlighter-rouge">AppDelegate</code> for later use by the new Dart <code class="language-plaintext highlighter-rouge">initialize(apiKey, endpoint)</code> method.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.initBraze()</code> is deprecated. Use the <code class="language-plaintext highlighter-rouge">configure</code> + Dart <code class="language-plaintext highlighter-rouge">initialize</code> pattern instead.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/14.0.1...14.0.4#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 14.0.1 to 14.0.4</a>.</li>
</ul>

<h2 id="1710">17.1.0</h2>

<h5 id="added-1">Added</h5>
<ul>
  <li>Adds support to import the Flutter iOS package via Swift Package Manager (SPM).
    <ul>
      <li>The Braze Flutter SDK still supports CocoaPods integrations at this time.</li>
      <li>For instructions on how to migrate from CocoaPods to SPM, reference <a href="https://docs.flutter.dev/packages-and-plugins/swift-package-manager/for-app-developers">Flutter’s official docs</a>.</li>
      <li>The minimum Flutter version of the Braze SDK remains unchanged, but integration with SPM requires Flutter version <code class="language-plaintext highlighter-rouge">3.24.0</code> or higher.</li>
    </ul>
  </li>
  <li>The Flutter iOS sample app has been updated to use SPM to import the Braze SDK.
    <ul>
      <li>This also removes all relevant files to the CocoaPods integration for the sample app.</li>
    </ul>
  </li>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v41.0.0...v41.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 41.0.0 to 41.1.1</a>.</li>
</ul>

<h2 id="1700">17.0.0</h2>

<h5 id="breaking-1">Breaking</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 13.3.0 to 14.0.1</a>.</li>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v40.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 40.0.0 to 41.0.0</a>.</li>
</ul>

<h5 id="added-2">Added</h5>
<ul>
  <li>Adds support for logging banner analytics to Braze using <code class="language-plaintext highlighter-rouge">BrazeBanner</code> instances.
    <ul>
      <li>See <code class="language-plaintext highlighter-rouge">logBannerClicked(placementId:buttonId:)</code> and <code class="language-plaintext highlighter-rouge">logBannerImpression(placementId:)</code> on the <code class="language-plaintext highlighter-rouge">BrazePlugin</code> interface.</li>
    </ul>
  </li>
</ul>

<h2 id="1600">16.0.0</h2>

<h5 id="breaking-2">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 39.0.0 to 40.0.0</a>.</li>
</ul>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Banner views will no longer call <code class="language-plaintext highlighter-rouge">setState</code> extraneously if the view component is not mounted.
    <ul>
      <li>Previously, this could cause an exception to occur if the Banner tried to update its height while the view was not mounted within the widget hierarchy.</li>
    </ul>
  </li>
  <li>Fixes UI flickering and display issues with <code class="language-plaintext highlighter-rouge">BrazeBannerView</code> when navigating between screens on Android</li>
</ul>

<h5 id="added-3">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 13.2.0 to 13.3.0</a>.</li>
</ul>

<h2 id="1510">15.1.0</h2>

<h5 id="added-4">Added</h5>
<ul>
  <li>Adds support for Banner properties via new public methods for <code class="language-plaintext highlighter-rouge">BrazeBanner</code>.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">banner.getStringProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">String</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getNumberProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">num</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getTimestampProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">int</code> Unix UTC millisecond timestamp  properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getBooleanProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">bool</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getImageProperty(key:)</code> for accessing image URL properties as <code class="language-plaintext highlighter-rouge">String</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getJSONProperty(key:)</code> for accessing JSON properties as <code class="language-plaintext highlighter-rouge">Map&lt;String, dynamic&gt;</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="1500">15.0.0</h2>

<h5 id="breaking-3">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 36.0.0 to 39.0.0</a>.</li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 12.0.0 to 13.2.0</a>.
    <ul>
      <li>This includes Xcode 26 support.</li>
    </ul>
  </li>
</ul>

<h5 id="added-5">Added</h5>
<ul>
  <li>Adds the ability to unset the following user attributes by setting these values to <code class="language-plaintext highlighter-rouge">null</code>:
    <ul>
      <li>First name</li>
      <li>Last name</li>
      <li>Phone number</li>
      <li>Email</li>
      <li>Gender</li>
      <li>Language</li>
      <li>Home city</li>
      <li>Country</li>
    </ul>
  </li>
</ul>

<h2 id="1403">14.0.3</h2>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Fixes missing <code class="language-plaintext highlighter-rouge">Braze</code> symbol error in <code class="language-plaintext highlighter-rouge">BrazeBannerViewFactory</code> when using dynamically-linked frameworks.</li>
</ul>

<h2 id="1402">14.0.2</h2>

<blockquote>
  <p>[!IMPORTANT]
This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. However, we are not reintroducing formal support for &lt; API 25. Read more <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600">here</a>.</p>
</blockquote>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Fixes a display issue introduced in <code class="language-plaintext highlighter-rouge">14.0.1</code> when changing a Banner dynamically.</li>
  <li>The <code class="language-plaintext highlighter-rouge">minSdk</code> enforced by the Flutter Android layer is now downgraded from <code class="language-plaintext highlighter-rouge">25</code> to <code class="language-plaintext highlighter-rouge">21</code>, matching the <code class="language-plaintext highlighter-rouge">minSdk</code> in the Android native layer.</li>
</ul>

<h2 id="1401">14.0.1</h2>

<h5 id="fixed-5">Fixed</h5>
<ul>
  <li>Fixes a crash on iOS when the app is force-closed while a Banner is visible on the screen.
    <ul>
      <li>Note: This fix may cause display issues when trying to change Banners dynamically. This will be addressed in a future patch.</li>
    </ul>
  </li>
</ul>

<h2 id="1400">14.0.0</h2>

<p>⚠️ <strong>Important:</strong> This version has a known issue related to Banners. Upgrade to version <code class="language-plaintext highlighter-rouge">14.0.2</code> instead.</p>

<h5 id="breaking-4">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 35.0.0 to 36.0.0</a>.</li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.9.0...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.9.0 to 12.0.0</a>.</li>
</ul>

<h5 id="fixed-6">Fixed</h5>
<ul>
  <li>Fixes an issue on iOS where <code class="language-plaintext highlighter-rouge">getUserId()</code> would not return any value if the user was anonymous.
    <ul>
      <li>This API will now return <code class="language-plaintext highlighter-rouge">null</code> if the user is anonymous.</li>
    </ul>
  </li>
  <li>Fixes the iOS implementation of <code class="language-plaintext highlighter-rouge">setDateOfBirth</code> to correctly report dates using the Gregorian calendar instead of the user’s device calendar.
    <ul>
      <li>Previously, the SDK would re-format the input date components with the device’s calendar settings if they were non-Gregorian.</li>
    </ul>
  </li>
  <li>Fixes the in-app message data model to reflect the correct types under the following circumstances:
    <ul>
      <li>HTML in-app messages will now reflect their correct type <code class="language-plaintext highlighter-rouge">html</code>, instead of the default <code class="language-plaintext highlighter-rouge">slideup</code> type.</li>
      <li>Full in-app messages will now reflect their correct type <code class="language-plaintext highlighter-rouge">full</code>, instead of incorrectly being marked as <code class="language-plaintext highlighter-rouge">html_full</code>. HTML full messages will still continue to work as expected.</li>
    </ul>
  </li>
</ul>

<h2 id="1300">13.0.0</h2>

<p>⚠️ <strong>Important:</strong> This version has a known issue related to Banners. Upgrade to version <code class="language-plaintext highlighter-rouge">14.0.2</code> instead.</p>

<h5 id="breaking-5">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 33.0.0 to 35.0.0</a>.
    <ul>
      <li>The minimum required Android SDK version is 25. See more details <a href="https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information">here</a>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-6">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">BrazeBannerView</code> widget to display a Banner Card directly in Dart.
    <ul>
      <li>To use this feature, insert the widget <code class="language-plaintext highlighter-rouge">BrazeBannerView(placementId:)</code> into your Dart view hierarchy with the relevant <code class="language-plaintext highlighter-rouge">placementId</code>.</li>
      <li>Reference our integration in our <a href="https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart">sample app</a>.</li>
    </ul>
  </li>
  <li>Adds support for the Braze Banner Cards product and APIs to utilize them.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.requestBannersRefresh(List&lt;String&gt; placementIds)</code> - to request a refresh of the banners associated with the provided placement IDs. This must be called at least once to set the list of banners to retrieve. On iOS only, failures will be logged if unsuccessful.</li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.getBanner(String placementId)</code> - to get a banner with the provided placement ID if available in cache, otherwise returns null.</li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.subscribeToBanners(void Function(List&lt;BrazeBanner&gt;) onEvent)</code> - to subscribe to the stream of banners and call [onEvent] when it receives the list of banners.</li>
    </ul>
  </li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.6.1 to 11.9.0</a>.</li>
</ul>

<h2 id="1211">12.1.1</h2>

<h5 id="added-7">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.6.0...11.6.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.6.0 to 11.6.1</a>.</li>
</ul>

<h2 id="1210">12.1.0</h2>

<h5 id="added-8">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.3.0...11.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.3.0 to 11.6.0</a>.</li>
</ul>

<h2 id="1200">12.0.0</h2>

<h5 id="breaking-6">Breaking</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 10.3.1 to 11.3.0</a>.</li>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 32.1.0 to 33.1.0</a>.</li>
</ul>

<h2 id="1110">11.1.0</h2>

<h5 id="added-9">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.2.0...10.3.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 10.2.0 to 10.3.1</a>.</li>
</ul>

<h2 id="1100">11.0.0</h2>

<h5 id="breaking-7">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.4.0 to 32.1.0</a>.
    <ul>
      <li>Changes the behavior of <code class="language-plaintext highlighter-rouge">wipeData()</code> on Android to retain external subscriptions (like <code class="language-plaintext highlighter-rouge">subscribeToContentCards()</code>) after being called.</li>
    </ul>
  </li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 9.0.0 to 10.2.0</a>.</li>
</ul>

<h5 id="added-10">Added</h5>
<ul>
  <li>Adds support for 3 new Feature Flag property types:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.getTimestampProperty(String key)</code> for accessing Int Unix UTC millisecond timestamps as <code class="language-plaintext highlighter-rouge">int?</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.getJSONProperty(String key)</code> for accessing JSON objects as <code class="language-plaintext highlighter-rouge">Map&lt;String, dynamic&gt;?</code> types.</li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.getImageProperty(String key)</code> for accessing image URLs as <code class="language-plaintext highlighter-rouge">String?</code>s.</li>
    </ul>
  </li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">getUserId()</code> method to get the ID of the current user. This method will return <code class="language-plaintext highlighter-rouge">null</code> if the current user is anonymous.</li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">hideCurrentInAppMessage()</code> method, which dismisses the currently displayed in-app message.</li>
</ul>

<h5 id="fixed-7">Fixed</h5>
<ul>
  <li>Fixes an issue on Android where push notification stream subscriptions were not receiving events after clicking on a push notification when the app was in a terminated state.
    <ul>
      <li>Thank you @Neelansh-ns for the contribution!</li>
    </ul>
  </li>
</ul>

<h2 id="1010">10.1.0</h2>

<h5 id="added-11">Added</h5>
<ul>
  <li>Updated the Android Gradle plugin from <code class="language-plaintext highlighter-rouge">8.0.2</code> to <code class="language-plaintext highlighter-rouge">8.1.1</code>.</li>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v30.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.3.0 to 30.4.0</a>.</li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">BrazeInAppMessage.isTestSend</code> property, which indicates whether an in-app message was triggered as part of a test send.</li>
</ul>

<h2 id="1000">10.0.0</h2>

<h5 id="breaking-8">Breaking</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 8.4.0 to 9.0.0</a>.</li>
</ul>

<h5 id="added-12">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">getDeviceId</code> method to replace <code class="language-plaintext highlighter-rouge">getInstallTrackingId</code>, which is now deprecated.</li>
</ul>

<h5 id="fixed-8">Fixed</h5>
<ul>
  <li>Fixes an issue where StrictMode DiskReadViolation was triggered on Android.
    <ul>
      <li>Thanks @radivojeostojic for pointing this out.</li>
    </ul>
  </li>
</ul>

<h2 id="900">9.0.0</h2>

<h5 id="breaking-9">Breaking</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.7.0 to 8.4.0</a>.
    <ul>
      <li>The minimum iOS deployment target has been updated to 12.0.</li>
      <li>The minimum supported Xcode version is 15.2.</li>
    </ul>
  </li>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 29.0.1 to 30.3.0</a>.</li>
  <li>The minimum supported Dart version is <code class="language-plaintext highlighter-rouge">2.15.0</code>.</li>
  <li>The minimum supported Swift Language Version is Swift 5.</li>
</ul>

<h5 id="added-13">Added</h5>
<ul>
  <li>Push notification payloads are now accessible in the Dart layer by calling <code class="language-plaintext highlighter-rouge">subscribeToPushNotificationEvents(void Function(BrazePushEvent) onEvent)</code>. This allows you to run custom Dart code after a push is received or when a push is clicked.
    <ul>
      <li>On iOS, this callback can only be triggered for push click events.</li>
      <li>Reference our <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/flutter/push_notifications">Flutter Push Notification documentation</a> with details on how to utilize this feature.</li>
      <li>This feature is compatible with the <code class="language-plaintext highlighter-rouge">replayCallbacksConfigKey</code> to replay the push event callback for any notifications that were received prior to calling <code class="language-plaintext highlighter-rouge">subscribeToPushNotificationEvents</code>.</li>
      <li>Due to <a href="https://github.com/flutter/flutter/issues/155479">an issue in the Flutter framework</a>, this feature is not compatible with subscribing to <a href="https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app#Receive-background-notifications">iOS silent push notifications</a>.</li>
    </ul>
  </li>
  <li>Adds support for Braze tracking properties.
    <ul>
      <li>Adds the <code class="language-plaintext highlighter-rouge">updateTrackingPropertyAllowList(allowList)</code> method to dynamically configure Braze tracking properties.</li>
      <li>For further usage details, refer to the <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/">Swift privacy manifest documentation</a>.</li>
    </ul>
  </li>
  <li>Deprecates <code class="language-plaintext highlighter-rouge">setGoogleAdvertisingId(id, adTrackingEnabled)</code> in favor of <code class="language-plaintext highlighter-rouge">setAdTrackingEnabled(adTrackingEnabled, id)</code>.</li>
</ul>

<h2 id="820">8.2.0</h2>

<h5 id="added-14">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.3.0...7.7.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.3.0 to 7.7.0</a>.</li>
  <li>Adds example integrations for <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications">Braze Rich Push Notifications</a> and <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories">Braze Push Stories</a> to the iOS sample app.</li>
</ul>

<h5 id="fixed-9">Fixed</h5>
<ul>
  <li>Removes the automatic assignment of <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/delegate"><code class="language-plaintext highlighter-rouge">BrazeDelegate</code></a> in the iOS native layer, allowing for custom implementations to be assigned to the <code class="language-plaintext highlighter-rouge">braze</code> instance.
    <ul>
      <li>The plugin now uses the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazesdkauthdelegate"><code class="language-plaintext highlighter-rouge">sdkAuthDelegate</code> property</a> for the SDK Authentication feature instead.</li>
    </ul>
  </li>
</ul>

<h2 id="810">8.1.0</h2>

<h5 id="added-15">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.2.0...7.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.2.0 to 7.3.0</a>.</li>
</ul>

<h2 id="800">8.0.0</h2>

<h5 id="breaking-10">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 27.0.1 to 29.0.1</a>.</li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.6.1...7.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.6.1 to 7.2.0</a>.</li>
  <li>Modifies the behavior for Feature Flags methods.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.getFeatureFlagByID(String id)</code> will now return <code class="language-plaintext highlighter-rouge">null</code> if the feature flag does not exist.</li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.subscribeToFeatureFlags(void Function(List&lt;BrazeFeatureFlag&gt;) onEvent))</code> will only trigger in the following situations:
        <ul>
          <li>When a refresh request completes with success or failure.</li>
          <li>Upon initial subscription if there was previously cached data from the current session.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>The minimum supported Android SDK version is 21.</li>
</ul>

<h5 id="fixed-10">Fixed</h5>
<ul>
  <li>Moved the <code class="language-plaintext highlighter-rouge">compileSDKVersion</code> for Android down to 33 to match Flutter’s versioning.</li>
</ul>

<h2 id="700">7.0.0</h2>

<h5 id="breaking-11">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701">from Braze Android SDK 26.1.1 to 27.0.1</a>.</li>
  <li>Adds support for Gradle 8.</li>
</ul>

<h5 id="added-16">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.3.0...6.6.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.3.0 to 6.6.1</a>.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazePlugin.logFeatureFlagImpression(String id)</code> to log a Feature Flag impression.</li>
  <li>Adds support for custom user attributes to be nested objects.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazeUser.setNestedCustomUserAttribute()</code></li>
      <li><code class="language-plaintext highlighter-rouge">BrazeUser.setCustomUserAttributeArrayOfObjects()</code></li>
      <li>You can specify that the Dictionary be merged with the existing value.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">BrazeUser.setNestedCustomUserAttribute(string, Map&lt;string, dynamic&gt;, true)</code></li>
        </ul>
      </li>
      <li>See https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/ for more information.</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazeUser.setCustomUserAttributeArrayOfStrings()</code> to set arrays of strings as a custom attribute.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazePlugin.getCachedContentCards()</code> to get the most recent content cards from the cache.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazePlugin.registerPushToken()</code> to send a push token to Braze’s servers.
    <ul>
      <li>Deprecates <code class="language-plaintext highlighter-rouge">BrazePlugin.registerAndroidPushToken()</code> in favor of this new method.</li>
    </ul>
  </li>
  <li>Adds an example integration of iOS push notifications as well as custom scheme deep links, <a href="https://docs.flutter.dev/cookbook/navigation/set-up-universal-links">universal links</a> (iOS), and <a href="https://docs.flutter.dev/cookbook/navigation/set-up-app-links">app links</a> (Android) to the Flutter sample app.</li>
</ul>

<h2 id="601">6.0.1</h2>

<h5 id="fixed-11">Fixed</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2611">from Braze Android SDK 26.1.0 to 26.1.1</a>.</li>
</ul>

<h2 id="600">6.0.0</h2>

<h5 id="breaking-12">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v25.0.0...v26.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 25.0.0 to 26.1.0</a>.</li>
</ul>

<h5 id="fixed-12">Fixed</h5>
<ul>
  <li>Fixes an issue where <code class="language-plaintext highlighter-rouge">BrazeContentCard.imageAspectRatio</code> would always return <code class="language-plaintext highlighter-rouge">1</code> for whole-number <code class="language-plaintext highlighter-rouge">int</code> values.
    <ul>
      <li>The field <code class="language-plaintext highlighter-rouge">imageAspectRatio</code> is now a <code class="language-plaintext highlighter-rouge">num</code> type instead of a <code class="language-plaintext highlighter-rouge">double</code> type. No changes are required.</li>
    </ul>
  </li>
</ul>

<h5 id="added-17">Added</h5>
<ul>
  <li>Added support for Braze Feature Flags.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.getFeatureFlagByID(String id)</code> - Get a single Feature Flag</li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.getAllFeatureFlags()</code> - Get all Feature Flags</li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.refreshFeatureFlags()</code> - Request a refresh of Feature Flags</li>
      <li><code class="language-plaintext highlighter-rouge">BrazePlugin.subscribeToFeatureFlags(void Function(List&lt;BrazeFeatureFlag&gt;) onEvent))</code> - Subscribe to Feature Flag updates</li>
      <li>Feature Flag property getter methods for the following types:
        <ul>
          <li>Boolean: <code class="language-plaintext highlighter-rouge">featureFlag.getBooleanProperty(String key)</code></li>
          <li>Number: <code class="language-plaintext highlighter-rouge">featureFlag.getNumberProperty(String key)</code></li>
          <li>String: <code class="language-plaintext highlighter-rouge">featureFlag.getStringProperty(String key)</code></li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.0.0...6.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze iOS SDK 6.0.0 to 6.3.0</a>.</li>
</ul>

<h2 id="500">5.0.0</h2>

<h5 id="breaking-13">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2500">Braze Android SDK 25.0.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#600">Braze iOS SDK 6.0.0</a>.
    <ul>
      <li>If you wish to access remote URLs for in-app messages instead of local URLs, replace your implementation of the <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUIDelegate</code> method <code class="language-plaintext highlighter-rouge">inAppMessage(_:willPresent:view:)</code> with a custom implementation of <code class="language-plaintext highlighter-rouge">BrazeInAppMessagePresenter</code> or a <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUI</code> subclass. This is relevant if you are caching asset URLs outside of the Braze SDK.</li>
      <li>For reference, see our sample code <a href="https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift">here</a>.</li>
    </ul>
  </li>
</ul>

<h2 id="410">4.1.0</h2>

<h5 id="fixed-13">Fixed</h5>
<ul>
  <li>Fixes an issue in <code class="language-plaintext highlighter-rouge">4.0.0</code> where the version in <code class="language-plaintext highlighter-rouge">braze_plugin.podspec</code> was not incremented correctly.</li>
</ul>

<h5 id="changed">Changed</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#5120">Braze iOS SDK 5.12.0</a>.</li>
</ul>

<h2 id="400">4.0.0</h2>

<blockquote>
  <p>Starting with this release, this SDK will use <a href="https://semver.org/">Semantic Versioning</a>.</p>
</blockquote>

<h5 id="breaking-14">Breaking</h5>
<ul>
  <li>Fixes the behavior in the iOS bridge introduced in version <code class="language-plaintext highlighter-rouge">3.0.0</code> when logging clicks for in-app messages and content cards. Calling <code class="language-plaintext highlighter-rouge">logClick</code> now only sends a click event for metrics, instead of both sending a click event as well as redirecting to the associated <code class="language-plaintext highlighter-rouge">url</code> field.
    <ul>
      <li>For instance, to log a content card click and redirect to a URL, you will need two commands:
```
braze.logContentCardClicked(contentCard);</li>
    </ul>

    <p>// Your own custom implementation
Linking.openUrl(contentCard.url);
```</p>
    <ul>
      <li>This brings the iOS behavior to match version <code class="language-plaintext highlighter-rouge">2.x</code> and bring parity with Android’s behavior.</li>
    </ul>
  </li>
  <li>Removes <code class="language-plaintext highlighter-rouge">setBrazeInAppMessageCallback()</code> and <code class="language-plaintext highlighter-rouge">setBrazeContentCardsCallback()</code> in favor of subscribing via streams.
    <ul>
      <li>Reference our <a href="https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart">sample app</a> for an example on how to use <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/flutter/inapp_messages/#receiving-in-app-message-data"><code class="language-plaintext highlighter-rouge">subscribeToInAppMessages()</code></a> or <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/flutter/content_cards/#receiving-content-card-data"><code class="language-plaintext highlighter-rouge">subscribeToContentCards()</code></a>.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2430">Braze Android SDK 24.3.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#5112">Braze iOS SDK 5.11.2</a>.</li>
  <li>Improves behavior when using <code class="language-plaintext highlighter-rouge">replayCallbacksConfigKey</code> alongside having subscriptions to in-app messages or content cards via streams.</li>
</ul>

<h2 id="310">3.1.0</h2>

<h5 id="breaking-15">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2420">Braze Android SDK 24.2.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#590">Braze iOS SDK 5.9.0</a>.</li>
  <li>The minimum iOS deployment target is 11.0.</li>
</ul>

<h2 id="301">3.0.1</h2>

<h5 id="fixed-14">Fixed</h5>
<ul>
  <li>Updates the <code class="language-plaintext highlighter-rouge">braze_plugin.podspec</code> file to statically link the iOS framework by default. This prevents the need to do a manual step when migrating to <code class="language-plaintext highlighter-rouge">3.x.x</code>.</li>
  <li>Fixes an issue introduced in version <code class="language-plaintext highlighter-rouge">2.2.0</code> where the content cards callback was not being called when receiving an empty list of content cards.</li>
</ul>

<h2 id="300">3.0.0</h2>

<h5 id="breaking-16">Breaking</h5>
<ul>
  <li>The native iOS bridge now uses the <a href="https://github.com/braze-inc/braze-swift-sdk">new Braze Swift SDK</a>, <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#564">version 5.6.4</a>.
    <ul>
      <li>The minimum iOS deployment target is 10.0.</li>
    </ul>
  </li>
  <li>During migration, update your project with the following changes:
    <ul>
      <li>To initialize Braze, <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/a2-configure-braze">follow these integration steps</a> to create a <code class="language-plaintext highlighter-rouge">configuration</code> object. Then, add this code to complete the setup:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>let braze = BrazePlugin.initBraze(configuration)
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>This migration requires re-identifying users. To do so, you must call the <code class="language-plaintext highlighter-rouge">changeUser</code> method on the Braze instance for non-anonymous users. You can read more about it <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/#Re-identify-users">here</a>.</li>
      <li>To continue using <code class="language-plaintext highlighter-rouge">SDWebImage</code> as a dependency, add this line to your project’s <code class="language-plaintext highlighter-rouge">/ios/Podfile</code>:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>pod 'SDWebImage', :modular_headers =&gt; true
</pre></td></tr></tbody></table></code></pre></div>        </div>
        <ul>
          <li>Then, follow <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support">these setup instructions</a>.</li>
        </ul>
      </li>
      <li>For guidance around other changes such as receiving in-app message and content card data, reference our sample <a href="https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift"><code class="language-plaintext highlighter-rouge">AppDelegate.swift</code></a>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-18">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">isControl</code> field to <code class="language-plaintext highlighter-rouge">BrazeContentCard</code>.</li>
</ul>

<h5 id="changed-2">Changed</h5>
<ul>
  <li>Updates the parameter syntax for <code class="language-plaintext highlighter-rouge">subscribeToInAppMessages()</code> and <code class="language-plaintext highlighter-rouge">subscribeToContentCards()</code>.</li>
</ul>

<h2 id="261">2.6.1</h2>

<h5 id="added-19">Added</h5>
<ul>
  <li>Adds support to replay the <code class="language-plaintext highlighter-rouge">onEvent</code> method for queued in-app messages and content cards when subscribing via streams.
    <ul>
      <li>This feature must be enabled by setting <code class="language-plaintext highlighter-rouge">replayCallbacksConfigKey: true</code> in <code class="language-plaintext highlighter-rouge">customConfigs</code> for the <code class="language-plaintext highlighter-rouge">BrazePlugin</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-3">Changed</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2330">Braze Android SDK 23.3.0</a>.</li>
  <li>Updates the parameter type for <code class="language-plaintext highlighter-rouge">subscribeToInAppMessages()</code> and <code class="language-plaintext highlighter-rouge">subscribeToContentCards()</code> to accept a <code class="language-plaintext highlighter-rouge">Function</code> instead of a <code class="language-plaintext highlighter-rouge">void</code>.</li>
</ul>

<h2 id="260">2.6.0</h2>

<h5 id="breaking-17">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2320">Braze Android SDK 23.2.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#451">Braze iOS SDK 4.5.1</a>.</li>
  <li><code class="language-plaintext highlighter-rouge">process(inAppMessage)</code> is renamed to <code class="language-plaintext highlighter-rouge">processInAppMessage(inAppMessage)</code> in the iOS layer.</li>
</ul>

<h5 id="added-20">Added</h5>
<ul>
  <li>Adds the ability to subscribe to data for in-app messages and content cards via streams.
    <ul>
      <li>Use the methods <code class="language-plaintext highlighter-rouge">subscribeToInAppMessages()</code> and <code class="language-plaintext highlighter-rouge">subscribeToContentCards()</code>, respectively.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-4">Changed</h5>
<ul>
  <li>Updates the iOS layer to use Swift. <code class="language-plaintext highlighter-rouge">BrazePlugin.h</code> and <code class="language-plaintext highlighter-rouge">BrazePlugin.m</code> are now consolidated to <code class="language-plaintext highlighter-rouge">BrazePlugin.swift</code>.</li>
  <li>Deprecates <code class="language-plaintext highlighter-rouge">setBrazeInAppMessageCallback()</code> and <code class="language-plaintext highlighter-rouge">setBrazeContentCardsCallback()</code> in favor of subscribing via streams.</li>
</ul>

<h2 id="250">2.5.0</h2>

<h5 id="breaking-18">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2100">Braze Android SDK 21.0.0</a>.</li>
  <li>Removes <code class="language-plaintext highlighter-rouge">logContentCardsDisplayed()</code>. This method was not part of the recommended Content Cards integration and can be safely removed.</li>
</ul>

<h5 id="added-21">Added</h5>
<ul>
  <li>Adds support for the <a href="https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication/">SDK Authentication</a> feature.
    <ul>
      <li>To handle authentication errors, use <code class="language-plaintext highlighter-rouge">setBrazeSdkAuthenticationErrorCallback()</code>, and use <code class="language-plaintext highlighter-rouge">setSdkAuthenticationSignature()</code> to update the signature. When calling <code class="language-plaintext highlighter-rouge">changeUser()</code>, be sure to pass in the <code class="language-plaintext highlighter-rouge">sdkAuthSignature</code> parameter.</li>
      <li>Thanks @spaluchiewicz for contributing to this feature!</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">setLastKnownLocation()</code> to set the last known location for the user.</li>
</ul>

<h2 id="240">2.4.0</h2>

<h5 id="breaking-19">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2000">Braze Android SDK 20.0.0</a>.</li>
  <li>Removes <code class="language-plaintext highlighter-rouge">setAvatarImageUrl()</code>.</li>
</ul>

<h5 id="changed-5">Changed</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#443">Braze iOS SDK 4.4.3</a>.</li>
</ul>

<h2 id="230">2.3.0</h2>

<h5 id="breaking-20">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1700">Braze Android SDK 17.0.0</a>.</li>
  <li>The minimum supported Android SDK version is 19.</li>
  <li>Removes support for Android V1 Embedding APIs. Please reference <a href="https://flutter.dev/docs/development/packages-and-plugins/plugin-api-migration">the Flutter migration guide</a> to update to the V2 APIs.</li>
</ul>

<h5 id="added-22">Added</h5>
<ul>
  <li>Custom events and purchases now support nested properties.
    <ul>
      <li>In addition to integers, floats, booleans, dates, or strings, a JSON object can be provided containing dictionaries of arrays or nested dictionaries. All properties combined can be up to 50 KB in total length.</li>
    </ul>
  </li>
  <li>Adds the ability to restrict the Android automatic integration from natively displaying in-app messages.
    <ul>
      <li>To enable this feature, add this to your <code class="language-plaintext highlighter-rouge">braze.xml</code> configuration:
```</li>
    </ul>
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    <p>```</p>
    <ul>
      <li>The available options are <code class="language-plaintext highlighter-rouge">DISPLAY_NOW</code> or <code class="language-plaintext highlighter-rouge">DISCARD</code>. If this entry is ommitted, the default is <code class="language-plaintext highlighter-rouge">DISPLAY_NOW</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-6">Changed</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#441">Braze iOS SDK 4.4.1</a>.</li>
</ul>

<h2 id="220">2.2.0</h2>

<h5 id="breaking-21">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1600">Braze Android SDK 16.0.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#440">Braze iOS SDK 4.4.0</a>.</li>
  <li>Streamlines the Android integration process to not involve any manual writing of code to automatically register for sessions, in-app messages, or Content Card updates from the native SDK.
    <ul>
      <li>To migrate, remove any manual calls to <code class="language-plaintext highlighter-rouge">registerActivityLifecycleCallbacks()</code>, <code class="language-plaintext highlighter-rouge">subscribeToContentCardsUpdates()</code>, and <code class="language-plaintext highlighter-rouge">setCustomInAppMessageManagerListener()</code>.</li>
      <li>To disable this feature, set the boolean <code class="language-plaintext highlighter-rouge">com_braze_flutter_enable_automatic_integration_initializer</code> to <code class="language-plaintext highlighter-rouge">false</code> in your <code class="language-plaintext highlighter-rouge">braze.xml</code> configuration.</li>
    </ul>
  </li>
</ul>

<h5 id="added-23">Added</h5>
<ul>
  <li>Adds the ability to set the in-app message callback and content cards callback in the constructor of <code class="language-plaintext highlighter-rouge">BrazePlugin</code>.</li>
  <li>Adds the option to store any in-app messages or content cards received before their callback is available and replay them once the corresponding callback is set.
    <ul>
      <li>To enable this feature, add this entry into the <code class="language-plaintext highlighter-rouge">customConfigs</code> map in the BrazePlugin constructor:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>replayCallbacksConfigKey : true
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>Thank you @JordyLangen for the contribution!</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazePlugin.addToSubscriptionGroup()</code> and <code class="language-plaintext highlighter-rouge">BrazePlugin.removeFromSubscriptionGroup()</code> to manage SMS/Email Subscription Groups.</li>
</ul>

<h5 id="fixed-15">Fixed</h5>
<ul>
  <li>Fixes an issue in the iOS bridge where custom events without any properties would not be logged correctly.</li>
</ul>

<h2 id="210">2.1.0</h2>

<h5 id="breaking-22">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#432">Braze iOS SDK 4.3.2</a>.</li>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1500">Braze Android SDK 15.0.0</a>.</li>
</ul>

<h5 id="added-24">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">logContentCardsDisplayed()</code> to manually log an impression when displaying Content Cards in a custom UI.</li>
</ul>

<h2 id="200">2.0.0</h2>

<h5 id="breaking-23">Breaking</h5>
<ul>
  <li>Migrates the plugin to support null safety. All non-optional function parameters have been updated to be non-nullable unless otherwise specified. <a href="https://dart.dev/null-safety">Read here</a> for more information about null safety.
    <ul>
      <li>Please reference <a href="https://dart.dev/null-safety/migration-guide">the Dart documentation</a> when migrating your app to null safety.</li>
      <li>Apps that have not yet migrated to null safety are compatible with this version as long as they are using Dart 2.12+.</li>
      <li>Thanks @IchordeDionysos for contributing!</li>
    </ul>
  </li>
  <li>Passing through <code class="language-plaintext highlighter-rouge">null</code> as a value for user attributes is no longer supported.
    <ul>
      <li>The only attribute that is able to be unset is <code class="language-plaintext highlighter-rouge">email</code> by passing in <code class="language-plaintext highlighter-rouge">null</code> into <code class="language-plaintext highlighter-rouge">setEmail</code>.</li>
    </ul>
  </li>
  <li>The methods <code class="language-plaintext highlighter-rouge">logEvent</code> and <code class="language-plaintext highlighter-rouge">logPurchase</code> now take an optional <code class="language-plaintext highlighter-rouge">properties</code> parameter.</li>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1400">Braze Android SDK 14.0.0</a>.</li>
  <li>The minimum supported Dart version is <code class="language-plaintext highlighter-rouge">2.12.0</code>.</li>
</ul>

<h5 id="changed-7">Changed</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">logEventWithProperties</code> and <code class="language-plaintext highlighter-rouge">logPurchaseWithProperties</code> are now deprecated in favor of <code class="language-plaintext highlighter-rouge">logEvent</code> and <code class="language-plaintext highlighter-rouge">logPurchase</code>.</li>
</ul>

<h2 id="150">1.5.0</h2>

<h5 id="breaking-24">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#402">Braze iOS SDK 4.0.2</a>.</li>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312">Braze Android SDK 13.1.2</a>.</li>
  <li>The minimum supported Flutter version is 1.10.0.</li>
</ul>

<h5 id="added-25">Added</h5>
<ul>
  <li>Adds a public repository for the Braze Flutter SDK here: https://github.com/braze-inc/braze-flutter-sdk.
    <ul>
      <li>We look forward to the community’s feedback and are excited for any contributions!</li>
    </ul>
  </li>
</ul>

<h2 id="140">1.4.0</h2>

<h5 id="breaking-25">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1300">Braze Android SDK 13.0.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3340">Braze iOS SDK 3.34.0</a>.</li>
</ul>

<h5 id="added-26">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazePlugin.setGoogleAdvertisingId()</code> to set the Google Advertising ID and the associated Ad-Tracking Enabled field for Android. This is a no-op on iOS.</li>
</ul>

<h5 id="fixed-16">Fixed</h5>
<ul>
  <li>Fixes an issue where the Braze Android SDK’s <code class="language-plaintext highlighter-rouge">Appboy.setLogLevel()</code> method wasn’t respected.</li>
</ul>

<h2 id="130">1.3.0</h2>

<h5 id="breaking-26">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1200">Braze Android SDK 12.0.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3310">Braze iOS SDK 3.31.0</a>.</li>
</ul>

<h5 id="added-27">Added</h5>
<ul>
  <li>Adds support for the Braze plugin to be used with Android V2 Embedding APIs. Integrations using V1 Embedding will also continue to work.</li>
  <li>Allows the Android Braze plugin to be used with multiple Flutter engines.</li>
</ul>

<h2 id="120">1.2.0</h2>

<h5 id="breaking-27">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3300">Braze iOS SDK 3.30.0</a>.</li>
</ul>

<h5 id="added-28">Added</h5>
<ul>
  <li>Allows the iOS Braze plugin to be used with multiple Flutter engines.</li>
</ul>

<h2 id="110">1.1.0</h2>

<h5 id="breaking-28">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1100">Braze Android SDK 11.0.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3291">Braze iOS SDK 3.29.1</a>.</li>
</ul>

<h2 id="100">1.0.0</h2>

<h5 id="breaking-29">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3270">Braze iOS SDK 3.27.0</a>. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.</li>
</ul>

<h2 id="0101">0.10.1</h2>

<h5 id="changed-8">Changed</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3261">Braze iOS SDK 3.26.1</a>.</li>
</ul>

<h2 id="0100">0.10.0</h2>

<h5 id="breaking-30">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810">Braze Android SDK 8.1.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3260">Braze iOS SDK 3.26.0</a>.</li>
</ul>

<h5 id="fixed-17">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">setBoolCustomUserAttribute</code> always set the attribute to <code class="language-plaintext highlighter-rouge">true</code> on iOS.</li>
</ul>

<h2 id="090">0.9.0</h2>

<h5 id="breaking-31">Breaking</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#700">Braze Android SDK 7.0.0</a>.</li>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3220">Braze iOS SDK 3.22.0</a>.</li>
</ul>

<h2 id="080">0.8.0</h2>

<h5 id="breaking-32">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3213">Braze iOS SDK 3.21.3</a>.</li>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#402">Braze Android SDK 4.0.2</a>.
    <ul>
      <li>If you are using a custom <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener</code>, then you will need to define new methods added to that interface in <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#400">Braze Android SDK 4.0.0</a>. See the <code class="language-plaintext highlighter-rouge">MainActivity.kt</code> file of our sample app for a reference example.</li>
    </ul>
  </li>
</ul>

<h2 id="070">0.7.0</h2>

<h5 id="added-29">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazePlugin.launchContentCards()</code> and <code class="language-plaintext highlighter-rouge">BrazePlugin.refreshContentCards()</code> to natively display and refresh Content Cards.</li>
  <li>Adds a Dart callback for receiving Braze Content Card data in the Flutter host app.
    <ul>
      <li>Similar to in-app messages, you will need to subscribe to Content Card updates in your native app code and pass Content Card objects to the Dart layer. Those objects will then be passed to your callback within a <code class="language-plaintext highlighter-rouge">List&lt;BrazeContentCard&gt;</code> instance.</li>
      <li>To set the callback, call <code class="language-plaintext highlighter-rouge">BrazePlugin.setBrazeContentCardsCallback()</code> from your Flutter app with a function that takes a <code class="language-plaintext highlighter-rouge">List&lt;BrazeContentCard&gt;</code> instance.
        <ul>
          <li>The <code class="language-plaintext highlighter-rouge">BrazeContentCard</code> object supports a subset of fields available in the native model objects, including <code class="language-plaintext highlighter-rouge">description</code>, <code class="language-plaintext highlighter-rouge">title</code>, <code class="language-plaintext highlighter-rouge">image</code>, <code class="language-plaintext highlighter-rouge">url</code>, <code class="language-plaintext highlighter-rouge">extras</code>, and more.</li>
        </ul>
      </li>
      <li>On Android, you will need to register an <code class="language-plaintext highlighter-rouge">IEventSubscriber&lt;ContentCardsUpdatedEvent&gt;</code> instance and pass returned Content Card objects to the Dart layer using <code class="language-plaintext highlighter-rouge">BrazePlugin.processContentCards(contentCards)</code>.
        <ul>
          <li>See the <code class="language-plaintext highlighter-rouge">MainActivity.kt</code> file of our sample app for a reference example.</li>
        </ul>
      </li>
      <li>On iOS, you will need to create an <code class="language-plaintext highlighter-rouge">NSNotificationCenter</code> listener for <code class="language-plaintext highlighter-rouge">ABKContentCardsProcessedNotification</code> events and pass returned Content Card objects to the Dart layer using <code class="language-plaintext highlighter-rouge">BrazePlugin.processContentCards(contentCards)</code>.
        <ul>
          <li>See the <code class="language-plaintext highlighter-rouge">AppDelegate.swift</code> file of our sample app for a reference example.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Added support for logging Content Card analytics to Braze using <code class="language-plaintext highlighter-rouge">BrazeContentCard</code> instances. See <code class="language-plaintext highlighter-rouge">logContentCardClicked()</code>, <code class="language-plaintext highlighter-rouge">logContentCardImpression()</code>, and <code class="language-plaintext highlighter-rouge">logContentCardDismissed()</code> on the <code class="language-plaintext highlighter-rouge">BrazePlugin</code> interface.</li>
</ul>

<h2 id="061">0.6.1</h2>

<h5 id="fixed-18">Fixed</h5>
<ul>
  <li>Fixed an issue where the Braze Kotlin plugin file’s directory structure did not match its package structure.</li>
</ul>

<h2 id="060">0.6.0</h2>

<h5 id="changed-9">Changed</h5>
<ul>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#380">Braze Android SDK 3.8.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.4">Braze iOS SDK 3.20.4</a>.</li>
</ul>

<h2 id="052">0.5.2</h2>

<p><strong>Important:</strong> This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md">Braze iOS SDK Changelog</a> for more information.</p>

<h5 id="changed-10">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.2">Braze iOS SDK 3.20.2</a>.</li>
</ul>

<h2 id="051">0.5.1</h2>

<p><strong>Important</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 0.5.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 0.5.2 or above if you make use of HTML in-app messages.</p>

<h5 id="changed-11">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.1">Braze iOS SDK 3.20.1</a>.</li>
</ul>

<h2 id="050">0.5.0</h2>

<p><strong>Important</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 0.5.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 0.5.2 or above if you make use of HTML in-app messages.</p>

<h5 id="breaking-33">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3200">Braze iOS SDK 3.20.0</a>.</li>
  <li><strong>Important:</strong> Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to these methods as soon as possible to ensure a smooth transition as devices upgrade to iOS 13. In <code class="language-plaintext highlighter-rouge">application:didRegisterForRemoteNotificationsWithDeviceToken:</code>, replace
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>[[Appboy sharedInstance] registerPushToken:
              [NSString stringWithFormat:@"%@", deviceToken]];
</pre></td></tr></tbody></table></code></pre></div>    </div>
    <p>with</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>[[Appboy sharedInstance] registerDeviceToken:deviceToken]];
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
  <li><code class="language-plaintext highlighter-rouge">registerPushToken()</code> was renamed to <code class="language-plaintext highlighter-rouge">registerAndroidPushToken()</code> and is now a no-op on iOS. On iOS, push tokens must now be registered through native methods.</li>
</ul>

<h2 id="040">0.4.0</h2>

<h5 id="breaking-34">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3180">Braze iOS SDK 3.18.0</a>.</li>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#360">Braze Android SDK 3.6.0</a>.</li>
</ul>

<h5 id="added-30">Added</h5>
<ul>
  <li>Added the following new field to <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code>: <code class="language-plaintext highlighter-rouge">zippedAssetsUrl</code>.
    <ul>
      <li>Note that a known issue in the iOS plugin prevents HTML in-app messages from working reliably with the Dart in-app message callback. Android is not affected.</li>
    </ul>
  </li>
</ul>

<h2 id="030">0.3.0</h2>

<h5 id="breaking-35">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3150">Braze iOS SDK 3.15.0</a>.</li>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#350">Braze Android SDK 3.5.0</a>.</li>
  <li>Support for the Android configuration parameter <code class="language-plaintext highlighter-rouge">com_appboy_inapp_show_inapp_messages_automatically</code> has been removed.
    <ul>
      <li>To control whether an in-app message object should be displayed natively or not, create and register an instance of <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener</code> in your native Android code and implement decisioning in the <code class="language-plaintext highlighter-rouge">beforeInAppMessageDisplayed</code> method. See <code class="language-plaintext highlighter-rouge">MainActivity</code> in our sample app for an example.</li>
    </ul>
  </li>
  <li>On Android, in-app message objects are no longer sent automatically to the Dart in-app message callback after calling <code class="language-plaintext highlighter-rouge">BrazePlugin.setBrazeInAppMessageCallback()</code> in your Dart code.
    <ul>
      <li>Similar to iOS, you will need to implement a delegate interface in your native app code and pass in-app message objects to the Dart layer for passing to the callback.</li>
      <li>On Android, the delegate interface is <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener</code> and the method for passing objects to Dart is <code class="language-plaintext highlighter-rouge">BrazePlugin.processInAppMessage(inAppMessage)</code>.</li>
      <li>See the sample <code class="language-plaintext highlighter-rouge">IInAppMessageManagerListener</code> implementation in the <code class="language-plaintext highlighter-rouge">MainActivity.kt</code> file of our sample app for an example.</li>
      <li>This approach gives the integrator more flexibility in deciding when a message should be displayed natively, discarded, or passed into the Dart layer.</li>
    </ul>
  </li>
</ul>

<h5 id="added-31">Added</h5>
<ul>
  <li>Added support for logging in-app message analytics to Braze using <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code> instances. See <code class="language-plaintext highlighter-rouge">logInAppMessageClicked</code>, <code class="language-plaintext highlighter-rouge">logInAppMessageImpression</code>, and <code class="language-plaintext highlighter-rouge">logInAppMessageButtonClicked</code> on the <code class="language-plaintext highlighter-rouge">BrazePlugin</code> interface.</li>
</ul>

<h2 id="021">0.2.1</h2>

<h5 id="added-32">Added</h5>
<ul>
  <li>Added the following new fields to <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code>: <code class="language-plaintext highlighter-rouge">imageUrl</code>, <code class="language-plaintext highlighter-rouge">useWebView</code>, <code class="language-plaintext highlighter-rouge">duration</code>, <code class="language-plaintext highlighter-rouge">clickAction</code>, <code class="language-plaintext highlighter-rouge">dismissType</code>, <code class="language-plaintext highlighter-rouge">messageType</code></li>
  <li>Added the following new fields to <code class="language-plaintext highlighter-rouge">BrazeButton</code>: <code class="language-plaintext highlighter-rouge">useWebView</code>, <code class="language-plaintext highlighter-rouge">clickAction</code>.</li>
</ul>

<h2 id="020">0.2.0</h2>

<h5 id="breaking-36">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3140">Braze iOS SDK 3.14.0</a>.</li>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#321">Braze Android SDK 3.2.1</a>.</li>
</ul>

<h5 id="added-33">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">addAlias()</code> to the public API interface.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">requestLocationInitialization()</code> to the public API interface.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">getInstallTrackingId()</code> to the public API interface.</li>
  <li>Adds support for disabling native in-app message display on Android.
    <ul>
      <li>To disable automatic in-app message display, create a boolean element named <code class="language-plaintext highlighter-rouge">com_appboy_inapp_show_inapp_messages_automatically</code> in your Android app’s <code class="language-plaintext highlighter-rouge">appboy.xml</code> and set it to <code class="language-plaintext highlighter-rouge">false</code>.</li>
      <li>Note: Disabling automatic in-app message display was already possible for iOS. For instructions, see <code class="language-plaintext highlighter-rouge">README.md</code>.</li>
    </ul>
  </li>
  <li>Adds a Dart callback for receiving Braze in-app message data in the Flutter host app.
    <ul>
      <li>Analytics are not currently supported on messages displayed through the callback.</li>
      <li>To set the callback, call <code class="language-plaintext highlighter-rouge">BrazePlugin.setBrazeInAppMessageCallback()</code> from your Flutter app with a function that takes a <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code> instance.
        <ul>
          <li>The <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code> object supports a subset of fields available in the native model objects, including <code class="language-plaintext highlighter-rouge">uri</code>, <code class="language-plaintext highlighter-rouge">message</code>, <code class="language-plaintext highlighter-rouge">header</code>, <code class="language-plaintext highlighter-rouge">buttons</code>, and <code class="language-plaintext highlighter-rouge">extras</code>.</li>
        </ul>
      </li>
      <li>The callback should begin to function on Android immediately after being set.</li>
      <li>On iOS, you will additionally need to implement the <code class="language-plaintext highlighter-rouge">ABKInAppMessageControllerDelegate</code> delegate as described in our <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#in-app-message-controller-delegate">public documentation</a>. Your <code class="language-plaintext highlighter-rouge">beforeInAppMessageDisplayed</code> delegate implementation must call <code class="language-plaintext highlighter-rouge">BrazePlugin.process(inAppMessage)</code>. For an example, see <code class="language-plaintext highlighter-rouge">AppDelegate.swift</code> in our example app.</li>
    </ul>
  </li>
</ul>

<h2 id="011">0.1.1</h2>
<ul>
  <li>Formatted <code class="language-plaintext highlighter-rouge">braze_plugin.dart</code>.</li>
</ul>

<h2 id="010">0.1.0</h2>
<ul>
  <li>Removes the unused <code class="language-plaintext highlighter-rouge">dart:async</code> import in <code class="language-plaintext highlighter-rouge">braze_plugin.dart</code>.</li>
  <li>Makes <code class="language-plaintext highlighter-rouge">_callStringMethod</code> private in <code class="language-plaintext highlighter-rouge">braze_plugin.dart</code>.</li>
  <li>Adds basic dartdoc to the public API interface.</li>
</ul>

<h2 id="002">0.0.2</h2>
<ul>
  <li>Updates the version of Kotlin used by the Android plugin from <code class="language-plaintext highlighter-rouge">1.2.71</code> to <code class="language-plaintext highlighter-rouge">1.3.11</code>.</li>
</ul>

<h2 id="001">0.0.1</h2>
<ul>
  <li>Initial release.</li>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.12.0">Braze iOS SDK 3.12.0</a>.</li>
  <li>The native Android bridge uses <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#310">Braze Android SDK 3.1.0</a>.</li>
</ul>




**Tip:**


You can also find a copy of the [React Native Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md).



<h2 id="2000">20.0.0</h2>

<h5 id="breaking">Breaking</h5>
<ul>
  <li>Updates the native Android SDK version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v41.1.1...v42.0.0">from Braze Android SDK 41.1.1 to 42.0.0</a>.</li>
</ul>

<h5 id="fixed">Fixed</h5>
<ul>
  <li>Fixes an Android <a href="https://github.com/braze-inc/braze-react-native-sdk/pull/320">issue</a> where <code class="language-plaintext highlighter-rouge">getContentCards()</code> could crash natively if its <code class="language-plaintext highlighter-rouge">Promise</code> was settled more than once. Also, the promise may now be rejected with <code class="language-plaintext highlighter-rouge">no_active_react_instance</code> when React is inactive.</li>
</ul>

<h2 id="1920">19.2.0</h2>

<h5 id="added">Added</h5>
<ul>
  <li>Adds support for delayed SDK initialization via <code class="language-plaintext highlighter-rouge">Braze.initialize(apiKey, endpoint)</code> in JavaScript.
    <ul>
      <li>On iOS, use <code class="language-plaintext highlighter-rouge">BrazeReactInitializer.configure(_:postInitialization:)</code> in your <code class="language-plaintext highlighter-rouge">AppDelegate</code> to register configuration and post-initialization closures before React Native starts, such as inside the <code class="language-plaintext highlighter-rouge">didFinishLaunching</code>. The closures are applied when <code class="language-plaintext highlighter-rouge">Braze.initialize()</code> is called from the JavaScript layer.</li>
      <li>On Android, set <code class="language-plaintext highlighter-rouge">com_braze_enable_delayed_initialization</code> to <code class="language-plaintext highlighter-rouge">true</code> in your <code class="language-plaintext highlighter-rouge">braze.xml</code> to prevent auto-initialization. SDK configuration values from <code class="language-plaintext highlighter-rouge">braze.xml</code> are applied automatically when <code class="language-plaintext highlighter-rouge">Braze.initialize()</code> is called.</li>
      <li>Deprecates <code class="language-plaintext highlighter-rouge">BrazeReactBridge.initBraze(_:)</code> on iOS. Use <code class="language-plaintext highlighter-rouge">BrazeReactInitializer.configure(_:postInitialization:)</code> in your <code class="language-plaintext highlighter-rouge">AppDelegate</code> and <code class="language-plaintext highlighter-rouge">Braze.initialize(apiKey, endpoint)</code> from JavaScript instead.</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">BrazeReactInitializer</code>, a Swift-first helper class for configuring delayed initialization on iOS. This resolves a Swift type-resolution issue where <code class="language-plaintext highlighter-rouge">Braze.Configuration</code> was not directly usable from Swift in the Objective-C bridge.</li>
</ul>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Updates the native Swift SDK version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/14.0.1...14.0.4#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 14.0.1 to 14.0.4</a>.</li>
</ul>

<h2 id="1910">19.1.0</h2>

<h5 id="added-1">Added</h5>
<ul>
  <li>Updates the native Android SDK version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v41.0.0...v41.1.1">from Braze Android SDK 41.0.0 to 41.1.1</a>.</li>
</ul>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Fixes an Android <a href="https://github.com/braze-inc/braze-react-native-sdk/issues/301">issue</a> where <code class="language-plaintext highlighter-rouge">getInitialPushPayload()</code> would not return the push payload when the app was cold-started via a deep link routed through <code class="language-plaintext highlighter-rouge">ACTION_VIEW</code> instead of the direct Braze push intent.</li>
</ul>

<h2 id="1900">19.0.0</h2>

<h5 id="breaking-1">Breaking</h5>
<ul>
  <li>Updates the native Swift SDK version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 13.3.0 to 14.0.1</a>.</li>
  <li>Updates the native Android SDK version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v40.0.2...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 40.0.2 to 41.0.0</a>.</li>
</ul>

<h5 id="added-2">Added</h5>
<ul>
  <li>Adds Android support for <code class="language-plaintext highlighter-rouge">Braze.getInitialPushPayload()</code> to handle push notification deep links when the app is launched from a terminated state.
    <ul>
      <li>This resolves an <a href="https://github.com/braze-inc/braze-react-native-sdk/issues/301">issue where deep links from push notifications were not handled on Android when the app was cold started</a>.</li>
      <li>To use this feature, call <code class="language-plaintext highlighter-rouge">BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)</code> in your <code class="language-plaintext highlighter-rouge">MainActivity.onCreate()</code> method before React Native initializes. See <code class="language-plaintext highlighter-rouge">BrazeProject.tsx</code> in the sample app for an example implementation.</li>
      <li>This provides feature parity with the existing iOS implementation added in version <code class="language-plaintext highlighter-rouge">13.1.0</code>.</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">logBannerImpression(placementId)</code> and <code class="language-plaintext highlighter-rouge">logBannerClick(placementId, buttonId?)</code> methods to manually log banner analytics for custom banner UI implementations.</li>
  <li>Updates the Braze sample app to use React Native version <a href="https://reactnative.dev/blog/2025/12/10/react-native-0.83"><code class="language-plaintext highlighter-rouge">0.83.0</code></a>. This change validates SDK compatibility with the latest version of React Native.</li>
</ul>

<h2 id="1800">18.0.0</h2>

<h5 id="breaking-2">Breaking</h5>
<ul>
  <li>Fixes the Typescript type for the callback of <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage</code> and <code class="language-plaintext highlighter-rouge">addListener</code> for <code class="language-plaintext highlighter-rouge">Braze.Events.IN_APP_MESSAGE_RECEIVED</code>.
    <ul>
      <li>These listeners now properly return a callback with the new <code class="language-plaintext highlighter-rouge">InAppMessageEvent</code> type. Previously, the methods were annotated to return a <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code> type, but it was actually returning a <code class="language-plaintext highlighter-rouge">String</code>.</li>
      <li>If you are using either subscription API, ensure that the behavior of your in-app messages are unchanged after updating to this version. See our sample code in <a href="https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/BrazeProject.tsx"><code class="language-plaintext highlighter-rouge">BrazeProject.tsx</code></a>.</li>
    </ul>
  </li>
  <li>The APIs <code class="language-plaintext highlighter-rouge">logInAppMessageClicked</code>, <code class="language-plaintext highlighter-rouge">logInAppMessageImpression</code>, and <code class="language-plaintext highlighter-rouge">logInAppMessageButtonClicked</code> now accept only a <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code> object to match its existing public interface.
    <ul>
      <li>Previously, it would accept both a <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code> object as well as a <code class="language-plaintext highlighter-rouge">String</code>.</li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">BrazeInAppMessage.toString()</code> now returns a human-readable string instead of the JSON string representation.
    <ul>
      <li>To get the JSON string representation of an in-app message, use <code class="language-plaintext highlighter-rouge">BrazeInAppMessage.inAppMessageJsonString</code>.</li>
    </ul>
  </li>
  <li>On iOS, <code class="language-plaintext highlighter-rouge">[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]</code> has been moved to <code class="language-plaintext highlighter-rouge">[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]</code>.
    <ul>
      <li>This new method is a now a class method instead of an instance method.</li>
    </ul>
  </li>
  <li>Adds nullability annotations to <code class="language-plaintext highlighter-rouge">BrazeReactUtils</code> methods.</li>
  <li>Removes the following deprecated methods and properties from the API:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">getInstallTrackingId(callback:)</code> in favor of <code class="language-plaintext highlighter-rouge">getDeviceId</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">registerAndroidPushToken(token:)</code> in favor of <code class="language-plaintext highlighter-rouge">registerPushToken</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)</code> in favor of <code class="language-plaintext highlighter-rouge">setAdTrackingEnabled</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">PushNotificationEvent.push_event_type</code> in favor of <code class="language-plaintext highlighter-rouge">payload_type</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">PushNotificationEvent.deeplink</code> in favor of <code class="language-plaintext highlighter-rouge">url</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">PushNotificationEvent.content_text</code> in favor of <code class="language-plaintext highlighter-rouge">body</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">PushNotificationEvent.raw_android_push_data</code> in favor of <code class="language-plaintext highlighter-rouge">android</code>.</li>
      <li><code class="language-plaintext highlighter-rouge">PushNotificationEvent.kvp_data</code> in favor of <code class="language-plaintext highlighter-rouge">braze_properties</code>.</li>
    </ul>
  </li>
  <li>Updates the native Android SDK version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 39.0.0 to 40.0.2</a>.</li>
</ul>

<h5 id="added-3">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">imageAltText</code> and <code class="language-plaintext highlighter-rouge">language</code> fields to <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code> for accessibility features.</li>
  <li>Updates the native Swift SDK version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/13.2.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 13.2.0 to 13.3.0</a>.</li>
</ul>

<h2 id="1701">17.0.1</h2>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Fixes an iOS issue where existing Banner views would fail to re-display after navigating away and returning.</li>
  <li>Fixes an incompatibility with React Native <code class="language-plaintext highlighter-rouge">0.80+</code> where iOS Banner views would not be generated as Fabric components but as legacy <code class="language-plaintext highlighter-rouge">RCTView</code>s.
    <ul>
      <li>This issue has no known impacts that are visible to the end user.</li>
    </ul>
  </li>
</ul>

<h2 id="1700">17.0.0</h2>

<h5 id="breaking-3">Breaking</h5>
<ul>
  <li>Updates the native Android SDK version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 37.0.0 to 39.0.0</a>.</li>
  <li>Removes support for News Feed. The following APIs have been removed:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">launchNewsFeed</code></li>
      <li><code class="language-plaintext highlighter-rouge">requestFeedRefresh</code></li>
      <li><code class="language-plaintext highlighter-rouge">getNewsFeedCards</code></li>
      <li><code class="language-plaintext highlighter-rouge">logNewsFeedCardClicked</code></li>
      <li><code class="language-plaintext highlighter-rouge">logNewsFeedCardImpression</code></li>
      <li><code class="language-plaintext highlighter-rouge">getCardCountForCategories</code></li>
      <li><code class="language-plaintext highlighter-rouge">getUnreadCardCountForCategories</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.Events.NEWS_FEED_CARDS_UPDATED</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.CardCategory</code></li>
    </ul>
  </li>
</ul>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Fixes an issue where <code class="language-plaintext highlighter-rouge">getDeviceID()</code> did not return when an error occurred.</li>
  <li>Fixes the Android implementation of the <code class="language-plaintext highlighter-rouge">FeatureFlag</code> object to return the correct values for timestamp, image, and JSON objects. Prior to this change, the following APIs would return <code class="language-plaintext highlighter-rouge">undefined</code> on Android:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagTimestampProperty(id)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagJSONProperty(id)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagImageProperty(id)</code></li>
    </ul>
  </li>
  <li>Fixes the <code class="language-plaintext highlighter-rouge">FeatureFlagTimestampProperty</code> object type to be <code class="language-plaintext highlighter-rouge">datetime</code> instead of <code class="language-plaintext highlighter-rouge">timestamp</code>.</li>
  <li>Fixes an issue where passing a null value for <code class="language-plaintext highlighter-rouge">googleAdvertisingId</code> to <code class="language-plaintext highlighter-rouge">setAdTrackingEnabled()</code> could cause a crash on Android.</li>
</ul>

<h5 id="added-4">Added</h5>
<ul>
  <li>Adds support for Banner properties via new public methods for <code class="language-plaintext highlighter-rouge">Banner</code>:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">banner.getStringProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">String</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getNumberProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">num</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getTimestampProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">int</code> Unix UTC millisecond timestamp  properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getBooleanProperty(key:)</code> for accessing <code class="language-plaintext highlighter-rouge">bool</code> properties.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getImageProperty(key:)</code> for accessing image URL properties as <code class="language-plaintext highlighter-rouge">String</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">banner.getJSONProperty(key:)</code> for accessing JSON properties as <code class="language-plaintext highlighter-rouge">Map&lt;String, dynamic&gt;</code>.</li>
    </ul>
  </li>
  <li>Deprecates the following static methods in favor of new <code class="language-plaintext highlighter-rouge">FeatureFlag</code> instance methods:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagStringProperty(flagId, propertyKey)</code>, instead use <code class="language-plaintext highlighter-rouge">flag.getStringProperty(key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagBooleanProperty(flagId, propertyKey)</code>, instead use <code class="language-plaintext highlighter-rouge">flag.getBooleanProperty(key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagNumberProperty(flagId, propertyKey)</code>, instead use <code class="language-plaintext highlighter-rouge">flag.getNumberProperty(key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagTimestampProperty(flagId, propertyKey)</code>, instead use <code class="language-plaintext highlighter-rouge">flag.getTimestampProperty(key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagJSONProperty(flagId, propertyKey)</code>, instead use <code class="language-plaintext highlighter-rouge">flag.getJSONProperty(key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlagImageProperty(flagId, propertyKey)</code>, instead use <code class="language-plaintext highlighter-rouge">flag.getImageProperty(key)</code></li>
    </ul>
  </li>
</ul>

<h2 id="1610">16.1.0</h2>

<h5 id="fixed-5">Fixed</h5>
<ul>
  <li>Fixes a missing symbol error when compiling for Android on the React Native legacy bridge architecture on <code class="language-plaintext highlighter-rouge">0.81</code>.
    <ul>
      <li>This change is backwards compatible with prior versions of React Native.</li>
    </ul>
  </li>
</ul>

<h5 id="added-5">Added</h5>
<ul>
  <li>Updates the native Swift SDK version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/13.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 13.0.0 to 13.2.0</a>.
    <ul>
      <li>This includes Xcode 26 support.</li>
    </ul>
  </li>
</ul>

<h2 id="1600">16.0.0</h2>

<h5 id="breaking-4">Breaking</h5>
<ul>
  <li>Updates the native Android SDK version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 36.0.0 to 37.0.0</a>.</li>
  <li>Updates the native Swift SDK version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 12.0.0 to 13.0.0</a>.
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">"sdkAuthenticationError"</code> event will now trigger for both “Required” <strong>and “Optional”</strong> authentication errors.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-6">Fixed</h5>
<ul>
  <li>Fixes the iOS implementation of <code class="language-plaintext highlighter-rouge">setDateOfBirth</code> to correctly report dates using the Gregorian calendar instead of the user’s device calendar.
    <ul>
      <li>Previously, the SDK would re-format the input date components with the device’s calendar settings if they were non-Gregorian.</li>
    </ul>
  </li>
</ul>

<h5 id="added-6">Added</h5>
<ul>
  <li>Updates the Braze sample app to use React Native version <a href="https://reactnative.dev/blog/2025/06/12/react-native-0.80"><code class="language-plaintext highlighter-rouge">0.80.0</code></a>. This change validates SDK compatibility with the latest version of React Native.</li>
  <li>Adds ability to unset user first name, last name, phone number, email, gender, language, home city, and country by setting these values to <code class="language-plaintext highlighter-rouge">null</code>.</li>
</ul>

<h2 id="1501">15.0.1</h2>

<h5 id="fixed-7">Fixed</h5>
<ul>
  <li>Improves the TypeScript declarations in the following areas:
    <ul>
      <li>Adds missing TypeScript definitions for the <code class="language-plaintext highlighter-rouge">BrazeBannerView</code> component and its children properties.</li>
      <li>Usage comments that were previously missing for properties on <code class="language-plaintext highlighter-rouge">PushNotificationEvent</code> and <code class="language-plaintext highlighter-rouge">TrackingPropertyAllowList</code> will now appear in the TypeScript auto-complete descriptions.</li>
    </ul>
  </li>
</ul>

<h2 id="1500">15.0.0</h2>

<blockquote>
  <p>[!IMPORTANT]
This release reverts the increase to the minimum Android SDK version of the Braze Android SDK from API 21 to API 25 introduced in 34.0.0. This allows the SDK to once again be compiled into apps supporting as early as API 21. However, we are not reintroducing formal support for &lt; API 25. Read more <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600">here</a>.</p>
</blockquote>

<h5 id="breaking-5">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 35.0.0 to 36.0.0</a>.</li>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.9.0...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.9.0 to 12.0.0</a>.</li>
  <li>Updates the unit representation of <code class="language-plaintext highlighter-rouge">PushNotificationEvent.timestamp</code> to milliseconds on iOS.
    <ul>
      <li>Previously, this value would be represented in seconds on iOS. This will now match the existing Android implementation.</li>
    </ul>
  </li>
</ul>

<h2 id="1410">14.1.0</h2>

<h5 id="fixed-8">Fixed</h5>
<ul>
  <li>Updates the internal implementations of the following methods to use non-deprecated methods from the native Swift SDK:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">getUserId</code> now uses <code class="language-plaintext highlighter-rouge">braze.user.identifier</code> instead of <code class="language-plaintext highlighter-rouge">[braze.user idWithCompletion:]</code>, which was deprecated in Swift SDK <a href="https://github.com/braze-inc/braze-swift-sdk/releases/tag/11.5.0">11.5.0</a>.</li>
      <li><code class="language-plaintext highlighter-rouge">Banner.trackingId</code> now uses the underlying <code class="language-plaintext highlighter-rouge">banner.trackingId</code> instead of <code class="language-plaintext highlighter-rouge">banner.identifier</code>, which was deprecated in Swift SDK <a href="https://github.com/braze-inc/braze-swift-sdk/releases/tag/11.4.0">11.4.0</a>.</li>
      <li>These deprecations do not have any impacts to functionality.</li>
    </ul>
  </li>
  <li>Fixes the callback signature of <code class="language-plaintext highlighter-rouge">getInitialPushPayload</code> to indicate that <code class="language-plaintext highlighter-rouge">null</code> can be returned when there is no payload object available.</li>
  <li>Fixes the relative path reference to various Braze data models in the <code class="language-plaintext highlighter-rouge">NativeBrazeReactModuleSpec</code>.</li>
  <li>Resolves a build failure in the <code class="language-plaintext highlighter-rouge">BrazeBannerView</code> class introduced in <code class="language-plaintext highlighter-rouge">14.0.0</code>, which would occur under certain iOS project configurations.</li>
</ul>

<h5 id="added-7">Added</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.7.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.7.0 to 11.9.0</a>.</li>
</ul>

<h2 id="1400">14.0.0</h2>

<h5 id="breaking-6">Breaking</h5>
<ul>
  <li>Resolves an Android issue with <code class="language-plaintext highlighter-rouge">setDateOfBirth(year, month, day)</code> introduced in <code class="language-plaintext highlighter-rouge">1.38.0</code>, where the month was indexed 0-11 instead of 1-12. The months are now indexed from 1-12 on both Android and iOS.
    <ul>
      <li>The previous behavior on Android would assign <code class="language-plaintext highlighter-rouge">setDateOfBirth(1970, 1, 1)</code> to the month of February instead of the intended month of January, and <code class="language-plaintext highlighter-rouge">setDateOfBirth(1970, 12, 1)</code> to <code class="language-plaintext highlighter-rouge">null</code> instead of the intended month of December.</li>
      <li>Customers who wish to retroactively rectify this are recommended to ask their users to confirm their dates of birth and call <code class="language-plaintext highlighter-rouge">setDateOfBirth</code> with these values.</li>
    </ul>
  </li>
  <li>Updates the native Android version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 32.1.0 to 35.0.0</a>.
    <ul>
      <li>The minimum required Android SDK version is 25. See more details <a href="https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information">here</a>.</li>
    </ul>
  </li>
  <li>The <code class="language-plaintext highlighter-rouge">NativeBrazeReactModule.ts</code> file has been moved into a sub-directory called <code class="language-plaintext highlighter-rouge">specs</code>.
    <ul>
      <li>If your project contains direct references to this file, you will need to update the relative path of your imports to <code class="language-plaintext highlighter-rouge">/specs/NativeBrazeReactModule</code>.</li>
      <li>For an example, refer to the sample test setup <a href="https://github.com/braze-inc/braze-react-native-sdk/tree/master/__tests__">here</a>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-8">Added</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.2.0...11.7.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.2.0 to 11.7.0</a>.</li>
  <li>Adds support for the Braze Banner Cards product and APIs to utilize them.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.requestBannersRefresh(placementIds)</code> - to request a refresh of the banners associated with the provided placement IDs. On iOS only, failures will be logged if unsuccessful.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getBanner(placementId)</code> - to get a banner with the provided placement ID if available in cache, otherwise returns null.</li>
      <li><code class="language-plaintext highlighter-rouge">Braze.Events.BANNER_CARDS_UPDATED</code> event for <code class="language-plaintext highlighter-rouge">Braze.addListener</code> - to subscribe to banners updates.</li>
    </ul>
  </li>
  <li>Adds the default UI components for Braze Banner Cards.
    <ul>
      <li>To use this feature, insert the <code class="language-plaintext highlighter-rouge">Braze.BrazeBannerView</code> component into your view hierarchy with the required <code class="language-plaintext highlighter-rouge">placementID</code> property.</li>
    </ul>
  </li>
</ul>

<h2 id="1320">13.2.0</h2>

<h5 id="added-9">Added</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.1.1...11.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.1.1 to 11.2.0</a>.</li>
  <li>Updates the Android bridge to add compatibility with React Native version 0.77.0.
    <ul>
      <li>Updates the Braze sample app to use React Native version 0.77.0.</li>
    </ul>
  </li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">setIdentifierForAdvertiser</code> and <code class="language-plaintext highlighter-rouge">setIdentifierForVendor</code> methods to set the <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/">IDFA</a> and <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)/">IDFV</a>, respectively (iOS only). This is a no-op on Android.</li>
</ul>

<h2 id="1311">13.1.1</h2>

<h5 id="fixed-9">Fixed</h5>
<ul>
  <li>Resolves an iOS issue that would deallocate existing references of <code class="language-plaintext highlighter-rouge">braze.delegate</code> when performing a hot reload of the app.</li>
</ul>

<h2 id="1310">13.1.0</h2>

<h5 id="fixed-10">Fixed</h5>
<ul>
  <li>Updates the iOS sample app to properly retain the <code class="language-plaintext highlighter-rouge">BrazeReactDelegate</code> instance. Internally, the Braze SDK uses a weak reference to the delegate, which could be deallocated if not retained by the app. This change ensures the delegate is retained for the lifecycle of the app.</li>
</ul>

<h5 id="added-10">Added</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.0.0...11.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.0.0 to 11.1.1</a>.</li>
  <li>Adds the method <code class="language-plaintext highlighter-rouge">Braze.getInitialPushPayload()</code> to get the push notification payload when opening the app via notification click while the application was in a terminated state.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.getInitialURL()</code> is now deprecated in favor of <code class="language-plaintext highlighter-rouge">Braze.getInitialPushPayload()</code>. To access the initial URL, use the new method to receive the push notification payload, and access the value of the <code class="language-plaintext highlighter-rouge">url</code> key.</li>
      <li>If you are using <code class="language-plaintext highlighter-rouge">Braze.getInitialPushPayload()</code>, add the following code to your <code class="language-plaintext highlighter-rouge">application:didFinishLaunchingWithOptions:launchOptions:</code>:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>[[BrazeReactUtils sharedInstance] populateInitialPayloadFromLaunchOptions:launchOptions];
</pre></td></tr></tbody></table></code></pre></div>        </div>
        <p>This replaces <code class="language-plaintext highlighter-rouge">populateInitialUrlFromLaunchOptions</code>, which is now deprecated.</p>
      </li>
    </ul>
  </li>
</ul>

<h2 id="1300">13.0.0</h2>

<p>⚠️ <strong>Important:</strong> This version includes a Swift SDK version with a known issue related to push subscription status. Upgrade to version <code class="language-plaintext highlighter-rouge">13.1.0</code> instead.</p>

<h5 id="breaking-7">Breaking</h5>
<ul>
  <li>Updates the native Android version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 31.1.0 to 32.1.0</a>.</li>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 10.3.0 to 11.0.0</a>.</li>
</ul>

<h2 id="1220">12.2.0</h2>

<h5 id="added-11">Added</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.1.0...10.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 10.1.0 to 10.3.0</a>.</li>
  <li>Updates the Braze sample app to use React Native version 0.75.2.</li>
  <li>Updates the Braze sample app to show how to support GIFs in in-app messages and content cards on iOS.</li>
  <li>Adds the ability to conditionally import the <code class="language-plaintext highlighter-rouge">android-sdk-location</code> Braze library in <code class="language-plaintext highlighter-rouge">gradle.properties</code> via <code class="language-plaintext highlighter-rouge">importBrazeLocationLibrary=true</code>.</li>
</ul>

<h2 id="1210">12.1.0</h2>

<h5 id="added-12">Added</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 10.0.0 to 10.1.0</a>.</li>
</ul>

<h2 id="1200">12.0.0</h2>

<h5 id="breaking-8">Breaking</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 9.0.0 to 10.0.0</a>.
    <ul>
      <li>When subscribing to push notification events, the subscription will be triggered on iOS for both <code class="language-plaintext highlighter-rouge">"push_received"</code> and <code class="language-plaintext highlighter-rouge">"push_opened"</code>, instead of only for <code class="language-plaintext highlighter-rouge">"push_opened"</code> events.</li>
    </ul>
  </li>
</ul>

<h5 id="added-13">Added</h5>
<ul>
  <li>Updates the Braze sample app to use React Native version 0.74.1.</li>
  <li>Adds support for 3 new Feature Flag property types and various APIs for accessing them:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagTimestampProperty(id, key)</code> for accessing Int Unix UTC millisecond timestamps as <code class="language-plaintext highlighter-rouge">number</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagImageProperty(id, key)</code> for accessing image URLs as <code class="language-plaintext highlighter-rouge">string</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagJSONProperty(id, key)</code> for accessing JSON objects as <code class="language-plaintext highlighter-rouge">object</code> types.</li>
    </ul>
  </li>
</ul>

<h2 id="1100">11.0.0</h2>

<h5 id="breaking-9">Breaking</h5>
<ul>
  <li>Updates the native Android version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v31.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.4.0 to 31.1.0</a>.</li>
</ul>

<h5 id="fixed-11">Fixed</h5>
<ul>
  <li>Fixes an issue on Android where the <code class="language-plaintext highlighter-rouge">timestamp</code> of a <code class="language-plaintext highlighter-rouge">PushNotificationEvent</code> was incorrectly translated from a <code class="language-plaintext highlighter-rouge">long</code> to a <code class="language-plaintext highlighter-rouge">int</code>. The value received by the JavaScript layer is now the same as the value sent from the Android code.</li>
</ul>

<h2 id="1000">10.0.0</h2>

<h5 id="breaking-10">Breaking</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 8.4.0 to 9.0.0</a>.</li>
</ul>

<h5 id="added-14">Added</h5>
<ul>
  <li>Updates the native Android version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v30.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.3.0 to 30.4.0</a>.</li>
</ul>

<h2 id="920">9.2.0</h2>

<h5 id="fixed-12">Fixed</h5>
<ul>
  <li>Fixes the Android implementation of <code class="language-plaintext highlighter-rouge">Braze.setCustomUserAttribute()</code> to correctly handle null values.
    <ul>
      <li>Thanks @owonie for your contribution!</li>
    </ul>
  </li>
</ul>

<h5 id="added-15">Added</h5>
<ul>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/8.2.1...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 8.2.1 to 8.4.0</a>.</li>
</ul>

<h2 id="910">9.1.0</h2>

<h5 id="fixed-13">Fixed</h5>
<ul>
  <li>Fixes the iOS implementation of <code class="language-plaintext highlighter-rouge">Braze.registerPushToken()</code> to correctly pass the device token to the native SDK.</li>
</ul>

<h5 id="added-16">Added</h5>
<ul>
  <li>Adds the <code class="language-plaintext highlighter-rouge">BrazeInAppMessage.isTestSend</code> property, which indicates whether an in-app message was triggered as part of a test send.</li>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/8.1.0...8.2.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 8.1.0 to 8.2.1</a>.</li>
  <li>Updates the native Android version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.1.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.1.1 to 30.3.0</a>.</li>
</ul>

<h2 id="900">9.0.0</h2>

<h5 id="breaking-11">Breaking</h5>
<ul>
  <li>Bumps React Native minimum requirement version to <a href="https://reactnative.dev/blog/2023/01/12/version-071">0.71.0</a>.
    <ul>
      <li>For further details about levels of support for each React Native release, refer to <a href="https://github.com/reactwg/react-native-releases#releases-support-policy">Releases Support Policy</a> in the React Working Group.</li>
    </ul>
  </li>
  <li>Bumps the minimum required iOS version to 12.0.</li>
  <li>Updates the native iOS version bindings <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.5.0 to 8.1.0</a>.</li>
  <li>Updates the native Android version bindings <a href="https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 29.0.1 to 30.1.1</a>.</li>
</ul>

<h2 id="840">8.4.0</h2>

<h5 id="fixed-14">Fixed</h5>
<ul>
  <li>Fixes the <code class="language-plaintext highlighter-rouge">hasListeners</code> property in the iOS native layer to prevent duplicate symbol errors with other libraries.</li>
  <li>Addresses redefinition build errors when using the iOS Turbo Module with statically linked frameworks.</li>
</ul>

<h5 id="added-17">Added</h5>
<ul>
  <li>Adds support to modify the allow list for Braze tracking properties via the following TypeScript properties and methods:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">TrackingProperty</code> string enum</li>
      <li><code class="language-plaintext highlighter-rouge">TrackingPropertyAllowList</code> object interface</li>
      <li><code class="language-plaintext highlighter-rouge">updateTrackingPropertyAllowList</code> method</li>
      <li>For details, refer to the Braze <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/">iOS Privacy Manifest documentation</a>.</li>
    </ul>
  </li>
  <li>Deprecates the <code class="language-plaintext highlighter-rouge">setGoogleAdvertisingId</code> method in favor of <code class="language-plaintext highlighter-rouge">setAdTrackingEnabled</code>.
    <ul>
      <li>This new method will now set <code class="language-plaintext highlighter-rouge">adTrackingEnabled</code> flag on iOS and both the <code class="language-plaintext highlighter-rouge">adTrackingEnabled</code> flag and the Google Advertising ID on Android.</li>
    </ul>
  </li>
  <li>Exposes the <code class="language-plaintext highlighter-rouge">ContentCardTypes</code> enum through the public TypeScript interface in <code class="language-plaintext highlighter-rouge">index.d.ts</code>.</li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...7.7.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.5.0 to 7.7.0</a>.</li>
</ul>

<h2 id="830">8.3.0</h2>

<h5 id="added-18">Added</h5>
<ul>
  <li>Adds example integrations for <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications">Braze Rich Push Notifications</a> and <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories">Braze Push Stories</a> to the iOS sample app.</li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.3.0...7.5.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.3.0 to 7.5.0</a>.</li>
  <li>Adds support for <a href="https://reactnative.dev/blog/2023/12/06/0.73-debugging-improvements-stable-symlinks">React Native 0.73</a>.
    <ul>
      <li>Removes strict Java version dependencies in the <code class="language-plaintext highlighter-rouge">build.gradle</code> file of the Braze library.</li>
      <li>Updates the Braze sample app to use React Native version 0.73.1.</li>
    </ul>
  </li>
</ul>

<h2 id="820">8.2.0</h2>

<h5 id="fixed-15">Fixed</h5>
<ul>
  <li>Adds a missing update <a href="https://github.com/braze-inc/braze-android-sdk/compare/v29.0.0...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 29.0.0 to 29.0.1</a> in the <code class="language-plaintext highlighter-rouge">8.1.0</code> release.</li>
</ul>

<h5 id="added-19">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.1.0...7.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.1.0 to 7.3.0</a>.
    <ul>
      <li>This release includes compatibility with Expo Notifications. Refer to the <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/">push notification setup documentation</a> for more details.</li>
    </ul>
  </li>
</ul>

<h2 id="810">8.1.0</h2>

<h5 id="fixed-16">Fixed</h5>
<ul>
  <li>Fixes the <code class="language-plaintext highlighter-rouge">setLastKnownLocation</code> method to sanitize null inputs before calling the native layer.
    <ul>
      <li>This previously caused an issue when calling this method on the legacy React Native architecture.</li>
    </ul>
  </li>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v29.0.0...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 29.0.0 to 29.0.1</a>.</li>
</ul>

<h5 id="added-20">Added</h5>
<ul>
  <li>Push notification objects are now accessible in the JavaScript layer via new fields on the <code class="language-plaintext highlighter-rouge">PushNotificationEvent</code> interface.
    <ul>
      <li>Deprecates the following fields from the <code class="language-plaintext highlighter-rouge">PushNotificationEvent</code> interface in favor of the new names that can be used on both iOS and Android:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">push_event_type</code> -&gt; Use <code class="language-plaintext highlighter-rouge">payload_type</code> instead.</li>
          <li><code class="language-plaintext highlighter-rouge">deeplink</code> -&gt; Use <code class="language-plaintext highlighter-rouge">url</code> instead.</li>
          <li><code class="language-plaintext highlighter-rouge">content_text</code> -&gt; Use <code class="language-plaintext highlighter-rouge">body</code> instead.</li>
          <li><code class="language-plaintext highlighter-rouge">raw_android_push_data</code> -&gt; Use the <code class="language-plaintext highlighter-rouge">android</code> object instead.</li>
          <li><code class="language-plaintext highlighter-rouge">kvp_data</code> -&gt; Use <code class="language-plaintext highlighter-rouge">braze_properties</code> instead.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Adds iOS support for the listener event <code class="language-plaintext highlighter-rouge">Braze.Events.PUSH_NOTIFICATION_EVENT</code>.
    <ul>
      <li>On iOS, only <code class="language-plaintext highlighter-rouge">"push_opened"</code> events are supported, indicating the user interacted with the received notification.</li>
      <li>The iOS event does not support the deprecated legacy fields mentioned above.</li>
    </ul>
  </li>
  <li>Adds methods to manually perform the action of an In-App Message or Content Card when using a custom UI.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.performInAppMessageButtonAction(inAppMessage, buttonId)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.performInAppMessageAction(inAppMessage)</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.processContentCardClickAction(id)</code></li>
    </ul>
  </li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.0.0...7.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.0.0 to 7.1.0</a>.</li>
</ul>

<h2 id="800">8.0.0</h2>

<h5 id="breaking-12">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v29.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 27.0.1 to 29.0.0</a>.</li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.6.0...7.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.6.0 to 7.0.0</a>.</li>
  <li>Renames the <code class="language-plaintext highlighter-rouge">Banner</code> Content Card type to <code class="language-plaintext highlighter-rouge">ImageOnly</code>:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">BannerContentCard</code> → <code class="language-plaintext highlighter-rouge">ImageOnlyContentCard</code></li>
      <li><code class="language-plaintext highlighter-rouge">ContentCardTypes.BANNER</code> → <code class="language-plaintext highlighter-rouge">ContentCardTypes.IMAGE_ONLY</code></li>
      <li>On Android, if the XML files in your project contain the word <code class="language-plaintext highlighter-rouge">banner</code> for Content Cards, it should be replaced with <code class="language-plaintext highlighter-rouge">image_only</code>.</li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">Braze.getFeatureFlag(id)</code> will now return <code class="language-plaintext highlighter-rouge">null</code> if the feature flag does not exist.</li>
  <li><code class="language-plaintext highlighter-rouge">Braze.Events.FEATURE_FLAGS_UPDATED</code> will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.</li>
</ul>

<h5 id="added-21">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">Braze.getUserId()</code> to get the ID of the current user.</li>
</ul>

<h2 id="700">7.0.0</h2>

<h5 id="breaking-13">Breaking</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701">from Braze Android SDK 26.3.2 to 27.0.1</a>.</li>
</ul>

<h5 id="fixed-17">Fixed</h5>
<ul>
  <li>Fixes the Android layer to record date custom user attributes as ISO strings instead of integers.</li>
  <li>Fixes a bug introduced in <code class="language-plaintext highlighter-rouge">6.0.0</code> where <code class="language-plaintext highlighter-rouge">Braze.getInitialUrl()</code> may not trigger the callback on Android.</li>
</ul>

<h5 id="added-22">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.4.0...6.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.4.0 to 6.6.0</a>.</li>
  <li>Adds support for nested custom user attributes.
    <ul>
      <li>The <code class="language-plaintext highlighter-rouge">setCustomUserAttribute</code> now accepts objects and arrays of objects.</li>
      <li>Adds an optional <code class="language-plaintext highlighter-rouge">merge</code> parameter to the <code class="language-plaintext highlighter-rouge">setCustomUserAttribute</code> method. This is a non-breaking change.</li>
      <li>Reference our <a href="https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/">public docs</a> for more information.</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">Braze.setLastKnownLocation()</code> to set the last known location for the user.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">Braze.registerPushToken()</code> in the JavaScript layer to post a push token to Braze’s servers.
    <ul>
      <li>Deprecates <code class="language-plaintext highlighter-rouge">Braze.registerAndroidPushToken()</code> in favor of <code class="language-plaintext highlighter-rouge">Braze.registerPushToken()</code>.</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">Braze.getCachedContentCards()</code> to get the most recent content cards from the cache, without a refresh.</li>
  <li>Adds support for the Feature Flag method <code class="language-plaintext highlighter-rouge">logFeatureFlagImpression(id)</code>.</li>
</ul>

<h2 id="602">6.0.2</h2>

<h5 id="fixed-18">Fixed</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2632">from Braze Android SDK 26.3.1 to 26.3.2</a>.</li>
</ul>

<h2 id="601">6.0.1</h2>

<h5 id="fixed-19">Fixed</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">'DEFINES_MODULE' =&gt; 'YES'</code> to the iOS Podspec when compiling the Turbo Module to prevent the need for static framework linkage when using the Braze Expo plugin.</li>
</ul>

<h2 id="600">6.0.0</h2>

<h5 id="breaking-14">Breaking</h5>
<ul>
  <li>If you are using the New Architecture, this version requires React Native <code class="language-plaintext highlighter-rouge">0.70</code> or higher.</li>
  <li>Fixes the sample setup steps for iOS apps conforming to <code class="language-plaintext highlighter-rouge">RCTAppDelegate</code>.
    <ul>
      <li>⚠️ If your app conforms to <code class="language-plaintext highlighter-rouge">RCTAppDelegate</code> and was following our previous <code class="language-plaintext highlighter-rouge">AppDelegate</code> setup in the sample project or <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/react_sdk_setup/?tab=ios#step-2-complete-native-setup">Braze documentation</a>, you will need to reference our <a href="https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm">updated samples</a> to prevent any crashes from occurring when subscribing to events in the new Turbo Module. ⚠️</li>
    </ul>
  </li>
  <li>If your project contains unit tests that depend on the Braze React Native module, you will need to update your imports to the <code class="language-plaintext highlighter-rouge">NativeBrazeReactModule</code> file to properly mock the Turbo Module functions in Jest.
    <ul>
      <li>For an example, refer to the sample test setup <a href="https://github.com/braze-inc/braze-react-native-sdk/tree/master/__tests__">here</a>.</li>
    </ul>
  </li>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v25.0.0...v26.3.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 25.0.0 to 26.3.1</a>.</li>
  <li>Fixes the presentation of in-app messages to match the documented behavior.
    <ul>
      <li>Calling <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage</code> or <code class="language-plaintext highlighter-rouge">addListener</code> in the Javascript layer will no longer cause a custom <code class="language-plaintext highlighter-rouge">BrazeInAppMessageUIDelegate</code> implementation on iOS to be ignored.</li>
      <li>Calling <code class="language-plaintext highlighter-rouge">Braze.addListener</code> for the <code class="language-plaintext highlighter-rouge">inAppMessageReceived</code> event will subscribe in both the Javascript and the native layers (iOS + Android). This means it is no longer required to call <code class="language-plaintext highlighter-rouge">Braze.subscribeToInAppMessage</code>.
        <ul>
          <li>Per the Braze documentation, you do not need to explicitly call <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage</code> to use the default In-App Message UI.</li>
        </ul>
      </li>
      <li>See our documentation for more details around <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/inapp_messages/?tab=ios#advanced-customization">Advanced customization</a>.</li>
    </ul>
  </li>
</ul>

<h5 id="added-23">Added</h5>
<ul>
  <li>Migrates the Braze bridge to a backwards-compatible <a href="https://reactnative.dev/docs/next/the-new-architecture/pillars-turbomodules">New Architecture Turbo Module</a>.
    <ul>
      <li>This is a non-breaking change to your existing imports of the Braze SDK if you are using React Native <code class="language-plaintext highlighter-rouge">0.70</code>+.</li>
      <li>The Braze SDK continues to be compatible with both the New Architecture and old React Native architecture.</li>
    </ul>
  </li>
  <li>Adds the <code class="language-plaintext highlighter-rouge">getDeviceId</code> method to replace <code class="language-plaintext highlighter-rouge">getInstallTrackingId</code>, which is now deprecated.</li>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.3.1...6.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.3.1 to 6.4.0</a>.</li>
  <li>Adds a conditional library namespace to the Android <code class="language-plaintext highlighter-rouge">build.gradle</code> file to prepare for React Native 0.73, which uses AGP 8.x.
    <ul>
      <li>For more details, refer to this <a href="https://github.com/react-native-community/discussions-and-proposals/issues/671">React Native announcement</a>.</li>
    </ul>
  </li>
</ul>

<h2 id="520">5.2.0</h2>

<h5 id="fixed-20">Fixed</h5>
<ul>
  <li>Fixes an issue on Android where push notifications wouldn’t be forwarded after the app was closed.</li>
  <li>Fixes an issue on iOS preventing in-app message subscription events from being sent if <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage</code> is called prior to any <code class="language-plaintext highlighter-rouge">Braze.addListener</code> calls.</li>
  <li>Changed the Java compatibility version for the Android plugin to Java 11.</li>
</ul>

<h5 id="added-24">Added</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.2.0...6.3.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.2.0 to 6.3.1</a>.</li>
</ul>

<h2 id="510">5.1.0</h2>

<h5 id="fixed-21">Fixed</h5>
<ul>
  <li>Fixes an issue that occured whenever a custom event is logged with dictionary properties using a key named “type”.</li>
  <li>Removes the automatic assignment of <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/delegate"><code class="language-plaintext highlighter-rouge">BrazeDelegate</code></a> in the iOS bridge, allowing for custom implementations to be assigned to the <code class="language-plaintext highlighter-rouge">braze</code> instance.</li>
</ul>

<h2 id="500">5.0.0</h2>

<h5 id="breaking-15">Breaking</h5>
<ul>
  <li>Updates the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/5.13.0...6.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4edR1">from Braze Swift SDK 5.13.0 to 6.2.0</a>.</li>
  <li>Removes <code class="language-plaintext highlighter-rouge">setSDKFlavor</code> and <code class="language-plaintext highlighter-rouge">setMetadata</code>, which were no-ops starting from version <code class="language-plaintext highlighter-rouge">2.0.0</code>.
    <ul>
      <li>On iOS, these fields must be set using the <code class="language-plaintext highlighter-rouge">Braze.Configuration</code> object at SDK initialization.</li>
      <li>On Android, these fields must be set via the <code class="language-plaintext highlighter-rouge">braze.xml</code> file.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-22">Fixed</h5>
<ul>
  <li>Fixes an issue on Android with <code class="language-plaintext highlighter-rouge">getNewsFeedCards()</code> and <code class="language-plaintext highlighter-rouge">getContentCards()</code> where promises could be invoked more than once.</li>
</ul>

<h5 id="added-25">Added</h5>
<ul>
  <li>Updates the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v24.3.0...v25.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 24.3.0 to 25.0.0</a>.</li>
</ul>

<h2 id="410">4.1.0</h2>

<h5 id="fixed-23">Fixed</h5>
<ul>
  <li>Fixes an issue in the <code class="language-plaintext highlighter-rouge">PushNotificationEvent</code> object introduced in <code class="language-plaintext highlighter-rouge">2.0.1</code> where a field was named <code class="language-plaintext highlighter-rouge">context_text</code> instead of the correct value of <code class="language-plaintext highlighter-rouge">content_text</code>.</li>
</ul>

<h5 id="added-26">Added</h5>
<ul>
  <li>Adds support for the upcoming Braze Feature Flags product with the following methods:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlag(id)</code></li>
      <li><code class="language-plaintext highlighter-rouge">getAllFeatureFlags()</code></li>
      <li><code class="language-plaintext highlighter-rouge">refreshFeatureFlags()</code></li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagBooleanProperty(id, key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagStringProperty(id, key)</code></li>
      <li><code class="language-plaintext highlighter-rouge">getFeatureFlagNumberProperty(id, key)</code></li>
    </ul>
  </li>
  <li>Adds the Braze Event key <code class="language-plaintext highlighter-rouge">Braze.Events.FEATURE_FLAGS_UPDATED</code> for subscribing to Feature Flags updates.</li>
</ul>

<h2 id="400">4.0.0</h2>

<h5 id="breaking-16">Breaking</h5>
<ul>
  <li>The iOS bridge now automatically attaches the default In-App Message UI with the <code class="language-plaintext highlighter-rouge">braze</code> instance, without needing to call <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage()</code>. This updates the behavior from <code class="language-plaintext highlighter-rouge">2.0.0</code> to simplify integration.
    <ul>
      <li>This change doesn’t affect integrations using custom UIs for in-app messages.</li>
    </ul>
  </li>
  <li>Changes the returned value when subscribing to <code class="language-plaintext highlighter-rouge">Braze.Events.CONTENT_CARDS_UPDATED</code> to be a <code class="language-plaintext highlighter-rouge">Braze.ContentCardsUpdatedEvent</code> object instead of a boolean.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.ContentCardsUpdatedEvent</code> contains a <code class="language-plaintext highlighter-rouge">cards</code> property which is an array of the Content Cards in the update.</li>
      <li>Thanks @Minishlink for your contribution!</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-24">Fixed</h5>
<ul>
  <li>Fixes an issue in the iOS bridge where <code class="language-plaintext highlighter-rouge">getContentCards()</code> and <code class="language-plaintext highlighter-rouge">getNewsFeedCards()</code> returned data in a different format than the Android bridge.</li>
  <li>Fixes the behavior when using the recommended iOS integration where the React Bridge delegate had conflicts with other dependencies. The updated sample app code can be found <a href="https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm">here</a>.</li>
</ul>

<h5 id="added-27">Added</h5>
<ul>
  <li>Updates the native iOS bridge to <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#5130">Braze Swift SDK 5.13.0</a>.</li>
  <li>Improves typescript definitions for <code class="language-plaintext highlighter-rouge">addListener</code> event types.</li>
</ul>

<h2 id="300">3.0.0</h2>

<blockquote>
  <p>Starting with this release, this SDK will use <a href="https://semver.org/">Semantic Versioning</a>.</p>
</blockquote>

<h5 id="-breaking">⚠ Breaking</h5>
<ul>
  <li>Fixes the behavior in the iOS bridge introduced in version <code class="language-plaintext highlighter-rouge">2.0.0</code> when logging clicks for in-app messages, content cards, and news feed cards. Calling <code class="language-plaintext highlighter-rouge">logClick</code> now only sends a click event for metrics, instead of both sending a click event as well as redirecting to the associated <code class="language-plaintext highlighter-rouge">url</code> field.
    <ul>
      <li>For instance, to log a content card click and redirect to a URL, you will need two commands:
```
Braze.logContentCardClicked(contentCard.id);</li>
    </ul>

    <p>// Your own custom implementation
Linking.openUrl(contentCard.url);
```</p>
    <ul>
      <li>This brings the iOS behavior to match version <code class="language-plaintext highlighter-rouge">1.x</code> and bring parity with Android’s behavior.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-25">Fixed</h5>
<ul>
  <li>Fixes an issue in the iOS bridge introduced in <code class="language-plaintext highlighter-rouge">2.0.0</code> where <code class="language-plaintext highlighter-rouge">getContentCards()</code> and <code class="language-plaintext highlighter-rouge">getNewsFeedCards()</code> would return an array of cards with the <code class="language-plaintext highlighter-rouge">url</code> and <code class="language-plaintext highlighter-rouge">image</code> fields as <code class="language-plaintext highlighter-rouge">null</code>.</li>
</ul>

<h5 id="changed">Changed</h5>
<ul>
  <li>Updates the native iOS bridge to <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#5112">Braze Swift SDK 5.11.2</a>.</li>
  <li>Updates the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2430">Braze Android SDK 24.3.0</a>.</li>
  <li>Updates <code class="language-plaintext highlighter-rouge">getContentCards</code> on the iOS bridge to initiate a refresh before returning the array of Content Cards. This brings parity with the Android bridge behavior.</li>
</ul>

<h2 id="210">2.1.0</h2>

<h5 id="added-28">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">'DEFINES_MODULE' =&gt; 'YES'</code> to the Cocoapod’s xcconfig to remove the need for static framework linkage on iOS when using the Braze Expo plugin.</li>
</ul>

<h2 id="202">2.0.2</h2>

<h5 id="fixed-26">Fixed</h5>
<ul>
  <li>Removes the usage of Objective-C modules when importing the Braze Swift SDK for improved compatibility with Objective-C++.
    <ul>
      <li>When importing <code class="language-plaintext highlighter-rouge">BrazeKit</code> or <code class="language-plaintext highlighter-rouge">BrazeLocation</code>, you must use the <code class="language-plaintext highlighter-rouge">#import &lt;Module/Module-Swift.h&gt;</code> syntax:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">@import BrazeKit;</code> → <code class="language-plaintext highlighter-rouge">#import &lt;BrazeKit/BrazeKit-Swift.h&gt;</code></li>
          <li><code class="language-plaintext highlighter-rouge">@import BrazeLocation;</code> → <code class="language-plaintext highlighter-rouge">#import &lt;BrazeLocation/BrazeLocation-Swift.h&gt;</code></li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h2 id="201">2.0.1</h2>

<h5 id="fixed-27">Fixed</h5>
<ul>
  <li>Fixes compatibility issues with newer versions of React Native introduced in 2.0.0.</li>
  <li>Fixes an issue where callbacks were not being executed for some user attribute methods.</li>
</ul>

<h2 id="200">2.0.0</h2>

<h5 id="-breaking-1">⚠ Breaking</h5>
<ul>
  <li>The Braze React Native SDK npm package has moved from <code class="language-plaintext highlighter-rouge">react-native-appboy-sdk</code> to <code class="language-plaintext highlighter-rouge">@braze/react-native-sdk</code>.</li>
  <li>Renames <code class="language-plaintext highlighter-rouge">AppboyReactBridge</code> and <code class="language-plaintext highlighter-rouge">AppboyReactUtils</code> to <code class="language-plaintext highlighter-rouge">BrazeReactBridge</code> and <code class="language-plaintext highlighter-rouge">BrazeReactUtils</code>, respectively.</li>
  <li>This version requires React Native <code class="language-plaintext highlighter-rouge">0.68</code> or higher.</li>
  <li>Updates the native iOS bridge to use the new Swift SDK <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#591">version 5.9.1</a>.</li>
  <li>During migration, update your project with the following changes in your iOS integration:
    <ul>
      <li>To initialize Braze, <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/a2-configure-braze">follow these integration steps</a> to create a <code class="language-plaintext highlighter-rouge">configuration</code> object. Then, add this code to complete the setup:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>let braze = BrazePlugin.initBraze(configuration)
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>This migration requires re-identifying users. To do so, you must call the <code class="language-plaintext highlighter-rouge">changeUser</code> method on the Braze instance for non-anonymous users. You can read more about it <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/#Re-identify-users">here</a>.</li>
      <li>To continue using <code class="language-plaintext highlighter-rouge">SDWebImage</code> as a dependency, add this line to your project’s <code class="language-plaintext highlighter-rouge">/ios/Podfile</code>:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>pod 'SDWebImage', :modular_headers =&gt; true
</pre></td></tr></tbody></table></code></pre></div>        </div>
        <ul>
          <li>Then, follow <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support">these setup instructions</a>.</li>
        </ul>
      </li>
      <li>To use the default In-App Message UI, make sure to call <code class="language-plaintext highlighter-rouge">subscribeToInAppMessage()</code> or else follow <a href="https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui">these instructions</a> to add it to your app.</li>
      <li>For sample code to help with the migration, reference our sample app and <a href="https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/AppDelegate.mm"><code class="language-plaintext highlighter-rouge">AppDelegate.mm</code></a> file.</li>
      <li>If you are integrating this SDK with an application that uses only Objective-C, create an empty Swift file to ensure that all the relevant Swift runtime libraries are linked. Reference <a href="https://github.com/braze-inc/braze-react-native-sdk/blob/master/BrazeProject/ios/BrazeProject/empty-file.swift">this file</a> from our sample app.</li>
    </ul>
  </li>
  <li>The following methods for News Feed are now no-ops on iOS:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.launchNewsFeed()</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getCardCountForCategories()</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.getUnreadCardCountForCategories()</code></li>
    </ul>
  </li>
  <li>Updates the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2420">Braze Android SDK 24.2.0</a>.</li>
</ul>

<h5 id="added-29">Added</h5>
<ul>
  <li>Adds the following APIs to more easily interface with the News Feed product. Thanks @swissmanu for your contribution!
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Braze.getNewsFeedCards()</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.logNewsFeedCardClicked()</code></li>
      <li><code class="language-plaintext highlighter-rouge">Braze.logNewsFeedCardImpression()</code></li>
    </ul>
  </li>
</ul>

<h2 id="1410-1">1.41.0</h2>

<h5 id="-breaking-2">⚠ Breaking</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">setFacebookData()</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">setTwitterData()</code>.</li>
</ul>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2330">Braze Android SDK 23.3.0</a>.</li>
  <li>Exposes <code class="language-plaintext highlighter-rouge">isControl</code> field for <code class="language-plaintext highlighter-rouge">ContentCard</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">kotlinVersion</code> gradle template variable. To override the Kotlin version used, please use a Gradle dependency <code class="language-plaintext highlighter-rouge">resolutionStrategy</code>.</li>
</ul>

<h2 id="1400-1">1.40.0</h2>

<h5 id="-breaking-3">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2321">Braze Android SDK 23.2.1</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#451">Braze iOS SDK 4.5.1</a>.</li>
</ul>

<h5 id="changed-2">Changed</h5>
<ul>
  <li>Updated the <code class="language-plaintext highlighter-rouge">React</code> podspec dependency to <code class="language-plaintext highlighter-rouge">React-Core</code>.</li>
</ul>

<h2 id="1390">1.39.0</h2>

<h5 id="-breaking-4">⚠ Breaking</h5>
<ul>
  <li>Renamed the <code class="language-plaintext highlighter-rouge">kotlin_version</code> gradle template variable to <code class="language-plaintext highlighter-rouge">kotlinVersion</code>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2320">Braze Android SDK 23.2.0</a>.</li>
</ul>

<h5 id="fixed-28">Fixed</h5>
<ul>
  <li>Fixed an issue that caused a NativeEventEmitter warning message to appear.</li>
</ul>

<h2 id="1381">1.38.1</h2>

<h5 id="fixed-29">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 1.38.0 where <code class="language-plaintext highlighter-rouge">setEmail</code> did not work as expected on Android.</li>
</ul>

<h2 id="1380">1.38.0</h2>

<h5 id="-breaking-5">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2301">Braze Android SDK 23.0.1</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#450">Braze iOS SDK 4.5.0</a>.</li>
  <li>The Braze React Native Android SDK now requires Kotlin directly for compilation. An example is included below:
    <div class="language-groovy highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
</pre></td><td class="rouge-code"><pre>  <span class="n">buildscript</span> <span class="o">{</span>
      <span class="n">ext</span><span class="o">.</span><span class="na">kotlin_version</span> <span class="o">=</span> <span class="s1">'1.6.0'</span>

      <span class="n">dependencies</span> <span class="o">{</span>
          <span class="n">classpath</span> <span class="s2">"org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"</span>
      <span class="o">}</span>
  <span class="o">}</span>
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
</ul>

<h5 id="added-30">Added</h5>
<ul>
  <li>Introduced <code class="language-plaintext highlighter-rouge">Braze.Events.PUSH_NOTIFICATION_EVENT</code> which can be used to listen for Braze Push Notification events on Android. See example below:
    <div class="language-javascript highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="nx">Braze</span><span class="p">.</span><span class="nf">addListener</span><span class="p">(</span><span class="nx">Braze</span><span class="p">.</span><span class="nx">Events</span><span class="p">.</span><span class="nx">PUSH_NOTIFICATION_EVENT</span><span class="p">,</span> <span class="kd">function</span><span class="p">(</span><span class="nx">data</span><span class="p">)</span> <span class="p">{</span>
  <span class="nx">console</span><span class="p">.</span><span class="nf">log</span><span class="p">(</span><span class="s2">`Push Notification event of type </span><span class="p">${</span><span class="nx">data</span><span class="p">.</span><span class="nx">push_event_type</span><span class="p">}</span><span class="s2"> seen.
    Title </span><span class="p">${</span><span class="nx">data</span><span class="p">.</span><span class="nx">title</span><span class="p">}</span><span class="s2">\n and deeplink </span><span class="p">${</span><span class="nx">data</span><span class="p">.</span><span class="nx">deeplink</span><span class="p">}</span><span class="s2">`</span><span class="p">);</span>
  <span class="nx">console</span><span class="p">.</span><span class="nf">log</span><span class="p">(</span><span class="nx">JSON</span><span class="p">.</span><span class="nf">stringify</span><span class="p">(</span><span class="nx">data</span><span class="p">,</span> <span class="kc">undefined</span><span class="p">,</span> <span class="mi">2</span><span class="p">));</span>
<span class="p">});</span>
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">Braze.requestPushPermission()</code> to request a permissions prompt for push notifications.</li>
</ul>

<h2 id="1370">1.37.0</h2>

<h5 id="-breaking-6">⚠ Breaking</h5>
<ul>
  <li>The Braze React Native SDK now exports its default object as an ES Module. If you currently import the SDK using <code class="language-plaintext highlighter-rouge">require()</code>, you will need to now import it as a standard ES Module (e.g. <code class="language-plaintext highlighter-rouge">import Braze from "react-native-appboy-sdk"</code>).</li>
</ul>

<h5 id="added-31">Added</h5>
<ul>
  <li>Introduced <code class="language-plaintext highlighter-rouge">Braze.subscribeToInAppMessage()</code> which publishes an event to the Javascript layer when an in-app message is triggered and allows you to choose whether or not to use the default Braze UI to display in-app messages.</li>
</ul>

<h2 id="1360">1.36.0</h2>

<h5 id="-breaking-7">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2100">Braze Android SDK 21.0.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#444">Braze iOS SDK 4.4.4</a>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">setAvatarImageUrl()</code>.</li>
  <li>Removed <code class="language-plaintext highlighter-rouge">logContentCardsDisplayed</code>. This method was not part of the recommended Content Cards integration and can be safely removed.</li>
</ul>

<h2 id="1351">1.35.1</h2>

<h5 id="fixed-30">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">setMetadata</code> did not have a method implementation for Android.</li>
</ul>

<h2 id="1350">1.35.0</h2>

<h5 id="-breaking-8">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#442">Braze iOS SDK 4.4.2</a>.</li>
  <li>Drops support for iOS 9 and 10.</li>
</ul>

<h2 id="1341">1.34.1</h2>

<h5 id="fixed-31">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">getInitialUrl</code> would not resolve when there is no initial URL.</li>
</ul>

<h2 id="1340">1.34.0</h2>

<h5 id="-breaking-9">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1801">Braze Android SDK 18.0.1</a>.</li>
</ul>

<h5 id="fixed-32">Fixed</h5>
<ul>
  <li>Fixed an issue with Content Card types. Thanks @jtparret!</li>
</ul>

<h5 id="changed-3">Changed</h5>
<ul>
  <li>Improved logging around <code class="language-plaintext highlighter-rouge">getInitialUrl</code>.</li>
</ul>

<h2 id="1331">1.33.1</h2>

<h5 id="fixed-33">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 1.33.0 that caused a build error on iOS.</li>
</ul>

<h2 id="1330">1.33.0</h2>

<h5 id="-breaking-10">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1600">Braze Android SDK 16.0.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#434">Braze iOS SDK 4.3.4</a>.</li>
</ul>

<h5 id="added-32">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.addToSubscriptionGroup()</code> and <code class="language-plaintext highlighter-rouge">ReactAppboy.removeFromSubscriptionGroup()</code> to manage SMS/Email Subscription Groups.</li>
  <li>Custom events and purchases now support nested properties. In addition to integers, floats, booleans, dates, or strings, a JSON object can be provided containing dictionaries of arrays or nested dictionaries. All properties combined can be up to 50 KB in total length.</li>
</ul>

<h2 id="1320-1">1.32.0</h2>

<h5 id="-breaking-11">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1500">Braze Android SDK 15.0.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#432">Braze iOS SDK 4.3.2</a>.</li>
</ul>

<h2 id="1310-1">1.31.0</h2>

<h5 id="-breaking-12">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#431">Braze iOS SDK 4.3.1</a>.</li>
</ul>

<h5 id="added-33">Added</h5>
<ul>
  <li>Added support for new SDK Authentication feature to the Javascript layer. See <code class="language-plaintext highlighter-rouge">setSdkAuthenticationSignature</code> on the <code class="language-plaintext highlighter-rouge">Appboy</code> interface, as well as the optional <code class="language-plaintext highlighter-rouge">signature</code> parameter on <code class="language-plaintext highlighter-rouge">ReactAppboy.changeUser</code>.</li>
</ul>

<h2 id="1300-1">1.30.0</h2>

<h5 id="-breaking-13">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#430">Braze iOS SDK 4.3.0</a>, which fixes a crashing issue with Content Cards when using the default UI.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1401">Braze Android SDK 14.0.1</a>.</li>
</ul>

<h2 id="1291">1.29.1</h2>

<h5 id="️-known-issues">⚠️ Known Issues</h5>
<ul>
  <li>This release contains a known issue with the Content Cards default UI on iOS, where showing a “Classic” type card with an image causes a crash. If you are using the default Content Cards UI, do not upgrade to this version.</li>
</ul>

<h5 id="fixed-34">Fixed</h5>
<ul>
  <li>Fixed issue introduced in 1.29.0 where calling <code class="language-plaintext highlighter-rouge">ReactAppboy.changeUser</code> would cause an error on Android.</li>
</ul>

<h2 id="1290">1.29.0</h2>

<h5 id="️-known-issues-1">⚠️ Known Issues</h5>
<ul>
  <li>This release contains a known issue with the Content Cards default UI on iOS, where showing a “Classic” type card with an image causes a crash. If you are using the default Content Cards UI, do not upgrade to this version.</li>
</ul>

<h5 id="-breaking-14">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1400">Braze Android SDK 14.0.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#420">Braze iOS SDK 4.2.0</a>.</li>
</ul>

<h2 id="1280">1.28.0</h2>

<h5 id="-breaking-15">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#402">Braze iOS SDK 4.0.2</a>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312">Braze Android SDK 13.1.2</a>, which contains support for Android 12.</li>
</ul>

<h5 id="fixed-35">Fixed</h5>
<ul>
  <li>Fixed an issue where calling <code class="language-plaintext highlighter-rouge">getInstallTrackingId()</code> while the SDK was disabled would cause a crash on iOS.</li>
</ul>

<h5 id="added-34">Added</h5>
<ul>
  <li>Added support for <code class="language-plaintext highlighter-rouge">ReactAppboy.setGoogleAdvertisingId()</code> to set the Google Advertising ID and associated ad-tracking enabled field for Android devices. This is a no-op on iOS.</li>
</ul>

<h2 id="1270">1.27.0</h2>

<h5 id="-breaking-16">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3331">Braze iOS SDK 3.33.1</a>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1300">Braze Android SDK 13.0.0</a>.</li>
</ul>

<h5 id="added-35">Added</h5>
<ul>
  <li>Added support for receiving iOS push action button deep links in <code class="language-plaintext highlighter-rouge">ReactAppboy.getInitialURL()</code>. If you are using <code class="language-plaintext highlighter-rouge">ReactAppboy.getInitialURL()</code> and implement iOS push action button categories, add the following code to the beginning of your <code class="language-plaintext highlighter-rouge">userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:</code>:
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>[[AppboyReactUtils sharedInstance] populateInitialUrlForCategories:response.notification.request.content.userInfo];
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
</ul>

<h2 id="1260">1.26.0</h2>

<h5 id="-breaking-17">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3312">Braze iOS SDK 3.31.2</a>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1200">Braze Android SDK 12.0.0</a>.</li>
</ul>

<h2 id="1250">1.25.0</h2>

<h5 id="-breaking-18">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3291">Braze iOS SDK 3.29.1</a>, which adds improved support for in-app message display on iPhone 12 models.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1100">Braze Android SDK 11.0.0</a>.</li>
</ul>

<h2 id="1240">1.24.0</h2>

<h5 id="-breaking-19">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3280">Braze iOS SDK 3.28.0</a>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1010">Braze Android SDK 10.1.0</a>. Please read the Braze Android SDK changelog for details.</li>
</ul>

<h2 id="1230">1.23.0</h2>

<h5 id="-breaking-20">⚠ Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3270">Braze iOS SDK 3.27.0</a>. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.</li>
</ul>

<h2 id="1220-1">1.22.0</h2>

<h5 id="changed-4">Changed</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810">Braze Android SDK 8.1.0</a>, which contains support for Android 11.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3261">Braze iOS SDK 3.26.1</a>, which contains preliminary support for iOS 14.</li>
</ul>

<h2 id="1210-1">1.21.0</h2>

<h5 id="-breaking-21">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#801">Braze Android SDK 8.0.1</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3260">Braze iOS SDK 3.26.0</a>.</li>
</ul>

<h5 id="added-36">Added</h5>
<ul>
  <li>Added support for working with in-app messages in the JavaScript layer. In-App Messages can be instantiated using the <code class="language-plaintext highlighter-rouge">BrazeInAppMessage</code> class. The resulting object can be passed into the analytics methods: <code class="language-plaintext highlighter-rouge">logInAppMessageClicked</code>, <code class="language-plaintext highlighter-rouge">logInAppMessageImpression</code>, and <code class="language-plaintext highlighter-rouge">logInAppMessageButtonClicked</code> (along with the button index). See the README for additional implementation details or the <code class="language-plaintext highlighter-rouge">AppboyProject</code> sample app for an integration example.</li>
</ul>

<h5 id="changed-5">Changed</h5>
<ul>
  <li>Improved Typescript definitions for <code class="language-plaintext highlighter-rouge">setCustomUserAttribute</code> and <code class="language-plaintext highlighter-rouge">incrementCustomUserAttribute</code>.
    <ul>
      <li>Thanks @janczizikow!</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-36">Fixed</h5>
<ul>
  <li>Fixed incorrect TypeScript definition for <code class="language-plaintext highlighter-rouge">ContentCard</code>.
    <ul>
      <li>Thanks @Hannes-Sandahl-Mpya!</li>
    </ul>
  </li>
</ul>

<h2 id="1200-1">1.20.0</h2>

<h5 id="-breaking-22">⚠ Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#700">Braze Android SDK 7.0.0</a>.</li>
</ul>

<h5 id="added-37">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.requestGeofences()</code> to request a Braze Geofences update for a manually provided GPS coordinate. Automatic Braze Geofence requests must be disabled to properly use this method.</li>
</ul>

<h2 id="1190">1.19.0</h2>

<h5 id="breaking-17">Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#500">Braze Android SDK 5.0.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3213">Braze iOS SDK 3.21.3</a>.</li>
</ul>

<h2 id="1180">1.18.0</h2>

<h5 id="breaking-18">Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#380">Braze Android SDK 3.8.0</a>.</li>
</ul>

<h5 id="fixed-37">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">ReactContext.getJSModule()</code> could be called before the native module was initialized.
    <ul>
      <li>Thanks @tszajna0!</li>
    </ul>
  </li>
</ul>

<h5 id="changed-6">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3204">Braze iOS SDK 3.20.4</a>.</li>
</ul>

<h2 id="1174">1.17.4</h2>

<h5 id="fixed-38">Fixed</h5>
<ul>
  <li>Removed a support library reference in <code class="language-plaintext highlighter-rouge">AppboyReactBridge.java</code> that caused Androidx compatibility issues.</li>
</ul>

<h2 id="1173">1.17.3</h2>

<h5 id="fixed-39">Fixed</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">SDWebImage</code> and <code class="language-plaintext highlighter-rouge">Headers</code> pod directories to the <code class="language-plaintext highlighter-rouge">AppboyReactBridge</code> project’s Header Search Paths. Thanks @tomauty and @mlazari for your contributions! See https://github.com/braze-inc/braze-react-native-sdk/pull/70 and https://github.com/braze-inc/braze-react-native-sdk/pull/69.</li>
</ul>

<h5 id="changed-7">Changed</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#371">Braze Android SDK 3.7.1</a>.</li>
</ul>

<h2 id="1172">1.17.2</h2>

<p><strong>Important:</strong> This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md">Braze iOS SDK Changelog</a> for more information.</p>

<h5 id="changed-8">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3202">Braze iOS SDK 3.20.2</a>.</li>
</ul>

<h2 id="1171">1.17.1</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.17.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.17.2 or above if you make use of HTML in-app messages.</p>

<h5 id="changed-9">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3201">Braze iOS SDK 3.20.1</a>.</li>
</ul>

<h2 id="1170">1.17.0</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.17.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.17.2 or above if you make use of HTML in-app messages.</p>

<h5 id="breaking-19">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3200">Braze iOS SDK 3.20.0</a>.</li>
  <li><strong>Important:</strong> Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to these methods as soon as possible to ensure a smooth transition as devices upgrade to iOS 13. In <code class="language-plaintext highlighter-rouge">application:didRegisterForRemoteNotificationsWithDeviceToken:</code>, replace
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>[[Appboy sharedInstance] registerPushToken:
              [NSString stringWithFormat:@"%@", deviceToken]];
</pre></td></tr></tbody></table></code></pre></div>    </div>
    <p>with</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>[[Appboy sharedInstance] registerDeviceToken:deviceToken];
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
  <li><code class="language-plaintext highlighter-rouge">ReactAppboy.registerPushToken()</code> was renamed to <code class="language-plaintext highlighter-rouge">ReactAppboy.registerAndroidPushToken()</code> and is now a no-op on iOS. On iOS, push tokens must now be registered through native methods.</li>
</ul>

<h2 id="1160">1.16.0</h2>

<p><strong>Important</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.17.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.17.2 or above if you make use of HTML in-app messages.</p>

<h5 id="breaking-20">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3190">Braze iOS SDK 3.19.0</a>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#370">Braze Android SDK 3.7.0</a>.</li>
  <li>Note: This Braze React Native SDK release updates to Braze Android SDK and Braze iOS SDK dependencies which no longer enable automatic Braze location collection by default. Please consult their respective changelogs for information on how to continue to enable automatic Braze location collection, as well as further information on breaking changes.</li>
  <li>Removes the Feedback feature.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">submitFeedback()</code> and <code class="language-plaintext highlighter-rouge">launchFeedback()</code> have been removed from the <code class="language-plaintext highlighter-rouge">Appboy</code> interface.</li>
    </ul>
  </li>
</ul>

<h5 id="added-38">Added</h5>
<ul>
  <li>Added the ability to more easily create custom UIs for Content Cards from within the React Native layer by providing access to card data and analytics methods in Javascript.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.getContentCards</code> for getting locally cached content cards data.
        <ul>
          <li>To request a Content Cards update, use <code class="language-plaintext highlighter-rouge">ReactAppboy.requestContentCardsRefresh()</code>.</li>
        </ul>
      </li>
      <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.logContentCardsDisplayed</code> for manually logging an impression for the content card feed.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.logContentCardClicked</code> for manually logging a click to Braze for a particular card.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.logContentCardImpression</code> for manually logging an impression to Braze for a particular card.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.logContentCardDismissed</code> for manually logging a dismissal to Braze for a particular card.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.addListener</code> for subscribing to <code class="language-plaintext highlighter-rouge">ReactAppboy.Events.CONTENT_CARDS_UPDATED</code> events.
        <ul>
          <li>After a successful update, use <code class="language-plaintext highlighter-rouge">getContentCards</code> to retrieve updated cards.</li>
          <li>
            <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>ReactAppboy.addListener(ReactAppboy.Events.CONTENT_CARDS_UPDATED, async function() {
  let cards = await ReactAppboy.getContentCards();
  console.log('Content Cards Updated.', cards);
})
</pre></td></tr></tbody></table></code></pre></div>            </div>
          </li>
        </ul>
      </li>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/pull/58. Thanks @alexmbp!</li>
    </ul>
  </li>
</ul>

<h2 id="1150">1.15.0</h2>

<h5 id="breaking-21">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3170">Braze iOS SDK 3.17.0</a>.</li>
  <li>Removed the <code class="language-plaintext highlighter-rouge">NewsFeedLaunchOptions</code> enum. Using these arguments with <code class="language-plaintext highlighter-rouge">launchNewsFeed()</code> had been a no-op since version 1.7.0.</li>
</ul>

<h2 id="1140">1.14.0</h2>

<h5 id="breaking-22">Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#350">Braze Android SDK 3.5.0</a>.</li>
</ul>

<h5 id="fixed-40">Fixed</h5>
<ul>
  <li>Fixed an issue where logging custom events or purchases without event properties would cause crashes on Android, for example <code class="language-plaintext highlighter-rouge">logCustomEvent("event")</code>.</li>
</ul>

<h5 id="added-39">Added</h5>
<ul>
  <li>Added additional TypeScript definitions.</li>
</ul>

<h2 id="1130">1.13.0</h2>

<h5 id="breaking-23">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3150">Braze iOS SDK 3.15.0</a>.
    <ul>
      <li>This release of the iOS SDK added support for SDWebImage version 5.0.</li>
      <li>Note that upgrading to SDWebImage 5.0 also removed the FLAnimatedImage transitive dependency.</li>
    </ul>
  </li>
</ul>

<h2 id="1120">1.12.0</h2>

<h5 id="breaking-24">Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#330">Braze Android SDK 3.3.0</a>.</li>
</ul>

<h5 id="added-40">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.launchContentCards()</code> for launching the content cards UI.</li>
</ul>

<h2 id="1111">1.11.1</h2>

<h5 id="added-41">Added</h5>
<ul>
  <li>Added Typescript definitions for the <code class="language-plaintext highlighter-rouge">Appboy</code> interface.
    <ul>
      <li>Thanks @ahanriat and @josin for your contributions! See https://github.com/braze-inc/braze-react-native-sdk/pull/57 and https://github.com/braze-inc/braze-react-native-sdk/pull/38.</li>
      <li>Note that certain less-used parts of the API were excluded. Please file an issue if you would like specific method(s) added.</li>
    </ul>
  </li>
</ul>

<h2 id="1110">1.11.0</h2>

<h5 id="breaking-25">Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#320">Braze Android SDK 3.2.0</a>.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to directly use the Firebase messaging event <code class="language-plaintext highlighter-rouge">com.google.firebase.MESSAGING_EVENT</code>. This is now the recommended way to integrate Firebase push with Braze. The <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> should be removed from your <code class="language-plaintext highlighter-rouge">AndroidManifest</code> and replaced with the following:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre>&lt;service android:name="com.appboy.AppboyFirebaseMessagingService"&gt;
  &lt;intent-filter&gt;
    &lt;action android:name="com.google.firebase.MESSAGING_EVENT" /&gt;
  &lt;/intent-filter&gt;
&lt;/service&gt;
</pre></td></tr></tbody></table></code></pre></div>        </div>
        <ul>
          <li>Also note that any <code class="language-plaintext highlighter-rouge">c2dm</code> related permissions should be removed from your manifest as Braze does not require any extra permissions for <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to work correctly.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3140">Braze iOS SDK 3.14.0</a>.
    <ul>
      <li>Dropped support for iOS 8.</li>
    </ul>
  </li>
</ul>

<h5 id="added-42">Added</h5>
<ul>
  <li>Added support for sending JavaScript <code class="language-plaintext highlighter-rouge">Date()</code> type custom event and purchase properties through the <code class="language-plaintext highlighter-rouge">Appboy</code> interface.</li>
</ul>

<h2 id="1100-1">1.10.0</h2>

<h5 id="breaking-26">Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#310">Braze Android SDK 3.1.0</a>.</li>
</ul>

<h5 id="added-43">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">addAlias(aliasName, aliasLabel)</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to allow aliasing users.
    <ul>
      <li>Thanks @alexmbp!</li>
    </ul>
  </li>
</ul>

<h5 id="changed-10">Changed</h5>
<ul>
  <li>Updated <code class="language-plaintext highlighter-rouge">build.gradle</code> to use <code class="language-plaintext highlighter-rouge">project.ext</code> config if available.</li>
</ul>

<h2 id="190">1.9.0</h2>

<h5 id="breaking-27">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#3110">Braze iOS SDK 3.11.0</a>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#301">Braze Android SDK 3.0.1</a>.</li>
  <li>Updated the Android wrapper to use <code class="language-plaintext highlighter-rouge">api</code> and <code class="language-plaintext highlighter-rouge">implementation</code> syntax in it’s <code class="language-plaintext highlighter-rouge">build.gradle</code> instead of <code class="language-plaintext highlighter-rouge">compile</code>. As part of this work, the Android Gradle plugin version was updated to <code class="language-plaintext highlighter-rouge">3.2.1</code>.</li>
</ul>

<h5 id="fixed-41">Fixed</h5>
<ul>
  <li>Fixed an issue where the Android wrapper would include an older version of React Native in test APK builds.</li>
</ul>

<h5 id="added-44">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">setUserAttributionData()</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to allow setting the attribution data for the current user.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">getInstallTrackingId()</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to allow getting the install tracking id. This method is equivalent to calling <code class="language-plaintext highlighter-rouge">Appboy.getInstallTrackingId()</code> on Android and returns the IDFV on iOS.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">setLanguage()</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to allow setting a language for the current user.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">hideCurrentInAppMessage()</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to allow hiding of the currently displayed in-app message.</li>
</ul>

<h5 id="changed-11">Changed</h5>
<ul>
  <li>Updated our sample projects to use React Native <code class="language-plaintext highlighter-rouge">0.56</code>.</li>
</ul>

<h2 id="181">1.8.1</h2>

<h5 id="changed-12">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#384">Braze iOS SDK 3.8.4</a>.</li>
</ul>

<h2 id="180">1.8.0</h2>

<h5 id="breaking-28">Breaking</h5>
<ul>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#270">Braze Android SDK 2.7.0</a>.
    <ul>
      <li><strong>Important:</strong> Note that in Braze Android SDK 2.7.0, <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code> was renamed to <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code>. This receiver is intended to be used for Firebase integrations. Please update the <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code> declaration in your <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code> to reference <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> and remove the <code class="language-plaintext highlighter-rouge">com.google.android.c2dm.intent.REGISTRATION</code> intent filter action.</li>
    </ul>
  </li>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#383">Braze iOS SDK 3.8.3</a>.</li>
</ul>

<h5 id="added-45">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">setLocationCustomAttribute()</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to allow setting of custom location attributes.</li>
</ul>

<h2 id="173">1.7.3</h2>

<h5 id="added-46">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">requestLocationInitialization()</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface. Calling this method is the equivalent of calling <code class="language-plaintext highlighter-rouge">AppboyLocationService.requestInitialization()</code> on the native Braze Android SDK. The method is a no-op on iOS.</li>
</ul>

<h2 id="172">1.7.2</h2>

<h5 id="fixed-42">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in <code class="language-plaintext highlighter-rouge">1.7.0</code> where calling <code class="language-plaintext highlighter-rouge">launchNewsFeed()</code> would cause crashes in the Android bridge.</li>
</ul>

<h2 id="171">1.7.1</h2>

<h5 id="fixed-43">Fixed</h5>
<ul>
  <li>Updated the podspec to point to Braze iOS SDK version 3.5.1.</li>
</ul>

<h2 id="170">1.7.0</h2>

<h5 id="breaking-29">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#351">Braze iOS SDK 3.5.1</a>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#240">Appboy Android SDK 2.4.0</a>.</li>
</ul>

<h5 id="added-47">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">Other</code>, <code class="language-plaintext highlighter-rouge">Unknown</code>, <code class="language-plaintext highlighter-rouge">Not Applicable</code>, and <code class="language-plaintext highlighter-rouge">Prefer not to Say</code> options for user gender.</li>
  <li>Updated the <code class="language-plaintext highlighter-rouge">AppboyProject</code> sample app to use FCM instead of GCM.</li>
  <li>Added toasts to provide feedback for user actions in the <code class="language-plaintext highlighter-rouge">AppboyProject</code> sample app.</li>
  <li>Implemented <code class="language-plaintext highlighter-rouge">requiresMainQueueSetup</code> in <code class="language-plaintext highlighter-rouge">AppboyReactBridge.m</code> to prevent warnings in React Native 0.49+.
    <ul>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/pull/39. Thanks @danieldecsi!</li>
    </ul>
  </li>
</ul>

<h5 id="changed-13">Changed</h5>
<ul>
  <li>Passing launch options into <code class="language-plaintext highlighter-rouge">launchNewsFeed()</code> is now a no-op.</li>
</ul>

<h2 id="160">1.6.0</h2>

<h5 id="breaking-30">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#333">Braze iOS SDK 3.3.3</a>.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#225">Braze Android SDK 2.2.5</a>.</li>
</ul>

<h5 id="added-48">Added</h5>
<ul>
  <li>Added support for wiping all customer data created by the Braze SDK via <code class="language-plaintext highlighter-rouge">Appboy.wipeData()</code>.
    <ul>
      <li>Note that on iOS, <code class="language-plaintext highlighter-rouge">wipeData()</code> will disable the SDK for the remainder of the app run. For more information, see our iOS SDK’s documentation for <a href="http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733"><code class="language-plaintext highlighter-rouge">disableSDK</code></a>.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.disableSDK()</code> to disable the Braze SDK immediately.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.enableSDK()</code> to re-enable the SDK after a call to <code class="language-plaintext highlighter-rouge">Appboy.disableSDK()</code>.
    <ul>
      <li>Note that on iOS, <code class="language-plaintext highlighter-rouge">enableSDK()</code> will not enable the SDK immediately. For more information, see our iOS SDK’s documentation for <a href="http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b"><code class="language-plaintext highlighter-rouge">requestEnableSDKOnNextAppRun</code></a>.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-14">Changed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">allowBackup</code> from the plugin <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code>.
    <ul>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/pull/34. Thanks @SMJ93!</li>
    </ul>
  </li>
</ul>

<h2 id="152">1.5.2</h2>

<h5 id="fixed-44">Fixed</h5>
<ul>
  <li>Fixed a race condition between SDK flavor reporting and sharedInstance initialization on iOS.</li>
</ul>

<h2 id="151">1.5.1</h2>

<h5 id="fixed-45">Fixed</h5>
<ul>
  <li>Fixed a bug that caused opted-in subscription states to not be reflected on the user profile.</li>
</ul>

<h2 id="150">1.5.0</h2>

<h5 id="breaking-31">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#300">Braze iOS SDK 3.0.0</a> or later.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#224">Braze Android SDK 2.2.4</a>.</li>
  <li>Changed success callbacks on <code class="language-plaintext highlighter-rouge">submitFeedback()</code> on Android to always return <code class="language-plaintext highlighter-rouge">true</code> as <code class="language-plaintext highlighter-rouge">submitFeedback()</code> was changed to return <code class="language-plaintext highlighter-rouge">void</code> in the native SDK.</li>
</ul>

<h2 id="141">1.4.1</h2>

<h5 id="added-49">Added</h5>
<ul>
  <li>Added support for apps that use use_frameworks in Podfile.
    <ul>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/commit/6db78a5bbeb31457f8a1dcf988a3265d8db9a437 and https://github.com/braze-inc/braze-react-native-sdk/issues/29. Thanks @jimmy-devine and @sljuka.</li>
    </ul>
  </li>
</ul>

<h2 id="140">1.4.0</h2>

<h5 id="breaking-32">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#2310">Braze iOS SDK 2.31.0</a> or later.</li>
  <li>Updated the native Android bridge to <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#214">Braze Android SDK 2.1.4</a>.</li>
</ul>

<h5 id="added-50">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">ReactAppboy.registerPushToken()</code> for registering push tokens with Braze.
    <ul>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/pull/13. Thanks @dcvz!</li>
    </ul>
  </li>
  <li>Added the local <code class="language-plaintext highlighter-rouge">react-native-appboy-sdk</code> Podspec for integrating the React Native iOS bridge via Cocoapods.
    <ul>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/pull/15. Thanks @pietropizzi!</li>
    </ul>
  </li>
</ul>

<h2 id="130">1.3.0</h2>

<h5 id="breaking-33">Breaking</h5>
<ul>
  <li>Updates the native iOS bridge to use <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#2290">Braze iOS SDK 2.29.0</a>, which drops support for iOS 7.</li>
  <li>Updates the native Android bridge to use <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#200">Braze Android SDK 2.0.0</a>.</li>
</ul>

<h5 id="added-51">Added</h5>
<ul>
  <li>Adds <code class="language-plaintext highlighter-rouge">ReactAppboy.requestImmediateDataFlush()</code> for requesting an immediate flush of any data waiting to be sent to Braze’s servers.</li>
  <li>Adds <code class="language-plaintext highlighter-rouge">ReactAppboy.requestFeedRefresh()</code> for requesting a refresh of the News Feed.
    <ul>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/pull/12. Thanks @stief510!</li>
    </ul>
  </li>
  <li>Added the ability to pass an optional dictionary of News Feed launch options to <code class="language-plaintext highlighter-rouge">launchNewsFeed()</code>. See <code class="language-plaintext highlighter-rouge">NewsFeedLaunchOptions</code> for supported keys.
    <ul>
      <li>For more information on currently supported <code class="language-plaintext highlighter-rouge">NewsFeedLaunchOptions</code> keys, see the card width and card margin properties on <a href="http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_view_controller.html">ABKFeedViewController</a>.</li>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/pull/10. Thanks @mihalychk!</li>
    </ul>
  </li>
</ul>

<h2 id="120">1.2.0</h2>

<h5 id="breaking-34">Breaking</h5>
<ul>
  <li>Updates the native iOS bridge to be compatible with React Native <a href="https://github.com/facebook/react-native/releases/tag/v0.40.0">v0.40.0</a>.</li>
</ul>

<h5 id="changed-15">Changed</h5>
<ul>
  <li>Updates the AppboyProject sample project to React Native v0.41.1.</li>
</ul>

<h2 id="110">1.1.0</h2>

<h5 id="breaking-35">Breaking</h5>
<ul>
  <li><strong>Update Required</strong> — Fixes a bug in the <a href="https://github.com/braze-inc/braze-react-native-sdk/blob/master/iOS/BrazeReactBridge/BrazeReactBridge/BrazeReactBridge.mm">iOS bridge</a> where custom attribute dates were converted incorrectly, causing incorrect date data to be sent to Braze. As a result of the fix, <code class="language-plaintext highlighter-rouge">setDateCustomUserAttribute()</code> in the iOS React bridge may now only be called with a double.
    <ul>
      <li>Note: The default Javascript Braze interface has not changed, so for most integrations this just requires updating the SDK, unless you were manually calling our iOS bridge outside of our recommended integration.</li>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/issues/7</li>
    </ul>
  </li>
</ul>

<h2 id="100">1.0.0</h2>

<h5 id="breaking-36">Breaking</h5>
<ul>
  <li><strong>Update Required</strong> — Updates iOS push handling in the AppboyProject sample project to be compatible with iOS 10. For more information, refer to the CHANGELOG for <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#2240">Braze iOS SDK v2.24.0</a>.</li>
</ul>

<h5 id="added-52">Added</h5>
<ul>
  <li>Adds callbacks to the native bindings to provide function call results to React Native.</li>
  <li>Exposes <code class="language-plaintext highlighter-rouge">ReactAppboy.getCardCountForCategories()</code> and <code class="language-plaintext highlighter-rouge">ReactAppboy.getUnreadCardCountForCategories()</code> for retrieving News Feed card counts.
    <ul>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/issues/1</li>
    </ul>
  </li>
  <li>Adds <code class="language-plaintext highlighter-rouge">ReactAppboy.getInitialURL()</code> for handling deep links when an iOS application is launched from the suspended state by clicking on a push notification with a deep link. See <code class="language-plaintext highlighter-rouge">componentDidMount()</code> in <code class="language-plaintext highlighter-rouge">AppboyProject.js</code> for a sample implementation.</li>
  <li>Exposes <code class="language-plaintext highlighter-rouge">ReactAppboy.setTwitterData()</code> and <code class="language-plaintext highlighter-rouge">ReactAppboy.setFacebookData()</code> for Twitter and Facebook integration.
    <ul>
      <li>See https://github.com/braze-inc/braze-react-native-sdk/issues/4</li>
    </ul>
  </li>
</ul>

<h5 id="changed-16">Changed</h5>
<ul>
  <li>Targets <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1153">Braze Android SDK version 1.15.3</a> and <a href="https://github.com/braze-inc/braze-ios-sdk/blob/master/CHANGELOG.md#2242">Braze iOS SDK version 2.24.2</a>.</li>
  <li>Updates the AppboyProject sample application to React Native v0.33.0.</li>
  <li>Updates the AppboyProject sample project to integrate session handling and in-app message manager registration using an <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/BrazeActivityLifecycleCallbackListener.kt">AppboyLifecycleCallbackListener</a>, as introduced in Braze Android SDK v1.15.0.</li>
</ul>

<h5 id="removed">Removed</h5>
<ul>
  <li>Removes <code class="language-plaintext highlighter-rouge">AppboyBroadcastReceiver.java</code> from the AppboyProject sample project, as Braze Android SDK v1.15.0 removes the need for a custom <code class="language-plaintext highlighter-rouge">AppboyBroadcastReceiver</code> for Braze push notifications.</li>
</ul>

<h2 id="030">0.3.0</h2>

<h5 id="changed-17">Changed</h5>
<ul>
  <li>Renames Android module to conform to rnpm standard.</li>
</ul>

<h2 id="020">0.2.0</h2>

<h5 id="changed-18">Changed</h5>
<ul>
  <li>Refactors Android module to have the source directly under the <code class="language-plaintext highlighter-rouge">android</code> folder.</li>
</ul>

<h2 id="010">0.1.0</h2>
<ul>
  <li>Initial release.  Targets Braze Android SDK version 1.12.0 and Braze iOS SDK Version 1.18.4.</li>
</ul>




**Tip:**


You can also find a copy of the [Roku Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-roku-sdk/blob/master/CHANGELOG.md).



<h2 id="221">2.2.1</h2>

<h5 id="fixed">Fixed</h5>
<ul>
  <li>Fixed a crash when processing a failed HTTP request for templated in-app messages while the device has intermittent or no connectivity.</li>
</ul>

<h2 id="220">2.2.0</h2>

<h5 id="added">Added</h5>
<ul>
  <li>Added support for new Feature Flag property types by adding <code class="language-plaintext highlighter-rouge">getJSONProperty(key)</code>, <code class="language-plaintext highlighter-rouge">getImageProperty(key)</code>, and <code class="language-plaintext highlighter-rouge">getTimestampProperty(key)</code> to <code class="language-plaintext highlighter-rouge">FeatureFlag</code>.</li>
  <li>Added support for adding user alias with <code class="language-plaintext highlighter-rouge">m.Braze.addUserAlias(alias, label)</code></li>
  <li>Use <code class="language-plaintext highlighter-rouge">SetMessagePort()</code> instead of deprecated <code class="language-plaintext highlighter-rouge">SetPort()</code>. Thanks @chrisdp for pointing this out.</li>
</ul>

<h2 id="210">2.1.0</h2>

<h5 id="added-1">Added</h5>
<ul>
  <li>Added support for sending App Version information to Braze.</li>
</ul>

<h2 id="200">2.0.0</h2>

<h5 id="breaking">Breaking</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">getFeatureFlag</code> will return <code class="language-plaintext highlighter-rouge">invalid</code> when the flag does not exist.</li>
  <li><code class="language-plaintext highlighter-rouge">BrazeTask</code> now observes <code class="language-plaintext highlighter-rouge">BrazeFeatureFlagsUpdated</code> to know when Feature Flags refreshes succeed or fail. Data values may not always be different.
    <ul>
      <li>This will prevent you from being notified on the initial cache load. You can still observe <code class="language-plaintext highlighter-rouge">BrazeFeatureFlags</code> if you want to be notified of the cache load.</li>
    </ul>
  </li>
</ul>

<h2 id="101">1.0.1</h2>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Fixed warning that occurs when Feature Flags are not enabled.</li>
</ul>

<h2 id="100">1.0.0</h2>

<h5 id="added-2">Added</h5>
<ul>
  <li>Support for Feature Flags.
    <ul>
      <li>Get a single feature flag
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre>ff = m.braze.getFeatureFlag("theme")
if ff &lt;&gt; invalid and ff.enabled 
  bgcolor = ff.getStringProperty("bgcolor")
  ...
end if
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>Get all feature flags.
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>allFeatureFlags = m.braze.getAllFeatureFlags()
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>Be notified when Feature Flags are updated. Data values may not always be different.
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>m.BrazeTask.ObserveField("BrazeFeatureFlagsUpdated", "onFeatureFlagChanges")
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>Refresh feature flags.
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>m.braze.refreshFeatureFlags()
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>If you want to not cache feature flags, you can put the following in your <code class="language-plaintext highlighter-rouge">main.brs</code>.
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>config[config_fields.FF_CACHE_DISABLED] = true
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
</ul>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Fixed a circular reference between Braze and BrazeTask.</li>
</ul>

<h2 id="013">0.1.3</h2>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Fixed an issue where in-app messages might not filter properly on property criteria.</li>
  <li>Fixed an issue where very low opacity values would cause colors to have the wrong value.</li>
</ul>

<h5 id="added-3">Added</h5>
<ul>
  <li>Added a new sample app (TorchieTV) that more closely mimics the common Roku app.</li>
</ul>

<h2 id="012">0.1.2</h2>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Reduced the number of superfluous requests to Braze servers</li>
</ul>

<h2 id="011">0.1.1</h2>

<h5 id="added-4">Added</h5>
<ul>
  <li>Style data on buttons in In-App messages is now available. See <code class="language-plaintext highlighter-rouge">README.md</code> for more information.</li>
</ul>

<h5 id="changed">Changed</h5>
<ul>
  <li>Get In-App Message triggers at the start of session to match other SDKs.</li>
</ul>

<h5 id="fixed-5">Fixed</h5>
<ul>
  <li>Fixed issues with messages that re-evaluate campaign eligibility before displaying.</li>
  <li>Fixed issues with users in the control group.</li>
  <li>Fixed issue where new session wasn’t started when changing users.</li>
</ul>

<h2 id="010">0.1.0</h2>

<h5 id="️-known-issues">⚠️ Known Issues</h5>
<ul>
  <li>This release contains a known issue with in-app message syncing. Do not use this version and upgrade to 0.1.1+ instead.</li>
</ul>

<h5 id="added-5">Added</h5>
<ul>
  <li>Added support for receiving In-App Messaging model data.</li>
  <li>Added field <code class="language-plaintext highlighter-rouge">BrazeTask.BrazeInAppMessage</code> for In-App Messages.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">LogInAppMessageImpression</code>, <code class="language-plaintext highlighter-rouge">LogInAppMessageButtonClick</code>, and <code class="language-plaintext highlighter-rouge">LogInAppMessageClick</code> to <code class="language-plaintext highlighter-rouge">BrazeSDK</code>.</li>
</ul>

<h2 id="004">0.0.4</h2>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>Replaced the <code class="language-plaintext highlighter-rouge">GetModel</code> method with the more precise <code class="language-plaintext highlighter-rouge">GetModelDetails().ModelNumber</code>.</li>
</ul>

<h5 id="fixed-6">Fixed</h5>
<ul>
  <li>Replaced the deprecated <code class="language-plaintext highlighter-rouge">GetVersion</code> Roku API method with <code class="language-plaintext highlighter-rouge">GetOSVersion</code>.</li>
</ul>

<h2 id="003">0.0.3</h2>

<h5 id="fixed-7">Fixed</h5>
<ul>
  <li>Fixed the polarity on <code class="language-plaintext highlighter-rouge">ad_tracking_enabled</code> sent to Braze via device info.</li>
</ul>

<h2 id="002">0.0.2</h2>

<h5 id="fixed-8">Fixed</h5>
<ul>
  <li>Fixed an issue with device Id generation.</li>
</ul>

<h2 id="001">0.0.1</h2>

<h5 id="added-6">Added</h5>
<ul>
  <li>Initial release.</li>
  <li>Supports logging custom events, purchases, setting default and custom user attributes, session tracking, and user identity management.</li>
</ul>




**Tip:**


You can also find a copy of the [Unity Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md).



<p>⚠️ In version 4.0.0, we changed the iOS bridge from AppboyKit, which is written in Objective-C, to the new <a href="https://github.com/braze-inc/braze-swift-sdk">Swift SDK</a>. If you are upgrading from a version below 4.0.0 to a version above 4.0.0, please read <a href="https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#400">the instructions</a> to ensure a smooth transition and backward compatibility.</p>

<h2 id="1000">10.0.0</h2>

<h4 id="breaking">Breaking</h4>
<ul>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 12.0.0 to 13.2.0</a>.
    <ul>
      <li>This includes Xcode 26 support.</li>
    </ul>
  </li>
</ul>

<h2 id="900">9.0.0</h2>

<h4 id="breaking-1">Breaking</h4>
<ul>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 35.0.0 to 36.0.0</a>.</li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/11.9.0...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 11.9.0 to 12.0.0</a>.</li>
</ul>

<h2 id="800">8.0.0</h2>

<h5 id="breaking-2">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 10.3.0 to 11.9.0</a>.</li>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 32.1.0 to 35.0.0</a>.
    <ul>
      <li>The minimum required Android SDK version is 25. See more details <a href="https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information">here</a>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed">Fixed</h5>
<ul>
  <li>Fixed a crash on iOS due to the completion handler for silent / background push notification being executed multiple times when Unity was configured to process remote notifications in addition to the Braze plugin (<code class="language-plaintext highlighter-rouge">UNITY_USES_REMOTE_NOTIFICATIONS = 1</code>).</li>
  <li>Fixed the <em>Push Received Listener</em> getting mistakenly called when a push was opened on iOS. The <em>Push Opened Listener</em> is now properly called instead.</li>
</ul>

<h5 id="added">Added</h5>
<ul>
  <li>Updated the version of <code class="language-plaintext highlighter-rouge">SDWebImage</code> from 5.19.0 to <a href="https://github.com/SDWebImage/SDWebImage/releases/tag/5.19.7">5.19.7+</a> when automatically importing via “Braze Configuration”.</li>
</ul>

<h2 id="710">7.1.0</h2>

<h5 id="added-1">Added</h5>
<ul>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.1.0...10.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 10.1.0 to 10.3.0</a>.</li>
</ul>

<h2 id="700">7.0.0</h2>

<h5 id="breaking-3">Breaking</h5>
<ul>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 30.3.0 to 32.1.0</a>.</li>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 9.0.0 to 10.1.0</a>.</li>
</ul>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Fixed an issue on Android where the <code class="language-plaintext highlighter-rouge">AndroidPushReceivedTimestamp</code> of a <code class="language-plaintext highlighter-rouge">PushNotification</code> was incorrectly translated from a <code class="language-plaintext highlighter-rouge">long</code> to an <code class="language-plaintext highlighter-rouge">int</code>. The value received by the C# layer is now the same as the value sent in the JSON.</li>
</ul>

<h5 id="added-2">Added</h5>
<ul>
  <li>On the <code class="language-plaintext highlighter-rouge">FeatureFlag</code> object, added these APIs to get specific properties:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.GetTimestampProperty(string id)</code> for accessing Int Unix UTC millisecond timestamps as <code class="language-plaintext highlighter-rouge">long?</code>s.</li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.GetJSONProperty(string id)</code> for accessing JSON objects as <code class="language-plaintext highlighter-rouge">JSONObject?</code> types.</li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.GetImageProperty(string id)</code> for accessing image URLs as <code class="language-plaintext highlighter-rouge">string?</code>s.</li>
    </ul>
  </li>
  <li>Updated the following APIs to use Pascal case and deprecated the previous variant:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.GetStringProperty(string id)</code>, replacing <code class="language-plaintext highlighter-rouge">getStringProperty</code></li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.GetIntegerProperty(string id)</code>, replacing <code class="language-plaintext highlighter-rouge">getIntegerProperty</code></li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.GetDoubleProperty(string id)</code>, replacing <code class="language-plaintext highlighter-rouge">getDoubleProperty</code></li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.GetBooleanProperty(string id)</code>, replacing <code class="language-plaintext highlighter-rouge">getBooleanProperty</code></li>
    </ul>
  </li>
  <li>Added the method <code class="language-plaintext highlighter-rouge">AppboyBinding.SetUserLanguage(string)</code> for setting the language user attribute.</li>
  <li>Added the method <code class="language-plaintext highlighter-rouge">AppboyBinding.SetAdTrackingEnabled(bool adTrackingEnabled, string googleAdvertisingId)</code> to set the <code class="language-plaintext highlighter-rouge">adTrackingEnabled</code> flag on iOS and both the <code class="language-plaintext highlighter-rouge">adTrackingEnabled</code> flag and the <code class="language-plaintext highlighter-rouge">Google Advertising ID</code> on Android.</li>
  <li>Added support to modify the allow list for Braze tracking properties via the following C# properties and methods:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">TrackingProperty</code> class</li>
      <li><code class="language-plaintext highlighter-rouge">TrackingPropertyAllowList</code> class</li>
      <li><code class="language-plaintext highlighter-rouge">AppboyBinding.UpdateTrackingPropertyAllowList(TrackingPropertyAllowList)</code> to modify the allow list for Braze tracking properties.</li>
      <li>For details, refer to the <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest">Braze iOS Privacy Manifest documentation</a>.</li>
    </ul>
  </li>
  <li>Added the <code class="language-plaintext highlighter-rouge">InAppMessage.IsTestSend</code> property to indicate whether an in-app message was sent as a test send.</li>
  <li>Added the method <code class="language-plaintext highlighter-rouge">AppboyBinding.HideCurrentInAppMessage()</code> to hide the visible in-app message, if applicable.</li>
</ul>

<h2 id="600">6.0.0</h2>

<h5 id="breaking-4">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.7.0 to 9.0.0</a>.</li>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 29.0.1 to 30.3.0</a>.</li>
</ul>

<h5 id="added-3">Added</h5>
<ul>
  <li>Added iOS <em>In App Message Manager Initial Display Operation</em> configuration setting.
    <ul>
      <li>This setting allows you to configure the initial display operation for in-app messages on iOS. For instance, set it to <em>Display Later</em> to delay the initial display of in-app messages until after your game has finished loading, and use the <code class="language-plaintext highlighter-rouge">AppboyBinding.DisplayNextInAppMessage()</code> method to display it when ready.</li>
    </ul>
  </li>
  <li>Added the <em>Entitlements File Path</em> configuration setting.
    <ul>
      <li>This setting allows you to specify the path to an entitlements file to be used / modified by Braze in the Xcode project.</li>
      <li>If left blank, the default entitlements file will be used / created.</li>
    </ul>
  </li>
</ul>

<h2 id="521">5.2.1</h2>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Fixed an issue with calling <code class="language-plaintext highlighter-rouge">LogInAppMessageClicked()</code>, <code class="language-plaintext highlighter-rouge">LogInAppMessageImpression()</code>, <code class="language-plaintext highlighter-rouge">LogInAppMessageButtonClicked</code>, and <code class="language-plaintext highlighter-rouge">LogContentCardDismissed(card)</code> on Android.</li>
</ul>

<h2 id="520">5.2.0</h2>

<h5 id="added-4">Added</h5>
<ul>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.4.0...7.7.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 7.4.0 to 7.7.0</a>.</li>
  <li>Updated the version of <code class="language-plaintext highlighter-rouge">SDWebImage</code> from 5.15.5 to <a href="https://github.com/SDWebImage/SDWebImage/releases/tag/5.19.0">5.19.0</a> when automatically importing via “Braze Configuration”.
    <ul>
      <li>This version of <code class="language-plaintext highlighter-rouge">SDWebImage</code> contains a Privacy Manifest file. See <a href="https://developer.apple.com/documentation/bundleresources/privacy_manifest_files">Apple’s documentation</a> for more information.</li>
    </ul>
  </li>
</ul>

<h2 id="510">5.1.0</h2>

<h5 id="added-5">Added</h5>
<ul>
  <li>Added support for custom user attributes to be nested objects.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">AppboyBinding.SetCustomUserAttribute(string, Dictionary&lt;string, object&gt;);</code></li>
      <li><code class="language-plaintext highlighter-rouge">AppboyBinding.SetCustomUserAttribute(string, List&lt;Dictionary&lt;string, object&gt;&gt;);</code></li>
      <li>You can specify that the Dictionary be merged with the existing value.
        <ul>
          <li><code class="language-plaintext highlighter-rouge">AppboyBinding.SetCustomUserAttribute(string, Dictionary&lt;string, object&gt;, bool merge);</code></li>
        </ul>
      </li>
      <li>See https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/ for more information.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.LogFeatureFlagImpression(string id)</code> to log a Feature Flag impression.</li>
</ul>

<h2 id="500">5.0.0</h2>

<h4 id="breaking-5">Breaking</h4>
<ul>
  <li>Updated the native iOS bridge <a href="https://github.com/braze-inc/braze-swift-sdk/compare/6.1.0...7.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Swift SDK 6.1.0 to 7.4.0</a>.
    <ul>
      <li>The iOS repository link now points to the prebuilt dynamic XCFrameworks from this repo: <code class="language-plaintext highlighter-rouge">https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic</code>.</li>
    </ul>
  </li>
  <li>Updated the native Android bridge <a href="https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">from Braze Android SDK 27.0.1 to 29.0.1</a>.</li>
  <li><code class="language-plaintext highlighter-rouge">AppboyBinding.GetFeatureFlag(string id)</code> will now return <code class="language-plaintext highlighter-rouge">null</code> if the Feature Flag does not exist.</li>
  <li><code class="language-plaintext highlighter-rouge">FEATURE_FLAGS_UPDATED</code> will only trigger when a refresh request completes with success or failure, and upon initial subscription if there was previously cached data from the current session.</li>
</ul>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in <code class="language-plaintext highlighter-rouge">4.0.0</code> which prevented compilation on Xcode 14.3+.
    <ul>
      <li>The additional <code class="language-plaintext highlighter-rouge">-fcxx-modules</code> flag under “Other C++ Flags” has been removed from the build process.</li>
      <li>The dependencies <code class="language-plaintext highlighter-rouge">BrazeKit</code> and <code class="language-plaintext highlighter-rouge">BrazeUI</code> now get directly linked to the main app’s target, instead of being transitively linked via <code class="language-plaintext highlighter-rouge">UnityFramework</code>.</li>
    </ul>
  </li>
  <li>Changed the iOS plugin to automatically update up to the next minor version, instead of up to the next major version.</li>
</ul>

<h2 id="430">4.3.0</h2>

<blockquote>
  <p>Starting with this release, this SDK will use <a href="https://semver.org/">Semantic Versioning</a>.</p>
</blockquote>

<h5 id="added-6">Added</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701">Braze Android SDK 27.0.1</a>.</li>
</ul>

<h2 id="420">4.2.0</h2>

<h4 id="breaking-6">Breaking</h4>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2620">Braze Android SDK 26.2.0</a>.</li>
</ul>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Fixed an issue on Android where In-App Message events would not properly get forwarded to the Unity layer.</li>
</ul>

<h2 id="411">4.1.1</h2>

<h5 id="fixed-5">Fixed</h5>
<ul>
  <li>Fixed the Braze iOS Push settings not being applied in the sample app code.</li>
</ul>

<h2 id="410">4.1.0</h2>

<h5 id="added-7">Added</h5>
<ul>
  <li>Added support for Feature Flags.
    <ul>
      <li><code class="language-plaintext highlighter-rouge">AppboyBinding.GetFeatureFlag(string id)</code> - Get a single Feature Flag.</li>
      <li><code class="language-plaintext highlighter-rouge">AppboyBinding.GetAllFeatureFlags()</code> - Get all Feature Flags.</li>
      <li><code class="language-plaintext highlighter-rouge">AppboyBinding.RefreshFeatureFlags()</code> - Request a refresh of Feature Flags.</li>
    </ul>
  </li>
  <li>Adds the ability to subscribe to Feature Flag updates.
    <ul>
      <li>Set the values for <code class="language-plaintext highlighter-rouge">Game Object Name</code> and <code class="language-plaintext highlighter-rouge">Callback Method Name</code> under “Braze Configuration” &gt; “Feature Flags” to the corresponding values in your application.</li>
    </ul>
  </li>
  <li>On <code class="language-plaintext highlighter-rouge">FeatureFlag</code> object, adds these APIs to get specific properties:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.getStringProperty(string id)</code></li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.getIntegerProperty(string id)</code></li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.getDoubleProperty(string id)</code></li>
      <li><code class="language-plaintext highlighter-rouge">featureFlag.getBooleanProperty(string id)</code></li>
    </ul>
  </li>
  <li>Updated the iOS plugin to use the <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#610">Braze Swift SDK 6.1.0</a>.</li>
</ul>

<h2 id="400">4.0.0</h2>

<h4 id="breaking-7">Breaking</h4>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2500">Braze Android SDK 25.0.0</a>
    <ul>
      <li>Update <code class="language-plaintext highlighter-rouge">com.appboy.unity.AppboyUnityPlayerActivity</code> references to <code class="language-plaintext highlighter-rouge">com.braze.unity.BrazeUnityPlayerActivity</code>.</li>
    </ul>
  </li>
  <li>Updates the native iOS bridge to use the new <a href="https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#600">Swift SDK version 6.0.0</a>.
    <ul>
      <li>Replace any instances of <code class="language-plaintext highlighter-rouge">#import &lt;Appboy_iOS_SDK/AppboyKit.h&gt;</code> in your iOS native code with:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>@import BrazeKit;
@import BrazeUI; // Only needed if you use the UI in the file
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>Replace the prefix <code class="language-plaintext highlighter-rouge">ABK</code> with <code class="language-plaintext highlighter-rouge">BRZ</code> for any of the constants found in <a href="https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/iOS/AppboyUnityManager.h">AppboyUnityManager.h</a>.</li>
      <li>Update your <code class="language-plaintext highlighter-rouge">AppDelegate</code> file with the code snippet below. Reference our <a href="https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/iOS/AppboyAppDelegate.mm">sample code here</a>.
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>BRZConfiguration *config = [[BRZConfiguration alloc] init];
Braze *braze = [AppboyUnityManager initBraze:config];
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>This migration requires re-identifying users. To do so, you must call the <code class="language-plaintext highlighter-rouge">changeUser</code> method on the Braze instance for non-anonymous users. You can read more about it <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/#Re-identify-users">here</a>.</li>
      <li>Reference <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide">this Migration Guide</a> and <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit">this documentation</a> for additional context around specific migration / integration steps.</li>
    </ul>
  </li>
  <li>Requires Unity version <a href="https://unity.com/releases/editor/whats-new/2020.3.42">2020.3.42</a> or newer.</li>
  <li>The following changes have been made to <code class="language-plaintext highlighter-rouge">AppboyUnityManager.h</code>:
    <ul>
      <li>Renames <code class="language-plaintext highlighter-rouge">addInAppMessageListenerWithObjectNameAndSetDelegate:callbackMethodName:</code> to <code class="language-plaintext highlighter-rouge">addInAppMessageListenerWithObjectName:callbackMethodName:</code>.</li>
      <li>Renames <code class="language-plaintext highlighter-rouge">ABKUnityMessageType</code> to <code class="language-plaintext highlighter-rouge">BRZUnityMessageType</code>.</li>
      <li>Removes <code class="language-plaintext highlighter-rouge">parsePlist</code> since it is implemented as a part of <code class="language-plaintext highlighter-rouge">initBraze:</code>.</li>
    </ul>
  </li>
  <li>Removes <code class="language-plaintext highlighter-rouge">setFacebookData</code> and <code class="language-plaintext highlighter-rouge">setTwitterData</code> from <code class="language-plaintext highlighter-rouge">AppboyBinding.cs</code>.</li>
  <li>Removes the release asset <code class="language-plaintext highlighter-rouge">Appboy-nodeps.unitypackage</code> in favor of using the “Braze Configuration” option mentioned below.</li>
</ul>

<h5 id="added-8">Added</h5>
<ul>
  <li>Adds a configuration option under “Braze Configuration” which allows you to toggle between importing <code class="language-plaintext highlighter-rouge">SDWebImage</code> into your iOS application.
    <ul>
      <li>If checked, the build process will automatically add <a href="https://github.com/SDWebImage/SDWebImage/releases/tag/5.15.5">SDWebImage version 5.15.5</a> to your project. If unchecked, it will be omitted.</li>
    </ul>
  </li>
</ul>

<h2 id="3110">3.11.0</h2>

<h5 id="breaking-8">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use Braze Android SDK 23.3.0.</li>
  <li>Streamlined the integration required for handling push notifications on Android.
    <ul>
      <li>References to <code class="language-plaintext highlighter-rouge">AppboyUnityPushBroadcastReceiver</code> must be removed from your <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code> file.</li>
      <li>Removed <code class="language-plaintext highlighter-rouge">binding.FlushAndroidPendingPushIntents()</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="3100">3.10.0</h2>

<h5 id="fixed-6">Fixed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyBinding.LogContentCardsDisplayed()</code>.</li>
</ul>

<h2 id="390">3.9.0</h2>

<h5 id="breaking-9">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use Braze Android SDK 23.1.0.</li>
  <li>Added the ability to request push notification permissions on Android 13+ devices via <code class="language-plaintext highlighter-rouge">Appboy.AppboyBinding.PromptUserForPushPermissions(false)</code>.
    <ul>
      <li>Either <code class="language-plaintext highlighter-rouge">true</code> or <code class="language-plaintext highlighter-rouge">false</code> result in the push prompt being shown, on Android. The parameter is unused.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-7">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">AppboyBinding.logPurchase()</code> calls could fail on Android based on the device locale.</li>
</ul>

<h2 id="381">3.8.1</h2>

<h5 id="added-9">Added</h5>
<ul>
  <li>Added Assembly Definitions for the SDK.
    <ul>
      <li>See <a href="https://docs.unity3d.com/Manual/ScriptCompilationAssemblyDefinitionFiles.html">the Unity Asm Def docs</a> for more information.</li>
      <li>Special thanks to @starikcetin!</li>
    </ul>
  </li>
</ul>

<h2 id="380">3.8.0</h2>

<h5 id="breaking-10">Breaking</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyBinding.SetUserAvatarImageURL()</code> from the binding.</li>
  <li><code class="language-plaintext highlighter-rouge">Utilities/MiniJson.cs</code> now uses <code class="language-plaintext highlighter-rouge">InvariantCulture</code> during serialization.</li>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2100">Braze Android SDK 21.0.0</a>
    <ul>
      <li>This SDK version relies on <code class="language-plaintext highlighter-rouge">implementation "androidx.recyclerview:recyclerview:1.2.1</code> or higher.</li>
    </ul>
  </li>
</ul>

<h5 id="added-10">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.SetUserLastKnownLocation()</code> to manually set the last known location for the user.</li>
  <li>Added SDK Authentication Support.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.SetSdkAuthenticationSignature(sdkAuthSignature)</code> to set the signature only.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.ChangeUser(userId, sdkAuthSignature = null)</code> to optionally set the SDK Authentication signature when changing users.</li>
      <li>Added SDK Authentication under “Braze Configuration”. There are separate configurations for iOS and Android. If you want to configure at runtime, use:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">AppboyBinding.IOSSdkAuthenticationFailureGameObjectName</code>, <code class="language-plaintext highlighter-rouge">AppboyBinding.IOSSdkAuthenticationEnabled</code>, and <code class="language-plaintext highlighter-rouge">AppboyBinding.IOSSdkAuthenticationFailureCallbackMethodName</code> for iOS.</li>
          <li><code class="language-plaintext highlighter-rouge">AppboyBinding.AndroidSdkAuthenticationEnabled</code>, <code class="language-plaintext highlighter-rouge">AppboyBinding.AndroidSdkAuthenticationFailureGameObjectName</code>, and <code class="language-plaintext highlighter-rouge">AppboyBinding.AndroidSdkAuthenticationFailureCallbackMethodName</code> for Android.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h5 id="changed">Changed</h5>
<ul>
  <li>Updated the iOS plugin to use Braze iOS SDK 4.4.3.</li>
</ul>

<h2 id="371">3.7.1</h2>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>Updated the Android plugin to use Braze Android SDK 18.0.1.</li>
</ul>

<h2 id="370">3.7.0</h2>

<h5 id="breaking-11">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use Braze Android SDK 18.0.0.
    <ul>
      <li>This SDK version requires a dependency on Kotlin coroutines. This can be added to your <code class="language-plaintext highlighter-rouge">mainTemplate.gradle</code> file via <code class="language-plaintext highlighter-rouge">implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.5.2"</code></li>
    </ul>
  </li>
</ul>

<h5 id="fixed-8">Fixed</h5>
<ul>
  <li>Fixed an issue where <code class="language-plaintext highlighter-rouge">AppboyUnityPlayerActivity</code> could not be extended on Android.</li>
</ul>

<h2 id="360">3.6.0</h2>

<h5 id="breaking-12">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use Braze Android SDK 16.0.0.
    <ul>
      <li>This SDK version requires a dependency on Kotlin. This can be added to your <code class="language-plaintext highlighter-rouge">mainTemplate.gradle</code> file via <code class="language-plaintext highlighter-rouge">implementation "org.jetbrains.kotlin:kotlin-stdlib:1.5.21"</code></li>
      <li>This SDK version has removed a dependency on the <code class="language-plaintext highlighter-rouge">appcompat</code> library.</li>
    </ul>
  </li>
</ul>

<h5 id="added-11">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.AddToSubscriptionGroup()</code> and <code class="language-plaintext highlighter-rouge">AppboyBinding.RemoveFromSubscriptionGroup()</code> to the binding.</li>
  <li>Added the <code class="language-plaintext highlighter-rouge">DisplayNextInAppMessage()</code> method, available on both iOS and Android.</li>
  <li>Added the ability to receive in-app messages UI events via <code class="language-plaintext highlighter-rouge">AppboyBinding.inAppMessageListener</code>. See <code class="language-plaintext highlighter-rouge">BrazeInAppMessageListener</code> for more information.</li>
</ul>

<h5 id="changed-2">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.3">Braze iOS SDK 4.3.3</a>.</li>
  <li>Removed the iOS specific method <code class="language-plaintext highlighter-rouge">DisplayNextInAppMessage(bool withDelegate)</code>.</li>
</ul>

<h2 id="351">3.5.1</h2>

<h5 id="fixed-9">Fixed</h5>
<ul>
  <li>Fixed an issue where simulator architectures were included in the iOS framework.</li>
</ul>

<h2 id="350">3.5.0</h2>

<h5 id="breaking-13">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use Braze Android SDK 15.0.0.</li>
</ul>

<h5 id="changed-3">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2">Braze iOS SDK 4.3.2</a>.</li>
</ul>

<h2 id="340">3.4.0</h2>

<h5 id="added-12">Added</h5>
<ul>
  <li>Added the ability to change the display flow of In-App Messages directly from Unity code via <code class="language-plaintext highlighter-rouge">AppboyBinding.SetInAppMessageDisplayAction()</code>.
    <ul>
      <li>See the <code class="language-plaintext highlighter-rouge">BrazeUnityInAppMessageDisplayActionType</code> enum.</li>
    </ul>
  </li>
  <li>Added the ability to open the default Content Cards UI via <code class="language-plaintext highlighter-rouge">DisplayContentCards()</code> on the binding.
    <ul>
      <li>For Android, this requires the following dependencies:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>implementation "androidx.swiperefreshlayout:swiperefreshlayout:+"
implementation "androidx.recyclerview:recyclerview:+"
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
</ul>

<h2 id="330">3.3.0</h2>

<h5 id="breaking-14">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use Braze Android SDK 14.0.0.</li>
</ul>

<h5 id="added-13">Added</h5>
<ul>
  <li>Added the ability to delay sending Android push notification data to the Unity layer until the native libraries have finished loading and any AppboyBinding method has been called.
    <ul>
      <li>Configured under “Braze Configuration -&gt; Automate Unity Android Integration -&gt; Push Configuration -&gt; Delay Sending Push Notification Intents”.</li>
      <li>Pending Android push notification intents are flushed automatically after the first call to any method on the Android binding is made.</li>
      <li>To optionally have finer control over when these push notification intents are flushed, call the following from Unity:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>#if UNITY_ANDROID
BrazeAndroidPlatform binding = (BrazeAndroidPlatform) Appboy.AppboyBinding.mBinding;
binding.FlushAndroidPendingPushIntents();
#endif
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
</ul>

<h2 id="320">3.2.0</h2>

<h5 id="breaking-15">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use Braze Android SDK 14.0.0.1.</li>
</ul>

<h5 id="fixed-10">Fixed</h5>
<ul>
  <li>Fixed an issue introduced in 3.1.0 on Android where push opens could fail to launch the application on certain devices.</li>
  <li>Fixed an issue introduced in 3.0.0 in the iOS binding where <code class="language-plaintext highlighter-rouge">enableSDK()</code> and <code class="language-plaintext highlighter-rouge">disableSDK()</code> had swapped behaviors.</li>
</ul>

<h2 id="310">3.1.0</h2>

<p><strong>Important:</strong> This release has known issues with push notifications on Android. This is fixed in version 3.2.0.</p>

<h5 id="changed-4">Changed</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1312">Braze Android SDK 13.1.2</a>.</li>
</ul>

<h2 id="300">3.0.0</h2>

<h5 id="important">Important</h5>
<ul>
  <li>This release contains several minor changes to our iOS push code. Most integrations will be unaffected, however, we recommend additional testing.</li>
</ul>

<h5 id="breaking-16">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1300">Braze Android SDK 13.0.0</a>.</li>
  <li>If automatic iOS push integration is enabled, Braze will now automatically add the Xcode Push Capability in <code class="language-plaintext highlighter-rouge">OnPostprocessBuild()</code>.
    <ul>
      <li>To disable this, check “Disable Automatic Push Capability” in the Braze configuration editor.</li>
    </ul>
  </li>
  <li>In <code class="language-plaintext highlighter-rouge">AppboyUnityManager.mm</code>:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">registerForRemoteNotifications:</code> has been replaced with <code class="language-plaintext highlighter-rouge">registerForRemoteNotificationsWithProvisional:(BOOL)provisional</code>. If using this method, note that the new method calls Apple’s APIs directly and does not respect Braze configuration’s settings for automatic push integration and registration.</li>
      <li><code class="language-plaintext highlighter-rouge">registerApplication:didReceiveRemoteNotification:fetchCompletionHandler:</code> and <code class="language-plaintext highlighter-rouge">registerPushToken</code> have also been updated to no longer internally read Braze config.</li>
      <li>Several obsolete methods were removed, including methods where the manager trivially wrapped the native <code class="language-plaintext highlighter-rouge">Appboy</code> instance.</li>
      <li>Most integrations will not be affected by these changes.</li>
    </ul>
  </li>
</ul>

<h5 id="added-14">Added</h5>
<ul>
  <li>Added the option to disable iOS provisional push authorization when automatic iOS push integration is enabled.
    <ul>
      <li>To use, check “Disable Provisional Authorization” in the Braze configuration editor.</li>
      <li>When provisional push authorization is disabled, users will see the native push prompt dialog at app startup.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.ConfigureListener()</code> as an alternative method for configuring GameObject listeners for push, in-app messages, Content Cards, and News Feed. Use the new <code class="language-plaintext highlighter-rouge">BrazeUnityMessageType</code> enum to specify the desired message type.
    <ul>
      <li>On iOS, to receive push opened and received callbacks, <code class="language-plaintext highlighter-rouge">Integrate Push With Braze</code> must be enabled.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.PromptUserForPushPermissions(bool provisional)</code> to request authorization and register for push notifications on iOS.
    <ul>
      <li>Set <code class="language-plaintext highlighter-rouge">provisional</code> to <code class="language-plaintext highlighter-rouge">true</code> to request provisional authorization, or <code class="language-plaintext highlighter-rouge">false</code> to show the push prompt directly.</li>
      <li>If you would like to read the user response, pass an instance of <code class="language-plaintext highlighter-rouge">PushPromptResponseReceived</code> into the method.</li>
      <li>We recommend using this method with the following settings:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">Integrate Push With Braze</code> enabled.</li>
          <li><code class="language-plaintext highlighter-rouge">Disable Automatic Push Registration</code> enabled.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.SetPushTokenReceivedFromSystemDelegate()</code> to receive push tokens Braze receives from the OS (iOS only).</li>
</ul>

<h5 id="fixed-11">Fixed</h5>
<ul>
  <li>Braze push delegates are no longer called automatically in fully manual integrations.
    <ul>
      <li>Automatic push integration must be enabled for Braze push delegates to function.</li>
    </ul>
  </li>
</ul>

<h2 id="280">2.8.0</h2>

<h5 id="breaking-17">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1200">Braze Android SDK 12.0.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.31.2">Braze iOS SDK 3.31.2</a>.</li>
</ul>

<h5 id="added-15">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.AddAlias()</code> to the binding.</li>
</ul>

<h2 id="271">2.7.1</h2>

<h5 id="fixed-12">Fixed</h5>
<ul>
  <li>Fixed an issue where the return type for the Android implementation of <code class="language-plaintext highlighter-rouge">setIsDismissed</code> in <code class="language-plaintext highlighter-rouge">AppboyBinding</code> was incorrectly set to <code class="language-plaintext highlighter-rouge">bool</code>.</li>
  <li>Removed a deprecated usage of <code class="language-plaintext highlighter-rouge">PBXProject.GetUnityTargetName()</code>.</li>
</ul>

<h2 id="270">2.7.0</h2>

<h5 id="breaking-18">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.29.1">Braze iOS SDK 3.29.1</a>.</li>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1100">Braze Android SDK 11.0.0</a>.</li>
</ul>

<h5 id="fixed-13">Fixed</h5>
<ul>
  <li>Fixed a metadata issue for Android artifacts.</li>
</ul>

<h2 id="260">2.6.0</h2>

<h5 id="breaking-19">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1000">Braze Android SDK 10.0.0</a>.
    <ul>
      <li>Note that this SDK release internally uses AndroidX depdendences. See the linked SDK changelog entry for more information.</li>
      <li>All “jetified” packages are removed since the android artifacts are now fully on AndroidX.</li>
    </ul>
  </li>
  <li>Removed <code class="language-plaintext highlighter-rouge">PushNotification.cs#CollapseKey</code>.</li>
</ul>

<h5 id="changed-5">Changed</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">PushNotification.cs#RawJsonString</code>, <code class="language-plaintext highlighter-rouge">PushNotification.cs#AndroidPushReceivedTimestamp</code>.</li>
</ul>

<h5 id="added-16">Added</h5>
<ul>
  <li>Added Braze configuration option for Android to toggle automatically displaying In-App Messages.</li>
</ul>

<h5 id="fixed-14">Fixed</h5>
<ul>
  <li>Fixed push notification parsing for Android in <code class="language-plaintext highlighter-rouge">PushNotification.cs</code>.</li>
  <li>Fixed use of outdated <code class="language-plaintext highlighter-rouge">UNITY_IPHONE</code> directive in <code class="language-plaintext highlighter-rouge">Card.cs</code>.</li>
</ul>

<h2 id="250">2.5.0</h2>

<h5 id="breaking-20">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3270">Braze iOS SDK 3.27.0</a>. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.</li>
</ul>

<h2 id="240">2.4.0</h2>

<h5 id="changed-6">Changed</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#810">Braze Android SDK 8.1.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.26.1">Braze iOS SDK 3.26.1</a>.</li>
</ul>

<h5 id="fixed-15">Fixed</h5>
<ul>
  <li>Fixed return type of <code class="language-plaintext highlighter-rouge">AppboyBinding.RegisterAppboyPushMessages()</code> for iOS to be <code class="language-plaintext highlighter-rouge">void</code>.</li>
  <li>Fixed the automatic config for Android push icons to correctly used <code class="language-plaintext highlighter-rouge">drawable</code> instead of <code class="language-plaintext highlighter-rouge">string</code>.</li>
</ul>

<h2 id="230">2.3.0</h2>

<h5 id="changed-7">Changed</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#801">Braze Android SDK 8.0.1</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.25.0">Braze iOS SDK 3.25.0</a>.</li>
</ul>

<h5 id="added-17">Added</h5>
<ul>
  <li>Added functionality to apps using the UserNotification framework to forward via <code class="language-plaintext highlighter-rouge">UnitySendMessage</code> push notification opens to game object methods on iOS.</li>
</ul>

<h2 id="222">2.2.2</h2>

<h5 id="added-18">Added</h5>
<ul>
  <li>Added a method for manually providing a push registration token via <code class="language-plaintext highlighter-rouge">AppboyBinding.RegisterAppboyPushMessages()</code> for iOS.
    <ul>
      <li>Note that the Android implementation accepts <code class="language-plaintext highlighter-rouge">string</code>.</li>
      <li>The iOS implementation accepts <code class="language-plaintext highlighter-rouge">byte[]</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed-16">Fixed</h5>
<ul>
  <li>Fixed an issue which caused the extras dictionary to not be populated in JSON push payloads sent by the SDK to Unity listeners.</li>
</ul>

<h2 id="221">2.2.1</h2>

<h5 id="added-19">Added</h5>
<ul>
  <li>Added an implementation for <code class="language-plaintext highlighter-rouge">AppboyBinding.GetInstallTrackingId()</code> for iOS.</li>
</ul>

<h5 id="changed-8">Changed</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#700">Braze Android SDK 7.0.0</a>.</li>
</ul>

<h2 id="210">2.1.0</h2>

<h5 id="-breaking">⚠ Breaking</h5>
<ul>
  <li>Removes the unused <code class="language-plaintext highlighter-rouge">CrossPromotionSmall.cs</code> News Feed model.</li>
</ul>

<h5 id="added-20">Added</h5>
<ul>
  <li>Added the ability to automatically integrate Unity builds on Android in the ‘Braze Configuration’ window. Using this option obviates the need for a manually created <code class="language-plaintext highlighter-rouge">appboy.xml</code> file to configure Android apps.
    <ul>
      <li>If enabled, an autogenerated config file will be generated at <code class="language-plaintext highlighter-rouge">/unity-android-resources/res/values/appboy-generated.xml</code> in your temp gradle out directory. If disabled, this auto-generated file will be deleted.</li>
      <li>If already using an <code class="language-plaintext highlighter-rouge">appboy.xml</code> file, the values from that configuration should be transferred in order to prevent build resource XML conflicts.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.LogContentCardDismissed()</code> to log a Content Card dismissal.</li>
  <li>Added Other, Unknown, Not Applicable, and Prefer not to Say options for user gender.</li>
  <li>Added the ability to set the endpoint for iOS via the automatic config window <code class="language-plaintext highlighter-rouge">Braze Configuration</code>.</li>
  <li>Added support for <code class="language-plaintext highlighter-rouge">UserNotifications</code> Framework on iOS for push.</li>
</ul>

<h5 id="changed-9">Changed</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#600">Braze Android SDK 6.0.0</a>.</li>
  <li>Removed root level <code class="language-plaintext highlighter-rouge">Libraries</code> folder. Now, iOS frameworks exclusively exist under <code class="language-plaintext highlighter-rouge">Assets/Plugins/iOS/</code>.</li>
</ul>

<h2 id="200">2.0.0</h2>

<h5 id="-breaking-1">⚠ Breaking</h5>
<ul>
  <li>The structure of the Android plugin (i.e. found under <code class="language-plaintext highlighter-rouge">Assets/Plugins/Android/</code>) has been changed to only include AAR artifacts. All other folders have been removed.
    <ul>
      <li>Additionally, depending on the <code class="language-plaintext highlighter-rouge">.unitypackage</code> chosen, you can import jetified Braze AAR artifacts. These artifacts were transformed using the <a href="https://developer.android.com/studio/command-line/jetifier"><code class="language-plaintext highlighter-rouge">jetifier</code></a> tool to be compatible with <code class="language-plaintext highlighter-rouge">androidX</code> support libraries instead of the <code class="language-plaintext highlighter-rouge">v4</code> support libraries. This is particularly relevant if you wish to update your <a href="https://firebase.google.com/docs/unity/setup"><code class="language-plaintext highlighter-rouge">unity firebase messaging</code></a> dependencies to the latest versions, which use and require <code class="language-plaintext highlighter-rouge">androidX</code> support libraries. Please see our documentation for more information.</li>
    </ul>
  </li>
</ul>

<h5 id="added-21">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.RequestImmediateDataFlush()</code> to immediately request a data flush.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">AppboyBinding.RequestGeofences(latitude, longitude)</code> to manually request Braze Geofences.</li>
  <li>Adds an option to disable automatic geofence requests on session start. Note that this is required in order to manually request geofences.
    <ul>
      <li>iOS - You can do this in the plist by adding the Appboy dictionary to your Info.plist file. Inside the Appboy dictionary, add the <code class="language-plaintext highlighter-rouge">DisableAutomaticGeofenceRequests</code> boolean subentry and set the value to <code class="language-plaintext highlighter-rouge">YES</code>.</li>
      <li>Android - You can do this by configuring the boolean value for <code class="language-plaintext highlighter-rouge">com_appboy_automatic_geofence_requests_enabled</code> to <code class="language-plaintext highlighter-rouge">false</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code>.</li>
    </ul>
  </li>
</ul>

<h5 id="changed-10">Changed</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#500">Braze Android SDK 5.0.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.21.3">Braze iOS SDK 3.21.3</a>.</li>
</ul>

<h2 id="1220">1.22.0</h2>

<h5 id="added-22">Added</h5>
<ul>
  <li>Added the ability to receive Content Cards data within a Unity Game Object or method in C#.
    <ul>
      <li>On Android, set <code class="language-plaintext highlighter-rouge">com_appboy_content_cards_updated_listener_game_object_name</code> and <code class="language-plaintext highlighter-rouge">com_appboy_content_cards_updated_listener_callback_method_name</code> in your <code class="language-plaintext highlighter-rouge">appboy.xml</code> to set your Game Object and Callback Method for receiving Content Cards updates.</li>
      <li>On iOS, set <code class="language-plaintext highlighter-rouge">ContentCardsCallbackMethodName</code> and <code class="language-plaintext highlighter-rouge">ContentCardsGameObjectName</code> inside of a dictionary named <code class="language-plaintext highlighter-rouge">Unity</code> set inside a dictionary named <code class="language-plaintext highlighter-rouge">Appboy</code> within your <code class="language-plaintext highlighter-rouge">Info.plist</code>. Alternatively, use the configuration UI under the <code class="language-plaintext highlighter-rouge">Braze</code> menu added when integrating the Braze Unity package.</li>
      <li>Our <a href="https://github.com/Appboy/appboy-unity-sdk/blob/master/Assets/Plugins/Appboy/Tests/AppboyBindingTester.cs">Callback example class</a> contains an example of parsing the received Content Cards json as well as using our provided convenience model class, <code class="language-plaintext highlighter-rouge">ContentCard.cs</code> to wrap the data and log analytics. Currently, <code class="language-plaintext highlighter-rouge">ContentCard.cs</code> supports logging clicks and impressions.</li>
    </ul>
  </li>
</ul>

<h2 id="1212">1.21.2</h2>

<p><strong>Important:</strong> This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md">Braze iOS SDK Changelog</a> for more information.</p>

<h5 id="changed-11">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.2">Braze iOS SDK 3.20.2</a>.</li>
</ul>

<h2 id="1211">1.21.1</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.21.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.21.2 or above if you make use of HTML in-app messages.</p>

<h5 id="changed-12">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.1">Braze iOS SDK 3.20.1</a>.</li>
</ul>

<h2 id="1210">1.21.0</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.21.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.21.2 or above if you make use of HTML in-app messages.</p>

<h5 id="breaking-21">Breaking</h5>
<ul>
  <li>Updated the iOS plugin to use <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.0">Braze iOS SDK 3.20.0</a>.</li>
  <li><strong>Important:</strong> Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to these methods as soon as possible to ensure a smooth transition as devices upgrade to iOS 13. In <code class="language-plaintext highlighter-rouge">application:didRegisterForRemoteNotificationsWithDeviceToken:</code>, replace
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>[[Appboy sharedInstance] registerPushToken:
              [NSString stringWithFormat:@"%@", deviceToken]];
</pre></td></tr></tbody></table></code></pre></div>    </div>
    <p>with</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>[[Appboy sharedInstance] registerDeviceToken:deviceToken]];
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#370">Braze Android SDK 3.7.0</a>.</li>
  <li>Note: This Braze Unity SDK release updates to a Braze Android SDK dependency which no longer enables automatic Braze location collection by default. Please consult the changelogs for information on how to continue to enable automatic Braze location collection, as well as further information on breaking changes.</li>
  <li>Removes the Feedback feature and all associated methods, classes, and interfaces.</li>
</ul>

<h2 id="1200">1.20.0</h2>

<h5 id="breaking-22">Breaking</h5>
<ul>
  <li>Updated the iOS plugin to use <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.18.0">Braze iOS SDK 3.18.0</a>.</li>
  <li>Note: This Braze Unity SDK release updates to a Braze iOS SDK dependency which no longer enables automatic Braze location collection by default. Please consult the changelogs for information on how to continue to enable automatic Braze location collection, as well as further information on breaking changes.</li>
</ul>

<h5 id="added-23">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">RequestLocationInitialization</code> to the Appboy interface for requesting Braze geofences and a single location update.</li>
</ul>

<h2 id="1190">1.19.0</h2>

<h5 id="breaking-23">Breaking</h5>
<ul>
  <li>Updated the iOS plugin to use <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.16.0">Braze iOS SDK 3.16.0</a>.</li>
</ul>

<h2 id="1180">1.18.0</h2>

<h5 id="breaking-24">Breaking</h5>
<ul>
  <li>Updated the iOS plugin to use <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.14.0">Braze iOS SDK 3.14.0</a>.</li>
</ul>

<h2 id="1170">1.17.0</h2>

<h5 id="breaking-25">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#321">Braze Android SDK 3.2.1</a>.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to directly use the Firebase messaging event <code class="language-plaintext highlighter-rouge">com.google.firebase.MESSAGING_EVENT</code>. This is now the recommended way to integrate Firebase push with Braze. The <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> should be removed from your <code class="language-plaintext highlighter-rouge">AndroidManifest</code> and replaced with the following:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre>&lt;service android:name="com.appboy.AppboyFirebaseMessagingService"&gt;
  &lt;intent-filter&gt;
    &lt;action android:name="com.google.firebase.MESSAGING_EVENT" /&gt;
  &lt;/intent-filter&gt;
&lt;/service&gt;
</pre></td></tr></tbody></table></code></pre></div>        </div>
        <ul>
          <li>Also note that any <code class="language-plaintext highlighter-rouge">c2dm</code> related permissions should be removed from your manifest as Braze does not require any extra permissions for <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to work correctly.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h2 id="1160">1.16.0</h2>

<h5 id="breaking-26">Breaking</h5>
<ul>
  <li>Updated the iOS plugin to use <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.11.0">Braze iOS SDK 3.11.0</a>.</li>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#310">Braze Android SDK 3.1.0</a>.</li>
</ul>

<h5 id="fixed-17">Fixed</h5>
<ul>
  <li>Fixed an issue where the binding would cache the Appboy singleton instance.</li>
  <li>Fixed <code class="language-plaintext highlighter-rouge">Card.cs</code> to always return <code class="language-plaintext highlighter-rouge">CardCategory.NO_CATEGORY</code> in all cases where no valid categories are found.
    <ul>
      <li>See https://github.com/Appboy/appboy-unity-sdk/pull/43. Thanks @Sencerd!</li>
    </ul>
  </li>
</ul>

<h5 id="changed-13">Changed</h5>
<ul>
  <li>Updated the Appboy configuration editor to use Braze branding.</li>
  <li>By default, native in-app messages on Android no longer show the status bar.</li>
</ul>

<h2 id="1150">1.15.0</h2>

<h5 id="breaking-27">Breaking</h5>
<ul>
  <li>Updated the Android plugin to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#270">Braze Android SDK 2.7.0</a>.
    <ul>
      <li><strong>Important:</strong> Note that in Braze Android SDK 2.7.0, <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code> was renamed to <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code>. This receiver is intended to be used for Firebase integrations. Please update the <code class="language-plaintext highlighter-rouge">AppboyGcmReceiver</code> declaration in your <code class="language-plaintext highlighter-rouge">AndroidManifest.xml</code> to reference <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> and remove the <code class="language-plaintext highlighter-rouge">com.google.android.c2dm.intent.REGISTRATION</code> intent filter action.</li>
    </ul>
  </li>
</ul>

<h5 id="added-24">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">SetAttributionData</code> to the Appboy interface.</li>
</ul>

<h2 id="1140">1.14.0</h2>

<h5 id="breaking-28">Breaking</h5>
<ul>
  <li>Updated the iOS plugin to use Braze iOS SDK 3.7.1.
    <ul>
      <li>Updated the iOS plugin to use the Braze iOS SDK framework instead of local files.</li>
      <li>As a result, imports using local file syntax (e.g. <code class="language-plaintext highlighter-rouge">"AppboyKit.h"</code>) must change to framework (e.g.<code class="language-plaintext highlighter-rouge">&lt;Appboy_iOS_SDK/AppboyKit.h&gt;</code>) syntax.</li>
    </ul>
  </li>
  <li>Updates the Android plugin to use Braze Android SDK 2.6.0.</li>
  <li>Removes Android Support Library artifacts from the Braze Unity Plugin. This is to avoid duplicating the Android Support Library artifacts that are automatically included as part of the Firebase Unity SDK, our recommended push integration. Integrators not using Firebase or importing Android Support Library artifacts through another SDK must include the Android Support Library manually (v4 only).</li>
</ul>

<h5 id="fixed-18">Fixed</h5>
<ul>
  <li>Fixed an issue that required manual import of non-xib Braze iOS SDK resources into Unity-generated Xcode projects.</li>
</ul>

<h5 id="added-25">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">GetInstallTrackingId</code> to the Appboy interface. This method is currently only implemented on Android and is a no-op on iOS.</li>
  <li>Updated the Unity Samples sample app to use FCM instead of GCM.</li>
</ul>

<h5 id="changed-14">Changed</h5>
<ul>
  <li>In-app message analytics events on the Appboy interface no longer require using an Appboy Unity player subclass.
    <ul>
      <li>See https://github.com/Appboy/appboy-unity-sdk/pull/38/files. Thanks @MartinGonzalez!</li>
    </ul>
  </li>
</ul>

<h5 id="removed">Removed</h5>
<ul>
  <li>Removes <code class="language-plaintext highlighter-rouge">showStreamView:</code> from the <code class="language-plaintext highlighter-rouge">AppboyUnityManager.h</code> interface.</li>
</ul>

<h2 id="1130">1.13.0</h2>

<h5 id="breaking-29">Breaking</h5>
<ul>
  <li>Updates the iOS plugin to use Braze iOS SDK 3.4.0.</li>
  <li>Updates the Android plugin to use Braze Android SDK 2.3.0.</li>
  <li>Removes Windows support.</li>
  <li>Removes <code class="language-plaintext highlighter-rouge">LogSlideupImpression</code> and <code class="language-plaintext highlighter-rouge">LogSlideupClicked</code> from the Appboy interface.</li>
</ul>

<h5 id="added-26">Added</h5>
<ul>
  <li><code class="language-plaintext highlighter-rouge">PostBuild.cs</code> now adds SDWebImage and FLAnimatedImage to XCode embedded binaries automatically.
    <ul>
      <li>See https://github.com/Appboy/appboy-unity-sdk/pull/35. Thanks @nlattessi!</li>
    </ul>
  </li>
  <li><code class="language-plaintext highlighter-rouge">PostBuild.cs</code> may now run in Unity environments without Unity iOS Build Support.
    <ul>
      <li>See https://github.com/Appboy/appboy-unity-sdk/pull/36. Thanks @Sencerd!</li>
    </ul>
  </li>
  <li>Added support for wiping all customer data created by the Braze SDK via <code class="language-plaintext highlighter-rouge">Appboy.AppboyBinding.wipeData()</code>.
    <ul>
      <li>Note that on iOS, <code class="language-plaintext highlighter-rouge">wipeData()</code> will disable the SDK for the remainder of the app run. For more information, see our iOS SDK’s documentation for <a href="http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733"><code class="language-plaintext highlighter-rouge">disableSDK</code></a>.</li>
    </ul>
  </li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.AppboyBinding.disableSDK()</code> to disable the Braze SDK immediately.</li>
  <li>Added <code class="language-plaintext highlighter-rouge">Appboy.AppboyBinding.enableSDK()</code> to re-enable the SDK after a call to <code class="language-plaintext highlighter-rouge">Appboy.AppboyBinding.disableSDK()</code>.
    <ul>
      <li>Note that on iOS, <code class="language-plaintext highlighter-rouge">enableSDK()</code> will not enable the SDK immediately. For more information, see our iOS SDK’s documentation for <a href="http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b"><code class="language-plaintext highlighter-rouge">requestEnableSDKOnNextAppRun</code></a>.</li>
    </ul>
  </li>
</ul>

<h2 id="1120">1.12.0</h2>

<h5 id="breaking-30">Breaking</h5>
<ul>
  <li>Updates the iOS plugin to use Braze iOS SDK 3.3.1.</li>
  <li>Updates the Android plugin to use Braze Android SDK 2.2.2.</li>
  <li>Removes methods <code class="language-plaintext highlighter-rouge">RequestInAppMessage</code> and <code class="language-plaintext highlighter-rouge">RequestSlideup</code> as they are removed in the Braze native SDKs.</li>
</ul>

<h2 id="1110">1.11.0</h2>

<h5 id="breaking-31">Breaking</h5>
<ul>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.29.0, which drops support for iOS 7.</li>
  <li>Updates the Android plugin to use Braze Android SDK 2.0.0.</li>
  <li>Removes methods <code class="language-plaintext highlighter-rouge">SetUserIsSubscribedToEmails</code> and <code class="language-plaintext highlighter-rouge">SetUserBio</code> as they are removed in the Braze native SDKs.</li>
</ul>

<h2 id="1100">1.10.0</h2>

<h5 id="breaking-32">Breaking</h5>
<ul>
  <li>Updates the Android plugin to use Braze Android SDK 1.18.0.</li>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.25.0.</li>
</ul>

<h5 id="added-27">Added</h5>
<ul>
  <li>Adds a new method <code class="language-plaintext highlighter-rouge">DisplayNextInAppMessage(bool withDelegate)</code> in iOS plugin to display next in-app message from the in-app message stack, if there is one.
    <ul>
      <li>When the withDelegate is false, the in-app message will be displayed in Braze’s default UI. Otherwise, it will follow the normal in-app message displaying path by going through the <code class="language-plaintext highlighter-rouge">- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp</code> in <code class="language-plaintext highlighter-rouge">AppboyUnityManager.m</code>.</li>
    </ul>
  </li>
  <li>Updates the SDK to be compatible with Unity 5.5+.</li>
</ul>

<h2 id="190">1.9.0</h2>

<h5 id="breaking-33">Breaking</h5>
<ul>
  <li>Updates the SDK to require XCode 8.</li>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.24.0, which supports iOS 10 and has the new in-app message V2 feature. The new in-app message V2 feature includes new in-app message UI change, event property trigger and templated in-app message.</li>
  <li>Updates the Android plugin to use Braze Android SDK 1.15.0 with the new triggered in-app message feature.</li>
</ul>

<h2 id="182">1.8.2</h2>

<h5 id="added-28">Added</h5>
<ul>
  <li>Updates the SDK to be compatible with Unity 5.4+.  In 5.4.0 Unity stopped implementing push delegates in UnityAppController in certain conditions, causing a crash when the Braze SDK tried to call them.</li>
</ul>

<h2 id="181">1.8.1</h2>

<h5 id="fixed-19">Fixed</h5>
<ul>
  <li>Updates SDK to modify delegate usage to fix an issue with push-click handling introduced in iOS 10 - see https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md for details.</li>
</ul>

<h2 id="180">1.8.0</h2>

<h5 id="breaking-34">Breaking</h5>
<ul>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.21.0, which drops support for iOS 6.</li>
  <li>Updates the Android plugin to use Braze Android SDK 1.13.5.</li>
  <li>Drops support for Windows Phone 8.</li>
</ul>

<h5 id="added-29">Added</h5>
<ul>
  <li>Adds support for passing triggered in-app messages to Unity.</li>
  <li>Bundles the Android and iOS plugins, along with Braze’s native Unity functionality, as a Unity package.</li>
  <li>Adds a native Unity solution for automating the iOS SDK integration.</li>
  <li>Adds object handling for custom event and purchase properties.</li>
  <li>Exposes the extras on the News Feed Card model in Unity.</li>
  <li>Updates the Unity sample project to Unity v.5.3.5.</li>
</ul>

<h2 id="170">1.7.0</h2>

<h5 id="breaking-35">Breaking</h5>
<ul>
  <li>Updates the Android plugin to use Braze Android SDK 1.13.2.</li>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.19.1.</li>
</ul>

<h5 id="added-30">Added</h5>
<ul>
  <li>Adds binding methods for setting user’s Facebook and Twitter data (Android/iOS).</li>
  <li>Adds binding method to set the GCM registrationId (Android).</li>
  <li>Adds overloads to the binding methods for <code class="language-plaintext highlighter-rouge">logCustomEvent</code> and <code class="language-plaintext highlighter-rouge">logPurchase</code> that include properties (Android/iOS).</li>
</ul>

<h2 id="160">1.6.0</h2>

<h5 id="breaking-36">Breaking</h5>
<ul>
  <li>Updates the Android plugin to use Braze Android SDK 1.11.0.</li>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.17.0.</li>
</ul>

<h2 id="150">1.5.0</h2>

<h5 id="breaking-37">Breaking</h5>
<ul>
  <li>Removes Unity 4 support. Unity 5 or higher is required to use this and future versions of the Braze Unity SDK. Unity 4 users may integrate Braze Unity SDK release 1.4.0, which includes analytics and push functionality but does not include native in-app messages on Android; however, upgrading to Unity 5 and using the latest Braze Unity SDK is recommended.</li>
  <li>Removes Froyo support, which was dropped in Unity 4.3. See https://unity3d.com/unity/whats-new/unity-4.3.</li>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.12.1.</li>
  <li>Updates the Android plugin to use Braze Android SDK 1.8.0.</li>
</ul>

<h5 id="added-31">Added</h5>
<ul>
  <li>Adds native Braze ui capability to Android, including in-app messages, the News Feed, and Braze’s webview. Note: As a result of this change, in-app messages will display automatically with native Braze layouts.  To disable this functionality, set com_appboy_inapp_show_inapp_messages_automatically to false in your Unity project’s appboy.xml file.</li>
</ul>

<h2 id="140">1.4.0</h2>

<h5 id="breaking-38">Breaking</h5>
<ul>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.11.2.</li>
  <li>Updates the Android plugin to use Braze Android SDK 1.7.2.</li>
</ul>

<h5 id="added-32">Added</h5>
<ul>
  <li>Adds a sample Unity application that uses the Braze plugin.</li>
  <li>Adds new in-app message models for the Modal and Full screen types added in Android 1.7 and iOS 2.11.</li>
</ul>

<h2 id="131">1.3.1</h2>

<h5 id="breaking-39">Breaking</h5>
<ul>
  <li>Updates the Android plugin to use Braze Android SDK 1.6.1.</li>
</ul>

<h2 id="130">1.3.0</h2>

<h5 id="breaking-40">Breaking</h5>
<ul>
  <li>Updates the Android plugin to use Braze Android SDK 1.6.0.</li>
  <li>Updates the iOS plugin to use Braze iOS SDK 2.9.3.</li>
</ul>

<h5 id="added-33">Added</h5>
<ul>
  <li>Adds plugins for Windows Phone 8 and Windows Universal apps.</li>
</ul>

<h5 id="fixed-20">Fixed</h5>
<ul>
  <li>Fixes the corrupted support-v4 jar in the Android plugin.</li>
</ul>

<h2 id="122">1.2.2</h2>

<h5 id="breaking-41">Breaking</h5>
<ul>
  <li>Updates the Android plugin to use Braze Android SDK 1.5.2.</li>
</ul>

<h5 id="added-34">Added</h5>
<ul>
  <li>Adds logFeedDisplayed, logFeedbackDisplayed, SetUserAvatarImageURL, IncrementCustomUserAttribute; updates email and push notification subscription types to current options supported in the Android and iOS SDKs (OPTED_IN, SUBSCRIBED, or UNSUBSCRIBED).</li>
</ul>

<h2 id="121">1.2.1</h2>

<h5 id="breaking-42">Breaking</h5>
<ul>
  <li>Updates the plugin libraries to Braze Android SDK 1.5.1 and Braze iOS SDK 2.9.1 (without Facebook iOS SDK Support).</li>
</ul>

<h5 id="added-35">Added</h5>
<ul>
  <li>Adds quantity parameter as an option when logging purchase. The quantity should be an unsigned interger greater than 0 and no larger than 100.</li>
  <li>New Custom Attribute Data Type (Array): Braze now supports custom attributes which contain an array of string elements. In addition, we also provide methods for adding or removing an string element from an array type custom attribute.</li>
</ul>

<h2 id="12">1.2</h2>

<h5 id="breaking-43">Breaking</h5>
<ul>
  <li>Updates the plugin libraries to Braze Android SDK 1.4.3 and Braze iOS SDK 2.8 (without Facebook iOS SDK Support).</li>
</ul>

<h5 id="added-36">Added</h5>
<ul>
  <li>Adds SlideFrom, ClickAction, DismissType and Uri to Slideup; added logging slideup impressions and clicks.</li>
  <li>Exposes the card models from Braze to Unity; adds methods for requesting feed from Braze server or cache; adds logging impressions and clicks.</li>
</ul>

<h5 id="changed-15">Changed</h5>
<ul>
  <li>In Android SDK, changes the device identifier from the device persistent ANDROID_ID to a non device persistent identifier for compliance with the new Google Play Terms of Service.</li>
</ul>

<h2 id="11">1.1</h2>

<h5 id="breaking-44">Breaking</h5>
<ul>
  <li>Updates the plugin libraries to Braze Android SDK 1.2.1 and Braze iOS SDK 2.3.1 (without Facebook iOS SDK Support).</li>
</ul>

<h5 id="added-37">Added</h5>
<ul>
  <li>Adds Prime31 plugin compatibility.</li>
</ul>

<h2 id="10">1.0</h2>

<h5 id="added-38">Added</h5>
<ul>
  <li>Initial release</li>
</ul>




**Tip:**


You can also find a copy of the [.NET MAUI Braze SDK changelog on GitHub](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md).



<h2 id="900">9.0.0</h2>

<h5 id="breaking">Breaking</h5>
<ul>
  <li>Updated the Android binding from <a href="https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Android SDK 37.0.0 to 41.0.0</a>.</li>
  <li>Updated the iOS binding from <a href="https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Swift SDK 13.3.0 to 14.0.1</a>.</li>
  <li>Added new transitive NuGet dependencies required by the Braze Android SDK:
    <ul>
      <li><code class="language-plaintext highlighter-rouge">Xamarin.AndroidX.DataStore.Preferences</code> (1.1.7.1)</li>
      <li><code class="language-plaintext highlighter-rouge">Xamarin.KotlinX.Serialization.Json.Jvm</code> (1.9.0.2)</li>
      <li><code class="language-plaintext highlighter-rouge">Xamarin.Kotlin.StdLib</code> has been updated from 2.0.21.3 to 2.3.0.1. If your project explicitly pins this package to an older version, you will need to update it to avoid restore errors.</li>
    </ul>
  </li>
  <li>Removed the News Feed feature.
    <ul>
      <li>This feature was removed from the native Android SDK in version <a href="https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0"><code class="language-plaintext highlighter-rouge">38.0.0</code></a>.</li>
      <li>This feature was removed from the native Swift SDK in version <a href="https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0"><code class="language-plaintext highlighter-rouge">14.0.0</code></a>.</li>
    </ul>
  </li>
  <li>The <code class="language-plaintext highlighter-rouge">BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData</code> enum case has been renamed to <code class="language-plaintext highlighter-rouge">BRZInAppMessageDismissalReason.WipeData</code>.</li>
</ul>

<h5 id="added">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazePlatform.BrazeAndroidLocationBinding</code>, which introduces support for location services and geofences on Android.
    <ul>
      <li>This package is available <a href="https://www.nuget.org/packages/BrazePlatform.BrazeAndroidLocationBinding/">here on Nuget</a>.</li>
    </ul>
  </li>
</ul>

<h2 id="800">8.0.0</h2>

<h5 id="breaking-1">Breaking</h5>
<ul>
  <li>Updated the iOS binding from <a href="https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Swift SDK 12.1.0 to 13.3.0</a>.
    <ul>
      <li>This includes Xcode 26 support.</li>
    </ul>
  </li>
</ul>

<h2 id="700">7.0.0</h2>

<h5 id="breaking-2">Breaking</h5>
<ul>
  <li>Added support for .NET 9.0 for the iOS and Android bindings.
    <ul>
      <li>This removes support for .NET 8.0.</li>
      <li>This requires a <a href="https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0">minimum version of iOS 12.2</a>.</li>
    </ul>
  </li>
  <li>Updated the Android binding from <a href="https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Android 32.0.0 to 37.0.0</a>.</li>
  <li>Updated the iOS binding from <a href="https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Swift SDK 10.0.0 to 12.1.0</a>.</li>
</ul>

<blockquote>
  <p><strong><em>NOTE:</em></strong>  This release contains APIs for the Banners feature but is not currently fully supported by this SDK. If you wish to use Banners in your .NET MAUI app, please contact your Customer Support Manager before integrating into your application.</p>
</blockquote>

<h2 id="600">6.0.0</h2>

<h5 id="breaking-3">Breaking</h5>
<ul>
  <li>Added support for .NET 8.0 for the iOS and Android bindings as .NET 7.0 has reached end of life support.
    <ul>
      <li>This removes support for .NET 7.0.</li>
    </ul>
  </li>
  <li>Updated the Android binding from <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Android 30.4.0 to 32.0.0</a>.</li>
  <li>Updated the iOS binding from <a href="https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Swift SDK 9.0.0 to 10.0.0</a>.
    <ul>
      <li>When subscribing to push notification events, the subscription will be triggered on iOS for both “Push Received” and “Push Opened”, instead of only for “Push Opened” events.</li>
    </ul>
  </li>
</ul>

<h5 id="fixed">Fixed</h5>
<ul>
  <li>Removed the files under the <code class="language-plaintext highlighter-rouge">Modules</code> directories in the XCFrameworks to reduce the final size of the distributed application.</li>
</ul>

<h2 id="500">5.0.0</h2>

<h5 id="breaking-4">Breaking</h5>
<ul>
  <li>Updated the iOS binding from <a href="https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Swift SDK 8.4.0 to 9.0.0</a>.</li>
</ul>

<h2 id="403">4.0.3</h2>

<h5 id="added-1">Added</h5>
<ul>
  <li>Updated the Android binding from <a href="https://github.com/braze-inc/braze-android-sdk/compare/v30.1.0...v30.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Android 30.1.0 to 30.4.0</a>.</li>
  <li>Updated the iOS binding from <a href="https://github.com/braze-inc/braze-swift-sdk/compare/8.0.1...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Swift SDK 8.0.1 to 8.4.0</a>.</li>
</ul>

<h2 id="402">4.0.2</h2>

<h5 id="added-2">Added</h5>
<ul>
  <li>Updated the Android binding from <a href="https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Android SDK 29.0.1 to 30.1.0</a>.</li>
  <li>Updated the iOS binding from <a href="https://github.com/braze-inc/braze-swift-sdk/compare/7.6.0...8.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Swift SDK 7.6.0 to 8.0.1</a>.</li>
</ul>

<h2 id="401">4.0.1</h2>

<h5 id="fixed-1">Fixed</h5>
<ul>
  <li>Corrected the incorrect dependency versions in the nuspecs of recent iOS libraries.</li>
</ul>

<h2 id="400">4.0.0</h2>

<h5 id="breaking-5">Breaking</h5>
<ul>
  <li>This version updates the iOS binding to use the <a href="https://github.com/braze-inc/braze-swift-sdk/">Braze Swift SDK</a>. Most iOS public APIs have changed, please refer to our <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide">migration guide</a> (Swift) for guidance about replacement to use. We provide compatibility bindings to keep making use of the old public APIs.
    <ul>
      <li>The iOS binding is now composed of multiple modules:
        <ul>
          <li><strong>BrazeKit</strong>: Main SDK library providing support for analytics and push notifications (nuget: <a href="https://www.nuget.org/packages/Braze.iOS.BrazeKit">Braze.iOS.BrazeKit</a>).</li>
          <li><strong>BrazeUI</strong>: Braze-provided user interface library for In-App Messages and Content Cards (nuget: <a href="https://www.nuget.org/packages/Braze.iOS.BrazeUI">Braze.iOS.BrazeUI</a>).</li>
          <li><strong>BrazeLocation</strong>: Location library providing support for location analytics and geofence monitoring (nuget: <a href="https://www.nuget.org/packages/Braze.iOS.BrazeLocation">Braze.iOS.BrazeLocation</a>).</li>
          <li><strong>BrazeKitCompat</strong>: Compatibility library with support for pre-4.0.0 APIs (nuget: <a href="https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat">Braze.iOS.BrazeKitCompat</a>).</li>
          <li><strong>BrazeUICompat</strong>: Compatibility library with support for pre-4.0.0 UI APIs (nuget: <a href="https://www.nuget.org/packages/Braze.iOS.BrazeUICompat">Braze.iOS.BrazeUICompat</a>).</li>
        </ul>
      </li>
      <li>This migration requires re-identifying users. To do so, you must call the <code class="language-plaintext highlighter-rouge">changeUser</code> method on the Braze instance for non-anonymous users. You can read more about it <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/#Re-identify-users">here</a>.</li>
      <li>Refer to the <em>BrazeiOSMauiSampleApp</em> for the new integration, and to <em>BrazeiOSMauiCompatSampleApp</em> for usage of the compatibility modules.</li>
    </ul>
  </li>
  <li>Updated the iOS binding to the <a href="https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0">Braze Swift SDK 7.6.0</a></li>
  <li>The iOS binding requires using .NET 7 for compatibility with Xcode 15.</li>
</ul>

<h2 id="300">3.0.0</h2>

<h5 id="breaking-6">Breaking</h5>
<ul>
  <li>The NuGet package has been renamed from <code class="language-plaintext highlighter-rouge">AppboyPlatformXamariniOSBinding</code> to <a href="https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/"><code class="language-plaintext highlighter-rouge">BrazePlatform.BrazeiOSBinding</code></a>.
    <ul>
      <li>To use the updated package, replace any instances of <code class="language-plaintext highlighter-rouge">using AppboyPlatformXamariniOSBinding;</code> with:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>using Braze;
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
    </ul>
  </li>
  <li>This version requires using .NET 6+ and removes support for projects using the Xamarin framework. See <a href="https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin">Microsoft’s policy</a> around the end of support for Xamarin.</li>
  <li>Updated the Android binding from <a href="https://github.com/braze-inc/braze-android-sdk/compare/v26.3.1...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze Android SDK 26.3.2 to 29.0.1</a>.</li>
</ul>

<h5 id="fixed-2">Fixed</h5>
<ul>
  <li>Fixed an issue where some Android <code class="language-plaintext highlighter-rouge">set</code> methods were being hidden by the Xamarin framework.</li>
</ul>

<h5 id="added-3">Added</h5>
<ul>
  <li>Added support for .NET 6 (or newer) and support for projects using <a href="https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui?view=net-maui-8.0">.NET MAUI</a>.
    <ul>
      <li>For a reference iOS implementation, see <code class="language-plaintext highlighter-rouge">BrazeiOSMauiSampleApp.sln</code>.</li>
    </ul>
  </li>
  <li>Updated the iOS binding from <a href="https://github.com/Appboy/appboy-ios-sdk/compare/4.4.1...4.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed">Braze iOS SDK 4.4.1 to 4.6.0</a>.
    <ul>
      <li>The underlying iOS assets have been updated to use XCFrameworks:
        <ul>
          <li><code class="language-plaintext highlighter-rouge">Appboy_iOS_SDK.framework</code> -&gt; <code class="language-plaintext highlighter-rouge">Appboy_iOS_SDK.xcframework</code></li>
          <li><code class="language-plaintext highlighter-rouge">SDWebImage.framework</code> -&gt; <code class="language-plaintext highlighter-rouge">SDWebImage.xcframework</code></li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h2 id="201">2.0.1</h2>

<h5 id="fixed-3">Fixed</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2632">Braze Android SDK 26.3.2</a>.</li>
</ul>

<h2 id="200">2.0.0</h2>

<blockquote>
  <p>Starting with this release, this SDK will use <a href="https://semver.org/">Semantic Versioning</a>.</p>
</blockquote>

<h5 id="breaking-7">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2630">Braze Android SDK 26.3.0</a>.</li>
</ul>

<h2 id="1270">1.27.0</h2>

<h5 id="added-4">Added</h5>
<ul>
  <li>Added <code class="language-plaintext highlighter-rouge">BrazePlatform.BrazeAndroidBinding</code> which introduces .NET 6+ framework support for MAUI.
    <ul>
      <li>This package is available <a href="https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/">here on Nuget</a>.</li>
    </ul>
  </li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2420">Braze Android SDK 24.2.0</a>.</li>
</ul>

<h2 id="1260">1.26.0</h2>

<h5 id="breaking-8">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2330">Braze Android SDK 23.3.0</a>.</li>
</ul>

<h2 id="1250">1.25.0</h2>

<h5 id="breaking-9">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2100">Braze Android SDK 21.0.0</a>.</li>
</ul>

<h2 id="1240">1.24.0</h2>

<h5 id="breaking-10">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1900">Braze Android SDK 19.0.0</a>.</li>
</ul>

<h2 id="1230">1.23.0</h2>

<h5 id="breaking-11">Breaking</h5>
<ul>
  <li>Updated the iOS binding to use <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#441">Braze iOS SDK 4.4.1</a>.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">AddToSubscriptionGroupWithGroupId</code> and <code class="language-plaintext highlighter-rouge">RemoveFromSubscriptionGroupWithGroupId</code> to <code class="language-plaintext highlighter-rouge">ABKUser</code>.</li>
    </ul>
  </li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1801">Braze Android SDK 18.0.1</a>.
    <ul>
      <li>This introduces a hard dependency on <code class="language-plaintext highlighter-rouge">Xamarin.Kotlin.StdLib</code> in your package references.</li>
      <li>This introduces a hard dependency on <code class="language-plaintext highlighter-rouge">Xamarin.KotlinX.Coroutines.Android</code> in your package references.</li>
    </ul>
  </li>
</ul>

<h2 id="1211">1.21.1</h2>

<h5 id="changed">Changed</h5>
<ul>
  <li>Updated the iOS binding to use <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#432">Braze iOS SDK 4.3.2</a>.</li>
</ul>

<h2 id="1210">1.21.0</h2>

<h5 id="breaking-12">Breaking</h5>
<ul>
  <li>Updated the iOS binding to use <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#431">Braze iOS SDK 4.3.1</a>.
    <ul>
      <li>This includes several breaking changes in the binding, and integrators should test before releasing. Please read the Braze iOS SDK changelog for details.</li>
    </ul>
  </li>
</ul>

<h2 id="1200">1.20.0</h2>

<h5 id="breaking-13">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1500">Braze Android SDK 15.0.0</a>.</li>
</ul>

<h2 id="1190">1.19.0</h2>

<h5 id="changed-1">Changed</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1312">Braze Android SDK 13.1.2</a>.</li>
</ul>

<h2 id="1180">1.18.0</h2>

<h5 id="breaking-14">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1300">Braze Android SDK 13.0.0</a>.</li>
  <li>Updated the iOS binding to use <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3331">Braze iOS SDK 3.33.1</a>.</li>
</ul>

<h2 id="1170">1.17.0</h2>

<h5 id="breaking-15">Breaking</h5>
<ul>
  <li>Updated the iOS binding to use <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3291">Braze iOS SDK 3.29.1</a>.</li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1100">Braze Android SDK 11.0.0</a>.</li>
</ul>

<h2 id="1160">1.16.0</h2>

<h5 id="breaking-16">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1000">Braze Android SDK 10.0.0</a>.</li>
</ul>

<h2 id="1150">1.15.0</h2>

<h5 id="breaking-17">Breaking</h5>
<ul>
  <li>The native iOS bridge uses <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3270">Braze iOS SDK 3.27.0</a>. This release adds support for iOS 14 and requires XCode 12. Please read the Braze iOS SDK changelog for details.</li>
  <li><code class="language-plaintext highlighter-rouge">ABKIDFADelegate.IsAdvertisingTrackingEnabled</code> has been renamed to <code class="language-plaintext highlighter-rouge">ABKIDFADelegate.IsAdvertisingTrackingEnabledOrATTAuthorized</code>.</li>
  <li>The class <code class="language-plaintext highlighter-rouge">ABKIdentifierForAdvertisingProvider</code> has been removed.</li>
</ul>

<h2 id="1140">1.14.0</h2>

<h5 id="breaking-18">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.26.1">Braze iOS SDK 3.26.1</a>.</li>
</ul>

<h2 id="1130">1.13.0</h2>

<h5 id="breaking-19">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#810">Braze Android SDK 8.1.0</a>.</li>
</ul>

<h2 id="1120">1.12.0</h2>

<h5 id="breaking-20">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#801">Braze Android SDK 8.0.1</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.24.2">Braze iOS SDK 3.24.2</a>.
    <ul>
      <li>Flipped <code class="language-plaintext highlighter-rouge">ABKLocationManager.DisableLocationTracking</code> to <code class="language-plaintext highlighter-rouge">ABKLocationManager.EnableLocationTracking</code>.</li>
      <li>Replaced <code class="language-plaintext highlighter-rouge">ABKInAppMessageWindowController.supportedOrientationMasks</code> with <code class="language-plaintext highlighter-rouge">ABKInAppMessageWindowController.supportedOrientationMask</code>.</li>
    </ul>
  </li>
</ul>

<h2 id="1110">1.11.0</h2>

<h5 id="breaking-21">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#600">Braze Android SDK 6.0.0</a>.</li>
  <li>Changed the Android binding to target Android 10.</li>
</ul>

<h2 id="1102">1.10.2</h2>

<p><strong>Important:</strong> This patch updates the Braze iOS SDK Dependency from 3.20.1 to 3.20.2, which contains important bugfixes. Integrators should upgrade to this patch version. Please see the <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md">Braze iOS SDK Changelog</a> for more information.</p>

<h5 id="changed-2">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.2">Braze iOS SDK 3.20.2</a>.</li>
</ul>

<h2 id="1101">1.10.1</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.10.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.10.2 or above if you make use of HTML in-app messages.</p>

<h5 id="changed-3">Changed</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.1">Braze iOS SDK 3.20.1</a>.</li>
</ul>

<h2 id="1100">1.10.0</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.10.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.10.2 or above if you make use of HTML in-app messages.</p>

<h5 id="breaking-22">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.20.0">Braze iOS SDK 3.20.0</a>.</li>
  <li><strong>Important:</strong> Braze iOS SDK 3.20.0 contains updated push token registration methods. We recommend upgrading to these methods as soon as possible to ensure a smooth transition as devices upgrade to iOS 13. In <code class="language-plaintext highlighter-rouge">application.RegisteredForRemoteNotifications:</code>, replace
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>Appboy.SharedInstance?.RegisterPushToken(deviceToken.ToString());
</pre></td></tr></tbody></table></code></pre></div>    </div>
    <p>with</p>
    <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>Appboy.SharedInstance?.RegisterDeviceToken(deviceToken);
</pre></td></tr></tbody></table></code></pre></div>    </div>
  </li>
</ul>

<h2 id="190">1.9.0</h2>

<p><strong>Important:</strong> This release has known issues displaying HTML in-app messages. Do not upgrade to this version and upgrade to 1.10.2 and above instead. If you are using this version, you are strongly encouraged to upgrade to 1.10.2 or above if you make use of HTML in-app messages.</p>

<h5 id="breaking-23">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#370">Braze Android SDK 3.7.0</a>.</li>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.19.0">Braze iOS SDK 3.19.0</a>.</li>
  <li>Note: This Braze Xamarin SDK release updates to Braze Android SDK and Braze iOS SDK dependencies which no longer enable automatic Braze location collection by default. Please consult their respective changelogs for information on how to continue to enable automatic Braze location collection, as well as further information on breaking changes.</li>
  <li>Removes the Feedback feature as well as all associated methods, classes, and interfaces.</li>
</ul>

<h2 id="180">1.8.0</h2>

<h5 id="changed-4">Changed</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#330">Braze Android SDK 3.3.0</a>.</li>
</ul>

<h5 id="added-5">Added</h5>
<ul>
  <li>Added C# bindings for Braze Android SDK classes with Firebase Cloud Messaging dependencies.</li>
</ul>

<h2 id="170">1.7.0</h2>

<h5 id="breaking-24">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#321">Braze Android SDK 3.2.1</a>.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to directly use the Firebase messaging event <code class="language-plaintext highlighter-rouge">com.google.firebase.MESSAGING_EVENT</code>. This is now the recommended way to integrate Firebase push with Braze. The <code class="language-plaintext highlighter-rouge">AppboyFcmReceiver</code> should be removed from your <code class="language-plaintext highlighter-rouge">AndroidManifest</code> and replaced with the following:
        <div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre>&lt;service android:name="com.appboy.AppboyFirebaseMessagingService"&gt;
&lt;intent-filter&gt;
&lt;action android:name="com.google.firebase.MESSAGING_EVENT" /&gt;
&lt;/intent-filter&gt;
&lt;/service&gt;
</pre></td></tr></tbody></table></code></pre></div>        </div>
      </li>
      <li>Also note that any <code class="language-plaintext highlighter-rouge">c2dm</code> related permissions should be removed from your manifest as Braze does not require any extra permissions for <code class="language-plaintext highlighter-rouge">AppboyFirebaseMessagingService</code> to work correctly.</li>
    </ul>
  </li>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.14.0">Braze iOS SDK 3.14.0</a>.
    <ul>
      <li>Drops support for iOS 8.</li>
      <li>Removes Cross-Promotion cards from the News Feed.</li>
    </ul>
  </li>
</ul>

<h2 id="160">1.6.0</h2>

<h5 id="breaking-25">Breaking</h5>
<ul>
  <li>Updated the native iOS bridge to <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.11.0">Braze iOS SDK 3.11.0</a>.</li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#301">Braze Android SDK 3.0.1</a>.</li>
</ul>

<h2 id="152">1.5.2</h2>

<h5 id="breaking-26">Breaking</h5>
<ul>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#250">Braze SDK version 2.5.0</a>.</li>
</ul>

<h5 id="fixed-4">Fixed</h5>
<ul>
  <li>Fixed an issue that caused C# bindings to not be generated for certain classes in the Braze UI library.</li>
</ul>

<h5 id="changed-5">Changed</h5>
<ul>
  <li>Updated the Android sample app to use Firebase Cloud Messaging (FCM).</li>
</ul>

<h2 id="151">1.5.1</h2>

<h5 id="changed-6">Changed</h5>
<ul>
  <li>Updated the iOS binding to use Braze SDK version <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.3.4">Braze iOS SDK 3.3.4</a>.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">DisableSDK()</code> and <code class="language-plaintext highlighter-rouge">RequestEnableSDKOnNextAppRun()</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to disable and re-enable the Braze SDK.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">WipeDataAndDisableForAppRun()</code> on the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to support wiping all customer data created by the Braze SDK.</li>
      <li>Note that methods that disable the SDK will cause <code class="language-plaintext highlighter-rouge">Appboy.SharedInstance</code> to return <code class="language-plaintext highlighter-rouge">null</code>. If you have code that uses <code class="language-plaintext highlighter-rouge">Appboy.SharedInstance</code>, do not use <code class="language-plaintext highlighter-rouge">DisableSDK()</code> or <code class="language-plaintext highlighter-rouge">WipeDataAndDisableForAppRun()</code> until your code can safely execute even if <code class="language-plaintext highlighter-rouge">Appboy.SharedInstance</code> is null.</li>
    </ul>
  </li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#225">Braze SDK version 2.2.5</a>.
    <ul>
      <li>Added <code class="language-plaintext highlighter-rouge">DisableSdk()</code> and <code class="language-plaintext highlighter-rouge">EnableSdk()</code> to the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to disable and re-enable the Braze SDK.</li>
      <li>Added <code class="language-plaintext highlighter-rouge">WipeData()</code> on the <code class="language-plaintext highlighter-rouge">Appboy</code> interface to support wiping all customer data created by the Braze SDK.</li>
    </ul>
  </li>
</ul>

<h2 id="15">1.5</h2>

<h5 id="breaking-27">Breaking</h5>
<ul>
  <li>Updated the iOS binding to use Braze SDK version <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.3.0">Braze iOS SDK 3.3.0</a>.</li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#221">Braze SDK version 2.2.1</a>.</li>
  <li>Removed the need to include <code class="language-plaintext highlighter-rouge">Appboy.bundle</code> manually in iOS integrations. Integrators should remove existing <code class="language-plaintext highlighter-rouge">Appboy.bundle</code> files from their iOS integrations.</li>
</ul>

<h5 id="added-6">Added</h5>
<ul>
  <li>Added the ability to report to Braze that the app is running Xamarin to iOS integrations. We strongly recommend reporting this value to allow Braze to calculate accurate usage around different SDK platforms. To enable reporting, add <code class="language-plaintext highlighter-rouge">Appboy.SharedInstance.SdkFlavor = ABKSDKFlavor.Xamarin;</code> to your <code class="language-plaintext highlighter-rouge">AppDelegate.cs</code> after calling <code class="language-plaintext highlighter-rouge">Appboy.StartWithApiKey()</code>.</li>
  <li>Braze Xamarin Bindings are now available on <a href="nuget.org">Nuget</a>. Check out our <a href="https://www.nuget.org/packages/AppboyPlatformXamariniOSBinding/">iOS Binding</a> and <a href="https://www.nuget.org/packages/AppboyPlatform.AndroidBinding/">Android Binding</a>. Note that Braze Xamarin SDK version <code class="language-plaintext highlighter-rouge">1.5.0</code> is the last version to receive a Xamarin component store release. Future releases will be released to Nuget and the open source repo only.</li>
</ul>

<h2 id="14">1.4</h2>

<h5 id="breaking-28">Breaking</h5>
<ul>
  <li>Updated the iOS binding to use Braze SDK version <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/2.29.0">Braze iOS SDK 2.29.0</a>.</li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#200">Braze SDK version 2.0.0</a>.</li>
</ul>

<h2 id="13">1.3</h2>

<h5 id="breaking-29">Breaking</h5>
<ul>
  <li>Updated the iOS binding to use Braze SDK version <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/2.24.2">Braze iOS SDK 2.24.2</a>.</li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1153">Braze SDK version 1.15.3</a>.</li>
  <li><strong>Update Required</strong> — Updated iOS push handling in the AppboyProject sample project to be compatible with iOS 10. For more information, refer to the CHANGELOG for <a href="https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#2240">Braze iOS SDK v2.24.0</a>.</li>
</ul>

<h5 id="changed-7">Changed</h5>
<ul>
  <li>Updated the AppboyProject sample project to integrate session handling and in-app message manager registration using an <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/com/appboy/AppboyLifecycleCallbackListener.java">AppboyLifecycleCallbackListener</a>, as introduced in Braze Android SDK v1.15.0.</li>
</ul>

<h5 id="removed">Removed</h5>
<ul>
  <li>Removed <code class="language-plaintext highlighter-rouge">AppboyBroadcastReceiver.cs</code> from the AppboyProject sample project, as Braze Android SDK v1.15.0 removes the need for a custom <code class="language-plaintext highlighter-rouge">AppboyBroadcastReceiver</code> for Braze push notifications.</li>
</ul>

<h2 id="12">1.2</h2>

<h5 id="breaking-30">Breaking</h5>
<ul>
  <li>Updated the iOS binding to use Braze SDK version <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/2.17.1">Braze iOS SDK 2.17.1</a>.</li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1110">Braze SDK version 1.11.0</a>.</li>
</ul>

<h2 id="11">1.1</h2>

<h5 id="breaking-31">Breaking</h5>
<ul>
  <li>Updated the iOS binding to use Braze SDK version <a href="https://github.com/Appboy/appboy-ios-sdk/releases/tag/2.12.0">Braze iOS SDK 2.12.0</a>.</li>
  <li>Updated the Android binding to use <a href="https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#180">Braze SDK version 1.8.0</a>.</li>
</ul>

<h5 id="added-7">Added</h5>
<ul>
  <li>Added a Xamarin Forms sample application with News Feed integrations.</li>
  <li>Added AppboyXamarinFormsFeedFragment that inherits from Android.App.Fragment to be compatible with Xamarin Forms.</li>
</ul>

<h2 id="10">1.0</h2>

<h5 id="added-8">Added</h5>
<ul>
  <li>Added support for all standard API and UI functionality in the Android SDK and iOS SDKs.</li>
  <li>iOS functionality not included in this release: IDFA collection, custom Slideup viewControllers, social data collection.</li>
  <li>Please contact support@braze.com for more information about these features and the timeline for their inclusion.</li>
</ul>



