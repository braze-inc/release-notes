# Kubit cohort import

> This article describes how to import user cohorts from [Kubit](https://kubit.ai/) to Braze. For more information on integrating Kubit and its other functionalities, see the main [Kubit article](https://www.braze.com/docs/partners/data_and_analytics/analytics/kubit/).

## Data import integration

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Kubit**. Here, you will find the REST endpoint and generate your Braze data import key. 

Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Kubit's dashboard.

![The Kubit technology partner page in Braze.](https://www.braze.com/docs/assets/img/kubit/kubit.png?926926329e5670be306376abe1a553ce){: style="max-width:90%;"}

### Step 2: Configure Braze in Kubit

Provide the Braze data import key and Braze REST endpoint to your Kubit support contact. They will configure the integration on their side and let you know when the integration is live.  

### Step 3: Import Cohorts to Braze

#### Create a cohort in Kubit
[Create a cohort](https://www.kubit.ai/doc/fundamentals#cohort) in Kubit and define the criteria of your target users.<br><br>![](https://www.braze.com/docs/assets/img/kubit/create_cohort.png?86de9672a40933cd06885b145a01ce53){: style="max-width:80%;"}

#### Import users to Braze
Once you have saved your cohort, you can import them to Braze to be used in Braze segments. These segments can then be used to create targeted email or push campaigns and Canvases.

To do this, navigate to your existing cohort and under **Cohort Control** select **Import to Braze**.

![](https://www.braze.com/docs/assets/img/kubit/import_to_braze.png?5dc37ee389fa08f17783eb81bcebd6c8){: style="max-width:80%;"}

Next, select the desired import cadence. One-time imports allow you to import once now. Scheduled imports allow you to import daily, weekly, or monthly at a specific time. Note that each cohort can only have one live import schedule. 

![](https://www.braze.com/docs/assets/img/kubit/import_schedule.png?41768aa4f6394c2c46cb27e536e7a7a2){: style="max-width:40%;"}

**Important:**


Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.



#### Verify import status
Once an import has been completed, an email notification will be sent to the recipients(s) specified in the import schedule. You can also check a cohort's import status under **Schedule** in Kubit. The schedule history will display every import execution time, outcome, and the total number of users in the cohort who were imported to Braze.<br><br>![](https://www.braze.com/docs/assets/img/kubit/import_history.png?3ecec4dd67299d0649163a18f49c25e0)<br><br>You can manually trigger an import by clicking on **Import to Braze** icon for that import schedule.

### Step 4: Create Braze segments with Kubit cohorts
After importing cohorts to Braze, you can use them as filters to create Braze segments and include them in Braze campaigns or Canvas. Visit our segment documentation to learn more about [how to create Braze segments](https://www.braze.com/docs/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![In the Braze segment builder, the user attribute "Kubit cohorts" is set to "includes_value" and shows a list of available cohorts.](https://www.braze.com/docs/assets/img/kubit/segment_with_kubit_cohorts.png?c964daf3df2cdb54a67ae002d8bae50c){: style="max-width:70%;"}

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.