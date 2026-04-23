# Content Cards

> Learn about Content Cards for the Braze SDK, including the different data models and card-specific properties available for your application.

**Tip:**


Using Content Cards for banner-style messages? Try out [Banners](https://www.braze.com/docs/user_guide/message_building_by_channel/banners/)&#8212; perfect for inline, persistent in-app and web messages.





**Note:**


This guide uses code samples from the Braze Web SDK 4.0.0+. To upgrade to the latest Web SDK version, see [SDK Upgrade Guide](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).




## Prerequisites

Before you can use Content Cards, you'll need to [integrate the Braze Web SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web) into your app. However, no additional setup is required. To build your own UI instead, see [Content Card Customization Guide](https://www.braze.com/docs/developer_guide/content_cards/).

**Note:**


Some ad blockers and browser privacy extensions can block the Braze Web SDK script or related network requests, which can prevent Content Cards from loading. If you're using the CDN integration method, consider switching to the [NPM integration method](https://www.braze.com/docs/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web), which stores SDK libraries locally on your website and can avoid some ad-blocker-related issues.



## Standard feed UI

To use the included Content Cards UI, you'll need to specify where to show the feed on your website. 

In this example, we have a `<div id="feed"></div>` in which we want to place the Content Cards feed. We'll use three buttons to hide, show, or toggle (hide or show based on its current state) the feed.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script> 
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

When using the `toggleContentCards(parentNode, filterFunction)` and `showContentCards(parentNode, filterFunction)` methods, if no arguments are provided, all Content Cards will be shown in a fixed-position sidebar on the right-hand side of the page. Otherwise, the feed will be placed in the specified `parentNode` option.

|Parameters | Description |
|---|---|
|`parentNode` | The HTML node to render the Content Cards into. If the parent node already has a Braze Content Cards view as a direct descendant, the existing Content Cards will be replaced. For example, you should pass in `document.querySelector(".my-container")`.|
|`filterFunction` | A filter or sort function for cards displayed in this view. Invoked with the array of `Card` objects, sorted by `{pinned, date}`. Expected to return an array of sorted `Card` objects to render for this user. If omitted, all cards will be displayed. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[See the SDK reference docs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) for more information on Content Card toggling.

## Testing Content Cards on the web

You can test your Content Cards integration using your browser's developer tools.

1. Create a Content Card campaign and target your test user.
2. Log in to the website that has your Web SDK integration.
3. Open your browser console. For Chrome, right-click the page, select **Inspect**, then select the **Console** tab.
4. Run these commands in the console:
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## Card types and properties

The Content Cards data model is available in the Web SDK and offers the following Content Card types: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), and [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Each type inherits common properties from a base model [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) and has the following additional properties.

**Tip:**


To log Content Card data, see [Logging analytics](https://www.braze.com/docs/developer_guide/content_cards/logging_analytics/).



### Base card model

All Content Cards have these shared properties:

|Property|Description|
|---|---|
| `expiresAt` | The UNIX timestamp of the card's expiration time.|
| `extras`| (Optional) Key-value pair data formatted as a string object with a value string. |
| `id` | (Optional) The id of the card. This will be reported back to Braze with events for analytics purposes. |
| `pinned` | This property reflects if the card was set up as "pinned" in the dashboard.|
| `updated` | The UNIX timestamp of when this card was last modified. |
| `viewed` | This property reflects whether the user viewed the card or not.|
| `isControl` | This property is `true` when a card is a "control" group within an A/B test.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image only

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) cards are clickable full-sized images.

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The UNIX timestamp of the card's creation time from Braze. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captioned image

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) cards are clickable, full-sized images with accompanying descriptive text.

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The UNIX timestamp of the card's creation time from Braze. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `title` | The title text for this card. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classic

The [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) model can contain an image with no text or a text with image.

|Property|Description|
|---|---|
| `aspectRatio` | The aspect ratio of the card's image and serves as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
| `categories` | This property is purely for organization in your custom implementation; these categories can be set in the dashboard composer. |
| `clicked` | This property indicates whether this card has ever been clicked on this device. |
| `created` | The UNIX timestamp of the card's creation time from Braze. |
| `description` | The body text for this card. |
| `dismissed` | This property indicates if this card has been dismissed. |
| `dismissible` | This property reflects if the user can dismiss the card, removing it from view. |
| `imageUrl` | The URL of the card's image.|
| `linkText` | The display text for the URL. |
| `title` | The title text for this card. |
| `url` | The URL that will be opened after the card is clicked on. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Control group

