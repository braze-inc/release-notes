# Braze MCP server functions

> The Braze MCP server exposes read and write tools. Most map to Braze REST API endpoints. Some are available only through the MCP server. For more information, see [Braze MCP server].

**Important:**


The locally hosted Braze MCP server (beta) is deprecated and doesn't receive additional updates.




**Note:**


The Braze MCP server includes tools that are only available to customers participating in beta programs. If you try to access a tool that is part of a beta program and your account does not have the feature enabled, you may receive an error response. To join a beta program, contact your account manager.



## Prerequisites

Before you can use this feature, you'll need to [set up the Braze MCP server].

## Available Braze API functions

Your MCP client references these tools to interact with the Braze MCP server. Tools labeled "MCP only" in the API endpoint column are available only through the Braze MCP server. They don't have a corresponding public REST API endpoint.

### Workspaces

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_workspaces` | MCP only | read | None | Discover which Braze workspaces the current OAuth access token can reach. Call this first: each returned workspace `id` is the `app_group_id` every other tool requires. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Workspaces" }

### Campaigns

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns) | read | View campaign analytics | Export a list of campaigns with name, campaign API identifier, API-campaign flag, and tags. |
| `get_campaign_details` | [`/campaigns/details`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details) | read | View campaign analytics | Retrieve relevant information on a specified campaign by `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_analytics) | read | View campaign analytics | Daily series of campaign stats over time (sends, opens, clicks, conversions by channel). |
| `duplicate_campaign` | [`/campaigns/duplicate`](https://www.braze.com/docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns) | create | Create campaigns | Duplicate an existing campaign. |
| `create_campaign` | MCP only | create | Create campaigns | Create a new campaign. |
| `edit_campaign` | MCP only | update | Edit campaigns | Edit an existing campaign. |
| `launch_campaign`<sup>*</sup> | MCP only | update | Launch campaigns | Launch a campaign. |
| `stop_campaign` | MCP only | update | Stop campaigns | Stop a running campaign. |
| `archive_campaign`<sup>*</sup> | MCP only | update | Archive campaigns | Archive a campaign. |
| `unarchive_campaign`<sup>*</sup> | MCP only | update | Archive campaigns | Unarchive a campaign. |
| `get_campaign_draft` | MCP only | read | View campaign analytics | Retrieve draft campaign details. |
| `get_campaign_live_details` | MCP only | read | View campaign analytics | Retrieve live campaign details. |
| `create_campaign_message` | MCP only | create | Edit campaigns | Create a message within a campaign. |
| `update_campaign_message` | MCP only | update | Edit campaigns | Update a campaign message. |
| `delete_campaign_message` | MCP only | delete | Edit campaigns | Delete a campaign message. |
| `create_campaign_message_variation` | MCP only | create | Edit campaigns | Create a message variation within a campaign. |
| `update_campaign_message_variation` | MCP only | update | Edit campaigns | Update a campaign message variation. |
| `delete_campaign_message_variation` | MCP only | delete | Edit campaigns | Delete a campaign message variation. |
| `update_campaign_distribution` | MCP only | update | Edit campaigns | Update campaign distribution settings. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Campaigns" }

The campaign tools are generally available and don't require you to join a beta program, except for the tools marked with an asterisk (*).

<sup>*</sup> This tool is only available to customers participating in the campaign APIs beta program. If your account does not have this feature enabled, you may receive an error when attempting to use it. To join the beta program, contact your account manager.
{: .reset-td-br-1 }

### Canvases

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvases) | read | View Canvas analytics | Export a list of Canvases with name, Canvas API identifier, and tags. |
| `get_canvas_details` | [`/canvas/details`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_details) | read | View Canvas analytics | Export Canvas metadata: name, time created, current status, and more. |
| `get_canvas_data_series` | [`/canvas/data_series`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics) | read | View Canvas analytics | Export time series data for a Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics_summary) | read | View Canvas analytics | Export rollups of Canvas time series data for a concise results summary. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Canvases" }

