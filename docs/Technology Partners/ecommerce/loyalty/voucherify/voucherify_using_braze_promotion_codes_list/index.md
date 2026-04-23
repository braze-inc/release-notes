# Voucherify and Braze promotion codes list

> In addition to the Connected Content and custom attributes, you can share Voucherify codes using the Braze promo codes snippet. First, export codes from Voucherify, import codes to Braze, and add an email code snippet to pull codes from the promotion list. 

_This integration is maintained by Voucherify._

## Step 1: Export unique codes from Voucherify

In Voucherify, navigate to your Voucherify campaign. Next, select **Export to CSV** and edit the CSV file and remove the column's name to leave only the list of codes.

![](https://www.braze.com/docs/assets/img/voucherify/voucherify_promotion_export_codes.png?9c8899729b2b4ea87f2da3dd0524cd6f){: style="margin-top:15px;"}

## Step 2: Create a promotion codes list

Go to **Data Settings** > **Promotion Codes** and click **Create Promotion Code List**.

You can use the Voucherify campaign name to name the list and check data consistency.

![](https://www.braze.com/docs/assets/img/voucherify/voucherify_promotion_code_list.png?c2b791bf0ee952d149d9e0d8be01fea1){: style="max-width:50%;"}

Next, add the code snippet that refers to the codes from the list; it will be populated with a unique code when the message is sent.

### Additional settings

You can also set attributes for codes such as List Expiration and Threshold Alerts; however, note that Voucherify manages the logic behind your codes regardless of list settings.

![List expiration](https://www.braze.com/docs/assets/img/voucherify/voucherify_promotion_list_expiration.png?992970d21d72a41add79804496844e48)

## Step 3: Upload CSV file

Upload the CSV file with Voucherify codes.

![](https://www.braze.com/docs/assets/img/voucherify/voucherify_promotion_import_codes.png?9aa03744709f41184b08b0a281a4ad7f)

Confirm that the list only contains codes (not column header) and click **Start Upload**. When the import is done, click **Save List** to confirm the list details.

![](https://www.braze.com/docs/assets/img/voucherify/voucherify_promotion_upload_csv.png?af886fe7ef4c18f70de89ae4dcb52cad){: style="max-width:50%;"}

## Step 4: Use Code Snippet in Braze campaigns

To use codes from the list in a Braze campaign, Copy Snippet and add it to the email body.

![](https://www.braze.com/docs/assets/img/voucherify/voucherify_promotion_code_snippet.png?faa1974096e8d9abc4430da00d9f4c7e){: style="max-width:50%;"}

Add the code snippet to display a code from the list.

![](https://www.braze.com/docs/assets/img/voucherify/voucherify_promotion_liquid_email.png?be4fb1fc461a9d5761585a2b53ee675d)

Once the message with the code is sent, the same code won't be used again.

