# Set up your Decisioning Studio Go agent

> This article describes how to configure a Decisioning Studio Go agent with the self-serve setup flow in the Braze dashboard.

For an overview of how Decisioning Studio Go works, see [BrazeAI Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go). To confirm your program is a good fit before you configure an agent, see [Examples for Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/examples).

## Prerequisites

Confirm you have the following ready:

- A [segment](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment) for your entry audience that isn't actively used in another Canvas or campaign. We recommend a minimum audience of 20,000 users; the agent supports audiences up to a maximum of 40,000,000. Smaller audiences can run, but they learn more slowly and show less reliable lift.
- At least one email template.
- The variant content you want to test, such as alternative subject lines, calls to action (CTAs), and hero images. You can create variants during setup, but having them ready speeds up configuration.
- Workspace access with permissions to configure AI Decisioning agents.

If your workspace hasn't been provisioned for Decisioning Studio Go, you won't see the agent configuration option in the **AI Decisioning** tab. Contact your customer success manager to get access.

## Step 1: Set up your agent

1. In the Braze dashboard, go to the **AI Decisioning** tab.
2. Select **Create Agent**.
3. Give your agent a name that distinguishes this agent from others in your workspace. An example is "Loyalty Members—Weekly Engagement" rather than "Email Agent".
4. (Optional) Add a description to provide context that you or a teammate may need later. This can include what the agent is for, which segment it targets, and what success looks like.

The agent optimizes your email creative to maximize genuine engagement, measured by meaningful click activity per user. Clicks pass through multiple independent validation filters that screen out automated activity and opt-out-related clicks, so the signal reflects real customer interest rather than raw click volume.

## Step 2: Select the target audience

Select the Braze segment your agent sends to. Users in this segment are automatically split into two groups:

- **Decisioning Studio group:** Receives AI-optimized email content. The agent picks the best variant combination for each user.
- **Random control group:** A permanent measurement group that receives randomly chosen combinations of the same options you configured, on allowed days within the same schedule and constraints. The only difference from the Decisioning Studio group is that the choice is random rather than AI-optimized. This group is required, and it is how lift is measured. Users in this group still receive email.

### Choose your control group size

The recommended split scales with your audience size: a larger audience can measure lift reliably with a smaller control group, while a smaller audience needs a proportionally larger one to stay statistically meaningful. The minimum control group size is 5%.

| Audience size | Recommended split (Decisioning Studio / random control) |
| --- | --- |
| 20,000 – 100,000 | 80 / 20 |
| 100,000 – 1,000,000 | 90 / 10 |
| 1,000,000 – 40,000,000 | 95 / 5 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Choose your control group size" }

### Why a dedicated segment matters

If users in your selected segment also receive messages from other Canvases or campaigns, engagement the agent observes is affected by those other messages. The agent can't tell whether a user clicked because of its decisions or because of something else. A warning appears if your selected segment is in use elsewhere; proceed, but expect noisier results.

### User Lookup

Use **User Lookup** to verify whether specific users meet your segment criteria. This is useful for verifying your segment definition.

### Audience filters

Audience filters aren't supported in this release. If you need additional targeting criteria, [create a segment](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment) with those filters applied, then select that segment as your entry audience.

### Integrate with existing Canvases

To use Decisioning Studio Go inside a broader journey:

1. Create a dedicated segment for users who should be in the agent.
2. In your [Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas), use a User Update step to add the user to that segment at the right point in the journey.
3. Confirm that users exit the Canvas so the agent handles email sending for everyone in the segment from that point on.

## Step 3: Configure the schedule

Determine when the agent is allowed to send.

### Step 3.1: Determine the send frequency

Select how often users receive emails from this agent—for example, three times per week. This is a single selection. The agent doesn't optimize between different frequencies; it picks days and times within the frequency you set.

### Step 3.2: Select the days of the week

Choose which days the agent can send on. You must select at least as many days as your frequency requires (if the agent sends three times per week, select at least three days; selecting more days gives the agent more flexibility). The agent optimizes within that set, picking the best days for each user. For maximum flexibility, select all seven days.

### Step 3.3: Set quiet hours