### Catalogs

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | read | View catalogs | List catalogs in a workspace. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | read | View catalog items | Return multiple catalog items and their content. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | read | View catalog items | Return a single catalog item and its content. |
| `create_catalog` | [`/catalogs`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | create | Manage catalogs | Create a catalog. |
| `delete_catalog` | [`/catalogs/{catalog_name}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | delete | Manage catalogs | Delete a catalog. |
| `create_catalog_fields` | [`/catalogs/{catalog_name}/fields`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields) | create | Manage catalog fields | Create multiple fields in a catalog. |
| `delete_catalog_field` | [`/catalogs/{catalog_name}/fields/{field_name}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field) | delete | Manage catalog fields | Delete a catalog field. |
| `create_catalog_items` | [`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | create | Manage catalog items | Create multiple items in a catalog. Up to 50 items per request. |
| `edit_catalog_items` | [`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | update | Manage catalog items | Edit multiple existing items in a catalog. Up to 50 items per request. |
| `replace_catalog_items` | [`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | update | Manage catalog items | Replace multiple items in a catalog. Creates items if they don't exist. Up to 50 items per request. |
| `delete_catalog_items` | [`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | delete | Manage catalog items | Delete multiple items in a catalog. Up to 50 items per request. |
| `create_catalog_selection` | [`/catalogs/{catalog_name}/selections`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | create | Manage catalog selections | Create a selection in a catalog. |
| `delete_catalog_selection` | [`/catalogs/{catalog_name}/selections/{selection_name}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection) | delete | Manage catalog selections | Delete a catalog selection. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Catalogs" }

### Custom attributes

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`](https://www.braze.com/docs/api/endpoints/export/custom_attributes/get_custom_attributes) | read | View custom events, attributes, and purchases | Export custom attributes recorded for your app, in groups of 50, alphabetical. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Custom attributes" }

### Custom events

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_events` | [`/events`](https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events_data) | read | View custom events, attributes, and purchases | Export custom events recorded for your app, in groups of 50, alphabetical (cursor pagination). |
| `get_events_list` | [`/events/list`](https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events) | read | View custom events, attributes, and purchases | Export custom event names, in groups of 250, alphabetical (page pagination). |
| `get_events_data_series` | [`/events/data_series`](https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events_analytics) | read | View custom events, attributes, and purchases | Occurrences of a custom event over a designated time period. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Custom events" }

### CDI integrations

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`](https://www.braze.com/docs/api/endpoints/cdi/get_integration_list) | read | View Cloud Data Ingestion job status | List existing Cloud Data Ingestion integrations, 10 per call. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`](https://www.braze.com/docs/api/endpoints/cdi/get_job_sync_status) | read | View Cloud Data Ingestion job status | Past sync statuses for a given CDI integration, 10 per call. |
| `trigger_integration_sync` | [`/cdi/integrations/{integration_id}/sync`](https://www.braze.com/docs/api/endpoints/cdi/post_job_sync) | write | Sync Cloud Data Ingestion integrations | Trigger a sync for a given CDI integration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="CDI integrations" }

### KPI

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_dau_date) | read | View KPI data | Daily series of unique active users per date. |
| `get_mau_data_series` | [`/kpi/mau/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_mau_30_days) | read | View KPI data | Daily series of unique active users over a 30-day rolling window. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | read | View KPI data | Daily series of total new users per date. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date) | read | View KPI data | Daily series of total uninstalls per date. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="KPI" }

### Media library

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`](https://www.braze.com/docs/api/endpoints/media_library/manage_assets/create) | create | Manage media library assets | Upload an asset to the Braze media library through external URL or base64 file content. Exactly one upload mode must be provided. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Media library" }

### Purchases

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`](https://www.braze.com/docs/api/endpoints/export/purchases/get_list_product_id) | read | View custom events, attributes, and purchases | Paginated list of product IDs. |
| `get_quantity_series` | [`/purchases/quantity_series`](https://www.braze.com/docs/api/endpoints/export/purchases/get_number_of_purchases) | read | View custom events, attributes, and purchases | Total number of purchases in your app over a time range. |
| `get_revenue_series` | [`/purchases/revenue_series`](https://www.braze.com/docs/api/endpoints/export/purchases/get_revenue_series) | read | View custom events, attributes, and purchases | Total money spent in your app over a time range. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Purchases" }

### Segments

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment) | read | View segments | Export segments with name, Segment API identifier, and analytics-tracking flag. |
| `get_segment_details` | [`/segments/details`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment_details) | read | View segments | Retrieve relevant information on a segment by `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment_analytics) | read | View segments | Daily series of a segment's estimated size over time. |
| `get_segment_filters` | MCP only | read | View segments | Retrieve segment filter definitions. |
| `create_segment` | MCP only | create | Create segments | Create a new segment. |
| `edit_segment` | MCP only | update | Edit segments | Edit an existing segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Segments" }

The segment tools are generally available and don't require you to join a beta program.

**Note:**


The MCP tools are the supported way to manage Campaigns and Segments programmatically. The underlying APIs that power these tools are not listed in our public API documentation, and using them directly is not supported. Braze Support can't assist with issues from direct use of these APIs unless your company is enrolled in the API beta. For production workflows, use the MCP tools.



### Sends

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_send_analytics) | read | View send data | Daily stats for a tracked `send_id` (API campaigns). Braze stores send analytics for 14 days after the send. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Sends" }

### Sessions

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`](https://www.braze.com/docs/api/endpoints/export/sessions/get_sessions_analytics) | read | View session data | Number of sessions for your app over a designated time period. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Sessions" }

### Templates

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`](https://www.braze.com/docs/api/endpoints/templates/email_templates/get_list_email_templates) | read | View email templates | List available email templates in your Braze account. |
| `get_email_template_info` | [`/templates/email/info`](https://www.braze.com/docs/api/endpoints/templates/email_templates/get_see_email_template_information) | read | View email templates | Get information for a specific email template. Drag-and-drop editor templates are not accepted. |
| `create_email_template` | [`/templates/email/create`](https://www.braze.com/docs/api/endpoints/templates/email_templates/post_create_email_template) | create | Manage email templates | Create an email template on the Braze dashboard. |
| `update_email_template` | [`/templates/email/update`](https://www.braze.com/docs/api/endpoints/templates/email_templates/post_update_email_template) | update | Manage email templates | Update an existing email template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Templates" }

### Content blocks

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | read | View content blocks | List existing content block information. |
| `get_content_block_info` | [`/content_blocks/info`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | read | View content blocks | Get information for an existing content block, optionally with campaign or Canvas inclusion data. |
| `create_content_block` | [`/content_blocks/create`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | create | Manage content blocks | Create a content block. |
| `update_content_block` | [`/content_blocks/update`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block) | update | Manage content blocks | Update a content block. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Content blocks" }

### Operator

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `send_operator_prompt` | MCP only | update | Use BrazeAI Operator | Send a natural-language prompt to the BrazeAI Operator. Submits a background job and returns a job_id. |
| `get_operator_result` | MCP only | read | Use BrazeAI Operator | Poll for the result of a submitted Operator job using its job_id. |
| `cancel_operator_job` | MCP only | update | Use BrazeAI Operator | Cancel a running Operator job. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Operator" }

**Important:**


These tools are only available to customers participating in the Operator beta program. If your account does not have this feature enabled, you may receive an error when attempting to use it. To join the beta program, contact your account manager.



### Skills

| Tool | API endpoint | Access | Permission | Description |
| --- | --- | --- | --- | --- |
| `get_operator_skills` | MCP only | read | View Skills | List the workspace's skills, with each skill's name and description. |
| `get_operator_skill` | MCP only | read | View Skills | Read a skill, including its instructions. |
| `create_operator_skill` | MCP only | create | View Skills, Edit Skills | Create a skill. If the name is already in use, Braze adds a suffix. |
| `update_operator_skill` | MCP only | update | View Skills, Edit Skills | Edit a skill. Fields you leave out keep their current values. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Skills" }

For more information, see [Skills](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities/skills).

## Legal disclaimer
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

### How instructions and responses are handled

The Braze MCP server receives instructions from your Third-Party Provider MCP client, such as Claude, ChatGPT, Copilot, Gemini CLI, Codex, or Cursor, exactly as that provider's underlying AI model formulates them. When you type a request in natural language, the AI model interprets your request and translates it into one or more specific tool calls to Braze. Braze receives and executes the tool call as sent. Braze does not see your original natural-language prompt and cannot verify that the generated tool call fully or accurately reflects your intended request.

When Braze returns data or a result, that response is sent back to your Third-Party Provider MCP client, which then interprets, formats, and presents it to you. Braze does not control how the AI model presents, summarizes, or describes returned information.

Braze is not liable for instructions generated by, or responses conveyed through, any Third-Party Provider MCP client. Braze recommends not using "auto-mode" if your Third-Party Provider MCP client offers it for automatic action implementation. Review AI-generated summaries against source data in your Braze dashboard and review any AI-proposed action before implementing it through your Third-Party Provider MCP client.


