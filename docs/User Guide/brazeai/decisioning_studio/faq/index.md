# Frequently asked questions

> This article provides answers to some frequently asked questions about Decisioning Studio Pro.

## What is a decisioning agent?

A decisioning agent is a custom configuration for BrazeAI Decisioning Studio™ Pro that's tailor-made to meet a specific business goal. This is defined by the success metric, dimensions, and options you choose. The decisioning agent automatically discovers the optimal action for every customer to maximize your chosen business metric.

### What metrics can I optimize for?

You can optimize for any business metric that aligns with your goals, such as revenue, conversions, average revenue per user (ARPU), customer lifetime value (CLV), profit, contract renewals, or any other business KPI.

### What are dimensions in Decisioning Studio Pro?

Dimensions can be thought of as the *types of levers* that the decisioning agent can pull to maximize the success metric. Typical dimensions include offer, subject line, creative, channel, or send time.

### What is an action bank?

The action bank defines the *specific options* that the decisioning agent has access to for each dimension "lever". For instance, for a channel dimension, you define the specific channels the decisioning agent has access to. For an offer dimension, you define the specific offers the decisioning agent can test.

### Can the decisioning agent take actions I haven't configured?

No. The decisioning agent can only take actions that you configure and add to the action bank. This means that all possible actions are defined by the combinations of what you put in the action bank.

### What are constraints?

Constraints limit the decisioning agent's actions to respect critical business rules. For example, this could be preventing a specific offer from being selected for customers in an ineligible geography, or setting a maximum budget for the decisioning agent to spend.

### What is the difference between Decisioning Studio Go and Decisioning Studio Pro?

Decisioning Studio Go is a self-service option for recurring email programs that optimizes for clicks. Decisioning Studio Pro includes support from the AI Decisioning Services team, optimizes any business metric, and connects to any data source. To learn more about Go, see [Decisioning Studio Go](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio_go).
