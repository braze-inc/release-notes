# Heap cohort import

> [Heap](https://heap.io/), a digital insights platform, focuses you on opportunities in your digital experience that most impact your business, eliminating friction, delighting your customers, and accelerating revenue.

The Braze and Heap integration enables you to [import Heap data to Braze](#data-import-integration), create user cohorts, as well as [export Braze data to Heap](https://www.braze.com/docs/partners/data_and_analytics/analytics/heap/) to create segments.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Heap account | A [Heap](https://heap.io/about) account is required to take advantage of this partnership. |
| Braze Data Import key | This can be captured in the Braze dashboard from **Partner Integrations** > **Technology Partners** and then select **Heap**. |
| Braze REST endpoint | [Your REST endpoint URL](https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Braze Currents | In order to export data from Braze to Heap, you need [Braze Currents](https://www.braze.com/docs/user_guide/data_and_analytics/braze_currents/#access-currents) enabled on your account. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases
- Re-engage users who have abandoned a funnel: Trigger re-engagement messaging when users abandon the purchase or subscription funnel.
- Personalize the trial experience: Identify friction points in your trial experience and send correctly timed reminders to re-engage users during a trial and help them get to value.
- Drive higher engagement on announcements and offers: Target promotions, updates, and new service announcements to the relevant audiences.

## Data import integration

Use the Heap to Braze integration to automatically sync cohorts defined in Heap to Braze.

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and then select **Heap**. 

On this page, you can find your data import key and a REST endpoint. Take note of both of these values and provide them to your Heap account manager to finish setting up the integration.

![](https://www.braze.com/docs/assets/img/heap/heap2.png?e038c4b5f7f419b47487b9013b132eea){: style="max-width:90%;"}

### Step 2: Segment imported users in Braze

In Braze, navigate to **Segments**, name your Heap cohort segment, and select **Heap Cohorts** as your filter. From here, you can choose which Heap cohort you wish to include. After your Heap cohort segment is created, you can select it as an audience filter when creating a campaign or Canvas.

![In the Braze segment builder, the user attributes filter "Heap cohort" is set to "includes" and "Heap Test Cohort".](https://www.braze.com/docs/assets/img/heap/heap1.png?c7d54e311a1b100e79852251abb3a70b){: style="max-width:90%;"}

### Using this integration

To use your Heap segment, create a Braze campaign or Canvas and select the segment as your target audience.

![In the Braze campaign builder on the targeting step, the "Target users by segment" filter is set to "Heap cohort".](https://www.braze.com/docs/assets/img/heap/heap3.png?6fe0250113f4c95f7a849e88440bbb6d){: style="max-width:90%;"}

**Important:**


Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.



## Integration details

The payload structure for exported data is the same as the payload structure for custom HTTP connectors, which can be viewed in the [examples repository for custom HTTP connectors](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

