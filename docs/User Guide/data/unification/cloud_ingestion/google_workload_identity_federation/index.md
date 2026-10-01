# Configuring Google Cloud for Workload Identity Federation

> This page covers how to configure your Google Cloud project so Braze Cloud Data Ingestion (CDI) can access BigQuery and Google Cloud Storage (GCS) with Workload Identity Federation (WIF). For the rest of the source setup, see [Data warehouse integrations](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=bigquery), [Connected sources](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/connected_sources?tab=bigquery), or [File storage integrations](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/file_storage_integrations?tab=google%20cloud%20storage).

With WIF, Braze authenticates to Google Cloud with a short-lived identity from its own AWS environment, and then impersonates a service account in your project. You configure your project to trust that identity for your workspace only. You don't create or share a service account key.

You set up WIF once per Google Cloud project. One WIF credential serves both BigQuery and GCS sources, so if you've already completed these steps for one, grant the existing service account access to the new data in [Step 6](#step-6-grant-the-service-account-access-to-your-data) and skip the rest.

## Prerequisites

To complete these steps in the Google Cloud console, you need permission to create workload identity pools and service accounts, and to manage Identity and Access Management (IAM) policies on the service account and your data. For example, you can use the Workload Identity Pool Admin (`roles/iam.workloadIdentityPoolAdmin`) and Service Account Admin (`roles/iam.serviceAccountAdmin`) roles.

## Trust only your workspace's principal {#trust-only-your-workspaces-principal}

**Warning:**


Grant access to the full Braze principal Amazon Resource Name (ARN) from your credential form. Don't grant access to the Braze AWS role or AWS account. A role-level or account-level grant lets other Braze customers read your data.



Every Braze workspace on the same Braze instance presents the same AWS role. Only the session name at the end of the principal ARN, which is your workspace ID, is unique to you.

Google's default attribute mapping for AWS providers sets `aws_role` to the role ARN without the session name. This means granting access to identities that match an `aws_role` value, such as `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.aws_role/ROLE_ARN`, trusts every Braze workspace on your instance, including yours.

To keep your data scoped to your workspace:

- Grant access only to identities whose `subject` is your full Braze principal ARN. This is the `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/BRAZE_PRINCIPAL_ARN` principal.
- Don't grant access to **All identities in the pool**, or to identities filtered by `aws_role` or `account`.
- Don't write an attribute condition that checks only the AWS account or role.
- Keep the default attribute mapping for `google.subject`, which is `assertion.arn`.

The Braze principal ARN differs for each workspace and Braze instance, and Braze uses a separate AWS role for Google sources than for other sources such as Snowflake. Always copy the value from a BigQuery or GCS credential form in the workspace you're connecting.

## Setting up Workload Identity Federation

### Step 1: Copy the Braze principal ARN {#step-1-copy-the-braze-principal-arn}

In Braze, start creating your BigQuery or GCS source and select **Workload Identity Federation** as the authentication method. Copy the value in step 1 of the credential form, **Copy the Braze principal ARN**, and keep the form open.

If the field shows **Unavailable**, WIF isn't available for your Braze instance. Use a service account key instead.

### Step 2: Enable the required APIs

In the Google Cloud console, go to **APIs & Services** > **Library**, and enable the following APIs for your project:

- IAM Service Account Credentials API
- Security Token Service API
- Identity and Access Management (IAM) API

### Step 3: Create the workload identity pool and provider

1. Go to **IAM & Admin** > **Workload Identity Federation**, and then select **Create pool**.
2. Enter a name for the pool, such as "Braze CDI". Note the **Pool ID**, and then select **Continue**.
3. For **Select a provider**, select **AWS**.
4. Enter a provider name, such as "Braze AWS", and note the **Provider ID**.
5. For **AWS account ID**, enter the 12-digit number that follows `arn:aws:sts::` in the Braze principal ARN, and then select **Continue**.
6. Under **Configure provider attributes**, keep the default mapping, including `google.subject` = `assertion.arn`.
7. Select **Save**.

Pool and provider IDs must be 4 to 32 characters, using lowercase letters, numbers, and hyphens.

#### Restrict the provider to your principal (optional)

For defense in depth, add an attribute condition so the provider accepts only your workspace's principal. Google then rejects every other identity at the token exchange, before Google checks any service account permission.

1. In the pool, select the provider, and then select **Edit**.
2. Under **Attribute conditions**, select **Add condition**.
3. Enter the following condition, replacing *`BRAZE_PRINCIPAL_ARN`* with the full value that you copied in Step 1:

    ```text
    assertion.arn == 'BRAZE_PRINCIPAL_ARN'
    ```

4. Select **Save**.

