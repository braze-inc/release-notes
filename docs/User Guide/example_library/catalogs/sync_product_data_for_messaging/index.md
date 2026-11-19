# Sync product data to catalogs for messaging

> Keep product names, images, and inventory in a Braze catalog. Transactional, abandoned-cart, and back-in-stock messages stay current without calling an external API at send time.

## About this example

PantsLabyrinth, a fictional clothing retailer, stores product data in Databricks. Marketing needs item names, images, and stock levels in Braze for:

- Checkout and order confirmation messages that include purchased items
- Abandoned-cart reminders that show products left in the cart
- Back-in-stock alerts when a size-level SKU returns to inventory

This example syncs product rows into a Braze catalog with [Cloud Data Ingestion (CDI) for catalogs](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/). It personalizes messages with [catalog Liquid](https://www.braze.com/docs/user_guide/data/activation/catalogs/use/) and triggers [back-in-stock notifications](https://www.braze.com/docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) from custom events. The same catalog can also support [price drop notifications](https://www.braze.com/docs/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/).

## Considerations

- Design the catalog `id` to match the product identifier on your custom events and purchase or cart payloads. For back-in-stock alerts by size, use a size-level SKU as the catalog `id`, not only a style-level product ID.
- Sync only the fields your messages and triggers need. Extra columns increase [catalog storage](https://www.braze.com/docs/user_guide/data/activation/catalogs/create/#tiers) usage.
- Create or update the catalog schema in Braze before you change columns in the warehouse sync. Pause or avoid overlapping syncs while you change the schema.
- A subscription lasts 90 days, or until Braze sends the alert, whichever comes first. After the alert, Braze removes the subscription. To get another alert, the shopper subscribes again.
- Braze triggers back-in-stock and price drop notifications for up to 50,000 catalog item updates per day for your company, across all catalogs. To raise this limit, contact your Braze account manager.
- Each catalog supports up to 100 million active subscriptions. Braze skips subscribe events after a catalog reaches that cap.
- Back-in-stock and price drop subscriptions share one subscribe custom event and an optional unsubscribe event. Set `type` to an array of `"back_in_stock"`, `"price_drop"`, or both. If you omit `type`, Braze subscribes the user to back-in-stock.
- A user can subscribe to back-in-stock only when the item already exists in the catalog and its inventory field is exactly `0`. Braze drops the subscribe event when the item is missing, or when the inventory value is blank. When that field updates from `0` to a number greater than `0`, Braze can notify subscribed users.
- Prefer catalogs over [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/) when you want inventory-driven triggers in Braze and predictable scaling at send time. Connected Content retrieves product data from your endpoint at send time and requires you to own subscription and inventory-trigger logic yourself.
- This example covers the data and trigger setup. Build campaign or Canvas copy, audience, and channel settings separately for each use case.

**Warning:**


When a sync passes the daily trigger limit, Braze drops triggers for the remaining items. Those shoppers stay subscribed until the subscription expires. A later update to the same item sends no alert, because the stored inventory is no longer `0`.

This example stores one catalog item per size and color, so a large restock can reach the limit. Spread a large restock over more than one day.



## Setup

This example assumes:

| Asset | Details |
| --- | --- |
| Warehouse | Databricks table or view of product inventory |
| Catalog | `pantslabyrinth_products` with columns such as `id`, `name`, `size`, `color`, `image_url`, `price`, and `stock_quantity` |
| Custom events | `subscribed_to_product_updates` (subscribe) and optional `unsubscribed_from_product_updates` (unsubscribe) |
| Event properties | `product_id` (string matching catalog `id`), `catalog_name`, `type` (array) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Setup assumptions" }

### Step 1: Design the product catalog schema

1. List the fields each use case needs (for example, `name`, `image_url`, `price`, and `stock_quantity`).
2. Choose a stable catalog `id`. For PantsLabyrinth back-in-stock by size, each row is one size-color SKU:

| `id` | `size` | `color` | `name` | `image_url` | `stock_quantity` |
| --- | --- | --- | --- | --- | --- |
| `trail-runner-s-grey` | `S` | `grey` | `Trail Runner` | `https://cdn.pantslabyrinth.example/trail-runner-grey.jpg` | `0` |
| `trail-runner-m-grey` | `M` | `grey` | `Trail Runner` | `https://cdn.pantslabyrinth.example/trail-runner-grey.jpg` | `130` |
| `trail-runner-l-grey` | `L` | `grey` | `Trail Runner` | `https://cdn.pantslabyrinth.example/trail-runner-grey.jpg` | `243` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 aria-label="Example product catalog rows" }

{: start="3"}
3. Confirm your checkout, cart, and subscribe events send the same identifier you store as catalog `id`.

### Step 2: Create the catalog in Braze

You can create `pantslabyrinth_products` now, or create it in Step 4 when you set up the sync. If you create it during sync setup, Braze asks you to set a data type for each field.

To create the catalog now:

1. Go to **Data Settings** > **Catalogs** and create `pantslabyrinth_products`.
2. Add the fields from Step 1. Set `stock_quantity` (or your inventory column) to a number type so you can use it for back-in-stock.
3. Optionally add a seed item so you can test Liquid before the first CDI sync.

For field types and limits, see [Create a catalog](https://www.braze.com/docs/user_guide/data/activation/catalogs/create/).

### Step 3: Build a Databricks source for CDI

Create a table or view with `UPDATED_AT`, `ID`, `PAYLOAD`, and optional `DELETED`. Point the view at your product table and map each product field into `PAYLOAD`.

Use the following view shape, and adapt the names to your Databricks schema:

```sql
CREATE VIEW IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (
  SELECT
    last_updated AS UPDATED_AT,
    sku_id AS ID,
    TO_JSON(
      STRUCT(
        name,
        size,
        color,
        image_url,
        price,
        stock_quantity
      )
    ) AS PAYLOAD
  FROM BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1
);
```

For more information about the Databricks warehouse steps, see [Sync and delete catalog data](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/?tab=databricks).

**Note:**


You can update the same catalog with the [Catalogs REST API](https://www.braze.com/docs/api/endpoints/catalogs/) instead of CDI when a warehouse sync isn't available. Manage create, update, and delete logic in your service.



### Step 4: Connect Cloud Data Ingestion

1. In Braze, create a Databricks CDI integration and select the **Catalogs** sync type.
2. Enter a **Sync name** to identify the sync. Select the catalog separately in the next step.
3. For **Catalog to update**, select **Use existing catalog**, then select `pantslabyrinth_products`, or select **Create new catalog** and enter `pantslabyrinth_products` as the **Catalog name**.
4. Grant the Braze credentials access to the source table or view. For Databricks, select **OAuth M2M** (a service principal). The dashboard tags it **Recommended by provider**. **Personal Access Token** is the default.
5. Set a sync schedule that matches how often product and inventory data changes.
6. Test the connection, save the sync, and confirm sample rows appear in the catalog.

For more information, see [Sync and delete catalog data](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) and [Cloud Data Ingestion integrations](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks).

### Step 5: Personalize checkout and abandoned-cart messages

Pass product IDs on the event or user attribute that represents the purchase or cart, then look up catalog fields with Liquid.

The following Liquid looks up one product ID from an event property:


```liquid
{% catalog_items pantslabyrinth_products {{event_properties.${product_id}}} %}
{{ items[0].name }} in {{ items[0].size }} / {{ items[0].color }}
{% if items[0].image_url != blank %}
  <img src="{{ items[0].image_url }}" alt="{{ items[0].name }}">
{% endif %}
```


For multiple IDs, pass each ID into `catalog_items`. Each tag reads up to three item IDs, and Braze ignores any extra IDs. Use another `catalog_items` tag for more items, or combine catalog lookups with your cart attribute pattern. For more information, see [Using catalogs](https://www.braze.com/docs/user_guide/data/activation/catalogs/use/) and [Match catalog items to a custom attribute array](https://www.braze.com/docs/user_guide/example_library/catalogs/match_catalog_items_to_attribute_array/).

### Step 6: Enable back-in-stock notifications

1. Go to `pantslabyrinth_products` and select the **Settings** tab.
2. Turn on **Back in stock**.
3. Configure the global subscription settings if prompted:
   - **Fallback Catalog** (used when `catalog_name` is omitted on the event)
   - **Custom event for subscriptions** (for example, `subscribed_to_product_updates`)
   - **Custom event for unsubscribing** (optional)
   - **Item ID event property** (for example, `product_id`) that maps to the catalog `id`
4. Set notification rules (notify all subscribed users, or rate-limited batches).
5. Set **Inventory field in catalog** to `stock_quantity`.
6. Save settings.

Optionally turn on **Price drop** on the same catalog. Select a number field, such as `price`, as the **Price field**. Then set the **Price drop rule**:

- **Operator:** **is greater than** or **is greater than or equal to**
- **Value:** how much the price must change before Braze sends a notification
- **Unit:** **Percent of original price** or **Currency amount**

If catalog settings don't include **Price drop**, contact your Braze account manager. For the full setup, see [Price drop notifications](https://www.braze.com/docs/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/). Subscribe users to both notification types with one event by including both values in `type`.

### Step 7: Subscribe users with a custom event

Log the subscribe event when a shopper requests an alert (for example, from a product detail page). Send it after the item exists in the catalog and its inventory is exactly `0`. Include the catalog item ID as a string, the catalog name, and a `type` array.



```json
{
  "events": [
    {
      "external_id": "user_123",
      "name": "subscribed_to_product_updates",
      "time": "2026-02-17T10:00:00Z",
      "properties": {
        "product_id": "trail-runner-s-grey",
        "catalog_name": "pantslabyrinth_products",
        "type": ["back_in_stock"]
      }
    }
  ]
}
```


```javascript
braze.logCustomEvent("subscribed_to_product_updates", {
  product_id: "trail-runner-s-grey",
  catalog_name: "pantslabyrinth_products",
  type: ["back_in_stock"]
});
```



Configure the **Item ID event property** in catalog settings to `product_id` so it matches this payload. If you use `id` instead, align the property name in both the event and the catalog settings.

### Step 8: Enter users into a Canvas when stock returns

1. Create an action-based Canvas.
2. Set the entry trigger to **Back in stock** and select `pantslabyrinth_products`.
3. In the message, template the item that triggered the update:


```liquid
{% catalog_items pantslabyrinth_products {{context.${catalog_update}.item_id}} %}
{{ items[0].name }} is back in stock in size {{ items[0].size }}.
```


`{{context.${catalog_update}.previous_value}}` and `{{context.${catalog_update}.new_value}}` expose the inventory values before and after the update. For more information, see [Using back-in-stock notifications in a Canvas](https://www.braze.com/docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#using-back-in-stock-notifications-in-a-canvas).

You can also start from the Braze [Back in stock Canvas template](https://www.braze.com/docs/user_guide/messaging/templates/canvas_templates/braze_templates/back_in_stock/).

After Braze notifies a user, it removes that subscription. The shopper subscribes again to get another alert if the item sells out again.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/data/activation/catalogs"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Catalogs</span></span></div></a></li><li><a href="/docs/user_guide/data/activation/catalogs/use"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Using catalogs</span></span></div></a></li><li><a href="/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Sync and delete catalog data</span></span></div></a></li><li><a href="/docs/user_guide/data/unification/cloud_ingestion/integrations"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Cloud Data Ingestion integrations</span></span></div></a></li><li><a href="/docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Back-in-stock notifications</span></span></div></a></li><li><a href="/docs/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Price drop notifications</span></span></div></a></li><li><a href="/docs/user_guide/messaging/templates/canvas_templates/braze_templates/back_in_stock"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Back in stock Canvas template</span></span></div></a></li><li><a href="/docs/user_guide/example_library/catalogs/match_catalog_items_to_attribute_array"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Match catalog items to a custom attribute array</span></span></div></a></li></ul>
