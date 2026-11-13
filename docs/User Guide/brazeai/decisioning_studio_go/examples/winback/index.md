# Set up a winback decisioning agent

> A winback decisioning agent learns which message brings each lapsed customer back. You provide it with two to five approaches, and it chooses the one most likely to earn a click from each person. It also chooses the send day and time within the schedule you set.

Winback is a strong first program for [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go). The program can run continuously, and a click from someone who has stopped engaging is a useful signal. For how this program compares with other email examples, see [Examples for Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/examples).

## Why winback is a strong first program

Most winback programs send one message to every lapsed customer. A winback decisioning agent tests several approaches at once and learns which one each person responds to.

- **You already have the audience:** A lapsed segment is common, and it often sits outside a complex Canvas.
- **The risk is low:** These lapsed customers have already stopped engaging, so trying a new message has little downside.
- **The winback decisioning agent tests ideas for you:** It learns which approach earns a click from each person.
- **A click is a meaningful step back:** Re-engagement is the first sign a lapsed customer is returning, so clicks are a natural goal.
- **One live winback decisioning agent teaches the product:** After the first program is running, the same setup applies to the next one.

## Check whether you're ready

Use this table before you build. Decisioning Studio Go can run on a smaller or quieter audience, but that audience may take longer to learn.

| Check | You're ready when | Why it matters |
| --- | --- | --- |
| Audience size | Your lapsed segment has at least 20,000 users. Larger is better for this program, up to 40,000,000. | Lapsed customers click less often, so the winback decisioning agent needs enough people to see a pattern. |
| Send cadence | You can email this group at least weekly for 30 or more days. | The winback decisioning agent learns from repeated sends. |
| Content | You can provide two to five approaches that differ in angle, such as subject lines, calls to action (CTAs), or images. | The winback decisioning agent can only learn when the options are meaningfully different. |
| Access | **AI Decisioning** appears in your dashboard, and you can open **BrazeAI Decisioning Studio™**. | If the tab is missing, your workspace isn't provisioned yet. Contact your customer success manager. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Check whether you're ready" }

If your lapsed segment is under 20,000 users, you can still run this program. You may see results sooner by starting with a program that gets more clicks, such as a weekly newsletter, a loyalty reminder, or a repeat-purchase email. You can add winback as a later decisioning agent.

## What to expect over time

Plan on prep time to define the segment and gather content, then one working session to build the winback decisioning agent. After launch, the winback decisioning agent sends while it learns. Give it at least 30 days. A lapsed audience can take longer to personalize than a program whose readers click more often.

| Phase | What you do | What happens |
| --- | --- | --- |
| Prepare | Define the segment, gather two to five approaches, and get brand or legal sign-off. | This usually spans a few days. |
| Set up | Create the winback decisioning agent and add your content. | One working session, on your own or with your customer success manager. |
| Launch | Resolve the warnings on the **Review** screen, then launch. | The winback decisioning agent sends on the next eligible day. |
| Learn | Leave the audience and the control split unchanged. | The status is **Learning**. Results can look similar to the random control while the winback decisioning agent tries combinations. |
| Personalize | Check reporting, and add subject lines, CTAs, or images when you have new ones. | The status moves to **Personalization started**. The winback decisioning agent keeps learning after that. |
| Read results | Compare the Decisioning Studio group with the random control group. | Read the comparison after personalization has started. For how to read lift, see [Measuring Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="What to expect over time" }

## Build a winback decisioning agent

### Define the lapsed segment

The winback decisioning agent sends to one Braze segment. Build the entry rule, the exit rule, and the exclusions in that segment.