If you use the default Content Cards feed, impressions and clicks will be automatically tracked.

If you use a custom integration for Content Cards, you need need [log impressions](https://www.braze.com/docs/developer_guide/content_cards/logging_analytics/) when a Control Card would have been seen. As part of this effort, make sure to handle Control cards when logging impressions in an A/B test. These cards are blank, and while they aren’t seen by users, you should still log impressions in order to compare how they perform against non-Control cards.

To determine if a Content Card is in the Control group for an A/B test, check the `card.isControl` property (Web SDK v4.5.0+) or check if the card is a `ControlCard` instance (`card instanceof braze.ControlCard`).

## Card methods

### Default feed methods

Use these methods when displaying Content Cards using the Braze default feed UI:

|Method | Description |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Displays the default Content Cards feed. Renders cards into a provided `parentNode` HTML element, or as a fixed-position sidebar on the right side of the page if no element is given. Accepts an optional `filterFunction` to sort or filter cards before display. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Hides the default Content Cards feed if it is currently showing. |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Shows the default Content Cards feed if it is hidden, or hides it if it is visible. If you need to display multiple Content Card feeds simultaneously, use `showContentCards` and `hideContentCards` instead. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Custom feed methods

Use these methods when building your own Content Card UI:

|Method | Description |
|---|---|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Registers a callback function that is invoked whenever Content Cards are updated for the current user, such as on session start. Use this as the primary way to receive card data for your custom feed. Must be called before `openSession()` to receive updates on the initial session. |
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)| Returns all currently available cards from the most recent Content Cards refresh. Use this to immediately display cards on page load without waiting for a new server request, such as when the user returns to a page during an active session. |
|[`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)| Requests an immediate refresh of Content Cards from Braze servers. By default, cards refresh on session start and when the default feed is reopened. Use this to force a refresh at other times, such as after a specific user action. Be aware of [rate limits](https://www.braze.com/docs/developer_guide/content_cards/customizing_cards/feed/#rate-limit). |
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Logs impression events for an array of cards. Call this when cards are rendered and visible to the user. Required for accurate campaign reporting when using a custom UI, as impressions are not tracked automatically outside the default feed. |
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Logs a click event for a single card. Call this when a user interacts with a card in your custom UI. Required for accurate campaign reporting, as clicks are not tracked automatically outside the default feed. |
|[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)| Processes a card's URL and executes the configured on-click action, including Braze actions (`brazeActions://` URLs) and standard URL navigation. Call this in your card click handler to ensure on-click behaviors configured in the Braze dashboard are executed. |
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)| Programmatically dismisses a card, removing it from the user's feed. Use this to allow users to dismiss cards in your custom UI. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more details, refer to the [SDK reference documentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

## Best practices

### Call methods in the correct order

For custom feeds, Content Cards refresh only on session start if `subscribeToContentCardsUpdates()` is called before `openSession()`. Call your Braze methods in this order:

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### Use cached cards to persist content across page loads

Because `subscribeToContentCardsUpdates()` invokes only its callback when there are new updates (such as on session start), cards can disappear from your custom feed if a user refreshes the page mid-session. To prevent this, use `getCachedContentCards()` to immediately render cards from the local cache, alongside your subscription for new updates:

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### Log analytics for custom feeds

When using a custom UI, impressions, clicks, and dismissals are not tracked automatically. You must log each event manually:

- **Impressions:** Call `logContentCardImpressions([card1, card2, ...])` with an array of card objects when cards become visible to the user.
- **Clicks:** Call `logContentCardClick(card)` when a user interacts with a card.
- **On-click behavior:** Call `handleBrazeAction(card.url)` to execute the card's configured on-click action (such as navigating to a URL or logging a custom event).

**Warning:**


The argument passed to `logContentCardClick()` must be an original Braze `Card` object. If you transform or reconstruct the card data (for example, by serializing and deserializing), clicks are not logged and you see the error: "card must be a Card object."



## Using Google Tag Manager

