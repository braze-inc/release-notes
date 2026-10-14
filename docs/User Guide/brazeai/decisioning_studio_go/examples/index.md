# Examples for Decisioning Studio Go

> Decisioning Studio Go works best for recurring email programs where the agent has time to learn from engagement and where your content includes enough variant options for meaningful personalization. This page groups common email use cases by fit level, with examples and guidance for each.

For an overview of how Decisioning Studio Go works, see [BrazeAI Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go).

Each example in this guide is labeled with one of the following fit levels:

| Fit level | Description |
| --- | --- |
| **Best fit** | The agent has enough time to learn, your audience is stable enough to show lift, and personalization can meaningfully affect engagement. Start here. |
| **Supported** | The example can work well, but success depends on timing, audience size, or sequencing. Review the considerations before you commit. |
| **Not recommended** | The example conflicts with how the agent learns. Choose a different program type, or contact your customer success manager or solutions consultant about a different setup. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Examples for Decisioning Studio Go" }

Across all fit levels, the agent learns best when your audience generates enough engagement signal for the algorithm to detect patterns. We recommend a minimum audience of 20,000 users (the maximum is 40,000,000), with consistent weekly send volume. The agent can run on smaller audiences, but expect a longer learning period and less reliable lift. Your customer success manager or solutions consultant can help you confirm whether a given audience is sized appropriately.

## Run it always on

Decisioning Studio Go rewards programs that run continuously. Plan to run an agent for at least 30 days, and ideally keep it always on. The agent only starts delivering value once it has had time to learn, so the longer it runs, the more it pays off.

This also changes how to approach seasonal moments. Keep an always-on agent trained on your audience and swap in new creatives as the moment approaches.

- **Recommended:** Run an always-on repeat-purchase or lifecycle agent continuously. As Black Friday nears, swap the agent's creatives for your Black Friday content. The agent brings everything it has learned about your audience into the moment.
- **Not recommended:** Launch a new agent dedicated to a two-week Black Friday promotion. It doesn't finish training before the promotion ends.

## Best fit

### Always-on calendared campaigns

| Topic | Details |
| --- | --- |
| What it looks like | A marketing calendar that runs for several months or longer, with content swapped in and out over time—for example, a rewards-member calendar, a content drop schedule, or a lifestyle or inspiration calendar. |
| Why it fits | Long-running programs give the agent time to learn what works for different users. The audience is stable, content is refreshed regularly, and clicks are usually a meaningful indicator of engagement. |
| What to bring | Multiple base creatives or variant sets that you're comfortable rotating. The agent selects which version works for each user, but it needs enough variety in the options you provide. See [Creative setup and management](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/creative_setup) for how much variety, and how to structure it. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Always-on calendared campaigns" }

### Evergreen programs

| Topic | Details |
| --- | --- |
| What it looks like | Ongoing campaigns that aren't tied to specific dates or events—winbacks, re-engagement programs, dormant-account nudges, or milestone celebrations. |
| Why it fits | Like calendared campaigns, the audience is dynamic but the program runs indefinitely. The agent has time to learn, the content has flexibility, and clicks are a leading indicator the agent can optimize against. |
| What to bring | Variant options for subject line and call to action (CTA) that frame the message for different motivations. Image variants help if you have them. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Evergreen programs" }

## Supported use cases

### Multi-email promotions

| Topic | Details |
| --- | --- |
| What it looks like | A set of emails sent over several weeks under the same promotional theme—for example, a back-to-school series or a multi-week category promotion. |
| Why it works | If the promotion runs long enough—at least several weeks—the agent has runway to learn within the promotion. Click-through is usually a strong leading indicator of promotional engagement. |
| Considerations | The agent needs roughly 10 campaign days, days on which it actually sends, to develop strong recommendations. At a typical frequency of three sends per week, that's about three to four calendar weeks, which lines up with the 30-day minimum in [Run it always on](#run-it-always-on). For shorter promotions, consider whether an always-on evergreen program could carry the learning instead, so you can apply what you learn to the next promotion. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Multi-email promotions" }

### Action- or event-driven journeys

| Topic | Details |
| --- | --- |
| What it looks like | A single email or sequence triggered by a customer action—cart abandonment, browse abandonment, or post-purchase follow-up. |
| Why it works | Triggers create a clean entry point. If the journey is recurring and audience volume is consistent, the agent can learn which content works for which users. |
| Considerations | Timing matters. The agent decides once per day, so it isn't suited to emails that must go out within minutes of a trigger—confirm the send schedule fits with your customer success manager or solutions consultant. If users must receive emails in a specific order (Email 1 before Email 2), you need to orchestrate audience moves yourself—the agent doesn't sequence sends for a single user across a multi-email journey. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Action- or event-driven journeys" }

## Not recommended

### Drip sequences

| Topic | Details |
| --- | --- |
| What it looks like | A multi-email sequence—for example, an onboarding tutorial—where users must receive Email 1, then Email 2, then Email 3 in order. |
| Why it doesn't fit | The agent selects what to send each user based on what's likely to drive a click for that user. It doesn't model sequence requirements. If you need to enforce a specific order, you must orchestrate the audience yourself (moving users from segment to segment after each email), which reduces most of the benefit of using the agent. The agent also can't independently confirm that Email 1 succeeded before sending Email 2. |
| What to do instead | Use [Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas) to orchestrate the drip. If you want AI optimization within a drip, contact your customer success manager or solutions consultant about whether [Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/get_started) is a better fit. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Drip sequences" }

### One-time email blasts

| Topic | Details |
| --- | --- |
| What it looks like | A single email sent in one blast—a Black Friday announcement, a new product launch, or a one-off corporate communication. |
| Why it doesn't fit | The agent needs time to learn. A single send gives it no opportunity to improve decisions before the campaign ends. By the time it has enough engagement signal to make better choices, the program is over. |
| What to do instead | If you have an always-on program with similar content—for example, a year-round product-announcement program—use Decisioning Studio Go there and apply what you learn to one-time sends. For a one-time send, use [Optimize with BrazeAI™](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection) for A/B testing. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="One-time email blasts" }

## At a glance

| Scenario | Fit | Key consideration |
| --- | --- | --- |
| Always-on calendared campaigns | Best fit | Provide multiple base creatives or variant sets to refresh over time. |
| Evergreen programs (winbacks, re-engagement) | Best fit | Provide variant options that frame the same message for different motivations. |
| Multi-email promotions | Supported | Aim for at least 10 campaign days (about three to four calendar weeks) of runway; shorter promotions limit learning. |
| Action- or event-driven journeys | Supported | Confirm send-timing requirements; you are responsible for sequence enforcement. |
| Drip sequences (onboarding tutorials) | Not recommended | Use Canvas for sequencing; revisit Decisioning Studio Pro for in-drip optimization. |
| One-time email blasts | Not recommended | Use Optimize with BrazeAI™ for A/B testing instead. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="At a glance" }

## Next steps

Contact your Braze customer success manager if you're unsure whether your program is a fit. Strong signals include:

- The audience receives email regularly—at least weekly—over a window of a month or more.
- The audience is large enough to generate consistent engagement signal (at least 20,000 users is a useful starting target).
- You have at least two or three meaningful variant options to offer (subject lines, CTAs, or images that frame the message differently).
- Genuine clicks are a leading indicator of business value for this program.
- The segment isn't actively used by another Canvas or campaign that would compete for the same users' engagement.
