# Sync logs and observability

> The Cloud Data Ingestion (CDI) **Sync Log** dashboard allows you to monitor all data processed by CDI, verify whether data was synced successfully, and diagnose any issues with "incorrect" or missing data.

To access the sync logs, go to **Data Settings** > **Cloud Data Ingestion** and select the **Sync Log** tab.

<!-- support-analyzer-phase2:cdi_updated_at_row_sync -->
**Note:**


If warehouse row counts do not match **Rows Synced** or you see **Partial Success** runs, open the **Run ID** in Sync Log and review row-level **Error reason** values. CDI selects rows using `UPDATED_AT`—rows with timestamps already processed, unchanged `UPDATED_AT` after edits, or writes during an active sync may be skipped. For common cases, see [Why doesn't "Rows Synced" match the number in my warehouse?](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs/#why-doesnt-rows-synced-match-the-number-in-my-warehouse) and [Cloud Data Ingestion FAQ](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs/).




## Understanding the Sync Log dashboard

The main **Sync Log** page provides a high-level overview of all your sync runs, including an overview of recent syncs by their current or final status.

* **Running:** Sync jobs that are currently in progress.  
* **Success:** Sync jobs that completed, and all rows were processed successfully.  
* **Partial Success:** Sync jobs that completed, but one or more rows encountered an error.  
* **Error:** Sync jobs that failed to complete.  
* **Limit Exceeded:** Sync jobs that stopped processing because a data limit was exceeded.

![An example of sync logs with 6,576 total successes.](https://www.braze.com/docs/assets/img/cloud_ingestion/sync_logs1.png?e37a8e2479c8cc6190bbf878ee3bb443){: style="max-width:80%"}

Sync logs also provide the following details for each sync:

* **Sync name:** The name of the sync configuration.  
* **Run ID:** A unique identifier for a specific execution of the sync. Select this ID to view more details or to reference a sync run with Braze Support.   
* **Status:** The status of the run (success, partial success, error, running).  
* **New rows read from source:** The number of new rows pulled from your source for this run.  
* **Results:** A breakdown of how many rows succeeded or failed within the run.  
* **Last "UPDATED_AT":** The timestamp of the most recent record processed in this sync run. File storage syncs don't use an `UPDATED_AT` column to choose what to ingest, so don't use this value to tell which files a run processed. For more information, see [How do `UPDATED_AT` and `last_timestamp_synced` work for file storage syncs?](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs#updated-at-file-storage)  
* **Run start time:** When the sync job began.  
* **Run duration:** The total time the sync job took to complete.

### Data retention

Sync log data, including all row-level payloads and error details, is retained for up to **30 days**. Logs older than 30 days are automatically purged.

Sync run metadata such as the number of rows processed is retained for at least 12 months.

### Filtering sync logs

You can filter the sync logs table to find specific runs. The available filters include:

* **Job start date:** Select a predefined range (like "Last 30 days") or a custom date range.  
* **Status:** Filter by one or more sync statuses (like showing only **Error** and **Partial success** statuses).  
* **Sync name:** Search for a specific sync by its name.

To investigate a specific sync, select the relevant **Run ID** from the Sync logs table. In the **Run details** page, you'll find a granular, row-by-row log of the sync.

### Run overview

This section summarizes the selected run, including its start time, end time, duration, and the total number of rows read from the source. It also provides a count of how many rows succeeded and how many resulted in an error.

For file storage syncs, this section shows a **View file names** link that lists the files the run ingested, instead of an `UPDATED_AT` value.

#### How errors are counted

The **Error** count in the run summary includes rows that failed validation or were rejected during sync. Rows dropped as in-batch duplicate IDs are not included in this count and don't affect the run status (Success vs Partial Success), because the latest value for each ID was successfully synced. To view duplicate ID rows, filter **Rows processed in this run** by status **Error** and look for error type `DUPLICATE_ID`, or export using **Export rows** > **All rows** and filter on `ERROR_TYPE = DUPLICATE_ID`.

### Rows processed in this run

This table provides row-level visibility into the data processed during the sync, allowing you to validate individual records.

* **Search:** You can search for a specific user within the run's results using the **Search by user ID** bar.  
* **Available details:**   
  * **UPDATED_AT:** The timestamp from the `UPDATED_AT` column for that specific row.  
  * **ID:** The user identifiers (such as `external_id`, `email`, or `alias_name`) used to match the record to a Braze user profile.  
  * **Status:** The individual processing status for that row (**Success** or **Error**).  
  * **Source payload:** A link to view the data payload.  
  * **Error reason:** If the status is **Error**, this column provides a message explaining why the row failed to sync. For catalog syncs, rows with error type `DUPLICATE_ID` indicate that a newer row with the same ID was processed in the same batch. The latest value was synced successfully, so these rows are recorded for traceability but don't count as errors in the run summary.

#### Viewing payloads

To see the exact data sent to Braze for a specific row, select **View payload** in the **Source** payload column. This displays the raw JSON payload that was processed for that user.

#### Exporting sync logs

Select **Export rows** to export the row-level logs for a sync run. Then, choose to export by:

* **Rows with errors:** Downloads a file containing only the rows that had an **Error** status. This export is only available when the run has rows counted as errors (validation failures or rejections). Rows with error type `DUPLICATE_ID` (in-batch duplicates) are not included in this export because they don't count as errors in the run summary. To export duplicate ID rows, use **All rows** instead.
* **All rows:** Downloads a file containing every row processed in the run, including success, error, and duplicate ID rows. The export includes `ERROR_TYPE` and `ERROR_MESSAGE` columns to identify any issues.





**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





Logs can't be exported directly from the dashboard. After the export is generated, you’ll receive an email with a link to download the log export file. 

## Notifications

You can configure email notifications to stay informed about the status of your CDI syncs. These settings are configured when you create a sync and can be updated at any time.

### Error notifications

At least one email address contact is required to receive notifications for sync-level errors. These alerts are sent when an entire sync job fails to run or complete, or if the sync runs into an error that requires user intervention to change, such as expired credentials or a missing source table.

Additional notifications include:

- **Row error:** Receive alerts when a certain percentage of rows fail to update within a sync.
- **Failure threshold (%):** Specify the percentage of row failures that should trigger an alert. For example, setting this to **1** would send a notification if 1% or more of the rows in a sync run result in an error.
- **Sync success:** Receive a notification upon the successful completion of a sync.
- **Alert even if no rows change:** Receive a notification even when a successful sync run processes zero new or updated rows.