# Creative setup and management

> This guide shows how to build and maintain the creative library your Decisioning Studio Go agent chooses from—so the agent has real, meaningful choices to learn from.

The most important creative decision in Decisioning Studio Go is giving the agent a library of creative options that are meaningfully different from one another. You then need to size and manage that library over time. For the mechanics of adding creatives and marking personalization points, see [Set up your Decisioning Studio Go agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup).

## How the agent sees your creatives

When you add creatives, the agent reads the content and forms a representation of each one. This understanding is one of the three signals the agent learns from, alongside your audience and its engagement. The agent uses these signals to determine which content suits each user and generalize from one creative to the next.

The agent can only tell two creatives apart if they are genuinely different. Two creatives that read the same to the agent give it nothing to choose between.

### What the agent can and can't see

The agent evaluates each creative's fully resolved content. Liquid, catalog references, and Content Blocks are all expanded before the agent builds its understanding, so dynamic and assembled content is part of what it sees.

The one exception is [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content): emails that use it render and send normally, but the agent doesn't see or learn from what Connected Content returns. Make sure the difference between two creatives doesn't exist only in Connected Content. Otherwise, the creatives look identical to the agent.

## Meaningfully different options

The most important principle for creative setup is to provide meaningfully different options. A handful of genuinely distinct subject lines gives the agent more useful choices than a hundred reworded versions.

"Meaningfully different" means you vary the actual strategy (tone, angle, structure, and emotional hook).


| Difference | Example |
| --- | --- |
| Meaningfully different | "48 hours left—then it's gone" compared with "{{first_name}}, your cart misses you" (urgency compared with a personal reminder) |
| Too similar | "Don't miss our sale" compared with "Our sale is here" (the same message, reworded) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Meaningfully different options" }


The same principle applies to components and whole emails (base creatives). Distinct base creatives give the agent meaningful choices, while near-duplicates don't.

## Send frequency and library depth

Library size depends on how often you send.

- Increase your library depth as your send frequency increases. An agent that sends daily cycles through a small set of options sooner and must repeat them, so a daily program needs more creatives than a weekly one.
- Organize your library into groups of distinct options based on your send frequency. A large library works when it offers genuinely different options. For example, provide 10 distinct angles instead of 100 rewritten versions.

Your repetition constraints interact with this. If you cap how often a user can receive the same base creative or subject line (see [Set up your agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup)), you need enough distinct options that valid options remain after the cap is applied. Otherwise, the agent has nothing valid left to send and skips the send.

## Image-only emails

For an image-only email, configure one base creative and let the agent choose the image within it. You can also let the agent choose the subject line. Don't add each image variation as a separate base creative because the agent treats them as near-duplicates.

## Manage creatives over time

- Adding variants doesn't reset training. When you add a new subject line, CTA, or image, the agent keeps what it has learned about existing options and adds the new one to its menu. Add variants as needed.
- Promote changes to apply them. Creative edits take effect after you promote your configuration changes. Promoting changes doesn't reset the agent.
- Keep wholesale changes infrequent. Swapping out most of your library at once effectively restarts the agent's learning for those options. Plan wholesale library refreshes no more than once a month. Make targeted seasonal swaps as needed.
- Refresh content for seasonal moments on a trained agent. Keep your always-on agent running and swap in seasonal creatives as the moment approaches. The agent brings its accumulated learning into the new content.

## Checklist

- Each base creative is meaningfully different from the others (distinct angle or structure, not a reworded copy).
- Differences between creatives appear in authored content the agent can see. Content served only by Connected Content does not create that difference.
- Your library is deep enough for your send frequency and organized into distinct groups.
- Every personalized component has enough valid options that a repetition cap can't exhaust them.
- Image-only emails use one base creative with the image as a personalized component.
- You have a plan to refresh your full creative library no more than once a month and make targeted seasonal swaps as needed.

For what happens after you launch and how the agent learns from these creatives, see [What to expect after launch](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/after_launch).
