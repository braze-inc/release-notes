# Manage OAuth settings

> OAuth settings manage company-wide access to the [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server/), control which custom MCP client redirect URIs can connect to Braze, and let you revoke every MCP OAuth token for your company.

OAuth settings apply to your entire company. The permissions assigned to each user determine which workspaces and features they can access through the MCP server.

## Requirements

| Requirement | Description |
| --- | --- |
| "Admin" permission | You must have the company-level "Admin" permission to view OAuth settings, turn MCP OAuth access on or off, manage redirect URIs, or revoke MCP OAuth tokens. |
| "Use MCP Server" permission | Users must have this permission for each workspace they want to access through the MCP server. This permission is separate from the "Admin" permission used to manage OAuth settings. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements for managing OAuth settings" }

For more information about assigning permissions, see [User permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/).

## How OAuth access works

OAuth settings and user permissions work together:

- Company-wide OAuth settings determine whether users can connect MCP clients to Braze.
- The "Use MCP Server" permission determines whether an individual user can use the MCP server in a workspace.
- The user's existing dashboard permissions determine which Braze data and features an MCP client can access.
- One OAuth connection can access only the workspaces that the user is authorized to access.

Turning on MCP OAuth access doesn't grant users new workspace permissions. Similarly, removing a dashboard permission removes that capability from the user's connected MCP client.

## Company and workspace controls

OAuth policy is stored at the company level. Workspace admins can't override **MCP OAuth access** or redirect URI statuses for a single workspace.

| Control | Where you configure it | Scope |
| --- | --- | --- |
| **MCP OAuth access** | **Settings** > **Admin Settings** > **OAuth** | Entire company. When this is off, MCP OAuth is denied in every workspace. |
| Approved redirect URIs | **Settings** > **Admin Settings** > **OAuth** | Entire company. Approved and blocked URIs apply to all workspaces. |
| **Revoke MCP OAuth tokens** | **Settings** > **Admin Settings** > **OAuth** | Entire company. Revocation applies to every MCP OAuth token in every workspace. |
| "Use MCP Server" permission | **Settings** > **User Management** | Per workspace. Users need this permission in each workspace they access through the MCP server. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Company and workspace OAuth controls" }

Only users with the "Admin" permission can change **MCP OAuth access**, change redirect URI statuses, or revoke MCP OAuth tokens. For how workspace permissions interact with these company settings, see [OAuth and MCP access](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/oauth_settings/).

## Turn MCP OAuth access on or off

To update MCP OAuth access for your company:

1. Go to **Settings** > **Admin Settings** > **OAuth**.
2. In **Global access controls**, turn **MCP OAuth access** on or off.

When **MCP OAuth access** is on, users with the "Use MCP Server" permission can authorize approved MCP clients. When it's off, OAuth access to the MCP server is denied for all users and workspaces in your company.

Turning off **MCP OAuth access** doesn't remove or block your configured redirect URIs. Braze revokes existing MCP OAuth tokens for your company, so connected MCP clients lose access. The **Approved redirect URIs** section is hidden while MCP OAuth access is off; turn it back on to manage the same URI list again.

If Braze has turned off the remote MCP server for your environment, the **MCP OAuth access** toggle is disabled and a message explains that the company setting has no effect until the remote MCP server is turned on again.

## Manage approved redirect URIs

