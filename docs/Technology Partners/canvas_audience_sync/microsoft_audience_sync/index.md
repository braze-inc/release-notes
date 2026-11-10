# Audience Sync to Microsoft Ads

> Audience Sync to Microsoft Ads extends the reach of your cross-channel customer journeys to Bing, MSN, and the Microsoft Audience Network. Use your customer data to securely add or remove users from Microsoft Advertising customer lists based on behavioral triggers, segmentation, and more.





**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





**Common use cases for Audience Syncing include**:

- Targeting high-value users via multiple channels to drive purchases or engagement
- Retargeting users who are less responsive to other marketing channels
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand


This feature allows brands to control what specific first-party data is shared with . At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our [privacy policy](https://www.braze.com/privacy).


## Prerequisites

Make sure the following items are created, completed, or accepted before setting up your Microsoft Ads Audience Sync step in Canvas.

| Requirement | Origin | Description |
| --- | --- | --- |
| Beta access | Braze | Microsoft Ads is in beta. Contact your Braze account manager to join. |
| Microsoft Advertising account | [Microsoft Advertising](https://ads.microsoft.com/) | An active Microsoft Advertising account tied to your brand. The connecting Braze user must be a Super Admin on that Microsoft Advertising account and sign in with a Microsoft account. |
| Microsoft tenant consent (when required) | Microsoft | If Microsoft says approval is required, your Microsoft tenant admin must approve the Braze app before you can connect. For more information, see [Microsoft tenant consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent). |
| Customer Match terms | Microsoft | Before your first sync, accept the [Customer Match](https://help.ads.microsoft.com/#apex/ads/en/56921/1) terms in Microsoft Advertising for each customer you plan to sync. Create a customer list in Microsoft Advertising and select **I accept**. |
| Microsoft terms and policies | Microsoft | Agree to comply with applicable Microsoft Advertising terms, policies, and documentation related to your use of Audience Sync to Microsoft Ads. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

## Integration

### Step 1: Connect to Microsoft Ads

**Important:**


You must have the ["Admin" permission](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions/#admin) to connect Microsoft Ads to your Braze account.



1. In the Braze dashboard, go to **Partner Integrations** > **Technology Partners** and select **Microsoft Ads**.
2. Make sure the connecting user is a Super Admin on your Microsoft Advertising account and can sign in with a Microsoft account. If Microsoft requires approval, have your Microsoft tenant admin approve the Braze app, then try connecting again.
3. In the **Microsoft Ads Audience Sync** section, select **Connect Microsoft Ads**.
4. Complete the Microsoft sign-in and authorize Braze.
5. After you're redirected to Braze, select the Microsoft Advertising customers you want available in this workspace, then save your selection.

**Note:**


Braze lists Microsoft Advertising customers, not individual ad accounts, for Audience Sync. Each customer list you create or select applies to all ad accounts under that customer.



Your Microsoft Ads connection applies at the Braze workspace level. If your Microsoft Advertising admin removes your access, Braze detects an invalid token. As a result, active Canvases that use Microsoft Ads show errors, and Braze can't sync users.

### Step 2: Configure your Canvas entry criteria

Before you sync users to Microsoft Ads, decide who is eligible for advertising in your Canvas. When building audiences for ad tracking, you may want to include or exclude certain users based on their preferences, and to comply with privacy laws such as the “Do Not Sell or Share” right under the [CCPA](https://oag.ca.gov/privacy/ccpa). Implement the relevant filters for users’ eligibility within their Canvas entry criteria.

If you collect `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, or any other relevant custom attributes, include them in your Canvas entry criteria as a filter.

To learn more about complying with these data protection laws within the Braze platform, see [Data Protection Technical Assistance](https://www.braze.com/docs/dp-technical-assistance/).

### Step 3: Add an Audience Sync step with Microsoft Ads

Add a component in your Canvas and select **Audience Sync**. Open the component editor to choose your Audience Sync partner.

### Step 4: Sync setup

1. Select **Microsoft Ads** as the Audience Sync partner.
2. Select the **Customer** to sync to.
3. Under **Choose a New or Existing Audience**, enter the name of a new or existing Microsoft customer list.
4. Select whether to add users to or remove users from the audience.

Microsoft Ads supports email matching only. Braze automatically formats and hashes email addresses using SHA-256 before sending. You don't select other match fields for this destination.




#### Create a new audience

Enter a name for the new customer list, select **Add Users to Audience**, then select **Create Audience**.

Braze creates a customer list in Microsoft Advertising that applies to all ad accounts under the selected customer. After you save the step, you can reference that audience later in the Canvas to remove users.

When you launch a Canvas with a new audience, Braze syncs users as they enter the Audience Sync step, subject to [batching and latency](https://www.braze.com/docs/partners/canvas_audience_sync/overview/#batching-and-latency).




#### Sync with an existing audience

To keep an existing Microsoft customer list up to date, select the audience name, then choose **Add Users to Audience** or **Remove Users from Audience**. Braze syncs users as they enter the Audience Sync step, subject to [batching and latency](https://www.braze.com/docs/partners/canvas_audience_sync/overview/#batching-and-latency).




**Note:**


You can add other Audience Sync partners to the same Audience Sync step. Configure each partner destination as required.



### Step 5: Launch Canvas

After you configure your Audience Sync to Microsoft Ads, complete the remainder of your Canvas and launch. Users who flow through the Audience Sync step are passed into the selected Microsoft customer list. If your Canvas contains subsequent components, those users advance to the next step in their journey.

Match size typically appears in Microsoft Advertising about 48 hours after upload. A customer list generally needs at least 300 matched users before you can target it.

## User syncing and rate limit considerations

As users reach the Audience Sync step, Braze enqueues them for batching before sending them to Microsoft Ads. See [Batching and latency](https://www.braze.com/docs/partners/canvas_audience_sync/overview/#batching-and-latency) for how Braze dispatches batches.

Braze sends up to 1,000 hashed emails per request to Microsoft Ads. If Microsoft's API rate limits your account, Braze retries the sync for up to about 13 hours. If the sync is still not possible, Braze lists these users under the *Users Errored* metric.

## Understanding analytics

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| Metric | Description |
| --- | --- |
| Entered | Number of users who entered this component to be synced to Microsoft Ads. |
| Proceeded to Next Step | Number of users who advanced to the next component, if there is one. All users auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users Braze successfully sent to Microsoft Ads. This is not the same as users matched in Microsoft Advertising. |
| Users Not Synced | Number of users that have not been synced because of missing fields to match (for example, no email address). |
| Users Pending | Number of users currently being processed by Braze to sync into Microsoft Ads. |
| Users Errored | Number of users who were not synced to Microsoft Ads because of an API error. Rate limits and Microsoft server errors retry for about 13 hours first. Potential causes include an invalid Microsoft token, a deleted audience, or Customer Match terms that aren't accepted. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Understanding analytics" }

**Important:**


There can be a delay in reporting for *Users Synced* and *Users Errored* because of batching and the retry window, respectively. *Users Synced* reflects a successful send from Braze. Microsoft Advertising may still take time to process and match those users.



## Frequently asked questions

### How long does it take for audience sizes to populate in Microsoft Ads?

Match size typically appears in Microsoft Advertising about 48 hours after upload.

### What is the minimum audience size for Microsoft Ads?

A customer list generally needs at least 300 matched users before you can target it in Microsoft Advertising.

### Which user fields can I sync?

Email only. Braze formats each email address and hashes it with SHA-256 before sending. Phone numbers and mobile advertising IDs aren't supported for Microsoft Ads Audience Sync.

### Why do I need to select a customer instead of an ad account?

Microsoft Advertising organizes ad accounts under customers. Braze syncs to customer lists that apply to all ad accounts under the selected customer. In the Canvas step, select the customer, then choose or create the customer list.

### What should I do if I receive an authentication or permissions error?

Disconnect and reconnect Microsoft Ads on the Technology Partners page. Confirm you are a Super Admin on the Microsoft Advertising account, you signed in with a Microsoft account, and—if Microsoft required it—your tenant admin approved the Braze app. Also confirm Customer Match terms are accepted for each customer before syncing.

### Why is my Canvas not allowed to launch?

Confirm Microsoft Ads is successfully connected on the partner page, you selected a customer, and you chose or created an audience. For a new audience, enter a name and select **Add Users to Audience**.

### Can I combine Microsoft Ads with other Audience Sync partners in one step?

Yes. Add another partner in the Audience Sync step and configure each destination as required.
