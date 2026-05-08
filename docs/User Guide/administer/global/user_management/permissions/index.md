# Braze permissions 

> Learn how to create permission sets, create roles, edit user permissions, and export user permissions, so you can ensure your users only access the workspaces and features they need most.




**Important:**


Braze is introducing [granular permissions](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions), a more flexible way to manage user access. Refer to [Migrating to granular permissions](https://www.braze.com/docs/granular_permissions_migration/) to learn about the migration process, including how legacy permissions map to granular permissions.



## Creating a permission set

Use permission sets to bundle permissions related to specific subject areas or actions. You can apply permission sets to dashboard users who need the same access across different workspaces. To create a permission set, go to **Settings** > **Permission Settings**, then select **Create permission set**. For a description of each permission, see [List of permissions](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).



|Name|Permissions|
|-----------|----------------|
|Developers|“Access Dev Console”|
|Marketers|“Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers” <br> “Manage Media Library Assets”|
|User Management|“Manage Dashboard Users” <br> “Manage Teams”|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



## Creating a role

Roles allow for more structure by bundling together your individual custom permissions with workspace access controls. This is especially useful if you have many brands or regional workspaces in one dashboard. With roles, you can add dashboard users to the right workspaces and directly grant them the associated permissions. For a description of each permission, see [List of permissions](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).



| Role Name    | Workspace | Permissions  
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Center"<br>“Manage Media Library Assets” |
| Marketer - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | “Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers” <br>“Manage Media Library Assets” |
| User Management - All Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | “Manage Dashboard Users”<br>“Manage Teams” |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }



## How do permission sets and roles differ from Teams?



### Considerations for adding user permissions to Teams

You may encounter difficulties when trying to save permissions in the Braze dashboard, particularly when adding or removing users from a workspace, or adding them to a Team. The **Save/Update Users** button may become greyed out if the permissions for the user are identical to those they already have at the workspace level. This restriction exists because there is no benefit to having a Team if all users possess the same permissions as the entire workspace.

To successfully add a user to a Team while maintaining the same permissions, don't assign any permissions at the workspace level. Instead, assign permissions exclusively at the team level.

## Limited users

Limited users have specific permissions that allow them to manage certain aspects of the Braze dashboard while having restrictions compared to company admins and workspace admins.

| Permissions | Limited users can edit the permissions of other limited users if they have the "Manage Dashboard Users" permission checked. They can also create new limited users and modify their permission sets. However, they can't create or manage company admin accounts. |
| Role limitations | If a limited user has all permissions except "App Group Admin", they will still have access to all other permissions typically granted to an workspace admin. |
| Visibility of permissions | If a limited user has "Manage Dashboard Users" checked for one app group (such as Dev) but not for another (such as Prod), they won't see the Prod app group permissions in their "Manage Users" profile. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparing limited users

| Limited user type | Description |
| --- | --- |
| App group admin | App Group Admins have permissions specific to managing app groups but do not have the same authority as Company Admins. Limited Users can inherit permissions similar to those of App Group Admins if they have the necessary permissions checked. |
| Company admin | Company Admins have broader permissions, including the ability to delete dashboard users. However, they cannot delete their own accounts and must contact another Company Admin for that action. |
| Basic read-only permission | To access certain parts of the dashboard, such as the Technology Partners page, users must have a basic read-only permission. This includes having "Manage External Integrations" enabled, along with permissions for Access Campaigns, Canvases, Cards, Segments, and Media Library. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Limited access error

Users may encounter messages like "Limited Access. You do not have permissions to access this Page." In such cases, the account admin should check if they can resolve the issue by disabling and re-enabling the user's permissions.

**Note:**


It isn't possible to merge or import user permissions from one dashboard user to another.



## Editing a user's permissions

To edit a user's current admin, company, or workspace permissions, go to **Settings** > **Company Users**, then select their name.

