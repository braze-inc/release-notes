# Snowflake Cortex AI

> [Snowflake Cortex AI](https://docs.snowflake.com/user-guide/snowflake-cortex/llm-functions) provides serverless access to large language models (LLMs), including Claude and GPT, inside your Snowflake account.







































_This integration is maintained by Snowflake._

## About the integration

The Braze and Snowflake Cortex AI integration lets you connect your Snowflake account to Braze so you can use Cortex-hosted models when building custom AI agents. Braze uses your Snowflake programmatic access token to invoke Cortex LLM functions, and Snowflake bills the token usage to your Snowflake account. With this integration, your agents can generate personalized copy, make real-time decisions, or update catalog fields using Claude and GPT models hosted in Snowflake.

When you connect Snowflake Cortex AI, Braze shows a curated set of Cortex models for custom agents. The models available in Braze may differ from the full catalog in your Snowflake account, and availability also depends on your Snowflake region and configuration. For regional details, see [Snowflake Cortex model availability](https://docs.snowflake.com/en/user-guide/snowflake-cortex/model-availability).

For Snowflake Data Sharing and Cloud Data Ingestion, see [Snowflake](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake).

## Prerequisites

| Requirements | Description |
|---|---|
| Snowflake account | A Snowflake account with access to Cortex AI. |
| Programmatic access token | A Snowflake [programmatic access token](https://docs.snowflake.com/en/user-guide/authentication-programmatic-access-tokens) with the `SNOWFLAKE.CORTEX_USER` database role as its default role. |
| Account identifier | Your Snowflake account identifier (the part before `.snowflakecomputing.com` in your account URL). |
| Braze workspace permissions | [Edit External Integrations](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) permission to connect the Snowflake Cortex AI integration. |
| Braze instance | You can find your Braze instance on the [API overview page](https://www.braze.com/docs/api/basics/#endpoints) or from your Braze onboarding manager. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Create a programmatic access token in Snowflake

1. In your Snowflake account, create a [programmatic access token](https://docs.snowflake.com/en/user-guide/authentication-programmatic-access-tokens) for the user that invokes Cortex AI models.
2. Grant the `SNOWFLAKE.CORTEX_USER` database role to the token's user:
   ```sql
   GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO USER <username>;
   ```
3. Set the token's default role to `SNOWFLAKE.CORTEX_USER`. This ensures that Braze can invoke Cortex LLM functions without additional role switching.
4. Note your Snowflake account identifier. This is the part of your Snowflake account URL before `.snowflakecomputing.com`. For example, if your account URL is `myorg-myaccount.snowflakecomputing.com`, the account identifier is `myorg-myaccount`.

**Note:**


Cortex AI model availability varies by Snowflake region. If a model is unavailable in your account's home region, you can enable cross-region inference by setting `CORTEX_ENABLED_CROSS_REGION` on your Snowflake account. For details, see [Snowflake Cortex LLM Functions](https://docs.snowflake.com/user-guide/snowflake-cortex/llm-functions) and [Snowflake Cortex model availability](https://docs.snowflake.com/en/user-guide/snowflake-cortex/model-availability).



### Step 2: Connect Snowflake Cortex AI in Braze

1. Go to **Partner Integrations** > **Technology Partners** in the Braze dashboard and search for **Snowflake**.
2. In the Snowflake partner page, find the **Snowflake Cortex AI integration** panel.
3. Enter your **Snowflake programmatic access token** and **Snowflake account identifier**.
4. Select **Save**.

Braze verifies the credentials by calling Snowflake Cortex AI with a test prompt. When verification succeeds, your integration is ready to use. Braze displays a connected status with the date and time of the connection.

After you save, you can select Snowflake Cortex AI models when [creating a custom agent](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents/) in the Agent Console. Use the model picker as the source of truth for which Claude and GPT models are available for your workspace.

To confirm the integration is working, create a test agent that uses a Snowflake Cortex AI model. Enter a simple instruction, such as "Tell me a joke," and run a test invocation to verify the model responds as expected.

To remove the integration, select **Disconnect** on the Snowflake partner page.

## Billing and usage

When you run agents on Snowflake Cortex AI models, Snowflake bills the token usage directly to your Snowflake account. Braze does not charge for the LLM tokens consumed through Cortex.

Usage appears in your Snowflake account's billing as Cortex AI compute consumption. For details on Cortex AI pricing, see [Snowflake Cortex pricing](https://www.snowflake.com/en/data-cloud/cortex/pricing/).

Contact [Snowflake support](https://docs.snowflake.com/en/user-guide/contacting-support) with any issues or questions regarding your Snowflake account or Cortex access.
