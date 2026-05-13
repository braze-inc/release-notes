# OneTrust

> [OneTrust](https://www.onetrust.com/) is a privacy and security software provider providing the visibility you need to better understand your trust landscape, action to leverage powerful insights, and automation to keep you elevated from the competition. 

_This integration is maintained by OneTrust._

## About the integration

The Braze and OneTrust integration allows you to use the OneTrust workflow builder to create security workflows for your product.
## Prerequisites

| Requirements | Description |
|---|---|
| OneTrust account | A [OneTrust](https://www.onetrust.com/) account to take advantage of this partnership. |
| Braze API key | A Braze REST API key with permissions required for the endpoint your OneTrust action will use.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the [API overview page](https://www.braze.com/docs/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

The following integration provides guidance on creating a user consent update workflow and a user delete workflow. For more details on additionally supported Braze endpoints, refer to [Other supported actions](#Other-supported-actions).

### Add Braze credentials to OneTrust

In the OneTrust **Integrations** menu, Navigate to **Credentials** > **Add New** button to bring up the **Select System** screen. Here, find **Braze**, then click the **Next** button.

Follow the prompts in the **Enter Credential Details** screen and provide the following information. Save your credentials when complete.
  - Credential name
  - Set the connector type to **Web App**
  - Hostname: `<your-braze-instance-url>`
  - **Request Header**:
    - **Authorization**: Bearer
    - **Content-Type**: application/json
  - Token: `<your-braze-api-key>`

### Add Braze as a system

#### Step 1: Create a workflow



1. In the OneTrust integrations menu, navigate to **Gallery** > **Braze** > **Add** to create a new workflow.![](https://www.braze.com/docs/assets/img/onetrust/onetrust.png?d5234b0c5f449c698a89802486754fa1)<br><br>
2. Provide a name and notification email in the workflow modal. Click the **Create** button. On creation, you will be taken to the Workflow Builder. Your Braze workflow will be seeded with API calls and actions that can be used to process deletion requests. <br><br>
3. In the Workflow Builder, choose the action you want to trigger in the workflow.<br>![](https://www.braze.com/docs/assets/img/onetrust/onetrust2.png?b4d126caea8f2d1ea845cfe4fcefe732)




1. In the OneTrust integrations menu, navigate to **Gallery** > **Braze** > **Add** to create a new workflow.![](https://www.braze.com/docs/assets/img/onetrust/onetrust.png?d5234b0c5f449c698a89802486754fa1)<br><br>
2. Provide a name and notification email in the workflow modal. Click the **Create** button. On creation, you will be taken to the Workflow Builder. Your Braze workflow will be seeded with API calls and actions that can be used to process deletion requests. <br><br>
3. In the Workflow Builder, choose the action you want to trigger in the workflow.<br>![](https://www.braze.com/docs/assets/img/onetrust/onetrust8.png?477b85b120d4bf1e2332c08aae2fdfe8)



#### Step 2: Select action



1. When complete, click **Done** and choose **Add Action**. Note that the action you choose will depend on what type of preference is being updated and your preferred endpoint.
- To update a user’s global subscription preferences, choose the **POST User track - attributes** action.
- To update a user’s subscription group preferences, choose the **POST User Track - Attributes** action or the **POST Set Users Subscription Group Status** action.<br>![](https://www.braze.com/docs/assets/img/onetrust/onetrust4.png?98fc1d0a4af38c7b030131b51944e005)<br><br>
2. Choose your desired Action, select your previously created Braze credentials, and click **Next**.<br>![](https://www.braze.com/docs/assets/img/onetrust/onetrust5.png?05e2b5d9c6bf6a2b0d6e99f95d1af769)




1. When complete, click **Done** and choose **Add Action**.
- To delete a user from Braze, choose the **POST User Delete Action** action.
<br>![](https://www.braze.com/docs/assets/img/onetrust/onetrust9.png?4390a68ff02f43c68d0ce2e3b2ae9235)<br><br>
2. Choose your desired Action, select your previously created Braze credentials, and click **Next**.<br>![](https://www.braze.com/docs/assets/img/onetrust/onetrust5.png?05e2b5d9c6bf6a2b0d6e99f95d1af769)



#### Step 3: Update request body



1. Update the body to include any necessary dynamic values. Make sure the body of the action matches the [`/users/track` endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) and the [`/subscription/status/set` endpoint](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).
2. Customize the workflow with additional parameters or conditional logic to meet your organization's needs.
3. When finished editing, click **Finish** and then **Activate** to enable the workflow.

**Note:**


When using the OneTrust workflows to update subscription group preferences in Braze, the `subscription_group_id` must match the ID set by Braze when the subscription group was created. You can access a subscription group’s `subscription_group_id` by navigating to the **Subscription Group** page in the Braze dashboard.



![](https://www.braze.com/docs/assets/img/onetrust/onetrust6.png?77cedb37c75687f9c3c3ddb4b3e6d989)




1. Update the body to include any necessary dynamic values. Make sure the body of the action matches the [`/users/delete` endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/).
2. When finished editing, select **Finish** then **Activate** to enable the workflow.

![](https://www.braze.com/docs/assets/img/onetrust/onetrust10.png?d2b419b2e3295883530631578c53c3f9)

#### Update the data subject request workflow
1. On the **Privacy Rights Automation** menu, select **Workflows**. 
2. Select the workflow you want to update with the Braze integration. 
3. Select the **Edit** button to enable editing.
4. Next, select the workflow step to add the Braze integration to and click **Add Connection**.
5. Add the previously created Braze workflow as a system subtask.




## Other supported actions

In addition to the **POST User track - Attributes**, **POST Set Users Subscription Group Status**, and **POST User Delete** actions, Braze supports other endpoints that can be used to create custom workflows and used as subtasks within existing workflows. 

To see a full list of supported actions:
1. In OneTrust, click into **Systems** from your **Integrations** menu. 
2. Choose the **Braze** system.
3. Navigate to the **Actions** tab.

![](https://www.braze.com/docs/assets/img/onetrust/onetrust7.png?c5cdcee13ca886f67963146129733ace)