![The "Company Users" page in Braze with one user listed in the results.](https://www.braze.com/docs/assets/img/braze_permissions/selecting_a_user.png?d28314848ed4e956dece842568f78574)




### Admin

Admins have access to all features and the ability to modify any company setting. They can:

- Change [approval settings](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Add, edit, delete, suspend, or unsuspend other [Braze users](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/)
- Export Braze users as a CSV

To grant or remove admin privileges, select **This user is an admin**, then select **Update user**.

![The details of the selected user with the admin checkbox in focus.](https://www.braze.com/docs/assets/img/braze_permissions/admin_level_permissions.png?14c300edaa5008e6ee9aa6eba1dda237){: style="max-width:70%;"}

**Warning:**


If you remove admin privileges from a user, they won't be able to access Braze until you assign them at least one [company-level or workspace-level](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions&tab=company#legacypermissions_editing-a-users-permissions) permission.






### Company

To manage the following company-level permissions for a user, check or uncheck the box next to that permission. When you're finished, select **Update user**.

|Permission name|Description|
|----------|-----------|
|Manage company settings|Allows users to modify any company setting.|
|Create and delete workspaces|Allows users to create and delete workspaces.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }




### Workspace

You can give a user different permissions for each workspace they belong to in Braze. To manage their workspace-level permissions, select **Select workspaces and permissions**, then choose their permissions manually to select or assign a permission set [you previously created](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_creating-a-permission-set).

If you need to give a user different permissions for different workspaces, repeat this process as many times as needed. For a description of each permission, see [List of permissions](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions#legacypermissions_list-of-permissions).




Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permissions**, choose one or more permissions from the dropdown. Braze assigns these permissions only for the workspaces you have selected. Optionally, you can select **Enable Admin Access** if you'd like to give them full permissions for this workspace instead.

When you're finished, select **Update user**.

![Workspace-level permissions being manually selected in Braze.](https://www.braze.com/docs/assets/img/braze_permissions/workspace_level_permissions_individual_legacy.png?aa80d81d15dfd47b8ac402f7a3d53016)




Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permission Sets**, choose one permission set. Braze assigns these permissions only for the workspaces you have selected.

When you're finished, select **Update user**.

![Workspace-level permissions being assigned through a permission set in Braze.](https://www.braze.com/docs/assets/img/braze_permissions/workspace_level_permissions_set_legacy.png?740e4940a7bab02370093840971c586a)






## Exporting user permissions

To download a list of your users and their permissions, go to **Settings** > **Company Users**, then select **Export Users**. A CSV file will be sent to your email address shortly.

![The "Company Users" page in Braze with the "Export Users" option in focus.](https://www.braze.com/docs/assets/img/braze_permissions/exporting_user_permissions.png?64292c338e1614a7215faa059b9277e4)

## List of permissions

|Level|Name|Definition|
|---|---|---|
|Admin|Admin|Allows users to access all available features. This is the default setting for all new users. Can update company settings (company name and time zone), which limited users cannot do.|
|Company|Create and delete workspaces|Allows users to create and delete workspaces.|
|Company|Manage company settings|Allows users to modify any company setting.|
|Workspace|Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers|Allows users to view campaign and Canvas performance metrics, create and duplicate drafts of campaigns and Canvases, edit campaign and Canvas drafts and templates, view drafts of segments, templates and media, create templates, upload media, create or update promotion code lists, view engagement reports, and view global message settings in the dashboard. However, users with this permission cannot pause or edit existing live content.<br><br> When this permission is configured as a [Team permission](https://www.braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/teams/), if any campaigns or Canvases in the [engagement report](https://www.braze.com/docs/user_guide/analytics/reporting/engagement_reports/) are outside of a user’s assigned Teams or have no assigned Teams, the report is hidden from the user.|
|Workspace|Access Dev Console|Allows full access to the following settings and logs:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>API Keys</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Internal Groups</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Message Activity Log</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Event User Log</a></li></ul>{:/}|
|Workspace|Approve and Deny Campaigns|Allows users to approve or deny campaigns. The [approval workflow for campaigns](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you're interested in participating in the early access.|
|Workspace|Approve and Deny Canvases|Allows users to approve or deny Canvases. The [approval workflow for Canvases](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply.|
|Workspace|Edit Currents Integrations|Allows users to modify a Currents connection, including credentials. By default, users assigned the "External Integrations" permission are also assigned this permission.|
|Workspace|Edit Segments|Allows users to create and edit segments. You can still create campaigns with existing segments and filters without this permission. You need this permission to generate a segment from users in a CSV or retarget the group of users in the CSV.|
|Workspace|Export User Data|Allows users to export their user data from segments, campaigns, and Canvases. This permission includes sensitive user information like names, email addresses, and other collected personally identifiable information (PII). To export CSVs from the dashboard, you must have this permission and the "View PII" permission.|
|Workspace|Import and Update User Data|Allows users to import CSV and update files of app users as well as view the User Import page. This also allows you to edit the subscription status of a user and their subscription group opt-in/opt-out rules.|
|Workspace|Launch and Manage Content Blocks|Allows users to launch and manage [Content Blocks](https://www.braze.com/docs/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Workspace|Launch Preference Centers|Allows users to launch [preference centers](https://www.braze.com/docs/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Workspace|Manage Apps|Allows users to edit **App Settings**.|
|Workspace|Manage Catalogs Dashboard Permission|Allows users to create and manage catalogs.|
|Workspace|Manage Dashboard Users| Allows non-admins the ability to view, edit, and manage the **Company Users** page, and manage the dashboard users in their workspace by modifying the permissions of any user, including themselves. Users with this permission can’t delete users (only administrators can delete users).<br><br>This corresponds to the legacy permission `MANAGE_DEVELOPERS_AND_PERMISSIONS`.|
|Workspace|Manage Email Settings|Allows users to save email configuration changes (**Settings** > **Email Preferences**).|
|Workspace|Manage Events, Attributes, Purchases|Allows users to edit custom attributes (users without this capability can still view custom attributes), edit and view properties of custom events, and edit and view properties of products under **Data Settings**.|
|Workspace|Manage External Integrations|Allows access to all tabs under **Technology Partners**, ability to sync Braze with other platforms, and access to manage [Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data/cloud_ingestion/).|
|Workspace|Manage Feature Flags|Allows users to create or edit [feature flags](https://www.braze.com/docs/developer_guide/feature_flags/).|
|Workspace|Manage Media Library Assets|Allows users to add, edit, and delete media library assets.|
|Workspace|Manage Subscription Groups|Allows users to create and manage subscription groups.|
|Workspace|Manage Tags|Allows users to edit or delete tags (under **Tag Management**). You do not need this permission to add tags to campaigns or segments.|
|Workspace|Manage Teams|Allows users to manage **Internal Teams**. The ability to select this permission depends on your contract with Braze.<br><br>This corresponds to the legacy permission `MANAGE_TERRITORIES`.|
|Workspace|Manage Transformations|Allows users to create and manage Data Transformations.|
|Workspace|Send Campaigns, Canvases|Allows users to edit, archive, and stop campaigns and Canvases, create campaigns, and launch Canvases. |
|Workspace|View Billing Details|Allows users to view subscriptions and billing.|
|Workspace|View Currents Integration|Allows users to view all information about a Currents connection, excluding credentials. By default, users assigned the "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers" permission are also assigned this permission.|
|Workspace|View Custom Attributes Marked as PII|Allows non-admin users to view custom attributes that contain sensitive information and are marked as personally identifiable information (PII).|
|Workspace|View PII|Allows users to view personally identifiable information (PII) fields as defined by your company within the dashboard. Users can also view PII fields in the **Preview as a User** tab of message previews.<br><br>You need this permission to use [Query Builder](https://www.braze.com/docs/user_guide/analytics/query_builder/building_queries/), because it allows direct access to some customer data. To export CSVs from the dashboard, users need both this permission and the "Export User Data" permission.|
|Workspace|View User Profiles PII Compliant|Allows users to view user profiles that contain fields your company has defined as personally identifiable information (PII), but redacts the PII fields.<br><br>You need this permission to use the user search tool. |
|Workspace|View Transformations|Allows users to view [Braze Data Transformations](https://www.braze.com/docs/user_guide/data/data_transformation/overview/).|
|Workspace|View Usage Data|Allows users to view app usage, including the channel performance dashboards.|
|Workspace|Merge Duplicate Users|Allows users to merge duplicate user profiles.|
|Workspace|Preview Duplicate Users|Allows users to preview which user profiles are duplicated.|
|Workspace|Create and Edit Canvas Templates|Allows users to create and edit Canvas templates.|
|Workspace|View Canvas Templates|Allows users to view Canvas templates.|
|Workspace|Archive Canvas Templates|Allows users to archive Canvas templates.|
|Workspace|Manage Custom Event Property Segmentation|Allows users to create segments based on event property recency and frequency.|
|Workspace|Publish Landing Pages|Allows users to publish [landing pages](https://www.braze.com/docs/user_guide/engagement_tools/landing_pages/).|
|Workspace|Create Landing Page Drafts|Allows users to create and save landing page drafts.|
|Workspace|Access Landing Pages|Allows users to access the **Landing Pages** page.|
|Workspace|Create and Edit Landing Page Templates|Allows users to create and edit landing page templates.|
|Workspace|View Landing Page Templates|Allows users to view landing page templates.|
|Workspace|Archive Landing Page Templates|Allows users to archive landing page templates.|
|Workspace|View Custom AI Agents|Allows users to view [custom AI agents](https://www.braze.com/docs/user_guide/brazeai/agents/). This feature is currently in beta.|
|Workspace|Create Custom AI Agents|Allows users to create custom AI agents. This feature is currently in beta.|
|Workspace|Edit Custom AI Agents|Allows users to edit custom AI agents. This feature is currently in beta.|
|Workspace|Support Tickets | Create Support Ticket | Create and update Support tickets. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }













































<iframe width="560" height="315" src="https://www.youtube.com/embed/" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen class="media_embed "></iframe>



## Creating a permission set

Use permission sets to bundle permissions related to specific subject areas or actions. You can apply permissions sets to dashboard users who need the same access across different workspaces. To create a permission set, go to **Settings** > **Permission Settings**, then select **Create permission set**. For a description of each permission, see [List of permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).



|Name|Permissions|
|-----------|----------------|
|Developers|"View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger".|
|Marketers|"View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Email Link Templates", "Edit Email Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Dashboard Reports", "View Banner Templates", "View Localization Settings", "Use Operator", "View Decisioning Studio Agents".|
|User Management|"Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams".|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



## Creating a role

Roles allow for more structure by bundling together your individual custom permissions with workspace access controls. This is especially useful if you have many brands or regional workspaces in one dashboard. With roles, you can add dashboard users to the right workspaces and directly grant them the associated permissions. For a description of each permission, see [List of permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).



| Role Name    | Workspace | Permissions  
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Marketer - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} |"View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers".|
| User Management - All Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }



## How do permission sets and roles differ from Teams?



### Considerations for adding user permissions to Teams

You may encounter difficulties when trying to save permissions in the Braze dashboard, particularly when adding or removing users from a workspace, or adding them to a Team. The **Save/Update Users** button may become greyed out if the permissions for the user are identical to those they already have at the workspace level. This restriction exists because there is no benefit to having a Team if all users possess the same permissions as the entire workspace.

To successfully add a user to a Team while maintaining the same permissions, don't assign any permissions at the workspace level. Instead, assign permissions exclusively at the team level.

## Limited users

Limited users have specific permissions that allow them to manage certain aspects of the Braze dashboard while having restrictions compared to company admins and workspace admins.

| Scope | Description |
| --- | --- |
| Permissions | Limited users can edit the permissions of other limited users if they have the "Edit Dashboard Users" permission. They can also create new limited users and modify their permission sets. However, they can't create or manage company admin accounts. |
| Role limitations | If a limited user has all permissions except "Workspace Admin", they will still have access to all other permissions typically granted to a workspace admin. |
| Visibility of permissions | If a limited user has the "Edit Dashboard Users" permission for one workspace (such as Dev) but not for another (such as Prod), they won't see the Prod workspace permissions in their dashboard users detail page. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparing limited users

| Limited user type | Description |
| --- | --- |
| Workspace Admin | Workspace Admins have permissions specific to managing Workspaces but do not have the same authority as Company Admins. Limited Users can inherit permissions similar to those of Workspace Admins if they have the necessary permissions checked. |
| Admin (Company Admin) | Company Admins have broader permissions, including the ability to delete dashboard users. However, they cannot delete their own accounts and must contact another Company Admin for that action. |
| View-only access | To access parts of the dashboard, such as the Campaigns page, users must have view permissions assigned to them.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Limited access error

Users may encounter messages like "You need “View Landing Pages” permissions to access this page”. In such cases, the user and account admin should verify that the required permissions are granted. If they are, try resolving the issue by disabling and then re-enabling the user’s permissions. 

**Note:**


It isn't possible to merge or import user permissions from one dashboard user to another.



## Editing a user's permissions

To edit a user's current admin, company, or workspace permissions, go to **Settings** > **Company Users**, then select their name.

![The "Company Users" page in Braze showing a table of dashboard users.](https://www.braze.com/docs/assets/img/braze_permissions/selecting_a_user.png?d28314848ed4e956dece842568f78574)




### Admin

Admins have access to all features and the ability to modify any company setting. They can:

- Change [approval settings](https://www.braze.com/docs/user_guide/messaging/governance/approvals/#turning-on-the-approval-workflow)
- Add, edit, delete, suspend, or unsuspend other [Braze users](https://www.braze.com/docs/user_guide/administer/global/user_management/manage_company_users/#adding-company-users)
- Export Braze users as a CSV

To grant or remove admin privileges, select **This user is an admin**, then select **Update user**.

![The details of the selected user with the admin checkbox in focus.](https://www.braze.com/docs/assets/img/braze_permissions/admin_level_permissions.png?14c300edaa5008e6ee9aa6eba1dda237){: style="max-width:70%;"}

**Warning:**


If you remove admin privileges from a user, they won't be able to access Braze until you assign them at least one [company-level or workspace-level permission](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).






### Company

To manage the following company-level permissions for a user, check or uncheck the box next to that permission. When you're finished, select **Update user**.

|Permission name|Description|
|----------|-----------|
|Manage company settings|Allows users to modify permission settings and sender verification. .|
|Create and delete workspaces|Allows users to create and delete workspaces.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }




### Workspace

You can give a user different permissions for each workspace they belong to in Braze. To manage their workspace-level permissions, select **Select workspaces and permissions**, then choose their permissions manually or assign a [permission set or role](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) you previously created. If you need to give a user different permissions for different workspaces, repeat this process as many times as needed. For a description of each permission, see [List of permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).




Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permissions**, select one or more permissions. They will be assigned these permissions only for the workspaces you have selected. Optionally, you can select **Assign workspace admin access** if you'd like to give them full permissions for this workspace instead.

When you're finished, select **Update user**.

![Workspace-level permissions being manually selected in Braze.](https://www.braze.com/docs/assets/img/braze_permissions/workspace_level_permissions_individual.png?2da5bb5ca973e824c019108564417337)




Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permission Sets**, choose one permission set. They will be assigned these permissions only for the workspaces you have selected.

When you're finished, select **Update user**.

![Workspace-level permissions being assigned through a permission set in Braze.](https://www.braze.com/docs/assets/img/braze_permissions/workspace_level_permissions_set.png?4dc65f245b53a6d5f1addd0132124d98)




Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Role**, choose one role. They will be assigned these permissions only for the workspaces you have selected.

When you're finished, select **Update user**.

![Workspace-level permissions being assigned through a role in Braze.](https://www.braze.com/docs/assets/img/braze_permissions/workspace_level_role.png?4151e22b4491d46c3333b2e375e4bf18)






## Exporting user permissions

To download a list of your users and their permissions, go to **Settings** > **Company Users**, then select **Export Users**. A CSV file will be sent to your email address shortly.

![The "Company Users" page in Braze with the "Export Users" option in focus.](https://www.braze.com/docs/assets/img/braze_permissions/exporting_user_permissions.png?64292c338e1614a7215faa059b9277e4)

## List of permissions

### Messaging

| Product area | Permission | Definition |
| --- | --- | --- |
| Campaigns | View Campaigns | View campaigns |
| Campaigns | Launch Campaigns | Start, stop, pause, or resume existing campaigns |
| Campaigns | Archive Campaigns | Move campaigns to archive |
| Campaigns | Edit Campaigns | Create and update campaigns |
| Campaigns | Approve and Deny Campaigns | Approve or deny campaigns. The [approval workflow for campaigns](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you’re interested in participating in the early access. |
| Canvas | View Canvases | View Canvases |
| Canvas | Archive Canvases | Move Canvases to archive |
| Canvas | Edit Canvases | Create and update Canvases |
| Canvas | Launch Canvases | Start, stop, pause, or resume existing Canvases |
| Canvas | Approve and Deny Canvases | Approve or deny Canvases. The [approval workflow for Canvases](https://www.braze.com/docs/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you’re interested in participating in the early access. |
| Feature flags | View Feature Flags | View feature flags |
| Feature flags | Archive Feature Flags | Move feature flags to archive |
| Feature flags | Edit Feature Flags | Create and update feature flags |
| Frequency Caps | View Frequency Capping Rules | View Frequency Capping Rules |
| Frequency Caps | Edit Frequency Capping Rules | Create and update Frequency Capping Rules |
| Landing pages | View Landing Pages | View landing pages |
| Landing pages | Publish Landing Pages | Make a draft landing page active |
| Landing pages | Edit Landing Page Drafts | Create and save landing page drafts |
| Message Archiving Settings | View Message Archiving Settings | View Message Archiving settings without making changes |
| Message Archiving Settings | Edit Message Archiving Settings | Create and update Message Archiving settings |
| Message Prioritization | View Message Prioritization | View message prioritization settings without making changes |
| Message Prioritization | Edit Message Prioritization | Create and update message prioritization settings |
| WhatsApp Flows | View WhatsApp Flows | View all WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Audience

| Product area | Permission | Definition |
| --- | --- | --- |
| Global Control Group | View Global Control Group | View Global Control Group setup page |
| Global Control Group | Edit Global Control Group | Create and save changes to the Global Control Group. Users with the “Edit Global Control Group” permission must also be granted permissions for “Edit Campaigns” and “Edit Canvases”. Users with the “Edit Global Control Group” permission are also granted the “View Global Control Group” permission. |
| Locations | Archive Locations | Move locations to archive |
| Locations | View Locations | View locations |
| Locations | Edit Locations | Create and edit locations |
| Segments | View Segments | View segments. Users must have the “View Segments” permission to have the “Edit Segments” or “Archive Segments” permission |
| Segments | Archive Segments | Archive and un-archive segments. Users with the “Archive Segments” permission must also be granted the “View Segments” permission |
| Segments | Edit Segments | Create and update Segments. Users with the “Edit Segments” permission must also be granted the “View Segments permission” |
| User Data | View Import Users | View CSV user imports without making changes |
| User Data | Import Users | Upload users to the dashboard |
| User Data | Edit User Data | Create and update user data |
| User Data | Export User Data | Download users from the dashboard |
| User Deletion Records | View User Merge Records | View a list of user merge records |
| Users | View User Profiles (PII Redacted) | View user profiles in a PII compliant manner |
| Duplicate Users | Merge Duplicate Users | Combine duplicate users into one user. Duplicates are removed after merging |
| Users | Delete Users | Permanently delete users from the dashboard individually or in bulk |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Template

| Product area | Permission | Definition |
| --- | --- | --- |
| Banner Templates | View Banner Templates | View banner templates |
| Banner Templates | Archive Banner Templates | Move banner templates to archive |
| Banner Templates | Edit Banner Templates | Create and update banner templates |
| Canvas Templates | View Canvas Templates | View Canvas templates |
| Canvas Templates | Archive Canvas Templates | Move Canvas templates to archive |
| Canvas Templates | Create and Edit Canvas Templates | Create and update Canvas templates |
| Content Blocks | View Content Blocks | View Content Blocks |
| Content Blocks | Launch Content Blocks | Publish draft Content Blocks, and edit, archive, and unarchive launched Content Blocks |
| Content Blocks | Archive Content Blocks | Move Content Blocks to archive |
| Content Blocks | Edit Content Blocks | Create Content Blocks and edit draft Content Blocks |
| Email Link Templates | View Email Link Templates | View link templates without making changes |
| Email Link Templates | Edit Email Link Templates | Create and update link templates |
| Email Templates | View Email Templates | View email templates |
| Email Templates | Archive Email Templates | Move email templates to archive |
| Email Templates | Edit Email Templates | Create and update email templates |
| IAM Templates | View IAM Templates | View in-app message templates without making changes |
| IAM Templates | Archive IAM Templates | Move IAM templates to archive |
| IAM Templates | Edit IAM Templates | Create and update in-app message templates |
| Landing Page Templates | View Landing Page Templates | View landing page templates |
| Landing Page Templates | Archive Landing Page Template | Move landing page templates to archive |
| Landing Page Templates | Edit Landing Page Templates | Create and update landing page templates |
| Webhook Templates | View Webhook Templates | View webhook templates without making changes |
| Webhook Templates | Archive Webhook Templates | Move webhook templates to archive |
| Webhook Templates | Edit Webhook Templates | Create and update webhook templates |
| Whatsapp Message Templates | View WhatsApp Message Templates | Allows users to view [WhatsApp message templates](https://www.braze.com/docs/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-2-compose-your-whatsapp-message) |
| Whatsapp Message Templates | Edit WhatsApp Message Templates | Allows users to create WhatsApp message templates in the template builder. This feature is currently in early access. |
| WhatsApp Message Templates From Meta | View WhatsApp Message Templates From Meta | View All WhatsApp Templates |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Partner integrations

| Product area | Permission | Definition |
| --- | --- | --- |
| Currents Integrations | View Currents Integration | View Currents integrations |
| Currents Integrations | Edit Currents Integrations | Create, update, and delete Currents integrations |
| Technology Partners | Edit Technology Partners | Create and update technology partners |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Data settings

| Product area | Permission | Definition |
| --- | --- | --- |
| Catalogs | View Catalogs | View catalogs and selections |
| Catalogs | Delete Catalogs | Permanently delete catalogs |
| Catalogs | Export Catalogs | Download catalogs from the dashboard |
| Catalogs | Edit Catalogs | Create and update catalogs and selections |
| Cloud Data Ingestion | Edit Cloud Data Ingestion | Create, update, and delete sources and syncs |
| Custom Attributes | View Custom Attributes | View custom attributes and usage report |
| Custom Attributes | Export Custom Attributes | Download custom attributes from the dashboard |
| Custom Attributes | Delete Custom Attributes | Permanently delete custom attributes |
| Custom Attributes | Blocklist Custom Attributes | Add custom attributes to a blocklist that restricts use in the dashboard |
| Custom Attributes | Edit Custom Attributes | Create and update custom attributes |
| Custom Event Property Segmentation | Edit Custom Event Property Segmentation | Enable and disable segmentation for custom event properties |
| Custom Events | View Custom Events | View custom events and usage report, and add custom events to the daily analytics report email |
| Custom Events | Export Custom Events | Download custom events from the dashboard |
| PII | View PII | View PII |
| Custom Events | Delete Custom Events | Permanently delete custom events |
| Custom Events | Blocklist Custom Events | Add custom events to a blocklist that restricts use in the dashboard |
| Custom Events | Edit Custom Events | Create and update custom events |
| Products | View Products | View products |
| Products | Blocklist Products | Add products to a blocklist that restricts use in the dashboard |
| Products | Edit Products | Create and update products |
| Purchase Property Segmentation | Edit Purchase Property Segmentation | Enable and disable segmentation for purchase event properties |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Settings

| Product area | Permission | Definition |
| --- | --- | --- |
| API Identifiers | View API identifiers | View API identifiers and other identifiers |
| API Keys | View API Keys | View API keys |
| API Keys | Edit API Keys | Create and update API keys |
| API Limits | View API Limits | View API rate limits |
| API Usage Alerts | View API Usage Alerts | View API usage alerts |
| API Usage Alerts | Edit API Usage Alerts | Create and update API usage alerts |
| API Usage Data | View API Usage Dashboard | View the API usage dashboard |
| App Settings | Edit App Settings | Create, edit, and update apps within app settings |
| App Settings | View App Settings | View App Settings page |
| Audience Sync Settings | View Audience Sync Settings | View all settings of their connected Audience Sync partners |
| Dashboard Users | Edit Dashboard Users | View, create, and edit company users |
| Email Settings | View Email Settings | View Email Preferences |
| Email Settings | Edit Email Settings | Enable and update Email Preferences |
| Event User Log | View Event User Log | View event user logs |
| Internal Groups | View Internal User Groups | View internal groups |
| Internal Groups | Delete Internal User Groups | Delete internal groups |
| Internal Groups | Edit Internal User Groups | Create and update internal groups |
| Message Activity Log | View Message Activity Log | View message activity logs |
| Multi Language Settings | View Localization Settings | View Multi Language locale settings page |
| Multi Language Settings | Delete Localization Settings | Delete Multi Language locale |
| Multi Language Settings | Edit Localization Settings | Create Multi Language locales |
| Preference Centers | View Preference Centers | View preference centers |
| Preference Centers | Edit Preference Centers | Create and update preference centers |
| Preference Centers | Launch Preference Centers | Make a draft Preference Center active or update an existing one |
| Push Settings | View Push Settings | View Push settings |
| Push Settings | Edit Push Settings | Create and update Push settings |
| SDK Debugger | View SDK Debugger | View SDK Debugger  or debugging sessions |
| SDK Debugger | Edit SDK Debugger | Create and download SDK Debugger sessions |
| Tags | View Tags | View tags |
| Tags | Delete Tags | Permanently delete tags |
| Tags | Edit Tags | Create and update tags |
| Teams | View Teams | View Teams |
| Teams | Archive Teams | Move teams to archive |
| Teams | Edit Teams | Create and update teams |
| WhatsApp Settings | View WhatsApp Settings | View all WhatsApp channel settings |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Decisioning Studio

| Product area | Permission | Definition |
| --- | --- | --- |
| Decisioning Studio Agents | View Decisioning Studio Agent | View Decisioning Studio Agents configuration without making changes |
| Decisioning Studio Audience | View Decisioning Studio Audience | See audience details on Decisioning Studio Agent configuration summaries |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Other

| Product area | Permission | Definition |
| --- | --- | --- |
| App Usage | View Usage Data | View usage data |
| Billing | View Billing Details | View billing details |
| Custom Agents | View Agent Console AI Agents | Allows users to view custom AI agents |
| Custom Agents | Archive Agent Console AI Agents | Allows users to archive custom AI agents |
| Custom Agents | Edit Agent Console AI Agents | Allows users to create and update custom AI agents |
| Custom Attributes Marked As PII | View Custom Attributes Marked as PII | View custom attributes marked as PII |
| Dashboard Reports | View Dashboard Reports | View reports without making changes |
| Dashboard Reports | Delete Dashboard Reports | Permanently delete reports |
| Dashboard Reports | Edit Dashboard Reports | Create and update reports |
| Domain Settings | Edit Domain Settings | Add delegated domains and custom domains under Verified Domains |
| Field Level Encryption | Edit Identifier Field-Level Encryption | Enable and update Field-Level Encryption settings |
| Media Library Assets | View Media Library Assets | View media library assets |
| Media Library Assets | Delete Media Library Assets | Permanently delete media library assets |
| Media Library Assets | Edit Media Library Assets | Create and update media library assets |
| Messaging Rate Limits | View Messaging Rate Limits | View workspace-level messaging rate limits |
| Messaging Rate Limits | Edit Messaging Rate Limits | Configure and edit workspace-level messaging rate limits |
| Operator | Use BrazeAI Operator<sup>TM</sup> | Access and use Braze Operator to answer questions, navigate setup, troubleshoot issues, and brainstorm ideas |
| Placements | View Placements | View Banner placement |
| Placements | Archive Placements | Move Banner placements to archive |
| Placements | Edit Placements | View Banner placements without making changes |
| Promotion Codes | View Promotion Codes | View promo codes |
| Promotion Codes | Export Promotion Codes | Download a list of promo codes from the dashboard |
| Promotion Codes | Edit Promotion Codes | Create and update promo codes |
| Subscription Groups | Edit Subscriptions | Create and update subscription groups |
| Transformations | Edit Data Transformation | Create and update data transformations |
| Transformations | View Data Transformation | View data transformations |
| User Deletion Records | View User Deletion Records | View user deletion records |
| Support Tickets | Create Support Ticket | Create and update Support tickets |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }



