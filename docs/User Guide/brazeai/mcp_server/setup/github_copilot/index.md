# Connect GitHub Copilot to the Braze MCP server

> Learn how to connect GitHub Copilot to the Braze MCP server, sign in with OAuth, and confirm that Copilot can use Braze tools. This page covers Copilot in Visual Studio Code and GitHub Copilot CLI. For the setup that applies to every MCP client, see [Set up the Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server/setup).

This page covers GitHub Copilot. It doesn't cover Microsoft Copilot products, such as Microsoft Copilot Studio.

## Supported Copilot experiences

Copilot connects to the Braze MCP server as a remote MCP server and signs in with OAuth. The Copilot experience you use determines how your Braze admin approves it.

| Copilot experience | Can connect | How your admin approves it |
|---|---|---|
| Copilot Chat in Visual Studio Code | Yes | Approves **Visual Studio Code** as a verified MCP client. |
| GitHub Copilot CLI | Yes | Adds `http://127.0.0.1/` and `http://127.0.0.1/callback` as custom redirect URIs. |
| Copilot Chat in other IDEs, such as Visual Studio, JetBrains IDEs, Xcode, and Eclipse | Depends on the IDE | Braze hasn't verified these clients. If the IDE supports OAuth for remote MCP servers, your admin approves the redirect URI that it uses. |
| Copilot cloud agent and Copilot code review | No | These experiences don't support remote MCP servers that use OAuth. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Copilot experiences that can connect to the Braze MCP server" }

## Prerequisites

Before you start, make sure you have the following:

| Prerequisite | Description |
|---|---|
| GitHub Copilot | A Copilot plan, and either Visual Studio Code or GitHub Copilot CLI. If you have Copilot Business or Copilot Enterprise through an organization or enterprise, its "MCP servers in Copilot" policy must be turned on. |
| MCP OAuth access | A Braze company admin must turn on **MCP OAuth access**. For more information, see [Turn MCP OAuth access on or off](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin#turn-mcp-oauth-access-on-or-off). |
| Approved client or redirect URI | A Braze company admin must approve the Copilot experience you use, as described in [Step 1](#step-1-approve-copilot-in-braze). |
| "Use MCP Server" permission | You need the "Use MCP Server" permission in each workspace you want Copilot to access. |
| Braze dashboard account | You sign in with your normal Braze credentials, including SSO or SAML if your company uses it. There is no separate MCP login. |
| Paid Braze account | The Braze MCP server isn't available for free trial accounts. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites for connecting GitHub Copilot" }

## Step 1: Approve Copilot in Braze

A Braze company admin completes this step once for your company. If you aren't an admin, ask your admin to approve the Copilot experience you use.




1. Go to **Settings** > **Admin Settings** > **External Connections**.
2. Confirm **MCP OAuth access** is on under **OAuth Settings**.
3. Open the **MCP Clients** tab.
4. Select **Add MCP client** > **Browse verified MCP clients**, or select **Browse MCP Clients** if you haven't approved any clients yet.
5. Open **Visual Studio Code**, review its details, then select **Finish setup**. If Braze asks you to approve local addresses for the client, approve them.

For more information, see [Browse and approve a verified client](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin#browse-and-approve-a-verified-client).




1. Go to **Settings** > **Admin Settings** > **External Connections**.
2. Confirm **MCP OAuth access** is on under **OAuth Settings**.
3. Open the **MCP Clients** tab, then select **Add MCP client** > **Add custom redirect URIs**.
4. Enter `http://127.0.0.1/` and `http://127.0.0.1/callback`, then select **Save**.

Copilot CLI lists both of these redirect URIs, and Braze matches the path of a redirect URI exactly, so add both. Copilot CLI receives your Braze sign-in on a local address. Leave the port off so the URIs match whichever local port Copilot CLI uses. Local addresses aren't unique to one app, so other apps on your users' computers that use the same address can also connect. For more information, see [Add a custom redirect URI](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin#add-a-custom-redirect-uri).




## Step 2: Add the Braze MCP server

Add Braze as a remote MCP server that uses HTTP. Use the endpoint for your region:

- `https://mcp.braze.com/mcp` (US)
- `https://mcp.braze.eu/mcp` (EU)

EU customers should use the EU endpoint. Non-EU customers can use either endpoint. You don't need a client ID, client secret, or API key, because Copilot registers itself with Braze automatically. Registration doesn't approve Copilot for your company, so your admin still needs to complete [Step 1](#step-1-approve-copilot-in-braze).




1. In Visual Studio Code, open the Command Palette and run **MCP: Add Server**.
2. Select **HTTP (HTTP or Server-Sent Events)**.
3. Enter your Braze MCP endpoint, such as `https://mcp.braze.com/mcp`.
4. Enter a server ID, such as `braze`.
5. Choose whether to save the server for all your workspaces or only the current one.

To share the server with teammates who work in the same repository, add it to `.mcp.json` at the workspace root of that repository instead:

```json
{
  "mcpServers": {
    "braze": {
      "type": "http",
      "url": "https://mcp.braze.com/mcp"
    }
  }
}
```

For more information, see [MCP configuration reference](https://code.visualstudio.com/docs/agents/reference/mcp-configuration) in the VS Code documentation.




Run the following command in your terminal:

```bash
copilot mcp add --transport http braze https://mcp.braze.com/mcp
```

Alternatively, add the server to `~/.copilot/mcp-config.json`:

```json
{
  "mcpServers": {
    "braze": {
      "type": "http",
      "url": "https://mcp.braze.com/mcp",
      "tools": ["*"]
    }
  }
}
```

Set `type` to `http`, which uses the Streamable HTTP transport, rather than `sse`, which is the deprecated legacy transport. Copilot CLI requires the `tools` list in the configuration file. Use `["*"]` to make every Braze tool available.

For more information, see [Adding MCP servers for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers).




## Step 3: Sign in to Braze through OAuth

Copilot opens a browser window and sends you to Braze to sign in.




Start the Braze server by selecting **Start** next to the `braze` entry in your MCP configuration file, or ask Copilot a question that needs a Braze tool. When Visual Studio Code asks you to allow the Braze server to authenticate, approve the request. Your browser opens to Braze.




Start Copilot CLI with `copilot`. If the Braze server shows a `needs-auth` status in `/mcp`, run `/mcp auth braze`. Your browser opens to Braze.

Run `/mcp auth braze` again whenever your sign-in expires or you need to sign in to a different Braze company.




In your browser, complete the Braze sign-in:

1. Sign in to Braze as you normally would, including SSO if required.
2. If your login can access more than one company on the same cluster, select the company you want to use.
3. On the consent screen, review the access that Copilot is requesting.
4. Select the acknowledgment checkbox to agree to the Braze Privacy Policy, then select **Continue** to return to Copilot.

Your session uses short-lived access tokens that refresh automatically. You may occasionally need to sign in again.

## Step 4: Confirm that Copilot can use Braze tools

1. Open Copilot:
   - In Visual Studio Code, open Copilot Chat and select **Agent** mode. To list the Braze tools, select the tools icon in the chat box.
   - In Copilot CLI, start an interactive session with `copilot`. To list the Braze tools, run `/mcp show braze`.
2. Send a test prompt, such as `List the Braze tools available in this workspace.`
3. Confirm that Copilot called a Braze tool to answer. An answer without a tool call doesn't confirm the connection.

If your account can access more than one workspace, name the workspace in your prompt using the exact name shown in the Braze dashboard. For example:

- `Show my recent Canvases from the Production workspace.`
- `Compare this week's campaign analytics between my prod-1 workspace and my prod-2 workspace.`

If you don't name a workspace, Copilot may ask you to clarify or use an unexpected one. Before Copilot starts work, confirm which workspace it's using. For more example prompts, see [Using the Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server/usage).

## Troubleshooting

### "This app needs approval" or "An unexpected error occurred"

Your company hasn't approved the Copilot experience you're using. Ask your Braze admin to complete [Step 1](#step-1-approve-copilot-in-braze), then sign in again. For Copilot CLI, the redirect URIs must be `http://127.0.0.1/` and `http://127.0.0.1/callback` with no port, and their status must be **Approved**. For more information, see [Troubleshoot blocked connections](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin#troubleshoot-blocked-connections).

### Copilot cloud agent can't use Braze tools

Copilot cloud agent and Copilot code review don't support remote MCP servers that use OAuth, so they can't connect to the Braze MCP server. Use Copilot in Visual Studio Code or Copilot CLI instead.

### Other connection issues

For sign-in failures, missing tools, or the wrong workspace, see the Troubleshooting section of [Set up the Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server/setup#troubleshooting).

## Legal disclaimer
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

### How instructions and responses are handled

The Braze MCP server receives instructions from your Third-Party Provider MCP client, such as Claude, ChatGPT, Copilot, Gemini CLI, Codex, or Cursor, exactly as that provider's underlying AI model formulates them. When you type a request in natural language, the AI model interprets your request and translates it into one or more specific tool calls to Braze. Braze receives and executes the tool call as sent. Braze does not see your original natural-language prompt and cannot verify that the generated tool call fully or accurately reflects your intended request.

When Braze returns data or a result, that response is sent back to your Third-Party Provider MCP client, which then interprets, formats, and presents it to you. Braze does not control how the AI model presents, summarizes, or describes returned information.

Braze is not liable for instructions generated by, or responses conveyed through, any Third-Party Provider MCP client. Braze recommends not using "auto-mode" if your Third-Party Provider MCP client offers it for automatic action implementation. Review AI-generated summaries against source data in your Braze dashboard and review any AI-proposed action before implementing it through your Third-Party Provider MCP client.