After you turn on **MCP OAuth access**, the **Approved redirect URIs** section lists redirect URIs that custom MCP clients can use during authentication. For formatting guidance, see [Redirect URI formats](#redirect-uri-formats).

The **Approved redirect URIs** table shows the following information:

| Column | Description |
| --- | --- |
| Redirect URI | The exact address Braze matches against the client's callback, including the path. |
| Added by | The dashboard user who added or last updated the URI. |
| Date added | When the URI was added or last updated. |
| Status | Whether the URI is **Approved** or **Blocked**. |
| Actions | **Block** or **Unblock**, depending on the current status. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Approved redirect URIs table columns" }

### Redirect URI formats

| URI type | Format to use when adding |
| --- | --- |
| Local (loopback address) | Starts with `http://localhost` or `http://127.0.0.1`. Omit the port (the colon and numbers after the host) so any local port can match. For example, if the client shows `http://localhost:33491/oauth/callback`, enter `http://localhost/oauth/callback`. If you keep a port in the URI you add (such as `:33491`), Braze matches that port only. |
| Remote address | Enter the full address exactly as the client shows, for example `https://app.example.com/callback`. |
| Custom scheme | Starts with a custom URI scheme (not `http://` or `https://`), such as `cursor://`. Enter it exactly as shown. Some desktop apps use these addresses. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Redirect URI formats" }

### Add a redirect URI

To allow a custom MCP client that isn't already listed:

1. Select **Add redirect URI**.
2. Enter the full redirect URI with callback protocol from the client's OAuth or integration settings. Use the [Redirect URI formats](#redirect-uri-formats) table if you need help matching the client's callback.
3. Select **Save**.

For local clients, use `127.0.0.1` and omit the port number in the redirect URI you add.

Only redirect URIs with an **Approved** status can complete a new OAuth authorization. If a URI isn't on the list and isn't a Braze-verified client, Braze denies the authorization request.

### Block a redirect URI

To prevent new OAuth authorizations from a redirect URI, select **Block** for its row and confirm the action. Braze retains the URI record and changes its status to **Blocked**.

Blocking a redirect URI doesn't revoke tokens for users who are already connected to that MCP client. Select **Revoke MCP OAuth tokens** to end those sessions. Blocking the URI is a separate action that prevents new authorizations with that callback.

Alternatively, remove the "Use MCP Server" permission from a user to stop only that user from using the MCP server. Other users' MCP connections stay active until you select **Revoke MCP OAuth tokens**.

### Unblock a redirect URI

To restore access for a blocked redirect URI, select **Unblock** for its row and confirm the action. Braze updates the existing record to **Approved** instead of creating a duplicate.

Users who were previously connected to that MCP client need to authenticate again.

## Revoke MCP OAuth tokens

Revoking tokens invalidates every MCP OAuth token across your company at once. Use this if you think a token has been leaked or misused.

To revoke your company's MCP OAuth tokens:

1. Go to **Settings** > **Admin Settings** > **OAuth**.
2. In **Revoke MCP OAuth tokens**, select **Revoke MCP OAuth tokens**.
3. Review the confirmation dialog, then select **Revoke tokens**.

Braze revokes the tokens in the background and shows a confirmation message when the revocation finishes. For companies with many connections, this can take a few minutes. Leave the **OAuth** page open until the confirmation appears.

**Warning:**


Revoking tokens can't be undone. Every connected MCP client loses access to Braze, and each user has to sign in and connect their MCP client again.



### What revocation changes

| Item | Result |
| --- | --- |
| Access tokens | Revoked. Connected MCP clients stop working until the user reconnects. |
| Refresh tokens | Revoked. MCP clients can't reconnect on their own in the background. Users have to reconnect themselves. |
| **MCP OAuth access** | Unchanged. If it was on, users can reconnect right away. |
| Approved redirect URIs | Unchanged. Approved and blocked URIs stay as they are. |
| "Use MCP Server" permission | Unchanged. Users keep the permission and can reconnect. |
| New connections | Unaffected. Connections made after you start the revocation keep working. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What revoking MCP OAuth tokens changes" }

Requests that were already in progress when you revoked aren't recalled. To stop all MCP access instead of only ending current sessions, turn off **MCP OAuth access** (that also revokes MCP OAuth tokens). To remove one user's MCP access, remove the "Use MCP Server" permission from that user.

If revocation doesn't finish, Braze shows an error message. Some tokens may already be revoked, so contact support before trying again.

## Audit OAuth activity

Braze records OAuth connections to the MCP server in the [security event report](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings/#security-event-report). Use this report to audit when users connect through OAuth.

To revoke one user's MCP access, remove the "Use MCP Server" permission from that user. To revoke every MCP OAuth token in your company, see [Revoke MCP OAuth tokens](#revoke-mcp-oauth-tokens). For setup and troubleshooting guidance, see [Setting up the Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server/setup/).
