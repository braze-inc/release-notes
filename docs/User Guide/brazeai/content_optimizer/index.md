# Content Optimizer

> Content Optimizer helps you test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically.

## About Content Optimizer

Content Optimizer runs in a Canvas step. It helps you define message components to test, generate variants using generative AI or manual input, and automatically optimize which content combinations are sent to users. Content Optimizer is available for these channels: email, push notifications, and SMS/MMS/RCS messages.

This feature helps you to:

- Optimize subject lines, preheaders, sender names, body headers, body content, primary CTAs, and images for emails.
- Optimize titles, messages, and images for push notifications.
- Optimize hooks, bodies, and CTAs for SMS and MMS messages.
- Optimize hooks, bodies, CTAs, and images for RCS messages.
- Continuously improve message performance without manual A/B test setup.
- Test high volumes of content variants, leveraging AI for ideation.
- Automatically phase out underperforming content and scale up winners.

Learn how to create a [Content Optimizer step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

### Choose between Content Optimizer and similar features

Content Optimizer finds one winner for your audience by generating variants and mixing their elements. It does not personalize per user.

| If you want to | Use |
| --- | --- |
| Test campaign variants you already wrote | [Optimize with BrazeAI](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection) |
| Test Canvas journey paths | [Winning Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path) |
| Generate and mix content variants for the audience | Content Optimizer |
| Personalize creative, timing, or offers for each recipient | [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/decisioning_studio_go) or [Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Choose between Content Optimizer and similar features" }

For a full comparison of BrazeAI features, see [BrazeAI](https://www.braze.com/docs/user_guide/brazeai).

## How is my data used and sent to OpenAI? {#ai-policy} 
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per [OpenAI’s API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.


### OpenAI and Content Optimizer {#openai-and-content-optimizer}

Content Optimizer uses OpenAI only when you explicitly request AI-generated variant suggestions. It does not use OpenAI to choose which variant each user receives or to allocate send traffic.

- **Uses OpenAI:** When you select **Generate AI suggestions** for a content component, Braze sends your seed variant, instructions, optional [brand guideline](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/brand_guidelines), and (for launched steps with sufficient send data) aggregated performance context to OpenAI to generate variant ideas.
- **Bandit optimization:** Braze's proprietary multi-armed bandit algorithm handles traffic allocation, variant selection at send time, and performance-based optimization. See [How it works](#how-it-works).
- **Manual entry:** You can define variants by typing them yourself without sending content to OpenAI.

## Plan tiers

Content Optimizer availability depends on your plan.

| Feature | Free | Pro |
| --- | --- | --- |
| Active Content Optimizer steps | One active step at a time per workspace | Unlimited steps to launch |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content Optimizer plan tiers" }

On the Free plan, if you already have an active Content Optimizer step and try to launch another, you can continue editing and save the new step as a draft, but you can't launch it until you free up the active slot.

To free the slot, disconnect the existing active step and save the Canvas, or stop or archive another Canvas that has an active Content Optimizer step. Contact your Braze account manager if you need more than one active Content Optimizer step.

## Use cases

### Email

| Optimization use case | Goal | Description |
| --- | --- | --- |
| Subject line variations | Increase open rate | Test tone, urgency, personalization, and use of emojis. |
| Header messaging styles | Boost engagement | Compare emotional, value-driven, and clear messaging in the body header. | 
| Body content format | Improve readability and engagement | Test storytelling versus feature lists, bullets versus paragraphs, and content length. |
| CTA copy and tone | Increase click-throughs | Compare action-led, benefit-focused, and first-person CTA phrasing. |
| Image variations | Improve engagement | Test different creative, product shots, or visual treatments in the email body. |
| Themed content combinations | Discover high-performing combinations | Mix and match themed subject, body, CTA, and image components to find the best overall combination. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Email" }

### Push notifications

| Optimization use case | Goal | Description |
| --- | --- | --- |
| Title variations | Increase open rate | Test clarity, urgency, personalization, and tone in the push title. |
| Body copy styles | Improve engagement | Compare concise, benefit-led, and action-oriented messaging in the push body. |
| Image variations | Improve engagement | Test different creative or visual treatments in the push notification. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push notifications" }

### SMS, MMS, and RCS messages

| Optimization use case | Goal | Description |
| --- | --- | --- |
| Hook variations | Increase engagement | Test urgency, personalization, and tone in the first line shown in SMS previews, MMS captions, or RCS introductions. |
| Body copy styles | Improve engagement | Compare concise and action-oriented messaging in the body, including wording that accompanies media on MMS and RCS. |
| CTA copy variations | Increase click-throughs | Compare action-led and conversational CTA phrasing for links and next-step prompts in SMS, MMS, and RCS. |
| Image variations (RCS only) | Improve engagement | Test different creative or visual treatments in RCS messages. Image is not supported for SMS or MMS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS, MMS, and RCS messages" }

## How it works {#how-it-works}

Braze's bandit algorithm handles the optimization described in this section.

Content Optimizer uses a non-contextual [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) algorithm to allocate more sends to high-performing variants and reduce allocation to underperforming ones. Over time, this results in continuous improvement of your message content, with minimal manual intervention.

Braze's proprietary bandit optimization algorithm is built specifically for the combinatorial nature of the Content Optimizer step. Given that each message comprises several components, the bandit simultaneously learns about the performance of each component (such as the subject line, body, CTA) as well as their interactions when combined into a message. More concretely, when a given combination is sent, all combinations that share the same components benefit from the data of that send. This allows the bandit to learn much faster on the same amount of data, relative to a standard bandit algorithm.

When the step first launches, Content Optimizer sends variants randomly to collect initial performance data. Every step stays in the Learning state for at least seven days and no more than 15 days before Braze moves it to Optimizing or Action Recommended. During Learning, traffic is generally distributed across available variants so the algorithm can learn from their relative performance. After Learning, Content Optimizer begins shifting traffic toward higher-performing content combinations and gradually reducing allocation to underperforming options. For details, see [Step states](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step#step-states).

Content Optimizer is similar to the Message step in Canvas, with features like quiet hours, [Intelligent Timing](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/intelligent_timing), and event logging. You can configure a Content Optimizer step by creating a base message and defining which content components (such as subject line, body text, or call-to-action) to optimize. Variants for each component can be generated with AI or entered manually, and Liquid tags must be added to the base message to map components into the message content.

Each user receives one message per entry into the Content Optimizer step. Re-entries are treated as new, with no memory of previous variants.

## Canvas entry setup

For best results, use Content Optimizer in Canvases where users enter the step gradually and regularly over time, such as in recurring or always-on Canvases with consistent daily volume. If all users enter the step at once, Content Optimizer won’t have time to learn from early results. The step will behave more like a static A/B test than a live optimization engine.

The best fit for Content Optimizer is in daily recurring entry Canvases, as well as event-triggered and API-triggered Canvases with relatively consistent daily user entries. If you do use Content Optimizer in single-send Canvases or "spiky" entry Canvases (like recurring monthly), consider using [Entry controls](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) to smooth out user entries over the course of multiple days.

### Key concepts

| Term                    | Description |
|-------------------------|-------------|
| Base message   | The main message template that variants are built from, including all send settings. |
| Content components  | Elements within a message (for example, subject line or primary CTA) that can be tested and optimized. Marketers must insert the relevant Liquid tag into the message where the component should appear. |
| Content variants    | The different values a content component can take. |
| Content combinations| Unique messages created by mixing and matching content variants. |
| Optimization event       | Determines how Content Optimizer evaluates performance and allocates traffic to content combinations over time, such as clicks or opens for email. Applies to all content components in a step. Content Optimizer continuously learns from this event and automatically shifts delivery toward higher-performing content combinations. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Key concepts" }

## Considerations

- Content Optimizer is available for these channels: email, push notifications, and SMS/MMS/RCS messages.
- For email, Content Optimizer can generate up to 625 combinations per step:
   - Up to four components per step
   - Up to five variants for each component
- For push notifications, Content Optimizer can generate up to 125 combinations per step:
   - Up to three components per step (title, message, and image)
   - Up to five variants for each component
- For SMS and MMS messages, Content Optimizer can generate up to 125 combinations per step:
   - Up to three components per step (hook, body, and CTA)
   - Up to five variants for each component
   - Image is not supported for SMS or MMS
- For RCS messages, Content Optimizer can generate up to 625 combinations per step:
   - Up to four components per step (hook, body, CTA, and image)
   - Up to five variants for each component
- Only one message is sent per user per entry. There is no memory of previous sends for re-entries.
- Marketers must manually insert Liquid tags for each component in the message composer where the defined content component variants should render.
- If a user's send is delayed by delivery controls such as quiet hours, Intelligent Timing, rate limiting, or message prioritization, they can still receive a variant you deactivated after assignment. See [Edit a launched step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step#edit-a-launched-step).

## Next steps

- Contact your Braze account manager if you need more than one active Content Optimizer step.
- Learn how to create a [Content Optimizer step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step).
