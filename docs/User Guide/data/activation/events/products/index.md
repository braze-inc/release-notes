# Products

> The **Products** page in **Data Settings** lists the product IDs Braze recorded from [purchase events](https://www.braze.com/docs/user_guide/data/activation/events/purchase_events). Use this page to manage product IDs for targeting and triggering, and to blocklist or delete products you no longer need.

Go to **Data Settings** > **Products** to open the list of products in your workspace. From this page, you can:

- Search for products by name
    - Each product name corresponds to a purchase event `product_id`
- Filter by status (**Active** or **Blocklisted**)
- Add products before they appear from live purchase data
- Manage purchase properties for a product
- Blocklist, reactivate, or delete a product

## How products get populated

Products appear on the **Products** page in several ways:

| Source | How it works |
| --- | --- |
| Purchase events | When your app, site, or backend logs a purchase with a `product_id` through the SDK or the [`/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) endpoint, Braze adds that `product_id` to the Products list if it isn't already there. |
| Pre-population | You can add products in the dashboard before your engineering team finishes logging them, so the names are available in campaign and segment dropdowns. |
| API export | You can retrieve the paginated list of product IDs with the [Export product IDs](https://www.braze.com/docs/api/endpoints/export/purchases/get_list_product_id) endpoint. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="How products get populated" }

### Pre-populate products

1. Go to **Data Settings** > **Products**.
2. Select **Add products**.
3. Enter one or more product names, then save.

Product names are case-sensitive. When your team integrates purchase logging, use the exact same `product_id` strings or Braze will create separate products.

For the shared workflow across custom attributes, custom events, and products, see [Manage custom data](https://www.braze.com/docs/user_guide/data/activation/custom_data/managing_custom_data#pre-populate-custom-data).

## Limitations

| Limit | Details |
| --- | --- |
| Products per workspace | Braze stores up to 5,000 `product_id` values in the dashboard. |
| `product_id` length | Up to 255 characters. |
| Products per user profile | User profiles that accumulate more than 20,000 distinct product names in purchases may be blocked as spam. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Products page limits" }

**Tip:**


Follow [Product ID naming conventions](https://www.braze.com/docs/api/objects_filters/purchase_object#naming-conventions) and use simple product or category names instead of unique SKUs whenever possible. That keeps the products list manageable and makes segmentation and triggering clearer.



## Manage product properties

After a product exists, select **Manage properties** to:

- Add purchase properties for that product
- Blocklist individual product properties
- See which campaigns or Canvases use a property in a trigger event

## Blocklist or delete products

### Blocklist

Blocklisting stops Braze from processing new data for that product while your engineering team removes it from your app or website. Existing purchase data remains on profiles, but the product no longer appears in filters or graphs for new processing.

1. Go to **Data Settings** > **Products**.
2. Search for the product, then select it.
3. Select **Blocklist**.

You can reactivate a blocklisted product later from the same page. For permissions, effects on campaigns and Canvases, and broader blocklist guidance, see [Blocklist custom data](https://www.braze.com/docs/user_guide/data/activation/custom_data/blocklist_custom_data).

### Delete

You can delete a product from the actions menu when it isn't referenced by filters or triggers elsewhere in Braze. Deleted products can't be recovered. If the product is still referenced, Braze blocks deletion until those references are removed.

To stop your SDK or API from sending a `product_id`, either blocklist that product, or delete it and remove it from your integration.

## Related topics

<ul class="guide_tiles"><li><a href="/docs/user_guide/data/activation/events/purchase_events"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Purchase events</span></span></div></a></li><li><a href="/docs/api/objects_filters/purchase_object"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Purchase object</span></span></div></a></li><li><a href="/docs/user_guide/data/activation/custom_data/managing_custom_data"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Manage custom data</span></span></div></a></li><li><a href="/docs/user_guide/data/activation/custom_data/blocklist_custom_data"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Blocklist custom data</span></span></div></a></li><li><a href="/docs/api/endpoints/export/purchases/get_list_product_id"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Export product IDs</span></span></div></a></li></ul>
