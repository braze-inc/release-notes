# Cloud Data Ingestion for Amazon S3

> This page covers everything you need to sync data from Amazon S3 to Braze using Cloud Data Ingestion (CDI): the AWS resources to create, how to connect the source and create a sync in Braze, the file format for each data type, and S3-specific troubleshooting.

## How it works

Amazon S3 integrations are event-driven rather than scheduled. When new files are published to S3, a message is posted to an Amazon Simple Queue Service (SQS) queue, and Braze consumes that message to ingest the new file.

The integration requires the following resources:

- S3 bucket for data storage
- SQS queue for new file notifications
- IAM role for Braze access

### AWS definitions

| Term | Definition |
| --- | --- |
| Amazon Resource Name (ARN) | The ARN is a unique identifier for AWS resources. |
| Identity and Access Management (IAM) | IAM is a web service that lets you securely control access to AWS resources. In this tutorial, create an IAM policy and assign it to an IAM role to integrate your S3 bucket with Braze Cloud Data Ingestion. |
| Amazon Simple Queue Service (SQS) | SQS is a hosted queue that lets you integrate distributed software systems and components. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AWS definitions" }

## Set up Cloud Data Ingestion in AWS {#setting-up-cloud-data-ingestion-in-aws}

### Step 1: Create a source bucket

Create a general-purpose S3 bucket with default settings in your AWS account. S3 buckets can be reused across syncs as long as the folder is unique.

The default settings are:

- ACLs Disabled
- Block all public access
- Disable bucket versioning
- SSE-S3 encryption
  - SSE-S3 is the only supported server-side encryption type. Amazon KMS encryption is not supported.

Note the region where you created the bucket. You'll create an SQS queue in the same region in the next step.

### Step 2: Create SQS queue

Create an SQS queue to track when objects are added to the bucket you've created. Use the default configuration settings for now.

An SQS queue must be unique globally (for example, only one can be used for a CDI sync and cannot be reused in another workspace).

**Important:**


Be sure to create this SQS in the same region as the one you created the bucket in.



Note the ARN and URL of the SQS queue. You'll need them frequently during this configuration.