Specify the times the agent shouldn't choose for a send. Quiet hours use the user's local time zone, and the most common use is to block late-night and very-early-morning sends. Outside quiet hours, the agent schedules sends at the times most likely to drive clicks for each user.

Quiet hours guide the times the agent chooses for a send. For a guaranteed send block, also set [workspace-level quiet hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours).

For audiences across multiple time zones, the agent prioritizes delivering your message over sending it at the precise intended local time. A message may occasionally arrive outside its intended day or time window. If most of your audience is in one region, consider that when setting allowed days and quiet hours.

### Step 3.4: Set frequency capping rules

Your frequency capping rules can be applied at the agent level:

- **Apply frequency cap:** Prevents the agent from sending to a user once their frequency cap has been met. Depending on how your rules are configured, this cap may apply at the individual user level or the overall account level. In either case, messages are not sent to that user while the cap is met.
- **Count toward cap:** Choose whether sends from this agent count toward the user's overall cap.

**Tip:**


If your frequency cap protects user experience, the agent's sends are already targeted and you may not need to count them toward the cap. If your cap controls overall send volume or spend, you likely want them counted. Your customer success manager or solutions consultant can help you confirm the right approach for your workspace.



## Step 4: Add content and templates

Define what the agent has to work with:

- **Base creatives:** The full email templates. The agent first picks which base creative to send to a given user.
- **Creative components:** The specific elements within a base creative—subject line, CTA, and hero image—that the agent personalizes per user.

You can build base creatives by:

- Using the standard Braze email composer
- Importing an email from an existing Canvas or campaign

Use a single base creative or many. With one base creative, the agent personalizes only the components inside it. With multiple base creatives—for example, one casual, one formal, and one promotional—the agent also picks which base creative is right for each user. The agent can also choose from several base creatives with no additional creative components.

When you add creatives, the agent builds its own representation of each one and uses that understanding to decide which content suits which users. Meaningfully different options help it distinguish between creatives and learn from them. For guidance on structuring your creative library, see [Creative setup and management](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/creative_setup).

### Step 4.1: Mark personalization points with Liquid tags

For each component you want the agent to personalize, replace the static content in your base creative with a Liquid tag from the personalization menu. Then provide the variant options in the **Creative Components** section.

The supported components in this release are:

- **Subject line:** Replace the subject line in **Sending Settings** with the Liquid tag for subject line.
- **CTA:** Replace the button text in the email body with the Liquid tag for CTA.
- **Image:** Replace the hero image URL with the Liquid tag for image.

The agent evaluates each creative's fully resolved content. Liquid, catalog references, and Content Blocks are expanded before the agent builds its understanding, so dynamic and assembled content is part of what it sees.

[Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content) is an exception. It renders and sends normally, but the agent doesn't see or learn from what it returns, so don't rely on Connected Content as the thing that makes two creatives different.

### Step 4.2: Add variants

In the **Creative Components** section, add the variant options for each personalization point:

- Multiple subject line options
- Multiple CTA text options
- Multiple images

Each variant can be associated with specific base creatives, or made available across all base creatives. For example, if you have one base creative promoting a sale and another promoting new arrivals, you can restrict your `Don't miss our biggest savings of the year` subject line to the sale creative only, while keeping your `Just dropped` CTA available across both.

Images must be selected from the Braze [media library](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library). You can't paste a raw image URL. If there's an image you want to use, upload it to the media library first.

If your email is a single image with no separate text elements, use one base creative and let the agent choose the image within it. You can also let the agent choose the subject line. Don't load each image variation as a separate base creative.

### Step 4.3: Preview and test

As you add more content, preview and test your message using the dynamic preview that shows how different variant combinations render. This is helpful to spot and resolve rendering issues before launch. After your base creatives and variants are configured, you can see a full list of all combinations the agent is allowed to send.

You can also test send the message to yourself or a teammate. Test sends display the specific variant combination you select, not what the agent would pick for any particular user.

## Step 5: Define constraints

Constraints prevent the agent from sending repetitive content to the same user. The following levels are available:

- **Base creative level:** Prevents the same base creative from being sent to a user more than once within a window you define. Useful when each base creative is distinct enough that repeating it within, for example, a week would feel stale.
- **Subject line level:** Prevents the same subject line from being sent to a user more than once within a window you define. Useful when subject lines are the most visible repetition signal.

