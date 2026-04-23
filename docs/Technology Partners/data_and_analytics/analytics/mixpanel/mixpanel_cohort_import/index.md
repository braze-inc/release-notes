# Mixpanel cohort import

> This article describes how to import user cohorts from [Mixpanel](https://mixpanel.com/) to Braze. For more information on integrating Mixpanel and its other functionalities, see the main [Mixpanel article](https://www.braze.com/docs/partners/data_and_analytics/analytics/mixpanel/).

## Data import integration

Any integration you set up will log data points. If you have any questions about the nuances of Braze data points, your Braze account manager can answer them.

**Important:**


In adherence to Mixpanel's data retention policies, events sent before January 1, 2010 will be removed during import.



### Step 1: Get the Braze data import key

In Braze, go to **Partner Integrations** > **Technology Partners** and select **Mixpanel**. Here, you will find the REST endpoint and generate your Braze data import key. 

Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Mixpanel's dashboard.<br><br>![](https://www.braze.com/docs/assets/img_archive/currents-mixpanel-edit.png?5e459c9172ed061eccb0ba20a773eb81)

### Step 2: Set up the Braze integration in Mixpanel

1. In Mixpanel, go to **Data Management > Integrations.** 
2. Select the Braze integration tab and select **Connect**. 
3. In the prompt that appears, provide the Braze data import key and REST endpoint.
4. Select **Continue**.

![](https://www.braze.com/docs/assets/img_archive/mixpanel2.png?09ffeb7c342422ec102bc508a79cb62b){: style="max-width:50%;"}

### Step 3: Export a Mixpanel cohort to Braze

In Mixpanel, go to **Data Management > Cohorts**. Select the cohort to send to Braze and then select **Export to Braze**. Lastly, select a one-time sync or dynamic sync. Selecting dynamic sync keeps the cohort updated on a recurring schedule controlled by Mixpanel. For the latest sync cadence, see [Mixpanel's Braze cohort sync documentation](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).

![](https://www.braze.com/docs/assets/img_archive/mixpanel3.png?ddb4d40231ba31da10031fdc016101d3){: style="max-width:50%;"}

**Important:**


Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.



### Step 4: Segment users in Braze

In Braze, to create a segment of these users, go to **Audience** > **Segments**, name your segment, and select **Mixpanel_Cohorts** as the filter. Next, use the "includes" option and choose the cohort you created in Mixpanel. 

![In the Braze segment builder, the user attributes filter "Mixpanel cohorts" is set to "includes" and "Braze cohort".](https://www.braze.com/docs/assets/img_archive/mixpanel1.png?8fa0d351236f3a90ac0e92793d2af3f7)

After saving, you can reference this segment during Canvas or campaign creation in the targeting users step.

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

## Troubleshooting

If a Mixpanel cohort sync looks incomplete or doesn't update for certain users, see [Troubleshooting](https://www.braze.com/docs/partners/data_and_analytics/analytics/mixpanel/#troubleshooting) on the main Mixpanel article.

For connector-specific steps and sync cadence, see [Mixpanel's Braze cohort sync documentation](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).