This condition dedicates the provider to one Braze workspace. To connect another workspace, create a separate provider for it, or list both principals, as in `assertion.arn in ['FIRST_BRAZE_PRINCIPAL_ARN', 'SECOND_BRAZE_PRINCIPAL_ARN']`.

### Step 4: Create the service account

If you already have a service account for Braze, such as one from the GCS setup, skip this step.

1. Go to **IAM & Admin** > **Service Accounts**, and then select **Create service account**.
2. Enter a name, such as "Braze CDI", and then select **Create and continue**.
3. Skip the optional project role and user access steps, and then select **Done**. You grant data access in Step 6.

### Step 5: Bind the Braze principal to the service account {#step-5-bind-the-braze-principal-to-the-service-account}

Grant your workspace's principal permission to impersonate the service account:

1. Go to **IAM & Admin** > **Workload Identity Federation**, and then select your pool.
2. Select **Grant access**, and then select **Grant access using service account impersonation**.
3. For **Service account**, select the service account from Step 4.
4. Under **Select principals**, select **Only identities matching the filter**.
5. For **Attribute name**, select **subject**. For **Attribute value**, paste the full Braze principal ARN from Step 1.
6. Select **Save**. If Google offers to download a client library configuration file, select **Dismiss**. Braze doesn't need it.

This grants the Workload Identity User role (`roles/iam.workloadIdentityUser`) on the service account to a principal in this form:

```text
principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/BRAZE_PRINCIPAL_ARN
```

To confirm, open the service account and select the **Permissions** tab. The Workload Identity User role should list this principal, ending in your full Braze principal ARN.

**Warning:**


