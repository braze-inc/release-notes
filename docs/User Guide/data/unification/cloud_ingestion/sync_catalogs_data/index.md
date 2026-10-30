# Sync and delete catalog data

> This page discusses how to sync catalog data with Cloud Data Ingestion (CDI). Catalog syncs are supported for every CDI source, and the source table or file format for each one is documented on that source's page.

## Step 1: Create a new catalog

Before creating a new CDI integration for [catalogs](https://www.braze.com/docs/user_guide/data/activation/catalogs), you need to create a new catalog or identify an existing catalog you want to use for the integration. There are a few ways to create a new catalog and any of these will work for the CDI integration:

- Upload a [CSV](https://www.braze.com/docs/user_guide/data/activation/catalogs/create)
- Create a catalog in the [Braze dashboard](https://www.braze.com/docs/user_guide/data/activation/catalogs/create) or during CDI setup.
- Create a catalog using the [Create catalog endpoint](https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)

Any changes to the catalog schema (for example, adding new fields or changing field type) must be made through the catalog dashboard before updated data is synced through CDI. Braze recommends making these updates when the sync is paused or not scheduled to run to avoid conflicts between your data warehouse data and the schema in Braze.

## Step 2: Set up the catalog sync {#step-2-set-up-the-catalog-sync}

The setup for a catalog sync closely follows the process for user data syncs on the same source. Open your source page and select the **Catalog items** tab for the source table or file format, then complete the rest of the setup on that page.

| Source | Catalog setup |
| --- | --- |
| Snowflake | [Snowflake source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/snowflake#step-1-set-up-your-source-table) |
| Amazon Redshift | [Redshift source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/amazon_redshift#step-1-set-up-your-source-table) |
| Google BigQuery | [BigQuery source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/google_bigquery#step-1-set-up-your-source-table) |
| Databricks | [Databricks source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/databricks#step-1-set-up-your-source-table) |
| Microsoft Fabric | [Microsoft Fabric source table](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/microsoft_fabric#step-4-set-up-your-source-table) |
| Amazon S3 | [Amazon S3 file formats](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/amazon_s3#required-file-formats) |
| Google Cloud Storage | [Google Cloud Storage file formats](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/google_cloud_storage#required-file-formats) |
| Azure Blob Storage | [Azure Blob Storage file formats](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/azure_blob_storage#required-file-formats) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catalog setup by source" }

Whichever source you use, the following applies:

- Select the **Catalogs** sync type when creating the sync.
- The name of the integration must **exactly match** the name of the catalog you previously created.
- If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.

### Required columns

| Column | Required? | Description |
| --- | --- | --- |
| `ID` | Yes | The ID of the catalog item to create or update. |
| `PAYLOAD` | Yes | A JSON string of the fields to sync to the catalog item in Braze. |
| `DELETED` | Optional | When set to `true`, the corresponding catalog item is removed from the catalog. |
| `UPDATED_AT` | Data warehouse sources only | The time this row was updated or added. File storage sources don't support `UPDATED_AT` columns. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Required catalog columns" }

## How the integration works

**Note:**


The sync behavior in this section applies to data warehouse integrations only. For file storage, Braze processes new files as they're uploaded to your bucket or container.



Each time the sync runs, Braze pulls in all rows where `UPDATED_AT` is later than the last synced value. Rows at the exact boundary timestamp may be re-synced if new rows share that same timestamp.

Braze recommends creating a view in your data warehouse from your catalog data to set up a source table that fully refreshes each time a sync runs. With views, you don't need to rewrite the query each time. For a worked example in your warehouse's SQL dialect, see the **Catalog items** tab on your source page.

Whichever source you use:

- The data fetched from the integration is used to create or update items in the target catalog based on the `id` provided.
- If `DELETED` is set to `true`, the corresponding catalog item is deleted.
- The sync doesn't log data points, but all data synced counts toward your total catalog usage. This usage is measured based on the total data stored, so you don't need to worry about only syncing changed data.
