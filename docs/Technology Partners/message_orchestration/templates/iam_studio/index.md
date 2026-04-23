# IAM Studio

> [IAM Studio](https://www.inappmessage.com) is a no-code message personalization platform that allows you to create personalized, rich in-app experiences and deliver them through Braze.

_This integration is maintained by IAM Studio.*s._

## About the integration

With the Braze and IAM Studio integration, you can easily insert customizable in-app message templates into your Braze in-app messages, offering image replacement, text modification, deep link settings, custom attributes, and event settings. Using IAM Studio, you can reduce message production time and dedicate more time to content planning. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| IAM Studio account | A [IAM Studio account](https://www.inappmessage.com/register) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Use cases

- Encouraging the purchase of goods
- User information collection
- Increasing membership registration
- Coupon issuance information

## Integration

### Step 1: Choose a template

Choose an in-app message template you want to use from the in-app message template gallery

![The IAM Studio template gallery shows different templates such as "carousel slide modal", "simple icon modal", "modal full image", and more.](https://www.braze.com/docs/assets/img/iam_studio/iam_template_gallery.png?d301491375088b1f8cdf7ecfbc830b61)

### Step 2: Customize the template

First, customize the image, text, and button for your content. Be sure to connect **Deeplink** for the image and button.



![The IAM Studio UI showing the options to customize the image. These options include the image, image radius, and image dimmed.](https://www.braze.com/docs/assets/img/iam_studio/iam_customize_image.png?9f431536e71e5a0c679de03f23910435)


![The IAM Studio UI showing the options to customize the title and subtitle of your message. These options include text, formatting, and font.](https://www.braze.com/docs/assets/img/iam_studio/iam_customize_text.png?25b8829b1c3c01eb46ad6e83b2b110ba)


![The IAM Studio UI showing the options to customize the main, left and right button. These options include color, deep link, text, and formatting.](https://www.braze.com/docs/assets/img/iam_studio/iam_customize_button.png?913d6f615f3a6586b1283702ca497d2e)



Next, create your personalized in-app message by adding custom fonts and using Liquid tags. To enable logging and tracking, select **Log data and track user behavior**.



![The IAM Studio UI showing the options to add Liquid. These options include making personalized sentence.](https://www.braze.com/docs/assets/img/iam_studio/iam_custom_font.png?40ec911c58a199974fce54639e153615)


![The IAM Studio UI showing the options to customize event/attribute logging. These options include that user behavior log.](https://www.braze.com/docs/assets/img/iam_studio/iam_liquid.png?6200e12e0abb1ca4f5f1a57a541e6808)


![The IAM Studio UI showing the options to customize font. These options include that user can customize font style.](https://www.braze.com/docs/assets/img/iam_studio/iam_tracking_logging.png?e41095c0349da829c3ad7c273266bfa1)



### Step 3: Export the template

Once all editing has been completed, export the template by clicking **Export**. After exporting, the in-app message HTML code will be generated. Copy this code by clicking the **Copy code** button. 

![](https://www.braze.com/docs/assets/img/iam_studio/export_iam_code.png?29012e7725043fa9b60d9ab6749ee3a5){: style="max-width:45%;"}

### Step 4: Use code in Braze 

Navigate to Braze, and in your in-app message, paste the custom code in the **HTML Input** box. Make sure to test your message to check it is displaying correctly.

![](https://www.braze.com/docs/assets/img/iam_studio/braze_campaign_editor.png?93c2b494261969d3fa837421486fa4fd){: style="max-width:85%;"}


