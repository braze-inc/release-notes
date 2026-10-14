# Use Decisioning Studio Go with Canvas

> Most teams run Decisioning Studio Go alongside an existing journey rather than on its own. This guide shows how to hand the email portion of a journey to an agent while keeping the rest of your orchestration in Canvas.

A Decisioning Studio Go agent sends to a single Braze segment. Users enter the agent's audience when they join that segment, so you can use anything that changes segment membership to add them, most commonly a Canvas that adds users at the right moment.

## The core pattern: hand off the email, keep the rest

The cleanest way to use an agent inside a broader journey is to route users into the agent's segment at the point where you want the agent to take over email, while letting other channels continue in the Canvas.

1. Create a dedicated segment for the agent. For more information, see [Creating a segment](https://www.braze.com/docs/user_guide/audience/segments/creating_a_segment). The segment should not be actively used by another Canvas or campaign. Overlapping messaging makes the agent's results noisier because it can't tell whether a click came from its decision or from another message.
2. Add users to that segment at the right point in your Canvas using a [User Update step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/user_update). Where available, a [Send to Destination step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/send_to_destination) can pass users from a Canvas into an agent.
3. Make sure users exit the Canvas email path after they enter the agent's segment, so the agent owns email for those users from that point on. Other channels, such as SMS and push, can continue in the Canvas.

## Keep other channels in the Canvas

A common setup is a journey that sends both email and SMS. Hand email to the agent and keep SMS in the Canvas:

- Use a path or experiment split so the agent-owned email and the Canvas-owned SMS don't both send at the same time.
- Remember that the agent decides send timing per user, so its email sends won't line up with a fixed Canvas schedule. If your SMS is meant to pair closely with an email, keep that pairing inside the Canvas rather than splitting it across the agent and the Canvas.

## Use Canvas to run a business-as-usual comparison

A Canvas [Experiment Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step) step is the recommended way to test the agent against your current business-as-usual (BAU) program. Route one path to BAU and the other into the agent's segment. This is a clean, random split. See [Measuring Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring) for how to set up a fair comparison.

## Segment hygiene checklist

- The agent's segment is dedicated to the agent and isn't shared with another active Canvas or campaign.
- Users who enter the agent's segment exit the Canvas email path.
- Exit and suppression logic you need, such as removing a user for 14 days after a purchase, is built into the segment definition as an exclusion group. The agent reevaluates segment membership daily.
- Verify that a few representative users land in the segment as intended by using **User Lookup** in the Braze dashboard.

## Consideration for global audiences

Sends happen in each recipient's local time zone. The agent prioritizes delivering a message over sending it at the exact intended local time, so if your audience spans time zones far from your workspace, a message may occasionally arrive outside its intended day or time window.

If your journey depends on precise local timing across very different regions, contact your customer success manager or solutions consultant about the best setup.
