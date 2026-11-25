# Reporting for Decisioning Studio Go

> This page explains what you see in your decisioning agent's reporting: the email performance metrics, the learning signal, the decisioning agent preferences view, and the decisioning agent identifiers written to your send events.

On the **Performance** tab, **Email Performance** shows standard email metrics, the same metrics as Campaign Analytics. **Agent learning signal** shows *Unique customers who clicked per day* for the **AI-Driven** and **Random** groups.

Because these two metrics count clicks differently, a difference between them is expected. For more information, see [Why the learning signal reads lower than your click rate](#why-the-learning-signal-reads-lower-than-your-click-rate).

## Agent status

The top of the **Performance** tab shows your decisioning agent's current stage, so you know what to expect before and after the first send. Read the decisioning agent's learning signal alongside this stage. The results are not ready for you to judge until the decisioning agent is **Fully trained**. For what happens at each stage, see [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch).

To change audience, schedule, creatives, or constraints, go to the **Configuration** tab. For more information, see [Set up your Decisioning Studio Go agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup#edit-an-active-agent).

## Email performance

The **Email Performance** table shows the standard Braze email metrics for everything your decisioning agent has sent. Use it to confirm your decisioning agent is sending and to compare its engagement with your other email programs, using metrics you already know.

**Note:**


Earlier versions of decisioning agent reporting showed sends, opens, unsubscribes, and other email stats calculated by Decisioning Studio. Those stats have been replaced by the **Email Performance** table, which uses the same metrics as Campaign Analytics.



The table uses the same metrics and formatting as Campaign Analytics, and you can add or remove columns. For what each metric means, see [Campaign Analytics](https://www.braze.com/docs/user_guide/analytics/reporting/campaign_analytics). The date range includes today, so this table is the quickest way to check whether your decisioning agent sent this morning.

### Choose a date range

By default, the table covers your decisioning agent's launch date through today. Use the date range picker to choose a custom range, or select a preset for the last 7, 14, 30, or 90 days.

## Agent learning signal

The **Agent learning signal** section on the **Performance** tab shows the metric your decisioning agent learns from and optimizes for: *Unique customers who clicked per day*.

### What it means

*Unique customers who clicked per day* is the share of your decisioning agent's audience that clicked at least one email on a given day. For each day, the decisioning agent counts:

- Who clicked: each person counts once per day, however many times they clicked.
- Which clicks count: only genuine clicks. Before a click counts, it passes validation filters that remove automated activity, such as link scanners and bots, and clicks related to unsubscribing.
- What the rate divides by: everyone in the group's audience that day, whether or not the decisioning agent emailed them that day.

### Compare groups and read uplift

**Comparison groups** compares your decisioning agent's two groups: **AI-Driven**, which receives the decisioning agent's personalized choices, and **Random**, which receives randomly chosen combinations of the same options.

The headline shows the **AI-Driven** group's rate. Next to it, a comparison shows that rate against the other group, such as versus **Random**. **Uplift** is the relative change between the two rates. For example, if the **AI-Driven** group's rate is 3.0% and the **Random** group's rate is 2.5%, **Uplift** is 20% (0.5 ÷ 2.5).

Because both groups go through the same filters and are measured the same way, **Uplift** against **Random** shows what the decisioning agent's decisions add compared with random choices.

### Aggregate results

The **Aggregate results** table breaks down each group's rate for the date range you selected:

| Column | What it shows |
| --- | --- |
| **Group** | The group, such as **AI-Driven** or **Random**. |
| **Conversion** | The average number of customers in the group who clicked at least one email per day over the selected period. In this table, a conversion is a customer who clicked that day. |
| **Customer** | The average number of customers in the group's audience per day over the selected period. |
| **Conversion per customer** | Conversion divided by Customer. This is the group's learning signal, the same rate shown in the headline. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aggregate results columns" }

#### Why Conversion and Customer show decimals

**Conversion** and **Customer** are averages per day over the date range you selected, so they can be fractions:

- **Conversion** is the average number of unique customers who clicked per day.
- **Customer** is the average number of customers in the group's audience per day.

For example, say the same 15 customers are in the audience every day for three days, and 3, 5, and 2 of them click on those days:

- **Customer** is 15, because the audience didn't change.
- **Conversion** is (3 + 5 + 2) ÷ 3 = 3.33, the average number of customers who clicked per day.
- **Conversion per customer** is 3.33 ÷ 15 = 22.2%.

**Customer** shows decimals too when your audience size changes from day to day, as people enter and leave the segment. Averaging both numbers per day keeps the rate comparable when that happens.

### Trends over time

Two charts show how the learning signal changes over time:

- **Unique customers who clicked per day** plots each group's daily rate.
- **Uplift** plots the change between the groups.

Use **Aggregation** to choose how each chart groups the data. **Daily** shows each day on its own, which can vary a lot from day to day. A rolling window, such as **7 days rolling**, averages each point over the previous days so the trend is easier to see.

Dashed vertical lines on both charts mark **First sends** and **Agent started personalizing**. Results before **Agent started personalizing** are from while the decisioning agent is exploring, so use that line as your starting point when you read the trend.

Expect **Uplift** to swing widely early on, positive and negative. While the decisioning agent is in training, it's deliberately exploring and the daily numbers are small, so don't treat early swings as a final result. Read the **Uplift** trend after the agent is **Fully trained**. For more information, see [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch).

### The most recent days are incomplete

Click data takes about two days to fully arrive and be counted. Until it does, the most recent days include fewer clicks than the days that have finished processing, so the learning signal and **Uplift** usually dip for those days. Don't read the last two days as a drop in performance. For a complete view, set your end date to two days before today.

Right after launch, the learning signal can take a few days to populate. This is expected and doesn't mean anything is broken.

### Why the learning signal reads lower than your click rate

Expect the learning signal to be much lower than the click rate in the **Email Performance** table. Three things cause the gap, and the biggest one is what each rate divides by:

| | Unique click rate (email performance) | Learning signal |
| --- | --- | --- |
| Clicks counted | All unique clicks, including automated clicks | Genuine clicks only |
| A person counts | Once per email | Once per day |
| Divided by | Emails delivered | Everyone in the audience that day |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Why the learning signal differs from unique click rate" }

For example, say your decisioning agent's audience is 100,000 people. On a given day, the decisioning agent emails 40,000 of them and 300 people make a genuine click. Measured against the people emailed, that is 0.75%. Measured against the whole audience, which is what the learning signal does, it is 0.3%. Both rates use those 300 clicks. The learning signal divides by the whole audience. Filtering out automated clicks lowers the number further, and dividing by the whole audience accounts for most of the difference.

**Note:**


Don't compare the learning signal directly with the click rate of your other campaigns. To compare the decisioning agent's email engagement with your other programs, use the **Email Performance** table. To judge whether personalization is working, use **Uplift** against **Random**.



## Agent preferences

The **Agent preferences** tab shows how often your decisioning agent has chosen each of the options you gave it, such as base creatives, subject lines, calls to action (CTAs), and images. The tab uses the date range you select, and it opens on the **AI-Driven** group. Use **Assignment groups** to see another group, such as **Random**. Breakdowns for each subject line, CTA, and image show how those options perform across the combinations the decisioning agent sends.

Use this view to:

- Confirm the decisioning agent is using your full library. If some options are rarely chosen, the decisioning agent may consider them a poor fit for most recipients, or they may be too similar to other options for the decisioning agent to tell apart. For more information, see [Creative setup and management](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/creative_setup).
- Plan your next creatives. Patterns in what the decisioning agent favors can inform what you write next.
- Watch how preferences change. Preferences shift as the decisioning agent learns and as your audience changes.

Keep in mind that the decisioning agent chooses for each person, not for the whole audience. An option the decisioning agent picks less often can still be the right choice for a smaller group of recipients, so don't retire an option based only on how often the decisioning agent chooses it. During training, the decisioning agent deliberately tries a wide range of options, so expect choices to be spread out before the decisioning agent is **Fully trained**.

**Important:**


Deactivating or removing a base creative drops that creative's past sends and clicks from this view. Avoid retiring creatives during an active test. For more information, see [Historical numbers changed after I edited creatives](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/troubleshooting#historical-numbers-changed-after-i-edited-creatives).



## Agent events in your warehouse

Your decisioning agent sends through the standard Braze email pipeline, so its emails produce the same email events as any other campaign: sends, deliveries, opens, clicks, unsubscribes, and so on. To distinguish decisioning agent sends from your other emails, each decisioning agent send carries identifiers on the send event.

### The decisioning agent identifiers

Each send writes these fields to `message_extras` on the `users.messages.email.Send` event. They're written automatically in every workspace, so there's nothing to turn on.

| Field | What it is | Use it to |
| --- | --- | --- |
| `ds_go_agent_id` | Which decisioning agent sent the message | Filter to one decisioning agent's sends |
| `ds_go_regime` | Which group the recipient is in: `offerfit` is **AI-Driven**, `control` is **Random**, and `bau` is **business-as-usual (BAU)** | Compare groups |
| `offerfit_rec_id` | The ID of the specific decision (recommendation) | Trace an individual decision |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Agent identifiers on the email send event" }

### How decisioning agent events relate to the send event

The decisioning agent identifiers are only on the send event. Opens, clicks, and other engagement events don't carry them. To analyze engagement by decisioning agent or by group, start from the send event and join your engagement events to it.

1. Confirm your [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) or data export includes `message_extras` on the email send event.
2. Filter send events to your decisioning agent using `ds_go_agent_id`.
3. Join opens, clicks, or other email events to those sends on `user_id` and [`dispatch_id`](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/dispatch_id).
4. Group the results by `ds_go_regime` to compare `offerfit` (**AI-Driven**) with `control` (**Random**). A business-as-usual program you run outside the decisioning agent does not carry these fields. For how to compare that program, see [Compare Decisioning Studio Go against your business-as-usual program](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring).

**Note:**


To match the numbers you calculate in your warehouse with the learning signal, count only genuine clicks, count each person once per day, average the results per day, and divide by the whole audience. Unique click rates calculated from raw click events are closer to the **Email Performance** table.



## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/after_launch"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">What to expect after launch</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/measuring"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Compare against your BAU program</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/troubleshooting"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Troubleshooting Decisioning Studio Go</span></span></div></a></li></ul>
