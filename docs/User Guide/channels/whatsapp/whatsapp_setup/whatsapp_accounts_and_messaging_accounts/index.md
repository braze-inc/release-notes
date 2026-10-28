# WhatsApp accounts and Messaging accounts

> Meta organizes WhatsApp business messaging with two account types: a WhatsApp account for the phone number, and a Messaging account for templates, billing, webhooks, and analytics. This page explains how that model works with Braze.

## Account types

| Account type | What it holds |
| --- | --- |
| WhatsApp account | The business phone number |
| Messaging account | Templates, billing, webhook subscriptions, and analytics. Each provider on a number gets its own Messaging account. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp account types" }

## Share a phone number with Braze

To use an existing WhatsApp number with Braze, [share the WhatsApp account](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number) that holds the number through [Embedded Signup](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

When you share a number:

- The number stays on the WhatsApp account. Conversations and other providers remain in place unless you remove a provider's access.
- Braze gets its own Messaging account for that connection. Templates and billing for Braze stay in that Messaging account.
- Messaging limits (applies at the portfolio level) and throughput (applies at the phone-number level) are shared across providers on the number.

## What stays separate per provider

- **Templates:** Not shared across Messaging accounts. Recreate the templates you need in Braze. New templates usually need about two to four weeks of sending history before Meta treats them as fully established.
- **Billing:** Each provider's Messaging account is billed separately.
- **Webhooks and analytics:** Scoped to the Messaging account for that provider.

## Using one number with more than one provider or workspace {#using-one-number-with-more-than-one-provider-or-workspace}

### More than one provider

You can share the same WhatsApp account (and phone number) with Braze and another provider. Meta's thread control can separate traffic between different providers. It does not separate Messaging accounts that belong to the same provider.

### More than one Braze workspace

Braze treats each Messaging account as a separate WhatsApp connection, so the one-account-per-workspace rule still applies. You can connect the same phone number in more than one Braze workspace if each connection uses a different Messaging account.

Inbound messages go to every Braze workspace that shares that number. Braze can't tell which workspace you meant to reply from. Plan routing and response handling accordingly.

### If Braze loses Messaging account access {#if-braze-loses-messaging-account-access}

If someone removes Braze's access to your Messaging account in Meta, Braze isn't notified. Sends start failing with authorization errors. Braze eventually marks the number inactive, the Message Activity Log can show "WhatsApp messaging service has no sending numbers," and the number is hidden from the WhatsApp composer. See [Investigate WhatsApp send failures](https://www.braze.com/docs/user_guide/channels/whatsapp/send_failures#messaging-account-access-removed).

**Note:**


Meta's `waba_id` API field and existing IDs refer to the Messaging account ID. You may see "WhatsApp Business Account" or "WABA" in Meta Terms of Service, older screenshots, or platform labels—those names also refer to the Messaging account ID.



## Additional resources

<ul class="guide_tiles"><li><a href="https://developers.facebook.com/documentation/business-messaging/whatsapp/whatsapp-business-accounts"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Meta: WhatsApp accounts and Messaging accounts</span></span></div></a></li><li><a href="https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Meta: Updates to WhatsApp Business accounts</span></span></div></a></li><li><a href="https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/onboarding/"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Meta: Onboarding</span></span></div></a></li><li><a href="/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Use an existing WhatsApp phone number</span></span></div></a></li></ul>
