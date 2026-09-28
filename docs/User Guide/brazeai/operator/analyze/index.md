# Operator Analyze

> Operator Analyze is how Operator answers performance and analytics questions. Ask from the same conversation panel you use for everything else—about channel engagement, revenue, or industry benchmarks—and Operator returns charts, comparisons, insights, and recommendations pulled from your workspace data.

Operator Analyze is included with BrazeAI OperatorTM. Analytics questions count toward your company's Operator [usage limit](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities#limitations).

## Prerequisites

To use Operator Analyze, you need the "Use Operator", "View Dashboard Reports", and "View PII" [user permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) for your workspace. Analysis is scoped to the current workspace only. For how Operator uses your permissions, see [What you can do with Operator](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities).

## Analyze versus saved reports

Use Operator Analyze for quick conversational answers about performance from anywhere in the dashboard. Results appear in your Operator conversation thread.

Use [Report Builder](https://www.braze.com/docs/user_guide/analytics/reports/report_builder) or [Dashboard Builder](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder) when you need a saved report or dashboard you can revisit and share. Operator can also help you [build reports and dashboards](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities#build-reports-and-dashboards) from a natural-language brief.

## What to expect

Operator Analyze pulls answers from your workspace data, so allow a few minutes per question. Operator shows progress while it runs.

Your answer appears in the Operator conversation—a chart, table, or written summary with insights.

Each question triggers a live query against your workspace data, and each one counts toward your company's daily Operator [usage limit](https://www.braze.com/docs/user_guide/brazeai/operator/capabilities#limitations). When you want several reads for the same period, include them in one question—for example, a benchmark comparison and a trend together rather than as separate prompts.

## Example questions

Describe what you want to know, and let Operator take it from there. Select a tab for sample prompts.




Compare your channel performance against industry benchmarks. To see which channels and metrics include benchmarks, see [Supported channels and metrics](#supported-channels-and-metrics).

- "How does our email *Open Rate* compare to industry benchmarks for the last 30 days?"
- "Are we higher or lower than the benchmark for SMS *Delivery Rate* this quarter?"
- "Where are we underperforming the industry across our channel mix?"




See how your channels are performing at a glance.

- "Which channels are performing best for us in FY26 to date?"
- "Break down engagement by channel for the last 90 days."
- "How much *Attributed Revenue* did each marketing channel drive last quarter?"




Rank individual campaigns and Canvases by engagement or revenue.

- "What are our top 10 email campaigns by *Click-Through Rate* this fiscal quarter?"
- "Which Canvases drove the most *Clicks* last month?"
- "Which campaigns generated the most *Attributed Revenue* in FY26 Q1?"
- "Show our worst-performing push campaigns over the last 30 days."




Track how metrics change over time.

- "What's the month-over-month trend in push engagement for FY26?"
- "How has email *Click-Through Rate* changed quarter-over-quarter over the last year?"
- "How has our *Attributed Revenue* trended over the last 12 months?"
- "Show me our weekly engagement trend for in-app messages over the last 90 days."




Ask about *Attributed Revenue* and *Conversions* at the campaign, Canvas, channel, or program level.

- "Compare *Attributed Revenue* and *Conversions* for the most recent quarter against the prior quarter."
- "Which campaigns drove the most *Attributed Revenue* in the last 90 days?"
- "Break down *Attributed Revenue* by channel for FY26 to date."




Get a broad read on your engagement program with recommendations.

- "Give me a full review of our engagement program with recommendations."
- "Where are our biggest opportunities and risks across channels right now?"




## Charts and tables

When the data supports it, Operator adds a chart or table to its response. Line charts work well for trends over time, bar charts for comparing categories, and tables for everything else.

When a response includes multiple metrics, Operator prioritizes engagement rates (*Open Rate*, *Click Rate*, *Push Open Rate*) over raw counts.

## Supported channels and metrics

You can ask about *Attributed Revenue* and *Conversions* at the campaign, Canvas, channel, or program level. See the **Revenue and conversions** tab under [Example questions](#example-questions) for sample prompts.

| Channel | Metrics | Industry benchmarks |
| --- | --- | --- |
| Email | Sends, Deliveries, Unique Opens, Unique Clicks, Unsubscribes | Yes |
| Push (iOS, Android, Web) | Sends, Deliveries, Opens | Yes |
| SMS | Sends, Deliveries, Link Clicks | Delivery Rate only |
| In-app messages | Impressions, Clicks | Yes |
| Content Cards | Sends, Impressions, Clicks | Yes |
| WhatsApp | Sends, Deliveries, Reads, Clicks | No |
| RCS | Sends, Deliveries, Reads, Clicks (including text URL, button, action, reply action, and reply button sub-types) | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Supported channels, metrics, and benchmark availability" }


**Tip:**


Operator uses unique counts for rates (for example, *Unique Opens* divided by *Deliveries* for *Email Open Rate*). If a figure differs from a dashboard, compare attribution window, time range, and definition. Operator lists all three in each response.



## Time periods and attribution windows

### Fiscal and calendar year defaults

By default, Operator interprets time periods using the Braze fiscal year (February 1 through January 31).

| Fiscal quarter | Months |
| --- | --- |
| FQ1 | Feb – Apr |
| FQ2 | May – Jul |
| FQ3 | Aug – Oct |
| FQ4 | Nov – Jan |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze fiscal quarters and calendar months" }


For calendar-year questions, include "CY", "calendar year", or "standard year" in your prompt. If you say "last year" without specifying, Operator asks which calendar you mean.

You can also name explicit ranges, such as `Q4 2025` or `2025-03-01 to 2025-05-31`.

### Attribution windows

The default attribution window is 7 days. Name a window in your question to change it:

- **1-day** for quick engagement checks
- **3-day** for short-cycle campaigns
- **7-day** for general overviews and campaign reads (default)
- **30-day** for strategic or long-range views
- **All windows** for a 1-day / 3-day / 7-day / 30-day side-by-side comparison

### Channel cutoffs

Each channel has a maximum attribution period. A channel only contributes to windows at or before its cutoff:

| Channel | Cutoff |
| --- | --- |
| In-app messages, Content Cards | 3 days |
| Push, SMS, RCS, WhatsApp | 7 days |
| Email | 30 days |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Channel attribution cutoffs" }

The wider the window, the fewer channels are included in the count:

- **1-day and 3-day:** All channels
- **7-day:** Push, SMS, RCS, WhatsApp, and Email — in-app messages and Content Cards have passed their cutoff
- **30-day:** Email only

## Data freshness

Data refreshes daily. Same-day activity appears after the next refresh. Each response states the latest date in the dataset. If that date looks stale, contact your customer success manager.

## Limitations

Operator Analyze has boundaries.

- **Product-level breakdowns:** *Attributed Revenue* and engagement roll up to the campaign, Canvas, channel, or program level. Product- or SKU-level breakdowns aren't supported. Reach out to your customer success manager if you need product-level analysis.
- **Industry benchmarks:** Benchmarks are available for email, push, in-app messages, Content Cards, and SMS *Delivery Rate*. Benchmarks aren't available yet for WhatsApp, RCS, or other SMS metrics.
- **Per-user and per-send lookups:** Results are aggregated. Operator can't look up activity for a specific user or message. For individual user activity, use user profiles or the **Message Activity Log**.
- **Opt-in and subscription state:** Operator Analyze reports messaging engagement (sends, deliveries, opens, clicks), not current opt-in or consent status. For subscription state, use your audience or user profile views.

When a question falls outside these boundaries, Operator tells you directly and suggests an alternative where one exists.

## Best practices

Specific prompts get clearer answers. Keep these in mind when you ask about performance:

- **Name the time range and metric:** Include the period you mean ("FY26 Q2", "the last 90 days", "calendar year 2025") and the rate or outcome you care about (*Open Rate*, *Click-Through Rate*, *Attributed Revenue*).
- **Use follow-ups to refine the read:** Drill into a result, change the attribution window, or switch channels. Operator keeps context across the conversation.

## Data privacy and security

Operator Analyze follows the same privacy and security model as BrazeAI OperatorTM. For more information, see [Data privacy and security](https://www.braze.com/docs/user_guide/brazeai/operator/data_privacy_security).

## Next steps

<ul class="guide_tiles"><li><a href="/docs/user_guide/brazeai/operator"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">BrazeAI Operator</span><span class="guide_tile_description">Access Operator and explore its dashboard capabilities.</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/operator/reviewing_actions"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Review actions</span><span class="guide_tile_description">Review and approve Operator&#39;s proposed changes.</span></span></div></a></li></ul>

