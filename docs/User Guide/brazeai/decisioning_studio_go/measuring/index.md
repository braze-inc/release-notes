# Measuring Decisioning Studio Go

> This guide covers how to measure your agent's impact—using the built-in random control, and by comparing against your current business-as-usual (BAU) program.

Decisioning Studio Go gives you one comparison by default: the agent compared with a random control. You can set up a second comparison yourself: the agent compared with your current program. This guide covers both, plus how to read the numbers and pull the data into your own warehouse.

## The built-in comparison: agent versus random control

Every agent automatically splits its audience into two groups:

- The Decisioning Studio group receives AI-optimized content.
- The random control group receives randomly chosen combinations of the same options you configured, within the same schedule and constraints.

Because both groups draw from the same options and the same schedule, the difference between them isolates the effect of the agent's decision-making. This is your cleanest, always-available measure of lift. There is nothing extra to set up.

### The lift metric

The headline metric is *Unique Customers Who Clicked Daily*: the number of distinct users who click, not raw click volume. Lift is the difference between the Decisioning Studio group and the random control on this measure.

The agent learns only from genuine clicks. Before a click counts, it passes validation filters that screen out automated activity and opt-out-related clicks. This makes Decisioning Studio click totals lower than your raw email reports. The same filtering applies to both groups equally, so the comparison between them stays valid.

### Size the control group

The minimum control size is 5%. Scale it to your audience. Smaller audiences need a proportionally larger control to stay statistically meaningful:

| Audience size | Recommended split (Decisioning Studio / random control) |
| --- | --- |
| 20,000 – 100,000 | 80 / 20 |
| 100,000 – 1,000,000 | 90 / 10 |
| 1,000,000 – 40,000,000 | 95 / 5 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sizing the control group" }

## Compare against your business-as-usual program

The random control measures the agent against randomly chosen combinations of the same options. To measure the agent against your current program, set up a BAU comparison yourself. Decisioning Studio Go does not orchestrate or report on the BAU group—you assemble this comparison.

### Step 1: Split your audience into a BAU group and an agent group

You can use either of these methods:

- Use an [Experiment Paths step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step) in a Canvas (recommended) to route users down a BAU path or into the agent's segment. A Canvas Experiment Paths step is a clean, random split and is the recommended way to set up a fair test. See [Use Decisioning Studio Go with Canvas](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/composing_with_canvas).
- Use [random bucket numbers](https://www.braze.com/docs/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) outside a Canvas to carve out a BAU group and an agent group from the same audience.

### Step 2: Check your audience is large enough to split

The agent group must contain at least 20,000 users after the split and after allocating its random control. If your total audience is about 40,000 users or smaller, a 50/50 BAU split leaves each half under that minimum. For smaller but still-eligible audiences, reserve a smaller BAU portion, or rely on the built-in random control instead of a BAU comparison.

### Step 3: Make the test fair

A BAU comparison is only meaningful if the two groups differ in who makes the decisions. Before you launch:

- Keep send behavior equal. Match the agent's send frequency to your BAU frequency, or set it to the BAU average. If one group sends more often than the other, you measure send volume instead of decisioning.
- Load the BAU creatives into the agent. Every subject line, call to action (CTA), and image must be available to both the BAU group and the agent. A difference then reflects the decisions, because both groups have the same content available.
- Align how you count a click across both groups, so you're comparing like with like.
- Hold the BAU steady over the measurement window. Don't re-optimize it during the test.

### Step 4: Wait for a fair read

A still-training agent usually trails a mature, already-optimized BAU program early. That gap is expected. Wait until the agent is **Fully trained** before comparing. For more information, see [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch).

## Analyze results in your own warehouse

Each send writes identifiers to `message_extras` on the `users.messages.email.Send` event. These are written automatically in every workspace:

| Field | What it is |
| --- | --- |
| `ds_go_agent_id` | Which agent sent the message |
| `ds_go_agent_regime` | Which group the user is in—AI-driven or random control |
| `ds_go_rec_id` | The ID of the specific decision (recommendation) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analyzing results in your own warehouse" }

To analyze these fields in your warehouse:

1. Confirm your [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) or data export includes `message_extras` on the send event.
2. Join the send event, which carries the group tag, to opens and clicks on `user_id` and [`dispatch_id`](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/dispatch_id).
3. Compare your metric of choice across `ds_go_agent_regime` values, and across your BAU and agent split if you set one up.

## How to read the reporting

- Set the end date to two days ago. Reporting data lags by about a day, so an end date of two days ago gives you a complete view.
- Give reporting a few days to populate after launch. If it looks empty immediately after you launch, that's expected. Reporting is still collecting data.
- Use the **Performance** and **Agent preferences** views. **Performance** shows lift compared with the random control. **Agent preferences** shows how often the agent has chosen each variant.
