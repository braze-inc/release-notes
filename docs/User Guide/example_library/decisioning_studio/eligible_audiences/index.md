# Identify eligible audiences and experiment cohorts

> Decisioning Studio Pro uses segments for two jobs: who is eligible for the scenario, and which experiment cohort each consumer belongs to. This example covers the six segments a typical Braze scenario configures, and who builds each one.

For how a decision becomes a message, see [Get started with Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/get_started#message-activation-flow).

## How it works

Segments define two things in a Decisioning Studio scenario:

- **Eligible audience:** The master segment holds marketing-opted-in consumers who may become eligible for the scenario. Decisioning Studio downloads profile and engagement data for consumers in this segment. The base segment holds the consumers eligible for this one scenario.
- **Experiment cohorts:** Smaller segments decide which treatment a consumer receives: an AI decision, a random comparison, business as usual (BAU), or a holdout. Each consumer is randomly assigned to one cohort.

A standard Decisioning Studio Pro scenario in Braze uses these segments:

| Segment | Description | When to use |
| --- | --- | --- |
| Master segment | Holds marketing-opted-in consumers who may become eligible for the scenario. If you run more than one scenario, the master segment can include consumers who are eligible for at least one of them. | Download profile and engagement data for the consumers Decisioning Studio can consider. |
| Base segment with scenario filters | Holds consumers eligible for this one scenario. | Suppress sends in real time, so messages stay with consumers who are still eligible after the last Decisioning Studio data sync. |
| AI cohort | The subset that receives AI-personalized selections. | Measure the incremental impact of Decisioning Studio on your key metrics. |
| Business-as-usual cohort | The subset that receives your current campaign selections. | Set the baseline for your existing strategy. |
| Random control | The subset that receives a random action from the action bank. | Set the baseline for automated, always-on messaging. |
| Holdout | The subset that receives no messages from this scenario. | Set the baseline for organic performance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Scenario segments" }

## Roles and responsibilities

Your team builds the segments in the Braze dashboard. The AI Decisioning Services team configures randomization in the Decisioning Studio pipeline and advises on the filters.

| Task | Owner | Where |
| --- | --- | --- |
| Build each segment | Your team | Braze dashboard |
| Choose which eligibility filters belong on each segment | AI Decisioning Services team, with your team | Scenario design |
| Randomly assign consumers to an experiment cohort, including the method and the size of each cohort | AI Decisioning Services team, agreed with your team during design | Decisioning Studio pipeline |
| Apply the cohort segments on campaigns and Canvases so each cohort gets the right messages | Your team, with guidance from the AI Decisioning Services team | Braze dashboard |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Segment ownership" }

## Prerequisites

- The target audience is defined, the profile filters are known, and the data is available in Braze.
- Your team and the AI Decisioning Services team agree on how consumers are randomly assigned to the AI, business-as-usual, random control, and holdout segments.

## Build the segment for inbound data

### Step 1: Create the master segment

Build one segment of marketing-opted-in consumers who may become eligible for the scenario.

A clear name is "Decisioning Studio — Master". If you run more than one scenario, include consumers who are eligible for at least one of them. An example filter is "The consumer is opted in to a channel the scenario can send."

This segment supplies profile data and historical engagement to Decisioning Studio. For the dashboard steps, see [Create a segment](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment).

**Important:**


Consumers outside of this master segment are left out of recommendations and reporting. Decisioning Studio downloads profile and engagement data only for consumers in this segment.



Keep engagement-based eligibility out of this master segment. If eligibility depends on recent behavior, such as no purchase in the last 30 days, the AI Decisioning Services team sets that rule in the Decisioning Studio pipeline. Engagement status changes daily. A consumer who makes a purchase needs to remain in the data feed long enough for that conversion to appear in reporting.

## Build segments for suppression and reporting

Your team creates these segments in Braze. The AI Decisioning Services team advises on randomization and segment size.

Create the base segment with this scenario's eligibility filters. For example, country is United States, Canada, or United Kingdom. Use it to suppress sends in real time, so messages stay with consumers who are still eligible after the last Decisioning Studio data sync.

| Segment | Who is in it | What it is for | Messages received |
| --- | --- | --- | --- |
| Base segment with eligibility filters | A daily view of everyone eligible for the scenario, including engagement-based filters | Suppress this audience from agreed sends outside the scenario, such as a flash sale, and suppress consumers who became ineligible after the last daily extract | None by itself. This segment is a suppression list. |
| AI | Eligible consumers randomly assigned to the AI cohort | Limit Decisioning Studio sends to the AI and random cohorts, and identify the AI cohort in reporting | Messages chosen by Decisioning Studio |
| Random | Eligible consumers randomly assigned to random control | Limit Decisioning Studio sends to the AI and random cohorts, and identify the random cohort in reporting | A random action from the action bank |
| Business as usual | Eligible consumers randomly assigned to the business-as-usual cohort | Limit business-as-usual sends to that cohort, and identify it in reporting | Messages from your business-as-usual campaigns or Canvases |
| Holdout | Eligible consumers randomly assigned to the holdout | Suppress holdout consumers from the scenario's campaigns, and identify them in reporting | No messages from this scenario |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Suppression and reporting segments" }

**Note:**


Cohort split percentages vary by scenario and by deployment phase. Launches often start with a small AI and random share next to a large business-as-usual group. Single-digit percentages are common at launch, then grow as confidence grows. Agree on the splits with your AI Decisioning Services team.



### Step 2: Apply cohort segments to campaigns and Canvases

During design, agree which messages apply to which cohort:

- The AI cohort receives AI-personalized decisions from the API-triggered Canvas or campaigns.
- The random cohort receives a random action from the action bank through those same sends.
- The business-as-usual cohort receives messages based on your current rules, from your business-as-usual Canvases or campaigns.
- The holdout cohort is excluded from the scenario's campaigns.

Add the matching segment to each in-scope campaign or Canvas so each consumer receives messages only from the sends for their cohort.

For the treatment-group overview, including other customer engagement platforms, see [Define your audience](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/audience).

## Best practices

- Build each experiment cohort from the base segment plus the cohort assignment. When the audience definition changes, update the base segment with the eligibility filters, and the cohorts follow.
- Agree during design which campaigns outside the scenario each cohort should receive. For reporting to stay comparable, a message outside the scenario goes to every cohort or to none of them.
- Use a holdout that belongs to this scenario. A [global control group](https://www.braze.com/docs/user_guide/audience/global_control_group) measures the audience with no messages at all. The scenario holdout measures the audience with no messages from this scenario. Compare this scenario's cohorts with each other.

## Frequently asked questions

### What if I leave out a cohort?

Each cohort measures a different baseline, which is how you read incremental performance and investigate issues. The AI Decisioning Services team works with you to size each cohort so it can do that job while keeping as much of the audience as possible on AI-optimized decisions.

### What if my base segment is small?

Small segments produce noisier results. Broaden eligibility, such as a longer lookback or fewer geographic filters, and confirm a workable audience size with your AI Decisioning Services team.

### Can one cohort serve more than one scenario?

Give each scenario its own cohort, assigned randomly and on its own. Sharing a cohort mixes models and makes the measurement hard to interpret.
