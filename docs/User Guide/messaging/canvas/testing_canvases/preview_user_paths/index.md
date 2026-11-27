# Preview user paths in Canvas

> Experience the Canvas journey you've created for your users. This includes previewing the timing and messages your users receive. These test runs act as quality assurance that your messages are sent to the right audience, all before sending your Canvas.

## Compare Canvas testing methods

Use these tables to choose a testing method. Methods differ in whether they send live messages, evaluate journey logic, and how they handle entry data, context variables, and profile updates.

| Method | What it does | Best for | Sends live messages? | Evaluates journey logic? |
| --- | --- | --- | --- | --- |
| **Test Canvas** (preview user paths) | Simulates the path for a selected user, including timing, Liquid, and step branching | End-to-end journey QA before launch | Optional (path test sends or **Send All Test Messages**) | Yes (supported steps) |
| [Composer **Preview and Test**](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/preview_personalization) | Renders one message with a selected or custom preview user | Layout and Liquid on a single Message step | Optional (composer test send) | No |
| Composer or Canvas test send (without path preview) | Sends the selected message content to internal users or Content Test Groups | Device and inbox checks | Yes | No (does not walk the Canvas path) |
| [Live test with a duplicate Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) | Launches a restricted copy so real users enter and progress | Production-like entry, delays, and delivery | Yes | Yes (full live Canvas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Compare Canvas testing methods overview" }

| Method | Entry audience and triggers | Context steps and context variables | `canvas_entry_properties` / event properties | User Update |
| --- | --- | --- | --- | --- |
| **Test Canvas** | Assumes entry criteria are met; shows why a user wouldn't qualify in production | Evaluated along the path; you can seed values before **Run Test** | Seed values Braze detects in Liquid, or leave blank | UI editor only; JSON-editor steps are skipped |
| Composer **Preview and Test** | Not applicable | Not populated from Canvas Context steps | Custom event properties only when you enter them in preview or on the **Test** tab | Not applicable |
| Composer or Canvas test send | Not applicable | Seed Groups and standalone test sends do not run Context steps for seed recipients | Depends on override and customized-user options; see [Send test messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages) | Not applicable |
| Live duplicate Canvas | Fully evaluated | Fully evaluated | Fully evaluated when users enter with real event or API payloads | Fully evaluated (including JSON editor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Compare what each Canvas testing method evaluates" }

For personalization-only checks outside the Canvas path, see [Preview personalization](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/preview_personalization). For API-based branch testing with `/users/track`, see [Send test Canvases](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/sending_test_canvases).

## Creating a test run

Follow these steps to preview your user journey:

1. Go to your Canvas builder. Resolve any validation errors that block **Test Canvas**.
2. Select **Test Canvas** in the footer.
3. If the Canvas is active and has a post-launch draft, choose **Draft changes** or **Active Canvas**.
4. If you have unsaved edits, confirm whether you need to save before the run (see [Active Canvases and unsaved changes](#active-canvases-and-unsaved-changes)).
5. Select a test user under **Preview Canvas as a User**.
6. (Optional) Enter context or entry property values if the sidebar shows **Enter context variable values**.
7. (Optional) Select test recipients if you want to send messages during the path preview.
8. Select **Run Test**.

You can run a preview if you don't have permission to edit a Canvas. Depending on your permissions, unsaved edits may be included in the run or excluded—follow the modal prompts when they appear.

### Active Canvases and unsaved changes

- **Active Canvas with a draft:** When you select **Test Canvas**, Braze asks whether to test **Draft changes** or the **Active Canvas**.
- **Unsaved changes that must be saved:** If you can edit the Canvas, Braze may require **Save and Test** so the run uses your latest edits.
- **Unsaved changes that aren't saved:** In some cases Braze continues without saving and warns that unsaved changes aren't reflected in the test run.

To include the latest draft edits in the run, save when prompted. To validate the live journey as customers see it, choose **Active Canvas**.

### Supported steps

The following steps are supported:

- Message
- Audience Paths
- Decision Split
- Delay
- Action Paths
- Experiment Paths
- Agent
- Context
- User Update (UI editor only; steps that use the JSON editor are skipped)
- Send to Destination

If the test reaches a step type that isn't listed here, Braze skips that step and the test user continues to the next supported step—unless the Canvas includes a step type that blocks testing entirely. In that case, **Test Canvas** stays disabled. See [Troubleshoot Test Canvas](#troubleshoot-test-canvas).

### Agent steps

When a test run reaches an [Agent step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/agent_step), Braze pauses and asks **Do you want to run the agent "{agentName}"?** Choose how to continue:

- **Yes:** Optionally add context in the text field (in addition to the test user's profile and any Canvas context already in the journey), then select **Simulate response** to invoke the agent. You can enter sample values in plain language—for example, describing cart contents or inbound message text—to mimic runtime context the agent would receive in production.
- **No:** Braze does not invoke the agent. The step uses the agent's configured **fallback output** from the **Output** section in [Agent Console](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents#configure-fallback-values).

When you select **Yes** and **Simulate response**, the agent runs for the preview user, stores its output in the Agent step's output variable, and the test continues down the journey. Invocations from **Simulate response** count toward the agent's daily invocation limit and appear on the agent's **Logs** tab.

To test an Agent step in isolation (without running the full Canvas path), use the in-step preview in the Canvas builder. For setup details, see [Test the agent](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/agent_step#step-5-test-the-agent) in Agent step.

If your Agent step depends on data from an upstream [Context step](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context), run **Test Canvas** so context variables are populated along the path. Seed Groups do not evaluate Context steps or context variables for seed recipients.

### Canvas step details

To view more details for the entrance criteria, select **See more**. Steps with segmentation show the met or unmet criteria. Messages also show this for delivery validations and channel eligibility. Message steps show which channels were sent versus not sent.

### Liquid

Braze processes Liquid logic during a test run, even if you're not sending an actual test message. This means the [abort message logic](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) and other Liquid logic are reflected and could impact the Canvas user journey.

If your preview sends the last step of your user journey instead of aborting, the preview may be using the current time as the time being tested for Liquid evaluation, not the actual time the user would be in the step based on the Canvas entry time.

## Previews for timing

For scheduled Canvases, the test user enters at the next scheduled entrance time. For action-based Canvases with start dates, the test user enters at the start date and time. 

While the default start times still apply, the entrance time is configurable in all instances, meaning you can simulate a date in the past or future. However, you can't test before the start date or after the end date for the Canvas.

Message and Delay steps show the time at which a user would progress or receive the message without needing to reconfigure the delays. Note that while the steps indicate whether Intelligent Timing is used, this preview of the user path does not calculate an estimate for a test user.

For Canvases with an action trigger like "change in custom attribute value," Braze attempts to simulate the change by temporarily setting the user's attribute in the trigger to be blank **only for the test run of the Canvas** (this doesn't affect the user profile). This is meant to test that the attribute changes from its current value.

## When users enter and exit

Test users enter the preview even if they aren't eligible in real life. If they aren't eligible, you can see why they haven't met the criteria. When a test user enters the preview, we assume the test user has met the target audience criteria and performed the action trigger criteria. For example, for a Canvas that uses custom events in the entry criteria, the test user is assumed to have performed the custom event as expected in the entry criteria. However, if the same custom event is used elsewhere in the Canvas (like in the exit criteria), consider how this might impact your user path.

Events, API triggers, custom attributes, and Canvas entry properties that are assumed to let a test user enter the Canvas are not updated in the actual user profile and do not persist beyond the test run. For example, during testing, when a custom attribute is used as a Canvas trigger, the trigger criteria is applied to the user's preview **as if** they had triggered the custom attribute change.

### Consideration

If you test an Action Paths step with actions that correspond to exit criteria (including event properties), the exit criteria is triggered, and the test run ends. If you test a Message step that corresponds to exit criteria, the exit criteria is triggered, and the test run ends. 

At this point, you can't select a specific event or property within an Action Paths step to trigger exit criteria (only the path as a whole). If a user could potentially meet multiple exit criteria, the first one that is processed and that they meet is shown as the result.

## Experiment Paths and Canvas variants

- For Canvases with top-level variants, select a variant at the start of the test.
- For Experiment Paths, select the variant the user progresses through when the test user encounters the step.
- For Experiment Paths using Winning Path, the preview doesn't include the delay period when a test user waits in a Message step. Braze assumes that the user progressed through the selected path immediately.

## Entry properties and context variables

When your Canvas references context variables or Canvas entry properties in Liquid—for example `{{context.${property}}}` or `{{canvas_entry_properties.${property}}}`—the **Test Canvas** sidebar can show **Enter context variable values** before you select **Run Test** or **Send All Test Messages**.

- Braze lists variables defined on Context steps, plus property names it detects in Liquid across steps.
- Enter sample values to avoid blank personalization in the preview. If you leave a value empty, Liquid that references that property can render blank or trigger abort logic.
- For object or array context variable types, enter a JSON value (for example `{"tier":"gold"}` or `["a","b"]`) that matches the variable's data type.
- Agent output variables aren't listed for manual entry; they're set when you simulate the Agent step during the run.
- Nested paths such as `order.total` appear when Liquid or Context filters reference them; enter the value for the listed name as shown in the sidebar.

This editor seeds preview context only. It doesn't write entry properties or context values to the live user profile. For production-like nested payloads on entry, use a [live duplicate Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) or send a real API-triggered entry with a JSON payload.

**Note:**


Canvas Context availability varies by workspace. If **Context** doesn't appear in your step menu, use the entry-property workflow for your workspace. For details, see [Context](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context).



## Test sends

You can opt to send test messages to an internal test group or an individual user as the test run populates. This means that only messages the user encounters along the test path are sent. The recipients receive messages with their attributes by default, but you can override these with the test user’s attributes.

To send all test messages in a Canvas at once, regardless of the path, and without previewing the path, you can select **Send All Test Messages** in the **Test Sends** tab.

## Responsiveness

Canvas steps are responsive to timing when previewing user paths. Updates made via the User Update step are reflected in subsequent steps in the flow but are not applied to the actual user profile. The effects of a user entering a variant are reflected in future steps in a preview.

Similarly, filters recognize actions that occurred as a result of the test user interacting with other steps in the Canvas. For example, this preview mode recognizes that a user encountered a Message step that was “sent” earlier in the Canvas, and it recognizes that the test user “took action” to advance through an Action Paths step.

Refer to [Exit criteria](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/exit_criteria) for more details on responsive behavior.

## Connected Content

Connected Content is executed if it’s included in the Canvas. This means if you test a Canvas that has Connected Content calls or Content Blocks that contain Connected Content, the Canvas may send the Connected Content calls, which would modify the data referenced in other campaigns or Canvases.

**Note:**


Connected Content retry logic only applies to live sends (including test sends), not to previewing user paths. If a Connected Content call with `:retry` fails during previewing user paths, Braze does not retry the call. For more information, see [Connected Content retries](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries#preview-behavior).



When previewing user paths, consider removing the Connected Content that alters user profiles or data referenced in other Canvases or campaigns.

## Webhooks

Webhooks execute when test messages are sent, but not during the test run. Similar to Connected Content, consider removing webhooks that alter user profiles or data referenced in other Canvases or campaigns.

## Context variables and Seed Groups

For a Message step with email as the messaging channel, Seed Groups send seed copies of emails when a user reaches this step in the Canvas. These seed copies are not sent as part of the Seed Group recipients' own Canvas journeys, so Braze does not execute [Context steps](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context) or evaluate context variables for those recipients. If your email content references context variables, Seed Group recipients receive a seed copy without that data populated. To test messages that rely on context variable data, use the **Test Canvas** preview with test sends instead of Seed Groups.

## View messages sent to users

Preview user paths simulates a journey; it does not replace checking actual sends on a user profile. To review messages Braze sent to a specific user, open their profile from **Audience** > **Search Users**, then use the **Messaging History** and **Engagement** tabs.

For search fields, tab details, and the 30-day Messaging History window, see [User profiles](https://www.braze.com/docs/user_guide/audience/manage_audience/user_profiles).

## Troubleshoot Test Canvas

### Test Canvas is disabled

Hover over **Test Canvas** in the footer to see why it's unavailable:

| Tooltip | What to do |
| --- | --- |
| "Errors must be fixed before testing your Canvas." | Open the error tray, resolve validation errors on steps or Canvas settings, then try again. Demo or learning-sandbox notices don't block testing. |
| "Unable to perform test due to unsupported steps." | Your Canvas includes a step type that blocks path preview. Remove or replace that step, or use a [live duplicate Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) for end-to-end testing. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Test Canvas disabled tooltips" }

### Preview aborts, looks blank, or skips personalization

- **Abort message logic:** Liquid abort conditions run during the test even when you don't send a message. Check the step result for abort reasons such as quiet hours, ineligibility, Liquid abort, template parse errors, or Connected Content retry failure.
- **Blank context or entry values:** Seed values under **Enter context variable values**, or select a preview user whose profile has the attributes your Liquid expects. Empty seeded values produce blank substitutions.
- **Time-based Liquid:** Preview may evaluate time-sensitive Liquid against the current time rather than the simulated step time. If the last step sends instead of aborting, confirm the timing used in the run.
- **User Update JSON editor:** Those steps are skipped in **Test Canvas**. Convert the update to the UI editor for path preview, or validate JSON updates with a live duplicate Canvas.
- **Seed Groups:** Seed email copies don't evaluate Context steps. Use **Test Canvas** with test sends when email content depends on context variables.

### Test send failures during a path preview

If Braze can't deliver one or more test messages during the run, a toast lists the failed sends (for example, "Unable to send # test messages"). Confirm recipients, channel eligibility, and that message steps have channel content. For channel-specific test-send requirements, see [Send test messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages).

If a Message step is missing channel content, fix the step content before launch or before relying on test sends from that step.

## Use case

In this scenario, the Canvas is set up to target users who haven't had a session in an app. This journey includes a Message step with a welcome email, a Delay step set for one day, and an Audience Paths step that splits into two paths: users with at least one session, and everyone else. Depending on which audience path a user falls into, the subsequent Message step is sent.

Because our test user meets the Canvas entry criteria, they can enter the Canvas and go through the user journey. However, because our test user hasn't opened the app in the last calendar day, they continue down the "Everyone else" path and receive a push notification that reads: "Last chance! Complete your first task for an exclusive bonus."

![The "Test Results" section shows that the test user has met the entry criteria and provides a summary of their journey, including which steps they were sent.](https://www.braze.com/docs/assets/img/preview_user_path_results_example.png?761e13808fbdaa7440b63299ab875e4d)
