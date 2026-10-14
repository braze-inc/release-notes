# Manage multi-channel scenarios

> Decisioning Studio Pro can choose the channel that best advances the scenario for each customer, along with creative, offer, timing, and frequency. Channels include email, SMS, push, and in-app messages. This guide covers how channel decisioning works and how those decisions send through your Braze setup.

For how a decision becomes a message, see [Get started with Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/get_started#message-activation-flow).

## How it works

A channel is an experiment dimension in a Decisioning Studio scenario. The agent chooses it alongside creative, offer, send time, and frequency, and selects the channel that its learning indicates advances the scenario objective for that customer.

Decisioning Studio sends the decision through Braze's API-triggered messaging. When the agent selects "email, template B" for a customer, it calls the Braze endpoint for that email template, fills the template with the content from that decision, and Braze delivers the message through its usual send pipeline.

## Prerequisites

Before you set up multi-channel decisioning, confirm that:

- Every channel in the scenario is connected in your Braze workspace.
- Each customer profile has reliable opt-in and opt-out data for every channel in the scenario.

## Set up multi-channel decisioning

### Step 1: Prepare the action bank

The action bank lists the creative options Decisioning Studio can test for a dimension in the scenario. Channel is usually part of the message dimension, rather than its own dimension.

1. Build the message action bank. List each message option as a row.
2. Tag each message with the channel it sends on, such as email or SMS.

Decisioning Studio chooses only the channels listed in the action bank. Add a channel to the action bank before the agent can select it, even when that channel is already connected in Braze.

For how the action bank fits agent design, see [Design decisioning agents](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/design_agents).

### Step 2: Confirm your message architecture

Decisioning Studio activates a channel decision by calling a Canvas or campaign you build in Braze in advance. The structure depends on how many channels and variants you have, and how much logic those channels share. These are the two common structures:

| Architecture | Description | A good fit when |
| --- | --- | --- |
| One API-triggered Canvas for all channels | One Canvas splits by channel near the entry, then branches by variant under each channel. | You want to build the messages in the Canvas builder, or the scenario includes in-app messages. |
| One API-triggered campaign per channel and message | Each pairing of channel and creative is its own campaign, with its own `campaign_id`. | The action bank has a small, stable set of channel and creative pairings, and you want each pairing to map to one endpoint. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Message architectures for multi-channel decisioning" }

A scenario uses API-triggered campaigns or an API-triggered Canvas for every message. Your AI Decisioning Services team helps you choose during scenario design. For a fuller comparison, see [Choose an API-triggered campaign or Canvas](https://www.braze.com/docs/user_guide/example_library/decisioning_studio/api_triggered_campaign_or_canvas).

### Step 3: Configure Braze for activation

Your team builds and maintains the Canvases or campaigns that receive Decisioning Studio API calls. That work depends on your message assets, brand templates, and workspace permissions. The AI Decisioning Services team reviews the architecture, maps action bank entries to Braze objects, and checks the API payload. That team does not build or own the Braze assets.

A typical Braze setup looks like this:

1. Create the API-triggered Canvases or campaigns you chose in Step 2.
2. In each message, reference Decisioning Studio values as [context variables](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables) in a Canvas, or as [`api_trigger_properties`](https://www.braze.com/docs/api/objects_filters/trigger_properties_object) in a campaign. Map those values to creative fields stored in the action bank.
3. Add the recommendation ID (`rec_id`) to each Canvas or campaign with the [`message_extras`](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) Liquid tag so outcomes map back to the decision that produced them.
4. In the action bank, tag each message option with the `campaign_id` or `canvas_id` used to send it.

For the Braze API key and the campaign setup path, see [Set up orchestration](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/orchestration_setup).

### Step 4: Test before launch

1. On the Canvas or campaign **Test** tab, preview rendering for every channel with sample entry or trigger property values.
2. Finish pre-launch testing with your AI Decisioning Services team.

## Best practices

- Set channel eligibility with Decisioning Studio guardrails. Include customers who can receive any channel in the scenario in the base audience, so the audience stays as large as possible. Use guardrails to keep a customer off a channel they are not eligible for.
- Add a channel to the action bank when that channel has engagement history and opted-in volume the agent can learn from.
- Keep variant coverage comparable across channels. If email has 30 creative variants, give SMS and push a comparable set so the action bank is a fair choice for the agent.
- Watch the channel mix over time. If one channel receives nearly all sends in the Decisioning Studio cohort, check whether other channels have thin opt-in data or whether guardrails leave the agent few eligible options. If the agent prefers one channel, add creatives for the other channels in the action bank after launch.

## Frequently asked questions

### Is the channel split a setting on the Canvas or campaign?

Channel is a decision the agent makes, in the same way it chooses creative or send time. The Canvas or campaign is the Braze object that sends whichever channel Decisioning Studio selects.

### Who builds the Canvases or campaigns Decisioning Studio sends?

Your team configures and owns the Braze messaging setup: the Canvases or campaigns, the templates, and the API permissions. The AI Decisioning Services team supports the design (architecture, action bank mapping, and payload checks) and does not build or maintain those Braze assets.

### Can I add a channel after the scenario launches?

Yes. Add that channel's actions to the action bank and extend the Braze setup to support them. Decisions already made stay as they are. New decisions can include the channel. Adding a channel takes additional engineering work from your team and the AI Decisioning Services team.
