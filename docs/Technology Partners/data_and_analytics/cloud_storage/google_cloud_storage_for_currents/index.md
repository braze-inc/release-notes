# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/) is massively scalable object storage for unstructured data offered by Google as part of the Cloud Computing product suite.

**Important:**


If you're switching between cloud storage providers, contact your Braze customer success manager for further assistance on setting up and validating your new integration.



The Braze and Google Cloud Storage integration allows you to stream Currents data to Google Cloud Storage. You can later use an ETL process (Extract, Transform, Load) to transfer your data to other locations, such as Google BigQuery.

**Note:**


Currents doesn't connect directly to BigQuery, so it isn't part of the [Google Cloud Ready - BigQuery](https://cloud.google.com/bigquery/docs/bigquery-ready-overview) validation of Braze. Currents writes event data to your Google Cloud Storage bucket, and you can then use BigQuery tools to load or query that data from Cloud Storage.



## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Google Cloud Storage account | A Google Cloud Storage account is required to take advantage of this partnership. |
| Currents | To export data back into Google Cloud Storage, you need to have [Braze Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) set up for your account. Currents isn't required if you're only setting up message archiving. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

To integrate with Google Cloud Storage, you must set up the appropriate credentials that allow Braze to get information about the storage buckets being written to (`storage.buckets.get`) and create objects within that bucket (`storage.objects.create`). 

Braze supports two authentication methods:

- [Service account key method](#service-account-key-auth-method)
- [Workload identity federation method](#workload-identity-federation-auth-method) (Currents only)

## Service account key auth method

The following instructions walk you through creating a role and service account that generates a private key to use in your Currents integration.

### Step 1: Create role

Create a new role in your Google Cloud Platform Console by navigating to **IAM & admin** > **Roles** > **+ Create Role**.

![Google Cloud IAM roles page with the Create Role action.](https://www.braze.com/docs/assets/img/gcs1.png?4e1f3a9236118018ea5648ae97b77c44)

Give the role a name, then select **+Add Permissions** and choose the following:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

**Note:**


The `storage.objects.delete` permission is optional. It allows Braze to clean up incomplete files.<br><br>In rare circumstances, Google Cloud may terminate connections early, resulting in Braze writing incomplete files to Google Cloud Storage. In most cases, Braze will retry and create a new file with the correct data, leaving the old file in Google Cloud Storage.



**Important:**


If your bucket uses [hierarchical namespace](https://cloud.google.com/storage/docs/hns-overview), you must also add the `storage.folders.create` permission. On these buckets, folders are managed resources, so Braze needs this permission to create the folder structure for your exported files. Without it, Braze cannot write to the bucket and the integration fails to export data.



When you're finished, select **Create**.

![Google Cloud custom role editor with storage permissions selected.](https://www.braze.com/docs/assets/img/gcs2.png?15e5fa535cb3cce9e29ab0aeefc4b408)

### Step 2: Create a new service account

#### Step 2.1: Create the service account

Create a new service account in your Google Cloud Platform Console by navigating to **IAM & admin** > **Service Accounts** and selecting **Create Service Account**.

![Google Cloud service accounts page with Create Service Account selected.](https://www.braze.com/docs/assets/img/gcs3.png?e6a0627949edaeec00b8ea7bf284f67d)

Next, give the service account a name and grant it access to your newly created custom role.

![In the Google Cloud Platform, on the create services page, type the name of your role in the "Select a Role" field.](https://www.braze.com/docs/assets/img/gcs4.png?45c5bc62266d6207e6d060b2c8c87031)

#### Step 2.2: Create a key

At the bottom of the page, use the **Create Key** button to create a **JSON** private key to use in Braze. After the key is created, it will download onto your machine.

![Google Cloud service account key creation dialog set to JSON key type.](https://www.braze.com/docs/assets/img/gcs5.png?fa5b2e2962c25642ef33c54b0447bf84)

### Step 3: Set up Currents in Braze

In Braze, navigate to **Currents** > **Create New Current** > **Google Cloud Storage Data Export** and provide your integration name and contact email.

Provide a contact email for integration error notifications. Braze sends notifications to this address if the integration encounters errors, such as credential issues or connectivity problems. To help ensure the right people receive alerts, use a distribution list or group email address.


Next, upload your JSON private key under **GCS JSON Credentials** and provide your GCS bucket name and GCS prefix. Note that you must generate these credentials through Google Cloud Platform, as described in the previous steps.

**Important:**


It's important to keep your credentials file up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **5 days**, the connector's events will be dropped, and data will be permanently lost.



![The Google Cloud Storage Currents page in Braze. On this page exist fields for integration name, contact email, GCS JSON credential, GCS bucket name, and prefix.](https://www.braze.com/docs/assets/img/gcs6.png?8bbd6f1f51d69846e2356bdbd201bdf8)

Finally, scroll to the bottom of the page and select which message engagement events or customer behavior events you would like to export. When completed, launch your Current.

### Step 4: Set up Google Cloud Storage exports

To set up Google Cloud Storage (GCS) exports, go to **Technology Partners** > **Google Cloud Storage**, enter your GCS credentials, and select **Make this the default data export destination**.

Keep in mind that the organization and contents of any exported files will be identical across AWS S3, Microsoft Azure, and Google Cloud Storage integrations.

**Important:**


Be sure to input the full JSON value that's [generated by Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).



![The Google Cloud Storage page in the Braze dashboard.](https://www.braze.com/docs/assets/img/gcs7.png?fac682f7456377055e972c0d6c54c1cd){: style="max-width:70%;"}

### Step 5: Test your service account credentials (optional)

Your Google Cloud IAM service account must have the following permissions:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

To verify these permissions in the Braze dashboard, go to the **Google Cloud Storage** page, then select **Test Credentials**.

![The Google Cloud Storage credentials section in the Braze dashboard.](https://www.braze.com/docs/assets/img/gcs8.png?06a0888d97e08557a94525b638324352){: style="max-width:70%;"}

## Workload identity federation auth method

This method lets Braze authenticate to Google Cloud through [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation), then write to your bucket using Identity and Access Management (IAM). You don't create a service account key or give Braze any other secret. It's available for Braze Currents only.

**Note:**


Braze stores no secret for this method. Your workload identity pool trusts a short-lived token that Braze issues for each connection. Braze can access your bucket only through the [role you grant](#wif-4), and you can revoke that access at any time by disabling or deleting the workload identity pool provider in Google Cloud.



Before you begin, make sure you have a Google Cloud Storage bucket for Braze to write to, and [create the custom role](#step-1-create-role) described in the service account key method. You don't need to create a service account key.

### Step 1: Enable the required APIs {#wif-1}

In the Google Cloud project where you'll create the workload identity pool, enable the **Security Token Service API** (`sts.googleapis.com`).

If you'll have Braze impersonate a service account (see [Step 4](#wif-4)), also enable the **IAM Service Account Credentials API** (`iamcredentials.googleapis.com`) in the project that contains the workload identity pool. If your service account is in a different project, enable it there too.

For detailed steps, see Google's [Enabling and disabling services](https://cloud.google.com/service-usage/docs/enable-disable).

### Step 2: Get the Braze values {#wif-2}

In Braze, go to **Currents** > **Create New Current** > **Google Cloud Storage Data Export**, then select the **Workload Identity Federation** tab under **Credentials**. Braze displays the **Issuer URL**, **Subject**, and **Braze audience** values you need for the next steps. Keep this page open, or copy the values somewhere you can reach them.

The **Issuer URL** is specific to the Braze environment your dashboard runs on, and the **Braze audience** is unique to your workspace and doesn't change.

### Step 3: Create a workload identity pool and provider {#wif-3}

In the Google Cloud console, go to **IAM & Admin** > **Workload Identity Federation**, then select **Create pool**:

1. Enter a name for the pool (for example, `braze-currents`), then select **Continue**.
2. For **Select a provider**, select **OpenID Connect (OIDC)**, and enter a name for the provider.
3. For **Issuer (URL)**, enter the **Issuer URL** value from Braze.
4. For **Audiences**, select **Allowed audiences**, then enter the **Braze audience** value from Braze.
5. Select **Continue**. Under **Configure provider attributes**, map `google.subject` to `assertion.sub`.
6. Select **Save**.

For detailed steps, see Google's [Configure workload identity federation with other identity providers](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers).

**Important:**


Enter each value exactly as Braze shows it. Google Cloud matches the issuer and audience character for character, and a mismatch causes authentication to fail. If you add an [attribute condition](https://cloud.google.com/iam/docs/workload-identity-federation#conditions), it must allow the **Subject** value from Braze.



When you're finished, take note of the provider's full resource name. You'll provide it to Braze in [Step 5](#wif-5). It looks like this:

```
//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID
```

The resource name uses your project number, not your project ID. You can find the project number on your project's **Dashboard** in the Google Cloud console.

### Step 4: Grant access to your bucket {#wif-4}

Next, give Braze permission to write to your bucket. You can grant access directly to the Braze identity, or have Braze impersonate a service account you control.

#### Option 1: Grant access directly

In the Google Cloud console, go to **Cloud Storage** > **Buckets** and select your bucket. Then select **Permissions** > **Grant access**:

1. For **New principals**, enter the following, replacing `PROJECT_NUMBER` and `POOL_ID` with the values from your provider's resource name, and `SUBJECT` with the **Subject** value from Braze:
   ```
   principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
   ```
2. For **Role**, select the [custom role](#step-1-create-role) you created.
3. Select **Save**.

For detailed steps, see Google's [Add a principal to a bucket-level policy](https://cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

#### Option 2: Impersonate a service account

1. Go to **IAM & Admin** > **Service Accounts** and create a service account (for example, `braze-currents`). Don't create a key for it.
2. On your bucket, grant the service account the [custom role](#step-1-create-role) you created.
3. On the service account, go to **Permissions** > **Grant access**. For **New principals**, enter the `principal://` value from Option 1. For **Role**, select **Workload Identity User** (`roles/iam.workloadIdentityUser`). Then select **Save**.

Take note of the service account's email. You'll provide it to Braze in [Step 5](#wif-5).

For detailed steps, see Google's [Grant access to service accounts](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#access).

**Important:**


Without this role, Braze can authenticate to Google Cloud but can't write to your bucket. We recommend granting it on the bucket Braze writes to, rather than on the project, so Braze can access only that bucket.



### Step 5: Set up Currents {#wif-5}

Return to the **Google Cloud Storage Data Export** page in Braze. If you haven't already, enter your integration name and contact email.

Provide a contact email for integration error notifications. Braze sends notifications to this address if the integration encounters errors, such as credential issues or connectivity problems. To help ensure the right people receive alerts, use a distribution list or group email address.


For **Credentials**, make sure the **Workload Identity Federation** tab is selected and enter the following:

| Field | Value |
| ----- | ----- |
| Workload identity provider | The provider's full resource name from [Step 3](#wif-3). |
| Service account email (optional) | The service account email from [Option 2](#option-2-impersonate-a-service-account) in Step 4, if Braze impersonates a service account. Leave blank if you granted access directly. |
| GCS Bucket Name | The name of your bucket. |
| Prefix | A path prefix for your exported data within the bucket. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Workload identity federation fields" }

The **Issuer URL**, **Subject**, and **Braze audience** fields are read-only. They show the same values you entered in Google Cloud in [Step 3](#wif-3).

When you save, Braze checks that it can authenticate through your provider and write to your bucket. If the check fails right after you grant access in [Step 4](#wif-4), wait a few minutes for the IAM change to take effect, then try again.

Finally, scroll to the bottom of the page and select which message engagement events or customer behavior events you'd like to export. When completed, launch your Current.

## Updating GCS credentials for Currents {#updating-currents-credentials}

You can update the credentials on an existing Braze Currents connector without stopping the integration or losing data already exported to your bucket.

To refresh credentials—or to switch between the **Service account key** and **Workload Identity Federation** methods—finish the Google Cloud steps for your chosen method earlier in this article. Then, in Braze, go to **Currents**, locate your Google Cloud Storage connector in the list, select **Edit Current**, update **Credentials**, and select **Update Current**. Braze validates the credentials you enter; your connector keeps running and data already in your bucket remains available. For more information, see [Updating Currents in Set up Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/setting_up_currents/#updating-currents).

### Workload identity federation credentials

Workload identity federation has no secret to rotate or expire, so there's nothing to renew on a schedule. Keep the following in mind:

- **Changing your provider or service account:** If you create a new provider or service account, update the **Workload identity provider** or **Service account email** in Braze, and grant the new identity access as described in [Step 4](#wif-4).
- **Revoking access:** To stop Braze from writing to your bucket, disable or delete the workload identity pool provider in Google Cloud. You can also remove the role from your bucket, or the Workload Identity User role from your service account.
- **Braze values:** The issuer URL, subject, and audience Braze shows are fixed for your workspace. If you recreate the provider in Google Cloud, enter the same values.

If the provider is disabled or doesn't match the values in Braze, or if the role is removed, the connector can't authenticate or write to your bucket and stops sending events. Braze sends an integration error notification to your integration's contact email. If this persists for more than **5 days**, the connector's events are dropped, and data is permanently lost. To resume, correct the configuration in Google Cloud, or update the integration in Braze.

## Export behavior

Users who have integrated a cloud data storage solution and are trying to export APIs, dashboard reports, or CSV reports will experience the following:

- All API exports will not return a download URL in the response body and must be retrieved through data storage.
- All dashboard reports and CSV reports will be sent to the user's email for download (no storage permissions required) and backed up on Data Storage.

**Important:**


**JSON format requirement**: For JSON exports, Braze uses JSONL (newline-delimited JSON) format, where each line contains a separate JSON object. This format differs from standard JSON, which is a single JSON array or object. Each line in the exported file is a valid JSON object, but the file as a whole is not a single valid JSON document. When processing these files, parse each line individually as a separate JSON object rather than attempting to parse the entire file as a single JSON document.

Currents exports use Apache Avro format (`.avro` files), not JSON. This JSON format requirement applies to dashboard data exports and API exports that use JSON format.



## Troubleshooting

### Google Cloud Storage Credentials are invalid

If you receive the following error when attempting enter your credentials:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Ensure that your Google Cloud IAM service account has the following permissions:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

After verifying, you can [test your credentials in the Braze dashboard](#step-5-test-your-service-account-credentials-optional).