Google Tag Manager works by injecting the [Braze CDN](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (a version of our Web SDK) directly into your website code, which means that all SDK methods are available just as if you had integrated the SDK without Google Tag Manager, except when implementing Content Cards.

### Setting up Content Cards



For a standard integration of the Content Card feed, you can use a **Custom HTML** tag in Google Tag Manager. Add the following to your Custom HTML tag, which will activate the standard Content Card feed:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Tag Configuration in Google Tag Manager of a Custom HTML tag that shows the Content Card feed.](https://www.braze.com/docs/assets/img/web-gtm/gtm_content_cards.png?0568575182a8f9fbe2e5acfd37f9a3c4)



For more freedom over customizing the appearance of Content Cards and their feed, you can directly integrate Content Cards into your native website. There are two approaches you can take with this: using the standard feed UI or creating a custom feed UI.



When implementing the [standard feed UI](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), Braze methods must have `window.` added to the start of the method. For example, `braze.showContentCards` should instead be `window.braze.showContentCards`.



For [custom feed](https://www.braze.com/docs/developer_guide/content_cards/creating_cards/) styling, the steps are the same as if you had integrated the SDK without GTM. For example, if you want to customize the width of the Content Card feed, you can paste the following into your CSS file:


```css
body .ab-feed { 
    width: 800px;
}
```






### Upgrading templates {#upgrading}

To upgrade to the latest version of the Braze Web SDK, take the following three steps in your Google Tag Manager dashboard:

1. **Update tag template**<br>Go to the **Templates** page within your workspace. Here you should see an icon indicating an update is available.<br><br>![Templates page showing an update is available](https://www.braze.com/docs/assets/img/web-gtm/gtm-update-available.png?f36c891c9e7be7f37f873e17517a827b)<br><br>Click that icon and after reviewing the change, click to **Accept Update**.<br><br>![A screen comparing the old and new tag templates with a button to "Accept Update"](https://www.braze.com/docs/assets/img/web-gtm/gtm-accept-update.png?417cfc6f52f25fc1953509c10e637ed1)<br><br>
2. **Update version number**<br>Once your tag template has been updated, edit the Braze Initialization Tag, and update the SDK version to the most recent `major.minor` version. For example, if the latest version is `4.1.2`, enter `4.1`. You can view a list of SDK versions in our [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Braze Initialization Template with an input field to change the SDK Version](https://www.braze.com/docs/assets/img/web-gtm/gtm-version-number.png?9487bc3d9318863f2899478c0265715f)<br><br>
3. **QA and publish**<br>Verify the new SDK version is working using Google Tag Manager's [debugging tool](https://support.google.com/tagmanager/answer/6107056?hl=en) prior to publishing an update to your tag container.

### Troubleshooting {#troubleshooting}

#### Enable tag debugging {#debugging}

Each Braze tag template has an optional **GTM Tag Debugging** checkbox which can be used to log debug messages to your web page's JavaScript console.

![Google Tag Manager's Debug tool](https://www.braze.com/docs/assets/img/web-gtm/gtm-tag-debugging.png?7389da92ab6dd818760e71b6f48dfbab)

#### Enter debug mode

Another way to help debug your Google Tag Manager integration is using Google's [Preview mode](https://support.google.com/tagmanager/answer/6107056) feature.

This will help identify what values are being sent from your web page's data layer to each triggered Braze tag and will also explain which tags were or were not triggered.

![The Braze Initialization Tag summary page provides an overview of the tag, including information on which tags were triggered.](https://www.braze.com/docs/assets/img/web-gtm/gtm-debug-mode.png?f7a1f3c237c28bc521087754a40561f3)

#### Verify tag sequencing for custom events {#tag-sequencing}

If custom events or other actions aren't logging in Braze, a common cause is a race condition where an action tag (such as **Custom Event** or **Purchase**) fires before the **Braze Initialization** tag has completed. To fix this, configure [tag sequencing](https://support.google.com/tagmanager/answer/6238868) in GTM:

1. Open the action tag that isn't logging correctly.
2. Under **Advanced Settings** > **Tag Sequencing**, select **A tag that fires before \[this tag\]**.
3. Choose your **Braze Initialization** tag as the setup tag.

This ensures the SDK is fully initialized before any action tags attempt to send data to Braze.

#### Enable verbose logging

To capture detailed logs for troubleshooting, you can enable verbose logging on your Google Tag Manager integration. These logs will appear in the **Console** tab of your browser's [developer tools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools).

In your Google Tag Manager integration, navigate to your Braze Initialization Tag and select **Enable Web SDK Logging**.

![The Braze Initialization Tag summary page with the option to Enable Web SDK Logging turned on.](https://www.braze.com/docs/assets/img/web-gtm/gtm_verbose_logging.png?c5d9946843f312420b2b6e00ea669647)

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md




## Prerequisites

Before you can use Braze Content Cards, you'll need to integrate the [Braze Android SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=android) into your app. However, no additional setup is required.

## Google fragments

In Android, the Content Cards feed is implemented as a [fragment](https://developer.android.com/guide/components/fragments.html) available in the Braze Android UI project. The [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) class will automatically refresh and display the contents of the Content Cards and log usage analytics. The cards that can appear in a user's `ContentCards` are created on the Braze dashboard.

To learn how to add a fragment to an activity, see [Google's fragments documentation](https://developer.android.com/guide/fragments#Adding).

## Card types and properties

The Content Cards data model is available in the Android SDK and offers the following unique Content Card types. Each type shares a base model, which allows them to inherit common properties from the base model, in addition to having their own unique properties. For full reference documentation, see [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Base card model {#base-card-for-android}

The [base card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) model provides foundational behavior for all cards.  

|Property | Description |
|---|---|
|`getId()` | Returns the card's ID set by Braze.|
|`getViewed()` | Returns a boolean reflects if the card is read or unread by the user.|
|`getExtras()` | Returns a map of key-value extras for this card.|
|`getCreated()`  | Returns the unix timestamp of the card's creation time from Braze.|
|`isPinned` | Returns a boolean that reflects whether the card is pinned.|
|`getOpenUriInWebView()`  | Returns a boolean that reflects whether Uris for this card should be opened <br> in the Braze WebView or not.|
|`getExpiredAt()` | Gets the expiration date of the card.|
|`isRemoved()` | Returns a boolean that reflects whether the end user has dismissed this card.|
|`isDismissibleByUser()`  | Returns a boolean that reflects whether the card is dismissible by the user.|
|`isClicked()` | Returns a boolean that reflects the clicked state of this card.|
|`isDismissed` | Returns a boolean that reflects whether the card has been dismissed. Set to `true` to mark the card as dismissed. If a card is already marked as dismissed, it cannot be marked as dismissed again.|
|`isControl()` | Returns a boolean if this card is a control card and should not be rendered.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image only {#banner-image-card-for-android}

[Image only cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) are clickable full-sized images.

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card's image.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL.|
|`getDomain()` | Returns link text for the property URL.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Captioned image {#captioned-image-card-for-android}

[Captioned image cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) are clickable, full-sized images with accompanying descriptive text.

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card's image.|
|`getTitle()` | Returns the title text for the card.|
|`getDescription()` | Returns the body text for the card.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL.|
|`getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Classic {#text-Announcement-card-for-android}

A classic card without an image included will result in a [text announcement card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). If an image is included, you will receive a [short news card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Property | Description |
|---|---|
|`getTitle()` | Returns the title text for the card. |
|`getDescription()` | Returns the body text for the card. |
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL. | 
|`getDomain()` | Returns the link text for the property URL. |
|`getImageUrl()` | Returns the URL of the card's image, applies only to the classic Short News Card. |
|`isDismissed` | Returns a boolean that reflects whether the card has been dismissed. Set to `true` to mark the card as dismissed. If a card is already marked as dismissed, it cannot be marked as dismissed again. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Card methods

All [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) data model objects offer the following analytics methods for logging user events to Braze servers.

|Method | Description |
|---|---|
|`logImpression()` | Manually log an impression to Braze for a particular card. |
|`logClick()` | Manually log a click to Braze for a particular card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }




## Prerequisites

Before you can use Content Cards, you'll need to integrate the [Braze Swift SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift) into your app. However, no additional setup is required.

## View controller contexts

The default Content Cards UI can be integrated from the `BrazeUI` library of the Braze SDK. Create the Content Cards view controller using the `braze` instance. If you wish to intercept and react to the Content Card UI lifecycle, implement [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) as the delegate for your `BrazeContentCardUI.ViewController`.

**Note:**


For more information about iOS view controller options, refer to the [Apple developer documentation](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).



The `BrazeUI` library of the Swift SDK provides two default view controller contexts: [navigation](#swift_navigation) or [modal](#swift_modal). This means you can integrate Content Cards in these contexts by adding a few lines of code to your app or site. Both views offer customization and styling options as described in the [customization guide](https://www.braze.com/docs/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios). You can also create a custom Content Card view controller instead of using the standard Braze one for even more customization options&#8212;refer to the [Content Cards UI tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) for an example.

**Important:**


To handle control variant Content Cards in your custom UI, pass in your [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) object, then call the `logImpression` method as you would with any other Content Card type. The object will implicitly log a control impression to inform our analytics of when a user would have seen the control card.



### Navigation

A navigation controller is a view controller that manages one or more child view controllers in a navigation interface. Here is an example of pushing a `BrazeContentCardUI.ViewController` instance into a navigation controller:




```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```




```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```




### Modal

Use modal presentations to create temporary interruptions in your app’s workflow, such as prompting the user for important information. This model view has a navigation bar on top and a **Done** button on the side of the bar. Here is an example of pushing a `BrazeContentCard.ViewController` instance into a modal controller:




```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```




```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```




For example usage of `BrazeUI` view controllers, check out the corresponding Content Cards UI samples in our [Examples app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Base card model

The Content Cards data model is available in the `BrazeKit` module of the Braze Swift SDK. This module contains the following Content Card types, which are an implementation of the `Braze.ContentCard` type. For a full list of Content Card properties and their usage, see  [`ContentCard` class](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard). 

- Image only
- Captioned image
- Classic
- Classic image
- Control

To access the Content Cards data model, call `contentCards.cards` on your `braze` instance. See [Logging analytics](https://www.braze.com/docs/developer_guide/content_cards/logging_analytics/) for more information on subscribing to card data.

**Note:**


Keep in mind, `BrazeKit` offers an alternative [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) class for Objective-C compatibility.



## Card methods

Each card is initialized with a `Context` object, which contains various methods for managing your card's state. Call these methods when you want to modify the corresponding state property on a particular card object.

| Method                               | Description                                                                                                                              |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()`      | Log the content card impression event.                                                                                                   |
| `card.context?.logClick()`           | Log the content card click event.                                                                                                        |
| `card.context?.processClickAction()` | Process a given [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction) input. |
| `card.context?.logDismissed()`       | Log the content card dismissed event.                                                                                                    |
| `card.context?.logError()`           | Log an error related to the content card.                                                                                                |
| `card.context?.loadImage()`          | Load a given content card image from a URL. This method can be nil when the content card does not have an image.                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For more details, refer to the [`Context` class documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)




## Prerequisites

Before you can use this feature, you'll need to [integrate the Cordova Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=cordova).

## Card Feeds

The Braze SDK includes a default card feed. To show the default card feed, you can use the `launchContentCards()` method. This method handles all analytics tracking, dismissals, and rendering for a user's Content Cards.

## Content Cards

You can use these additional methods to build a custom Content Cards Feed within your app:

|Method | Description |
|---|---|
|`requestContentCardsRefresh()`|Sends a background request to request the latest Content Cards from the Braze SDK server.|
|`getContentCardsFromServer(successCallback, errorCallback)`|Retrieves Content Cards from the Braze SDK. This will request the latest Content Cards from the server and return the list of cards upon completion.|
|`getContentCardsFromCache(successCallback, errorCallback)`|Retrieves Content Cards from the Braze SDK. This will return the latest list of cards from the local cache, which was updated at the last refresh.|
|`logContentCardClicked(cardId)`|Logs a click for the given Content Card ID.|
|`logContentCardImpression(cardId)`|Logs an impression for the given Content Card ID.|
|`logContentCardDismissed(cardId)`|Logs a dismissal for the given Content Card ID.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }




## About Flutter Content Cards

The Braze SDK includes a default card feed to get you started with Content Cards. To show the card feed, you can use the `braze.launchContentCards()` method. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards.

## Prerequisites

Before you can use this feature, you'll need to [integrate the Flutter Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=flutter).

## Card methods

You can use these additional methods to build a custom Content Cards Feed within your app by using the following methods available on the [plugin public interface](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart):

| Method                                         | Description                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Requests the latest Content Cards from the Braze SDK server.                                           |
| `braze.logContentCardClicked(contentCard)`    | Logs a click for the given Content Card object.                                                            |
| `braze.logContentCardImpression(contentCard)` | Logs an impression for the given Content Card object.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | Logs a dismissal for the given Content Card object.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Receiving Content Card data

To receive Content Card data in your Flutter app, the `BrazePlugin` supports sending Content Card data by using [Dart Streams](https://dart.dev/tutorials/language/streams).

The `BrazeContentCard` [object](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html) supports a subset of fields available in the native model objects, including `description`, `title`, `image`, `url`, `extras`, and more.

### Listen for Content Card data in the Dart layer

To receive Content Card data in the Dart layer, use the code below to create a `StreamSubscription` and call `braze.subscribeToContentCards()`. Remember to `cancel()` the stream subscription when it is no longer needed.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

For an example, see [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) in the Braze Flutter SDK sample application.

### Forward Content Card data from the native iOS layer




Content Card data is automatically forwarded from both the Android and iOS native layers. No additional setup is required.




If you're using Flutter SDK 17.1.0 or earlier, Content Card data forwarding from the iOS native layer requires manual setup. Your application likely contains a `contentCards.subscribeToUpdates` callback that calls `BrazePlugin.processContentCards(contentCards)`. To migrate to Flutter SDK 18.0.0, remove the `BrazePlugin.processContentCards(_:)` call—data forwarding is now handled automatically.

For an example, see [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in the Braze Flutter SDK sample application.




#### Replaying the callback for Content Cards

To store any Content Cards triggered before the callback is available and replay them after it is set, add the following entry to the `customConfigs` map when initializing the `BrazePlugin`:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```




## About React Native Content Cards

The Braze SDKs include a default card feed to get you started with Content Cards. To show the card feed, you can use the `Braze.launchContentCards()` method. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards.

## Prerequisites

Before you can use this feature, you'll need to [integrate the React Native Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native).

## Cards methods

To build your own UI, you can get a list of available cards, and listen for updates to cards:

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

**Important:**


If you choose to build your own UI to display cards, you must call `logContentCardImpression` in order to receive analytics for those cards. This includes `control` cards, which must be tracked even though they are not displayed to the user.



You can use these additional methods to build a custom Content Cards Feed within your app:

| Method                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Launches the Content Cards UI element.                                                                 |
| `requestContentCardsRefresh()`           | Requests the latest Content Cards from the Braze SDK server. The resulting list of cards is passed to each of the previously registered [content card event listeners](#reactnative_cards-methods). |
| `getContentCards()`                      | Retrieves Content Cards from the Braze SDK. This returns a promise that resolves with the latest list of cards from the server. |
| `getCachedContentCards()`                | Returns the most recent Content Cards array from the cache.                                            |
| `logContentCardClicked(cardId)`          | Logs a click for the given Content Card ID. This method is used only for analytics. To execute the click action, call `processContentCardClickAction(cardId)` in addition.                                                        |
| `logContentCardImpression(cardId)`       | Logs an impression for the given Content Card ID.                                                      |
| `logContentCardDismissed(cardId)`        | Logs a dismissal for the given Content Card ID.                                                        |
| `processContentCardClickAction(cardId)`  | Perform the action of a particular card.                                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Card types and properties

The Content Cards data model is available in the React Native SDK and offers the following Content Cards card types: [Image Only](#image-only), [Captioned Image](#captioned-image), and [Classic](#classic). There's also a special [Control](#control) card type, which is returned to users that are in the control group for a given card. Each type inherits common properties from a base model in addition to its own unique properties.

**Tip:**


For a full reference of the Content Card data model, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) documentation.



### Base card model

The base card model provides foundational behavior for all cards.

|Property      | Description                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`          | The card's ID set by Braze.                                                                                            |
|`created`     | The UNIX timestamp of the card's creation time from Braze.                                                             |
|`expiresAt`   | The UNIX timestamp of the card's expiration time. When the value is less than 0, it means the card never expires.      |
|`viewed`      | Whether the card is read or unread by the user. This does not log analytics.                                           |
|`clicked`     | Whether the card has been clicked by the user.                                                                         |
|`pinned`      | Whether the card is pinned.                                                                                            |
|`dismissed`   | Whether the user has dismissed this card. Marking a card as dismissed that has already been dismissed will be a no-op. |
|`dismissible` | Whether the card is dismissible by the user.                                                                           |
|`url`         | (Optional) The URL string associated with the card click action.                                                       |
|`openURLInWebView` | Whether URLs for this card should be opened in the Braze WebView or not.                                            |
|`isControl`   | Whether this card is a control card. Control cards should not be displayed to the user.                                |
|`extras`      | The map of key-value extras for this card.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the base card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) documentation.

### Image only

Image only cards are clickable, full-sized images.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `IMAGE_ONLY`.                                                                              |
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the image only card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) documentation.

### Captioned image

Captioned image cards are clickable, full-sized images with accompanying descriptive text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `CAPTIONED`.                                                                               |
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the captioned image card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct) documentation.

### Classic

Classic cards have a title, description, and an optional image on the left of the text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | The Content Card type, `CLASSIC`.                                                                                 |
|`image`            | (Optional) The URL of the card's image.                                                                           |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the classic (text announcement) Content Card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) documentation. For the classic image (short news) card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct) documentation.

### Control

Control cards include all of the base properties, with a few important differences. Most importantly:

- The `isControl` property is guaranteed to be `true`.
- The `extras` property is guaranteed to be empty.

For a full reference of the control card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct) documentation.




## Prerequisites

Before you can use Content Cards, you'll need to integrate the [Braze Swift SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=swift) into your app. Then you'll need to complete the steps for setting up your tvOS app.

**Important:**


Keep in mind, you'll need to implement your own custom UI since Content Cards are supported via headless UI using the Swift SDK&#8212;which does not include any default UI or views for tvOS.



## Setting up your tvOS app

### Step 1: Create a new iOS app

In Braze, select **Settings** > **App Settings**, then select **Add App**. Enter a name for your tvOS app, select **iOS**&#8212;_not tvOS_&#8212;then select **Add App**.

![ALT_TEXT.](https://www.braze.com/docs/assets/img/tvos.png?d1c5036d5b83f425591adb03556ca684){: style="width:70%"}

**Warning:**


If you select the **tvOS** checkbox, you will not be able to customize Content Cards for tvOS.



### Step 2: Get your app's API key

In your app settings, select your new tvOS app then take note of your app's API key. You'll use this key to configure your app in Xcode.

![ALT_TEXT](https://www.braze.com/docs/assets/img/tvos1.png?9851deb799c1c88a248f97bd284c91cb){: style="width:70%"}

### Step 3: Integrate BrazeKit

Use your app's API key to integrate the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) into your tvOS project in Xcode. You only need to integrate BrazeKit from the Braze Swift SDK.

### Step 4: Create your custom UI

Because Braze doesn't provide a default UI for content cards on tvOS, you'll need to customize it yourself. For a full walkthrough, see our step-by-step tutorial: [Customizing content cards for tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). For a sample project, see [Braze Swift SDK samples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).




## Prerequisites

Before you can use this feature, you'll need to [integrate the Unity Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=unity).

## Displaying Content Cards natively {#unity-content-cards-native-ui}

You can display the default UI for Content Cards using the following call:

```csharp
Appboy.AppboyBinding.DisplayContentCards();
```

## Receiving Content Card data in Unity

You may register Unity game objects to be notified of incoming Content Cards. We recommend setting game object listeners from the Braze configuration editor.

If you need to configure your game object listener at runtime, use `AppboyBinding.ConfigureListener()` and specify `BrazeUnityMessageType.CONTENT_CARDS_UPDATED`.

Note, you will additionally need to make a call to `AppboyBinding.RequestContentCardsRefresh()` to start receiving data in your game object listener on iOS.

## Parsing Content Cards

Incoming `string` messages received in your Content Cards game object callback can be parsed into our pre-supplied [`ContentCard`](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) model object for convenience.

Parsing Content Cards requires JSON parsing, see the following example for details:

##### Example Content Cards callback

```csharp
void ExampleCallback(string message) {
  try {
    JSONClass json = (JSONClass)JSON.Parse(message);

    // Content Card data is contained in the `mContentCards` field of the top level object.
    if (json["mContentCards"] != null) {
      JSONArray jsonArray = (JSONArray)JSON.Parse(json["mContentCards"].ToString());
      Debug.Log(String.Format("Parsed content cards array with {0} cards", jsonArray.Count));

      // Iterate over the card array to parse individual cards.
      for (int i = 0; i < jsonArray.Count; i++) {
        JSONClass cardJson = jsonArray[i].AsObject;
        try {
          ContentCard card = new ContentCard(cardJson);
          Debug.Log(String.Format("Created card object for card: {0}", card));

          // Example of logging Content Card analytics on the ContentCard object 
          card.LogImpression();
          card.LogClick();
        } catch {
          Debug.Log(String.Format("Unable to create and log analytics for card {0}", cardJson));
        }
      }
    }
  } catch {
    throw new ArgumentException("Could not parse content card JSON message.");
  }
}
```

## Refreshing Content Cards

To refresh Content Cards from Braze, call either of the following methods:

```csharp
// results in a network request to Braze
AppboyBinding.RequestContentCardsRefresh()

AppboyBinding.RequestContentCardsRefreshFromCache()
```

## Analytics

Clicks and impressions must be manually logged for Content Cards not displayed directly by Braze.

Use `LogClick()` and `LogImpression()` on [ContentCard](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/Models/Cards/ContentCard.cs) to log clicks and impressions for specific cards.





## About .NET MAUI Content Cards

The Braze .NET MAUI (formerly Xamarin) SDK includes a default card feed to get you started with Content Cards. The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user’s Content Cards.

## Prerequisites

Before you can use this feature, you'll need to [integrate the .NET MAUI Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=.net%20maui%20(xamarin)).

## Card types and properties

The Braze .NET MAUI SDK has three unique Content Cards card types that share a base model: [Banner](#xamarin_banner), [Captioned Image](#xamarin_captioned-image), and [Classic](#xamarin_classic). Each type inherits common properties from a base model and has the following additional properties.

### Base card model

|Property           | Description                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | The card's ID set by Braze.                                                                                            |
|`created`          | The UNIX timestamp of the card's creation time from Braze.                                                             |
|`expiresAt`        | The UNIX timestamp of the card's expiration time. When the value is less than 0, it means the card never expires.      |
|`viewed`           | Whether the card is read or unread by the user. This does not log analytics.                                           |
|`clicked`          | Whether the card has been clicked by the user.                                                                         |
|`pinned`           | Whether the card is pinned.                                                                                            |
|`dismissed`        | Whether the user has dismissed this card. Marking a card as dismissed that has already been dismissed will be a no-op. |
|`dismissible`      | Whether the card is dismissible by the user.                                                                           |
|`urlString`        | (Optional) The URL string associated with the card click action.                                                       |
|`openUrlInWebView` | Whether URLs for this card should be opened in the Braze WebView or not.                                                 |
|`isControlCard`    | Whether this card is a control card. Control cards should not be displayed to the user.                                |
|`extras`           | The map of key-value extras for this card.                                                                             |
|`isTest`           | Whether this card is a test card.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the base card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) documentation.

### Banner

Banner cards are clickable, full-sized images.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the banner card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) documentation (now renamed to image only).

### Captioned image

Captioned image cards are clickable, full-sized images with accompanying descriptive text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | The URL of the card's image.                                                                                      |
|`imageAspectRatio` | The aspect ratio of the card's image. It is meant to serve as a hint before image loading completes. Note that the property may not be supplied in certain circumstances. |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the captioned image card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct) documentation.

### Classic

Classic cards have a title, description, and an optional image on the left of the text.

|Property           | Description                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (Optional) The URL of the card's image.                                                                           |
|`title`            | The title text for the card.                                                                                      |
|`cardDescription`  | The description text for the card.                                                                                |
|`domain`           | (Optional) The link text for the property URL, for example, `"braze.com/resources/"`. It can be displayed on the card's UI to indicate the action/direction of clicking on the card. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the classic (text announcement) Content Card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) documentation. For a full reference of the classic image (short news) card, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct) documentation.

## Card methods

You can use these additional methods to build a custom Content Cards Feed within your app:

| Method                                   | Description                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Requests the latest Content Cards from the Braze SDK server.                                           |
| `getContentCards()`                      | Retrieves Content Cards from the Braze SDK. This will return the latest list of cards from the server. |
| `logContentCardClicked(cardId)`          | Logs a click for the given Content Card ID. This method is used only for analytics.                    |
| `logContentCardImpression(cardId)`       | Logs an impression for the given Content Card ID.                                                      |
| `logContentCardDismissed(cardId)`        | Logs a dismissal for the given Content Card ID.                                                        |



