# Choose an API-triggered campaign or Canvas

> Decisioning Studio Pro sends each message through API-triggered campaigns or through one API-triggered Canvas. Choose one architecture per scenario and keep it. A scenario cannot mix both architectures.

For how a decision becomes a message, see [Get started with Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/get_started#message-activation-flow).

## How it works

Decisioning Studio Pro chooses the message, channel, and time for each consumer. The architecture you choose controls how those decisions enter Braze and reach consumers.

You make this choice during design. Changing the architecture after implementation means rebuilding the Braze setup.

### API-triggered campaigns

Each combination of channel and variant has its own API-triggered campaign. Decisioning Studio Pro chooses which `campaign_id` to trigger, then fills that campaign with the message content for that decision.

### API-triggered Canvas

One API-triggered Canvas branches by channel and variant inside Braze. Decisioning Studio Pro chooses which Canvas branch the consumer follows.

## Prerequisites

Share the following with your AI Decisioning Services team so they can recommend an architecture:

- Channels included in the scenario
- Number of message templates per channel
- Third-party integrations to include in the deployment
- Pre-send or post-send logic to include in the deployment

## Compare the architectures

The AI Decisioning Services team helps you choose the architecture for your scenario.

| Element | API-triggered campaign | API-triggered Canvas |
| --- | --- | --- |
| Entry point | Multiple endpoints, one per combination of channel and variant | One entry point, with branches by channel and template inside the Canvas |
| Channel selection | Decisioning Studio Pro chooses the `campaign_id`. The channel is implied by that endpoint. | Decisioning Studio Pro chooses the Canvas branch. Canvas logic routes by channel. |
| In-app messages | Not supported | Supported |
| Variant management | Each variant is its own campaign | [Content Blocks](https://www.braze.com/docs/user_guide/messaging/design_and_edit/content_blocks) or [Audience Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/audience_paths) |
| Pre-send and post-send logic | Lives in the message HTML | Lives in the Canvas configuration |
| Setup scope | One campaign per combination of channel and template. Templates for a channel stay in separate campaigns. | One Canvas branches internally. Use one Canvas per template, or one Canvas for the full scenario. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Architecture comparison" }

## Choose an API-triggered campaign

Use API-triggered campaigns when:

- The scenario is a single channel, such as email only, SMS only, or push only.
- You want each combination of channel and template to map to its own campaign endpoint.

## Choose an API-triggered Canvas

Use an API-triggered Canvas when:

- The scenario sends across channels in one flow, such as email, SMS, push, and in-app messages. A campaign per combination can add many objects to the workspace.
- The scenario needs rules before or after the send. For example, add a delay so the send doesn't race another message flow, or pair an AI-generated message with a banner update in your app. You configure that logic in the Canvas builder.
- The scenario includes in-app messages or in-app branching.
- Your team wants to manage channel routing and related steps in the Canvas builder, with less of that logic maintained in message HTML.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/example_library/decisioning_studio/multi_channel"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Manage multi-channel scenarios</span><span class="guide_tile_description">Channel routing across email, SMS, push, and in-app messages</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Message extras Liquid tag</span><span class="guide_tile_description">Pass decision data on the send for reporting</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio/audience"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Define your audience</span><span class="guide_tile_description">Structure the eligible audience and experiment cohorts</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio/orchestration_setup"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Set up orchestration</span><span class="guide_tile_description">Braze API connection, including the API-triggered campaign path</span></span></div></a></li></ul>

