# What to expect after launch

> Your agent learns before it performs. This guide explains the training period, how to tell which stage your agent is in, and how to read early results without drawing the wrong conclusion.

When you launch a Decisioning Studio Go agent, it learns first. Emails go out from day one, and during the early training period the agent is still exploring. Knowing what's normal during this period is the difference between giving the agent a fair chance and turning it off before it has shown what it can do.

## The training stages

Your agent moves through five stages, and reporting always shows which one it's in.

| Stage | What's happening | What you should do |
| --- | --- | --- |
| **Launched, not yet sending** | The agent is active but hasn't made its first send. | Wait for the first send. |
| **Waiting for signal** | The agent is sending, but hasn't gathered enough genuine clicks to begin training. | Make sure the program is generating engagement. If it sits here a long time, the audience may be too small or too low-engagement. See [The two things that move your agent forward](#the-two-things-that-move-your-agent-forward). |
| **In training** | The agent has enough signal and is actively exploring combinations. Performance can look close to random here. This is expected. | Don't read results yet. Let the agent run. |
| **Partially trained** | The agent is personalizing, but results aren't yet robust enough to treat as final. | You can start watching the trend, but don't make decisions on it yet. |
| **Fully trained** | The agent is fully trained, and results are robust. | This is the stage to read lift, report it, and make decisions. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="The training stages" }

## The two things that move your agent forward

You need two conditions for a trustworthy result. Both have to be met:

1. Enough genuine clicks. The agent trains on clicks, but only genuine ones. Automated and opt-out-related clicks are filtered out first. Training begins once enough genuine clicks accrue, and results become robust at a higher threshold. A low-engagement or small audience reaches these thresholds slowly.
2. Enough time. Even with strong signal, personalization becomes meaningful only after the agent has had roughly the first week and a half of training to work with. You can typically assess results after a few weeks.

An agent still in **Waiting for signal** needs more genuine clicks. If your agent is still in **Waiting for signal** well into the run (for example, after 10 days), it hasn't collected enough genuine clicks yet, often because the audience is smaller than the recommended size or doesn't click much. Growing the audience or increasing engagement moves it forward faster than waiting.

## Reading early results without drawing the wrong conclusion

The most common mistake is judging the agent during training against the wrong benchmark:

- Early numbers understate the agent. While it's exploring, the agent is deliberately trying options it hasn't learned about yet, so its performance looks close to random. That's the cost of learning, and it pays off once the agent is trained.
- A still-training agent usually trails a mature program. If you compare a brand-new agent against a program you've already optimized over months or years, the agent often looks worse at first. The gap closes once the agent finishes training. Wait until the agent is **Fully trained** before comparing.

**Note:**


Don't judge results, resize the audience, or change the control split while the agent is still training. Each of these either reads noise as signal or disrupts the learning in progress. Changing the control split or swapping the segment also reshuffles users between groups. For more information, see [Set up your Decisioning Studio Go agent](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/setup).



## What to check if your agent looks like it's losing

Before concluding the agent isn't working, confirm:

- Is it **Fully trained**? If not, you're reading the training period. Wait.
- What are you comparing against? The clean, built-in comparison is the agent compared with its random control. If you're comparing against a mature business-as-usual program, expect an early gap. See [Measuring Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring).
- Is the audience generating enough genuine clicks? If it's stuck in **Waiting for signal** or slow to leave **In training**, the audience may be too small or too low-engagement.
- Are your creatives meaningfully different? If the options all read the same to the agent, it has little to optimize. See [Creative setup and management](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/creative_setup).

## How long to run

Plan to run an agent for at least 30 days, and ideally keep it always on. Thirty days gives most programs enough time to clear training and produce a credible read. Running continuously lets the agent keep improving. You can support seasonal campaigns by swapping in new creatives.

After your agent is **Fully trained**, see [Measuring Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go/measuring) for how to read lift and compare against your current program.
