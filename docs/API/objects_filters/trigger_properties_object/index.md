# Trigger properties object

> When using one of the endpoints for sending a campaign with API-triggered delivery, you may provide a map of keys and values to customize your message.

If you make an API request that contains an object in `trigger_properties`, the values in that object can then be referenced in your message template under the `api_trigger_properties` namespace. For example, a request with the following could add the word `"shoes"` to a message by adding `{{api_trigger_properties.${product_name}}}`.

Note that while trigger properties can be templated into messages, they aren't automatically stored in the user profile by default.

**Note:**


The `trigger_properties` object and `api_trigger_properties.${product_name}` syntax is only supported in campaigns. To customize messages with keys and values from an API trigger request for Canvas, use the [Canvas entry properties object](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context/). The `trigger_properties` object has a maximum size limit of 50 KB.



## Object body

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"]
  }
}
```


