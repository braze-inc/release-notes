# OAuth and MCP access in a workspace

> Company-wide OAuth policy is configured in [Admin settings](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin). In a workspace, you grant individual users permission to use the MCP server.

You can't turn MCP OAuth access on or off for one workspace, and you can't maintain a separate redirect URI allowlist per workspace.

## What's company-wide versus per-workspace

| Control | Company-wide | Per workspace |
| --- | --- | --- |
| **MCP OAuth access** | Yes. This toggle is in **Settings** > **Admin Settings** > **OAuth** under **Global access controls**. | No. Workspace admins can't override the company setting. |
| Approved redirect URIs | Yes. Approved and blocked URIs apply to every workspace. | No. |
| **Revoke MCP OAuth tokens** | Yes. Revocation invalidates every MCP OAuth token in every workspace. | No. Workspace admins can't revoke tokens for one workspace. |
| "Use MCP Server" permission | No. | Yes. Grant this permission for each workspace the user should access through the MCP server. |
| Dashboard permissions mirrored by MCP | No. | Yes. The MCP client can use only the Braze features the user can already access in that workspace. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Company-wide versus per-workspace OAuth controls" }

## If MCP OAuth access is off for the company

When **MCP OAuth access** is off in **Admin Settings**, Braze denies MCP OAuth for every workspace. Users with the "Use MCP Server" permission still can't connect, and there is no workspace-level setting to turn MCP OAuth access back on.

Users who try to connect may see a message that remote MCP access hasn't been turned on for the company. A company admin can turn on **MCP OAuth access** in **Settings** > **Admin Settings** > **OAuth**.

Redirect URI records remain on the company **OAuth** page so you can keep or update the allowlist while MCP OAuth access is off.

For company-level MCP OAuth access, redirect URIs, token revocation, and who can change those settings, see [Manage OAuth settings](https://www.braze.com/docs/user_guide/administer/global/admin_settings/oauth_admin).
