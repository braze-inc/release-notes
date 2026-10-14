# Frequently asked questions

## General

### What is Decisioning Studio Go?

Decisioning Studio Go is an AI decisioning agent built into the Braze dashboard. You curate a menu of options (creative variants, send timing, days of the week) and the agent picks the right combination for each individual user, optimizing for clicks. It delivers one-to-one personalization without requiring a data scientist or a custom integration.

### How is Decisioning Studio Go different from A/B testing?

A/B testing finds the variant that performs best on average across an entire audience or within a segment, and rolls that one variant out to everyone in that group.

Decisioning Studio Go picks the best variant for each individual user, based on what that user has engaged with before. Different users can receive different variants on the same send. Instead of rolling out one winning variant to a group, Decisioning Studio Go personalizes content at the individual level.

### How is Decisioning Studio Go different from Decisioning Studio Pro?

Go is the self-serve tier. It's the right starting point for marketers who want one-to-one email personalization without a heavy implementation lift. It optimizes for clicks and works with options you configure directly inside Braze.

Pro is the full-service tier. It optimizes for any business metric, connects to any first-party data source, supports multiple channels, and comes with dedicated support from the Braze AI Decisioning Services team.

### What kind of AI does Decisioning Studio Go use? Is it generative?

No. The agent that decides what to send each user is a decisioning agent. It doesn't write content for you. You provide the options, and the agent learns which option works best for each individual user.

Decisioning Studio Go is built on reinforcement learning. The agent treats each send as an opportunity to learn: it tries combinations of the options you've approved, observes whether each user engages, and updates its understanding of what works for whom. Over time, it becomes increasingly accurate at matching each individual user with the option from your menu most likely to drive a click.

### What data does the agent learn from?

The agent learns from three things, all within Braze:

- **Your audience:** The users in the segment attached to the agent
- **That audience's email engagement:** How people respond to what the agent sends
- **Its own understanding of your content:** When you add creatives, the agent builds its own representation of each one and uses it to reason about which content suits which users

The agent does not learn from custom data such as custom attributes or warehouse data. If you want decisioning that draws on your first-party data or optimizes a custom business metric, use Decisioning Studio Pro.

## Audiences and control groups

### What's the difference between the Decisioning Studio group and the random control group?

The Decisioning Studio group receives AI-optimized email content. The agent picks the best variant for each user. The random control group receives randomly chosen combinations of the same options you configured, with no optimization.

Both groups respect the constraints you've configured (for example, if you've said not to repeat a subject line within 15 days, that rule applies to the random control as well). Comparing the two groups gives you a clean measure of the agent's lift.

### Is the random control a holdout group of users who receive no email?

No. Random control users still receive emails. They receive randomly chosen combinations of the options you configured, on allowed days within your schedule. This comparison is AI-personalized email against the same content chosen randomly.

### Why is the random control required, and how big should it be?

Two reasons. First, it gives you ongoing, real-time measurement of how much the agent is outperforming a random baseline. Second, the agent uses the random control's behavior as part of its learning signal.

The minimum random control size is 5%. We recommend scaling the split to your audience size: a larger audience can measure lift reliably with a smaller control group, while a smaller audience needs a proportionally larger one.

| Audience size | Recommended split (Decisioning Studio / random control) |
| --- | --- |
| 20,000 – 100,000 | 80 / 20 |
| 100,000 – 1,000,000 | 90 / 10 |
| 1,000,000 – 40,000,000 | 95 / 5 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Audience sizes and recommended splits" }

### Can I use a segment that's already used in another Canvas or campaign?

You can, but it's strongly discouraged and a warning appears. When the same users receive messages from Decisioning Studio Go and from other Canvases or campaigns at the same time, the other messages affect engagement in ways the agent can't account for. The cleanest setup is a segment dedicated to the agent.

## Configuration

### What can I personalize?

Within each base creative, you can mark the subject line, the call to action (CTA), and an image as personalization points using Liquid tags. The agent then chooses among the variants you provide for each component, per user. You can also have multiple base creatives; the agent picks which base creative to use as well.

### Can I use Content Blocks, catalog references, or Liquid in my creatives?

Yes. The agent evaluates each creative's fully resolved content. Liquid, catalog references, and Content Blocks are all expanded before the agent builds its understanding, so dynamic and assembled content is part of what it learns from.

The one exception is [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content): emails that use it render and send normally, but the agent doesn't see or learn from what Connected Content returns. Don't rely on Connected Content as the thing that makes two creatives meaningfully different.

### Can I use image-based templates with no clickable elements?

Yes. For an image-only email, use one base creative and let the agent choose the image within it. You can also let the agent choose the subject line. Don't load each image variation as a separate base creative. An image-only email has no separate text CTA to optimize.

### Can I change the conversion event?

For the self-serve tier, the supported conversion event is clicks. In Decisioning Studio Pro, you can optimize for any custom business metric.

### How does send frequency work?

You select a single frequency, such as three sends per week. The agent doesn't decide between frequencies. Within that frequency, it chooses which days (from the days you allowed) and which times to send.

### How do frequency caps work?

During setup, you can apply your workspace's frequency capping rules to the agent and choose whether the agent's sends count toward each user's global frequency cap. Your customer success manager or solutions consultant can help you decide the right approach for your program based on how frequency caps are configured in your workspace.

### Do quiet hours guarantee that no email sends during that window?

