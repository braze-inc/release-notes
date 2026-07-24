# Braze MCP server functions

> The Braze MCP server exposes read and write tools that map to specific Braze REST API endpoints. For more information, see [Braze MCP server].

**Important:**


The remote Braze MCP server is in Early Access. The locally hosted Braze MCP server (beta) is deprecated, remains available for now, and will not receive additional updates.




## Prerequisites

Before you can use this feature, you'll need to [set up the Braze MCP server].

## Available Braze API functions

Your MCP client references these tools to interact with the Braze MCP server.

### Workspaces

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_workspaces` | N/A | read | Discover which Braze workspaces the current OAuth access token can reach. Call this first: each returned workspace `id` is the `app_group_id` every other tool requires. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Workspaces" }

### Campaigns

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_campaign_list` | [`/campaigns/list`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns) | read | Export a list of campaigns with name, campaign API identifier, API-campaign flag, and tags. |
| `get_campaign_details` | [`/campaigns/details`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details) | read | Retrieve relevant information on a specified campaign by `campaign_id`. |
| `get_campaign_dataseries` | [`/campaigns/data_series`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_analytics) | read | Daily series of campaign stats over time (sends, opens, clicks, conversions by channel). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campaigns" }

### Canvases

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_canvas_list` | [`/canvas/list`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvases) | read | Export a list of Canvases with name, Canvas API identifier, and tags. |
| `get_canvas_details` | [`/canvas/details`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_details) | read | Export Canvas metadata: name, time created, current status, and more. |
| `get_canvas_data_series` | [`/canvas/data_series`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics) | read | Export time series data for a Canvas. |
| `get_canvas_data_summary` | [`/canvas/data_summary`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics_summary) | read | Export rollups of Canvas time series data for a concise results summary. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Canvases" }

### Catalogs

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_catalogs` | [`/catalogs`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | read | List catalogs in a workspace. |
| `get_catalog_items` | [`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | read | Return multiple catalog items and their content. |
| `get_catalog_item` | [`/catalogs/{catalog_name}/items/{item_id}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | read | Return a single catalog item and its content. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catalogs" }

### Custom attributes

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_custom_attributes` | [`/custom_attributes`](https://www.braze.com/docs/api/endpoints/export/custom_attributes/get_custom_attributes) | read | Export custom attributes recorded for your app, in groups of 50, alphabetical. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Custom attributes" }

### Custom events

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_events` | [`/events`](https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events_data) | read | Export custom events recorded for your app, in groups of 50, alphabetical (cursor pagination). |
| `get_events_list` | [`/events/list`](https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events) | read | Export custom event names, in groups of 250, alphabetical (page pagination). |
| `get_events_data_series` | [`/events/data_series`](https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events_analytics) | read | Occurrences of a custom event over a designated time period. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Custom events" }

### CDI integrations

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `list_integrations` | [`/cdi/integrations`](https://www.braze.com/docs/api/endpoints/cdi/get_integration_list) | read | List existing Cloud Data Ingestion integrations, 10 per call. |
| `get_integration_job_sync_status` | [`/cdi/integrations/{integration_id}/job_sync_status`](https://www.braze.com/docs/api/endpoints/cdi/get_job_sync_status) | read | Past sync statuses for a given CDI integration, 10 per call. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="CDI integrations" }

### KPI

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_dau_data_series` | [`/kpi/dau/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_dau_date) | read | Daily series of unique active users per date. |
| `get_mau_data_series` | [`/kpi/mau/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_mau_30_days) | read | Daily series of unique active users over a 30-day rolling window. |
| `get_new_users_data_series` | [`/kpi/new_users/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | read | Daily series of total new users per date. |
| `get_uninstalls_data_series` | [`/kpi/uninstalls/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date) | read | Daily series of total uninstalls per date. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="KPI" }

### Media library

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `create_media_library_asset` | [`/media_library/create`](https://www.braze.com/docs/api/endpoints/media_library/manage_assets/create) | create | Upload an asset to the Braze media library through external URL or base64 file content. Exactly one upload mode must be provided. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Media library" }

### Messages

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_scheduled_broadcasts` | [`/messages/scheduled_broadcasts`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | read | List scheduled campaigns and entry Canvases between now and a designated `end_time`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Messages" }

### Purchases

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_product_list` | [`/purchases/product_list`](https://www.braze.com/docs/api/endpoints/export/purchases/get_list_product_id) | read | Paginated list of product IDs. |
| `get_quantity_series` | [`/purchases/quantity_series`](https://www.braze.com/docs/api/endpoints/export/purchases/get_number_of_purchases) | read | Total number of purchases in your app over a time range. |
| `get_revenue_series` | [`/purchases/revenue_series`](https://www.braze.com/docs/api/endpoints/export/purchases/get_revenue_series) | read | Total money spent in your app over a time range. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Purchases" }

### SDK authentication

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_sdk_authentication_keys` | [`/app_group/sdk_authentication/keys`](https://www.braze.com/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | read | Retrieve all SDK authentication keys for an app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="SDK authentication" }

### Segments

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_segment_list` | [`/segments/list`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment) | read | Export segments with name, Segment API identifier, and analytics-tracking flag. |
| `get_segment_details` | [`/segments/details`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment_details) | read | Retrieve relevant information on a segment by `segment_id`. |
| `get_segment_data_series` | [`/segments/data_series`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment_analytics) | read | Daily series of a segment's estimated size over time. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Segments" }

### Sends

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_send_data_series` | [`/sends/data_series`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_send_analytics) | read | Daily stats for a tracked `send_id` (API campaigns). Braze stores send analytics for 14 days after the send. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sends" }

### Sessions

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_session_data_series` | [`/sessions/data_series`](https://www.braze.com/docs/api/endpoints/export/sessions/get_sessions_analytics) | read | Number of sessions for your app over a designated time period. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Sessions" }

### Subscription groups

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_subscription_group_status` | [`/subscription/status/get`](https://www.braze.com/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | read | Subscription state of a user in a subscription group. |
| `get_user_subscription_groups` | [`/subscription/user/status`](https://www.braze.com/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups) | read | List a user's subscription groups. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Subscription groups" }

### Templates

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_email_templates` | [`/templates/email/list`](https://www.braze.com/docs/api/endpoints/templates/email_templates/get_list_email_templates) | read | List available email templates in your Braze account. |
| `get_email_template_info` | [`/templates/email/info`](https://www.braze.com/docs/api/endpoints/templates/email_templates/get_see_email_template_information) | read | Get information for a specific email template. Drag-and-drop editor templates are not accepted. |
| `create_email_template` | [`/templates/email/create`](https://www.braze.com/docs/api/endpoints/templates/email_templates/post_create_email_template) | create | Create an email template on the Braze dashboard. |
| `update_email_template` | [`/templates/email/update`](https://www.braze.com/docs/api/endpoints/templates/email_templates/post_update_email_template) | update | Update an existing email template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Templates" }

### Content blocks

| Tool | API endpoint | Access | Description |
| --- | --- | --- | --- |
| `get_content_blocks` | [`/content_blocks/list`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | read | List existing content block information. |
| `get_content_block_info` | [`/content_blocks/info`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | read | Get information for an existing content block, optionally with campaign or Canvas inclusion data. |
| `create_content_block` | [`/content_blocks/create`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | create | Create a content block. |
| `update_content_block` | [`/content_blocks/update`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block) | update | Update a content block. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Content blocks" }

## Legal disclaimer
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

### How instructions and responses are handled

The Braze MCP server receives instructions from your Third-Party Provider MCP client, such as Claude, ChatGPT, Copilot, Gemini CLI, Codex, or Cursor, exactly as that provider's underlying AI model formulates them. When you type a request in natural language, the AI model interprets your request and translates it into one or more specific tool calls to Braze. Braze receives and executes the tool call as sent. Braze does not see your original natural-language prompt and cannot verify that the generated tool call fully or accurately reflects your intended request.

When Braze returns data or a result, that response is sent back to your Third-Party Provider MCP client, which then interprets, formats, and presents it to you. Braze does not control how the AI model presents, summarizes, or describes returned information.

Braze is not liable for instructions generated by, or responses conveyed through, any Third-Party Provider MCP client. Braze recommends not using "auto-mode" if your Third-Party Provider MCP client offers it for automatic action implementation. Review AI-generated summaries against source data in your Braze dashboard and review any AI-proposed action before implementing it through your Third-Party Provider MCP client.


