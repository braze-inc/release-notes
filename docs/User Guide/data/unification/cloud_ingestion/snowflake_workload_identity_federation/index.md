# Configuring Snowflake for Workload Identity Federation

> This page covers how to connect Snowflake to Braze Cloud Data Ingestion (CDI) with Workload Identity Federation. For role, warehouse, and database grants, and for the rest of source setup, see [Data warehouse integrations](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake), [Connected sources](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/connected_sources?tab=snowflake), or [SQL editor](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/sql_editor).

With Workload Identity Federation, Braze authenticates to Snowflake as a service user bound to Braze's AWS identity for Snowflake. That user has no password and no RSA key. RSA key-pair authentication remains supported. Existing key-pair credentials keep working, and you don't need to migrate them.

Workload Identity Federation and RSA key-pair authentication are separate setup paths. Follow the steps for the method you select on the credential form.

If **Workload Identity Federation** isn't on the credential form, use **Key pair**.

## Use the Snowflake principal from this workspace

The statement on the Snowflake credential form includes the Braze principal for Snowflake. That principal is an Amazon Resource Name (ARN) for Braze's AWS role for Snowflake. It is specific to your workspace and to your Braze instance.

Braze uses a different AWS role for Snowflake than it uses for Google BigQuery and Google Cloud Storage. Copy the statement from the Snowflake credential form in the workspace you're connecting. A principal from a BigQuery or Google Cloud Storage credential form is Braze's AWS role for Google sources, so Snowflake rejects it for this user.

**Important:**


Run the statement Braze shows on the Snowflake credential form. The form fills in your username, your role, and the Braze principal for this workspace. A statement copied from another workspace, from a Google credential form, or from an example doesn't match this workspace, and the connection test fails.



## Prerequisites

Before you run the statement:

- Create the role, and grant database access, in [Step 1.2: Set up the role and database permissions](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-12-set-up-the-role-and-database-permissions). Connected sources also need permission to create tables. For that grant, see [Step 2.1: Create a role and grant permissions](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/connected_sources?tab=snowflake#step-21-create-a-role-and-grant-permissions).
- Grant the role access to a warehouse in [Step 1.3: Set up the warehouse and give access to Braze role](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-13-set-up-the-warehouse-and-give-access-to-braze-role).
- If your Snowflake account uses a network policy, allow Braze IP addresses as described in [Step 1.5: Allow Braze IPs in Snowflake network policy (optional)](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional). A `TYPE = SERVICE` user is still subject to that policy.
- Use a Snowflake role that can create or alter users and grant roles, such as `SECURITYADMIN`.

Create a separate Snowflake user for each Braze workspace that connects to the same Snowflake account. Within one workspace, you can reuse the same user across integrations.

## What the generated statement does

Braze generates the statement on the Snowflake credential form. The statement changes as you enter **Username** and **Role**, and it includes the Braze principal for Snowflake. Run the statement from the form. This page describes the statement so you know what you're running.

### Create user

**Create user** is for a new Snowflake user. The statement is a `CREATE USER` command that does the following:

- Sets `WORKLOAD_IDENTITY` to `TYPE = AWS`, with the ARN set to the Braze principal for Snowflake shown on this credential form. That binding is what lets Braze authenticate as the user.
- Sets `TYPE = SERVICE`. The user is a service user, with no password and no RSA public key. Snowflake accepts `WORKLOAD_IDENTITY` on a service user.
- Sets `DEFAULT_ROLE` to the role you entered. Snowflake activates that role when Braze connects.
- Grants that role to the user, which allows the user to use it.

### Alter user

**Alter user** is for a username that already exists. The statement is an `ALTER USER` command that does the following:

- Sets `TYPE = SERVICE`. Workload Identity Federation requires a service user. If the user still has a password, Snowflake rejects this change before it binds the user to the Braze principal. Remove the password before you run the statement, or create a new service user instead.
- Sets `WORKLOAD_IDENTITY` to `TYPE = AWS`, with the ARN set to the same Snowflake principal.
- Grants the role you entered. If the user already has that role, the grant leaves the user unchanged.

Use the statement as the form generates it. The statement sets `TYPE = AWS` and the ARN of the Braze principal for Snowflake.

## Run the statement {#run-the-statement}

1. In Braze, go to **Data Settings** > **Cloud Data Ingestion** > **Sources**, select **Add data source**, and then select **Snowflake**.
2. Enter a **Credential name**, and then select **Workload Identity Federation**.
3. Under **Braze setup**, enter **Account Locator**, **Username**, and **Role**. For the account locator value, see [Step 2.1: Add Snowflake connection information](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-21-add-snowflake-connection-information).
4. Select **Create user** or **Alter user**.
5. When **Copy statement** is available, select **Copy statement**. If the statement still shows a placeholder for the principal, wait until Braze replaces it. If the form says Workload Identity Federation isn't available on this deployment, select **Key pair** instead.
6. In Snowsight, open a worksheet and run the statement.
7. Return to the Braze credential form and select **Save credential**.
8. Enter the warehouse, database, and schema for the source, select **Test connection**, and then select **Connect to Source**.

## Review a Snowflake credential {#review-a-snowflake-credential}

After you save a credential, review it on the **Credentials** page. Each source has its own section.

1. Go to **Data Settings** > **Cloud Data Ingestion** > **Credentials**.
2. Find **Snowflake Data Access Credentials**.
3. In that section, select the credential name.

The detail modal shows **Authentication method**, **Account Locator**, **Username**, and **Role**. **Used by** lists the sources and syncs that use the credential.

A Workload Identity Federation credential doesn't include an RSA public key. A key-pair credential also shows **RSA public key (primary)**. Select **View** to expand the `ALTER USER` statement for the current public key. To replace the key, select **Rotate credential**, and then select **Generate new key**. Run the new statement in a Snowflake worksheet. Braze moves the previous public key to a secondary key, which stays active while you install the new public key. For the rest of the key-pair setup, see [Authenticate the Snowflake user](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-22-authenticate-the-snowflake-user).

## Troubleshooting

### The statement isn't ready to copy

**Copy statement** stays unavailable in two cases:

- The form shows "Error loading the Braze principal ARN". Reload the page and open the credential form again.
- The form shows "Workload Identity Federation is not available on this deployment yet. Use a key pair instead." Select **Key pair**.

### The connection test fails after you run the statement

Check the following:

- You ran the statement from the Snowflake credential form in this workspace, after **Username** and **Role** were filled in.
- The Snowflake user is `TYPE = SERVICE` and has no password.
- The role, warehouse, and database grants from the prerequisites exist, and the statement's role grant succeeded.
- If the account uses a network policy, Braze IP addresses are allowed. See [Step 1.5: Allow Braze IPs in Snowflake network policy (optional)](https://www.braze.com/docs/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional).

### Alter user fails because the user has a password

Snowflake rejects `TYPE = SERVICE` for a user that still has a password, so the user keeps its current type. Remove the password and run the statement again, or select **Create user** and use a new username.
