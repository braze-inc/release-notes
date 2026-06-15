# Landing page surveys

> Braze surveys collect feedback on landing pages that you can analyze and use in follow-up messaging. During beta, surveys are built in the [landing page drag-and-drop editor](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/).





**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





## Prerequisites

Before creating a survey, you must:


- Have access to landing pages, in-app messages, or both in your Braze workspace
- Be familiar with [creating landing pages](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/) and [creating in-app messages in the drag-and-drop editor](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/)


## Create a survey

During early access, surveys are built inside your existing message composition flow.


1. Go to **Messaging** > **Landing Pages**, or create an [in-app message](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/) in a campaign or Canvas.
2. Create a new message.
3. Select **Survey** as your message type.




## Use survey form blocks

For shared styling and composition controls, see:


- [In-app message drag-and-drop editor blocks](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Landing page form blocks](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/#form-blocks)


You can add the following form blocks to surveys:

- Phone capture
- Email capture
- Radio button group
- Short text capture
- Long text capture
- Dropdown
- Single checkbox
- Checkbox group

### Long text capture

Long text capture is useful for qualitative feedback.

You can configure:

- Minimum and maximum character counts (up to 1,000)
- Whether to show character limits during composition
- Text area height (rows)
- Placeholder text

During early access, long text responses are available in reporting and exports, but they can't be logged as user profile custom attributes.

![Long text capture block settings.](https://www.braze.com/docs/assets/img/surveys/long-form-surveys.png?92db595db8a8cbd42cf1afbf62b4aabd){: style="max-width:40%;"}

## Configure required fields and attributes

For each form block, enter an **Identifier for Reporting** in the right-side settings panel. This identifier appears in survey reporting and CSV exports.

During early access:

- You can log most survey responses to user profile custom attributes.
- Long text responses can't be logged as custom attributes.
- If you choose not to log a response as a user attribute, you can't segment users by that response value.

![Identifier for reporting and attribute logging settings.](https://www.braze.com/docs/assets/img/surveys/reporting-id-surveys.png?e966bcb391751de783085c1c2c6ac02a){: style="max-width:40%;"}

## View reporting and analytics

After launch, review results in:


- The **Responses** tab for in-app message surveys
- The landing page analytics view for landing page surveys


![Landing page analytics tab.](https://www.braze.com/docs/assets/img/surveys/survey-analytics-1.png?c74df670cb15e1fd920839103fffa994)

Top-level analytics include:

- **All responses:** Total complete and incomplete responses
- **Completed:** Users who completed all required questions
- **Partially complete:** Users who submitted some data, but did not complete all required questions
- **Unique impressions:** Total page views



You can also review per-question response breakdowns and export data as CSV.

### Choose a chart type

For radio button, dropdown, and checkbox form blocks, you can choose among three chart types in the survey analytics view. This gives you more flexibility to interpret and share insights without exporting to a third-party tool.

| Chart type | Best for |
| --- | --- |
| Bar chart | The default horizontal view of response counts and percentages. |
| Column chart | A vertical view of response counts and percentages. Use this chart to compare responses side-by-side, especially for multi-select questions or questions with more answer options. |
| Pie chart | A proportional breakdown of responses. Use this chart for single-select questions when you want to see how responses are distributed across options. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Survey chart types" }

Each chart updates in real time as responses come in. You can switch chart types at any time without affecting the underlying data.

![Survey question-level breakdown using a bar chart.](https://www.braze.com/docs/assets/img/surveys/bar-charts-1.png?7b179c4e582b7a8e489b618dc5746236)

## Retarget and trigger

During early access, you can:

- Segment users by survey responses that are logged as user attributes.
- Segment users by survey completion status.



![Trigger setup and segmentation filters for survey follow-up.](https://www.braze.com/docs/assets/img/surveys/submit-survey-segment.png?67c763c098988fc9b52ecb9badc2068a)

- Trigger campaigns and Canvases when a user completes a survey in a landing page or an in-app message campaign.

![Trigger setup and segmentation filter for landing page survey follow up.](https://www.braze.com/docs/assets/img/surveys/trigger_landing_page_survey.png?ad61dccea1ce74a97085115769c7ec40)

![Trigger setup and segmentation filter for in-app message campaign survey follow up.](https://www.braze.com/docs/assets/img/surveys/interact-campaign-step.png?8f917ac4c1c067620c4aeb4e495d58c5)



### Limitations

During early access, you are restricted by the following:

- You can't segment users by long-form text responses.
- Question-and-answer triggering that does not rely on logged user attributes is not available.

