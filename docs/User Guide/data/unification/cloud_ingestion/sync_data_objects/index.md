# Sync data objects with Cloud Data Ingestion

> Use this page to sync data object records and their relationships from your source to Braze with Cloud Data Ingestion (CDI). Data objects let you store business records, such as accounts, and connect them to your users. For the underlying object model and the API endpoints, see [Data objects](https://www.braze.com/docs/api/endpoints/data_objects).

## Sync types

Data objects use three separate sync types. Each one is a separate sync in Braze, with its own source table or query and its own schedule.

| Data type | What each row represents | Required identifiers |
| --- | --- | --- |
| **Data Objects** | One data object record, such as a single account. | `OBJECT_ID` |
| **Data Object User Relationships** | A link between one record and one user. | `OBJECT_ID` and at least one user identifier |
| **Data Object Relationships** | A link between two records of the same or different types. | `OBJECT_ID` and `RELATED_OBJECT_ID` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Data object sync types" }

Sync records before the relationships that reference them. A relationship row whose record doesn't exist yet is held and retried rather than applied.

## Before you create a sync

CDI doesn't create or change data object fields during a sync, so set them up first:

1. In **Data Settings** > **Accounts**, add each field and relationship field you plan to send. Mark a field as required only if every row will have a value for it.
2. In your source, create the table or view for each sync, or plan the query you'll write directly from CDI.

## Create the sync

1. Go to **Data Settings** > **Cloud Data Ingestion** > **Syncs**, and select **Create data sync**.
2. Enter a name and select your source.
3. For **Data Type**, select **Data Objects**, **Data Object User Relationships**, or **Data Object Relationships**.
4. Select the **Data object type** for a record sync, or the **Relationship name** for either relationship sync. Relationship names show the relationship followed by the two types it connects, such as **User (Account-User)** or **Subaccount (Account-Account)**.
5. On the **Data definition** step, choose a sync mode. Data object syncs support **Table** and **SQL** on data warehouse sources. The visual mapper is not available for data object syncs.
6. Select **Preview and validate**, then continue through notifications and scheduling.

## Source columns

- `UPDATED_AT` - The time this row was updated in or added to the table. Braze syncs rows where `UPDATED_AT` is later than the last synced value. Rows at the exact boundary timestamp may be re-synced if new rows share that same timestamp.
- `OBJECT_ID` - The identifier of the data object record. This must match the `object_id` value used in Braze for this data object type.
- `PAYLOAD` - A JSON string of the fields and values to sync. Each key must match a field defined on the data object type in Braze.
- `DELETED` - When `true`, Braze deletes the record instead of updating it. Leave this null or `false` for rows you want to create or update.

Field names inside `PAYLOAD` are case-sensitive. A key named `NAME` does not match a field named `name`. If the casing doesn't match, validation reports the key as an undefined field and reports the field it was meant to populate as missing. Name your keys exactly as the fields appear in **Data Settings** > **Data Objects**.

Braze does not create or change data object types during a sync. Define the type and all of its fields in Braze before you create the sync. To add a field later, add it to the type first, then update your source table or query.


For the column definitions and example DDL in your source's SQL dialect, see your [source page](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources).

### User relationship identifiers

A user relationship row needs `OBJECT_ID` plus at least one user identifier: `EXTERNAL_ID`, the combination of `ALIAS_NAME` and `ALIAS_LABEL`, `EMAIL`, or `PHONE`.

## Validation

When you select **Preview and validate**, Braze checks the columns your table or query returns against the fields defined on the data object type. You can't continue past the **Data definition** step until validation passes.

| Error | Cause | How to fix |
| --- | --- | --- |
| Required fields are missing or null in your query | A field marked required on the type has no matching column, or that column is null in the previewed rows. | Add a column for each required field, and make sure every row has a value. |
| The data object type does not have the following fields defined | A column doesn't match any field on the type. Fields are case sensitive, so `TEAM_ID` doesn't match `team_id`. | Correct the column name to match the field exactly, remove the column, or add the field to the type in Braze. |
| Fields expect a different data type than in your query | A column's data type doesn't match the field's data type, such as a string where the field expects a number. | Cast the column to the expected type in your source table or query. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Data object sync validation errors" }

Note that validation checks only the first 10 rows your source returns. Rows that fail during a sync are reported in the [sync logs](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs).


## Delete records and relationships

Include a `DELETED` column in your source to remove records or relationships. When `DELETED` is `true`, Braze deletes that record or relationship instead of updating it. Deleting a record or a relationship does not delete the users it was related to.

## Related pages

- [Table setup](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/table_setup) for required columns and payload formatting
- [Best practices](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/best_practices) for sync scheduling and data point efficiency
- [Sync logs and observability](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs) for monitoring sync runs
- [FAQ](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs) for common questions across all sources

