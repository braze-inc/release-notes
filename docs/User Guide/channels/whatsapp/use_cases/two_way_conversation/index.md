# Two-way conversation orchestration in Canvas

> Build a Canvas that listens for inbound WhatsApp messages, responds immediately using response messages, and routes the conversation based on what the user says or selects. 

Response messages are the primary tool for this use case because they're faster to deploy than templates, require no Meta approval, and support interactive formats like quick replies and list menus.

## Requirements

Before building this Canvas, confirm the following are in place:

- Your WhatsApp Business Account is connected to Braze and your subscription group is configured. See [WhatsApp setup](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/).
- Your subscription group can receive and process inbound WhatsApp messages. See [Action-based triggers](https://www.braze.com/docs/user_guide/channels/whatsapp/message_processing/messaging_users/#action-based-triggers).
- Users who enter this Canvas are opted in to your WhatsApp subscription group.
- Only one active Canvas should use **None** under **Condition to match** for the same subscription group. If multiple Canvases match the same inbound message, a user may receive multiple responses.

## About response messages

Response messages are the core building block of two-way WhatsApp conversations in Braze. Unlike template messages, they don't require Meta approval and are composed directly in the Canvas editor. They can only be sent within the 24-hour conversation window, which opens when a user messages your business and resets each time they do.

Braze supports five response message layouts:

| Layout | Best used for |
| --- | --- |
| **Text Message** | Delivering information or a direct next step, such as a simple reply, confirmation, or follow-up |
| **Quick Reply** | Guiding the user toward a specific next action with up to three tappable button options |
| **List Message** | Guiding the user toward a specific next action with a structured menu (up to 10 rows total across sections) |
| **Call-to-action Button** | Delivering a direct next step by directing users to a URL |
| **Media Message** | Enriching responses with an image, video, audio file, or document |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Response message layouts" }

## Build a Canvas with two-way conversation orchestration

The Canvas you build does the following:

1. Trigger when a user sends your business a WhatsApp message
2. Immediately send a response message with reply options
3. Take a path based on the user's selection
4. Deliver a tailored response message on each path

### Step 1: Create the Canvas

1. Go to **Messaging** > **Canvas** and select **Create Canvas** > **Start a New Canvas**.
2. Name your Canvas (for example, "WhatsApp — Two-Way Conversation").
3. Under **Entry Schedule**, select **Action-Based**.
4. Under **Action-Based Options**, add the entry trigger **Send a WhatsApp inbound message** and select your **Subscription group**.
   - Under **Condition to match**, select **None** to respond to any inbound message regardless of content.
   - To trigger only on a specific keyword or phrase (for example, "HELP" or "START"), select **Message body text**, then configure **Where the message body** with the keyword.
5. Continue to **Target Audience**. In the **Entry Audience** section, go to **Entry Controls** and select **Allow users to re-enter this Canvas**. Select **Specified Window** and set re-eligibility to **0** seconds so users can start a new conversation as soon as they message again after exiting. See [Re-eligibility](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/re_eligibility) for other timeframe options.

**Tip:**


To handle multiple keywords with different flows, create a separate Canvas for each keyword rather than trying to branch on keywords within a single Canvas. This makes each flow easier to manage and update.



### Step 2: Send an opening response message

The first step in your Canvas should acknowledge the user and present their options.

1. Add a **Message** step immediately after the entry trigger.
2. Select **WhatsApp** as the channel and choose your subscription group.
3. Under **Message type**, select **Response Message**.
4. Choose a layout for your opening message:
   - Use **Quick Reply** if you have three or fewer options (for example, "Track my order," "Contact support," "Browse offers"). Each button label is limited to 20 characters.
   - Use **List Message** if you have more than three options or want to organize options into categories. You can add up to 10 rows total across sections. The button that opens the list is limited to 20 characters; each row title is limited to 24 characters.
5. Write your message body and configure your reply options.

**Important:**


Response messages can only be sent within the 24-hour conversation window. Because this Canvas is triggered by an inbound message, the window is open at entry, but keep downstream steps close to the trigger to avoid the window expiring before all messages send. See [Step 5](#step-5-handle-window-expiry-and-fallbacks) for how to handle this.



### Step 3: Branch on user reply with Action Paths

After sending the opening response message, use an **Action Paths** step to route users based on their reply.

1. Add an **Action Paths** step after the Message step.
2. Create one action group for each reply option you presented:
   - Set the trigger to **Send a WhatsApp inbound message** and select your **Subscription group**.
   - Under **Condition to match**, select **Message body text**, then configure **Where the message body** with the quick reply button label or list row title (for example, "Track my order").
3. Select the **Action Settings** banner, then set the **Evaluation Window** to a reasonable reply window, typically 1–5 minutes for an active conversation, or longer if users may step away before responding.
4. Leave the final path as **Everyone Else** to catch users who don't reply or send an unexpected response.

**Tip:**


Quick reply buttons send the button label text as the reply. List message selections send the row title as the reply, or the row title and description on separate lines if you included a description. Braze matches inbound message body filters without regard to capitalization, but the text must otherwise match the reply Braze receives.



### Step 4: Configure response messages for each path

Each branch of your conversation should deliver a response message tailored to what the user selected.

1. Add a **Message** step to each path in your Action Paths step.
2. For each message step, select **WhatsApp** > your subscription group > **Response Message** as the message type.
3. Choose the layout that best fits the content you're delivering on that path:

| Layout | When to use |
| --- | --- |
| **Text Message** | Delivering a direct answer, confirmation, or short piece of information |
| **Call-to-action Button** | Directing the user to a URL (for example, an order tracking page or support portal) |
| **Media Message** | Sending a visual asset such as a product image, how-to video, or PDF guide |
| **Quick Reply or List Message** | Continuing the conversation with another question or menu |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Response message layouts by path" }

{:start="4"}
4. Write the message body for each path. Use Liquid to personalize with user attributes or event properties where relevant.

#### Continuing the conversation

If a path leads to another question, repeat Steps 3 and 4. Add another Action Paths step to branch on the user's next reply, followed by another Message step. Each exchange resets the 24-hour conversation window as long as the user continues replying.

#### Ending the conversation

When a path reaches a natural endpoint (the user has received what they need), close it with an **Exit** step or let users exit by reaching the end of the Canvas.

### Step 5: Handle window expiry and fallbacks {#step-5-handle-window-expiry-and-fallbacks}

The 24-hour conversation window closes if a user stops replying. If you try sending a response message after the window closes, the message won't deliver.

On the **Everyone Else** path of any Action Paths step (users who didn't reply), choose one of the following:

- **Exit the Canvas:** End the flow and let the conversation close naturally.
- **Send a template message:** Re-engage the user after the window closes by adding a Message step using a **Template** message type. Template messages can be sent at any time and don't require an open conversation window.

**Important:**


Template messages sent as a re-engagement follow-up must be approved by Meta in advance. Use a utility template (for example, "We noticed you didn't finish — let us know if you still need help") rather than a marketing template to reduce the chance of users opting out.



### Step 6: Measure performance

After your Canvas runs for a meaningful period, review the following in **Canvas Analytics**:

| Metric | What to look for |
| --- | --- |
| **Messages sent** | Confirms the Canvas is triggering on inbound messages and responses are being delivered. |
| **Action Paths performance** | In each Action Paths step, review how many users **Entered** each action group to see which reply options are most common. |
| **Conversion rate** | Track how many users completed the desired outcome (for example, visited a support page, made a purchase). Set a primary conversion event that reflects your goal. |
| **Historical performance** | Review unsubscribe or opt-out trends over time to see whether the conversation flow is driving unwanted exits. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas Analytics metrics" }

**Tip:**


Review the **Everyone Else** path volume in your Action Paths steps. High drop-off there may mean users are replying with text you didn't anticipate, or that your reply window is too short.


