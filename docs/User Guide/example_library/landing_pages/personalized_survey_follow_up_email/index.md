# Send a personalized email after a landing page survey

> Collect rating responses on a Braze landing page survey, write them to the user profile as custom attributes, then trigger a personalized email that scores the responses and adapts the copy with Liquid.

## About this example

StyleRyde, a fictional on-demand ridesharing brand, asks drivers to complete a short safety self-check on a Braze landing page. Each question is a 1–5 rating. When a driver submits the survey, Braze logs the scores as custom attributes. StyleRyde then sends an email that calculates an average score and shows tips that match that score.

This scenario combines:

- [Landing page surveys](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys) with [rating scale](https://www.braze.com/docs/user_guide/messaging/surveys#number-scale-questions) form blocks
- Custom attributes for follow-up messaging and segmentation
- The [landing page Liquid tag](https://www.braze.com/docs/user_guide/messaging/landing_pages/tracking_users) so known users stay on one profile
- An action-based email campaign triggered by [Submitted a Landing Page form](https://www.braze.com/docs/user_guide/messaging/landing_pages/retargeting_users)
- Liquid math and conditionals for score-based copy

Use this example when you want survey answers on the profile and a near-real-time personalized message after submission. For survey analytics alone, profile attributes and follow-up messaging aren't required.

## Considerations

- Create the landing page with **Survey** as the message type so you get rating scale blocks, survey reporting, and attribute logging controls. Standard landing page forms support dropdowns for ratings, but those values save as [string custom attributes](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages), which limits numeric segment filters.
- Survey [rating scales](https://www.braze.com/docs/user_guide/messaging/surveys#number-scale-questions) can log responses as integer custom attributes. Prefer integers when you plan to segment on score thresholds or run Liquid math without converting strings.
- Writing custom attributes (and optional custom events) consumes [data points](https://www.braze.com/docs/user_guide/data/data_points/). Long-form text survey answers can't be logged as profile attributes.
- Embed the `{% landing_page_url %}` Liquid tag in the message that drives traffic to the survey. Without it, submitting the form can create a new anonymous profile instead of updating the known user. For more information, see [Track users through a form](https://www.braze.com/docs/user_guide/messaging/landing_pages/tracking_users) and [About landing page tracking data](https://www.braze.com/docs/user_guide/messaging/landing_pages/about_tracking_data).
- Prefer the native **Submitted a Landing Page form** trigger for follow-up campaigns. You don't need a separate custom event on the submit button for this example.
- Landing pages with forms need a confirmation experience (confirmation landing page, multi-step confirmation step, or post-submit URL). Plan that before you publish.
- Test the survey, attribute writes, trigger, and Liquid preview in a development workspace before you publish to production.

## Setup

### Step 1: Create custom attributes for each rating question

1. Go to **Data Settings** > **Custom Attributes**.
2. Create one custom attribute per survey question. For StyleRyde's two-question safety check, use integer attributes such as:
   - `driver_survey_attention` — how often the driver checks mirrors and blind spots (1–5)
   - `driver_survey_fatigue` — how rested the driver feels before a shift (1–5)
3. Use clear, stable names. Map each rating block to these attributes in the survey editor and reference the same names in Liquid.

If you already created the attributes with the wrong data type, create new integer attributes for rating scales rather than reusing string attributes meant for dropdowns.

### Step 2: Build the landing page survey

1. Go to **Messaging** > **Landing Pages** and create a new landing page.
2. On the message composition page, select **Survey** as the message type, then open the drag-and-drop editor.
3. Fill in site details (page URL, title, and related settings). For more information, see [Create landing pages](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages).
4. Add a [rating scale](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) block for each question (for example, 1–5).
5. For each rating block:
   - Set an **Identifier for Reporting** for survey analytics and CSV export
   - Turn on logging to the matching custom attribute from Step 1
   - Mark at least one question as required so you always capture a score when someone submits
6. Add a submit button, then set its click action to open your confirmation page or another post-submit URL.
7. (Optional) Use a [multi-step form](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) so questions and confirmation live in one survey flow.
8. Publish the landing page after you finish composition and confirmation.

### Step 3: Link known users to the survey from email

In the invitation or reminder email that sends drivers to the survey, insert the landing page Liquid tag so Braze can update the existing profile on submit.


```html
<a href="{% landing_page_url styleRyde-driver-safety-check %}" class="button">Start your safety check</a>
```


Replace `styleRyde-driver-safety-check` with your landing page URL handle. Generate the tag from **Personalization** > **Landing Page** in the message editor. For more information, see [Track users through a form](https://www.braze.com/docs/user_guide/messaging/landing_pages/tracking_users).

### Step 4: Create the personalized follow-up email campaign

1. Create an email campaign.
2. For delivery, select **Action-Based Delivery**, then **Submitted a Landing Page form**, and select the survey landing page from Step 2.
3. In the email body, assign the survey attributes to Liquid variables, calculate an average score, and branch the copy.

Use the following Liquid in an HTML block at the top of the message to assign and average the survey responses:


```liquid
{% comment %} Assign survey responses. plus: 0 coerces string values if a block logged strings instead of integers. {% endcomment %}
{% assign attention = {{custom_attribute.${driver_survey_attention}}} | plus: 0 %}
{% assign fatigue = {{custom_attribute.${driver_survey_fatigue}}} | plus: 0 %}
{% assign sum = attention | plus: fatigue %}
{% assign average = sum | divided_by: 2.0 %}
```


Use the following Liquid in the email body to branch the copy based on the average score:


```liquid
{% if average < 3 %}
Your StyleRyde safety score is {{ average | round: 1 }} out of 5. Here are tips to strengthen mirror checks and rest before your next shift.
{% elsif average >= 3 and average < 4 %}
Your StyleRyde safety score is {{ average | round: 1 }} out of 5. You're on a solid path—use these reminders to stay consistent.
{% elsif average >= 4 %}
Your StyleRyde safety score is {{ average | round: 1 }} out of 5. Great work—here are advanced habits to keep that score high.
{% else %}
Thanks for completing your StyleRyde safety check. Open the StyleRyde driver hub for more safety resources.
{% endif %}
```


Adapt attribute names, thresholds, and tips to your brand. Assign each custom attribute to a variable before you combine them in math filters. For more information, see [Math filters](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/filters/#math-filters).

Preview with users who have sample attribute values, then launch when the survey landing page is live.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Landing page surveys</span></span></div></a></li><li><a href="/docs/user_guide/messaging/surveys"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Surveys</span></span></div></a></li><li><a href="/docs/user_guide/messaging/landing_pages/create_landing_pages"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Create landing pages</span></span></div></a></li><li><a href="/docs/user_guide/messaging/landing_pages/tracking_users"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Track users through a form</span></span></div></a></li><li><a href="/docs/user_guide/messaging/landing_pages/retargeting_users"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Retarget users through a landing page</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid/filters"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Liquid math filters</span></span></div></a></li></ul>
