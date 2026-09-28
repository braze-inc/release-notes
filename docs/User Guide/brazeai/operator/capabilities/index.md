# What you can do with Operator {#operator-capabilities}

> [BrazeAI Operator™](https://www.braze.com/docs/user_guide/brazeai/operator) is an AI assistant built into the Braze dashboard. It answers questions, composes messages, and acts across supported pages—describe what you want in natural language and Operator handles it in context.

Operator has the same dashboard access you do. If you can't do something in Braze, Operator can't either. Within that access, a small number of actions are off-limits by design, see [Operator's boundaries](#limitations).

Operator understands your workspace—custom attributes, Connected Content, the page you're working on, and any brand guidelines you add as context—so its output is grounded in your actual data. When Operator proposes a change, it shows the change as a visual diff in an [action card](https://www.braze.com/docs/user_guide/brazeai/operator/reviewing_actions) that you review and approve before anything is saved. Because Operator uses your own permissions, some actions require the permission for that surface—for example, configuring a custom AI agent requires "Create/Edit Custom AI Agents". See the [list of permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) for what's required for a given action. If you don't see an entry point for something Operator should be able to help with, check with your Braze administrator to confirm you have the necessary permission.

You can keep the conversation going with follow-ups. Operator remembers earlier messages until you clear your chat history.

## What Operator can do {#what-operator-can-do}

Operator can help at nearly every stage of building and running a program, from setting up your audience to reporting on results.

| Task | How Operator can help |
| --- | --- |
| <a id="workspace-settings"></a>Access controls, roles, and security | Ask Operator to review or update [roles and permission sets](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) and [security settings](https://www.braze.com/docs/user_guide/administer/global/admin_settings/security_settings), including [SCIM provisioning](https://www.braze.com/docs/user_guide/administer/global/user_management/automated_user_provisioning), instead of configuring each one by hand. |
| <a id="generate-data-transformation-code"></a>Ingestion pipelines (data mapping) | When you're connecting a new data source or updating how an existing one maps into Braze, ask Operator to draft or revise the [transformation code](https://www.braze.com/docs/user_guide/data/unification/data_transformation) that turns the incoming webhook payload into a Braze API request. |
| Ongoing data quality and hygiene | Ask Operator to map an [import](https://www.braze.com/docs/user_guide/audience/manage_audience/import_users) file to the correct Braze fields, or reconcile duplicate profiles when [merging](https://www.braze.com/docs/user_guide/audience/manage_audience/merge_duplicate_users) them—deciding which profile's data should win when records conflict. |
| <a id="campaigns-and-audiences"></a><a id="create-predictions"></a>Audience strategy | Describe the audience you're trying to reach in plain language—Operator builds the [segment](https://www.braze.com/docs/user_guide/audience/segments) logic, including attribute, event, and catalog conditions, or a SQL-based [Segment Extension](https://www.braze.com/docs/user_guide/audience/segments/segment_extension). It can also propose [Predictive Churn](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_churn) and [AI Item Recommendation](https://www.braze.com/docs/user_guide/brazeai/item_recommendations/creating_recommendations/ai) predictions to help you decide who to target. |
| <a id="canvases"></a>Map the customer lifecycle and define campaign or Canvas strategies | Describe a lifecycle moment—"someone abandons their cart"—or a campaign brief, and Operator drafts the [campaign or Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas) end to end, including audience, content, delivery settings, entry criteria, steps, and send-time recommendations. Refine it with follow-up prompts before you launch it. You can also ask Operator to edit an existing one—adding or removing Canvas steps, adjusting connections, or setting up an A/B test variant. |
| <a id="generate-copy"></a><a id="generate-messages"></a><a id="create-content-blocks"></a><a id="create-message-templates"></a><a id="generate-images"></a>Build message content and creative | Ask Operator for any of the following, right in the composer you're building in: {::nomarkdown}<ul><li>Copy or a full message design, for any channel or editor, HTML or drag-and-drop</li><li>A <a href="/docs/user_guide/messaging/design_and_edit/content_blocks">Content Block</a></li><li>A <a href="/docs/user_guide/messaging/templates">message template</a></li><li>An <a href="/docs/user_guide/messaging/design_and_edit/media_library#generate-ai">image</a></li></ul>{:/} In drag-and-drop editors, Operator targets individual blocks when it edits, so you can ask it to rewrite one section, reorder rows, swap an image, or delete a block without regenerating the rest of your design. Each change includes a summary of what Operator did, so you can review the work before you save. <br><br>Content Blocks are created one at a time in the dashboard. To create them in bulk, use the <a href="/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block">Create Content Block API endpoint</a>. Because they're shared, updating one Content Block updates every message that references it. <br><br>Add <a href="/docs/user_guide/administer/global/workspace_settings/brand_guidelines">brand guidelines</a> as context in the Operator chat panel so generated copy, templates, and images match your brand's voice, tone, and style. |
| <a id="generate-liquid"></a>Personalize for audience and context | Ask Operator to personalize a message with real customer data—a first name, last purchase, or loyalty tier—with a fallback for missing values, using [Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid) grounded in your workspace's attribute, event, and catalog data. It can also review and explain existing Liquid in your campaigns, or translate your message for other markets. For prompting techniques, see [Best practices](https://www.braze.com/docs/user_guide/brazeai/operator#best-practices). |
| <a id="agents"></a>Configure an AI agent | Braze has two kinds of agents: general-purpose agents you build in [Agent Console](https://www.braze.com/docs/user_guide/brazeai/agents) for tasks like copywriting or journey routing, and [Decisioning Studio](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) agents, which personalize message content and timing using your data. Operator can help build or refine either one, including starting from an Agent Console [template](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator). |
| Set frequency capping rules | [Frequency capping](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping) rules combine channel, message capacity, frequency, and tag filters. Describe the cap you want—for example, "limit push to 2 per day, but let onboarding messages through"—and Operator builds the rule for your review before you save. |
| Set up email sending | Setting up [email sending](https://www.braze.com/docs/user_guide/channels/email/email_setup/setting_up_ips_and_domains/email_self_serve) involves several sequential steps—adding a sending domain, a tracking domain, and a dedicated IP, then configuring the resulting DNS records. Operator can walk you through the correct order and flag common mistakes. |
| <a id="review-content-quality"></a>Test content, compliance, and approvals before you launch | Before you send, ask Operator to check your message for spelling, tone, stray code, or unrendered Liquid, check a Canvas for configuration errors, or verify your content against your workspace's messaging rules and rate limits. Operator can also tell you about your workspace's [approval workflows](https://www.braze.com/docs/user_guide/messaging/governance/approvals). |
| <a id="build-reports-and-dashboards"></a><a id="write-sql-queries"></a>Report to stakeholders | Describe the report or dashboard you need, and Operator drafts it from a natural-language brief—choosing the right metrics in [Report Builder](https://www.braze.com/docs/user_guide/analytics/reports/report_builder) or configuring [Dashboard Builder](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder) tiles (chart type, axes, filters), so you don't have to build them field by field. It also writes the underlying SQL for a Query Builder [query template](https://www.braze.com/docs/user_guide/analytics/reports/query_builder/query_templates). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tasks in your program lifecycle and how Operator can help" }

## Operator's boundaries {#limitations}

Operator has intentional limitations and can't complete these actions:

- Launch anything that would affect your users. Operator can prepare a campaign, Canvas, or other message content end to end, including edits to existing active content, but you always have to launch changes yourself.
- Confirm a permanent deletion. Operator can prepare it, but you have to type the confirmation text yourself.
- Download a file to your device
- Upload a file from your device
- Complete an external authentication or consent flow
- Request a change that affects your billing or contract, such as a plan upgrade
- Generate or invalidate an API key for a technology partner integration
- Send feedback to Braze about a feature
- Opt out of a warning with "Don't show me this again"

Operator also can't manage its own approval status. It can't:

- Approve its own proposed action
- Turn on your auto-approve setting on your behalf
- Say you approved something you didn't

For certain actions, Operator always pauses for your approval, even with your [auto-approve setting](https://www.braze.com/docs/user_guide/brazeai/operator/reviewing_actions#auto-approve-actions) turned on. For details, see [Operator's human-in-the-loop model](https://www.braze.com/docs/user_guide/brazeai/operator/data_privacy_security#human-in-the-loop-model).

## Usage limits {#usage-limits}

Operator has a company-wide daily usage limit that resets at midnight in your company's time zone. All Operator actions count toward this limit, and usage scales with how much Operator has to read and produce. Asking questions, looking up information, and [filing a support ticket](https://www.braze.com/docs/user_guide/brazeai/operator/support_tickets) are lighter usage. Creating or editing items such as campaigns and Canvases is heavier usage. [Image generations](#generate-images) also count toward this limit. If the limit is reached, a "Daily limit reached" message appears and Operator doesn't process further requests until the limit resets.

## How is my data used and sent to OpenAI? {#ai-policy} 
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per [OpenAI’s API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.


## Data privacy and security {#data-privacy-and-security}

Operator integrates with OpenAI to generate output. For more information about what information Braze sends to OpenAI, how that data is used, and your intellectual property rights, see [How data is used with OpenAI](https://www.braze.com/docs/user_guide/brazeai/operator#data-privacy-and-security).

## Next steps {#next-steps}

<ul class="guide_tiles"><li><a href="/docs/user_guide/brazeai/operator"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Get started with Operator</span><span class="guide_tile_description">Access and use Operator in the Braze dashboard.</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/operator/prompt_library"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Prompt library</span><span class="guide_tile_description">Browse ready-to-use example prompts.</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/operator/reviewing_actions"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Review actions</span><span class="guide_tile_description">Review and approve Operator&#39;s proposed changes.</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/operator/troubleshooting"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Troubleshooting</span><span class="guide_tile_description">Reference common issues and solutions.</span></span></div></a></li></ul>
