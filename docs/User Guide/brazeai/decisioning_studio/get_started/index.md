BrazeAI Decisioning Studio™ allows you to design and deploy decisioning agents that optimize any business metric.

This reference gives an overview of the steps involved in setting up Decisioning Studio, including designing your agent, configuring and connecting data sources, setting up orchestration, and evaluating performance.

## Key design decisions

Work with the AI Decisioning Services team to make the following decisions:

| Decision | Description | Examples |
|----------|-------------|----------|
| **Success metric** | The business outcome the agent maximizes when personalizing customer engagement. | Revenue, LTV, ARPU, conversions, retention |
| **Audience** | The customers for whom the Decisioning Studio agent makes engagement decisions. | All customers, loyalty members, at-risk subscribers |
| **Experiment groups** | How should Decisioning Studio's randomized controlled trials be structured? | Decisioning Studio, Random Control, BAU, Holdout |
| **Dimensions** | The engagement decisions the agent personalizes for each customer. | Time of day, subject line, frequency, offers, channel |
| **Options** | The specific variants the agent can select within each dimension. | Specific templates, offers, time windows |
| **Constraints** | The business rules and limits that restrict agent decisions. | Geographic restrictions, budget limits, eligibility rules |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Key design decisions" }

Each of these decisions has implications for how much incremental uplift the agent may be able to generate, and how quickly. Our AI Decisioning Services team works with you to design an agent that generates maximum value while respecting all of your business rules.

![Diagram showing how success metrics, audience, experiment groups, dimensions, options, and constraints feed into a Decisioning Studio agent design](https://www.braze.com/docs/assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png?fc5870f6c0a7cf634c654d71e21b9436)

## Decisioning Studio capabilities

| Capability | Details |
|------------|---------|
| **Any success metric** | Optimize for revenue, conversions, ARPU, LTV, or any business KPI |
| **Unlimited dimensions** | Personalize across offer, channel, timing, frequency, creative, and more |
| **Any CEP** | Native integrations with Braze, Salesforce Marketing Cloud, or custom integrations for any platform |
| **AI Decisioning Services** | Dedicated support from Braze's data science team |
| **Advanced experiment design** | Fully customizable treatment groups and holdouts |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio capabilities" }

## Best practices

A few best practices for designing Decisioning Studio agents:

- **Maximize data richness:** The more information agents have about your customers, the better they perform.
- **Diversify actions:** The more diverse the set of actions the agent can take, the more it can personalize its strategy for each user.
- **Minimize constraints:** The fewer constraints on your agents, the better. Constraints should be designed to respect business rules while freeing agent-led experimentation as much as possible.