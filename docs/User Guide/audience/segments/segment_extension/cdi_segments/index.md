# CDI Segment Extensions

> With Braze [Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion) (CDI), you can set up a direct connection from your data warehouse or file storage system to Braze to sync relevant user or catalog data on a recurring basis.

**Warning:**


CDI Segment Extensions query your data warehouse directly, so you will incur all costs associated with running these queries in your data warehouse. CDI Segment Extensions won't consume [SQL segment credits](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments#credits), don't count towards your Segment Extension limit, and do not log data points.



## Prerequisites

To use your data warehouse data for segmentation within your Braze workspace, you'll need to create a [connected source](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/connected_sources), then create a CDI segment within your [Segment Extensions](https://www.braze.com/docs/user_guide/audience/segments/segment_extension). CDI Segment Extensions allow you to write SQL that directly queries your own data warehouse by using data made available through your CDI connections, and create a group of users that can be targeted within Braze.

## Creating a CDI segment

### Step 1: Set up your source

Before creating your first CDI Segment Extension, set up a new connected source with your data warehouse by following the steps in [Connected sources](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/connected_sources).

### Step 2: Create a segment

1. Go to **Audience** > **Segment Extensions**, then select **Create New Extension**.
2. In the **Select your Segment Extension creation experience** menu, select **Full refresh (including CDI Segments)**.

![The "Select your Segment Extension creation experience" menu with creation options.](https://www.braze.com/docs/assets/img/segment/segment_extension_modal.png?389f8fd34f15bb22810ef986bbc258c0){: style="max-width:60%;"}

{: start="3"}
3. In the **Select the data source for this Segment Extension** menu, choose **CDI Data Tables**. This menu appears only after you have set up at least one [connected source](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/connected_sources).

![The "Select the data source for this Segment Extension" menu with the CDI Data Tables option.](https://www.braze.com/docs/assets/img/segment/cdi_data_tables.png?33da447f7b1659144c832e17d978c14d){: style="max-width:60%;"}

{: start="4"}
4. Select a connection to use, then write your query. Each connection has a specific set of data tables. Your development team can configure your connections and data tables during CDI setup.
5. View the available data tables, including their schema and any available descriptions, by selecting **Source Explorer**.

![The Source Explorer showing the available data tables, including their schema and any available descriptions.](https://www.braze.com/docs/assets/img/segment/connection_schema_with_descriptions.png?242ac24afefc400186610bd05f249137){: style="max-width:100%;"}

{: start="6"}
6. Write the SQL for your segment using [the Braze SQL syntax](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql). Keep in mind, all CDI Segment Extensions must use `external_user_id` as the selected column, and your `external_user_id` should match the one set in Braze for users.<br><br>
If your query results include users that don't exist in Braze, those users are ignored. Braze doesn't create new users based on the output of your CDI Segment Extension.

**Important:**


`external_user_id` must be a string value. If your source ID is stored as a number (for example, `client_id` as an integer), [cast it to a string in your SQL](https://www.w3schools.com/sql/func_sqlserver_cast.asp) so it matches the `external_id` type in Braze.



{: start="7"}
7. [Use this Segment Extension](https://www.braze.com/docs/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment) within a Braze segment to send a campaign or Canvas to this audience.

**Tip:**


To learn how you can preview your Segment Extensions, manage your Segment Extensions, and run automated membership refreshes, see [SQL Segment Extensions](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments).



## Considerations

- A Segment Extension can reference data from only one connection, not multiple.    
- A Segment Extension can use one of the following as a data source: CDI data or Braze Snowflake (Currents) data. You cannot mix data sources within a Segment Extension, but you can create multiple Segment Extensions to reference together within a segment.

## Troubleshooting

- Your query might timeout when it reaches your maximum runtime, which is set up for each connection sync on the **Cloud Data Ingestion** page. The maximum runtime allowed is 60 minutes.
- Make sure your SQL is written using appropriate syntax for your data warehouse. 
