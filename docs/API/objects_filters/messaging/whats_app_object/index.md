# WhatsApp object

> The `whats_app` object allows you to modify or create WhatsApp messages via our [messaging endpoints](https://www.braze.com/docs/api/endpoints/messaging).

## WhatsApp object

```json
{
  "app_id": (required, string) see App Identifier,
  "subscription_group_id": (required, string) the ID of your subscription group,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "message_type": (required, string) the type of WhatsApp message being sent under the `message` key (template_message | text_response_message | text_image_response_message | quick_reply_response_message | list_response_message | flow_response_message | carousel_response_message),
  "message": (required, object) The message object that must include the required fields based on the selected `message_type`. Below are the specific message structures for each type. Refer to the relevant message type for the required fields and their format.
}
```

- [App identifier](https://www.braze.com/docs/api/identifier_types)

### Message Types

#### template_message

```json
{
  "template_name": (required, string) the WhatsApp template name for the message,
  "template_language_code": (required, string) the language code of the WhatsApp template for the message,
  "header_variables": (optional, header variables object) an object to specify header variable values for specified template_name, required if the header has variables; see object specification below,
  "body_variables": (optional, body variable object) an object to specify body variable values for specified template_name, required if the body has variables; see object specification below,
  "button_variables": (optional, button variables object) an object to specify button variable values for specified template_name, required if buttons have variables; see object specification below,
  "header_media_uri": (optional, string) URI to the header media, if the header is of type IMAGE in specified template_name. Only IMAGE and TEXT header types are supported by the messages/send API,
  "carousel_cards": (optional, array) an array of carousel card objects, required if the specified template_name is a carousel template; see object specification below
}
```

**Important:**


Media sends (documents, videos, and other media types) aren't supported by the `messages/send` API. Only `TEXT` and `IMAGE` header types are supported for template messages sent through the API. If your WhatsApp template uses a `DOCUMENT`, `VIDEO`, or other media type header, you can't send it using the `messages/send` API. Use the [Campaigns Triggered API](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) or the Braze dashboard to send templates with media headers. This applies to the template's main header only; carousel card media supports both image and video.



##### Carousel card object

Each carousel card fills one card of an approved carousel template, in order. The card at index `0` fills the template's first card.

```json
{
  "header_media_uri": (required, string) URI to the card's header media; must be Braze-hosted media,
  "header_media_type": (required, string) The type of the card's header media (image | video),
  "body_variables": (optional, body variables object) Values for the card's body variables, in the same format as the template-level body_variables,
  "button_variables": (optional, button variables object) Values for the card's button variables, in the same format as the template-level button_variables
}
```

##### Constraints

- `carousel_cards`: Must contain between 2 and 10 cards, matching the card count of the approved template.
- `header_media_uri`: Must refer to media hosted in the Braze media library.
- `header_media_type`: All cards must use the same media type, matching the approved template.

###### Example

```json
{
  "template_name": "weekly_picks",
  "template_language_code": "en",
  "body_variables": {
    "0": "Jane"
  },
  "carousel_cards": [
    {
      "header_media_uri": "https://braze-images.com/card1.png",
      "header_media_type": "image",
      "body_variables": {
        "0": "Runner X"
      }
    },
    {
      "header_media_uri": "https://braze-images.com/card2.png",
      "header_media_type": "image",
      "body_variables": {
        "0": "Trail Pro"
      },
      "button_variables": {
        "0": "/promo/123"
      }
    }
  ]
}
```

##### Header variables object

The `header_variables` object lets you specify values for header variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.

**Note:**


You can use `header_variables` only with templates that have TEXT-type headers. For IMAGE headers, use `header_media_uri` instead. DOCUMENT, VIDEO, and other media header types are not supported by the `messages/send` API.<br><br>

`header_image_uri` is used only for response message types (such as `quick_reply_response_message`), not template messages.



```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
Currently, only zero or one header variables can be specified.


###### Example

```json
{
  "0": "Check it out!"
}
```

##### Body variables object

The `body_variables` object lets you specify values for body variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.
```json
{
  "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

###### Example

```json
{
  "0": "Check it out!",
  "1": "It's pretty neat."
}
```

##### Button variables object

The `button_variables` object lets you specify values for button variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.

```json
{
  "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

Currently, only one button variable can be specified, which is the path component of a call-to-action URL. The variable index must match the CTA URL button index in the template. For example, if your CTA button is the second button in your template, use variable index "1".

###### Example

```json
{
  "1": "/marketing/promotion123"
}
```

### Response Messages

#### text_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "preview_url": (optional, boolean) whether WhatsApp should render a preview of links included in body
}
```

##### Example

```json
{
  "body": "Check out our new deals at https://braze.com",
  "preview_url": true
}
```

#### text_image_response_message

```json
{
  "image_uri": (required, string) the uri of the image to send,
  "caption": (optional, string) the caption for the image being sent
}
```

##### Example

```json
{
  "image_uri": "https://braze.com/promotion.jpg",
  "caption": "This won't last for long, check it out!"
}
```

#### quick_reply_response_message

```json
{
  "body": (required, string) the body of the message to send,
  "header_image_uri": (optional, string) the URI of the image to send as the message header (only valid if header_text not present),
  "header_text": (optional, string) the text to send as the message header (only valid if header_image_uri not present),
  "footer": (optional, string) the footer of the message to send,
  "buttons": (required, array) array of Button objects. Will render in message based on order in array.
}
```

##### Button object

```json
{
  "text": (required, string) the text of the button
}
```

###### Example

```json
{
  "body": "Want to keep hearing from us?",
  "buttons": [
    {
      "text": "Yes!"
    },
    {
      "text": "No thanks"
    }
  ]
}
```

#### list_response_message

The `list_response_message` type allows you to send a list-based message in WhatsApp. This message type includes a list of items that the recipient can interact with.

```json
{
  "header": (optional, string) the header of the message to send,
  "body": (required, string) the body of the message to send,
  "footer": (optional, string) the footer of the message to send,
  "list": (required, object) the list object that contains:
    "list_button_text": (required, string) the text that will appear on the list button,
    "list_sections": (required, array) an array of List Section Objects
}
```

#### List Section Object

```json
{
  "section_title": (required, string) The title of the section,
  "list_rows": (required, array) An array of List Row Objects
}
```

#### List Row Object

```json
{
  "row_title": (required, string) The title of the row,
  "row_description": (optional, string) The description for the row
}
```

##### Constraints

- `list_sections`: Must have at least one section.
- `list_rows`: A maximum of 10 rows can be included across all sections.
- `row_description`: Optional for each row.

##### Example

```json
{
  "body": "Here is a list of options to choose from:",
  "list": {
    "list_button_text": "Choose an option",
    "list_sections": [
      {
        "section_title": "Section 1",
        "list_rows": [
          {
            "row_title": "Option 1"
          },
          {
            "row_title": "Option 2",
            "row_description": "Description for Option 2"
          }
        ]
      },
      {
        "section_title": "Section 2",
        "list_rows": [
          {
            "row_title": "Option 3"
          },
          {
            "row_title": "Option 4"
          },
          {
            "row_title": "Option 5"
          }
        ]
      }
    ]
  }
}
```

#### flow_response_message

The `flow_response_message` type allows you to send a flow-based message in WhatsApp. This message type includes an interactive flow that the recipient can complete.

```json
{
  "header_text": (optional, string) the header text of the message to send,
  "body": (required, string) the body of the message to send,
  "footer": (optional, string) the footer of the message to send,
  "flow_button": (required, object) the flow button object that contains:
    "caption": (required, string) the text that will appear on the flow button,
    "flow_id": (required, string) the unique identifier of the WhatsApp Flow,
  "generate_custom_attribute": (optional, boolean) whether to save flow response on the user profile and generate a custom attribute upon responding to this flow message
}
```

##### Flow Button Object

```json
{
  "caption": (required, string) The text displayed on the button,
  "flow_id": (required, string) The ID of the flow
}
```

##### Constraints

- `flow_button`: Must include both `caption` and `flow_id`.
- `caption`: Maximum 20 characters.
- `flow_id`: Must be a valid published Flow ID.

##### Example

```json
{
  "body": "Please complete your order details",
  "flow_button": {
    "caption": "Start Order",
    "flow_id": "594425479261596"
  },
  "generate_custom_attribute": true
}
```

#### carousel_response_message

The `carousel_response_message` type allows you to send an interactive carousel of media cards that users can swipe through as a response message. Each card has media, optional body text, and either quick reply buttons or a website button.

```json
{
  "body": (required, string) the body of the message to send,
  "carousel_button_type": (required, string) the button type used by every card (quick_reply | url),
  "cards": (required, array) an array of Card objects. Cards render in the carousel in array order.
}
```

##### Card object

```json
{
  "media_uri": (required, string) the URI of the card's media,
  "media_type": (required, string) the type of the card's media (image | video),
  "body_text": (optional, string) the body text of the card,
  "buttons": (required for quick_reply, array) an array of button label strings,
  "cta_url_button": (required for url, object) the website button object that contains:
    "display_text": (required, string) the text displayed on the button,
    "url": (required, string) the URL the button opens
}
```

##### Constraints

- `cards`: Must contain between 2 and 10 cards.
- `media_type`: All cards must use the same media type.
- `body_text`: Maximum 160 characters per card.
- `buttons`: For `quick_reply`, every card must have the same number of buttons, with a maximum of two per card.
- `cta_url_button`: For `url`, every card must include a `cta_url_button`.

##### Example with quick reply buttons

```json
{
  "body": "Check out this week's picks!",
  "carousel_button_type": "quick_reply",
  "cards": [
    {
      "media_uri": "https://example.com/card1.png",
      "media_type": "image",
      "body_text": "Runner X - now 20% off",
      "buttons": ["Shop now", "Not for me"]
    },
    {
      "media_uri": "https://example.com/card2.png",
      "media_type": "image",
      "body_text": "Trail Pro - back in stock",
      "buttons": ["Shop now", "Not for me"]
    }
  ]
}
```

##### Example with website buttons

```json
{
  "body": "Check out this week's picks!",
  "carousel_button_type": "url",
  "cards": [
    {
      "media_uri": "https://example.com/card1.png",
      "media_type": "image",
      "body_text": "Runner X - now 20% off",
      "cta_url_button": {
        "display_text": "Visit",
        "url": "https://example.com/runner-x"
      }
    },
    {
      "media_uri": "https://example.com/card2.png",
      "media_type": "image",
      "body_text": "Trail Pro - back in stock",
      "cta_url_button": {
        "display_text": "Visit",
        "url": "https://example.com/trail-pro"
      }
    }
  ]
}
```
