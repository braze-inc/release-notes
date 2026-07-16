# What you can do with Operator {#operator-capabilities}

> The AI capabilities previously available as standalone assistants are now accessible through [BrazeAI Operator™](https://www.braze.com/docs/user_guide/brazeai/operator). Because Operator is built into the dashboard and understands your workspace (your brand guidelines, attributes, Connected Content, and the page you're working on), the output is more context-aware than what the previous assistants could produce.

Instead of opening a different tool for each task, describe what you want in natural language and Operator handles it in context. You can also keep the conversation going—asking for a different tone, a shorter version, or a translation—without starting over. Operator can also propose and execute changes directly through [action cards](https://www.braze.com/docs/user_guide/brazeai/operator/reviewing_actions) that you review before they take effect.

## Prerequisites

Operator has the same permissions you do, so certain actions require the relevant permission for that surface—for example, generating an image requires *Edit Media Library Assets*. If you don't see an entry point, check your permissions with your admin. For more information, see [List of permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions#list-of-permissions).

## What's available through Operator {#whats-available-through-operator}

All existing entry points remain in place, so your workflows are unaffected. These experiences are now powered by Operator. The following table maps each previous standalone assistant to where to find it now.

| Previous assistant | What it did | Where to find it now |
| --- | --- | --- |
| AI Copywriter | Generated marketing copy from a product name or description | A new **Ask Operator** icon in the SMS, push, HTML email, and Canvas composers |
| AI Liquid Assistant | Generated Liquid for personalization | A new **Ask Operator** icon in the SMS, push, HTML email, and Canvas composers |
| AI Image Generator | Generated images from a text prompt for the media library | A new **Generate with Operator** button in the media library |
| Data Transformations AI Copilot | Generated transformation code | The **Insert Code** button on the Data Transformation page |
| Content review | Checked content for spelling, grammar, tone, offensive language, and stray code | **Review with Operator** button on the **Test** tab |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="What's available through Operator" }

Operator can also generate HTML for Banners in the Banner HTML editor. For more information, see [Generate messages](#generate-messages).

## Apply brand guidelines {#apply-brand-guidelines}

Operator uses the brand guidelines configured in your workspace so generated copy, templates, and images match your brand's voice, tone, and style. To set up brand guidelines, go to **Content** > **Brand Guidelines**. For more information, see [Brand guidelines](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/brand_guidelines). For details on applying brand guidelines for use with Operator, see [Apply brand guidelines](https://www.braze.com/docs/user_guide/brazeai/operator#apply-brand-guidelines).

## Generate copy {#generate-copy}

You can use Operator to brainstorm or generate copy from anywhere, but you get the best experience using it directly in the message composer, where it can work alongside you on the message you're building. Describe your product or campaign, and Operator returns copy you can review and insert.

Operator improves on the standalone copywriter in a few ways:

- It applies your [brand guidelines](#apply-brand-guidelines) automatically when they're configured.
- It uses [page-aware context](https://www.braze.com/docs/user_guide/brazeai/operator#leverage-page-aware-context), so you don't have to re-describe the channel or message you're working on. Because it's page-aware, you can also use it to edit or refine an existing message instead of generating one from scratch.
- It can look up your [custom attributes](https://www.braze.com/docs/user_guide/data/activation/attributes/custom_attributes) and events, so you can ask it to personalize copy recommendations with real Liquid.
- You can keep the conversation going and iterate. For example, ask for a different tone, a shorter version, or a translation.

### Tones {#generate-copy-tones}

The tone of generated copy is driven by your prompt. Describe the style you want—for example, formal, casual, urgent, or eye-catching—and Operator adjusts its output to match. You can also refine the tone in follow-up prompts, such as asking for a more relaxed or more polished version. When [brand guidelines](#apply-brand-guidelines) are configured, Operator applies them automatically so copy stays consistent with your brand's voice.

### Example prompts {#generate-copy-example-prompts}

<div class="copy-block">
  <p class="copy-block-text">Write a short, eye-catching push notification announcing our summer sale.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Write a short, eye-catching push notification announcing our summer sale." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Rewrite this subject line in a more casual tone.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Rewrite this subject line in a more casual tone." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Translate this copy into Spanish.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Translate this copy into Spanish." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


## Generate messages {#generate-messages}

Operator can generate message HTML in supported composers. Describe the message you want in natural language, review the output, and insert it into your composer.

You get the best results when you use Operator in the composer you're building, where it has [page-aware context](https://www.braze.com/docs/user_guide/brazeai/operator/#leverage-page-aware-context) for the channel and message type. When [brand guidelines](#apply-brand-guidelines) are configured, Operator applies them automatically.

### HTML Banners {#generate-messages-html-banners}

In the [Banner HTML editor](https://www.braze.com/docs/user_guide/channels/banners/create_a_banner/#compose-a-banner), select **Ask Operator** to generate HTML for your Banner. Describe the layout, content, and styling you want. Operator can include [Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/) personalization in the generated markup.

Keep the conversation going to refine the result—for example, ask for a different layout, shorter copy, or updated button styling—before you insert the HTML into the editor.

#### Example prompts {#generate-messages-html-banners-example-prompts}

<div class="copy-block">
  <p class="copy-block-text">Build a Banner that promotes our summer sale with a headline, short description, and Shop now button.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Build a Banner that promotes our summer sale with a headline, short description, and Shop now button." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Use a two-column layout with a product image in the first column and the headline, description, and Shop now button stacked in the second column.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Use a two-column layout with a product image in the first column and the headline, description, and Shop now button stacked in the second column." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Make the dismiss button smaller and position it as a corner dismiss control.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Make the dismiss button smaller and position it as a corner dismiss control." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


## Generate Liquid {#generate-liquid}

In any message composer, open Operator to generate and refine Liquid for personalization. Operator understands [Liquid syntax](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid), your standard and [custom attributes](https://www.braze.com/docs/user_guide/data/activation/attributes/custom_attributes), and [Connected Content](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content), and it can explain what the code does.

### Where you can generate Liquid {#generate-liquid-supported-channels}

As with copywriting, you can ask Operator to generate Liquid from anywhere, and it works across all channels and message composers. You get the best results from within a message composer, where Operator has the full context of the message you're building.

### Liquid capabilities {#generate-liquid-attributes}

Operator is highly capable with Liquid. It can generate complex Liquid logic grounded in the data in your workspace—including looking up [catalog](https://www.braze.com/docs/user_guide/data/activation/catalogs) data to find example values—and it can review and explain the existing Liquid in your campaigns.

### Best practices {#generate-liquid-best-practices}

#### Use natural language {#generate-liquid-use-natural-language}

Operator is trained to understand natural language. Chat with it as you would with a coworker when asking for help. This helps Operator comprehend your needs and provide accurate assistance.

#### Give context {#generate-liquid-give-context}

Providing context helps Operator understand the bigger picture surrounding your project. It's helpful to include context such as:

- Your company name and industry
- A campaign you're working on, such as Black Friday or holiday sales
- Your goal, such as increasing your click-through rate
- Specific custom attributes you want to include in your message

Including context in your prompt helps Operator tailor its responses to better suit your needs. You can also include details from your campaign, message brief, or brainstorming document to bring Operator up to speed.

#### Be specific {#generate-liquid-be-specific}

Operator can ask follow-up questions, but providing details upfront can lead to more precise results sooner. Consider including details such as:

- Any known preferences or requirements for the message
- Instructions on how to handle situations, such as a lack of responses from the message recipient or fallback message options
- Exact or similar values for the custom attributes you want to use, which help Operator generate and test more accurate logic
- When asking for Liquid that uses Connected Content, documentation for the API endpoint, a sample API response, or both

#### Get creative {#generate-liquid-get-creative}

Try different prompts to see how Operator can enhance your messaging. Experiment with different prompts and ideas, as creativity can lead to more engaging results.

### Example prompts {#generate-liquid-example-prompts}




<div class="copy-block">
  <p class="copy-block-text">What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="What is Liquid, and how can it help me enhance the personalization of my marketing campaigns within Braze?" title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="What types of data can I use in Liquid to personalize my marketing messages, such as demographic information or past purchases?" title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Can you give me some examples of how Liquid is used in marketing campaigns to increase engagement and conversion rates?" title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="What are some common use cases for Liquid in text messages for summer sales, such as abandoned cart reminders or personalized promotions?" title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>





<div class="copy-block">
  <p class="copy-block-text">Add a countdown to this message that shows the time until the user&#39;s flight.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Add a countdown to this message that shows the time until the user&#39;s flight." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Personalize this message with the user&#39;s first name, with a fallback if it&#39;s missing.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Personalize this message with the user&#39;s first name, with a fallback if it&#39;s missing." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Improve this Liquid so it&#39;s easier to read.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Improve this Liquid so it&#39;s easier to read." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Create a message that shows different content based on my customer&#39;s loyalty status. If we don&#39;t know about their loyalty status, send a fallback message.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Create a message that shows different content based on my customer&#39;s loyalty status. If we don&#39;t know about their loyalty status, send a fallback message." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Write a dynamic message that includes a user&#39;s favorite product and their last purchase date. If there&#39;s no last purchase, abort the message.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Write a dynamic message that includes a user&#39;s favorite product and their last purchase date. If there&#39;s no last purchase, abort the message." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Write me Liquid to encourage someone to click my message that includes a countdown with how much time is left. If the offer has expired, abort the message." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Help me write a message to encourage users to come back and check out if they have items remaining in their cart.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Help me write a message to encourage users to come back and check out if they have items remaining in their cart." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Write Liquid to personalize a message based on a customer&#39;s country. I want to fill in the message with the country&#39;s name. If we don&#39;t have either of them, suggest they click on a link to update their profile.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Write Liquid to personalize a message based on a customer&#39;s country. I want to fill in the message with the country&#39;s name. If we don&#39;t have either of them, suggest they click on a link to update their profile." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">How can I personalize a welcome message with a user&#39;s first name and write different copy based on the user&#39;s gender?</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="How can I personalize a welcome message with a user&#39;s first name and write different copy based on the user&#39;s gender?" title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Write Liquid to display different messages based on a custom attribute, &quot;CUSTOM_ATTRIBUTE_NAME&quot; and its value. There are six different options I could send. If there&#39;s no value for the custom attribute, I want to send a placeholder message.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Write Liquid to display different messages based on a custom attribute, &quot;CUSTOM_ATTRIBUTE_NAME&quot; and its value. There are six different options I could send. If there&#39;s no value for the custom attribute, I want to send a placeholder message." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>





## Generate images {#generate-images}

Operator generates images using [GPT Image 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/), an AI system from OpenAI and a Braze third-party provider. This lets you create realistic images and art from a description in natural language.

In the [media library](https://www.braze.com/docs/user_guide/messaging/design_and_edit/media_library), select **Generate with Operator** from the **Upload Assets** panel. Describe the image you want, and Operator generates it and saves it directly to your media library.

### Prompt tips {#generate-images-prompt-tips}

- Describe the subject, style, mood, and colors specifically. The more detail you include, the better the result.
- Text input only; uploading a reference image is not supported.
- When you apply [brand guidelines](#apply-brand-guidelines) as context in your Operator prompt, Operator applies them directly to the generated image, so the result reflects your brand's visual style.
- Image generations count toward your daily Operator usage limit. For more information, see [Limitations](https://www.braze.com/docs/user_guide/brazeai/operator/troubleshooting#limitations).

### Example prompts {#generate-images-example-prompts}

<div class="copy-block">
  <p class="copy-block-text">Generate a bright, summery banner image of a beach scene for an email header.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Generate a bright, summery banner image of a beach scene for an email header." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Create a minimalist product background in our brand colors.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Create a minimalist product background in our brand colors." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


## Generate data transformation code {#generate-data-transformation-code}

In the [Data Transformation](https://www.braze.com/docs/user_guide/data/unification/data_transformation) editor, select **Insert Code** to generate transformation code that turns an incoming webhook payload into valid Braze API requests.

For step-by-step instructions on creating a transformation, see [Create a transformation](https://www.braze.com/docs/user_guide/data/unification/data_transformation/creating_a_transformation).

### Example prompts {#generate-data-transformation-example-prompts}

<div class="copy-block">
  <p class="copy-block-text">Write transformation code that maps this survey webhook to a custom event on the user&#39;s profile.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Write transformation code that maps this survey webhook to a custom event on the user&#39;s profile." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


<div class="copy-block">
  <p class="copy-block-text">Update this transformation to identify users by email address instead of external ID.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Update this transformation to identify users by email address instead of external ID." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


## Review content quality {#review-content-quality}

On the **Test** tab for SMS, Android push, iOS push, and traditional in-app messages, select **Review with Operator** to review your content before sending. By default, Operator reviews your campaign for spelling and grammar errors, off-brand or inappropriate tone, offensive language, and any stray code, test content, or unrendered Liquid, and it recommends how to fix what it finds. You can also ask Operator to tailor how it reviews your content directly in your prompt.

### What you can ask Operator to check {#review-content-quality-supported-features}

Beyond its default review, you can direct Operator to focus on specific checks. Consider prompting it to look at any of the following:

| Check | What to ask for |
| --- | --- |
| Spelling and grammar | Ask Operator to proofread for spelling and grammar mistakes and suggest corrections that improve the accuracy of your content. |
| Tone | Ask Operator to evaluate whether the tone matches your intended communication style and flag anything that could be misunderstood. |
| Offensive language | Ask Operator to scan for potentially offensive or inappropriate language so you can revise it and keep your messaging respectful. |
| Accidental content | Ask Operator to catch stray code, markup, or test messages that you added unintentionally, including Liquid that didn't render for a test user. |
| Other languages | Ask Operator to review content written in another language. Support for non-English content can vary, so review the results carefully. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="What you can ask Operator to check" }

### Best practices {#review-content-quality-best-practices}

Consider the following to make the most of content review:

- **Proofread your message:** Although content review can help identify errors, it is still essential to proofread your content manually. Rely on the AI-generated suggestions as a helpful guide, but use your judgment to ensure accuracy.
- **Understand the tone analysis:** The tone analysis results are subjective and based on the AI model's understanding. While they can provide useful insights, consider your intended tone and the conversation context to make appropriate adjustments.
- **Double-check flagged offensive language:** Offensive language detection is designed to be robust, but it may occasionally flag false positives. Review flagged sections carefully and make appropriate changes as necessary.

### Example prompts {#review-content-quality-example-prompts}

<div class="copy-block">
  <p class="copy-block-text">Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it.</p>
  
  <span class="copy-feedback"></span>
  <button class="btn copy-block-btn" data-clipboard-text="Review this push notification for spelling, grammar, and tone, and flag any unrendered Liquid or leftover test content before I send it." title="Copy to clipboard" aria-label="Copy to clipboard">
    <i class="fas fa-copy" aria-hidden="true"></i>
  </button>
</div>


## How is my data used and sent to OpenAI? {#ai-policy} 
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

To generate AI output through BrazeAI features that leverage OpenAI (“Output”), Braze will send certain information (“Input”) to OpenAI. Input consists of your prompts, and may include the content displayed in the dashboard, and other workspace data relevant to your queries, as applicable. Per [OpenAI’s API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. OpenAI may retain data for 30 days for abuse monitoring purposes, after which it is deleted. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.


## Data privacy and security {#data-privacy-and-security}

Operator integrates with OpenAI to generate output. For more information about what information Braze sends to OpenAI, how that data is used, and your intellectual property rights, see [How data is used with OpenAI](https://www.braze.com/docs/user_guide/brazeai/operator#data-privacy-and-security).

## Next steps {#next-steps}

- [Get started with Operator](https://www.braze.com/docs/user_guide/brazeai/operator): Access and use Operator
- [Review actions](https://www.braze.com/docs/user_guide/brazeai/operator/reviewing_actions): Review and approve Operator's proposed changes
- [Troubleshooting](https://www.braze.com/docs/user_guide/brazeai/operator/troubleshooting): Reference common issues and solutions
