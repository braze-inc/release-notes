# Zero-copy personalization using CDI

> Learn how to sync Canvas triggers using CDI for zero-copy personalization. This feature accesses user-specific information from your data storage solution and passes it to a destination Canvas. Canvas steps can optionally include personalization fields that are not persisted on Braze user profiles.

## Syncing Canvas triggers

### Quick start steps

If you're already familiar with Braze CDI, note that the setup for a Canvas trigger sync closely follows the process for user data syncs on the same source, with the following caveats:

- Only external ID or user alias identifiers are supported. Email and phone numbers are not supported identifiers.
- Only existing Braze users can be synced. New users cannot be created.
- `PROPERTIES` replaces the `PAYLOAD` column. This is a JSON string of the fields you want to use as Canvas entry properties for personalization.

To get started, select the **Canvas Triggers** data type when creating a new sync.

### Step 1: Set up data source for Canvas triggers {#step-1-set-up-data-source-for-canvas-triggers}

For the source table or file format for your source, open your source page and select the **Canvas triggers** tab. Complete the credentials and network setup on that page as well.

| Source | Canvas trigger setup |
| --- | --- |
| Snowflake | [Snowflake source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/snowflake#step-1-set-up-your-source-table) |
| Amazon Redshift | [Redshift source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/amazon_redshift#step-1-set-up-your-source-table) |
| Google BigQuery | [BigQuery source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/google_bigquery#step-1-set-up-your-source-table) |
| Databricks | [Databricks source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/databricks#step-1-set-up-your-source-table) |
| Microsoft Fabric | [Microsoft Fabric source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/microsoft_fabric#step-4-set-up-your-source-table) |
| Amazon S3 | [Amazon S3 file formats](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/amazon_s3#required-file-formats) |
| Google Cloud Storage | [Google Cloud Storage file formats](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/google_cloud_storage#required-file-formats) |
| Azure Blob Storage | [Azure Blob Storage file formats](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/azure_blob_storage#required-file-formats) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas trigger setup by source" }

If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the Canvas triggers source table.

### Step 2: Configure your destination Canvas {#step-2-configure-your-destination-canvas}

1. Set up your destination Canvas for Canvas triggers. Create a new or select an existing API-triggered Canvas. Refer to [Entry schedule types](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas#entry-schedule-types) for instructions on how to create a Canvas with an API-triggered delivery schedule type.
2. After selecting the API-triggered delivery schedule type, continue with Canvas setup and build your Canvas. Canvases can range from simple single-message sends to complex customer workflows with multiple steps.
3. Within your Canvas steps, use [Canvas entry properties](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) to personalize messages with properties fields that you plan to sync from your source table.
  * For example, if in Step 1 you instrumented a properties field for `account_balance`, you would use the following Liquid templating to personalize your message: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
4. After building your Canvas, launch it and proceed to [Step 3](#step-3-create-your-zero-copy-sync).

### Step 3: Create your zero-copy sync {#step-3-create-your-zero-copy-sync}

With your source setup complete and destination Canvas launched, create a new data sync:

1. In Braze, go to **Data Settings** > **Cloud Data Ingestion**.
2. Set up the connection by entering connection details (or reuse existing credentials) and the source table from [Step 1](#step-1-set-up-data-source-for-canvas-triggers).
3. Provide a name for the integration.
4. Select the **Canvas triggers** data type.
5. Choose your destination Canvas (from [Step 2](#step-2-configure-your-destination-canvas)).
6. Choose a [sync frequency](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion#how-it-works).
7. Set up notification preferences.
8. Select **Test Connection** to confirm everything works as expected. If connecting to Snowflake, first add the public key displayed on the dashboard to the user created for Braze to connect to Snowflake. To complete this step, you'll need **SECURITYADMIN** access or higher in Snowflake.
9. Save the sync to begin syncing Canvas triggers.

When the sync runs, users in your source table begin to enter the Canvas. Use Canvas analytics and the Cloud Data Ingestion sync logs page to monitor performance.

**Tip:**


Review your entire configuration (from sync behavior to Canvas setup) to avoid unexpected sends. Canvas settings such as rate limiting, frequency capping, and segmentation filters can further refine message delivery.<br><br>Braze recommends conducting a trial run with a small or test audience before implementing production use cases.



## Considerations

CDI Canvas triggers utilize your REST API rate limit for `/canvas/trigger/send`. If you're using this endpoint simultaneously with CDI Canvas triggers and your REST API integration, expect the combined usage to count towards your rate limit.

Each sync run enters users into its respective destination Canvas at a maximum rate of approximately 3.75 million users per hour. Be prepared for longer source-to-Canvas entry times when:

* Syncing more than 3.75 million users per sync run.
* Using CDI Canvas triggers when already saturating your REST API's [rate limit for `/canvas/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases#endpoint-reference).

Consider the following about zero-copy CDI when Message Archiving is enabled:

* The results of the table are temporarily stored in Braze during processing. They are also exported to Snowflake for 30 days so you can view exactly what was synced.
* Archived messages are not saved anywhere within Braze. The copies are sent to be stored exclusively in your configured storage.
* When using zero-copy CDI with Canvas triggers, Braze doesn't store a backup of the query results from the data warehouse and no data is copied into the user profile.
* Canvas context properties may be logged in internal systems for up to 30 days.
