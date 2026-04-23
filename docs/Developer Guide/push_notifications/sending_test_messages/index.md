# Sending test messages

> Before sending out a messaging campaign to your users, you may want to test it to make sure it looks right and operates in the intended manner. You can use the dashboard to create and send test messages with push notifications, in-app messages (IAM), or email.

## Sending a test message

### Step 1: Create a designated test segment <a class="margin-fix" name="test-segment"></a>

After you set up a test segment, you can use it to test any of your Braze messaging channels. When set up correctly, this only needs to be done a single time.

To set up a test segment, go to **Segments** and create a new segment. Select **Add Filter**, then choose a one of the test filters.

![A Braze test campaign displaying the filters available in the targeting step.](https://www.braze.com/docs/assets/img_archive/testmessages1.png?c440e858d187b30c92b316dfa12b9774)

With test filters, you can ensure that only users with a specific email address or [external user ID](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) are sent the test message.

![A dropdown menu displaying several filters listed under a heading that reads Testing](https://www.braze.com/docs/assets/img_archive/testmessages2.png?8c289defede0c6ba588c9b8ba8d0c9f5)

Both email address and external user ID filters offer the following options:

| Operator          | Description |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals`      | This will look for an exact match of the email or user ID that you provide. Use this if you only want to send the test campaigns to devices associated with a single email or user ID. |
| `does not equal` | Use this if you want to exclude a particular email or user ID from test campaigns. |
| `matches`     | This will find users that have email addresses or user IDs that match part of the search term you provide. You could use this to find only the users that have an `@yourcompany.com` address, allowing you to send messages to everyone on your team. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

You can select multiple specific emails using the "`matches`" option and separating the email addresses with a &#124; character. For example: "`matches`" "`email1@braze.com` &#124; `email2@braze.com`". You can also combine multiple operators together. For example, the test segment could include an email address filter that "`matches`" "`@braze.com`" and another filter that "`does not equal`" "`sales@braze.com`". 

After adding the testing filters to your test segment, you can verify it's working by selecting **Preview** or by selecting **Settings** > **CSV Export All User Data** to export that segment's user data to a CSV file.

![A section of a Braze campaign titled Segment Details](https://www.braze.com/docs/assets/img_archive/testmessages3.png?78e031a18aad06f510fd2ac4946bf7c5)

**Note:**


Exporting the segment's User Data to a CSV file is the most accurate verification method, as the preview will only show a sample of your users and may not include all users.



### Step 2: Send the message

You can send a message using the Braze dashboard or the command line.





To send test push notifications or in-app messages, you need to target your previously created test segment. Begin by creating your campaign and following the usual steps. When you reach the **Target Audiences** step, select your test segment from the dropdown menu.

![A Braze test campaign displaying the segments available in the targeting step.](https://www.braze.com/docs/assets/img_archive/test_segment.png?25ae32cc99d02e6dcdd9b66a0adf75e4)

Confirm your campaign and launch it to test your push notification and in-app messages.

**Note:**


Be sure to select **Allow users to become re-eligible to receive campaign** under the **Schedule** portion of the campaign composer if you intend to use a single campaign to send a test message to yourself more than once.





If you're only testing email messages, you do not necessarily have to set up a test segment. In the first step of the campaign composer where you compose your campaign's email message, click **Send Test** and enter the email address to which you wish to send a test email. 

![A Braze campaign with the Test Send tab selected](https://www.braze.com/docs/assets/img_archive/testmessages45.png?883cb58cd3adf2e8315817db896b7914)

**Tip:**

 
You can also enable or disable [TEST (or SEED)](https://www.braze.com/docs/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) being appended on your test messages.







Alternatively, you can send a single notification using cURL and the [Braze Messaging API](https://www.braze.com/docs/api/endpoints/messaging/). Note that these examples make a request using the `US-01` instance. To find out yours, refer to [API endpoints](https://www.braze.com/docs/api/basics/#endpoints).



```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```



```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```



```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```



Replace the following:

| Placeholder         | Description                                               |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY`      | Your Braze API key used for authentication. In Braze, go to **Settings** > **API Keys** to locate your key. |
| `EXTERNAL_USER_ID` | The external user ID used to send your message to a specific user. In Braze, go to **Audience** > **Search users**, then search for a user. |
| `CUSTOM_KEY`         | (Optional) A custom key for additional data.              |
| `CUSTOM_VALUE`       | (Optional) A custom value assigned to your custom key.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}



## Test limitations

There are a few situations where test messages don't have complete feature parity with launching a campaign or Canvas to a real set of users. In these instances, to validate this behavior, you should launch the campaign or Canvas to a limited set of test users.

- Viewing the Braze [preference center](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) from **Test Messages** will cause the submit button to be grayed out.
- The list-unsubscribe header is not included in emails sent by the test message functionality.
- For in-app messages and Content Cards, the target user must have a push token for the target device.

