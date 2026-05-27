# Geographic permissions

> Geographic permissions enhance security and protect against fraudulent SMS, MMS, and RCS traffic by enforcing controls on the countries to which you can send messages. You can specify an allowlist of countries to make sure that SMS, MMS, and RCS messages are only sent to approved regions. Only admins can make changes to the country allowlist. Non-admin users have access to a read-only version of the allowlist that indicates which countries a subscription group is able to send to.

If you're an admin, you can configure the countries that are on the allowlist. The country allowlist is configured at the [subscription group](https://www.braze.com/docs/sms_rcs_subscription_groups/) level. You can access it by going to **Audience** > **Subscriptions** and selecting an SMS, MMS, or RCS subscription group. The allowlist is under **Geographic Permissions**.

![The editable SMS Geographic Permissions section for an admin with several countries selected in the "Country allowlist".](https://www.braze.com/docs/assets/img/sms/sms_geographic_permissions.png?82d785c3a865b1965f00205dada257ac){: style="max-width:80%;"}

### Selecting countries

Add countries to the allowlist with the dropdown. The most common SMS and RCS countries are shown at the top, with others shown below. You can also search for countries by typing in the text field.

![The "Country allowlist" dropdown with the most common countries displaying at the top.](https://www.braze.com/docs/assets/img/sms/allowlist_dropdown.png?fdf84b8364c3970633cdaaf14b8a6deb){: style="max-width:80%;"}

Remove previously selected countries by clearing the respective boxes next to them.

### Saving your changes

Changes will take effect after you select **Save**. Removing countries from your allowlist will prevent all SMS, MMS, and RCS messages from sending to numbers in those countries.

![Warning modal confirming the countries that will be deleted from the allowlist.](https://www.braze.com/docs/assets/img/sms/delete_allowlist_warning.png?99e4c6af954e64752cee284da48189fc){: style="max-width:70%;"}

## High-risk countries

Certain countries have a higher risk of SMS and RCS traffic pumping. These countries are indicated by a **High Risk** tag in the country dropdown.

![The country dropdown with Azerbaijan having a "High Risk" tag.](https://www.braze.com/docs/assets/img/sms/high_risk.png?f1a43ea7496ec9cafd699ca6db260998){: style="max-width:80%;"}

If you allow sending in these countries, you must first acknowledge the risk of doing so before the country is added to your allowlist.

**Note:**


Limit the countries on your allowlist to only those required to support your business needs. This will minimize your potential for fraudulent traffic. For more guidance on preventing SMS traffic pumping, view [SMS traffic pumping fraud FAQs](https://www.braze.com/docs/sms_traffic_pumping_fraud/).



## Visibility of blocked sends

Attempted sends to countries that aren't on your allowlist will be aborted. Aborted messages will be logged to the [Message Activity Log](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) and within the [SMS abort message engagement event](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/). 

Aborted messages caused by blocked sends show as **Aborted Message Errors** and have the message "The recipient's phone number is in a blocked country".

![Abort log showing several SMS sendds that were blocked because the phone number is in a blocked country.](https://www.braze.com/docs/assets/img/sms/abort_log.png?6a10f77437d8d32def7aea66ec06d011){: style="max-width:80%;"}

