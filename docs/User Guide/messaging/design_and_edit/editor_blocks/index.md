# Drag-and-drop editor blocks

> Editor blocks are the various blocks available in the **Drag-And-Drop Editor**. This reference article includes a series of tiles that represent the different kinds of content you can use in your messages.




## Using email editor blocks

Editor blocks are located under the **Content** section for email messages. To use an editor block, drag an editor block inside a column in the drag-and-drop editor. It will auto-adjust to the column width. Each editor block has its owns settings, such as granular control on padding.

For more information on how to use and customize these editor blocks in your email, check out [Other customizations](https://www.braze.com/docs/user_guide/message_building_by_channel/email/drag_and_drop/#other-customizations).

**Tip:**


You can also add [custom attributes](https://www.braze.com/docs/user_guide/data/activation/custom_data/custom_attributes/) to any URL within the `Image`, `Button`, or `Text` editor blocks.



## Types

The following table describes how users can use each editor block type.

| Name | Description |
|---|---|
|Title| Adds text for Headers within the email. | 
|Paragraph| Enters text into their message. A toolbar helps with font and text editing functionality. | 
|List| Adds a bulleted list. |
|Button| Adds a standard button. Properties for this block allow for editing and setting links easily. | 
|Divider| Inserts a solid, dotted, or dashed line to help with spacing.|
|Spacer| Adds space, or "padding", between other blocks. |
|Image| Inserts an image from the [media library](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library/). | 
|Video| Creates a link to the video content. |
|Social| Inserts social media platform icon. You can upload custom images for brand specific icons. |
|Icons| Inserts an icon. You can upload custom images. Braze uses an oversized placeholder icon until you upload an image. |
|HTML| Inserts raw HTML. Recommended for [Liquid](https://www.braze.com/docs/liquid/), such as Connected Content or conditional statements. | 
|Menu| Creates a flexible menu for the message you're designing. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Personalization in email

- **Liquid:** Under **Content** > **Personalization**, select an attribute, copy the snippet, and paste it into a text block (basic Liquid) or HTML block (advanced Liquid). In general, while you can use basic Liquid in text blocks, we recommend using HTML blocks for heavier logic to avoid layout issues. Note that Liquid isn't supported in image blocks or in button URL fields.
- **Connected Content:** Add an **HTML** block and place your `{% connected_content %}` call there.

## Properties

Details for each editor block's properties are provided in the following tables.

### Title
Refer to the following table for details on the `Title` editor block properties.

| Properties | Description |
|---|---|
|Title| Selects the heading style. | 
|Font family| This is the font style for your title. |
|Font weight| This is the overall boldness of the font. |
|Font size| Determines the size of your text. |
|Text color| Modifies the color of the title. |
|Link color| Modifies the color of the link. |
|Align| Moves the title to be left, center, or right-oriented. |
|Line height| Modifies the distance between lines of text. |
|Line spacing| Modifies the distance in between each character. |
|Text direction| Default left-to-right, but can be edited to be [right-to-left](https://www.braze.com/docs/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paragraph

Refer to the following table for details on the `Paragraph` editor block properties.

| Properties | Description |
|---|---|
|Font family| This is the font style for your paragraph text. |
|Font weight| This is the overall boldness of the font. |
|Font size| Determines the size of your text. |
|Text color| Modifies the color of the title. |
|Link color| Modifies the color of the link. |
|Align| Moves the title to be left, center, or right-oriented. |
|Paragraph spacing| Modifies the space between paragraphs. |
|Line height| Modifies the distance between lines of text. |
|Letter spacing| Modifies the distance in between each character. |
|Text direction| Default left-to-right, but can be edited to be [right-to-left](https://www.braze.com/docs/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### List

Refer to the following table for details on the `List` editor block properties.

| Properties | Description |
|---|---|
|List type| This is the type of list. Can be either bulleted or numbered. |
|List style type| Determines the style of your list. |
|Start list from| Determines the starting number for your list. |
|Font family| This is the font style for your paragraph text. |
|Font weight| This is the overall boldness of the font. |
|Font size| Determines the size of your text. |
|Text color| Modifies the color of the title. |
|Link color| Modifies the color of the link. |
|Align| Moves the title to be left, center, or right-oriented. |
|List items spacing| Modifies the space between list items. |
|List items indent| Modifies the indentation of list items. |
|Line height| Modifies the distance between lines of text. |
|Letter spacing| Modifies the distance in between each character. |
|Text direction| Default left-to-right, but can be edited to be [right-to-left](https://www.braze.com/docs/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Divider

Refer to the following table for details on the `Divider` editor block.

| Properties | Description |
|---|---|
|Transparent| If enabled, 'line' and 'width' options are removed. |
|Line| The different line formats, whether dotted, spotted, or solid. In addition, you can modify the thickness and color of the divider line. |
|Width | Adjusts the spread of the divider in increments of 5.  |
|Align| Moves the line to be either left, center, or right-oriented. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Spacer

Refer to the following table for details on the `Spacer` editor block.

| Properties | Description |
|---|---|
|Height| Adjusts the height of the spacer block. The default is 60px.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

Refer to the following table for details on the `Image` editor block. For dynamic images (images with Liquid or Connected Content), you must set a fallback image to use the auto-width settings. For image specifications, refer to our [email image specifications](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/image_specs/#email).











































| Properties | Description |
|---|---|
|Auto Width| Modifies the width of the image in pixels. |
|Align| Orients the image to either the left, center or right of the block. |
|Image with Liquid| Use [Liquid](https://www.braze.com/docs/liquid/) logic to dynamically set different images within the same block of content. |
|URL| Set an image using the address to where it's hosted. |
|Alternate text| A short description of the image that gives users the same information that's shown in the image. This is essential for screen-reader accessibility or when the image fails to load. |
|Image with Rounded Corners| Render the image with rounded corners. By default, images are rendered with squared corners. |
|Action| Triggers an action when the user clicks the image.|
|Block Options| Sets padding around the image block. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Tip:**


For `Auto Width`, automatic image resizing picks the best size for the image based on a combination of image width and available space in the layout:
- Images wider than the available space will be set at 100% width and will keep this ratio on mobile, using the entire device display width.
- Images smaller than the available space will use the image's natural size to avoid distortion effects or blurry pictures.



### Video

Refer to the following table for details on the `Video` editor block.

| Properties | Description |
|---|---|
|URL| The URL for the video. Note that only YouTube and Vimeo are supported. |
|Title| Auto-generated from the video meta data or can be customized. |
|Play Icon Style| Includes different options for the play button located at the top of a video image. |
|Play Icon Color| Option to select either **Light** or **Dark** for the play button. |
|Play Icon Size| Choose the pixel size for the play button. Pre-fixed range from 50&nbsp;px to 80&nbsp;px (incremented by 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Tip:**


Videos hosted by Vimeo will only work if they are set to public. All other security settings available within Vimeo (for example, "Hide from Vimeo.com") will generate a different link format that is not supported by this Content Block. These types of links are altered by the builder, which prevents Braze from generating a thumbnail.



### Social

Refer to the following table for details on the `Social` editor block.

| Properties | Description |
|---|---|
|Select icon collection| Sets the style of your icon collection. |
|Configure icon collection| Sets the URL for each social icon. Includes the **More options** toggle to edit the title and alternative text. |
|Align| Moves the social icon to be left, center, or right-oriented. |
|Icon spacing| Determines the spacing between each social icon. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Icons

Refer to the following table for details on the `Icons` editor block.

| Properties | Description |
|---|---|
|Font family| This is the font style for your paragraph text. |
|Font weight| This is the overall boldness of the font. |
|Font size| Determines the size of your text. |
|Text color| Modifies the color of the title. |
|Link color| Modifies the color of the link. |
|Align| Moves the icon to be left, center, or right-oriented. |
|Letter spacing| Modifies the distance in between each character. |
|Icon size| Determines the size of your icon. |
|Icon spacing| Modifies the space of the icon. |
|Icon padding| Modifies the padding of the icon. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML

Refer to the following table for details on the `HTML` editor block.

| properties | description |
|---|---|
|html editor| Enter the raw HTML. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Menu

Refer to the following table for details on the `Menu` editor block.

| Properties | Description |
|---|---|
|Configure menu items| Add a menu item. |
|Font Family| The style to be used for your menu. |
|Font Size| The size of your menu. |
|Text Color| Modifies the color of the menu. |
|Link Color| Modifies the color of the menu text. |
|Align| Moves the menu to be left, center, or right-oriented. |
|Letter spacing| Modifies the distance in between each character. |
|Layout| Determines the layout to be either horizontal or vertical. |
|Separator| Add character(s) between the menu options. |
|Mobile menu| Includes options to modify the icon size, color, and icon type when shown on a mobile device. |
|Item padding| Modifies the padding by using either the **+** or **-** button, or by entering a specific number. |
|All sides| Sets a consistent padding number if Item padding is disabled. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Actions

You can assign an action that occurs when a user taps a button, link, or image in the message. You can also use [Liquid](https://www.braze.com/docs/liquid/) to personalize the actions. Details for each editor block's actions are provided in the following tables.

### Button

Refer to the following table for details on the `Button` editor block.

| Properties | Description |
|---|---|
|Link Type| Determines the action when clicking the button and sets the appropriate protocol. |
|URL| Dynamic based on the **Open web page** link type.|
|Mail to, Subject, and Body| For the **Send email** link type, this sets the recipient email address, subject, and content that will populate in a draft email when the user selects the button.|
|Tel| For the **Make call** and **Send SMS** link type, this sets the phone number the user will call or text when selecting the button.|
|Message| For the **Send SMS** link type, this sets the content that will populate in a draft SMS message when the user selects the button.|
|Button options| Sets various button options, such as font, width, color, and others.|
|Button Hover| The style of the button when a user hovers over it using a mouse or trackpad. This includes the button's background color, font color, and border styles.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }




## Using in-app message editor blocks

Editor blocks are located under the **Build** section for in-app messages. To use them, drag an editor block inside a column. It will auto-adjust to the column width. Each editor block has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element.

## Types

The following table describes how you can use each editor block type.

| Name | Description |
| --- | --- |
| Title | Enters a title text into the message. |
| Paragraph | Enters a paragraph text into the message. |
| Button | Adds a standard button. Properties for this block allow for editing, setting links, and logging analytics. |
| Radio Button | Adds a list of options from which users can select one. When submitted, the user profile logs the associated custom attribute, which must be a string to be saved. Custom attributes with other data types do not save to the user profile. |
| Image | Inserts an image from the [media library](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library/). |
| Link | Inserts a hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone. |
| Spacer | Adds space or padding between other blocks. |
| Custom Code | Inserts and runs custom HTML, CSS, or JavaScript for advanced customization.  |
| Phone Capture | Inserts a form field for phone numbers. When submitted, the user is subscribed to the [SMS](https://www.braze.com/docs/sms_rcs_subscription_groups/) or [WhatsApp subscription group](https://www.braze.com/docs/whatsapp_subscription_groups/). |
| Email Capture | Inserts a form field for email addresses. When submitted, the email address is added to that user's profile in Braze. |
| Short Text    | Inserts a form field that supports standard attributes (such as first and last name) or a custom attribute string of your choice. |
| Dropdown      | Inserts a dropdown with a pre-defined list of items from which users can select one. You can add any custom attribute strings to the list. |
| Checkbox      | Inserts a checkbox. If the user checks the box, the block's attribute is set to `true`. If left unchecked, its attribute is set to `false`. |
| Checkbox Group| Users can select from multiple choices presented. Values are either set or added to a defined array custom attribute. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Properties

Details for each editor block's properties are provided in the following tables.

### Title and Paragraph

| Property | Description |
| --- | --- |
| Font family | The font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| Line height | Modifies the distance between lines of text |
| Letter spacing | Modifies the distance in between each character |
| Text alignment | Moves the text to be aligned left, center, right, or justified |
| Text color | Modifies the color of the text |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Button

| Property | Description |
| --- | --- |
| Button width | Modifies the width of the button to be automatic or manual |
| Font family | This is the font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| Letter spacing | Modifies the distance in between each character |
| Button alignment | Moves the button to be left, center, or right-oriented |
| Button text color | Modifies the color of the text on the button |
| Background color | Modifies the color of the button's background |
| Border style | Determines the style of the button's border of the button | 
| Border radius | Determines how round you would like the corners |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image











































| Property | Description |
| --- | --- |
| URL | The hosted address for the image |
| Alignment | Moves the image to be left, center, or right-oriented |
| Background color | Modifies the color of the image's background |
| Border style | Determines the style of the image's border | 
| Border radius | Determines how round you would like the corners of the image |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Property | Description |
| --- | --- |
| Font family | This is the font style for the text |
| Font weight | Determines the thickness of the text |
| Letter spacing | Modifies the distance in between each character |
| Text color | Modifies the color of the text |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Spacer

| Property | Description |
| --- | --- |
| Background color | Modifies the background color of the spacer |
| Height | Modifies the height of the spacer. You can also modify this by using the resize handles on the spacer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Custom code

| Property | Description |
| --- | --- |
| Custom Code | Allows you to add, edit, or delete HTML, CSS, and JavaScript for an in-app message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Phone capture

| Property | Description |
| --- | --- |
| Subscription group | The [SMS](https://www.braze.com/docs/sms_rcs_subscription_groups/) or [WhatsApp subscription group](https://www.braze.com/docs/whatsapp_subscription_groups/) that the user will be subscribed to by collecting their phone number, with an option to collect numbers from all countries |
| Text alignment | Moves the text to be aligned left, center, right, or justified |
| Placeholder text | A placeholder phone number to display |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Email capture

| Property | Description |
| --- | --- |
| Font family | The font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| Line height | Modifies the distance between lines of text |
| Text color | Modifies the color of the text |
| Letter spacing | Modifies the distance in between each character |
| Text alignment | Moves the text to be aligned left, center, right, or justified |
| Placeholder text | A placeholder email address to display |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Actions

You can assign an action that occurs when a user taps a button, link, or image in the message. You can also use [Liquid](https://www.braze.com/docs/liquid/) to personalize the actions. Details for each editor block's actions are provided in the following tables.

### Button

| Action | Description |
| --- | --- |
| Submit form when button is clicked | Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. |
| Set separate behaviors for each platform | Customizes the behavior of the button for each platform separately. |
| On-click behavior | Determines the action when the user clicks the button, such as closing the message, opening the web URL, deeplinking into a specific page of the app, going to another page, or [requesting push permission](https://www.braze.com/docs/push_primer/). |
| Log custom attributes or events | Determines if clicking the button will update the user's profile with custom data. You can also select the identifier for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

For image specifications, refer to our [in-app message image specifications](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

| Action | Description |
| --- | --- |
| Alt text | The written copy that appears in place of an image if the image fails to load. Screen readers announce alt text to explain images, so use plain language to provide key information about an image. |
| Submit form when image is clicked | Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. |
| Set separate behaviors for each platform | Customizes the behavior of the image for each platform separately. |
| On-click behavior | Determines the action when the user clicks the image, such as closing the message, opening the web URL, deeplinking into a specific page of the app, going to another page, or [requesting push permission](https://www.braze.com/docs/push_primer/). |
| Log custom attributes or events | Determines if clicking the image will update the user's profile with custom data. You can also select the identifier for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Action | Description |
| --- | --- |
| URL | The hyperlink to navigate to |
| Identifier for Reporting | Determines what identifier is used for reporting |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }





