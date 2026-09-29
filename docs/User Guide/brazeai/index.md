## Start with your goal

Each goal has one recommended starting point. You can also combine features. For more information, see [Features that work well together](#features-that-work-well-together).

| Your goal | Start with | Before you start |
| --- | --- | --- |
| Draft or refine copy, images, Liquid, or HTML in the dashboard | [BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator) | Uses your existing dashboard permissions. Actions count toward a company-wide daily usage limit. |
| Write message copy that changes per user, based on that user's data | [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents) | Message or Action Credits. Contact your account manager if you don't have them. |
| Classify, route, or enrich a user from their real-time context | [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents) | Same credits requirement. Deploy the agent in a Canvas step or a catalog field. |
| Find the best-performing variant of a campaign | [Optimize with BrazeAI](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection) | At least two active variants. Multi-send campaigns also need a conversion event and a re-eligibility window of 24 hours or more. |
| Find the best-performing path through a Canvas | [Winning Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) | An Experiment Paths step with more than one path. |
| Generate and test many content variants continuously | [Content Optimizer](https://www.braze.com/docs/user_guide/brazeai/content_optimizer) | Currently in beta, for email, push, and SMS/MMS/RCS. Contact your customer success manager to get started. |
| Personalize every send in a recurring email program, per recipient | [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go) | A recurring email program, and more than one option to choose between: creatives, subject lines, images, or send times. |
| Maximize a business or financial metric, including what offer to give | [Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) | Connected first-party data and the AI Decisioning Services team. Contact your customer success manager to scope it. |
| Send at the time each user is most likely to engage | [Intelligent Timing](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_timing) | Best results when time zones are set on user profiles. Not recommended with rate limiting or IP warming. |
| Send on the channel each user is most likely to engage with | [Intelligent Channel filter](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_channel) | Engagement data across two or more supported channels, and at least three messages per channel. |
| Score how likely a user is to churn | [Predictive Churn](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_churn) | Typically 300,000 monthly active users in a single workspace. |
| Score how likely a user is to take a specific action | [Predictive Events](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_events) | Enough users who have performed the event. For the current threshold, see [event analytics](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_events/analytics) (typically at least 3,500 users with Past Event Behavior). |
| Recommend products or content from a catalog | [Item recommendations](https://www.braze.com/docs/user_guide/brazeai/item_recommendations) | At least one catalog. For AI Personalized recommendations, see the [data guidelines](https://www.braze.com/docs/user_guide/brazeai/item_recommendations/creating_recommendations/ai). |
| Query Braze data from Claude, Cursor, ChatGPT, or another AI tool | [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server) | Dashboard permissions govern access. Not available if your workspace uses IP allowlisting. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="BrazeAI features by goal" }

**Tip:**


If a rule on clean data answers the question, use a standard Canvas step. Steps cost no credits. Use AI when a rule can't express the decision.



## Reasoning or statistics

Every feature on this page decides something. These features split into two kinds. Knowing which kind you're looking at clears up most confusion between similar features.

Features that reason read the context in front of them (a user's profile, last message, or catalog row) and answer that one case. Braze Agents and Operator work this way. Features that reason handle unstructured text, judgment calls, open-ended writing, and users with no history. You can read the output and see why it says what it says. Features that reason don't learn from whether the output worked.

Features that learn find patterns in outcomes across many users, or across one user's own history. Predictive Suite, item recommendations, Intelligent Timing, the Intelligent Channel filter, and Decisioning Studio work this way. Features that learn handle numeric behavior at scale, aggregate signals, and large option sets. Features that learn don't read unstructured text such as a support thread.

Use this test: Could someone who read everything this one user has said and done already know what to do? If yes, you need reasoning. If that person still needs to test across thousands of users, you need statistics.

Each kind fits a different situation. The [features that work well together](#features-that-work-well-together) use both at once.

## Choose between similar features

### Optimize what you send

These features all improve what a message contains, in increasing order of scope.

| Feature | What it decides | Who it decides for |
| --- | --- | --- |
| [Optimize with BrazeAI](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection) | Which of your campaign variants wins | The audience as a whole |
| [Winning Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) | Which of your Canvas paths wins | The audience as a whole |
| [Content Optimizer](https://www.braze.com/docs/user_guide/brazeai/content_optimizer) | Which combination of content elements wins, from variants it generates for you | The audience as a whole |
| [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go) | Which creative to send (including its subject line, call to action (CTA), and image) and when to send it | Each recipient individually |
| [Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) | Which offer, channel, timing, and frequency to use | Each user individually |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Optimizing what you send" }

Optimize with BrazeAI, Winning Paths, and Content Optimizer find one winner for everyone. Decisioning Studio Go and Pro find a different answer for each person.

Within the first three:

- Optimize with BrazeAI tests message variants in a campaign.
- Winning Paths tests journey paths in a Canvas.
- Content Optimizer writes the variants for you and mixes their elements.

Go and Pro differ in scope and setup. Go optimizes engagement, is self-serve, and uses data already in Braze. Pro optimizes a business or financial metric, can decide offer values, and needs connected external data and the AI Decisioning Services team.

### Decide what to do for each user

| If you want to | Use | Why not the others |
| --- | --- | --- |
| Decide from one user's context, including free text or a judgment call | [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents) | Agents handle unstructured input and single-case judgment. Agents don't monitor whether a decision worked, and don't improve on their own. |
| Score how likely a user is to churn or act, as a number | [Predictive Suite](https://www.braze.com/docs/user_guide/brazeai/predictive_suite) | Predictive Suite learns from measured outcomes and reports its own accuracy. An agent can only give a plausible-sounding guess. |
| Pick items from a large catalog | [Item recommendations](https://www.braze.com/docs/user_guide/brazeai/item_recommendations) | A large catalog doesn't fit in an agent's context. An agent also tends to pick the same few items repeatedly. |
| Improve results against a metric, over time | [Decisioning Studio](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) | Decisioning Studio learns from outcomes and optimizes toward the metric you choose. Braze Agents don't learn from outcomes. |
| Set an offer value, or maximize revenue or margin | [Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) | Offer decisions weigh cost against uplift. Decisioning Studio Go is limited to engagement and doesn't decide offers. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Deciding what to do for each user" }

### Generate content

[BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator) and [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents) both write, at different moments.

- Operator works with you in the dashboard while you're building. By default you [review and approve](https://www.braze.com/docs/user_guide/brazeai/operator/reviewing_actions) each proposed action. Some actions always require approval. Use it to draft, rewrite, brainstorm, review a journey, or work through a blocker.
- Braze Agents work without you, at send time. You write instructions once, and the agent produces a different result for each user as that user passes through a Canvas. Use Braze Agents when the content must vary per user.

[BrazeAI generative AI capabilities](https://www.braze.com/docs/user_guide/brazeai/generative_ai) (copywriting, images, Liquid, HTML templates, and content review) are reached through Operator.

## Features that work well together

When a job needs rich copy and a large catalog, split the work. [Item recommendations](https://www.braze.com/docs/user_guide/brazeai/item_recommendations) select from your catalog. A [Braze Agent](https://www.braze.com/docs/user_guide/brazeai/agents) writes the copy around those items.

A cart recovery journey can combine several features:

- Item recommendations select the products to feature.
- A Braze Agent writes copy around those products, using that user's context.
- Predictive Events scores how likely the user is to come back.
- Intelligent Timing and the Intelligent Channel filter decide when and where to send.
- Decisioning Studio Pro decides the offer when the cart value justifies the setup.

## Start with the lightest tool that does the job

Among the features that learn, capability and setup both rise in steps.

1. Read one dimension off a user's own history. [Intelligent Timing](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_timing) and the [Intelligent Channel filter](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_channel) are self-serve toggles with no added cost.
2. Learn one pattern across your whole population. [Predictive Churn](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_churn), [Predictive Events](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_events), and [AI item recommendations](https://www.braze.com/docs/user_guide/brazeai/item_recommendations/creating_recommendations/ai) are still self-serve, with moderate setup.
3. Optimize several levers at once, per user. [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go) has low setup on data already in Braze and optimizes engagement only.
4. Optimize every lever, including offers, against a key performance indicator (KPI). [Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) needs external data plus the AI Decisioning Services team.

Match the level to what the use case is worth. For a low-value or single-dimension need, a lighter tool usually fits better. Extra capability from a heavier tool often isn't worth the additional data and setup.

## Braze Agent versus decisioning agent

Braze uses the word *agent* for two different products. The difference is which kind of decision each one makes.

| Term | What it is |
| --- | --- |
| Braze Agent | An AI helper you configure in Agent Console and deploy in a Canvas step or a catalog field. It reasons over one user's context to write content, classify, route, or enrich data. It does not learn from whether its output worked. |
| Decisioning agent | A configuration in Decisioning Studio that manages an entire use case, such as winback or cross-sell. It learns from outcomes across your population to find the decision that maximizes your metric. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze Agent versus decisioning agent" }

Both decide. A Braze Agent decides by reading. A decisioning agent decides by measuring. If you're unsure which product a page covers, check whether it's about Braze Agents or Decisioning Studio.

## All BrazeAI features

### Enrich profiles and predict behavior

| Feature | What it does | How it decides |
| --- | --- | --- |
| [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents) (Canvas step) | Classifies, routes, or enriches a user from their real-time context, and composes copy | Large language model |
| [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents) (catalog field) | Writes, updates, or localizes item metadata | Large language model |
| [Predictive Churn](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_churn) | Scores 0–100 how likely a user is to churn | Gradient-boosted decision trees |
| [Predictive Events](https://www.braze.com/docs/user_guide/brazeai/predictive_suite/predictive_events) | Scores 0–100 how likely a user is to take an action | Gradient-boosted decision trees |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="BrazeAI data features" }

### Find what works best for a population

| Feature | What it does | How it decides |
| --- | --- | --- |
| [Optimize with BrazeAI](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection) | Tests campaign variants and shifts traffic to the winner | A/B/n test |
| [Winning Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) | Tests Canvas paths and shifts traffic to the winner | A/B/n test |
| [Content Optimizer](https://www.braze.com/docs/user_guide/brazeai/content_optimizer) | Mixes and matches content variants for population engagement. | Multi-armed bandit |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="BrazeAI experimentation features" }

### Choose the best action for each individual

| Feature | What it does | How it decides |
| --- | --- | --- |
| [Intelligent Timing](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_timing) | Finds each user's best send time | Statistics on that user's history |
| [Intelligent Channel filter](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_channel) | Ranks channels for each user by their history | Statistics on that user's history |
| [AI item recommendations](https://www.braze.com/docs/user_guide/brazeai/item_recommendations/creating_recommendations/ai) | Picks catalog items for each user | Deep learning |
| [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go) | Personalizes content, timing, and frequency for engagement | Reinforcement learning |
| [Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) | Personalizes every lever, including offers, against a business KPI | Reinforcement learning |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="BrazeAI decisioning features" }

### Get your own work done faster

| Feature | What it does | How it decides |
| --- | --- | --- |
| [BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator) | Builds, reviews, and analyzes campaigns and Canvases with you, in conversation | Large language model |
| [Generative AI](https://www.braze.com/docs/user_guide/brazeai/generative_ai) | Copy, images, Liquid, HTML templates, and content review, through Operator | Large language model |
| [Braze MCP server](https://www.braze.com/docs/user_guide/brazeai/mcp_server) | Exposes Braze data without personally identifiable information (PII) to tools such as Claude and Cursor (Model Context Protocol) | Integration, not a model |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="BrazeAI workflow features" }

## How Braze uses your data

BrazeAI features that use a Braze-provided large language model send your prompt and inputs to that model. Data sent to a Braze-provided model is not used to train or improve it. Output belongs to you. Braze asserts no copyright over it. Braze makes no warranty about AI-generated content.

Which model a feature uses, and how long the provider retains data, is documented on each feature's page:

- [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents#how-is-my-data-used-and-sent-to-braze-provided-llms)
- [Operator data privacy and security](https://www.braze.com/docs/user_guide/brazeai/operator/data_privacy_security)

You can also connect your own model provider, such as OpenAI, Anthropic, Google Gemini, or Databricks Mosaic, when using [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents).

## Frequently asked questions

**What is BrazeAI?**


BrazeAI is the set of AI features built into Braze. It covers data enrichment, experimentation, decisioning, and dashboard workflow. Each feature is set up separately, and some require specific credits or plans. To find the feature you need, see [Start with your goal](#start-with-your-goal).



**Which BrazeAI feature should I use first?**


If you're new to BrazeAI, start with [BrazeAI Operator](https://www.braze.com/docs/user_guide/brazeai/operator). It needs no separate product setup, works in the composers you already use, and by default asks you to approve each action before it takes it. From there, pick the feature that matches your goal in [Start with your goal](#start-with-your-goal).



**How do I choose between two features that sound similar?**


Ask whether someone who read everything this one user has said and done could already decide. If the answer needs testing across thousands of users, use a feature that learns. Reasoning fits Braze Agents. Learning fits Predictive Suite or Decisioning Studio. See [Reasoning or statistics](#reasoning-or-statistics).



**What is the difference between Content Optimizer and Optimize with BrazeAI?**


Optimize with BrazeAI picks a winner from campaign variants you wrote. Content Optimizer generates variants for you and keeps mixing and testing their elements in a Canvas step. Both find one winner for your audience. For per-user personalization, see [Decisioning Studio](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio).



**What is the difference between a Braze Agent and a decisioning agent?**


A Braze Agent reasons over one user's context. A decisioning agent in Decisioning Studio learns from measured outcomes across your population. For more information, see [Braze Agent versus decisioning agent](#braze-agent-versus-decisioning-agent).



**Do BrazeAI features cost credits?**


Some BrazeAI features cost credits. Braze Agents require Message or Action Credits, and each agent run counts against a daily invocation limit. Operator actions count toward a separate company-wide daily usage limit rather than credits. Features such as Intelligent Timing and Optimize with BrazeAI have no credit cost, but do have data requirements. If a rule answers your question, use a standard Canvas step. Contact your account manager about credits.



**Can I use my own AI model?**


Yes, with [Braze Agents](https://www.braze.com/docs/user_guide/brazeai/agents). Agents can connect to providers such as OpenAI, Anthropic, Google Gemini, or Databricks Mosaic instead of the Braze-provided model. Other BrazeAI features use Braze-provided models only.