Don't select **All identities in the pool**, and don't filter by **aws_role**. Both match every Braze workspace on your Braze instance, because they all share the same AWS role. For details, see [Trust only your workspace's principal](#trust-only-your-workspaces-principal).



Grant this role on the service account only. A project-level grant lets the principal impersonate every service account in the project.

IAM changes can take a few minutes to take effect. If a connection test fails right after you grant access, wait a few minutes and try again.

### Step 6: Grant the service account access to your data {#step-6-grant-the-service-account-access-to-your-data}

Grant the service account the permissions for your source:

- **BigQuery:** The BigQuery roles in Step 1.2 of [Data warehouse integrations](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=bigquery#step-12-create-credentials-for-braze), or in Step 2.1 of [Connected sources](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/connected_sources?tab=bigquery#step-21-create-credentials-for-braze)
- **Google Cloud Storage:** The bucket and subscription permissions in [Assign permissions](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/file_storage_integrations?tab=google%20cloud%20storage#step-5-assign-permissions)

If you use one credential for both sources, grant both sets of permissions to the same service account.

### Step 7: Enter the values in Braze

Return to the Braze credential form, and enter the following values from the Google Cloud console:

| Braze field | Where to find it |
| --- | --- |
| **Project number** | The **Project info** card on the console **Dashboard**. Use the numeric project number rather than the project ID. |
| **Workload identity pool ID** | The **Pool ID** from Step 3 |
| **Provider ID** | The **Provider ID** from Step 3 |
| **Service account email** | The service account's **Email** on the **Service Accounts** page |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Values to enter in Braze" }

Braze combines the project number, pool ID, and provider ID into the audience, which tells Google which provider validates the request from Braze. By default, a provider accepts its own resource name as the audience. If you set custom allowed audiences on your provider, include the provider's full resource name.

### Step 8: Test the connection {#step-8-test-the-connection}

When you test the connection in Braze, Braze also checks that your configuration trusts only your workspace. During the test, Braze attempts the same exchange with a test session name of all zeros, in this form:

```text
assumed-role/cdi-gcs-bigquery-sync-<deployment>/000000000000000000000000
```

Your configuration must reject this identity, either at the token exchange or when it tries to impersonate your service account. If both steps succeed, the test fails, because your configuration trusts identities other than your workspace's principal. To fix this, refer to the section [Your configuration trusts identities other than your workspace](#your-configuration-trusts-identities-other-than-your-workspace).

If you set the optional attribute condition, Google rejects the test identity at the token exchange. Otherwise, Google rejects the test identity when that identity tries to impersonate your service account. Either way, the test passes.

You may see this rejected attempt in your Google Cloud audit logs each time you test the connection. This behavior is expected. The attempt comes from the Braze check, and the attempt doesn't give anyone access to your data.

Don't add a condition that rejects only this test session. Such a condition passes the test while your configuration still trusts other Braze workspaces.

## Removing Braze access

To stop Braze from accessing your data, remove the Workload Identity User role for the Braze principal from the service account's **Permissions** tab, or delete the provider.

## Setting up with the gcloud CLI

If you prefer the command line, the following commands complete Steps 2 through 5. Replace the values in the first block, and paste the Braze principal ARN exactly as copied.

```bash
PROJECT_ID="YOUR-PROJECT-ID"
POOL_ID="braze-cdi"
PROVIDER_ID="braze-aws"
SA_NAME="braze-cdi"
BRAZE_PRINCIPAL_ARN="PASTE-THE-BRAZE-PRINCIPAL-ARN-FROM-YOUR-CREDENTIAL-FORM"

PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"
BRAZE_AWS_ACCOUNT_ID="$(echo "$BRAZE_PRINCIPAL_ARN" | cut -d: -f5)"
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"

gcloud services enable iam.googleapis.com iamcredentials.googleapis.com sts.googleapis.com \
  --project="$PROJECT_ID"

gcloud iam workload-identity-pools create "$POOL_ID" \
  --project="$PROJECT_ID" --location="global" --display-name="Braze CDI"

gcloud iam workload-identity-pools providers create-aws "$PROVIDER_ID" \
  --project="$PROJECT_ID" --location="global" --workload-identity-pool="$POOL_ID" \
  --account-id="$BRAZE_AWS_ACCOUNT_ID"

# Optional: restrict the provider to your principal
gcloud iam workload-identity-pools providers update-aws "$PROVIDER_ID" \
  --project="$PROJECT_ID" --location="global" --workload-identity-pool="$POOL_ID" \
  --attribute-condition="assertion.arn == '${BRAZE_PRINCIPAL_ARN}'"

# Skip if you already have a service account for Braze
gcloud iam service-accounts create "$SA_NAME" \
  --project="$PROJECT_ID" --display-name="Braze CDI"

gcloud iam service-accounts add-iam-policy-binding "$SA_EMAIL" \
  --project="$PROJECT_ID" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL_ID}/subject/${BRAZE_PRINCIPAL_ARN}"
```

## Troubleshooting

### Your configuration trusts identities other than your workspace {#your-configuration-trusts-identities-other-than-your-workspace}

The connection test fails with the following error:

> Your workload identity pool trusts every Braze customer, not only this workspace. Braze authenticated against it with a test identity (000000000000000000000000) that belongs to no Braze workspace, and your Google Cloud project accepted it, so another Braze customer could read this data. Grant the Workload Identity User role on your service account to the full Braze principal shown on the credential screen (principal://.../subject/&lt;full ARN&gt;) rather than to the role (principalSet://.../attribute.aws_role/...); restricting the pool provider's attribute condition to that same principal works as well. Then test the connection again.

This means Google accepted the Braze test identity at both the token exchange and the service account impersonation, as described in [Step 8](#step-8-test-the-connection). This error usually happens when the service account grants access to all identities in the pool, or to identities filtered by `aws_role`.

To fix this error:

1. In the Google Cloud console, open the service account and select the **Permissions** tab.
2. Find every principal with the Workload Identity User role that starts with `principalSet://` and references your pool. Remove the role from each one.
3. Make sure your full principal has the role, as in [Step 5](#step-5-bind-the-braze-principal-to-the-service-account).
4. Go to **IAM & Admin** > **IAM** and check for project-level Workload Identity User grants to your pool. Remove them.
5. Test the connection again.

Alternatively, restrict the provider's attribute condition to your full principal, as described in [Restrict the provider to your principal (optional)](#restrict-the-provider-to-your-principal-optional). Google then rejects every other identity at the token exchange. We still recommend granting access to your full principal only.

### Braze couldn't confirm that your pool trusts only this workspace {#braze-could-not-confirm-your-pool-trusts-only-this-workspace}

The connection test fails with the following error:

> Braze could not confirm that your workload identity pool trusts only this workspace. The check needs Google to explicitly refuse an identity that is not yours, and this attempt failed for another reason instead. Please try again; if it keeps happening, contact support.

The Braze check in [Step 8](#step-8-test-the-connection) didn't reach a result. For example, a network error or a temporary Google Cloud error interrupted the check. This error doesn't mean your configuration is too broad. Test the connection again. If the error keeps happening, contact [Braze Support](https://www.braze.com/docs/user_guide/administer/personal/braze_support).

### Permission denied when Braze impersonates the service account

The connection test fails with a permission error on `iam.serviceAccounts.getAccessToken`. Check the following:

- The service account's **Permissions** tab lists the Workload Identity User role for a principal that ends in your full Braze principal ARN, copied from a BigQuery or GCS credential form in the same workspace.
- The IAM Service Account Credentials API is enabled.
- You've waited a few minutes since granting access.

### The token exchange is rejected

The connection test fails at the Google Security Token Service token exchange. Check the following:

- The project number, pool ID, and provider ID that you entered in Braze match your Google Cloud configuration.
- The provider's AWS account ID matches the account ID in the Braze principal ARN.
- If you set an attribute condition, it contains your full principal ARN, exactly as copied.
- If you set custom allowed audiences, they include the provider's full resource name.
- The pool and provider are enabled.
