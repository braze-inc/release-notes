## Choose a source

Cloud Data Ingestion connects to two categories of source, and the category determines how syncs are triggered.

| Source category | Sources | How syncs run |
| --- | --- | --- |
| Data warehouse | Snowflake, Amazon Redshift, Google BigQuery, Databricks, Microsoft Fabric | On a schedule you set, as often as every 5 minutes or as rarely as once per month, or on demand through the API. Braze queries your source table for rows where `UPDATED_AT` is later than the last synced value. |
| File storage | Amazon S3, Google Cloud Storage, Azure Blob Storage | Event-driven. Your provider publishes a notification when a new file lands, and Braze ingests that file. File storage sources don't use `UPDATED_AT`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Choose a source" }

## What each source page covers

Every source page follows the same shape, so you can set up any source without reading across multiple articles:

- The resources to create in your warehouse or cloud account, including roles, users, service accounts, and network access.
- A **Set up authentication** section that lists the authentication methods the source supports, with setup steps for each method.
- How to create the source and the sync in the Braze dashboard.
- A tab for each data type you can sync from that source, covering user attributes, custom events, purchase events, catalog items, Canvas triggers, and user deletions.
- Source-specific query optimization and troubleshooting.

## Authentication methods by source

Each source supports one or more ways for Braze to authenticate. Select a source to go to its **Set up authentication** section.


| Source | Authentication methods |
| --- | --- |
| [Snowflake](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/snowflake#set-up-authentication) | Key pair authentication |
| [Amazon Redshift](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/amazon_redshift#set-up-authentication) | Username and password |
| [Google BigQuery](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/google_bigquery#set-up-authentication) | Workload Identity Federation, Service account key |
| [Databricks](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/databricks#set-up-authentication) | OAuth M2M (recommended), Personal access token |
| [Microsoft Fabric](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/microsoft_fabric#set-up-authentication) | Service principal |
| [Amazon S3](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/amazon_s3#set-up-authentication) | IAM role |
| [Google Cloud Storage](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/google_cloud_storage#set-up-authentication) | Workload Identity Federation, Service account key |
| [Azure Blob Storage](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/azure_blob_storage#set-up-authentication) | Service principal |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Authentication methods by source" }


## Data types by source

Not every data type is available for every source. Use this table to confirm what a source supports before you start.

| Data type | Data warehouse sources | File storage sources |
| --- | --- | --- |
| User attributes | Supported | Supported |
| Custom events | Supported | Supported |
| Purchase events | Supported | Supported |
| Catalog items | Supported | Supported |
| User deletions | Supported | Supported |
| Canvas triggers | Supported | Supported |
| Connected sources | Supported | Not supported |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Data types by source" }

## Shared reference

Some Cloud Data Ingestion behavior is the same no matter which source you use:

- [Table setup](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/table_setup) explains required columns and how `PAYLOAD` formatting maps to the `/users/track` object formats.
- [Best practices](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/best_practices) covers sync scheduling, `UPDATED_AT` behavior, and how to minimize data point consumption.
- [Sync logs and observability](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs) covers monitoring sync runs and exporting logs.
- [FAQ](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs) answers common questions about sync behavior, errors, and security.
