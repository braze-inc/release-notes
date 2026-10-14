# BrazeAI Decisioning Studio™ Go

> Learn how to set up and integrate BrazeAI Decisioning Studio™ Go into Braze.

## About Decisioning Studio Go

Decisioning Studio Go is an AI decisioning agent for recurring email programs. Instead of choosing one winning subject line, send time, or image for an entire audience, the agent selects the best combination for each recipient based on their past engagement.

You define the variants the agent can choose from—such as subject lines, calls to action (CTAs), images, send days, and send times. For each user in your segment, the agent picks the option most likely to drive engagement, within the constraints and schedule you configure.

This differs from campaign-level A/B testing with [Optimize with BrazeAI™](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection), which optimizes variants for the audience. Decisioning Studio Go personalizes at the individual level across every send in the program.

### How it works

The agent splits a Braze segment into two groups: a Decisioning Studio group that receives AI-optimized email content, and a random control group that receives randomly chosen combinations of the same options you configured. The random control gives you an ongoing, like-for-like measurement of the agent's lift. You can always see how the personalized experience performs against the same content chosen without personalization. The minimum control size is 5%, and we recommend scaling it to your audience (see [Set up your agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup)).

For each user in the Decisioning Studio group, the agent chooses across the options you provided: which creative to send (including the specific subject line, CTA, and image within it), and when to send it (day of the week and time of day, respecting quiet hours and the user's local time zone). [Set up your Decisioning Studio Go agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup) covers each of these in detail.

As users engage—or don't—the agent learns. It draws on three signals, all within Braze: your audience, that audience's email engagement, and its own understanding of your content. When you add creatives, the agent builds its own representation of each one and uses it to reason about which content suits which users. The agent moves through defined training stages, and reporting always shows which stage it's in, so you know when it's still exploring versus actively personalizing. See [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch) for the stages and how to read early results.

### What you configure

| Configuration | Description |
| --- | --- |
| **Audience** | A single Braze segment as the entry audience (we recommend a minimum of 20,000 users; the maximum is 40,000,000). The agent automatically splits the segment between the decisioning group and the random control group. |
| **Schedule** | Send frequency (for example, a single selection three times per week), allowed days of the week, quiet hours in the user's local time zone, and agent-level frequency capping rule adherence. |
| **Creatives** | One or more base creatives built in the Braze composer. Within each base creative, you can mark a subject line, CTA, and image as personalization points using Liquid tags, then provide a list of variants for each. The agent decides which base creative and variant to use for each recipient. |
| **Constraints** | Limits that prevent the agent from sending the same base creative or the same subject line to a user more than once within a window you define. |
| **Review and launch** | A final validation screen surfaces any warnings to attend to before you launch. The agent moves from **Draft** to **Active** and begins sending. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What you configure" }

### When to use Decisioning Studio Go

The strongest fit is recurring email programs with stable audiences and clickable content, such as always-on calendars (rewards, content drops, lifecycle nudges), evergreen programs (winbacks, re-engagement), and multi-email promotions. These give the agent enough volume and variety to learn meaningfully.

An always-on agent is also the right way to handle seasonal moments: keep a trained agent running and swap in updated creatives as a moment approaches, rather than spinning up a dedicated agent for a short promotion that would end before the agent finishes learning.

See [Examples for Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/examples) for detailed fit guidance by program type.

### Where Decisioning Studio Go sits in the Decisioning Studio suite

Decisioning Studio Go is the entry tier of BrazeAI Decisioning Studio. It's designed for marketers who want one-to-one email personalization without the setup overhead of a full Decisioning Studio Pro implementation. Go learns from your audience and its engagement within Braze.

Decisioning Studio Pro adds:

- Optimization for any business metric, including revenue and conversions
- Connection to any first-party data source
- Multichannel decisioning
- Extended orchestration patterns
- Dedicated support from the Braze AI Decisioning Services team

## Decide between Decisioning Studio Go and Pro

Decisioning Studio Go and Pro are two tiers of the same decisioning engine. This guide helps you pick the right one for your use case.

Decisioning Studio Go is the self-serve tier: you set it up yourself inside Braze, it optimizes email for clicks, and it works with the options you configure. Decisioning Studio Pro is the full-service tier: the same engine, opened up to any channel, data source, and business metric, with support from the Braze AI Decisioning Services team.

Everything you can do in Decisioning Studio Go, you can also do in Decisioning Studio Pro. The question is whether your use case fits inside Decisioning Studio Go's scope or needs Decisioning Studio Pro.

### Overview

Choose Decisioning Studio Go for a recurring email program where clicks are a meaningful signal and you can provide subject line, CTA, image, and base creative options yourself. Choose Decisioning Studio Pro when you need a custom metric, first-party data, multiple channels, offer or product decisioning, or custom constraints.

| Capability | Decisioning Studio Go | Decisioning Studio Pro |
| --- | --- | --- |
| Channel | Email | Any channel |
| Optimizes for | Genuine clicks (engagement) | Any business metric, including revenue, conversions, and lifetime value |
| Learns from | Your audience, its email engagement, and the agent's understanding of your content | All Go data, plus your first-party data, such as custom attributes, warehouse or Cloud Data Ingestion (CDI) data, and custom conversion events |
| Offers and product decisioning | Not supported | Supported |
| Constraints and guardrails | Productized frequency, repeat-content limits, and quiet hours | Custom constraints and logic |
| Setup | Self-serve in the Braze dashboard | Designed and configured with the AI Decisioning Services team |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning Studio Go and Pro capabilities" }

### Common triage examples

As a general rule, Decisioning Studio Pro uses custom data and can optimize a custom conversion metric. Decisioning Studio Go optimizes clicks using your audience and its engagement.

If you're not sure which tier fits your program, your customer success manager or solutions consultant can help you decide.

| Goal | What to use |
| --- | --- |
| Personalize a recurring email program for engagement with self-serve setup | Decisioning Studio Go |
| Optimize the same program for conversions or revenue | Decisioning Studio Pro |
| Choose which product or offer to feature for each user | Decisioning Studio Pro |
| Use CDI or custom attribute data to drive decisions | Decisioning Studio Pro |
| Personalize across email, push, and SMS together | Decisioning Studio Pro |
| Start with self-serve email personalization and get expert help later if you outgrow it | Decisioning Studio Go, then Decisioning Studio Pro |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Common Decisioning Studio tier examples" }


## Next steps

<ul class="guide_tiles"><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/setup"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Set up your Decisioning Studio Go agent</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/creative_setup"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Creative setup and management</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/after_launch"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">What to expect after launch</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/measuring"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Measuring Decisioning Studio Go</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/composing_with_canvas"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Use Decisioning Studio Go with Canvas</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/examples"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Review examples for Decisioning Studio Go</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/troubleshooting"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Troubleshooting Decisioning Studio Go</span></span></div></a></li><li><a href="/docs/user_guide/brazeai/decisioning_studio_go/faq"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">FAQ</span></span></div></a></li></ul>
