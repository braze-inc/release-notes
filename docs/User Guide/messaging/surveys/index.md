# Surveys

> Braze surveys let you collect first-party feedback directly from your users and act on it in follow-up messaging, without leaving the Braze dashboard. Use surveys to understand user sentiment, capture preferences, and build segments and triggers from the responses you collect.

## Channel availability

Surveys are available on landing pages and in-app messages. On either channel, select **Survey** as your message type on the message composition page before opening the editor to switch into survey mode. You can also collect an NPS score from email by linking an [email NPS Survey block](https://www.braze.com/docs/user_guide/channels/email/drag_and_drop/nps_survey) to a published survey landing page. Each channel page covers the channel-specific create flow, composition, and reporting location, while this page covers the concepts and capabilities that apply across channels.

| Channel | Build surveys in |
| --- | --- |
| Landing pages | [Landing page surveys](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys) |
| In-app messages | [In-app message surveys](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys) |
| Email | [Email NPS survey block](https://www.braze.com/docs/user_guide/channels/email/drag_and_drop/nps_survey) (links score clicks to a landing page survey) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Survey channel availability" }

## Surveys page

Go to **Messaging** > **Surveys** to find surveys across landing pages, campaigns, and Canvases in one place. Use it as your entry point for reviewing survey performance across channels.

**Note:**


If you don't see **Surveys** under **Messaging**, contact your Braze account manager.



## Analytics {#analytics}

Every survey question type includes enhanced reporting by default, so you can review response data without building a segment or exporting to a separate tool first.

Top-level analytics include:

- **All responses:** Total complete and incomplete responses
- **Completed:** Users who completed all required questions
- **Partially complete:** Users who submitted some data, but did not complete all required questions
- **Unique impressions:** Total page views

Partial submissions have a six-hour grace period before they appear in results, so users can finish the rest of the survey. A response can stay partially complete until the user selects the final submit control—even when the only question is an NPS rating, such as a score recorded from an [email NPS Survey block](https://www.braze.com/docs/user_guide/channels/email/drag_and_drop/nps_survey).

![Survey responses page showing NPS score analytics with promoter, passive, and detractor percentages and a horizontal bar chart of score distribution.](https://www.braze.com/docs/assets/img/surveys/survey_responses.png?81fd35feff57a0e05d364c0e18f05cbc)

### Chart types

For radio button, dropdown, and checkbox form blocks, you can choose among three chart types in the survey analytics view. This gives you more flexibility to interpret and share insights without exporting to a third-party tool.

| Chart type | Best for |
| --- | --- |
| **Bar chart** | The default horizontal view of response counts and percentages. |
| **Column chart** | A vertical view of response counts and percentages. Use this chart to compare responses side by side, especially for multi-select questions or questions with more answer options. |
| **Pie chart** | A proportional breakdown of responses. Use this chart for single-select questions when you want to see how responses are distributed across options. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Survey chart types" }

Each chart shows real-time data as responses come in. You can switch chart types at any time without affecting the underlying data.

![Survey question-level breakdown using a bar chart.](https://www.braze.com/docs/assets/img/surveys/bar-charts-1.png?7b179c4e582b7a8e489b618dc5746236)

## Multi-step landing page forms

Build a survey as a single landing page with multiple steps that are automatically linked together, instead of creating multiple standalone landing pages and linking them manually. For example, you can define separate steps for each survey question, plus a confirmation step at the end.

This capability is specific to the landing pages channel. In-app message surveys also support a page manager for moving between steps; see [Compose an in-app message survey](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys#compose-an-in-app-message-survey) for details.

![Landing page editor with a multi-step Form preview and the Form properties panel listing steps and a locked Confirmation step.](https://www.braze.com/docs/assets/img/surveys/multi_step.png?d86d88b24dec6e397d32c59210896f27)

## Question and form blocks

Landing pages and in-app messages support all their standard form blocks in surveys too, including radio button group, checkbox, checkbox group, dropdown, phone capture, email capture, and short text capture. This section highlights the three form blocks with reporting built specifically for surveys: NPS, number scale, and long-form text.



### Standalone NPS block {#standalone-nps-block}

The **NPS** block is a separate form block from the **Rating** (number scale) block, not a configuration option within it. Add it to a survey to ask the standard Net Promoter Score question (0–10) and get reporting built specifically for that use case.

The **NPS** block gives you better dashboard reporting than a plain rating question used for the same purpose. Instead of a flat count of responses per number, Braze automatically groups responses into promoters (9–10), passives (7–8), and detractors (0–6) and surfaces those segments—and the resulting NPS score—directly in the survey analytics view.

Currents exports the numeric score (and, if added, the free-text feedback field) on the **Survey Response** event. Promoter, passive, and detractor segments aren't separate Currents fields.

![A mobile NPS survey next to the Survey responses dashboard, which shows an NPS score with promoter, passive, and detractor breakdowns and a response distribution chart.](https://www.braze.com/docs/assets/img/surveys/survey_and_chart.png?073d81290a48a7aedec6d867b7d27f35)



### Number scale questions {#number-scale-questions}

Also called a rating scale on the channel pages; both terms refer to the same **Rating** form block. Capture 1–5, 1–10, or 0–10 number-scale questions to fit different survey and reporting needs, from simple satisfaction ratings to likelihood-to-recommend scores. For channel-specific composition screenshots, see the Rating scale section on the [landing page surveys](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) or [in-app message surveys](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) page.

You can collect a rating as a survey response, log it as an integer custom attribute, or both. Pair a number scale question with a [long-form text capture](#long-form-text-capture) block to collect a numeric score alongside qualitative feedback in the same survey.

![Landing page survey editor with a 1–5 rating question selected and the Rating properties panel open on the right.](https://www.braze.com/docs/assets/img/surveys/rating_block.png?c8b66581715b64f402e144df0178bd52)



### Long-form text capture {#long-form-text-capture}

Long-form text capture is useful for qualitative feedback. You can configure the minimum and maximum character count (up to 1,000 characters), whether to show the character limit during composition, the text area height, and placeholder text.

![Long text capture block settings.](https://www.braze.com/docs/assets/img/surveys/long-form-surveys.png?92db595db8a8cbd42cf1afbf62b4aabd){: style="max-width:40%;"}

**Important:**


Long-form text fields in iOS in-app message surveys are temporarily limited to 250 characters. This limitation is being addressed in a future iOS SDK update. For now, consider keeping your maximum character count at or below 250 for surveys shown to iOS users.



Long text responses are available in reporting and exports, but they can't be logged as user profile custom attributes—so you can't segment users by a long-form response value directly. See [Limitations](#limitations) for the full list.

In Currents, long-form responses use `answer_type = 'free_form_text'` with the text in `answer_long_string`.



## Randomized choice order

Radio button group, checkbox group, and dropdown blocks support randomized answer choices. Turn on **Randomize choice order** to shuffle the choices each time the survey loads, which reduces order bias when the same first option could otherwise skew responses.

Randomization changes only the display order for each survey respondent. Reporting labels and values stay mapped to the choices you configured, so analytics, CSV exports, and segmentation use the same response data regardless of the order a given user saw.

## Survey templates

Save a survey as a template from the landing page or in-app message template library so builders can start from it instead of recreating the same questions and form blocks each time. When survey templates are enabled for your workspace, filter the library by **Survey** to find and reuse saved survey structures across campaigns, Canvases, and landing pages.

## Survey Response events

Survey responses flow into [Braze Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) so you can export survey data to your data warehouse or a third-party BI tool for analysis, joins with other engagement data, and custom reporting that goes beyond the dashboard's built-in analytics.

Braze exports individual survey answers through the **Survey Response** event (`users.messages.survey.Response`). Each event represents one respondent's answer to one survey question. For the full field reference, see [Survey Response events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) in the Currents event glossary.

The same data is available as the `USERS_MESSAGES_SURVEY_RESPONSE_SHARED` SQL table in [Query Builder](https://www.braze.com/docs/user_guide/analytics/reports/query_builder), [SQL Segment Extensions](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments), and [Snowflake Data Sharing](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake). The examples in the following tabs use that table. For column details, see the [SQL table reference](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SURVEY_RESPONSE_SHARED).

The `answer_type` value matches the survey question type from the composer—for example, `single_choice`, `multiple_choice`, `free_form_text`, `nps`, `single_boolean`, or `single_number`. Use that value (not a separate response-shape enum) when filtering these queries.



Use `survey_completion_status` to see how many survey sessions were completed versus left incomplete for a given survey.

```sql
SELECT
  survey_id,
  COUNT(DISTINCT survey_session_id) AS total_sessions,
  COUNT(DISTINCT CASE WHEN survey_completion_status = 'complete' THEN survey_session_id END) AS completed_sessions,
  COUNT(DISTINCT CASE WHEN survey_completion_status = 'incomplete' THEN survey_session_id END) AS incomplete_sessions
FROM USERS_MESSAGES_SURVEY_RESPONSE_SHARED
GROUP BY survey_id;
```



Use `answer_single_string` for radio button, dropdown, and other single-choice responses (`answer_type = 'single_choice'`). Group by `question_reporting_id` rather than display position, because randomized choice order doesn't affect how responses are reported.

```sql
SELECT
  question_reporting_id,
  answer_single_string AS choice,
  COUNT(*) AS response_count
FROM USERS_MESSAGES_SURVEY_RESPONSE_SHARED
WHERE answer_type = 'single_choice'
GROUP BY question_reporting_id, answer_single_string
ORDER BY question_reporting_id, response_count DESC;
```



Use `answer_multiple_strings` for checkbox group responses where a respondent can select more than one choice (`answer_type = 'multiple_choice'`). Selected values are stored as a JSON array string (for example, `["Option A","Option C"]`).

```sql
SELECT
  question_reporting_id,
  answer_multiple_strings,
  COUNT(*) AS response_count
FROM USERS_MESSAGES_SURVEY_RESPONSE_SHARED
WHERE answer_type = 'multiple_choice'
GROUP BY question_reporting_id, answer_multiple_strings;
```



Use `answer_single_boolean` for single checkbox blocks (`answer_type = 'single_boolean'`).

```sql
SELECT
  question_reporting_id,
  answer_single_boolean,
  COUNT(*) AS response_count
FROM USERS_MESSAGES_SURVEY_RESPONSE_SHARED
WHERE answer_type = 'single_boolean'
  AND question_reporting_id = 'REPLACE_WITH_YOUR_QUESTION_REPORTING_ID'
GROUP BY question_reporting_id, answer_single_boolean;
```



NPS block responses use `answer_type = 'nps'` with the score in `answer_single_number` (and optional free-text feedback in `answer_single_string`). Rating (number scale) questions use `answer_type = 'single_number'` with the score in `answer_single_number`.

Promoter, passive, and detractor segments appear in the survey analytics dashboard. They aren't separate fields in the SQL table—derive them from the 0–10 score when you need them in Query Builder or Snowflake:

```sql
SELECT
  question_reporting_id,
  CASE
    WHEN answer_single_number >= 9 THEN 'promoter'
    WHEN answer_single_number >= 7 THEN 'passive'
    ELSE 'detractor'
  END AS nps_segment,
  COUNT(*) AS response_count
FROM USERS_MESSAGES_SURVEY_RESPONSE_SHARED
WHERE answer_type = 'nps'
  AND question_reporting_id = 'REPLACE_WITH_YOUR_NPS_QUESTION_REPORTING_ID'
GROUP BY question_reporting_id, nps_segment;
```



Use `answer_long_string` for long-form text capture responses (`answer_type = 'free_form_text'`). These are free-text values, so consider your own PII handling policy before exporting them.

```sql
SELECT
  survey_id,
  question_id,
  question_reporting_id,
  response_id,
  answer_long_string AS response_text,
  time
FROM USERS_MESSAGES_SURVEY_RESPONSE_SHARED
WHERE answer_type = 'free_form_text'
  AND question_reporting_id = 'REPLACE_WITH_YOUR_QUESTION_REPORTING_ID';
```



Landing page survey responses include a populated `landing_page_api_id`. In-app message survey responses use campaign or Canvas identifiers (`campaign_api_id` or `canvas_api_id` and related variation and step fields) instead.

```sql
SELECT
  CASE WHEN landing_page_api_id IS NOT NULL THEN 'landing_page' ELSE 'in_app_message' END AS channel,
  COUNT(DISTINCT survey_session_id) AS sessions
FROM USERS_MESSAGES_SURVEY_RESPONSE_SHARED
GROUP BY 1;
```



## Landing page events

Landing page surveys also generate **Landing Page Impression** and **Landing Page Click** events for page views and tracked clicks. Completing a landing page survey writes a **Survey Response** event; it doesn't also fire the generic **Landing Page Form Submission** event, which is for standard (non-survey) landing page forms. For the full field reference for these events, see the [Currents event glossary](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

**Note:**


Landing Page Impression events are anonymous, so you can't join them to **Survey Response** or **Landing Page Form Submission** on `user_id` to calculate response or conversion rates.





Braze exports a **Landing Page Click** event (`users.messages.landingpage.Click`) each time a user clicks a tracked element or form field on a landing page. The `target` field identifies which element was clicked—not just that a click happened—so you can compare click volume by element. For the full field reference, see [Landing Page Click events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#landing-page-click-events).

```sql
SELECT
  landing_page_name,
  target,
  COUNT(*) AS clicks
FROM USERS_MESSAGES_LANDINGPAGE_CLICK_SHARED
GROUP BY landing_page_name, target
ORDER BY clicks DESC;
```

Use this query to compare click volume across tracked elements on the same page—for example, to see that one call-to-action earns several times the clicks of another—or to feed `target` values into a CDP or ad platform to retarget users who clicked a specific offer.



Braze exports a **Landing Page Form Submission** event (`users.messages.landingpage.FormSubmission`) when a user completes a standard (non-survey) landing page form. This event records that a form was submitted, not the individual field values, so treat it as a conversion event rather than a source of response data. Survey completions use **Survey Response** instead.

```sql
SELECT
  landing_page_name,
  COUNT(*) AS submissions
FROM USERS_MESSAGES_LANDINGPAGE_FORMSUBMISSION_SHARED
GROUP BY landing_page_name
ORDER BY submissions DESC;
```

Sync submitters to a CRM or email service provider as leads, or use the event to trigger a follow-up welcome or nurture flow as soon as someone submits.



## Limitations {#limitations}

These limits apply to Braze surveys built with the drag-and-drop editor on landing pages and in-app messages (select **Survey** as the message type). They don't describe third-party survey partners or the older [Simple Survey](https://www.braze.com/docs/user_guide/channels/in_app_messages/message_types/simple_survey) template in the traditional in-app message editor.

| Topic | Support |
| --- | --- |
| Answer-based branching or skip logic | Not supported. You can't show or hide later questions based on a previous answer. Use [multi-step landing page forms](#multi-step-landing-page-forms) or the in-app message page manager only for a fixed page order. |
| Maximum checkbox selections | Supported. On a **Checkbox group** block, set **Maximum Choices** (and optionally **Minimum Choices** when the field is required) in the properties panel. For property details, see [Drag-and-drop editor blocks](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks). |
| Maximum choices per question | Radio button group and checkbox group blocks support up to 25 choices each. |
| Questions per survey | Up to 100 questions per survey. |
| Long-form text | Up to 1,000 characters (250 on iOS in-app message surveys). Long-form responses can't be logged as custom attributes. |
| Embedding a survey on an external website | There is no standalone survey embed or iframe widget. Publish a [landing page survey](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys) and link to its URL, or deliver an [in-app message survey](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys) through the Braze Web SDK. |
| Retargeting by individual answer values | Survey answers aren't available as segment filters or campaign triggers on their own. To retarget by what someone answered, [log the response as a custom attribute](#completion-data). You can also filter or trigger on survey completion. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Survey limitations" }

Channel pages also list channel-specific limits under [Limitations](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys#limitations).

## NPS from email

Email doesn't host a full Braze survey. To collect an NPS score in email, use the [email NPS Survey block](https://www.braze.com/docs/user_guide/channels/email/drag_and_drop/nps_survey). The score is recorded on a linked survey landing page where respondents can finish related follow-up questions.

## What gets recorded on survey completion {#completion-data}

When someone answers a drag-and-drop survey, Braze can write data in three places: the user profile (optional per question), survey analytics in the dashboard, and Currents (when Currents is enabled).

| Destination | What is written | Notes |
| --- | --- | --- |
| User profile | Custom attributes you configure with **Save to user profile** on each form block | Email and phone capture always save to the profile when submitted. Long-form text can't be saved as a custom attribute. |
| Survey analytics | Response counts, completion status, and per-question breakdowns | Includes complete and partially complete responses. Partial submissions have a six-hour grace period before they appear. |
| Currents **Survey Response** event (`users.messages.survey.Response`) | One event per answered question in a survey session | For the full field reference, see [Survey Response events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#survey-response-events) in the Currents event glossary. |
| Landing page engagement events | **Landing Page Impression** and **Landing Page Click** | Landing page surveys only. Completing a survey does **not** also fire **Landing Page Form Submission** (that event is for non-survey forms). |
| In-app message engagement events | Standard in-app message impression and click metrics for the campaign or Canvas step | Survey answers for drag-and-drop surveys use **Survey Response** events, not the Simple Survey `button_id` click pattern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Survey completion data destinations" }

Respondent-level exports (CSV from survey analytics, Currents, Query Builder, SQL Segment Extensions, and Snowflake Data Sharing) include the same per-question answer fields. For field definitions and example queries, see [Survey Response events](#survey-response-events).

### Map `question_id` to question labels {#map-question-ids}

Each survey question has two identifiers:

| Field | What it is | Where you set or see it |
| --- | --- | --- |
| `question_id` | Stable UUID for the question | Currents, SQL, and CSV exports. Assigned when the question is created; it doesn't change if you edit the label. |
| `question_reporting_id` | The **Identifier for reporting** value for that question | Currents and SQL. In the editor, enter **Identifier for reporting** in the block properties panel. The same value appears as the question label in survey analytics and as the CSV column header (with the UUID in parentheses). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Question ID mapping" }

To map exported `question_id` values back to human-readable labels:

1. In the editor, note each question's **Identifier for reporting**.
2. In Currents or SQL, join or filter on `question_id`, and use `question_reporting_id` (or the CSV header) as the display label.
3. Prefer grouping analytics by `question_reporting_id` or `question_id` rather than by on-page position—especially when [randomized choice order](#randomized-choice-order) is on.

## Reporting edge cases {#reporting-edge-cases}

### Removed questions

If you remove a question after the survey has collected responses:

- The question is no longer shown to new respondents.
- Prior responses remain in analytics and exports.
- Survey analytics mark the question as **Removed** and show the removal date with the historical response count.
- CSV exports prefix the column header with `[Deleted]`.

Deleted individual choices on radio button, checkbox group, and dropdown questions follow the same pattern: they're hidden from new respondents, and historical selections can still appear in reporting.

### Test submissions

Campaign and Canvas **test sends** that deliver an in-app message survey use a test tracking payload. Braze skips those submissions when writing survey response data, so they don't appear in survey analytics or Currents **Survey Response** events.

**Note:**


Submitting a published landing page survey URL in a browser (including opening the live page while QA-ing) is a real submission for the user who completes it. Use a test user profile when you need to exercise the live page without affecting production segments.



### Partial and page-level responses

- A response stays **Partially complete** until the respondent selects the final submit control—even when the only recorded answer is an NPS score from an [email NPS Survey block](https://www.braze.com/docs/user_guide/channels/email/drag_and_drop/nps_survey).
- Multi-step landing page surveys can record answers as the user moves through steps; incomplete sessions still count toward partially complete analytics after the grace period.
- Landing page impression metrics are separate from survey response metrics and aren't joined on `user_id`. For details, see [Landing page events](#landing-page-events).

## Frequently asked questions

### How do I start a survey, including NPS or CSAT?

On the message composition page for a landing page or in-app message, select **Survey** as your message type before you open the editor. NPS, CSAT, and other feedback surveys all use that same entry point into survey mode—there isn't a separate create flow per survey type. Then add the form blocks you need (for example, the [standalone NPS block](#standalone-nps-block)) in the editor.

### Where do I find surveys across channels?

Go to **Messaging** > **Surveys** to review surveys across landing pages, campaigns, and Canvases. If you don't see that page, contact your Braze account manager.

### Can I branch to different questions based on an answer?

No. Braze surveys don't support answer-based branching or skip logic. Keep a fixed question order, or split follow-up questions into a later campaign or Canvas step that targets users by a logged custom attribute.

### Can I limit how many checkboxes a user selects?

Yes. On a **Checkbox group** block, set **Maximum Choices** in the properties panel. When the field is required, you can also set **Minimum Choices**.

### How do I put a survey on my website?

Publish a landing page survey and share its URL, or show an in-app message survey to users who have the Braze Web SDK. Braze doesn't provide a separate survey iframe or embed snippet.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Landing page surveys</span><span class="guide_tile_description">Create flow, composition, and reporting for the landing pages channel</span></span></div></a></li><li><a href="/docs/user_guide/channels/in_app_messages/drag_and_drop/surveys"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">In-app message surveys</span><span class="guide_tile_description">Create flow, composition, and reporting for the in-app messages channel</span></span></div></a></li><li><a href="/docs/user_guide/channels/email/drag_and_drop/nps_survey"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Email NPS survey block</span><span class="guide_tile_description">Collect NPS scores from drag-and-drop email and finish on a landing page survey</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/editor_blocks"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Drag-and-drop editor blocks</span><span class="guide_tile_description">Full reference for the form blocks you can add to a survey</span></span></div></a></li><li><a href="/docs/user_guide/data/distribution/braze_currents"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Braze Currents</span><span class="guide_tile_description">Set up data export to your warehouse or BI tool</span></span></div></a></li></ul>
