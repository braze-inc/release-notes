# Shopify order metafields

> With the [Shopify standard integration](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_standard_integration/#add-order-metafields-to-order-events), you can add selected order metafields to order events. Order metafields hold your own data about an order, such as a gift note or fulfillment preference.

You can select up to 20 order metafield definitions. Braze writes them onto supported Shopify order events so you can use them to segment and personalize.

## How order metafields appear on events

Each selected metafield is added to the event's `metadata` object as `<namespace>_<key>`, next to fields such as `metadata.tags`. For example, the Shopify definition `custom.gift_note` appears as `metadata.custom_gift_note`:

```json
{
  "metadata": {
    "order_number": "1234",
    "tags": ["heavy", "heavy2"],
    "custom_gift_note": "Happy birthday!"
  }
}
```

Order tags are unchanged; Braze still sends all tags on the event. Empty metafield values are omitted.

## Supported order metafield types

Only definitions with the following types appear in the picker. References, files, JSON, money, and rating aren't offered.

| Shopify type | Stored on the event as |
| --- | --- |
| Single line text, Multi-line text, Color, URL, ID | String |
| Integer | Integer |
| Decimal | Number |
| True or false | Boolean |
| Date, Date and time | ISO 8601 string in UTC. A date with no time lands at midnight UTC. |
| List of single line text, dates, dates and times, colors, IDs, or URLs | Array of strings |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported order metafield types" }

Braze omits a value from the event when:

- A string value, or an item in a list, is longer than 255 characters.
- A value can't be converted to the definition's type, for example text in an integer field.
- The key (`<namespace>_<key>`) is longer than 255 characters or contains `$` or `.`.
- The key collides with a property Braze already writes on the event, such as `order_number` or [Shopify Markets](https://www.braze.com/docs/partners/ecommerce/shopify/shopify_markets/) fields.

## Supported events

These events include the selected order metafields in `metadata`:

- Order placed (`ecommerce.order_placed`)
- Order cancelled (`ecommerce.order_cancelled`)
- `shopify_paid_order`
- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`

Order refunded (`ecommerce.order_refunded`) and checkout events don't carry order metafields.

## When Braze includes order metafields

| Source | Description |
| --- | --- |
| Shopify order webhooks | The value is a snapshot of the metafield when Shopify sends the order webhook. Events aren't rewritten after they're sent. |
| Historical backfill | If you select order metafields during initial setup and historical backfill is on, backfilled orders include the selected metafields. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="When order metafield values sync" }

Changing the selection applies only to orders that arrive after the change. There is no re-sync of past orders.

## Change or remove metafields

1. On the integration page, select **Edit settings**.
2. In the **Track Shopify data** step, open **Show additional order event settings**.
3. Update **Add order metafields to order events**. Clearing the checkbox clears the selection.

If you delete a definition in Shopify, Braze removes it from your selection automatically. Events already sent keep their values.

## Segmentation and personalization

Order metafield values are event properties under `metadata`, the same place as tags, so you can use them the same way you use `metadata.tags` today. For example, `{{event_properties.${metadata}.custom_gift_note}}` returns `Happy birthday!` for the `custom.gift_note` example in this article.
