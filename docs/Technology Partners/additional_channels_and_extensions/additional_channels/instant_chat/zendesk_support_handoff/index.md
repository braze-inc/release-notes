# Zendesk Support Handoff

> [Zendesk](https://www.zendesk.com/) is a customer service platform for omnichannel support. With this integration, your Braze Conversational AI agent can hand a live conversation to a human support agent in Zendesk when it needs to. After the handoff, a person takes over in the Zendesk Agent Workspace, and messages flow both ways until the agent closes the conversation.




**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





## About the integration

This integration runs on [Sunshine Conversations](https://docs.smooch.io/), Zendesk's messaging platform. You configure a few settings in Zendesk, then connect in Braze. Braze creates the messaging integration and webhook in your Zendesk account, so you don't need to build those on the Zendesk side beyond creating an API key.

Handoff is channel-agnostic. It works with all [Conversational Agents](https://www.braze.com/docs/user_guide/brazeai/agents/conversational_agents) channels—Web, SMS, RCS, and WhatsApp. After a handoff, agent replies return on the same channel the session started on.

Each workspace supports one Zendesk Support Handoff integration. Reconnecting with a different subdomain replaces the existing integration.

For Zendesk ticket creation and sync through Braze webhooks, see [Zendesk](https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/support/zendesk). For two-way SMS with Zendesk Chat, see [Zendesk Chat](https://www.braze.com/docs/partners/additional_channels_and_extensions/additional_channels/instant_chat/zendesk_chat).

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| Zendesk account with Agent Workspace and messaging | A Zendesk account with Agent Workspace and messaging (Sunshine Conversations) enabled. Most Zendesk messaging accounts already have this. |
| Multi-conversations enabled | Braze checks this during setup and can't enable it for you. After you turn multi-conversations on in Zendesk, you can't turn it back off. See Zendesk's guide to [allowing multiple conversations for your end users](https://support.zendesk.com/hc/en-us/articles/8008427696410-Allowing-multiple-conversations-for-your-end-users). |
| Conversations API key | Create a Conversations API key in Zendesk Admin Center. You need the **App ID**, **Key ID**, and **Secret** from the dialog (shown only once). See Zendesk's guide to [using Conversations API keys](https://support.zendesk.com/hc/en-us/articles/4576088682266-Using-the-Conversations-API-keys). |
| Zendesk subdomain | The subdomain from your Zendesk URL. For example, use `acme` for `acme.zendesk.com`. |
| Braze Technology Partners permission | Workspace permission to view and connect Technology Partners. See [Edit Technology Partners](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions). |
| Support handoff enabled | Support handoff must be enabled for your workspace. Contact your Braze account manager if you don't see the Zendesk connection options. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Use cases

- Escalate Conversational AI chats to a live Zendesk agent when the user asks for a human, or when the agent can't resolve the request.
- Keep the conversation in one thread so the Zendesk agent sees prior context and can reply in the Agent Workspace.
- Continue the conversation on Web, SMS, RCS, or WhatsApp—whichever channel the session started on—until the Zendesk agent closes it.

## Integrating Zendesk Support Handoff

Multi-conversations and the Conversations API key are independent in Zendesk, so you can complete those steps in either order.

### Step 1: Set up Zendesk

1. Confirm that Agent Workspace with messaging (Sunshine Conversations) is enabled in your Zendesk account.
2. Turn on [multi-conversations](https://support.zendesk.com/hc/en-us/articles/8008427696410-Allowing-multiple-conversations-for-your-end-users) for your end users.
3. In Zendesk Admin Center, go to **Apps and integrations** > **APIs** > **Conversations API**, then select **Create API key**.
4. Copy the **App ID**, **Key ID**, and **Secret**. Zendesk shows these values only once.

You don't need to create an integration or webhook in Zendesk. Braze sets those up when you connect.

### Step 2: Connect in Braze

You'll enter four values. Three come from the Conversations API key dialog in Step 1:

| Value | Source |
| --- | --- |
| **Zendesk subdomain** | The subdomain from your Zendesk URL. For example, use `acme` for `acme.zendesk.com`. |
| **Sunshine Conversations app ID** | The **App ID** from your Conversations API key. |
| **API key ID** | The **Key ID** from your Conversations API key. |
| **API key secret** | The **Secret** from your Conversations API key. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Connection values" }

Then:

1. In Braze, go to **Partner Integrations** > **Technology Partners**, then select **Zendesk**.
2. Enter the four values and select **Connect**.

Braze verifies the connection, confirms multi-conversations is on, and creates a dedicated Braze integration and webhook in your Sunshine app. Your API credentials are stored encrypted. Invalid credentials fail at connect time.

To confirm the connection:

- In Braze, the Zendesk integration panel shows a green **Connected** status.
- In Zendesk, go to Admin Center > **Apps and integrations** > **Conversations integrations**. You should see a Braze integration that Braze added when you connected.

### Step 3: Turn on handoff in Braze

Connecting Zendesk doesn't make the agent hand off on its own. In your Conversational Agents settings, set your handoff guidance—the plain-language rules for when the agent should escalate to a human.

Without handoff guidance, the agent isn't offered the escalate-to-support tool, so it won't hand off on its own. A workflow step that explicitly includes a route-to-support action can still offer escalation.

For Conversational Agents setup, see [Conversational Agents](https://www.braze.com/docs/user_guide/brazeai/agents/conversational_agents).

## How user identity works

When Braze hands a conversation to Zendesk, it creates a Zendesk end user whose Sunshine Conversations `externalId` is the user's Braze ID. That ID is stable and works for anonymous users.

Braze doesn't push profile attributes such as name or email to Zendesk. The Zendesk end user is identified by Braze ID only.

## Reconnecting or rotating your API key

Reconnecting replaces the existing integration for the workspace.

Zendesk doesn't show the API key secret again after you create it, so reconnecting always means re-entering the secret. If you're rotating credentials (a new API key for the same Zendesk app), or switching to a different Zendesk subdomain, reconnect with the new values.

## Considerations

- **Multi-conversations:** Keep multi-conversations enabled in Zendesk. If it's off, a user's second handoff fails. Braze resets that attempt and the Conversational AI agent continues the conversation.
- **If support handoff is disabled for your workspace:** Open handoffs stop syncing both ways. In-progress handoffs return the user to the Conversational AI agent. The Zendesk conversation remains open on the Zendesk side.
