# Send to Destination step

> Use the Send to Destination step to send users to another Canvas or a Decisioning Studio Go agent. Users continue in the source Canvas. For example, you can connect Canvases that share messaging for promotional offers.

## How it works

![A Send to Destination step to send users to a new Canvas.](https://www.braze.com/docs/assets/img/send_to_destination1.png?fe2eea5457018add9a41076d8483eb24){: style="float:right;max-width:35%;margin-left:15px;"}

Your current Canvas with the Send to Destination step is the source. In **Destination type**, select **Canvas** or **Decisioning Studio agent**, then select the destination. Users continue in the source Canvas. The destination applies its own entry rules.

For a Canvas destination, users from the source Canvas must meet the destination Canvas audience criteria. Let's say you have two Canvases:

- **Source:** Canvas 1, includes a Send to Destination step that sends users to Canvas 2
- **Destination:** Canvas 2, with audience criteria to enter users who ordered an item

This step allows users from Canvas 1 to be sent to Canvas 2. When users from Canvas 1 enter the Send to Destination step, they are evaluated against Canvas 2's audience criteria to determine if they're eligible to enter the Canvas. In this case, users who ordered an item can enter Canvas 2 and also continue their journey in Canvas 1. For users who haven't ordered an item, they continue their journey in Canvas 1 only.

### Entry behavior

These rules apply when the destination is another Canvas.

The Send to Destination step enters users into the destination Canvas as soon as they reach this step. This step acts as a one-time entry point into the destination Canvas. Users who meet the destination Canvas audience criteria begin that Canvas journey. Users who don't meet those criteria at that moment don't enter the destination Canvas and continue in the source Canvas.

Send to Destination also respects the destination Canvas [re-entry settings](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) under **Entry Controls**. If a user isn't eligible to re-enter the destination Canvas, they aren't sent to it and continue in the source Canvas.

If the destination Canvas uses a scheduled entry schedule, the Send to Destination step bypasses that entry schedule. It also bypasses [**Limit entrance volume**](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) under **Entry Controls** on the destination Canvas when it's set to **Every time Canvas is schedule**. Users sent from this step don't wait for the next scheduled evaluation window—they're evaluated against the destination Canvas audience criteria and entered immediately when they reach the Send to Destination step.

If the destination Canvas uses action-based entry, the Send to Destination step bypasses the requirement for users to perform the configured entry action to enter that Canvas.

## Create a Send to Destination step

### Step 1: Add a step

Drag and drop the **Send to Destination** component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Send to Destination**.

### Step 2: Choose your destination

In **Destination type**, select **Canvas** or **Decisioning Studio agent**. In **Destination**, select the Canvas or agent, or enter its name. Then select **Done**.

![A Send to Destination step set up to send users from a Canvas named "Feature Adoption" to "New Canvas".](https://www.braze.com/docs/assets/img/send_to_destination2.png?319d903f29526f93b190c30c4306f05a)

### Step 3: Preview your destination

When the destination is a Canvas, select **Preview destination** to view the Canvas you're sending users to.

After you've set up this step, [preview the user path](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/preview_user_paths) to see whether a user continues in the current Canvas and whether they are sent to the destination.

## Send users to a Decisioning Studio Go agent

Use this step to add users from a Canvas to a Decisioning Studio Go agent. For how the agent sends after users join its audience, see [Use Decisioning Studio Go with Canvas](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/composing_with_canvas). For agent setup, see [Set up your Decisioning Studio Go agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup).

Set up the agent and its segment before you select the destination:

1. Create a segment for the agent's entry audience. For more information, see [Creating a segment](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment).
2. In the agent's **Entry audience**, select that segment and select **Add directly to the audience**.
3. On the segment, add a filter group. Select `Cohort membership` > `Decisioning Studio Agent`, then include this agent.
4. In the Send to Destination step, select **Decisioning Studio agent** in **Destination type**. Then select the agent in **Destination**.

When users reach the step, Braze adds them to the agent if it exists and **Add directly to the audience** is selected. The step doesn't evaluate the agent's segment at that moment. Users enter the agent's audience after the segment includes the `Decisioning Studio Agent` filter. The agent reevaluates segment inclusion each day before it generates recommendations.

Users continue in the source Canvas after the step.

If the agent has a draft or stopped status, the step shows a warning that users aren't sent until the agent is active. When **Add directly to the audience** is selected, the step can still add those users. If you clear **Add directly to the audience**, or the agent no longer exists, users aren't added. Select another agent before you launch the Canvas.

To see or change the agent, you need the "View Decisioning Studio Agent" permission in the workspace. If Decisioning Studio Go isn't available in the workspace, **Decisioning Studio agent** is unavailable, and the step links to [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go).

## Frequently asked questions

### Can I set the destination to a draft Canvas?

Yes. The destination Canvas can have a draft or idle status.

### Can I send users to a Decisioning Studio Go agent?

Yes. Select **Decisioning Studio agent** in **Destination type**, then select the agent in **Destination**. Select **Add directly to the audience** on the agent, and include that agent with the segment's `Decisioning Studio Agent` filter. Users who reach the step are added when **Add directly to the audience** is selected. They aren't added if **Add directly to the audience** is cleared, or if the agent no longer exists.

### Are context variables preserved?

Yes, when the destination is another Canvas. The [context](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables) of the source Canvas is passed to the destination Canvas. However, context variables must be invoked within the source Canvas to be passed to the destination Canvas.

### Can I use the Send to Destination step to connect Canvases instead of using API or User Update workarounds?

Yes. You can connect Canvases with the Send to Destination step when users should move directly into another Canvas journey.

You don’t need separate User Update steps, API triggers, or webhooks solely to move users between Canvases, as long as they meet the destination Canvas audience criteria when they’re sent.

### Do users enter at the start of the destination Canvas?

Eligible users enter immediately at the first step of the destination Canvas. They don't wait for a later scheduled entry time on the destination Canvas. You can't link into a specific Canvas step inside the destination Canvas.

### Does the Send to Destination step respect a scheduled destination Canvas entry schedule?

No. If the destination Canvas uses a scheduled entry type, users sent from the Send to Destination step don't wait for the next scheduled evaluation window. They're evaluated against the audience criteria and entered immediately when they reach the Send to Destination step.

### How does advancement behavior work for Send to Destination steps?

Users who enter the Send to Destination step continue their user journey if there are additional steps in the source Canvas. If the destination is a Canvas and users meet its audience criteria, they enter that Canvas and begin that journey. If the destination is a Decisioning Studio Go agent and **Add directly to the audience** is selected, Braze adds them to that agent. They continue in the source Canvas.

### Is the Send to Destination step subject to API rate limits?

No. Braze sends users to another Canvas or adds them to a Decisioning Studio Go agent without external API calls.
