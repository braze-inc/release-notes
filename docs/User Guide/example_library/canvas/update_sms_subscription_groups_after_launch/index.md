# Update SMS subscription groups on a live Canvas

> When you move SMS traffic to a new subscription group (for example, new long codes), update every SMS Message step and inbound Action Path rule on the live Canvas, then save a post-launch draft. Apply the draft at cutover so replies to both the old and new sending numbers still follow the same paths.

## About this example

StyleRyde, a fictional on-demand ridesharing brand, runs two-way SMS Canvases for ride updates. Riders receive status texts and reply with keywords (for example, to confirm a pickup). Those Canvases currently send from the `style_ryde_sms_legacy` subscription group. StyleRyde is moving sends to `style_ryde_sms`, which uses a new set of long codes.

If StyleRyde changes only the Message step, outbound SMS uses the new numbers, but Action Path rules still listen only on the old subscription group. Replies to the new long codes never match, so riders don't advance. If StyleRyde removes the original inbound rules too early, replies to the old numbers stop matching while some riders are still mid-journey.

This scenario:

1. Points every SMS Message step at the new subscription group.
2. Adds an inbound SMS trigger for the new subscription group on each Action Path that already listens for inbound SMS, and leaves the original trigger in place.
3. Saves the edits as a post-launch draft, then applies the draft when the new group is ready to send.

## Considerations

- Provision and configure the new SMS subscription group (senders and keywords) before you edit the Canvas. See [SMS and RCS subscription groups](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).
- You can save a draft before every rider is subscribed to the new group. Before you apply the draft, those users must be subscribed to the new group or the Message steps don't send.
- Update every Message step that sends SMS, MMS, or RCS in the Canvas. A missed step keeps sending from the old group after cutover.
- Inbound SMS Action Path triggers are scoped to one subscription group each. Add a trigger for the new group on every path that should still advance when a rider texts either set of numbers.
- Leave the original inbound triggers until you no longer need replies to the old long codes. Riders can receive one or more messages from the old group, then later messages from the new group, especially if you apply drafts on different Canvases at different times.
- A Canvas can have only one post-launch draft at a time. You can't edit the active Canvas while that draft exists. See [Save drafts for Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/canvas_drafts).
- Users already enqueued for a Message step may not pick up post-launch edits. See [Edit Canvases after launch](https://www.braze.com/docs/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch).
- Quiet Hours holds a message and sends it when the window ends. It does not re-evaluate segment membership for that held send. See [Quiet Hours](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/quiet_hours).
- Plan cutover around users sitting in Quiet Hours or already queued. Use [delivery validations](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) if you need an extra eligibility check at send time.
- This example is for Message steps and Action Paths. It doesn't cover campaigns or provisioning new long codes.
- You can't change the subscription group on a Content Optimizer step after that step launches.

## Setup

This example assumes:

| Asset | Details |
| --- | --- |
| Live Canvas | Two-way SMS journey (Message steps plus Action Paths that wait for inbound SMS) |
| Current subscription group | `style_ryde_sms_legacy` (existing long codes) |
| New subscription group | `style_ryde_sms` (new long codes), already created in the workspace |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Setup" }

### Step 1: Open a post-launch draft

1. Open the active Canvas.
2. Select **Save as draft** in the Canvas footer.

Work in the draft until cutover. The live Canvas keeps sending from `style_ryde_sms_legacy` until you apply the draft.

### Step 2: Point SMS Message steps at the new subscription group

For each Message step that includes SMS, MMS, or RCS:

1. Open the step and select the SMS/MMS/RCS channel.
2. In the **SMS/MMS/RCS Variants** dropdown, select `style_ryde_sms`.
3. Confirm the message body and keyword program still match the new group's configuration.

Braze adds an audience filter so only users subscribed to the selected group are eligible for that send.

### Step 3: Add inbound Action Path rules for the new group

For each Action Paths step that advances riders who send inbound SMS:

1. Open the action group that uses **Sent inbound SMS to subscription group**.
2. Keep the existing trigger that uses `style_ryde_sms_legacy`.
3. Add another trigger in the same action group: **Sent inbound SMS to subscription group**, and select `style_ryde_sms`.
4. Match the keyword category and any message-body filters to the original rule, unless the new group uses different keywords.

Riders who text either subscription group's numbers can then follow the same path. Repeat for every action group that should treat the two groups as equivalent.

### Step 4: Save the draft and apply it at cutover

1. Select **Save as draft** after you finish the Message and Action Path edits.
2. Confirm the new subscription group is ready to send and that the riders who should receive SMS are subscribed to `style_ryde_sms`.
3. Select **Update Canvas** to apply the post-launch draft to the active Canvas.

Until you apply the draft, outbound SMS and inbound matching on the live Canvas still use `style_ryde_sms_legacy`.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/canvas/managing_canvases/canvas_drafts"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Save drafts for Canvas</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/managing_canvases/change_your_canvas_after_launch"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Edit Canvases after launch</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/canvas_components/action_paths"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Action Paths</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/canvas_components/message_step"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Message step</span></span></div></a></li><li><a href="/docs/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">SMS and RCS subscription groups</span></span></div></a></li><li><a href="/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">SMS keyword handling</span></span></div></a></li><li><a href="/docs/user_guide/messaging/messaging_fundamentals/quiet_hours"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Quiet Hours</span></span></div></a></li></ul>
