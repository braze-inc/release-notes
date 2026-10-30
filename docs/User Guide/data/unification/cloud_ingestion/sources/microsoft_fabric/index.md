# Cloud Data Ingestion for Microsoft Fabric

> This page covers everything you need to sync data from Microsoft Fabric to Braze using Cloud Data Ingestion (CDI): the resources to create in Fabric, how to connect the source and create a sync in Braze, the source table for each data type, and Fabric-specific troubleshooting.

## Setup overview

1. Set up authentication for Braze, using one of the supported [authentication methods](#set-up-authentication), and grant access to Fabric APIs.
2. Set up a shared workspace and grant the service principal access to it.
3. In the shared Fabric workspace, set up the tables or views you want to sync to Braze.
4. Create a new source and sync in the Braze dashboard.
5. Validate the integration and start the sync.

## Step 1: Set up authentication {#set-up-authentication}

Braze connects to your Fabric warehouse with the following authentication method:


| Method | How Braze authenticates | What you enter in Braze |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Authentication methods for " }





## Step 2: Grant access to Fabric resources

Provide access for Braze to connect to your Fabric instance. In your Fabric admin portal, navigate to **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**.

* In **Developer settings** enable **Service principals can use Fabric APIs** so Braze can connect using Microsoft Entra ID.
* In **OneLake settings** enable **Users can access data stored in OneLake with apps external to Fabric** so that the service principal can access data from an external app.

## Step 3: Set up a shared workspace and grant access

Any Fabric resources you want to connect to Braze must be placed in a shared workspace. If you've only been using the default **My Workspace**, create a new shared workspace:

1. On the navigation menu, select **Workspaces**, then select **+ New workspace**.
2. Enter a **Name** for the workspace, then select **Apply**.

After you have a shared workspace, grant the service principal access:

1. Select the workspace, then select **Manage Access**.
2. Select **+ Add people or groups**.
3. Search for and select the name of the service principal you created in Step 1. If it doesn't appear, confirm you've enabled the **Service principals can use Fabric APIs** setting in Step 2.
4. In the role dropdown, select **Contributor**.

The service principal can now access Fabric warehouse resources in this workspace through their SQL endpoints, including the warehouse to use for Braze.

## Step 4: Set up your source table

The steps in this section create a table with a `PAYLOAD` column. If you plan to map columns with **Visual** or write a query with **SQL** on the **Data definition** step, you can use an existing table or view instead. Skip the table creation step, and grant Braze read access to the tables or views you want to sync. For a comparison of options, see [Choose a data definition option](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/table_setup#choose-a-data-definition-option).

Braze supports both tables and views in Fabric warehouses. If you need to create a new warehouse, create it within the shared workspace from Step 3. Go to **Create** > **Data Warehouse** > **Warehouse** in the Fabric console.

You can name the warehouse, schema, and table or view as you'd like, but the column names should match the definitions in the following tabs.

**Note:**


If you use a `PAYLOAD` column, your source table or view can include columns that aren't listed in the following tabs (for example, auditing or hashing). Braze reads only the columns described in these tabs; other columns are not used during Cloud Data Ingestion syncs.



Select the tab for the data type you want to sync.




User attributes, custom events, and purchase events all use the same source table shape. Only the contents of `PAYLOAD` differ.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

- `UPDATED_AT` - The time this row was updated in or added to the table. Braze syncs rows where `UPDATED_AT` is later than the last synced value. Rows at the exact boundary timestamp may be re-synced if new rows share that same timestamp.
- **User identifier columns** - Your table may contain one or more user identifier columns. Each row should only contain one identifier (either `external_id`, the combination of `alias_name` and `alias_label`, `braze_id`, `email` or `phone`). A source table may have columns for one, two, three, four, or all five identifier types.
    - `EXTERNAL_ID` - This identifies the user you want to update. This should match the `external_id` value used in Braze.
    - `ALIAS_NAME` and `ALIAS_LABEL` - These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - The Braze user identifier. This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias.
    - `EMAIL` - The user's email address. If multiple profiles with the same email address exist, the most recently updated profile is prioritized for updates. If you include both email and phone, email is used as the primary identifier.
    - `PHONE` - The user's phone number. If multiple profiles with the same phone number exist, the most recently updated profile is prioritized for updates.

- `PAYLOAD` - This is a JSON string of the fields you want to sync to the user in Braze.

For attribute syncs, `PAYLOAD` follows the [user attributes object](https://www.braze.com/docs/api/objects_filters/user_attributes_object) format. You can include nested custom attributes, arrays of objects, and subscription group statuses. For payload examples, see [Table setup](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/table_setup#payload-examples).




Custom events use the same source table as user attributes. Create the table shown in the **User attributes** tab, then populate `PAYLOAD` with an [events object](https://www.braze.com/docs/api/objects_filters/event_object).

To sync events, an event name is required. Format the `time` field as an ISO 8601 string or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. If the `time` field is not present, Braze uses the `UPDATED_AT` column value as the event time. Other fields, including `app_id` and `properties`, are optional.

You can sync one event per row.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
    }
}
```




Purchase events use the same source table as user attributes. Create the table shown in the **User attributes** tab, then populate `PAYLOAD` with a [purchases object](https://www.braze.com/docs/api/objects_filters/purchase_object).

To sync purchase events, `product_id`, `currency`, and `price` are required. Format the optional `time` field as an ISO 8601 string or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. If the `time` field is not present, Braze uses the `UPDATED_AT` column value as the event time. Other fields, including `app_id`, `quantity`, and `properties`, are optional.

You can sync one purchase event per row.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```




Before you create a catalog sync, create the target catalog in Braze. For the full catalog workflow, see [Sync and delete catalog data](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

The name of the integration must **exactly match** the name of the catalog you created in Braze.

Braze recommends creating a view from your catalog data so the source table fully refreshes each time a sync runs. For example, if you have a table of product data (`product_catalog`) with `id` and four additional attributes, you could sync the following view:

```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```




Canvas triggers power zero-copy personalization. For the destination Canvas setup and considerations, see [Zero-copy personalization](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/zero_copy_sync).

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

Canvas trigger syncs differ from other user data syncs in three ways:

- Only external ID or user alias identifiers are supported. Email and phone numbers are not supported identifiers.
- Only existing Braze users can be synced. New users cannot be created.
- `PROPERTIES` replaces the `PAYLOAD` column. This is a JSON string of the fields you want to use as Canvas entry properties for personalization.

Your Canvas triggers table needs the following columns:

- `UPDATED_AT` - The time this row was updated or added to the table. Braze syncs rows where `UPDATED_AT` is later than the last synced value. Rows at the exact boundary timestamp may be re-synced if new rows share that same timestamp.
- Either `EXTERNAL_ID` or `ALIAS_NAME` and `ALIAS_LABEL` as the user identifier column. These identify the users for whom you want to trigger Canvas messaging.
    - `EXTERNAL_ID` - Identifies the user to enter into the Canvas. This should match the `external_id` value used in Braze.
    - `ALIAS_NAME` and `ALIAS_LABEL` - These columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the alias type. Users may have multiple aliases with different labels, but only one `alias_name` per `alias_label`.
- `PROPERTIES` - A JSON string of fields to make available as personalization properties in your Canvas. This should contain user-specific information.

**Note:**


Properties are not required for every row or user. However, properties values must be a valid JSON string. Input an empty `{}` string if there are no properties for the row.




Create a service principal and grant permissions. If you already have credentials from another sync, you can reuse them, but make sure they have access to the Canvas triggers table.

To get started, select the **Canvas Triggers** data type when creating a new sync.




Source tables for user deletes should include one or more user identifier types and an `UPDATED_AT` timestamp. Payload columns aren't supported for user delete data.

- `UPDATED_AT` - The time this row was updated or added to the table. Braze syncs rows where `UPDATED_AT` is later than the last synced value. Rows at the exact boundary timestamp may be re-synced if new rows share that same timestamp.
- **User identifier columns** - Each row should only contain one identifier: either `external_id`, the combination of `alias_name` and `alias_label`, or `braze_id`. A source table may contain columns for one, two, or all three identifier types.
    - `EXTERNAL_ID` - This identifies the user you want to update. This should match the `external_id` value used in Braze.
    - `ALIAS_NAME` and `ALIAS_LABEL` - These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels but only one `alias_name` per `alias_label`.
    - `BRAZE_ID` - The Braze user identifier. This is generated by the Braze SDK and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias.

**Important:**


Do not include a `PAYLOAD` column in your table for user removal. To prevent accidental, permanent removal of users, a sync fails if a payload column is provided in the source table. Any other columns are allowed but are ignored by Braze.




```sql
CREATE OR ALTER TABLE [warehouse].[schema].[users_deletes]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  --at least one of external_id, alias_name and alias_label, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR
)
GO
```

On the **Create import sync** page, set the **Data Type** to **Delete Users** so that the proper actions are taken during the integration run. For more information, see [Delete users with Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/delete_users).

**Warning:**


Deleting user profiles cannot be undone. The delete action permanently removes users, which may cause discrepancies in your data. For details, see [Effects of deleting user profiles](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete#endpoint-reference).






## Step 5: Get the warehouse connection string

To retrieve the SQL endpoint for your warehouse, go to the **workspace** in Fabric, hover over the warehouse name in the item list, and select **Copy SQL connection string**.

![The "Fabric Console" page in Microsoft Azure, where users should retrieve the SQL Connection String.](https://www.braze.com/docs/assets/img/cloud_ingestion/fabric_1.png?6f3af1de9162d78cea9fab3e97093463)

## Step 6: Allow Braze IPs in your firewall (optional) {#allow-braze-ips}

Depending on the configuration of your Microsoft Fabric account, you may need to allow the following IP addresses in your firewall to allow traffic from Braze. For more information on enabling this, see the relevant documentation on [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).















<!--The following section is the list of IPs for IP allowlisting-->




## Step 7: Create a new source in the Braze dashboard

In the Braze dashboard, go to **Data Settings** > **Cloud Data Ingestion** > **Sources**, select **Add data source**, and then select **Microsoft Fabric**.

### Step 7.1: Add Microsoft Fabric connection information

Choose a name for your source and input your Microsoft Fabric credentials and configuration.

- **Credentials Name** is a label for these credentials in Braze, you can set a helpful value here.
- For the authentication method you set up in [Step 1](#set-up-authentication), enter its credentials. 


- For **Connection String**, see [Step 5](#step-5-get-the-warehouse-connection-string).

### Step 7.2: Test connection and connect to source

Next, select **Test connection**. Once successful, finalize remaining settings and click **Connect to Source**. If the connection fails, an error message appears to help troubleshoot the issue.

**Note:**


You must successfully test a source before it can be created. If you close the creation page, your source is not saved.



## Step 8: Create a new sync in the Braze dashboard

Go to **Data Settings** > **Cloud Data Ingestion** > **Syncs**, and select **Create data sync**.

### Configure sync details and define your data

Enter a name for your sync. Then, select an active source and a sync data type. Next, select **Visual** or **Table** and enter your source table, or select **SQL** to write a custom SQL query. Finally, select **Preview and validate**.

After validation succeeds, a preview of the data appears. Select **Next: Notifications** to continue. If validation fails, an error message appears to help troubleshoot the issue.

**Note:**


You must successfully validate a sync before progressing to next steps. If you need to close out of the sync creation page, select **Save as draft** to keep your work in progress.



### Add notification preferences

Input contact email(s) for sync error notifications. Braze uses this contact information to send notifications about integration errors, such as unexpected loss of table access.

Contact emails only receive notifications of global or sync-level errors such as missing tables, permissions, and others. They do not receive row-level issues. Global errors indicate critical problems with the connection that prevent syncs from running.

Such problems can include the following:

- Connectivity issues
- Lack of resources
- Permissions issues
- Catalog tier is out of space (catalog syncs only)

### Set the schedule

Lastly, configure your sync as non-recurring or recurring.

Non-recurring syncs run only when you select **Sync Now** in the dashboard or call the [Trigger a sync](https://www.braze.com/docs/api/endpoints/cdi/post_job_sync) endpoint.

Recurring syncs can run as often as every 5 minutes or as rarely as once per month. By default, the shortest interval you can set in the dashboard is 15 minutes, which helps manage your warehouse compute costs and request volume. To sync as often as every 5 minutes, contact Braze Support or your customer success manager. Braze schedules recurring syncs in UTC.


**Note:**


You must successfully validate an integration before it can move from Draft to Active state. If you close the creation page, your integration is saved, and you can revisit the details page to make changes and validate.



## Run the sync

When activated, your sync runs on the schedule configured during setup. If you want to run the sync outside its schedule or to fetch the most recent data, select **Sync Now**. This run does not impact regularly scheduled future syncs. To start a sync automatically when your data updates, call the [Trigger a sync](https://www.braze.com/docs/api/endpoints/cdi/post_job_sync) endpoint from your pipeline.

## Set up additional integrations or users (optional)

You can set up multiple integrations with Braze. When creating additional syncs, you can reuse existing credentials if connecting to the same Fabric account.

If you reuse the same user across integrations, you cannot delete the user in the Braze dashboard until it's removed from all active syncs.

## Use Microsoft Fabric as a connected source

A connected source is a zero-copy alternative to syncing data into Braze. Braze queries your Fabric warehouse directly to build CDI segments, without copying the underlying data. For concepts, limitations, and cost implications, see [Connected sources](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/connected_sources).

### Step 1: Set up authentication and grant access

Follow the same setup described in [Step 1](#set-up-authentication), [Step 2](#step-2-grant-access-to-fabric-resources), and [Step 3](#step-3-set-up-a-shared-workspace-and-grant-access). Then, retrieve the warehouse connection string as described in [Step 5](#step-5-get-the-warehouse-connection-string), and allow Braze IPs as described in [Step 6](#allow-braze-ips).

In your Fabric workspace, set up the source data and grant permissions to your service principal. The connected source may reference one or more tables, so ensure your Braze service principal has permission to access all tables you want in the connected source.

### Step 2: Create the connected source in Braze

Go to **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, select **Add data source**, and then select **Microsoft Fabric**.

In **Setup source**, enter the following:

- **Credentials:** **Credentials Name**, **Connection String**, and the fields for your [authentication method](#set-up-authentication). 


- **Configuration:** **Database** and **Schema**

If **Connect with SSH Tunnel** is available in your workspace and needed for your setup, also enter **Tunnel Host**, **Tunnel Port**, and **Tunnel Username**.

Choose a name for the connected source. This name is used in the list of available sources when you create a new CDI Segment Extension.

Configure a maximum runtime for this source. Braze automatically aborts any queries that exceed the maximum runtime. The maximum runtime allowed is 60 minutes; a lower runtime reduces costs incurred on your Microsoft Fabric account. This setting applies to queries run through this source, including syncs and CDI Segment Extensions that use it.

**Note:**


If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or scaling the Fabric capacity.



Select **Test Connection** to verify that the list of tables visible to the user is what you expect, then select **Done**. Your connected source is now created and ready to use in CDI Segment Extensions.

You may set up multiple connected sources with Braze, but each source should be configured to connect a different schema. When creating additional sources, you may reuse existing credentials if connecting to the same Azure account.

## Format a payload from existing columns

If you prefer to store each attribute in its own column internally, you need to convert those columns to a JSON string to populate the sync with Braze. Use this query in Microsoft Fabric to format source columns into CDI fields.

```sql
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```

For more optimization guidance, see [Cloud Data Ingestion best practices](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/best_practices).

## Troubleshooting

### Test Connection runs slow

Test Connection is running on your data warehouse, so increasing capacity may improve its speed.

### Service principal secret has expired

Azure doesn't allow unlimited expiry on service principal secrets. If syncs begin failing with authentication errors, refresh the client secret in Microsoft Entra ID and update the credentials in Braze.

### Where to run SQL checks

Run validation checks directly in the Fabric SQL query editor, against the same table or view used by your CDI integration. Fabric doesn't support `LIMIT`, so use an equivalent syntax such as `TOP`.

## Related pages

- [Table setup](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/table_setup) for required columns and payload formatting
- [Best practices](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/best_practices) for sync scheduling and data point efficiency
- [Sync logs and observability](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs) for monitoring sync runs
- [FAQ](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs) for common questions across all sources

