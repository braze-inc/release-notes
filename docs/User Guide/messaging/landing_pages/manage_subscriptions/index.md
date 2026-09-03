# Manage Subscriptions block

> Add a **Manage Subscriptions** block to a landing page so users can view, opt in to, and update their email, SMS, or WhatsApp subscription groups.

The **Manage Subscriptions** block supports two main use cases:

- **[Manage existing subscriptions](#update-existing-subscriptions):** Share the landing page's [Liquid tag](https://www.braze.com/docs/user_guide/messaging/landing_pages/tracking_users/) in an email, SMS, WhatsApp, or other channel message. When an identified user opens the page, the block automatically pre-fills each subscription group's checkbox with their current subscription state, so they can review and update their preferences.
- **[Capture new opt-ins](#capture-new-subscribers):** Add the block to a lead generation landing page alongside an **Email Capture** or **Phone Capture** block, so new visitors can choose which subscription groups to join when they submit the form.

**Important:**


Each **Manage Subscriptions** block is for one channel: [email](https://www.braze.com/docs/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states), or [WhatsApp](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states). To collect more than one channel, add a block for each. For RCS consent, use a [Phone Capture](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) block instead.



## Prerequisites

| Requirements | Description |
| --- | --- |
| Email, SMS, or WhatsApp subscription groups | At least one [email subscription group](https://www.braze.com/docs/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS subscription group](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states), or [WhatsApp subscription group](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) for the channel you add to the block. Create email groups from the dashboard or the [Subscription Group endpoints](https://www.braze.com/docs/api/endpoints/subscription_groups). SMS groups are provisioned during [SMS setup](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#enable-subscription-groups). WhatsApp groups are created when you [integrate WhatsApp](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/) with your workspace. |
| Landing page permissions | The same [permissions](https://www.braze.com/docs/user_guide/messaging/landing_pages#prerequisites) required to create and edit any landing page. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Step 1: Add the Manage Subscriptions block

In the drag-and-drop landing page editor, go to the **Build** section and select **Form Blocks**. Drag **Manage Subscriptions** into a row on your page; it auto-adjusts to the column width.

The block is empty until you add subscription groups to it. To show groups for more than one channel, add a **Manage Subscriptions** block for each channel.

## Step 2: Select the channel and subscription groups

With the **Manage Subscriptions** block selected, select **+ Add subscription groups** in the right-hand **Block properties** panel. The **Add subscription groups** modal opens.

1. On **Select channel**, choose **Email**, **SMS**, or **WhatsApp**. Each block supports one channel. If a channel already has a **Manage Subscriptions** block on the page, that channel card is disabled and labeled **Added**.
2. On **Select subscription groups**, select the groups to include. The list heading matches the channel (**Email subscription groups**, **SMS subscription groups**, or **WhatsApp subscription groups**).
3. Select **Add selected**.

Each subscription group appears as its own selectable checkbox on the landing page.

If you select **SMS** and your workspace has no SMS subscription groups yet, the modal shows **No SMS subscription groups yet**. Complete [SMS subscription group setup](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states), then return to the block.

If you select **WhatsApp** and your workspace has no WhatsApp subscription groups yet, the modal shows **No WhatsApp subscription groups yet**. Complete [WhatsApp subscription group setup](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states), then return to the block.

**Note:**


The **Manage Subscriptions** block only lists groups you explicitly add. Adding a subscription group to the block doesn't automatically subscribe visitors to it—a visitor must select the group's checkbox and submit the form.



## Step 3: Configure the block settings

Use the **Block properties** panel to adjust how the block behaves and appears.

### Subscription groups

- **Reorder groups:** Drag a subscription group by its handle to change the order it appears in the block.
- **Add or remove groups:** Select **+ Add subscription groups** to include more groups, or select the delete icon next to a group to remove it from the block.

### Include descriptions

Turn on **Include descriptions** to display each subscription group's description text alongside its name, giving visitors more context about what they're opting into. Email groups can include a description in Subscription Management. SMS and WhatsApp groups in this block don't show description text.

### "Subscribe to all" checkbox

Turn on the **"Subscribe to all" checkbox** setting to add an extra checkbox to the block. When a visitor selects it, every subscription group checkbox in the block is selected—useful for a quick opt-in to all listed groups.

## Update existing subscriptions

To let existing users review and update their email, SMS, or WhatsApp subscriptions, share the landing page using its [Liquid tag](https://www.braze.com/docs/user_guide/messaging/landing_pages/tracking_users/) in an email, SMS, WhatsApp, Canvas step, or other message. When a user opens the page through that link, Braze identifies them and automatically pre-fills each subscription group checkbox in the **Manage Subscriptions** block to match their current subscription state—similar to an [email preference center](https://www.braze.com/docs/user_guide/audience/subscription_preferences/preference_center/).

The user can select or clear checkboxes to update their subscriptions, then submit the form to save their changes.

**Note:**


Pre-filling a user's current subscription state in the **Manage Subscriptions** block is included by default and doesn't require the [Landing Pages Pro tier](https://www.braze.com/docs/user_guide/messaging/landing_pages#plan-tiers). This differs from [Liquid-based pre-fill](https://www.braze.com/docs/user_guide/messaging/landing_pages/personalize_landing_pages/#pre-fill-form-fields) for other form fields, which requires Landing Pages Pro.



## Capture new subscribers

To collect new subscribers, pair the **Manage Subscriptions** block with a capture field for that channel:

- **Email:** Add an [Email Capture](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) block so the page captures the visitor's email address alongside their email subscription group selections.
- **SMS or WhatsApp:** Add a [Phone Capture](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) block so the page captures the visitor's phone number alongside their SMS or WhatsApp subscription group selections.

If the visitor isn't identified (for example, they arrive without a landing page Liquid tag), the checkboxes start unselected. When they submit the form, they're subscribed to whichever subscription groups they selected.

## Things to know

- **One channel per block:** You can add one **Manage Subscriptions** block per channel on a page (one for email, one for SMS, and one for WhatsApp).
- **RCS:** This block doesn't list RCS subscription groups. To collect consent for RCS, use a [Phone Capture](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages) block.
- **Confirmation experience:** Landing pages with form blocks, including **Manage Subscriptions**, need a confirmation experience after submission. [Create a confirmation page](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/#step-4-create-a-confirmation-page-optional) and link to it from your **Submit** button.
- **Editor blocks reference:** For a full reference of every landing page block and its properties, see [Editor blocks (landing pages)](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
