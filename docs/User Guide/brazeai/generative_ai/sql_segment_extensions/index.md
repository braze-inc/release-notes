# AI SQL Generator

> Use the AI SQL Generator to describe an audience in plain language and generate Snowflake SQL for a SQL Segment Extension. This page covers the AI workflow. For creating, refreshing, and managing SQL Segment Extensions, see [SQL Segment Extensions](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments).

**Note:**


This feature is now part of [BrazeAI Operator™](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities), Braze's unified AI assistant. AI capabilities that were previously available as standalone assistants are now all accessible through Operator from wherever you're already working in the dashboard.




## Prerequisites

**Important:**


The AI SQL Generator is currently available as a beta feature. Contact your customer success manager if you're interested in participating in this beta trial.



To use the AI SQL Generator, you need these [permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) for your workspace:

| Permission | What it allows |
| --- | --- |
| "View Segments" | Open Segment Extensions and view SQL Segment Extensions |
| "Edit Segments" | Create, edit, and refresh SQL Segment Extensions |
| "View PII" | Run SQL preview queries that can return customer data |
{: .reset-td-br-1 .reset-td-br-2 aria-label="AI SQL Generator permissions" }

## Generate SQL for a Segment Extension

The AI SQL Generator uses [GPT](https://openai.com/gpt-4), powered by OpenAI, to recommend SQL for your SQL Segment Extension.

![AI SQL Generator with the prompt "Users that received a notification last month"](https://www.braze.com/docs/assets/img/ai_sql_generator.png?acea994f0ac93ccc2bf7e89098378667){: style="max-width:70%;"}

1. Create a [SQL Segment Extension](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments) with either full or incremental refresh.
2. Select **Launch AI SQL Generator**.
3. Enter your prompt and select **Generate** to translate it into SQL.
4. Review the generated SQL, then save your Segment Extension.

## Example prompts

- Users who received an email in the last month
- Users who made less than five purchases in the last year

## Tips

- Familiarize yourself with the available [Snowflake data tables](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Asking for data that doesn't exist in these tables may result in ChatGPT making up a fake table.
- Follow the [SQL writing rules](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql) for SQL Segment Extensions. For example, your SQL must select the `user_id` column. Starting your prompt with "users who" can help.
- You can send up to 20 prompts per minute with the AI SQL Generator.
- If the AI SQL Generator returns a statement that needs to be negated, it may automatically turn on **Invert SQL**. Confirm that the toggle matches the audience you want. For details, see [Determine if you need to invert SQL](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments#step-4-determine-if-you-need-to-invert-sql).

## How is my data used and sent to OpenAI? {#ai-policy} 
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per [OpenAI’s API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

