# Decision split 

> The decision split component in Canvas allows you to deliver personalized, real-time experiences for your users.

![A Decision Split step named "Push enabled?" for users who aren't push enabled and users who are push enabled.](https://www.braze.com/docs/assets/img/decision-split-1.png?8002d9565dec54ca88f7c5bcc96f7667){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

This component can be used to create Canvas branches based on whether a user matches a query.

## Create a decision split 

To create a decision split in your workflow, add a step to your Canvas. Then, drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Decision Split**.

### Define your split

How do you want to split your users? You can use [segments](https://www.braze.com/docs/user_guide/audience/segments) and filters to draw the line. Essentially, you're creating a `true` or `false` query that evaluates your users and then funnels them to one step or another. You must use at least one segment or one filter. You do not need to use both a segment and a filter.

![A Decision Split step with the filter "Foreground Push Enabled is true" selected.](https://www.braze.com/docs/assets/img/define-split-2.png?35e36b85eb7f9a4b24431fd111521c99)

**Note:**

 
By default, segments and filters for a Decision Split step are checked right after receiving a previous step, unless you add a delay. 



#### Retargeting filters in Canvases with re-entry

Retargeting filters in a Decision Split step, such as `Clicked/Opened Step In This Canvas`, evaluate engagement across all Canvas entries for a user, including prior entries. For example, if a user interacted with a step during a previous entry, the Decision Split recognizes that interaction when they re-enter the Canvas.

For Canvases with re-entry enabled, use an [Action Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/action_paths/) step with the **Interact with Step** trigger when you need to evaluate engagement only during the current Canvas entry within a time window. Action Paths count only interactions that occur during the step's evaluation window.

## Use your split

Use a Decision Split to send users down different paths based on segments, attributes, or channel eligibility—for example, whether they can receive push.

For example, Steppington, a fictional fitness brand, uses a Decision Split in its onboarding Canvas. After a welcome email, the Canvas asks **Push enabled?** with the filter **Foreground Push Enabled** is `true`:

- **Yes:** Users wait one day, receive a push, wait two more days, then receive a Day 3 email.
- **No:** Users wait three days, then receive the same Day 3 email.

Both paths reach the Day 3 email about three days after the split. You can also add an in-app message on the No path to encourage users to enable push.

If there is no step following one of the paths, users who go down that path exit the Canvas.

![A Decision Split step named "Push enabled?" for users who aren't push enabled and those who are. For users who aren't push enabled, they experience a 3-day delay then receive an email message. For users who are push enabled, they experience a 1-day delay, receive a push notification followed by a 2-day delay, then receive the same email message as the users who aren't push enabled.](https://www.braze.com/docs/assets/img/use-split-onboarding-3.png?7ed2fe220572856606d54a0a1829f46f){: style="max-width:60%"}

## Analytics

Refer to the following table for descriptions of analytics for this step:

| Metric | Description |
|---|---|
| _Entered_ | The total number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Decision Split step twice, two entries are recorded. |
| _Yes_ | The number of entries that met the specified criteria and proceeded down the "yes" path. |
| _No_ | The number of entries that did not meet the specified criteria and proceeded down the "no" path. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Analytics" }
