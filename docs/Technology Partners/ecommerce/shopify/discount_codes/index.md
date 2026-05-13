# Send unique discount codes through Shopify

> This community-submitted use case shows how to use Braze [promotion codes](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/) with the Shopify Bulk Discount Code Bot to generate unique discount codes for your campaigns and Canvases. Unique discount codes help avoid the exploitation of generic promotion codes.

**Important:**


This is a community-submitted integration and isn’t directly supported by Braze. The Bulk Discount Code Bot is directly supported by Shopify. Only Braze promotion codes are supported by Braze. 



## Requirements

| Requirement | Description |
| --- | --- |
| Set up a Shopify store | Confirm you've already [set up a Shopify store with Braze](https://www.braze.com/docs/shopify_overview/). |
| Install the Bulk Discount Code Bot app | Download the [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) app in the Shopify app store. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Generating unique discount codes

### Step 1: Configure your discount codes

Use the Bulk Discount Code Bot to configure your discount codes based on the number of codes to generate, code length, discount value, and more.

![The configuration options for a discount set.][1]

### Step 2: Export your codes

Find your discount set in the Bulk Discount Code Bot's search bar, then select **Export Codes** > **Download Codes** to download a CSV file to your Downloads folder.

![Search bar with a dropdown displaying the discount set and a row of buttons to select from.][2]{: style="max-width:70%;"}

In the CSV file, delete row 1 to remove the column header “Promo”. This will prevent "Promo" from becoming a discount code in Braze.

![A flowchart showing the removal of the row header "Promo" in a CSV file.][3]{: style="max-width:60%;"}

### Step 3: Add your discount codes to Braze

In Braze, go to **Data Settings** > **Promotion Codes** > **Create Promotion Code List** and [configure your discount codes list](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/#creating-a-promotion-code-list). Make sure you match the expiration date that was configured by the Bulk Discounts Code Bot.

Then, upload your CSV file and select **Save List**.

### Step 4: Add your discount codes to a Braze campaign or Canvas step

If you want to use your unique discount codes in a single-send campaign, or you don't mind users receiving multiple unique codes across different campaigns or Canvas steps, copy the code's Liquid snippet from the promotion codes list you saved.

![A Liquid code snippet with a button copy it.][4]{: style="max-width:60%;"}

Paste the Liquid snippet into a campaign or Canvas step. 

![A GIF showing the Liquid snippet being added to a Canvas step.][5]

If you want users to receive a single unique discount code no matter how many times the discount code is referenced in campaigns or Canvases, create a [User Update](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/user_update/) step directly before the first Message step that assigns the discount code to a custom attribute, like "Promo Code".

**Tip:**


You can also [create a custom attribute](https://www.braze.com/docs/user_guide/data/activation/attributes/custom_attributes/) by going to **Data Settings** > **Custom Attributes**.



In the User Update step, do the following for each field:
- **Attribute Name:** Select **Promo Code**.
- **Action:** Select **Update**.
- **Key Value:** Paste the Liquid code snippet.

![A User Update step that updates a "Promo Code" attribute with the Liquid snippet.][6]

Now, you can add the custom attribute `{{custom_attribute.${Promo Code}}}` to any message, and the discount code will be templated in.

## Discount code behavior

**Multichannel campaign or Canvas step**



When a discount code snippet is used in a multichannel campaign or Canvas step, users always receive a unique code. If a user is eligible to receive a code through more than one channel, they'll receive the same code through each channel. In other words, an eligible user would only receive one code across all the messages sent by that campaign or Canvas step.




**Different Canvas steps or separate campaigns**



When a discount code is referenced by multiple steps in the same Canvas or by separate campaigns, an eligible user will receive multiple unique promotion codes (one code for each Canvas step or campaign).




[1]: /docs/assets/img/Shopify/configure_discount_codes.png?60e48b6004c54a4315c0f99359648b58
[2]: /docs/assets/img/Shopify/export_discount_codes.png?246f9f43cdcf09e091fac9e3d04cb2a3
[3]: /docs/assets/img/Shopify/edited_codes_csv.png?b24894f0cb40b306879211942af11805
[4]: /docs/assets/img/Shopify/liquid_code_snippet.png?fae29377bc4d4e646d2a30d27a908a41
[5]: /docs/assets/img/Shopify/liquid_promo_code.gif?3dc1d2e66014c58bb882252ce1a7be12
[6]: /docs/assets/img/Shopify/user_update_step.png?3b414d45bc94722d8f7bb0245cdc28b2