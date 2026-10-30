# Connected sources

> Connected sources are a zero-copy alternative to directly syncing data with Braze's Cloud Data Ingestion (CDI) feature. A connected source directly queries your data warehouse to create new segments without copying any of the underlying data to Braze.

After adding a connected source to your Braze workspace, you can create a CDI segment within Segment Extensions. CDI Segment Extensions let you write SQL that directly queries your data warehouse (using data there that's made available through your CDI connected source), and creates and maintains a group of users that can be targeted within Braze.

For more information on creating a segment with this source, refer to [CDI Segment Extensions](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/cdi_segments).

**Warning:**


Because connected sources run on your data warehouse directly, you will incur all costs associated with running these queries in your data warehouse. Connected sources don't log data points, and CDI Segment Extensions don't consume SQL segment credits.



## Supported sources

Connected sources are available for data warehouse sources only. File storage sources don't support connected sources.

| Source | Setup instructions |
| --- | --- |
| Snowflake | [Use Snowflake as a connected source](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/snowflake#use-snowflake-as-a-connected-source) |
| Amazon Redshift | [Use Redshift as a connected source](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/amazon_redshift#use-redshift-as-a-connected-source) |
| Google BigQuery | [Use BigQuery as a connected source](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/google_bigquery#use-bigquery-as-a-connected-source) |
| Databricks | [Use Databricks as a connected source](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/databricks#use-databricks-as-a-connected-source) |
| Microsoft Fabric | [Use Microsoft Fabric as a connected source](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/microsoft_fabric#use-microsoft-fabric-as-a-connected-source) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported connected sources" }

## Set up a connected source {#set-up-a-connected-source}

Setting up a connected source follows the same four stages for every warehouse. The credentials, permissions, and SQL differ by source, so follow your source page for the exact commands.

1. **Set up your data warehouse.** Create the credentials Braze authenticates with, and grant them access to the tables you want to query. The connected source may reference one or more tables, so ensure your Braze user has permission to access all tables you want in the connected source.
2. **Create the connected source in Braze.** Go to **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**, select **Add data source**, and select your source. Enter the credentials and configuration for that source.
3. **Configure the source details.** Choose a name and a maximum runtime.
4. **Finalize the warehouse configuration and test.** For Snowflake, and for Redshift when using an SSH tunnel, add the public key Braze generates to your warehouse user. Then select **Test Connection** and **Done**.

**Note:**


You must successfully test a source before it can move from the "draft" to the "active" state. If you need to close out of the creation page, your integration is saved, and you can revisit the details page to make changes and test.



### Permissions to grant

Whichever source you use, the Braze credentials need two kinds of access:

- **Read access** to the tables or views you want available in CDI Segment Extensions. You may choose to grant access to all tables in a schema or dataset, or grant privileges only to specific tables. Whichever tables Braze has access to are available to query in the CDI Segment Extension.
- **Create table access** on the schema, so Braze can write your CDI Segment Extension query results to a table before updating the segment in Braze. Braze creates a temporary table per segment, and the table only persists while Braze is updating the segment.

After the connected source is created, Braze discovers the names and descriptions of all tables available to the credentials in the source schema.

### Maximum runtime

Configure a maximum runtime for each connected source. Braze automatically aborts any queries that exceed it. The maximum runtime allowed is 60 minutes, and a lower runtime reduces costs incurred on your warehouse account. This setting applies to queries run through this source, including syncs and CDI Segment Extensions that use it.

**Note:**


If queries are consistently timing out and you have set a maximum runtime of 60 minutes, consider trying to optimize your query execution time or dedicating more compute resources (such as a larger warehouse) to the Braze user.



## Set up additional sources (optional)

You may set up multiple connected sources with Braze, but each source should be configured to connect a different schema or dataset. When creating additional sources, you may reuse existing credentials if connecting to the same warehouse account.

For Snowflake, if you reuse the same user and role across integrations, you don't need to add the public key again.

## Using the connected source

After the source is created, you can use it to create one or more CDI Segment Extensions. For more information on creating a segment with this source, refer to the [CDI Segment Extensions documentation](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/cdi_segments).
