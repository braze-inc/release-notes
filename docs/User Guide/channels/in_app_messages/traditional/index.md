# Create an in-app message

> You can create an in-app message or in-browser message using the Braze platform using campaigns, Canvas, or as an API campaign. We recommend using the [drag-and-drop editor](https://www.braze.com/docs/iam_drag_and_drop/) for most use cases, and planning out your messages and preparing all materials ahead of time using our [In-app message prep guide](https://www.braze.com/docs/user_guide/channels/in_app_messages/best_practices).

## Prerequisites {#create-new-campaign-in-app}

Before you start, make sure you have the following:

| Requirement | Description |
| --- | --- |
| Braze SDK | Integrate the [Braze SDK](https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=web) into your app or website. |
| Campaign or Canvas | Use a [campaign](https://www.braze.com/docs/user_guide/messaging/campaigns) for a single targeted message or [Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas) for a multi-step user journey. |
| Message plan | Prepare your content and assets using the [in-app message prep guide](https://www.braze.com/docs/user_guide/channels/in_app_messages/best_practices). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="In-app message prerequisites" }

## Editing experience

For most in-app messages, use the [drag-and-drop editor](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop). It supports modal and fullscreen messages with the same core layouts as the traditional editor, plus rows, Content Blocks, templates, multi-page flows, and ongoing feature updates.

Use the [traditional editor](https://www.braze.com/docs/user_guide/channels/in_app_messages/traditional) when you need slideup messages or custom HTML.


Switching a drag-and-drop message to the traditional editor converts the message to HTML. You can't switch it back to the drag-and-drop editor.

## Start your message




1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **In-App Message**. Note that in-app messages aren't available in multichannel campaigns.
3. Name your campaign something clear and meaningful.
4. Add [Teams](https://www.braze.com/docs/user_guide/administer/global/user_management/teams) and [Tags](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/tags) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder](https://www.braze.com/docs/user_guide/analytics/reports/report_builder), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. You can choose different platforms, message types, and layouts for each of your added variants. For more on this topic, refer to [Multivariate and A/B testing](https://www.braze.com/docs/user_guide/messaging/ab_testing).

**Tip:**


If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.






1. [Create your Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas) using the Canvas composer.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) and specify a delay as needed.
4. Filter your audience for this step as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay at the time messages are sent.
5. Choose your [advancement behavior](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Choose any other messaging channels which you would like to pair with your message.


**Important:**


You can't have multiple in-app message variants in a single step.



You can find more Canvas-specific information in [In-app messages in Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).




## Delivery platforms {#step-2-specify-delivery-platforms}

Choose the platforms that receive the message. Platform selections apply to individual variants, so you can test engagement across different platforms.

| Platform | Message delivery |
| --- | --- |
| **Mobile Apps** | Android, iOS, Kindle, and tvOS apps |
| **Web Browsers** | Web apps |
| **Both Mobile Apps & Web Browsers** | Android, iOS, Kindle, Kepler, tvOS, and Web apps |
| **Roku Devices** | Roku apps |
{: .reset-td-br-1 .reset-td-br-2 aria-label="In-app message delivery platforms" }

## Message types

After selecting a delivery platform, choose a message type and layout. The available types depend on the delivery platform and editing experience. For appearance, behavior, and creative specifications, see [In-app message types](https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types).

| Message type | Editing experience | Availability and layouts | When to use |
| --- | --- | --- | --- |
| [Fullscreen](https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/fullscreen) | Drag-and-drop and traditional | Image and text or image only. The traditional editor can enforce portrait or landscape orientation. | Critical announcements or promotions that need the user's full attention. |
| [Modal](https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/modal) | Drag-and-drop and traditional | Text with an optional image or image only. Roku supports modal messages only. | Promotions and feature prompts that need to stand out without covering the entire screen. |
| [Slideup](https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/slideup) | Traditional | Appears at the top or bottom of the app screen. | Short announcements, such as new features or cookie notices, that shouldn't block the rest of the screen. |
| [Custom HTML](https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/custom_html) | Traditional | Supports custom HTML, CSS, and JavaScript. Enable `allowUserSuppliedJavascript` for JavaScript. | Custom layouts or interactive experiences that the standard message types don't support. |
| [Email capture form](https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/email_capture_form) | Traditional | Available for supported app and web platform selections. | Collecting email addresses from users in your app or website. |
| [Web modal with CSS](https://www.braze.com/docs/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#web-modal-css) | Traditional | Available when you select **Web Browsers**. | Web-only modal messages that need custom CSS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="In-app message types and editors" }

**Important:**


Custom code messages must include a close or dismissal control. You can use the following snippet:

`<a href="appboy://close">X</a>`



## Composition

The available fields depend on your platform, message type, layout, and editing experience.

| Field or setting | What it controls | Notes |
| --- | --- | --- |
| **Language** | Adds language-specific Liquid conditions. | Add languages before writing your content. |
| **Image** | Adds an uploaded image, image URL, badge, or Font Awesome icon. | Options depend on the message type. |
| **Header** and **Message** | Sets the message text. | Supports Liquid and other personalization. |
| **Button Text** and **On-click behavior** | Sets up to two buttons and their actions. | Available actions depend on the selected platforms. |
| **Message Close** | Controls how users dismiss the message. | Choose automatic dismissal or wait for the user to dismiss. |
| **Slideup Position** | Places a slideup at the top or bottom of the app screen. | Available for slideup messages only. |
| **HTML** and assets | Defines custom code and uploaded assets. | Available for custom code message types. |
| **Key value pairs** | Sends extra custom fields to user devices. | Configure these on the **Settings** tab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="In-app message fields and settings" }

For drag-and-drop composition, see [Create an in-app message with drag-and-drop](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop).

The **Compose** tab lets you edit the message's content and behavior.

![An example brand's in-app message to welcome new customers and prompt them to set up a user profile.](https://www.braze.com/docs/assets/img_archive/iam_compose.png?2ffe5a0312e6230487dcf792b2f2b3eb){: style="max-width:85%" }

The content of the **Compose** tab varies based on your selected message options.

### Language

Select **Add Languages** and select your desired languages from the provided list. This will insert [Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) into your message. We recommend selecting your languages before writing your content so you can fill in your text where it belongs in the Liquid. See our [full list of available languages](https://www.braze.com/docs/developer_guide/localization?tab=android).

### Image

Depending on your message type, you can **Upload Image**, **Pick a Badge**, or use **Font Awesome**. To upload an image, select **Add Image** or provide an image URL. Selecting **Add Image** opens the **Media Library**, where you can select a previously uploaded image or add a new one. Each message type and platform may have its own suggested proportions and requirements—be sure to check what those are before commissioning or making an image from scratch.







































### Header and body

Enter your header and message copy. You can use [Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) and other personalization. Keep headers and message content clear and concise.

Some message types don't need and therefore don't ask for headers.

#### Generate AI copy

To generate message copy, use the [AI copywriting assistant](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities#generate-copy).

![Launch AI Copywriter button, located in the Message field of the in-app message composer.](https://www.braze.com/docs/assets/img/ai_copywriter/ai_copywriter_iam.png?ee0903850c68f4837acd2eed22be5db5){: style="max-width:60%"}

#### Create right-to-left messages

For languages such as Arabic and Hebrew, see [Creating right-to-left messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Button text {#buttons}

When available for your message type, you can have up to two buttons appear under your body of text. You can create and edit custom button text and color. You can also add a Terms of Service link within email capture forms.

If you only use one button, it automatically adjusts to take over the available space at the bottom of your message instead of leaving room for an additional button.

#### Choosing a primary button

Use Button 2 for your primary call to action. Give it a contrasting color so it stands out from the rest of the message.

![Primary and secondary buttons in an in-app message](https://www.braze.com/docs/assets/img/primary-secondary-buttons.png?c54b52a7200647f3f3fc6b3786bd48be)

### On-click behavior {#button-actions}

When a user selects a button in your in-app message, the following actions may be available based on the platform and workspace configuration.

| Action | Description |
|---|---|
| **Close message** | Closes the current message. |
| **Open web URL** | Opens a web page. You can choose to open the URL inside the app. |
| **Deeplink into application** | Opens content within your app. For more information, see [Deep linking to in-app content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content). |
| **Log custom event** | Logs a [custom event](https://www.braze.com/docs/user_guide/data/activation/events/custom_events). |
| **Log custom attribute** | Sets a [custom attribute](https://www.braze.com/docs/user_guide/data/activation/attributes/custom_attributes) for the current user. |
| **Request push permission** | Shows the native push permission prompt. For more information, see [Push primers](https://www.braze.com/docs/user_guide/channels/push/best_practices/push_primer_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="On-click behavior #button-actions" }

The **Request push permission**, **Log custom event**, and **Log custom attribute** options require the following minimum SDK versions:

<div id='sdk-versions'><a href='/docs/developer_guide/platforms/swift/changelog/#540' class='sdk-versions--chip ios-sdk' target='_blank'><i class='fa-brands fa-apple'></i> &nbsp; Swift: 5.4.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/web/changelog/#403' class='sdk-versions--chip web-sdk' target='_blank'><i class='fa-solid fa-desktop'></i> &nbsp; Web: 4.0.3+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a><a href='/docs/developer_guide/platforms/android/changelog/#2100' class='sdk-versions--chip android-sdk' target='_blank'><i class='fa-brands fa-android'></i> &nbsp; Android: 21.0.0+ &nbsp;<i class='fa-solid fa-arrow-up-right-from-square'></i></a></div>

To combine multiple actions or perform additional SDK actions not available in the dashboard (such as adding to a subscription group or setting an email subscription type), you can use [Braze Actions deeplinks](https://www.braze.com/docs/developer_guide/braze_actions).

### iOS device options

For messages that include iOS apps, select **Change** to send to all devices, all iOS devices, iPads only, or iPhones and iPod Touches only.

### Message close

Choose between the following options:
 
- **Dismiss automatically:** Select how many seconds the message remains on the screen, up to 60 seconds.
- **Wait for user to dismiss:** Keep the message open until the user dismisses it.

Dismissing a message logs an impression but not a click. For how clicks are tracked by user action, see [Click tracking](https://www.braze.com/docs/user_guide/channels/in_app_messages/reporting#click-tracking).

### Slide up position

This setting only applies to the Slideup message type. Choose between having your slideup appear **From Bottom of App Screen** or **From Top of App Screen**.

### HTML and assets

This setting only applies to the custom code message type. Copy and paste HTML into the available space and upload your assets using a [ZIP file](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library#zip-file-uploads).

### Email capture input placeholder

This setting only applies to the email capture form message type. Enter custom copy that will appear as the placeholder text for the email input field. This defaults to "Enter your email address".

## Design {#step-5-style-your-in-app-message}

Use the **Design** tab to adjust the visual appearance of a message created in the traditional editor. The available settings depend on the platform, message type, and layout.

| Setting | What it controls |
| --- | --- |
| [Color profile](https://www.braze.com/docs/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#reusable-color-profiles) | Applies a reusable color profile from the in-app message templates gallery. |
| Text alignment | Aligns supported header and body text to the left, center, or right. |
| Header and text | Sets text color and opacity. |
| Buttons | Sets the background, text, border, and opacity for each button. |
| Background color | Sets the message background color and opacity. |
| Screen overlay | Sets the color and opacity around modal and fullscreen messages. |
| Close control | Sets the color of the chevron or other close control. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Traditional editor design settings" }

Always [preview and test](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) your message before sending.

**Important:**


Custom code message types don't include the **Design** tab. Add HTML, CSS, JavaScript, and assets in the **Compose** tab. For web-specific CSS templates, see [Web modal with CSS](https://www.braze.com/docs/user_guide/messaging/templates/in_app_message_templates/in_app_message_template#web-modal-css).



## Additional settings

### Key-value pairs

You can add [key-value pairs](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) to send extra custom fields to user devices.

1. In the message composer, select the **Settings** tab.
2. In **Key value pairs**, select **Add new pair**.
3. Enter a key and value for each pair. To add another pair, select **Add new pair** again.

## Delivery and targeting

### Choose a campaign trigger {#choose-a-trigger}

Choose an action that triggers the campaign, then set the campaign's start and optional end time.

**Important:**


To trigger an in-app message from a custom event, log the event through the SDK.



![Action-based campaign with the trigger action set to "Start Session".](https://www.braze.com/docs/assets/img_archive/in_app_schedule.png?792a3fe4de6bfc59f1491150e3d8df9d){: style="max-width:80%"}

In-app message campaigns support the following action triggers:

- Start a session in the app or website
- Make a purchase
- Perform a custom event logged through the SDK

For server-triggered and local messages, see [Trigger in-app messages](https://www.braze.com/docs/developer_guide/in_app_messages/triggering_messages?tab=web).

#### Trigger messages offline

Braze sends eligible messages and their triggers to the user's device. After a message is cached, it can display when its trigger occurs while the device is offline.

**Important:**


After an in-app message campaign is stopped, users who started a session before it stopped may still see the cached message when they perform the trigger event. These users count as unique impressions.



### Choose a priority {#choose-a-priority}

Set the order in which eligible in-app messages display when multiple messages share a trigger. Campaigns and Canvas Message steps use the same priority ordering.

You can choose between the following message priorities:

- High priority (shown before other messages)
- Medium priority (default)
- Low priority (shown after other messages)

The high, medium, and low options are priority buckets. New or newly assigned messages receive the highest position within their bucket unless you set an exact priority.

Select **Set exact priority** to drag campaigns and Canvases into a specific order. You can also pin a message to keep it at the top of the high-priority bucket.

![An example of how priority is set for an in-app message campaign and Canvas.](https://www.braze.com/docs/assets/img_archive/bucket_prioritization.png?4c1e084584d0ee31d8e143b9f3fed9f0){: style="max-width:70%"}

### Choose users to target {#choose-users-to-target}

Use segments and filters to [target users](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/target_users). Braze calculates exact segment membership before sending the message to the device.

**Note:**


If an in-app message step has a delay, Braze evaluates segment membership after the delay. If the user is eligible, the message syncs during the next available session.



#### Re-evaluate campaign eligibility and Liquid {#re-evaluate-campaign-eligibility-and-liquid}

For campaigns, select **Re-evaluate campaign eligibility before displaying** when eligibility depends on frequently changing attributes or the message needs current profile data.

![Checkbox for "Re-evaluate campaign eligibility before displaying" selected.](https://www.braze.com/docs/assets/img_archive/re-evaluate-iam-membership.png?57c8ca286b218a268d43280ad3673872){:style="max-width:60%"}

When you select this option, the SDK makes an additional request to confirm that the user is still eligible. Braze also evaluates [Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid) and [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content) immediately before displaying the message.

This option prevents cached messages from displaying when the user no longer meets the campaign's eligibility criteria.

**Note:**


This option requires a network connection and adds a request before display. Don't use it for messages that must trigger while the user is offline.



#### Use data added by REST API in a message

User data that the [`/users/track` endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) adds in the same session can sometimes be used in that user's in-app message. For example, if a user is in the audience for an in-app message that is waiting on a trigger, starts a session, and in that same session the REST API updates their profile, that new data can appear in the in-app message when **Re-evaluate campaign eligibility before displaying** is selected. Braze won't template the in-app message until it's time to render.

If one trigger both sends data to Braze and fires the in-app message, the message can't use that newly updated profile data, even with a scheduled delay. Use two separate triggers instead: one to send the data, and one to trigger the in-app message.

### Configure Canvas message controls

Canvas in-app messages include controls for expiration, trigger actions, and a delay of up to two hours. For details, see [In-app messages in Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas#messages-in-canvas).

## Things to know

### Active in-app message campaign capacity

To maintain message delivery performance, stop action-based in-app message campaigns that are no longer needed.

**Important:**


The default capacity is 200 active, action-based in-app message campaigns per workspace. Your workspace may have a different capacity. This doesn't apply to Canvases.



The count includes active campaigns that haven't reached their end time and campaigns without an end time. It excludes campaigns that have passed their end time, reached their maximum impressions, or are no longer enabled.

### Local time delivery evaluation

When an in-app message campaign uses the user's local time zone, Braze evaluates the campaign's start and end time in that time zone. A cached message displays only when the user is eligible and its trigger occurs within the configured delivery window.

## Next steps

After composing your in-app message, continue building and validating the campaign or Canvas:

- [Configure Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas) or finish [scheduling your campaign](https://www.braze.com/docs/user_guide/messaging/campaigns/schedule_your_campaign)
- [Target users](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/target_users) and configure [conversion events](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/conversion_events)
- [Preview and test the message](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message)
- Review [in-app message reporting](https://www.braze.com/docs/user_guide/channels/in_app_messages/reporting)
