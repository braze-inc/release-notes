# Amplitude cohort import

> This article covers how to import user cohorts from [Amplitude](https://amplitude.com/) to Braze. For more information on integrating Amplitude and its other functionalities, see the main [Amplitude article](https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Data import integration

Any integration you set up will count toward your account's data point volume.

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Amplitude**. Here, you will find the REST endpoint and generate your Braze data import key. 

Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Amplitude's dashboard.<br><br>![](https://www.braze.com/docs/assets/img/amplitude3.png?38b3dc2b3f9bde4d55eae3d00cb1fc64)

### Step 2: Set up the Braze integration in Amplitude

In Amplitude, navigate to **Sources & Destinations** > **[project name]** > **Destinations** > **Braze**. In the prompt that appears, provide the Braze data import key and REST endpoint, and click **Save**.

![](https://www.braze.com/docs/assets/img/amplitude.png?06f71e4a43cba36dc31e7b27d1eff321)

### Step 3: Export an Amplitude cohort to Braze

First, to export users from Amplitude to Braze, create a [cohort](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) of users you wish to export. Amplitude can sync cohorts to Braze using the following identifiers:
- User Alias
- Device ID
- User ID (External ID)

You can set up multiple Braze connections in your Amplitude account. This allows you to configure one connection to sync user IDs for known users and another to sync device IDs for anonymous users.

Once you have created a cohort, click **Sync to...** to export these users to Braze.

**Important:**


Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.



#### Defining sync cadence

Cohort syncs can be set to be one-time sync, scheduled as daily or hourly, or even real-time which updates every minute. 

Any integration you set up will log data points. If you have any questions about the nuances of Braze data points, your Braze account manager can answer them.

### Step 4: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement**, name your segment, and select **Amplitude Cohorts** as the filter. Next, use the "includes" option and choose the cohort you created in Amplitude. 

![In the Braze segment builder, the filter "amplitude_cohorts" is set to "includes_value" and "Amplitude cohort test".](https://www.braze.com/docs/assets/img/amplitude2.png?c16db929f9b372382754bdb88d8b70e0)

After saving, you can reference this segment during Canvas or campaign creation in the targeting users step.

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.
