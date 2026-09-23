# Send test Canvases

> After [creating your Canvas](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas), validate setup, audience, and content using the [Canvas QA checklist](https://www.braze.com/docs/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist). This article covers live end-to-end testing with a duplicate Canvas and API-based branch testing.

When possible, Braze recommends testing a Canvas before launching. For preview-only validation, see [Preview user paths](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/preview_user_paths) first, then return here for a live test that sends real messages through the full journey.

## Live end-to-end test (duplicate Canvas)

This method is recommended for complex journeys. Follow Phase 4 of the [Canvas QA checklist](https://www.braze.com/docs/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#phase-4-review-journey-logic-test-and-preview), then use the following steps.

### Step 1: Identify test users

Identify test users who will go through the Canvas steps without reaching your production audience. Test users can be existing email addresses that aren't used for live services on your Braze dashboard, or new email addresses used exclusively for testing.

Consider creating a [Content Test Group](https://www.braze.com/docs/user_guide/administer/global/user_management/internal_groups)—an Internal Group that receives test messages from campaigns and Canvases.

### Step 2: Duplicate and restrict entry

Create a duplicate of your Canvas for testing. In the duplicated Canvas, edit **Entry Audience** so only test users are eligible—for example, by adding an **Email Address** filter. In the following example, Canvas has been limited to two test users who have first used the app less than three days ago.

![A Canvas with an entry audience of "First used these apps less than 3 days ago" and the email addresses of two test users.](https://www.braze.com/docs/assets/img_archive/canvas_test2.png?4410d82b03178adbe89b1a67253c5698){: style="max-width:90%;"}

Reduce time delays to seconds or minutes so you can view messages quickly. Allow at least 2–3 minutes between tests to isolate specific actions to specific Canvas journeys.

### Step 3: Launch and verify

Launch your test Canvas and perform the user behaviors in your application (web, iOS, and Android) that send users through each branch.

Verify that test users receive the intended messages. Test users may not receive a message for reasons including:

- Not eligible for the Global Control Group
- Frequency capping limitations
- Mismatched segment membership
- Aborted messages
- Push tokens associated with different users

Continue to iterate until the Canvas performs as intended.

## General tips

### Identify your Canvas steps

In some cases, a user can receive multiple messages when going through a Canvas. If delays are shortened for testing, it may not be clear which message triggered. Include the step name or user ID (using Liquid) in test message titles so you can confirm the correct message reached the correct user.

### Leverage Content Blocks

If any content is going to be repeated in your testing framework (for example, complex Liquid to filter users into different Canvas steps), try saving this repeated content as a [Content Block](https://www.braze.com/docs/user_guide/messaging/design_and_edit/content_blocks). Now, you can include the Content Block throughout the individual Canvas steps.

### Use Postman and the Track user endpoint

You can run tests with Postman and the [Braze Postman Collection](https://www.braze.com/docs/api/postman_collection). Use the [`/users/track` endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track) to record and track custom events and purchases for your various test users.

Sending data to the user track API requires an external ID, so add test users to an internal group in the Braze dashboard so you can investigate specific errors. 

#### Testing for multiple branches

When you're testing a Canvas with multiple branches that target users based on different attributes and events, follow this testing plan:

1. For each branch, identify the attributes and events that the user must have to be included in the Canvas journey.
2. Build those into JSON payload to be posted using the `/users/track` endpoint.

