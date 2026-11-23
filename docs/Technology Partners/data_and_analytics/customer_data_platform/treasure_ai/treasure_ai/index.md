# Treasure AI

> [Treasure AI](https://www.treasure.ai/) (formerly Treasure Data) is an agentic experience platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and Treasure AI integration allows you to write job results from Treasure AI directly to Braze, letting you:
* Map external IDs from your CRM system to Braze user accounts
* Manage opt-out when an end-user updates their consent choosing not to participate
* Upload tracking of events, purchases, or custom profile attributes to build precise customer segments

## Prerequisites

| Requirement | Description |
| --- | --- |
| Treasure AI account | A [Treasure AI account](https://www.treasure.ai/) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track`, `users.delete`, `users.alias.new`, `users.identify` permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint depends on the [Braze URL for your instance](https://www.braze.com/docs/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Prerequisites" }

## Use cases

You can synchronize your consolidated customer profiles from Treasure AI into Braze to build-out target segments. Treasure AI supports first-party cookie data, Mobile IDs, third-party systems like your CRM, and many more.

## Integration

### Step 1: Create a new connection

In Treasure AI, navigate to the **Catalog** under the **Integrations Hub** and search for and select **Braze**. 

In the **New Authentication** prompt that shows up, name your connection and provide your Braze REST API key and REST endpoint. Select **Done** when finished.

![Treasure AI Braze authentication form with REST API key and endpoint fields.](https://www.braze.com/docs/assets/img/treasure_data/braze_authentication.png?f3b0a591b1a4fb3e1438145cfa87214d){: style="max-width:80%;"}

### Step 2: Define your query

In Treasure AI, navigate to **Queries** under your **Data Workbench** and select a query for which you would like to export data. Run this query to validate the result set.

**Note:**


For users using HIVE to build queries, HIVE requires that any columns or tables that begin with an underscore be wrapped by backquotes. For example, `_merge_objects`.



Next, select **Export Results** and select an existing integration authentication.

![Treasure AI query results page with Export Results and Braze integration selected.](https://www.braze.com/docs/assets/img/treasure_data/query_2.png?cd2c46ce629cad72ca056a4d0657e11a){: style="max-width:80%;"}

Define additional export results parameters as outlined in the following [customization section](#customization). In your export integration content, review the integration parameters.

![The "Export Results" page. On this page are fields for "mode", "track record type", and "pre-formatted fields". For this example, "User-Track" and "Custom Events" are set to these fields, respectively.](https://www.braze.com/docs/assets/img/treasure_data/braze_export_configuration.png?ce649a09eb873f6188563630fa619162){: style="max-width:80%;"}

Finally, select **Done**, run your query, and validate that your data moved to Braze.

### Customization

The export results parameters are included in the following table:

| Parameter                 | Values | Description |
|---------------------------|---|---|
| `mode`                    | User - New Alias<br>User - Identifying<br>User - Track<br>User - Delete | Connector mode |
| `pre_formatted_fields`    | String | Use for array or JSON columns to keep the format. |
| `track_record_type`       | Custom Events<br>Purchases<br>User Profile Attributes| Record type for **User - Track** mode |
| `skip_on_invalid_records` | Boolean | If enabled, continue and ignore any invalid records for the JSON column. <br> Otherwise, the job stops. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Customization" }

**Note:**


Visit [Treasure AI](https://docs.treasure.ai/int/braze-export-integration) for more information about pre-formatted fields, example queries, parameter details, and query export job scheduling.



## Webhooks

Treasure AI users can ingest data through the public REST API. You can use Treasure AI to create custom webhooks into your data. To learn more, visit the [Treasure AI documentation](https://docs.treasure.ai/)

