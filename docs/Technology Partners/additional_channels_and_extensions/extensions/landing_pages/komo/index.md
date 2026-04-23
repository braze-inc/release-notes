# Komo

> [Komo](https://komo.tech/) is a customer engagement platform specializing in gamification, interactive content, competitions, prizing, and loyalty.

_This integration is maintained by Komo._

## About the integration

The Braze and Komo integration allows you to gather first and zero-party data through Komo Engagement Hubs. These hubs are dynamic microsites that offer interactive content and gamification features. The user data collected from these hubs are then transmitted to the Braze API.

- Ingest first and zero-party user data gather from Komo to Braze in real-time
- Ingest market research and user preference data when they answer surveys, polls, and quiz questions
- Progressively build user profiles in Braze over time as the user continues to engage and share more data about themselves
- Standardize the look and feel of transactional emails sent through Braze

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Komo account | You will need an active Komo account to take advantage of this partnership. Visit [Komo](https://komo.tech/) to start a trial now. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL](https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.<br><br>For example, it should look something like: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Use cases




When a user submits a customizable data capture form in Komo, the Komo fields mapped in the Braze integration will be passed to Braze via the `/users/track/` API call.

Data capture forms exist either at the start or end of Cards.




Komo also enables the ability to pass through market research data captured when a user answers a quiz question, poll, personality test, swiper, and similar. This data will enable you to enhance a user's profile beyond data captured in form submissions.




## Integration

### Step 1: Publish a Komo Engagement Hub and card

You will need to publish a Komo Hub with at least one card containing a data capture form. When published, you can test the user experience end-to-end and verify the integration is working correctly.

![Komo Hub.](https://www.braze.com/docs/assets/img/Braze Komo Images v2/Braze-Komo-Step1.png?acb6d3c12d495ba2611b7239fdd6e51f)

### Step 2: Add the Braze Connected App 

In Komo, go to the **Company Settings** tab, and select the **Connected Apps** section. 

Next, find the Braze integration from the list, and select the **Connect** button to enable the integration.

![Connect Braze Integration.](https://www.braze.com/docs/assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png?9c4e4c5f5f4b6893bd77f468ed84fdb7){: style="max-width:50%;"}

![Connect Braze Integration Step 2b.](https://www.braze.com/docs/assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png?7d933236cb19512a463bc4997c2b735b)

#### Configure the integration via a Workflow

Now you need to setup a workflow, within a Workspace, Site or Card, to sync data to Braze. 

Whether you scope the workflow within the scope of the entire Workspace, a Site (which contains many Cards) or a single Card, is dependent on whether you want the workflow to trigger across many Cards or campaigns. 

After you've created a Workflow, define your trigger, search for Braze in the step menu and add the "Track User" step. 

![Track User setup.](https://www.braze.com/docs/assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png?3f7000146161b90e4f2f8ea96839c10f)

From here, configure the events, attributions, and subscriptions you want to sync from Komo to Braze. 

![Content blocks list.](https://www.braze.com/docs/assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png?a7ab0c7277dd44b34beb1bf1fbda8d73)

## Using the integration

Now your integration is up and running, and you can monitor each run in the Workflow Runs tab. 
