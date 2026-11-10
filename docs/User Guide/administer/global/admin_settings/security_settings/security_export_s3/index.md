# Security events export to cloud storage

> You can automatically export security events to Amazon S3, Microsoft Azure Blob Storage, or Google Cloud Storage with a daily job that runs at midnight UTC. After setting up, you don't need to manually export security events from the dashboard. The job exports the security events for the past 24 hours in CSV format to your configured storage. The CSV file uses the same columns as a manually exported report, plus a `Version` column.

**Important:**


Security event cloud export availability depends on your platform edition. If this feature isn't in your workspace, contact your customer success manager for information.<br><br>Starting December 2026, this export is planned to run hourly instead of daily. Review any downstream jobs that expect a single daily file.



**Note:**


Security event cloud exports aren't subject to the 10,000-row limit that applies to manual CSV report downloads from the dashboard.



## Set up cloud export in Braze

You can configure only one cloud storage provider at a time. Saving credentials for a provider removes any previous security event export configuration for a different provider.

1. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section.
2. Under **Export to cloud storage**, turn on **Export security event report to cloud storage**.
3. For **Cloud storage provider**, select **AWS S3**, **Azure**, or **Google Cloud Storage**.
4. Follow the steps for your provider.




Braze supports two S3 authentication and authorization methods:
- AWS secret access key method
- AWS role ARN method

### AWS secret access key method

This method generates a secret key and an access key ID that allows Braze to authenticate as a user on your AWS account to write data to your bucket.

#### Step 1: Create an Identity and Access Management (IAM) user