Quiet hours limit the times the agent chooses for a send. They aren't a guaranteed send block. For a hard guarantee that no message goes out during a window, additionally set [workspace-level quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours).

### How does the agent handle audiences across many time zones?

Sends happen in each user's local time zone. The agent prioritizes delivering your message over sending it at the precise intended local time, so if your audience spans time zones far from your workspace, a message may occasionally arrive outside its intended day or time window. If most of your audience is in one region, keep that in mind when setting allowed days and quiet hours.

### Can the agent send across multiple channels?

Each agent is single-channel, and the current supported channel is email. You can run multiple agents in parallel for different programs, but each agent handles one channel.

## Testing and launch

### How do I test before going live?

Use the native test send feature in the Braze Composer. Test sends show specific variant combinations that you select—they're for proofing the email itself, not for predicting what the agent would actually send to a real user. The dynamic preview in the composer also lets you see how different variant combinations render.

### What happens after I launch?

The agent enters a training period, and reporting always shows which stage it's in:

| Stage | What's happening |
| --- | --- |
| **Launched, not yet sending** | Active, but the first send hasn't gone out. |
| **Waiting for signal** | Sending, but not enough genuine clicks yet to begin training. |
| **In training** | Enough signal to train; the agent explores combinations. Performance can look close to random here—this is expected. |
| **Partially trained** | Personalizing, but results aren't yet robust enough to read as final. |
| **Fully trained** | Fully trained; results are robust. This is the point to trust and report on lift. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What happens after I launch?" }

A new user receives their first send on the first day they enter the audience, and the agent begins personalizing for them the day after. Emails keep sending the whole time the agent learns—there's no waiting period.

For what to expect through each stage and how to read early results, see [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch).

### My agent looks flat, or like it's losing, in the first couple of weeks. Is something wrong?

Usually, no. Early on, the agent is still training, and it's typically being compared against a mature program that has already been optimized over a long period. That early gap is expected. Two things gate a trustworthy read: the agent needs enough genuine clicks to train, and it needs time to move into full personalization. Wait until the agent is **Fully trained** before judging results, and make sure the comparison is fair. For more information, see [Measuring Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring).

### Can I edit the agent after launch?

Yes. Audience, schedule, creatives, and constraints can all be updated post-launch, and both variants and dimensions can be changed. You must promote changes before they take effect. Adding a new variant doesn't reset the agent's training on existing variants.

**Note:**


Two audience changes trigger a reshuffle of users between the Decisioning Studio and random control groups: changing the control-versus-AI split proportion, and swapping the segment. Avoid making these casually mid-flight. Creative, schedule, and constraint edits don't reshuffle the audience.



### What if I update content options after launch?

You can add, remove, or change variants the same way you set them up originally. Changes need to be promoted before they take effect. Adding a new variant doesn't reset the agent's training on existing variants.

## Reporting and results

### What metric does the agent optimize for, and what does the lift number mean?

The agent optimizes *Unique Customers Who Clicked Daily*, the number of distinct users who click. Lift is the difference between the Decisioning Studio group and the random control on this measure.

### Does Decisioning Studio Go reporting match what I see in my email analytics elsewhere in Braze?

The numbers may differ. The agent learns only from genuine clicks, so before any click counts, it passes through independent validation filters that screen out automated activity and opt-out-related clicks. This makes Decisioning Studio click totals lower than raw email reports. The relative comparison between the Decisioning Studio group and the random control stays valid, because the same filtering is applied to each group equally.

### How do I compare Decisioning Studio Go against my business-as-usual (BAU) program?

The built-in comparison is always the agent compared with its random control. To compare against your existing BAU program, you set that up yourself by splitting the audience into a BAU group and a Decisioning Studio Go group. Two ways to do it:

- **In a Canvas:** use an [Experiment Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step) step to route users down a BAU path or into the agent's segment. This is the recommended approach.
- **Outside of a Canvas:** use [random bucket numbers](https://www.braze.com/docs/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) to carve out a BAU group and a Decisioning Studio Go group.

For a fair test, keep send behavior equal across groups (match the agent's frequency to BAU, or set it to the BAU average) and make sure the BAU creatives are also loaded as options in the agent. Remember that a still-training agent usually trails a mature BAU early. See [Measuring Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring) for the full walkthrough.

### How can I see which group a user was in, or analyze results in my warehouse?

Each send writes identifiers to `message_extras` on the `users.messages.email.Send` event: `ds_go_agent_id` (which agent), `ds_go_agent_regime` (AI-driven or random control), and `ds_go_rec_id` (the decision's ID). These are written automatically. To use them in your warehouse, confirm your export includes `message_extras` on the send event, then join to opens and clicks on `user_id` and `dispatch_id`.

### When is my reporting fully populated?

Reporting data lags by about a day, so set your reporting end date to two days before today for a complete view. Full reporting also takes a few days to populate after launch—if it looks empty right after you launch, give it a few days rather than assuming it's broken.

### Can I see which combinations are performing best?

Yes. The **Agent preferences** view shows how often the agent has chosen each variant, and element-level breakdowns show how individual subject lines, CTAs, and images perform across combinations.

### Who's accountable for the content the agent sends?

You are. The agent only sends content that you've added as a variant. The agent decides the combination for each user, but every individual element comes from the variants you provided.

## Support

### Where can I get help with my agent?

Contact your Braze customer success manager or solutions consultant for help with configuration, performance review, or program design.
