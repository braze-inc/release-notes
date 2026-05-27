# Canvas context object

> When using one of the endpoints for triggering or scheduling a Canvas through the API, you may provide a map of keys and values to customize messages sent by the first steps of your Canvas, in the `context` namespace.

**Note:**


The context object has a maximum size limit of 50 KB.



## Object body

This object body contains an example request.

```json
"context": {"product_name" : "shoes", "product_price" : 79.99}
```


For example, you can include `"context": {"product_name" : "shoes", "product_price" : 79.99}` in your API request and then reference the word "shoes" in your message by adding ```{{context.${product_name}}}``` to the message template.

