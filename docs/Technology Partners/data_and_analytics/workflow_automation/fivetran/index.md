# Fivetran

> [Fivetran](https://fivetran.com/) is a globally recognized brand whose analyst-focused products and fully managed pipelines enable data-backed decisions by delivering ready-to-query data into your cloud warehouse.

The Braze and Fivetran integration allows users to create a zero-maintenance pipeline that enables you to collect and analyze Braze data by connecting all of your applications and databases to a central warehouse. After data has been collected in the central warehouse, data teams can explore Braze data effectively using their preferred business intelligence tools. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Fivetran account | A [Fivetran](https://fivetran.com/login?next=%2Fdashboard) account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with the following permissions:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance](https://www.braze.com/docs/api/basics/#api-definitions). |
| Braze Currents | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) should be connected to either Amazon S3 or Google Cloud Storage. |
| Amazon S3 or Google Cloud Storage | This integration requires you have access to one Amazon S3 or Google Cloud Storage. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integration

The following Currents integration is supported for both [Amazon S3](#setting-up-braze-currents-for-s3) and [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Setting up Braze Currents for S3

#### Step 1: Locate your external ID {#step-one}

In the [Fivetran Dashboard](https://fivetran.com/dashboard), select **+ Connector**, and then select the **Braze** connector to launch the setup form. Next, select **Amazon S3**. Note the external ID provided here; you will need it to allow Fivetran to access your S3 bucket. 

![The Fivetran set up Braze connector form. The external ID field needed for this step is located in the middle of the page in a light gray box.](https://www.braze.com/docs/assets/img/fivetran_braze_setupform_as3.png?951c5ef6aef31f0a64aea2988342b5e2)

#### Step 2: Give Fivetran access to a specified S3 bucket

##### Creating an IAM policy

Open the [Amazon IAM Console](https://console.aws.amazon.com/iam/home#home) and navigate to **Policies > Create Policy**.

![Amazon IAM Console with list of policies.](https://www.braze.com/docs/assets/img/fivetran_as3_iam.png?2abed30996afca101747137f42cbfd5e)

Next, open the **JSON** tab and paste the following policy. Make sure to replace `{your-bucket-name}` with the name of your S3 bucket.


```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```


Lastly, select **Review Policy** and give the policy a unique name and description. Select **Create Policy** to build your policy. 

![Fields to name the policy and provide a description.](https://www.braze.com/docs/assets/img/fivetran_iam_policy_meta.png?05dd159d97c9f3c2cacfc84a269fea45)

##### Create an IAM role {#step-two}

In AWS, navigate to **Roles**, then select **Create New Role**.

![The "Roles" page with the button to create a new role.](https://www.braze.com/docs/assets/img/fivetran_iam_new_role.png?c79df0de44d187c44470e94d72be1798)

Select **Another AWS Account** and provide the Fivetran account ID `834469178297`. Make sure to check the **Require external ID** checkbox. Here, you will provide the external ID found in step 1.

![The field to input your "Account ID", a checkbox to require the external ID, and a blank textbox to input your "External ID".](https://www.braze.com/docs/assets/img/fivetran_another_aws_account.png?8a8801a1c92baf38b75891eb4abbb784)

Next, select **Next: Permissions** to select the policy you just created.

![List of policies.](https://www.braze.com/docs/assets/img/fivetran_as3_select_policy.png?445d0d69159c67b0df4dfa98719a8e1a)

Select **Next: Review**, name your new role (such as Fivetran), and select **Create Role**. After the role is created, select it and note the Role ARN shown.

![The Amazon S3 ARN listed in the role.](https://www.braze.com/docs/assets/img/fivetran_iam_role_arn.png?9a0f1f9ff014eaf860f723f39f453a91)

**Note:**


You can specify permissions for the Role ARN that you designate for Fivetran. Giving selective permissions to this Role will allow Fivetran to only sync what it has permissions to see.



#### Step 3: Complete the Fivetran connector

In Fivetran, select **+ Connector**, and then select the **Braze** connector to launch the setup form. Within the form, fill the given fields with the appropriate values:
- `Destination schema`: A unique schema name.
- `API URL`: Your Braze REST API endpoint.
- `API Key`: Your Braze REST API key. 
- `External ID`: The external ID set in [step 2](#step-two) of the Currents set up directions. This ID is a fixed value.
- `Bucket`: Found in your Braze account by navigating to **Partner Integrations** > **Data Export** > your Current name.
- `Role ARN`: The Role ARN can be found in [step 1](#step-one) of the Current setup directions.

**Important:**


Ensure **Amazon S3** is selected as the **Cloud Storage** choice.



Lastly, select **Save & Test**, and Fivetran will do the rest by syncing with the data from your Braze account!

### Setting up Braze Currents for Google Cloud Storage

#### Step 1: Retrieve your Fivetran email from Google Cloud Storage {#step-one2}

In the [Fivetran dashboard](https://fivetran.com/dashboard), select **+ Connector**, and  then select the **Braze** connector to launch the setup form. Next, select **Google Cloud storage**. Make a note of the email address that appears.

![The Fivetran set up Braze connector form. The email field needed for this step is located in the middle of the page in a light gray box.](https://www.braze.com/docs/assets/img/fivetran_braze_setupform_gcs.png?67a17a20bc89a3deaf4282da68a840a4)

#### Step 2: Grant bucket access

Navigate to your [Google Storage Console](https://console.cloud.google.com/storage/browser) and select the bucket you configured Braze Currents with, and select **Edit bucket permissions**.

![The Google Storage Console available buckets. Locate a bucket and select the vertical three dot icon to open the drop down that allows you to edit bucket permissions.](https://www.braze.com/docs/assets/img/fivetran_edit_bucket_permissions_gcs.png?cf67ec9124da304b1efb01ded726a6d9)

Next, grant `Storage Object Viewer` access to the email from [step 1](#step-one2) by adding the email as a member. Make a note of the bucket name; you will need it in the next step to configure Fivetran.

![Bucket with permissions.](https://www.braze.com/docs/assets/img/fivetran_add_members_gcs.png?f7b02ad77eaaeef7993fb02c82534d31)

#### Step 3: Complete the Fivetran connector

In Fivetran, select **+ Connector**, and then select the **Braze** connector to launch the setup form. Within the form, fill the given fields with the appropriate values:
- `Destination schema`: A unique schema name.
- `API URL`: Your Braze REST API endpoint.
- `API Key`: Your Braze REST API key. 
- `Bucket Name`: Found in your Braze account by navigating to **Partner Integrations** > **Data Export** > your Current name.
- `Folder`: Found in your Braze account by navigating to **Partner Integrations** > **Data Export** > your Current name.

**Important:**


Ensure **Google Cloud Storage** is selected as the **Cloud Storage** choice.



Lastly, select **Save & Test**, and Fivetran will do the rest by syncing with the data from your Braze account!

