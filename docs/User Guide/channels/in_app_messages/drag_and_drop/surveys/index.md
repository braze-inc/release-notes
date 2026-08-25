# In-app message surveys

> Braze surveys collect feedback in in-app messages that you can analyze and use in follow-up messaging. Surveys are built in the [drag-and-drop editor](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop).



For an overview of Surveys and the capabilities shared across channels, see [Surveys](https://www.braze.com/docs/user_guide/messaging/surveys).

## Prerequisites

Before creating a survey, you must:


- Have access to landing pages, in-app messages, or both in your Braze workspace
- Be familiar with [creating landing pages](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/) and [creating in-app messages in the drag-and-drop editor](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/)


## Create a survey

Surveys are built inside your existing message composition flow.


1. Go to **Messaging** > **Landing Pages**, or create an [in-app message](https://www.braze.com/docs/user_guide/channels/in_app_messages/drag_and_drop/) in a campaign or Canvas.
2. Create a new message.
3. Select **Survey** as your message type.




## Use survey form blocks

For shared styling and composition controls, see:


- [In-app message drag-and-drop editor blocks](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)
- [Landing page form blocks](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages)


You can add the following form blocks to surveys:

- Phone capture
- Email capture
- Radio button group
- Short text capture
- Long text capture
- Dropdown
- Single checkbox
- Checkbox group
- Rating scale
- NPS

### Randomize answer choices

Radio button group, checkbox group, and dropdown blocks support randomized answer choices. Turn on **Randomize choice order** to shuffle the choices each time the survey loads. For more information, see [Randomized choice order](https://www.braze.com/docs/user_guide/messaging/surveys#randomized-choice-order).

### Long text capture

Long text capture is useful for qualitative feedback, up to 1,000 characters. For more information, see [Long-form text capture](https://www.braze.com/docs/user_guide/messaging/surveys#long-form-text-capture).

### Rating scale

Rating scale (also called a number scale question) is useful for capturing sentiment, satisfaction, or likelihood to recommend as a single number. For more information, see [Number scale questions](https://www.braze.com/docs/user_guide/messaging/surveys#number-scale-questions).


![Rating scale to give likelihood of recommending product to a friend from 1 to 10.](https://www.braze.com/docs/assets/img/surveys/landing_page_rating_scale_example.png?eeb3565e4c7192a17a872ad702c884ea){: style="max-width:70%;"}


## Configure required fields and attributes

For each form block, enter an **Identifier for Reporting** in the right-side settings panel. This identifier appears in survey reporting and CSV exports.

Keep in mind:

- You can log most survey responses to user profile custom attributes.
- Long text responses can't be logged as custom attributes.
- If you choose not to log a response as a user attribute, you can't segment users by that response value.

![Identifier for reporting and attribute logging settings.](https://www.braze.com/docs/assets/img/surveys/reporting-id-surveys.png?e966bcb391751de783085c1c2c6ac02a){: style="max-width:40%;"}

## View reporting and analytics

After launch, review results in:


- The **Responses** tab for in-app message surveys
- The landing page analytics view for landing page surveys


For definitions of the top-level analytics available for every survey (all responses, completed, partially complete, and unique impressions), see [Analytics](https://www.braze.com/docs/user_guide/messaging/surveys#analytics).



You can also review per-question response breakdowns, choose among three chart types, and export data as CSV. For more information, see [Chart types](https://www.braze.com/docs/user_guide/messaging/surveys#chart-types).

## Retarget and trigger

You can:

- Segment users by survey responses that are logged as user attributes.
- Segment users by survey completion status.



![Trigger setup and segmentation filters for survey follow-up.](https://www.braze.com/docs/assets/img/surveys/submit-survey-segment.png?67c763c098988fc9b52ecb9badc2068a)

- Trigger campaigns and Canvases when a user completes a survey in a landing page or an in-app message campaign.

![Trigger setup and segmentation filter for landing page survey follow up.](https://www.braze.com/docs/assets/img/surveys/trigger_landing_page_survey.png?ad61dccea1ce74a97085115769c7ec40)

![Trigger setup and segmentation filter for in-app message campaign survey follow up.](https://www.braze.com/docs/assets/img/surveys/interact-campaign-step.png?8f917ac4c1c067620c4aeb4e495d58c5)



### Limitations

You're restricted by the following:

- You can't segment users by long-form text responses.
- Question-and-answer triggering that does not rely on logged user attributes is not available.

