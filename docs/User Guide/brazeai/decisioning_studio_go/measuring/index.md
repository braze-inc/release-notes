# Compare Decisioning Studio Go against your business-as-usual program

> This page explains how to compare your agent against your current business-as-usual (BAU) program. The built-in comparison, the **AI-Driven** group against the **Random** group, needs no setup. For how to read it, see [Reporting for Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/reporting).

The **Random** group shows what the agent's decisions add compared with random choices from the same options. A BAU comparison answers a different question: whether the agent beats the program you run today. Decisioning Studio Go does not orchestrate or report on the BAU group, so you assemble this comparison yourself.

## Step 1: Split your audience into a BAU group and an agent group

You can use either of these methods:

- Use an [Experiment Paths step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step) in a Canvas (recommended) to route users down a BAU path or into the agent's segment. A Canvas Experiment Paths step is a clean, random split and is the recommended way to set up a fair test. See [Use Decisioning Studio Go with Canvas](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/composing_with_canvas).
- Use [random bucket numbers](https://www.braze.com/docs/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) outside a Canvas to carve out a BAU group and an agent group from the same audience.

## Step 2: Check your audience is large enough to split

The agent group must contain at least 20,000 users after the split and after allocating its random control. If your total audience is about 40,000 users or smaller, a 50/50 BAU split leaves each half under that minimum. For smaller but still-eligible audiences, reserve a smaller BAU portion, or rely on the built-in random control instead of a BAU comparison. For how to size the random control, see [Set up your Decisioning Studio Go agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup#choose-your-control-group-size).

## Step 3: Make the test fair

A BAU comparison is only meaningful if the two groups differ in who makes the decisions. Before you launch:

- Keep send behavior equal. Match the agent's send frequency to your BAU frequency, or set it to the BAU average. If one group sends more often than the other, you measure send volume instead of decisioning.
- Load the BAU creatives into the agent. Every subject line, call to action (CTA), and image must be available to both the BAU group and the agent. A difference then reflects the decisions, because both groups have the same content available.
- Align how you count a click across both groups, so you're comparing like with like.
- Hold the BAU steady over the measurement window. Don't re-optimize it during the test.

## Step 4: Wait for a fair read

A still-training agent usually trails a mature, already-optimized BAU program early. That gap is expected. Wait until the agent is **Fully trained** before comparing. For more information, see [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch).

## Read the results

Your BAU group sends outside the agent, so it doesn't appear in agent reporting and its sends don't carry the agent identifiers. To compare the two groups, use the reporting pages and your own data:

- **Agent's engagement against your BAU program:** Use the **Email Performance** table on the **Performance** tab, which uses the same counting as Campaign Analytics, and compare it with your BAU campaign or Canvas stats. Don't compare the agent learning signal with your BAU click rate because they count clicks differently. For more information, see [Email performance](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/reporting#email-performance).
- **Whether personalization is working:** Use **Uplift** against **Random** on the **Performance** tab. For more information, see [Agent learning signal](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/reporting#agent-learning-signal).
- **Analysis in your own warehouse:** Start from the agent identifiers on the email send event, and use your BAU campaign or Canvas identifiers to separate the BAU group. For the fields and join steps, see [Agent events in your warehouse](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/reporting#agent-events-in-your-warehouse).

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/reporting"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Reporting for Decisioning Studio Go</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/after_launch"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">What to expect after launch</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/composing_with_canvas"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Use Decisioning Studio Go with Canvas</span></span></div></a></li></ul>
