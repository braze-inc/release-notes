# SCIM group role mapping

> SCIM group role mapping lets you provision Braze dashboard permissions through your identity provider (IdP). Your IdP pushes groups and their members to Braze over SCIM, you map each group to a custom role, and every member of that group inherits the role's permissions.

SCIM group role mapping moves permission assignment to your IdP, so you can manage membership where you manage access, and Braze keeps your permissions in sync. This means you don't have to grant permissions one user at a time or make matching changes in your IdP and Braze.

## How it works

Group role mapping connects two relationships:

| Relationship | Managed by | How it works |
| --- | --- | --- |
| Users to groups | Your IdP | When you add or remove a member of a mapped group, the IdP syncs the change to Braze over the SCIM `/Groups` protocol. Group creates, updates, and deletes sync automatically. |
| Groups to roles | Braze admin | In the dashboard, you map each SCIM group to one or more custom roles. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="How it works" }

A user's effective permissions are the union of their directly assigned roles and every role reached through their group memberships. Group-derived roles are additive—they never remove a permission a user already has. When membership or a mapping changes, Braze re-evaluates the affected users' permissions on their next request.

Group members must already be SCIM-provisioned Braze users. Mapping a group grants a custom role, and the role carries the underlying permissions, so custom roles must be enabled for your company.

## Prerequisites

| Requirement | Details |
| ----------- | ------- |
| SCIM provisioning | You must have an active SCIM integration with Okta or Microsoft Entra ID. Group role mapping reuses the same SCIM token, IP allowlist, and rate limits as [automated user provisioning](https://www.braze.com/docs/user_guide/administer/global/user_management/automated_user_provisioning). |
| Custom roles | Custom roles must be enabled for your company. SCIM groups map to custom roles, not to individual [Braze permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) or permission sets. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Supported identity providers

Braze supports SCIM group role mapping with the same IdPs it supports for user provisioning.

| Identity provider | Notes |
| ----------------- | ----- |
| Okta | Provisions groups and members through the Okta SCIM integration. |
| Microsoft Entra ID | Provisions groups and members through the Entra ID SCIM integration. Entra ID matches groups by display name, so each group name must be unique in your workspace. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported identity providers" }

## Step 1: Provision groups from your identity provider

Configure your IdP to push the groups you want to use for provisioning. Group provisioning uses the SCIM integration you already set up for users, so no new token or endpoint is required.

| Identity provider | Provisioning steps |
| --- | --- |
| Okta | Assign the groups you want to sync to your Braze SCIM application and turn on group push. |
| Microsoft Entra ID | Add the groups to your Braze enterprise application's provisioning scope. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Provision groups from your identity provider" }

After a group syncs, its members—who must be existing SCIM-provisioned Braze users—become available for role mapping in Braze.

**Note:**


Members that your IdP sends but that don't yet exist as Braze users are skipped rather than rejected. Provision the user first, then the group membership takes effect.



## Step 2: Map a group to a custom role

1. Go to **Settings** > **User Management** > **Roles**.
2. Create a new custom role or open an existing one.
3. In the role's info panel, find **SCIM user group mapping**.
4. Select one or more groups provisioned from your IdP.
5. Save the role.

![The "Edit Role" page with the "Marketer UK" SCIM group selected in the "SCIM user group mapping" field.](https://www.braze.com/docs/assets/img/braze_permissions/scim_group_role_mapping.png?92e777de0d9a73069e4df9d782198f4d)

Every member of the selected groups inherits the role's permissions. The roles list shows how many SCIM groups map to each role.

To stop granting a role through a group, remove the group from the role's mapping and save. To change who receives the role, update the group's membership in your IdP.

## Frequently asked questions

### What happens to a user's directly assigned roles?

Nothing. Group-derived roles are added on top of direct assignments. Directly assigned roles remain editable in Braze; roles granted through a group are managed by editing the mapping or the group's membership.

### Can one group map to more than one role?

Yes. A group can map to multiple custom roles, and a role can be mapped from multiple groups.

### Where do I manage who is in a group?

In your identity provider. Braze receives membership from the IdP over SCIM and does not let you edit group membership directly in the dashboard.

### Does removing a user from a group revoke their permissions?

Yes, for permissions granted through that group. When the IdP removes the user from the group, Braze re-evaluates their permissions and drops any role they held only through that group. Permissions from direct assignments or other groups are unaffected.

Depending on your IdP and how you assign your Braze SCIM integration, removing a user from a group can also delete their Braze dashboard user:

- **[Microsoft Entra ID](https://www.braze.com/docs/user_guide/administer/global/user_management/automated_user_provisioning?tab=entra%20id):** If the user is in a group that is assigned to your Braze SCIM application, and the user isn't assigned to that application independently of that group, removing them from the group (or removing the group) deletes the user in Braze.
- **[Okta](https://www.braze.com/docs/user_guide/administer/global/user_management/automated_user_provisioning?tab=okta%20-%20braze%20app):** If the group is assigned to your Braze SCIM application and the user isn't assigned to that application independently, removing them from the group may delete the user in Braze.
