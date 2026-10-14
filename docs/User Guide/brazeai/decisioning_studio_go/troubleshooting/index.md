# Troubleshooting Decisioning Studio Go

> This page covers common questions about what you're seeing in reporting and setup, and what's normal versus what needs action.

Many of the things that look like problems in the first weeks are expected behavior. This guide covers the most common ones. For the bigger picture on the learning period, see [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch).

## Reporting

### My reporting is empty right after launch

Reporting takes a few days to populate after you launch, and the data lags by about a day. Set your reporting end date to two days before today for a complete view, and give it a few days before concluding anything is wrong.

### Decisioning Studio click numbers are lower than my other email reports

This is expected. The agent learns only from genuine clicks, so before any click counts it passes validation filters that screen out automated activity and opt-out-related clicks. That makes Decisioning Studio totals lower than raw email reports. The comparison between the Decisioning Studio group and the random control stays valid, because the same filtering applies to both.

### My agent looks like it's losing, or results are flat

Usually, this means the agent is still training, or it's being compared against the wrong benchmark. Check the following in order:

1. Is the agent **Fully trained**? If it's still in an earlier stage, you're reading the training period. Wait.
2. What are you comparing against? The clean comparison is the agent compared with its random control. A still-training agent usually trails a mature business-as-usual program at first. That gap is expected. See [Measuring Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring).
3. Is the audience generating enough genuine clicks? A small or low-engagement audience trains slowly.
4. Are your creatives meaningfully different? If the options read the same to the agent, it has little to optimize. See [Creative setup and management](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/creative_setup).

### My agent has been in "Waiting for signal" for a while

The agent hasn't gathered enough genuine clicks to begin training. This almost always means the audience is smaller than the recommended size of 20,000 or doesn't click much. Growing the audience or increasing engagement moves it forward faster than waiting.

### Historical numbers changed after I edited creatives

Deactivating or removing a base creative that an agent has been using can shift historical reporting, because that creative's past sends and clicks drop out of the view. If you need to retire a creative, expect the historical totals to change. Avoid deactivating campaigns linked to Decisioning Studio Go during an active test.

## Setup

### I don't see the agent configuration option

Your workspace may not be provisioned for Decisioning Studio Go yet. Contact your customer success manager to get access.

### I can't add an image variant, or my image URL doesn't work

Images must be selected from the Braze [media library](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library). You can't paste a raw image URL. Upload the image to the media library first, then select it.

### Does the agent see Content Blocks or catalog content?

Yes. The agent evaluates each creative's fully resolved content, so Liquid, catalog references, and Content Blocks are all part of what it learns from. The one exception is [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content): it renders and sends normally, but the agent doesn't see or learn from what it returns.

### Does selecting Launch again reset my agent?

No. Promote your configuration changes to apply edits. Promoting changes doesn't reset the agent or its training. Adding new variants also doesn't reset training on existing ones.

### I changed the control split or swapped the segment, and users moved between groups

That's expected. Changing the control split, or swapping the segment, triggers a reshuffle of users between the two groups. Avoid making these changes during an active test. Creative, schedule, and constraint edits do not reshuffle the audience.

### Some users aren't getting an email on their first day—or sends arrive late for distant time zones

A new user receives their first send on the first day they enter the audience, and the agent begins personalizing the day after. For audiences spread across time zones far from your workspace, the agent currently prioritizes delivery over exact local timing, so a message may occasionally arrive outside its intended day or time window.

## When to contact support

Reach out to your customer success manager or solutions consultant if, after you confirm these checks, your agent is **Fully trained** and still underperforming its random control, or if your agent's setup behaves in a way this guide doesn't explain.
