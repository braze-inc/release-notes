# Multiple WhatsApp Business accounts and phone numbers

> You can add multiple WhatsApp Business accounts and subscription groups (and phone numbers) to each workspace. <br><br>Each subscription group is connected to one unique phone number within a workspace, so you can't connect the same phone number to multiple subscription groups in the same workspace or connect multiple phone numbers to a subscription group.

**Note:**


Meta separates the phone number (WhatsApp account) from templates, billing, and webhooks (Messaging account). For an overview, see [WhatsApp accounts and Messaging accounts](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_accounts_and_messaging_accounts).



## Multiple WhatsApp Business accounts 

Having multiple WhatsApp Business accounts is useful if you want to send WhatsApp messages to users in a Braze workspace that has multiple brands. Each connection operates separately in WhatsApp and has its own Messaging account for templates, billing, and related settings.

Business accounts that are nested within the same Meta Business Manager will also share user access permission management and catalogs (not yet supported on Braze).

![Diagram of the Braze and WhatsApp ecosystem, showing how workspaces and WhatsApp Business accounts connect to each other: you can connect one subscription group to one phone number, multiple WhatsApp Business accounts to one workspace, and one workspace to multiple Meta Business Portfolios.](https://www.braze.com/docs/assets/img/whatsapp/whatsapp_braze_ecosystem.png?c48a73269371621db9598eb8dd726651) 

### Adding a WhatsApp Business account

You can add up to 10 WhatsApp Business accounts per workspace. The business accounts can be nested in different Meta Business Managers. To add an account:

1. Go to **Technology Partners** > **WhatsApp** and select **Add WhatsApp Business Account**. 

![WhatsApp Messaging Integration section with options to add a business account or add a subscription group and number.](https://www.braze.com/docs/assets/img/whatsapp/multiple_wabas.png?432027085b74a6da96800d095f97bb7e)

{: start="2"}
2. Go through the sign-up workflow. For a detailed step-by-step walkthrough, refer to [WhatsApp embedded signup](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

**Important:**


Any phone number you connect must meet [Meta's phone number requirements](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).



## Multiple subscription groups and phone numbers

You can add multiple [subscription groups](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) under the same WhatsApp Business account. Each subscription group is tied to one sending phone number, and each phone number appears as a separate WhatsApp chat to users.

Phone numbers on the same account can differ in display name, status, and quality rating. Shared scope varies:

- **Message templates:** Shared by every phone number on the same Messaging account. Not shared across Messaging accounts or providers.
- **Messaging limits:** Shared at the business portfolio level across providers on a number.
- **Throughput:** Shared at the phone-number level across providers on that number.

### Adding a subscription group and phone number

You can add up to 20 subscription groups (and sending phone numbers) per WhatsApp Business account. To add a subscription group and phone number:

1. Go to **Technology Partners** > **WhatsApp** and select **Add Subscription Group and Number**.

![WhatsApp Messaging Integration section with options to add a business account or add a subscription group and number.](https://www.braze.com/docs/assets/img/whatsapp/multiple_wabas.png?432027085b74a6da96800d095f97bb7e)

{: start="2"}
2. Go through the sign-up workflow. <br><br> In the **Select your WhatsApp Business Account** step, select your existing WhatsApp Business account and add a new phone number. The number must meet Meta's phone number requirements.

### Removing a subscription group and phone number 

1. Go **Audience** > **Subscriptions** and archive the subscription group.
2. Go to your Meta Business manager and delete the phone number.
