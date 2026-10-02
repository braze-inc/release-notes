# Webhook object

> The `webhook` object allows you to modify or create webhook messages via our [messaging endpoints](https://www.braze.com/docs/api/endpoints/messaging).

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string or JSON object) payload Braze sends in the webhook request. Pass a JSON object, or a string that contains your payload. If you pass a string that includes JSON, escape quotes and backslashes so the outer messaging request remains valid JSON,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

As a best practice, Braze recommends providing an explicit value for `Content-Type` in the `request_headers` field for consistent and predictable behavior, as senders and servers may change over time. If you don't specify a value for the `Content-Type` header, the system infers a value from the request body.

## Example webhook object with a JSON body

The `body` field holds the payload of the outbound webhook. When that payload is JSON, you can pass it as a JSON object, or as a string that contains the same JSON.

Both of the following webhook objects send the same payload to `https://example.com/hooks/braze`:

### JSON object in `body`

Braze accepts a JSON object for `body` and serializes it before sending the webhook.

```json
{
  "url": "https://example.com/hooks/braze",
  "request_method": "POST",
  "request_headers": {
    "Content-Type": "application/json"
  },
  "body": {
    "user_id": "12345",
    "event": "purchase",
    "properties": {
      "product": "sneakers",
      "price": 99.99
    }
  }
}
```

### JSON string in `body`

If you supply `body` as a string, build the inner JSON first, then escape double quotes and backslashes so the outer messaging request remains valid JSON:

```json
{
  "user_id": "12345",
  "event": "purchase",
  "properties": {
    "product": "sneakers",
    "price": 99.99
  }
}
```

That object becomes this escaped string value for `body`:

```json
{
  "url": "https://example.com/hooks/braze",
  "request_method": "POST",
  "request_headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"user_id\":\"12345\",\"event\":\"purchase\",\"properties\":{\"product\":\"sneakers\",\"price\":99.99}}"
}
```

**Note:**


Arrays and other non-object, non-string values aren't valid for `body`. Pass an object or a string.