1. Start with the lapse definition your team already uses. The lapse definitions table lists examples by business type.
2. Set the exit. Choose the action that means the lapsed customer is back, so they leave the segment on their own.
3. Exclude people who shouldn't get email, such as unsubscribed users, hard bounces, and anyone in a do-not-contact group.
4. Keep this segment dedicated to the winback decisioning agent. Overlap with another Canvas or campaign makes the results noisier, because it can't tell which message earned the click.
5. Confirm the audience size in [Check whether you're ready](#check-whether-youre-ready).

| Business type | Lapsed when (example) | Back when (exit) |
| --- | --- | --- |
| Subscription or streaming | No session in 30 or more days | Any new session |
| Retail or eCommerce | No purchase in 90 to 180 days | A new purchase |
| Restaurants and delivery | No order in 45 or more days | A new order |
| Apps and services | No login in 60 or more days | A new login |
| Financial services | No login or transaction in 60 or more days | A new login or transaction |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Lapse definitions by business type" }

When someone comes back, they leave the segment and return to your usual programs. The winback decisioning agent reevaluates segment membership daily. For how to build the segment, see [Creating a segment](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment).

### Hand off email from an existing Canvas

Skip this step if winback isn't in a Canvas today. If it is, choose one of these options:

- Rebuild the Canvas entry rules as a standalone segment, and select that segment as the winback decisioning agent's audience. This is the most direct route.
- Keep the Canvas and hand email to the winback decisioning agent. In the Canvas, add a [Send to Destination](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/send_to_destination) step, select **Decisioning Studio agent** as the destination, and exit users from the Canvas email path. SMS, push, and other channels can stay in the Canvas.

If a message has to arrive in a set sequence, keep that sequence in the Canvas. For the full handoff, see [Use Decisioning Studio Go with Canvas](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/composing_with_canvas).

### Plan your messages

Two to five options that take different approaches give the winback decisioning agent more to learn from than many versions of the same message. Start with what you've already sent to lapsed customers, then add one or two angles you've wanted to try. You can add more later, and adding variants keeps what the winback decisioning agent has already learned.

| Angle | Idea | Example subject line |
| --- | --- | --- |
| What's new | Show what changed since they left. | "A lot has changed since you've been gone" |
| We miss you | A warm reminder of the relationship. | "We saved your spot" |
| Value reminder | Remind them what they get. | "Your benefits are still waiting" |
| Incentive | Your existing winback offer, if you already use one. | "A little something to welcome you back" |
| Social proof | What other customers are enjoying. | "See what everyone's talking about" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Winback message angles" }

Have this ready before you create the agent:

- Two to five subject lines per angle. Vary the tone, the length, and whether you use personalization.
- Two to five CTAs, such as "See what's new", "Come back", and "Pick up where you left off".
- Two to five hero images, uploaded to the Braze [media library](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library).
- A clear name for each base creative, such as "Winback — what's new".
- Brand or legal sign-off before launch.

If you already send an incentive, include it as one base creative. The agent chooses among the creatives and components you provide. For how to structure the library, see [Creative setup and management](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/creative_setup).

**Tip:**


Contact your customer success manager if you want help choosing a segment or the first angles.



### Choose settings

Go to **AI Decisioning**, open **BrazeAI Decisioning Studio**, and select **Create agent**. Name each base creative when you create it, so you can tell the angles apart when you add options.

| Setting | Recommendation for this program |
| --- | --- |
| Agent name | A specific name, such as "Winback — lapsed 90 or more days". |
| Audience | Your dedicated lapsed segment. |
| Control group | Use the split recommended for your audience size. See [Choose your control group size](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup#choose-your-control-group-size). |
| Frequency | The cadence you already use for this audience. You select one frequency, and the winback decisioning agent sends on that cadence. |
| Days | All seven days, so the winback decisioning agent has the widest choice of send days. |
| Quiet hours | Required before launch. A common choice is an overnight window. |
| Frequency capping | Decide whether sends follow your frequency cap and whether they count toward it. |
| Base creatives | Two or three angles, each with a clear name. |
| Personalization | Subject line, CTA, and hero image, each marked with a Liquid tag. |
| Limit repeat sending | **Bi-weekly** on the base creative and the subject line. **Weekly** and **Monthly** are the other windows. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recommended settings for a winback program" }

Before you launch, preview the combinations the agent is allowed to send. For each setting, see [Set up your Decisioning Studio Go agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup).

### Launch and check the first two weeks

1. Resolve every warning on the **Review** screen, then select **Launch**. The winback decisioning agent moves from **Draft** to **Active**.
2. A few days later, confirm sends are going out. The status moves from **Preparing first send** to **Learning**.
3. While the status is **Learning**, keep the segment and the control split as they are. Changing either one reshuffles who is in the Decisioning Studio group and who is in the random control group. Adding subject lines, CTAs, or images does not.
4. Early results can look similar to the random control. The winback decisioning agent is still trying combinations.

### Read results and choose a second program

1. After the status is **Personalization started**, compare clicks for the Decisioning Studio group with the random control group. The winback decisioning agent keeps learning after personalization starts, so treat the first read as a checkpoint.
2. Open **Agent preferences** to see which angles, subject lines, and images the winback decisioning agent chooses most often.
3. Add new options based on what's working. Plan a full library refresh no more than once a month. Targeted swaps can happen sooner. See [Creative setup and management](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/creative_setup).
4. Connect the click lift to the outcome you care about, such as customers who return, purchase again, or start a session.
5. Use the same approach on a second program, such as a newsletter, a loyalty reminder, or a repeat-purchase email.

## Brainstorm ideas with Operator

Use [Operator](https://www.braze.com/docs/user_guide/brazeai/operator) to draft angles, subject lines, and CTAs before you add them as variants. Open Operator from the dashboard, describe the lapsed audience and the cadence, and ask for options that take different approaches. Review every suggestion against your brand guidelines and legal requirements before you add it to the agent.

Start with prompts like these:

- "Suggest five winback email angles for customers who haven't purchased in 90 days. Give each angle a different motivation."
- "Write four subject lines for a winback email about what's new since the customer left. Vary the tone and the length."
- "Draft three CTAs for a winback email that invite the reader back without a discount."
- "I have these winback angles. Which two should I load first as base creatives for a Decisioning Studio Go agent, and what should I check before I launch?"

See the [prompt library](https://www.braze.com/docs/user_guide/brazeai/operator/prompt_library) for more prompt ideas.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/setup"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Set up your Decisioning Studio Go agent</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/creative_setup"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Creative setup and management</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/after_launch"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">What to expect after launch</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/measuring"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Measuring Decisioning Studio Go</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/faq"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Decisioning Studio Go FAQ</span></span></div></a></li></ul>
