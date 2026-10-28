# Use an existing WhatsApp phone number

> If you already use a WhatsApp number with another provider, you don't need to move it. Share your WhatsApp account with Braze through Embedded Signup. Your number, conversations, and other providers stay in place. Templates and billing are separate for each provider, so recreate the templates you need in your Braze Messaging account.

## Prerequisites

Before you connect an existing number to Braze, confirm your phone number meets Meta's requirements:

- Your Meta Business account is verified.
- You can complete Meta's [Embedded Signup](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) flow with a Meta user who has permission to share the WhatsApp account with Braze.
- You understand that templates and billing stay separate per Messaging account. Recreate any templates you need to send from Braze.

**Note:**


Since September 23, 2026, Meta has begun [retiring the two-step verification PIN](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/onboarding/) for eligible numbers. Where that change applies, **WhatsApp Manager** no longer shows a **Two-step verification** tab, and there is no PIN to disable. Ownership verification with a one-time passcode (OTP) may still be required during Embedded Signup.



## Use a number that's already with another provider {#migrate-from-another-business-solution-provider}

If your WhatsApp phone number is already registered with another Business Solution Provider (BSP), share the WhatsApp account that holds that number with Braze. You don't need to remove the other provider for Braze to send on the number.

### Before you connect

- A phone number can stay available to more than one provider at a time. Sharing with Braze does not remove the current provider's access unless you later revoke that access in Meta.
- Templates aren't shared across Messaging accounts. Recreate the templates you need in your Braze Messaging account. Migrated or recreated templates start from a baseline quality rating; Meta's ramp-up typically takes about two to four weeks.
- Messaging limits (at the portfolio level) and throughput (at the phone-number level) are shared across providers on the same number.
- Review contracts and billing with your current provider. Message history may not transfer automatically.
- If you use separate support and marketing setups, see [Integrations, data, and reporting](https://www.braze.com/docs/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) and [Using one number with more than one provider or workspace](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_accounts_and_messaging_accounts#using-one-number-with-more-than-one-provider-or-workspace).

### Connection paths

| Current setup | Path |
| --- | --- |
| Number on another BSP; keep using that BSP and also send from Braze | Share the WhatsApp account with Braze through [Embedded Signup](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup). Recreate templates in your Braze Messaging account. |
| Number on another BSP; move sending fully to Braze | Share the WhatsApp account with Braze through Embedded Signup, then remove the other provider's access in Meta when you're ready. |
| Number on Braze native integration; move to Infobip billing | [BYO WhatsApp connector](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) (Infobip only) |
| Marketing on Braze and support on another provider | You can use separate numbers, or share one number across providers. For sharing behavior, see [Using one number with more than one provider or workspace](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_accounts_and_messaging_accounts#using-one-number-with-more-than-one-provider-or-workspace). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Connection paths for existing WhatsApp numbers" }

## Connect through Embedded Signup {#migrate-between-whatsapp-business-accounts}

1. In Braze, start the [Embedded Signup](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) flow from the WhatsApp partner page.
2. When Meta prompts you, select the business portfolio and WhatsApp account that already hold your phone number, then grant Braze access.
3. Select the phone number you want Braze to use.
4. Complete Meta's Embedded Signup workflow.

If Meta shows WhatsApp Business Account (WABA) labels, that may mean your business hasn't migrated to Meta's latest account model yet. Existing IDs and API field names such as `waba_id` continue to work. See [WhatsApp accounts and Messaging accounts](https://www.braze.com/docs/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_accounts_and_messaging_accounts).

## Development and production workspaces

Braze recommends separate Messaging accounts for development and production when possible:

- Use a dedicated test phone number in your sandbox or development workspace for integration testing.
- Keep your production phone number in your production workspace.
- If you need the same number in more than one workspace, connect it with a separate Messaging account in each workspace.
- Approve templates in the Messaging account tied to the workspace where you send. Template approvals apply per Messaging account.
