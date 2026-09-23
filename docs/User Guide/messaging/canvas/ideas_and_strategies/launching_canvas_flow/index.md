# Launch with Canvas Flow

> This reference article covers how to prepare and test a Canvas built using Canvas Flow before launch. This includes identifying important Canvas checkpoints such as Canvas entry conditions, audience summaries, and user segments.

As you prepare to launch your Canvas, Braze recommends that you check your Canvas at each stage of the Canvas builder for settings that can impact your message sending, including:
* [Race conditions](#race-conditions)
* [Delivery times](#delivery-times)
* [User segments](#segment-users)

## Race conditions 

Consider the [race conditions](https://www.braze.com/docs/user_guide/messaging/ab_testing/concepts/race_conditions) that may occur before launching your Canvas. 

To enter a Canvas, users must be in the entry audience before the entry schedule occurs regardless of whether the Canvas is scheduled, action-based, or API-triggered. 

![An Action-Based Canvas that enters users when they make any purchase during a user's local time from April 30, 2025 at 12 pm to May 7, 2025 at 12 pm.](https://www.braze.com/docs/assets/img_archive/launch_with_canvas_flow_example.png?f5f34302d27905223218d9557a14b26f){: style="max-width:75%;"}

Note that users who qualify for your entry audience after the Canvas launches will not enter the Canvas.

**Tip:**


Check out [Entry schedule types](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) for guidance and details for when to use scheduled, action-based, or API-triggered delivery for your Canvas!



### Review entry audience filters

In general, avoid configuring an action-based or API-triggered Canvas with the same trigger as the audience filter. For example, after a Canvas is launched, users who perform a specific action will be included in the entry audience, so there's no need to add the event as an audience filter. 

For more details on available segmentation filters to target your audience, see [Segmentation Filters](https://www.braze.com/docs/user_guide/audience/segments/segmentation_filters).

### Batch multiple API requests

Make your requests in the same API call, rather than multiple calls, to confirm that the user profile is created or updated first. Refer to [Using multiple endpoints](https://www.braze.com/docs/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-2-using-multiple-api-endpoints) for more examples.

### Add a delay

Another option to avoid race conditions is to use the Delay step (ideally set for 5 minutes) as the first step of your Canvas. 

This allows time for attributes, email addresses, and push tokens to be processed to new user profiles before they're targeted for the following Canvas steps. Without this Delay step, it's possible for an email to be sent to a user whose email hasn't been updated yet.

## Delivery times

Setting a Canvas delivery time in real-time can lead to increasing engagement and conversion rates. Take note of which delivery time you've set for your Canvas. To help increase engagement and conversion rates, it's best to trigger Canvases in real-time instead of on a scheduled, recurring basis.

If you selected a scheduled delivery for your Canvas, Braze recommends scheduling your Canvas at least 24 hours before you want it to launch to allow for any adjustments to your Canvas.

## User segments

Before oversaturating your Canvas Flow user journey with components, consider how you might keep a user journey simple. Use the simplified view in the Canvas editor to get a better idea of how your user journey branches. 

There are four main components you can use to segment your users in a simple, effective manner:

* [Audience Paths](#audience-paths)
* [Decision Split](#decision-split)
* [Action Paths](#action-paths)
* [Experiment Paths](#experiment-paths)

### Audience Paths

Use [Audience Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/audience_paths) steps to segment users within the Canvas based on custom attributes, custom events, and previous message engagement data from user profiles.

### Decision Split

The [Decision Split](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/decision_split) step allows you to send your users to different user journey paths based on their answers to a polar question.

### Action Paths

[Action Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/action_paths) focus on segmenting users based on real-time behaviors such as custom events, purchase events, and custom attribute changes. 

### Experiment Paths

Similar to Action Paths, you can leverage [Experiment Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/experiment_step) steps in your Canvas to test multiple Canvas paths against each other, along with a control group. This tracks path performance, allowing you to make informed decisions when building your Canvas journey. 

## Testing before launch

After reviewing the finer details of your Canvas, work through the [Canvas QA checklist](https://www.braze.com/docs/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist) for setup, audience, content, and journey validation. 

For live end-to-end testing with duplicate Canvases and API-based branch testing, see [Send test Canvases](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/sending_test_canvases).

## Troubleshooting

**Why are my users not receiving my Canvas messages?**


For pre-launch checks, see the [Canvas QA checklist](https://www.braze.com/docs/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist)—especially Phase 2 (audience and targeting) and Phase 5 (post-launch monitoring). For a deeper investigation path after go-live, see [Troubleshoot Canvases](https://www.braze.com/docs/user_guide/messaging/canvas/troubleshooting).


