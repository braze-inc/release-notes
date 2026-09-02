# Optimizing A/B tests

> Use **Optimize with BrazeAI™** to automatically optimize a campaign with multiple variants.

In the **Target Audiences** step, go to **A/B Testing**, then turn on **Optimize with BrazeAI™**.

For a single-send campaign, BrazeAI™ sends an initial test and then sends the best-performing variant to the remaining audience. For a multi-send campaign, BrazeAI™ reviews performance every 12 hours and shifts more users toward better-performing variants.

For prerequisites, configuration options, and reporting details, see [Optimizing A/B tests with BrazeAI](https://www.braze.com/docs/user_guide/brazeai/intelligence_suite/variant_selection).

**Note:**


Existing campaigns that use Personalized Variant continue to support that optimization and its analytics. Personalized Variant isn't available when creating a new campaign.



Braze checks user eligibility again before the second send in a single-send optimization. Users who weren't eligible for the initial test may enter the remaining audience, while users who are no longer eligible don't receive the follow-up send.

For information about campaign results, see [A/B testing analytics](https://www.braze.com/docs/user_guide/messaging/ab_testing/analytics).