![Selecting "Advanced" with an example JSON object to define who can access a queue.](https://www.braze.com/docs/assets/img/cloud_ingestion/s3_ARN.png?c7c113d521ab4f4253e9f6c3bbee669f)

### Step 3: Set up access policy

To set up the access policy, choose **Advanced options**.

Append the following statement to the queue's access policy, being careful to replace `YOUR-BUCKET-NAME-HERE` with your bucket name, and `YOUR-SQS-ARN` with your SQS queue ARN, and `YOUR-AWS-ACCOUNT-ID` with your AWS account ID:

``` json
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
}
```

### Step 4: Add an event notification to the S3 bucket

1. In the bucket created in step 1, go to **Properties** > **Event notifications**.
2. Give the configuration a name. Optionally, specify a prefix or suffix to target if you only want a subset of files to be ingested by Braze.
3. Under **Destination**, select **SQS queue** and provide the ARN of the SQS you created in step 2.

**Note:**


If you upload your files to the root folder of an S3 bucket and then move some of the files to a specific folder in the bucket, you may encounter an unexpected error. Instead, you can change the event notifications to send for only the files in the prefix, avoid placing files in the S3 bucket outside that prefix, or update the integration with no prefix, which then ingests all files.



### Step 5: Create an IAM policy

Create an IAM policy to allow Braze to interact with your source bucket. To get started, sign in to the AWS management console as an account administrator.

1. Go to the IAM section of the AWS Console, select **Policies** in the navigation bar, then select **Create Policy**.<br><br>![The "Create policy" button in the AWS Console.](https://www.braze.com/docs/assets/img/create_policy_1_list.png?fa9d5ec769c2511a55577e04b13a647f)<br><br>

2. Open the **JSON** tab and input the following code snippet into the **Policy Document** section, taking care to replace `YOUR-BUCKET-NAME-HERE` with your bucket name, and `YOUR-SQS-ARN-HERE` with your SQS queue name:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```

{: start="3"}
3. Select **Review Policy** when you're finished.

4. Give the policy a name and description, then select **Create Policy**.

![An example policy named "new-policy-name."](https://www.braze.com/docs/assets/img/create_policy_3_name.png?28c682eb61c2b23cf67a054d1bbec2aa)

![The description field for the policy.](https://www.braze.com/docs/assets/img/create_policy_4_created.png?61896a5e05b740d64baa27767e7aff14)

### Step 6: Set up authentication {#set-up-authentication}

Braze accesses your bucket and queue with the following authentication method:


| Method | How Braze authenticates | What you enter in Braze |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Authentication methods for " }



### IAM role {#iam-role}

Braze assumes an IAM role in your AWS account. Create the role and attach the [IAM policy you created](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sources/amazon_s3#step-5-create-an-iam-policy) to it.

1. Within the same IAM section of the console where you created the IAM policy, go to **Roles** > **Create Role**.

![The "Create role" button.](https://www.braze.com/docs/assets/img/create_role_1_list.png?2d08777407a38aae1270ebebdc3ea60d)

{: start="2"}
2. In AWS, select **Another AWS Account** as the trusted entity selector type. Provide your Braze account ID. Select the **Require external ID** checkbox.
3. In Braze, go to **Data Settings** > **Cloud Data Ingestion** > **Sources**, select **Add data source**, and select **Amazon S3** from the file sources section.
4. Copy the automatically generated **Braze Account ID**.

![The "Add New Source" page showing the Source Name and S3 Connection Details sections.](https://www.braze.com/docs/assets/img/braze_account_id.png?5a9f1d0535506159d0a7615fa51465f1)

{: start="5"}
5. In AWS, paste the account ID and then select **Next**.

![The S3 "Create Role" page. This page has fields for role name, role description, trusted entities, policies, and permissions boundary.](https://www.braze.com/docs/assets/img/create_role_2_another.png?d65b37508b1a76421859ad2263370d75)

{: start="6"}
6. Attach the IAM policy to the role. Search for the policy in the search bar, and select a checkmark next to the policy to attach it. Select **Next** when complete.

![Role ARN with the new-policy-name selected.](https://www.braze.com/docs/assets/img/create_role_3_attach.png?e3693d15b7f9ac545747f548c5b4fb3c)

{: start="7"}
7. Give the role a name and a description, and select **Create Role**.

![An example role named "new-role-name".](https://www.braze.com/docs/assets/img/create_role_4_name.png?a509d3bd2ab0a9c64a78ce2f6312bae4)

{: start="8"}
8. Take note of the ARN of the role you created and the external ID you generated, because you need them to create the Cloud Data Ingestion integration.



## Set up Cloud Data Ingestion in Braze {#setting-up-cloud-data-ingestion-in-braze}

1. First, create a new source in the Braze dashboard. Go to **Data Settings** > **Cloud Data Ingestion** > **Sources**, select **Add data source**, and then select **Amazon S3**.
2. Choose a name for your source and input the information from the AWS setup process to create a new source. Specify the following:

  - The credentials for your [authentication method](#set-up-authentication). 


  - Bucket name
  - Region

![The S3 Connection Details section showing Credentials (AWS setup and Braze setup) and Configuration fields.](https://www.braze.com/docs/assets/img/cloud_ingestion/s3_ingestion_1.png?952507f4b2a40065536a39aaf7a900b4)

{: start="3"}
3. Select **Test connection** to confirm Braze can access your bucket. After a successful test, select **Connect to Source**. If the connection fails, an error message appears to help troubleshoot the issue.

{: start="4"}
4. Next, create a new sync. Go to **Data Settings** > **Cloud Data Ingestion** > **Syncs** and select **Create data sync**.

{: start="5"}
5. Choose a name for your sync. Then, select any active S3 source and input your source table for the sync. Select a data type and select **Test Connection**.

![An option to test the connection with a data preview.](https://www.braze.com/docs/assets/img/cloud_ingestion/s3_ingestion_4.png?87bc3ce124b7b045a97ee7c4a3586178)

6. Input the remaining information from the AWS setup process. Specify the following:
- SQS URL (must be unique for each new integration)
- Folder path (optional, must be unique across syncs in a workspace)

7. Select a data type and select **Test Connection** to confirm Braze can list the files available to ingest (not the data inside those files). Once successful, select **Next: Notifications**.
8. Add contact email addresses for notifications if the sync breaks because of access or permissions issues. Optionally, turn on notifications for user-level errors and sync successes.
9. Create the sync.

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

- Braze deletes an SQS message only when the file has been successfully read and the resulting rows have been ingested into Braze's internal systems. Braze does not extend the visibility timeout. If you're seeing messages in your dead-letter queue, consider increasing your visibility timeout to match the time it takes for your largest files to process. Braze also tracks metadata for each file—if a file is successfully ingested and a duplicate SQS message appears for that file, Braze immediately deletes the duplicate message. If the file was not successfully ingested, Braze processes the SQS message normally.

## Troubleshooting {#troubleshooting}

### Uploading files and processing

CDI only processes files that are added after the sync is created. In this process, Braze looks for new files to be added, which triggers a new notification. This kicks off a new sync to process the new file. For Amazon S3, the notification is a message to SQS.

You can use existing files to validate that Braze can access your bucket and detect files to ingest, but they are not synced to Braze. For CDI to process them, you must re-upload to the source bucket any existing files that you want synced.

### Handling unexpected file errors

If you're observing a high number of errors or failed files, you may have another process adding files to the S3 bucket in a folder other than the target folder for CDI.

When files are uploaded to the source bucket but not in the source folder, CDI processes the SQS notification, but it does not take any action on the file, so this may appear as an error.

If your issue is related to S3 notifications or SQS destination permissions (for example, destination validation errors), refer to AWS documentation:

- [Enabling and configuring event notifications using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html)
- [Granting permissions to publish event notification messages to a destination](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)
- [Troubleshooting issues in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-troubleshooting.html)

### Incorrect Integration Object error

This error occurs when two or more workspaces have integrations pointing to the same cloud storage bucket or folder. Each cloud storage location can only be used by one integration at a time. For resolution steps, see the [FAQ](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs#why-am-i-seeing-an-incorrect-integration-object-error).

## Related pages

- [Table setup](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/table_setup) for required columns and payload formatting
- [Best practices](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/best_practices) for sync scheduling and data point efficiency
- [Sync logs and observability](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sync_logs) for monitoring sync runs
- [FAQ](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/faqs) for common questions across all sources

