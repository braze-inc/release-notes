# Cloud Data Ingestion for Google Cloud Storage

> This page covers everything you need to sync data from Google Cloud Storage (GCS) to Braze using Cloud Data Ingestion (CDI): the Google Cloud resources to create, how to connect the source and create a sync in Braze, the file format for each data type, and GCS-specific troubleshooting.

## How it works

Google Cloud Storage integrations are event-driven rather than scheduled. When new files are finalized in the bucket, GCS publishes an `OBJECT_FINALIZE` notification to a Pub/Sub topic. Braze consumes those notifications from a Pub/Sub subscription to ingest the new file.

The integration requires the following resources:

- A Cloud Storage bucket for data storage
- A Pub/Sub topic and subscription for new file notifications
- A service account that Braze accesses through one of the supported [authentication methods](#set-up-authentication)

### GCP definitions

| Term | Definition |
| --- | --- |
| Google Cloud project | A project organizes all your Google Cloud resources and is identified by a unique project ID and project number. |
| Cloud Storage bucket | A bucket is the container that holds the data files you want Braze to ingest. |
| Pub/Sub topic | A topic is the named resource that receives new-file notifications from your Cloud Storage bucket. |
| Pub/Sub subscription | A subscription attaches to a topic and delivers its messages. Braze consumes new-file notifications from a pull subscription. |
| Service account | A service account is a non-human identity that Braze uses to access your bucket and subscription. Braze impersonates it through Workload Identity Federation, or uses a JSON key you upload. |
| Workload Identity Federation | Workload Identity Federation (WIF) lets Braze impersonate your service account with a short-lived identity, so you don't create or upload a key. |
| IAM role | An Identity and Access Management (IAM) role is a collection of permissions that you assign to the service account on your bucket and subscription. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="GCP definitions" }

## Set up Cloud Data Ingestion in Google Cloud

### Step 1: Create a Cloud Storage bucket

In the Google Cloud console, go to **Cloud Storage** > **Buckets** > **Create**. Note the project ID and the bucket name. You'll need them when you configure the source in Braze. Braze recommends enabling uniform bucket-level access so that permissions are managed with IAM.

### Step 2: Create a Pub/Sub topic and subscription

In the Google Cloud console, go to **Pub/Sub** > **Topics** > **Create topic**. You can let Google create a default subscription, or create one separately. Then, create a **pull** subscription on that topic.

Note the **subscription ID**. Braze needs the subscription (not the topic) when you create the sync. The subscription must be a pull subscription.

**Warning:**


