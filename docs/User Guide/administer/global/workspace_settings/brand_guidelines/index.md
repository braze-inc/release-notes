# Brand guidelines

> Turn your existing brand files and websites into written guidelines. Operator and your agents use them to generate content in your brand's voice and style.

Create and manage brand guidelines from **Content** > **Brand Guidelines**.

## Create brand guidelines {#creating-brand-guidelines}

### Step 1: Fill out brand details

On the **Brand Guidelines** page, select **Create new**. Enter a name and description for your brand guideline.

If you want this brand guideline to be the default for the workspace, select the **Default** toggle. You can have one default per workspace.

### Step 2: Generate or write the guidelines

Choose whether to generate your brand guideline from existing sources or write it manually.

To generate a guideline, upload one or more files, such as a brand book, and add relevant website URLs. Select **Generate brand guidelines**. Braze uses a large language model (LLM) to analyze these sources and write a brand guideline in the dashboard. Review and edit the generated text to make sure it accurately represents your brand.

**Note:**


When you generate brand guidelines from a website URL, Braze might read only the page's text and not capture its visual design. Before you save, check that the guidelines include visual details like colors, layout, and imagery.



To write a guideline manually, describe what makes your brand unique. Include traits, values, voice, rules, and any archetypes that define your brand.

Keep the guidelines to 100,000 or fewer characters.

Consider the following characteristics when writing your guidelines:

| Characteristic       | Definition                                                                       | Example                                                       |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputation               | How you want your brand to be perceived in the market.                               | We are known for being the most reliable and customer-focused brand in our industry. |
| Personality traits       | Human-like characteristics that describe your brand's character.                     | Our brand is friendly, approachable, and always upbeat.          |
| Values                   | Core values that guide your brand's actions and decisions.                           | We value sustainability, transparency, and community.            |
| Differentiation          | Unique qualities that set your brand apart from competitors.                         | We stand out by offering personalized customer service that goes the extra mile. |
| Brand voice              | The tone and style of communication your brand uses.                                 | Our voice is casual yet informative, ensuring clarity without being too formal. |
| Rules                    | Language, claims, or formatting your brand follows.                                      | We use sentence case in headlines, address the reader as "you," and avoid competitor names. |
| Brand archetype          | The archetype that represents your brand's persona (The Hero, The Creator, and so on).    | We embody the "Explorer" archetype, always seeking new challenges and adventures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2: Generate or write the guidelines" }

### Step 3: Test your guideline

In the **Test your guideline** section, preview how your guideline shapes generated content or check whether existing content follows it.

To generate example copy:

1. For **Prompt**, enter an example for the copy generator to iterate on, such as "Shop our fall sale."
2. Select an output type from the **Output type** dropdown.
3. Select a language.
4. Select **Generate content**.

![The Generate content tab with a prompt, an email subject line output type, and five generated subject lines.](https://www.braze.com/docs/assets/img/brand_guidelines/brand_guideline1.png?6fac91846f84f526a548812dec2d9041){: style="max-width:70%;"}

To validate existing content, save the guideline first. Validation checks the content against your last saved guideline.

1. Select the **Validate content** tab.
2. Enter the content you want to check.
3. Select **Validate content**.

![The Validate content tab showing copy that doesn't follow the brand guideline, with an explanation and a suggested revision.](https://www.braze.com/docs/assets/img/brand_guidelines/brand_guideline2.png?db9816f57e1643e0193de174619c814f){: style="max-width:70%;"}

### Step 4: Save your guidelines

When you're happy with your guidelines, select **Save guideline**. Your guidelines are saved to your workspace for future use.

## Manage brand guidelines {#managing-brand-guidelines}

You can edit brand guidelines by selecting them on the **Brand Guidelines** page. Archive a brand guideline to make it inactive and unavailable in message composers. To make it active and selectable again, you can filter for archived brand guidelines and then unarchive it.

## Use brand guidelines {#using-brand-guidelines}

After you save a guideline, add it as context for Operator or an agent. This helps generated content follow the same voice and style.

In the Operator chat panel, select <i class="fa-regular fa-plus"></i>&nbsp;**Add context for Operator**, then choose one or more guidelines under **Brand guidelines**. Operator applies the guidelines you select to generated copy, templates, and images. By default, nothing is selected.

When you configure an agent, select brand guidelines under [Add context](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents#add-resources) so the agent follows that voice and style. The default brand guidelines for the workspace is selected by default.

## How is my data used and sent to OpenAI? {#ai-policy} 
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per [OpenAI’s API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