Variant-level constraints on specific images or CTAs aren't supported in this release.

## Step 6: Review and launch

The **Review** screen displays your full configuration: audience and random control split, schedule, base creatives, variant counts, and active constraints. Review and resolve any validation warnings (for example, segment overlap with another campaign) that display in this section.

Select **Launch** to activate the agent. It transitions from **Draft** to **Active** and begins sending on the next eligible day.

## After launch

### Training period

When your agent launches, it enters a training period, and its reporting shows which stage it's in. The agent progresses through these stages:

| Stage | What's happening |
| --- | --- |
| **Launched, not yet sending** | The agent is active but hasn't made its first send. |
| **Waiting for signal** | The agent is sending, but hasn't yet gathered enough genuine clicks to begin training. |
| **In training** | The agent has enough signal and is exploring combinations. It is expected that performance can look close to random during this phase. |
| **Partially trained** | The agent is personalizing, but results aren't yet robust enough to read as final. |
| **Fully trained** | The agent is fully trained and results are robust. This is the point to trust and report on lift. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Training period" }

Two things move the agent forward: accumulated genuine clicks (training begins after enough clean clicks accrue, and results become robust at a higher threshold) and calendar time (personalization becomes meaningful roughly from the start of the second week of training). A low-volume audience can stay in **Waiting for signal** for several days. This can indicate it needs more engagement volume.

A new user receives their first send on the first day they enter the audience, and the agent begins personalizing for them the day after. Emails continue to send the whole time the agent learns.

Don't judge results, resize the audience, or change the control split while the agent is still training. For what to expect through each stage and how to read early results, see [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch).

### Reporting views

The reporting interface offers three main views:

| View | Description |
| --- | --- |
| **Performance** | Click rates, engagement metrics, and the lift of the Decisioning Studio group versus the random control. The headline learning metric is *Unique Customers Who Clicked Daily*. |
| **Configuration** | The current settings of the agent—useful for confirming what's running. |
| **Agent preferences** | Counts of how often each variant has been chosen by the agent, showing what the agent is gravitating toward for your audience. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reporting views" }

Element-level breakdowns show how individual subject lines, CTAs, and images perform across all combinations.

### Edit an active agent

Go to the **Configuration** view to modify audience, schedule, creatives, or constraints after launch. Both variants and dimensions can be changed after launch. The Configuration view shows a summary of changes; promote them before they take effect. Adding new variants keeps the agent's training on existing variants and adds the new options to its menu.

Changing the control-versus-AI split proportion or swapping the segment triggers a reshuffle of users between the Decisioning Studio and random control groups. Creative, schedule, and constraint edits do not reshuffle the audience.

### Pause or stop

An agent's lifecycle is **Draft** > **Active** > **Stopped**. Select **Stop** at any time to halt an agent; it stops sending and resumes when you reactivate it.

## Reference

The following table summarizes areas of Decisioning Studio Go and related details.

| Area | Details |
| --- | --- |
| **Channel** | Email only |
| **Conversion metric** | Genuine clicks only (unique customers who clicked daily) |
| **Personalization points** | Subject line, CTA, hero image (per base creative) |
| **Audience** | One Braze segment (20,000 recommended minimum, 40,000,000 maximum), with required random control (minimum 5%; see recommended splits) |
| **Frequency** | Single selection (no frequency decisioning) |
| **Test sends** | Through Braze composer |
| **Reporting** | Performance, Configuration, and Agent preferences views, plus element-level breakdowns |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio Go reference" }

### Considerations

- The agent evaluates fully resolved content, so Liquid, catalog references, and Content Blocks are all part of what it learns from. [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content) renders and sends normally but isn't seen by the agent.
- Images are selected from the Braze media library. Pasting a raw image URL isn't supported.
- Audience filters aren't supported beyond segment selection.
- Body copy, preheader, and header personalization aren't available yet.

## Troubleshooting

Contact your customer success manager or solutions consultant for help with agent configuration, performance review, or program design.

For common reporting and setup questions, see [Troubleshooting Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/troubleshooting).

For common questions, see the [Decisioning Studio Go FAQ](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/faq).