Don't configure a dead-letter queue on this subscription. Braze doesn't support dead-letter queues for Cloud Data Ingestion subscriptions. To learn more, see [Dead-letter topics](https://cloud.google.com/pubsub/docs/dead-letter-topics) in the Google Cloud documentation.



### Step 3: Send bucket notifications to the topic

**Important:**


Creating a Cloud Storage to Pub/Sub notification isn't available in the Google Cloud console. You must use gcloud (shown here), Terraform, or the JSON API. To learn more, see [Configure Pub/Sub notifications for Cloud Storage](https://cloud.google.com/storage/docs/reporting-changes#enabling) in the Google Cloud documentation.



First, assign the Cloud Storage service agent permission to publish to the topic, then create the notification for `OBJECT_FINALIZE`. The `OBJECT_FINALIZE` event fires whenever a new object is created or finalized in the bucket.

```shell
# Get the Cloud Storage service agent for your project
gcloud storage service-agent --project=YOUR-PROJECT-ID

# Assign it Pub/Sub Publisher on the topic
gcloud pubsub topics add-iam-policy-binding YOUR-TOPIC \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
  --role="roles/pubsub.publisher"

# Create the OBJECT_FINALIZE notification (optionally scope to a folder with --object-prefix)
gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
  --topic=YOUR-TOPIC \
  --event-types=OBJECT_FINALIZE \
  --payload-format=json
```

Replace `YOUR-PROJECT-ID`, `YOUR-BUCKET-NAME`, and `YOUR-TOPIC` with your own values. `YOUR-PROJECT-NUMBER` is the numeric identifier in the service agent's email address, which differs from the project ID. Find it on the **Dashboard** in the Google Cloud console, or run `gcloud projects describe YOUR-PROJECT-ID --format="value(projectNumber)"`.

### Step 4: Create a service account

In the Google Cloud console, go to **IAM & Admin** > **Service Accounts** > **Create service account**. This example uses `braze-cdi-gcs` as the account name.

### Step 5: Assign permissions {#step-5-assign-permissions}

The connector needs exactly these permissions: `storage.buckets.get`, `storage.objects.get`, and `storage.objects.list` on the bucket, and `pubsub.subscriptions.consume` on the subscription. You can assign them with either a custom role or predefined roles.

**Custom role:** Create a custom role with exactly those permissions and bind it to the bucket and the subscription:

```shell
gcloud iam roles create brazeCdiGcs --project=YOUR-PROJECT-ID \
  --title="Braze CDI GCS" \
  --permissions=storage.buckets.get,storage.objects.get,storage.objects.list,pubsub.subscriptions.consume \
  --stage=GA

gcloud storage buckets add-iam-policy-binding gs://YOUR-BUCKET-NAME \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"

gcloud pubsub subscriptions add-iam-policy-binding YOUR-SUBSCRIPTION \
  --project=YOUR-PROJECT-ID \
  --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
  --role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"
```

**Predefined roles:** Instead of a custom role, assign `roles/storage.objectViewer` and `roles/storage.legacyBucketReader` on the bucket, and `roles/pubsub.subscriber` on the subscription. The `objectViewer` role provides `storage.objects.get` and `storage.objects.list`, and `legacyBucketReader` provides `storage.buckets.get`.

### Step 6: Set up authentication {#set-up-authentication}

Braze can access the service account with any of the following authentication methods:


| Method | How Braze authenticates | What you enter in Braze |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Authentication methods for " }








## Set up Cloud Data Ingestion in Braze {#setting-up-cloud-data-ingestion-in-braze-gcs}

1. In Braze, go to **Data Settings** > **Cloud Data Ingestion** > **Sources**, select **Add data source**, and then select **Google Cloud Storage**.

![The "Add New Source" screen with Google Cloud Storage selected from the list of data sources.](https://www.braze.com/docs/assets/img/cloud_ingestion/gcs_source_picker.png?154ab18321f0a4423ebf7efb4108d69c)

{: start="2"}
2. Complete the source fields:
    - **Bucket:** your bucket name
    - **Project ID:** your GCP project ID
    - **Credential:** give the credential a name and select the authentication method you set up in [Step 6](#set-up-authentication). 



![The Google Cloud Storage source form showing Bucket, Project ID, and credential upload fields.](https://www.braze.com/docs/assets/img/cloud_ingestion/gcs_source_form.png?faba91f61508cdd5ab603d6c84c577a8)

{: start="3"}
3. Select **Test connection**, then select **Connect to Source**.
4. Create a sync. Go to **Data Settings** > **Cloud Data Ingestion** > **Syncs** and select **Create data sync**. Choose a sync name and a **Data Type** (such as **User Attributes**, **Custom Events**, **Purchase Events**, **Catalog**, or **Delete Users**), then select **Next**.
5. On the **Data definition** step, select your GCS source, then specify the following:
    - **Pub/Sub subscription ID:** the subscription ID from step 2 (not the topic)
    - **Folder path** (optional): a path prefix within the bucket (see [Syncing a folder in a shared bucket](#syncing-a-folder-in-a-shared-bucket))

![The Google Cloud Storage sync form showing the Pub/Sub subscription ID and folder path fields.](https://www.braze.com/docs/assets/img/cloud_ingestion/gcs_sync_form.png?881490ae1af5568765ca57f23ff7e334)

{: start="6"}
6. Select **Preview and validate** to confirm Braze can reach the subscription and list the files available to ingest. A successful test lists existing files in the bucket, but those files aren't synced automatically.
7. Add contact email addresses for error notifications. Google Cloud Storage syncs are event-driven, so no schedule is required. Braze ingests new files as they're uploaded. Review the summary, then select **Create sync**.

### Syncing a folder in a shared bucket {#syncing-a-folder-in-a-shared-bucket}

You can reuse one bucket across multiple syncs, but each sync must target a distinct folder **and** have its own dedicated Pub/Sub subscription.

**Important:**


The folder path and the subscription must both be unique across syncs in a workspace for multiple syncs sharing the same source bucket. As in [Step 2](#step-2-create-a-pubsub-topic-and-subscription), don't configure a dead-letter queue on any of these subscriptions.



For each folder you want to sync in a shared bucket:

1. Set the sync's **Folder** field to the path prefix (for example, `attributes/`). Braze only lists and ingests objects whose path starts with that prefix.
2. Create a dedicated topic and a prefix-scoped notification for that folder, then create a subscription on that topic:

    ```shell
    # One topic per folder
    gcloud pubsub topics create YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID

    # Assign the Cloud Storage service agent publisher on the topic
    gcloud pubsub topics add-iam-policy-binding YOUR-ATTRIBUTES-TOPIC \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:service-YOUR-PROJECT-NUMBER@gs-project-accounts.iam.gserviceaccount.com" \
      --role="roles/pubsub.publisher"

    # Notification scoped to the folder with --object-prefix
    gcloud storage buckets notifications create gs://YOUR-BUCKET-NAME \
      --topic=YOUR-ATTRIBUTES-TOPIC --event-types=OBJECT_FINALIZE \
      --payload-format=json --object-prefix=attributes/

    # One subscription per sync
    gcloud pubsub subscriptions create YOUR-ATTRIBUTES-SUBSCRIPTION \
      --topic=YOUR-ATTRIBUTES-TOPIC --project=YOUR-PROJECT-ID --ack-deadline=60
    ```

3. Assign the Braze service account consume permission on that subscription, as in [Step 5](#step-5-assign-permissions):

    ```shell
    gcloud pubsub subscriptions add-iam-policy-binding YOUR-ATTRIBUTES-SUBSCRIPTION \
      --project=YOUR-PROJECT-ID \
      --member="serviceAccount:braze-cdi-gcs@YOUR-PROJECT-ID.iam.gserviceaccount.com" \
      --role="roles/pubsub.subscriber"
    ```

    If you created the custom role in [Step 5](#step-5-assign-permissions), use `--role="projects/YOUR-PROJECT-ID/roles/brazeCdiGcs"` instead.
4. When you create the sync in Braze, enter this folder's new **Pub/Sub subscription ID** and **Folder path** so the sync ingests only that folder's files.

## Required file formats {#required-file-formats}

Cloud Data Ingestion supports JSON, CSV, and Parquet files. The required columns depend on the data type. Braze doesn't enforce any additional filename requirements beyond what's enforced by your file storage provider. Filenames should be unique, and appending a timestamp helps ensure uniqueness.

**Note:**


Unlike with data warehouse sources, the `UPDATED_AT` column is neither required nor supported for file storage syncs.



For examples of all supported file types, see the sample files in [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

Select the tab for the data type you want to sync.




Each row requires exactly one user identifier and a `PAYLOAD` column. A source file may contain rows with different identifier types, but each individual row should only use one.

| Identifier | Description |
| --- | --- |
| `EXTERNAL_ID` | This identifies the user you want to update. This should match the `external_id` value used in Braze. |
| `ALIAS_NAME` and `ALIAS_LABEL` | These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels, but only one `alias_name` per `alias_label`. |
| `BRAZE_ID` | The Braze user identifier. This is generated by the Braze SDK, and new users cannot be created using a Braze ID through Cloud Data Ingestion. To create new users, specify an external user ID or user alias. |
| `EMAIL` | The user's email address. If multiple profiles with the same email address exist, the most recently updated profile is prioritized for updates. If you include both email and phone, Braze uses the email as the primary identifier. |
| `PHONE` | The user's phone number. If multiple profiles with the same phone number exist, the most recently updated profile is prioritized for updates. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="File storage user identifiers" }

The `PAYLOAD` column contains a JSON string of the fields you want to sync to the user in Braze, following the [user attributes object](https://www.braze.com/docs/api/objects_filters/user_attributes_object) format.

**JSON example**

``` json
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
```

**CSV example**

```plaintext
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
```

**Important:**


Every line in your source file must contain valid JSON, or the file is skipped.






Custom events use the same user identifier columns as user attributes. The `PAYLOAD` column follows the [events object](https://www.braze.com/docs/api/objects_filters/event_object) format.

``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```

**Important:**


Every line in your source file must contain valid JSON, or the file is skipped.






Purchase events use the same user identifier columns as user attributes. The `PAYLOAD` column follows the [purchases object](https://www.braze.com/docs/api/objects_filters/purchase_object) format.

``` json
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```

**Important:**


Every line in your source file must contain valid JSON, or the file is skipped.






Catalog files use different identifiers than user data files. Before you create a catalog sync, create the target catalog in Braze. For the full catalog workflow, see [Sync and delete catalog data](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).

| Column | Required | Description |
| --- | --- | --- |
| `ID` | Yes | The unique identifier for the catalog item. Used to create, update, or delete the item in Braze. |
| `PAYLOAD` | Yes | A JSON string of the catalog fields and values to sync. Must match the schema of your catalog in Braze. |
| `DELETED` | No | When `true`, the catalog item with the matching `ID` is removed from the catalog in Braze. Omit this column or set to `false` for create or update operations. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="File storage catalog identifiers" }

**JSON example**

```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"86","payload":"{\"product_name\":\"Product 86\",\"price\":86.86}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```

**CSV example with the `DELETED` column**

```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
86,"{""product_name"": ""Product 86"", ""price"": 86.86}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

**CSV example without the `DELETED` column**

```plaintext
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
86,"{""product_name"": ""Product 86"", ""price"": 86.86}"
```




Canvas triggers power zero-copy personalization. For the destination Canvas setup and considerations, see [Zero-copy personalization](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/zero_copy_sync).

| Field | Required | Description |
| --- | --- | --- |
| `EXTERNAL_ID` | Yes, one of `external_id` or `alias_name` and `alias_label` | This identifies the user you want to update. This should match the `external_id` value used in Braze. |
| `ALIAS_NAME` and `ALIAS_LABEL` | Yes, one of `external_id` or `alias_name` and `alias_label` | These two columns create a user alias object. `alias_name` should be a unique identifier, and `alias_label` specifies the type of alias. Users may have multiple aliases with different labels, but only one `alias_name` per `alias_label`. |
| `PROPERTIES` | Yes | JSON string of fields to make available as personalization properties in your Canvas. This should contain user-specific information. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="File storage Canvas trigger fields" }

To get started, select the **Canvas Triggers** data type when creating a new sync.




To delete user profiles in Braze using files in your source bucket:

1. Create a new Cloud Data Ingestion sync, using the same setup as for other syncs.
2. When configuring the sync in Braze, set **Data Type** to **Delete Users**.
3. Upload files to your source bucket that contain only user identifier columns. Do not include a `PAYLOAD` column—the sync fails if payload is present, to avoid accidental deletions.

Each row in the file must identify exactly one user using one of:

| Identifier | Description |
| --- | --- |
| `EXTERNAL_ID` | Matches the `external_id` used in Braze. |
| `ALIAS_NAME` and `ALIAS_LABEL` | Both columns together identify the user by alias. |
| `BRAZE_ID` | Braze-generated user ID (existing users only). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="File storage user deletion identifiers" }

**JSON example**

```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**CSV example**

```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

When the sync runs, Braze processes new files in the bucket and deletes the corresponding user profiles.

**Important:**


Deleting users is permanent and cannot be undone. Include only users you intend to remove. For more details, see [Delete users with Cloud Data Ingestion](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/delete_users).







## Deleting catalog items

To remove items from a catalog using file storage:

1. Use the same sync you use to [sync catalog data](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data) (data type **Catalogs**).
2. In your CSV or JSON files, add an optional **`deleted`** (or **`DELETED`**) column.
3. Set `deleted` to `true` for any catalog item you want removed from the catalog in Braze.

Each row still needs `ID` and `PAYLOAD`. For rows marked for deletion, the payload can be minimal; Braze removes the item by `ID`.

When the sync runs, rows with `deleted: true` cause the matching catalog item to be deleted in Braze. For full catalog sync and delete behavior, see [Sync and delete catalog data](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_catalogs_data).


## Things to know {#things-to-know}

- Files added to the source bucket or container should not exceed 512&nbsp;MB. This limit applies to Amazon S3, Google Cloud Storage, and Azure Blob Storage. Files larger than 512&nbsp;MB result in an error and are not synced to Braze. Azure Blob Storage itself allows much larger files, but CDI applies the same 512&nbsp;MB limit across all file storage sources.
- While there is no additional limit on the number of rows per file, Braze recommends using smaller files to improve how fast your syncs run. For example, a 500&nbsp;MB file would take considerably longer to ingest than five separate 100&nbsp;MB files.
- There's no additional limit on the number of files uploaded in a given time.
- Ordering isn't supported in or between files. Braze recommends batching updates periodically if you're monitoring for any expected race conditions.
- CDI only processes files that are added after the sync is created. You can use existing files to validate that Braze can access your bucket and detect files to ingest, but they are not synced to Braze. To have CDI process them, re-upload to the source bucket any existing files that you want synced.


## Troubleshooting {#troubleshooting}

### Uploading files and processing

CDI only processes files uploaded after the sync is created. Each new object triggers an `OBJECT_FINALIZE` message to your Pub/Sub topic. To ingest files that already exist in the bucket, re-upload them.

### Handling unexpected file errors

If files are not ingested, verify the following:

- The bucket notification exists. List the notifications on the bucket with `gcloud storage buckets notifications list gs://YOUR-BUCKET-NAME`.
- The Cloud Storage service agent has `roles/pubsub.publisher` on the topic.
- The Braze service account has consume permission on the subscription (`pubsub.subscriptions.consume`, assigned through either the custom role or `roles/pubsub.subscriber`).
- The subscription doesn't have a dead-letter queue configured. Braze doesn't support dead-letter queues for Cloud Data Ingestion subscriptions.

For more information, see [Pub/Sub notifications for Cloud Storage](https://cloud.google.com/storage/docs/pubsub-notifications) in the Google Cloud documentation.




### Incorrect Integration Object error

This error occurs when two or more workspaces have integrations pointing to the same cloud storage bucket or folder. Each cloud storage location can only be used by one integration at a time. For resolution steps, see the [FAQ](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs#why-am-i-seeing-an-incorrect-integration-object-error).

## Related pages

- [Table setup](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/table_setup) for required columns and payload formatting
- [Best practices](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/best_practices) for sync scheduling and data point efficiency
- [Sync logs and observability](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs) for monitoring sync runs
- [FAQ](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs) for common questions across all sources