To retrieve your secret access key and access key ID, you’ll need to create an IAM user, following the instructions in [Setting up your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

#### Step 2: Get credentials

1. After creating a new user, generate the access key and download your access key ID and secret access key.

![A summary page for a role called "liyu-chen-test".](https://www.braze.com/docs/assets/img/security_export/credentials1.png?fda727b860ccdbba2be9bc20fbab87a8)

{: start="2"}
2. Take note of these credentials somewhere or download the credential files, because you’ll need to input these into Braze later on.

![Fields containing the access key and secret access key.](https://www.braze.com/docs/assets/img/security_export/retrieve_access_keys.png?3d6c06ae42ec03c5587087235a3fd6ed)

#### Step 3: Create policy

1. Go to **IAM** (Identity and Access Management) > **Policies** > **Create Policy** to add permissions for your user.
2. Select **Create Your Own Policy**, which gives limited permissions so Braze can only access the specified buckets.
3. Specify a policy name of your choice.
4. Input the following code snippet into the **Policy Document** section. Be sure to replace "INSERTBUCKETNAME" with your bucket name. Without these permissions, the integration will fail a credentials check and not be created.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```

#### Step 4: Attach policy

1. After creating a new policy, go to **Users** and select your specific user.
2. In the **Permissions** tab, select **Add Permissions**, directly attach the policy, and then select that policy.

Now, you’re ready to link your AWS credentials to your Braze account!

#### Step 5: Link Braze to AWS

1. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section.
2. Turn on **Export security event report to cloud storage**, then select **AWS S3** as the **Cloud storage provider**.
3. Select **AWS secret access key**.
4. Input the following:
- AWS access key ID
- AWS bucket name
- AWS secret access key
    - When inputting this key, first select **Test Credentials** to confirm your credentials work.

{: start="5"}
5. Select **Save Changes**.

You’ve integrated AWS S3 into your Braze account!

### AWS role ARN method

The AWS role ARN method generates a role Amazon Resource Name (ARN) that allows the Braze Amazon account to authenticate as a member of that role.

#### Step 1: Create policy

1. Sign in to the AWS management console as an account administrator.
2. In the AWS console, go to the **IAM** (Identity and Access Management) section > **Policies**, and then select **Create Policy**.

![A page with a list of policies and button to "Create policy".](https://www.braze.com/docs/assets/img/security_export/policies.png?fbee7f9c445e84fff9e0ab18b01a29f3)

{: start="3"}
3. Open the **JSON** tab and input the following code snippet into the **Policy Document** section. Be sure to replace `INSERTBUCKETNAME` with your bucket name.

```json
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{: start="4"}
4. Select **Next** after reviewing the policy.

![A page that allows you to review your policy and optionally add permissions.](https://www.braze.com/docs/assets/img/security_export/specify_permissions.png?904867ef2cceb9537c27cba61c4e0d6b)

{: start="5"}
5. Give the policy a name and description, and then select **Create Policy**.

![A page to review and create your policy.](https://www.braze.com/docs/assets/img/security_export/review_and_create.png?198cc7420e2664188017f8678c2e7342)

#### Step 2: Create role

1. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section.
2. Turn on **Export security event report to cloud storage**, then select **AWS S3** as the **Cloud storage provider**.
3. Select **AWS Role ARN**.
4. Take note of the identifiers, Braze account ID, and Braze external ID needed to create your role.
5. In the AWS console, go to the **IAM** (Identity and Access Management) section > **Roles** > **Create Role**.
6. Select **Another AWS Account** as the trusted entity selector type.
7. Provide your Braze account ID, check the **Require external ID** box, and then enter your Braze external ID.
8. Select **Next** when complete.

![A page with options to select a trusted entity type and provide information about your AWS account.](https://www.braze.com/docs/assets/img/security_export/select_trusted_entity.png?b2e98455dc208fbb49397e75a0196e84)

#### Step 3: Attach policy

1. Search for the policy you created earlier in the search bar, and then place a checkmark next to the policy to attach it.
2. Select **Next**.

![A list of policies with columns for their type and description.](https://www.braze.com/docs/assets/img/security_export/add_permissions.png?ef23d4f17651b56a0cbdd2de64998fc2)

{: start="3"}
3. Give the role a name and a description, and select **Create Role**.

![Fields to provide role details, such as the name, description, trust policy, permissions, and tags.](https://www.braze.com/docs/assets/img/security_export/name_review_create.png?8fa678143b8355b43748274d50f5de44)

Your newly created role will appear in the list!

#### Step 4: Link to Braze AWS

1. In the AWS Console, find your newly created role in the list. Select the name to open up the details of that role, and take note of the **ARN**.

![The summary page for a role called "security-event-export-olaf".](https://www.braze.com/docs/assets/img/security_export/credentials2.png?9733cef1900870b97dc585b144835ccb)

{: start="2"}
2. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section.
3. Make sure **AWS S3** is selected as the **Cloud storage provider** and **AWS role ARN** is selected, then input your role ARN and AWS S3 bucket name in the designated fields.
4. Select **Test Credentials** to confirm your credentials work properly.
5. Select **Save Changes**.

You’ve integrated AWS S3 into your Braze account!








**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





Use a Microsoft Azure storage account connection string and a blob container for security event exports. For more detail on creating an Azure storage account, retrieving a connection string, and creating a blob container, see [Microsoft Azure Blob Storage](https://www.braze.com/docs/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/#connection-string-auth-method).

### Step 1: Get Azure credentials

1. In Microsoft Azure, create or open a storage account you want to use for security event exports.
2. From the storage account, open **Access keys** and copy a **Connection string**. Braze uses the connection string, not the key alone.
3. Under **Blob service**, create a blob container (or use an existing one) and note the container name.
4. Optionally choose a storage prefix Braze should use when writing files.

### Step 2: Link Braze to Azure

1. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section.
2. Turn on **Export security event report to cloud storage**, then select **Azure** as the **Cloud storage provider**.
3. Input the following:
- Azure storage container name
- Azure connection string
- Azure storage prefix (optional)

{: start="4"}
4. Select **Test Credentials** to confirm your credentials work properly.
5. Select **Save Changes**.

You’ve integrated Azure Blob Storage into your Braze account!








**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





Use a Google Cloud Storage bucket and a service account JSON key for security event exports. Braze needs permission to get information about the bucket (`storage.buckets.get`) and create objects in it (`storage.objects.create`).

For more detail on creating a custom role, service account, and JSON key, see [Google Cloud Storage](https://www.braze.com/docs/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/#integration).

### Step 1: Get Google Cloud Storage credentials

1. In Google Cloud, create a custom role that includes at least:

- `storage.buckets.get`
- `storage.objects.create`

{: start="2"}
2. Create a service account, grant it that role, and create a **JSON** key.
3. Note your GCS bucket name and, optionally, a prefix Braze should use when writing files.

### Step 2: Link Braze to Google Cloud Storage

1. In Braze, go to **Settings** > **Company Settings** > **Admin Settings** > **Security Settings** and scroll to the **Security Event Download** section.
2. Turn on **Export security event report to cloud storage**, then select **Google Cloud Storage** as the **Cloud storage provider**.
3. Input the following:
- Google Cloud Storage bucket name
- Google Cloud Storage credentials JSON
- Google Cloud Storage prefix (optional)

{: start="4"}
4. Select **Test Credentials** to confirm your credentials work properly.
5. Select **Save Changes**.

You’ve integrated Google Cloud Storage into your Braze account!



