<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Braze Platform Data Retention

*October 2026*

> This article covers general Braze platform data retention information.

Data stored in Braze is retained and usable for the lifetime of the customer's account. This means data such as user profile attributes, custom attributes, custom events, and purchases are stored indefinitely for active users unless removed by the customer, for the duration of the contract.

Braze has features, processes, and APIs in place to automatically implement good data hygiene practices for compliance with privacy laws and other best practices. These are described in the following sections.

## Data Retention During the Agreement

### User Deletion

Braze enables its customers to delete entire User profiles and/or specific attribute data directly from their workspace.

This means customers can:
- Delete User profiles using the Braze [Delete user API endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete)
- Delete (null) or amend attributes on User profiles using the Braze [Track user API endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_track)

For privacy compliance, you may need to delete personal data pertaining to an End User upon the End User's request. You can find instructions on our [data protection technical assistance](https://www.braze.com/docs/help/dp-technical-assistance#the-right-to-erasure) page on how to permanently delete an End User's User Profile from the Braze Services within 30 days of submitting the request.

**Note:**


An End User may have multiple profiles, and you may need to delete multiple profiles to delete all data pertaining to a single End User. Follow instructions on the data protection technical assistance page on how to fully delete all data regarding a User.

Behavioral events (custom events, sessions, campaigns, purchases) cannot be deleted from a User profile. To remove those events, you must delete the entire User profile.



### Inactive and Dormant Users

Each week, Braze runs a process to remove Inactive and Dormant Users from the Braze Services. In general, these are Users who are not reachable (for example, have no email address, no phone number, no push token, do not use your apps or visit your websites), have had no activity recorded on their user profile, and have not been messaged using or engaged with Braze. This is done to adhere to data protection principles and best practices. You can read more about this process on our [user archival definitions](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_archival) page.

**Note:**


Customers have full control over whether or not a user is Inactive or Dormant. They can prevent archiving of User profiles by making an update to a User Profile or sending a message to the User at regular intervals. Braze Canvas offers the ability to do this automatically, allowing you to effectively turn off this functionality for some or all of your Inactive or Dormant Users. Customers who wish to deactivate archival for a large user base (more than 500 million users) are encouraged to contact Braze directly to implement this request.



### Campaign and Canvas Interactions Data

Messaging interaction data refers to how a user interacts with a campaign or Canvas they received (for example, when a user opens campaign A or a user receives variant A). This data is used for retargeting. While message interaction data is not deleted (unless the user's profile is deleted), after a certain period of inactivity it can expire and be moved into long term storage. You can read more about messaging interaction data availability on [About messaging interaction data availability](https://www.braze.com/docs/messaging_interaction_data).

### Events Data

Braze anonymizes events data stored in Snowflake after two years by removing personal data from the events data. See more information in the [Snowflake Data Retention](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake/data_retention) page. Events data is deleted from ClickHouse after two years.

## BrazeAI Decisioning Studio

Decisioning Studio applies a 12-month rolling retention period to cloud storage files, after which they are automatically deleted. Retention periods can be extended on a per-use-case basis where longer historical data is required for training or reporting purposes, and adjusted individually to meet specific customer requirements.

Aggregated statistics (for example, weekly/monthly summaries) are retained indefinitely in BigQuery, throughout the life of the Agreement, to preserve historical trend visibility even after underlying raw data is purged.

## Data Deletion at the End of the Agreement

When a customer contract expires, Braze initiates deletion of customer data within 60 days. Full deletion, including by sub-processors, is completed within 90 days of contract expiry.

## Back Up Servers

When data is deleted from your production instance, the data remains in Braze's backup servers for six months and is then deleted according to our internal processes.
