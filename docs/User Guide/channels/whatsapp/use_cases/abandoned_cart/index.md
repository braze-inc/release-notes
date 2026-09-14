# Abandoned cart reminder in Canvas

> Build a WhatsApp Canvas that sends a personalized cart reminder when a user adds items to their cart but doesn't complete a purchase within a defined window.

## Requirements

Before building this Canvas, confirm the following are in place:

| Requirement | Description |
| --- | --- |
| WhatsApp Business Account | Your WhatsApp Business Account is connected to Braze and your subscription group is configured. For information on configuration, see [Setting up WhatsApp](https://www.braze.com/docs/user_guide/message_building_by_channel/whatsapp/overview/). |
| Approved marketing template | You have at least one approved WhatsApp marketing template for cart reminders. For steps on creating a template, see [WhatsApp Template Builder](https://www.braze.com/docs/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/). |
| Cart and purchase events | The events that fire when a user adds an item to their cart and when a user completes a purchase are tracked in Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Build a Canvas with abandoned cart reminders

The Canvas you build does the following:

1. Trigger when a user adds an item to their cart
2. Wait a set period without a completed purchase
3. Send a personalized WhatsApp message with a link to complete the purchase

### Step 1: Create the Canvas

1. Go to **Messaging** > **Canvas** and select **Create Canvas** > **Start a New Canvas**.
2. Name your Canvas (for example, "WhatsApp — Abandoned cart reminder").
3. Under **Entry Schedule**, select **Action-Based**. Set the entry trigger to the event your team uses to track when a user adds an item to their cart (for example, [`cart_updated`](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/ecommerce_events/#ecommerce-canvas-templates)).
4. Continue to **Target Audience**. In the **Entry Audience** section, go to **Entry Controls** and select **Allow users to re-enter this Canvas** so that repeat abandoners remain eligible for future sends.
5. Under **Exit Controls**, add an exception if a user completes a checkout, to prevent them from getting an unwanted message.

![Canvas exit controls with a checkout completion exception.](https://www.braze.com/docs/assets/img/whatsapp/abandoned_cart_exit_controls_1.png?11135eaa53c89de9dade696f4f92f972)

{:start="6"}
6. Build out the other settings of the canvas to your goals and preferences.

**Tip:**


If your cart events include item-level properties—such as product name, image URL, or price—consider using context and event properties. This allows you to create and use temporary data during a user’s journey through a specific Canvas. For guidance, see [Context and event properties](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/).



### Step 2: Build the Canvas flow

1. Add a **Delay** step immediately after the entry trigger. Set the delay to your preferred wait window before sending the reminder. A delay of 1–3 hours is common for cart abandonment.
2. After the Delay step, add an **Action Paths** step to check whether the user has completed a purchase during the delay window:
   - In the first path, add the purchase event your team uses to track completed orders. Name this path something like "Purchased."
   - Set the evaluation window for this Action Paths step to match the length of your delay.
   - Leave the second path as **Everyone Else**; this captures users who haven't yet purchased.
3. On the **Purchased** path, add an **Exit** step. Users who completed their purchase don't need a reminder.
4. On the **Everyone Else** path, add a **Message** step and continue to Step 3.

### Step 3: Configure the WhatsApp message

1. In the Message step, select **WhatsApp** as the channel.
2. Select your subscription group.
3. Under **Message type**, select **Template**.
4. Select your approved cart reminder template.
5. Fill in the template variables. Use Liquid to personalize with cart data:
   - To reference an event property captured at Canvas entry: `{{event_properties.${property_name}}}`
   - To include a return-to-cart URL, use a **URL button** in your template and pass the personalized link as the button variable.
6. Add a default value for every Liquid variable. WhatsApp messages with unresolved variable values won't be delivered.

**Important:**


WhatsApp template messages must be approved by Meta before use. If your cart reminder template hasn't yet been approved, it won't appear as an option in this step. Approval can take up to 24 hours after submission.



### Step 4: Set audience and launch settings

1. In the **Target Audience** settings, confirm your Canvas targets users who are opted in to your WhatsApp subscription group.
2. Add any additional filters relevant to your use case—for example, targeting only users with a minimum cart value.
3. Review your **Send Settings**:
   - Enable **Quiet Hours** to avoid sending messages at times unlikely to drive action.
   - Review **Frequency Capping** settings if users may be entering multiple active Canvases simultaneously.
4. Select **Review** to confirm your Canvas configuration, then select **Launch Canvas**.

### Step 5: Measure performance

After your Canvas has been running for at least one full send cycle, review the following in **Canvas Analytics**:

| Metric | What to look for |
| --- | --- |
| **Messages sent** | Confirms the Canvas is triggering correctly and messages are being delivered. |
| **Conversion rate** | Shows how many users completed a purchase after receiving the reminder. Set your primary conversion event to your purchase event with an appropriate conversion window. |
| **Revenue** | If revenue tracking is enabled, review the revenue attributed to this Canvas to assess direct impact. |
| **Opt-outs** | Monitor for increases that may indicate messaging frequency or timing needs adjustment. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas analytics metrics" }

**Tip:**


Use Canvas variants to A/B test different delay windows, message copy, or template designs to find what drives the highest conversion rate for your audience.


