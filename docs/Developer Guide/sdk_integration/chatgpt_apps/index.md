# Integrate Braze with ChatGPT apps

> This guide covers how to integrate Braze with ChatGPT apps to enable analytics and event logging within AI-powered applications.

![A Content Card integrated into ChatGPT app.](https://www.braze.com/docs/assets/img/chatgpt_app_integration.png?78e00c2a0ba475aaf2cae479a9a5fa0b){: style="float:right;max-width:30%;border:none;" }

## Overview

ChatGPT apps provide a powerful platform for building AI conversational applications. By integrating Braze with your ChatGPT app, you can continue to maintain first-party data control in the age of AI, including how to:

- Track user engagement and behavior within your ChatGPT app (such as identifying which questions or chat features your customers use)
- Segment and retarget Braze campaigns based on AI interaction patterns (such as emailing users who have used the chat more than three times per week)

### Key benefits

- **Own your customer journey:** While users interact with your brand through ChatGPT, you maintain visibility into their behavior, preferences, and engagement patterns. This data flows directly onto Braze user profiles, not just the AI platform's analytics.
- **Cross-platform retargeting:** Track user interactions in your ChatGPT app and retarget them across your owned channels (email, SMS, push notifications, in-app messaging) with personalized campaigns based on their AI usage patterns.
- **Return 1:1 promotional content to ChatGPT conversations:** Deliver Braze [in-app messages](https://www.braze.com/docs/user_guide/channels/in_app_messages/), [Content Cards](https://www.braze.com/docs/user_guide/channels/content_cards/), and more directly within your ChatGPT experience using the custom conversational UI components your team has built for your app.
- **Revenue attribution:** Track purchases and conversions that originate from ChatGPT app interactions.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Prerequisites

Before integrating Braze with your ChatGPT app, you must have the following:

- A new web app and API key in your Braze workspace
- A [ChatGPT app](https://openai.com/index/introducing-apps-in-chatgpt/) created in the OpenAI platform ([OpenAI sample app](https://github.com/openai/openai-apps-sdk-examples))

# ChatGPT app integration

## Setup

### Step 1: Get the Braze integration file

Copy the `braze.js` file from our [ChatGPT apps integration repository](https://github.com/braze-inc/chatgpt-apps-braze-integration/blob/main/src/braze/braze.ts) to your project. This file contains all the necessary Braze SDK configuration and helper functions.

### Step 2: Install dependencies

Install our Web SDK for Braze's most up-to-date set of features:

**For client-side integration:**
```bash
npm install @braze/web-sdk
```

<!-- **For server-side integration:**
```bash
npm install @braze/javascript-sdk
``` -->

<!-- The Braze JavaScript SDK is primarily designed for headless (server-side) environments and is currently in [beta](https://www.braze.com/company/legal/beta-terms). -->

## Implementation

There are two ways to integrate Braze with your ChatGPT app depending on your use case:

### Client-side integration (custom widgets)

**Tip:**


**Recommended Approach:** This method enables rich messaging experiences and real-time user interaction tracking within your ChatGPT app widgets.



For displaying Braze messaging and tracking user interactions within your custom ChatGPT app widgets, use the Web SDK integration. A full messaging example can be found in our sample repository [here](https://github.com/braze-inc/chatgpt-apps-braze-integration/tree/main/src/inbox).

#### Configure widget metadata

Add the following metadata to your MCP server file to allow Braze domains, ensuring to update the CDN domain based on [your region](https://www.braze.com/docs/developer_guide/platforms/web/content_security_policy):

```javascript
"openai/widgetCSP": {
  connect_domains: ["https://YOUR-SDK-ENDPOINT"],
  resource_domains: [
    "https://appboy-images.com",
    "https://braze-images.com",
    "https://cdn.braze.eu",
    "https://use.fontawesome.com"
  ],
}
```

Replace `YOUR-SDK-ENDPOINT` with your actual Braze SDK endpoint.

#### Set up the useBraze hook

```javascript
import { useBraze } from "./utils/braze";

function YourWidget() {
  const braze = useBraze({
    apiKey: "your-braze-api-key",
    baseUrl: "your-braze-endpoint.braze.com",
  });

  useEffect(() => {
    if (!braze.isInitialized) {
      return;
    }

    // Set user identity
    braze.changeUser("user-id-123");
    
    // Log widget interactions
    braze.logCustomEvent("viewed_pizzaz_list");
  }, [braze.isInitialized]);

  return (
    // Your widget JSX
  );
}
```

#### Display Braze Content Cards

```javascript
const [cards, setCards] = useState([]);

useEffect(() => {
  // Get cached content cards
  setCards(braze.getCachedContentCards()?.cards ?? []);

  // Subscribe to content card updates
  braze.subscribeToContentCardsUpdates((contentCards) => {
    setCards(contentCards.cards);
  });

  // Open session
  braze.openSession();

  return () => {
    braze.removeAllSubscriptions();
  }
}, []);
```

#### Track widget events

```javascript
// Track user interactions within your widget
const handleButtonClick = () => {
  braze.logCustomEvent("widget_button_clicked", {
    button_type: "save_list",
    widget_name: "pizza_list"
  });
};

const handleItemInteraction = (itemId) => {
  braze.logCustomEvent("item_interacted", {
    item_id: itemId,
    interaction_type: "view_details"
  });
};
```

### Server-side integration (MCP server)

<!-- For tracking events and purchases from your MCP server, add these code snippets to your server file (typically `server.js` or `server.ts`) where you handle ChatGPT app requests and tool calls. -->
If you also need a server-side integration for messaging functionality on your MCP server, contact <span style="white-space:nowrap;">`mcp-product@braze.com`</span>. For tracking events and purchases from your MCP server, use our [REST API](https://www.braze.com/docs/api/home).

<!-- #### Import the Braze functions

```javascript
// Import the desired methods from wherever you saved the file
import { BrazeSessionInfo, logCustomEvent, logPurchase } from "./braze/braze.js";
```

#### Set up session information

```javascript
// Create session info for Braze
const brazeSessionInfo: BrazeSessionInfo = {
  userId: userId,
  sessionId: sessionId || "default-session"
};
```

#### Track user interactions

```javascript
// Log custom events for user interactions
await logCustomEvent(brazeSessionInfo, "chatgpt_app_interaction", {
  app_id: "your_chatgpt_app_id",
  tool_name: request.params.name,
  user_authenticated: userId !== "anonymous",
  timestamp: new Date().toISOString()
});
```

#### Track purchases and transactions

```javascript
// Calculate order details for purchases
const totalPrice = examplePriceMethod(args.size, args.quantity);
const orderId = `ORDER-${Date.now()}`;

// Define the purchase properties you'd like to use
const purchaseProperties = {
  orderId,
  customerName: args.customerName,
  size: args.size,
  quantity: args.quantity,
  deliveryAddress: args.deliveryAddress,
  specialInstructions: args.specialInstructions,
  estimatedTime,
  totalPrice
};

// Log the purchase to Braze
await logPurchase(
  brazeSessionInfo, 
  "pizza", 
  totalPrice, 
  "USD", 
  args.quantity, 
  purchaseProperties
);
```

**Tip:**


Use the [SDK debugger](https://www.braze.com/docs/developer_guide/sdk_integration/debugging) to verify your integration and troubleshoot any issues.

 -->


