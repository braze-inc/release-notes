# Rate limits

> The Braze API infrastructure is designed to handle high volumes of data across our customer base. To this end, we enforce API rate limits per workspace.

A rate limit is the number of requests the API can receive in a given time period. Many load-based denial-of-service incidents in large systems are unintentional—caused by errors in software or configurations—not malicious attacks. Rate limits check that such errors don't deprive our customers of Braze API resources. If too many requests are sent in a given time frame, you may see error responses with a status code of `429`, which indicates the rate limit has been hit.

**Warning:**


API rate limits are subject to change depending on the proper usage of our system. We encourage sensible limits when making an API call to prevent damage or misuse.



## Rate limits by request type

Refer to the following for the default API rate limits of different request types. These default limits can be increased upon request. Contact your customer success manager for more information.

### Requests with different rate limits

| Request Type                                                                                                                                                                                                                                           | Default API Rate Limit                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/)                                                                                                                                                                                                                                   | **Requests:** 3,000 requests per three seconds.<br><br>**Batching:** Up to 75 total objects combined across `attributes`, `events`, and `purchases` per API request. Customers on legacy rate limits can include up to 75 objects per array independently. For more information, reference [Batching User Track requests](#batch-user-track).<br><br>**Limits for Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU:** see [guidance on limits here](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). |
| [`/users/export/ids`](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier/)                                                                                                                                                                                                                              | **If you onboarded on or after August 22, 2024:** 250 requests per minute. <br><br> **If you onboarded before August 22, 2024:** 2,500 requests per minute.                                                                                                                                                                                                                               |
| [`/users/delete`](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/)<br>[`/users/alias/new`](https://www.braze.com/docs/api/endpoints/user_data/post_user_alias/)<br>[`/users/alias/update`](https://www.braze.com/docs/api/endpoints/user_data/post_users_alias_update/)<br>[`/users/identify`](https://www.braze.com/docs/api/endpoints/user_data/post_user_identify/)<br>[`/users/merge`](https://www.braze.com/docs/api/endpoints/user_data/post_users_merge/)                                                                                                                    | 20,000 requests per minute, shared between the endpoints.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`](https://www.braze.com/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)                                                                                                                                                                                                                      | 1,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`](https://www.braze.com/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/)                                                                                                                                                                                                                      | 1,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`](https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events/)                                                                                                                                                                                                                                   | 1,000 requests per hour, shared with the `/purchases/product_list` endpoint.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`](https://www.braze.com/docs/api/endpoints/export/purchases/get_list_product_id/)                                                                                                                                                                                                                        | 1,000 requests per hour, shared with the `/events/list` endpoint.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_analytics/)                                                                                                                                                                                                                       | 50,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages/)<br>[`/campaigns/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)<br>[`/canvas/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)<br>[`/campaigns/trigger/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)<br>[`/canvas/trigger/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)                                                                                                                                                          | For broadcast calls (when broadly targeting segments, filters, or a connected audience), 250 requests per minute across all audiences, and 10 requests per minute per [unique audience](https://www.braze.com/docs/api/api_limits/#what-counts-as-the-same-unique-audience) (whichever limit hits first).<br><br>Otherwise, when targeting individual recipients, the request is included in the 250,000 requests per hour [shared rate limit](https://www.braze.com/docs/api/api_limits/#requests-with-shared-rate-limits).                                                                                                                                                                                                                    |
| [`/sends/id/create`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_create_send_ids/)                                                                                                                                                                                                                               | 100 requests per day.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)                                                                                                                                                                                                                       | 5,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`](https://www.braze.com/docs/api/endpoints/preference_center/get_create_url_preference_center/)<br>[`/preference_center/v1/list`](https://www.braze.com/docs/api/endpoints/preference_center/get_list_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`](https://www.braze.com/docs/api/endpoints/preference_center/get_view_details_preference_center/)                                                                            | 1,000 requests per minute.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`](https://www.braze.com/docs/api/endpoints/preference_center/post_create_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`](https://www.braze.com/docs/api/endpoints/preference_center/put_update_preference_center/)                                                                                                                                                            | 10 requests per minute.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/)<br>[`/catalogs`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)<br>[`/catalogs`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)                                                                                                                                                                             | 50 requests per minute shared between the endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/)                                                                                                                             | 16,000 requests per minute shared between the endpoints.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/)<br>[`/catalogs/{catalog_name}/items`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/)<br>[`/catalogs/{catalog_name}/items/{item_id}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 50 requests per minute shared between the endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`](https://www.braze.com/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 requests per minute shared between the endpoints. |
| [`/scim/v2/Users/{id}`](https://www.braze.com/docs/get_see_user_account_information/)<br>[`/scim/v2/Users?filter={userName@example.com}`](https://www.braze.com/docs/get_search_existing_dashboard_user_email/)<br>[`/scim/v2/Users/{id}`](https://www.braze.com/docs/post_update_existing_user_account/)<br>[`/scim/v2/Users/{id}}`](https://www.braze.com/docs/delete_existing_dashboard_user/)<br>[`/scim/v2/Users/`](https://www.braze.com/docs/post_create_user_account/)                                                                          | 5,000 requests per day, per company, shared between the endpoints.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`](https://www.braze.com/docs/api/endpoints/cdi/get_integration_list/)                                                                                                                                                                                                                              | 50 requests per minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`](https://www.braze.com/docs/api/endpoints/cdi/get_job_sync_status/)                                                                                                                                                                                                        | 20 requests per minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`](https://www.braze.com/docs/api/endpoints/cdi/post_job_sync/)                                                                                                                                                                                             | 100 requests per minute.                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Requests with shared rate limits

The following requests have a rate limit of 250,000 requests per hour, shared between them.

- [`/app_group/sdk_authentication/create`](https://www.braze.com/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/)
- [`/app_group/sdk_authentication/keys`](https://www.braze.com/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys/)
- [`/app_group/sdk_authentication/delete`](https://www.braze.com/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`](https://www.braze.com/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key/)
- [`/campaigns/details`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) (only for non-broadcast calls&#8212;those that specify `external_user_ids` or `aliases`)
- [`/campaigns/trigger/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) (only for non-broadcast calls)
- [`/campaigns/trigger/schedule/delete`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/)
- [`/campaigns/trigger/schedule/update`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/)
- [`/canvas/data_series`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_analytics/)
- [`/canvas/data_summary`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/)
- [`/canvas/details`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_details/)
- [`/canvas/list`](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvases/)
- [`/canvas/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) (only for non-broadcast calls)
- [`/canvas/trigger/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) (only for non-broadcast calls)
- [`/canvas/trigger/schedule/delete`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)
- [`/canvas/trigger/schedule/update`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
- [`/content_blocks/create`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
- [`/content_blocks/info`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)
- [`/content_blocks/list`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)
- [`/content_blocks/update`](https://www.braze.com/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/)
- [`/email/blocklist`](https://www.braze.com/docs/api/endpoints/email/post_blocklist/)
- [`/email/blacklist`](https://www.braze.com/docs/api/endpoints/email/post_blacklist/)
- [`/email/bounce/remove`](https://www.braze.com/docs/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/hard_bounces`](https://www.braze.com/docs/api/endpoints/email/get_list_hard_bounces/)
- [`/email/spam/remove`](https://www.braze.com/docs/api/endpoints/email/post_remove_spam/)
- [`/email/status`](https://www.braze.com/docs/api/endpoints/email/post_email_subscription_status/)
- [`/email/unsubscribes`](https://www.braze.com/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/)
- [`/events/data_series`](https://www.braze.com/docs/api/endpoints/export/custom_events/get_custom_events_analytics/)
- [`/kpi/dau/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_dau_date/)
- [`/kpi/mau/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/)
- [`/kpi/new_users/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/)
- [`/kpi/uninstalls/data_series`](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
- [`/messages/live_activity/start`](https://www.braze.com/docs/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`](https://www.braze.com/docs/api/endpoints/messaging/live_activity/update/)
- [`/messages/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages/) (only for non-broadcast calls)
- [`/messages/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/messages/schedule/delete`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/)
- [`/messages/schedule/update`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/)
- [`/messages/scheduled_broadcasts`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)
- [`/segments/data_series`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment_analytics/)
- [`/segments/details`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment_details/)
- [`/segments/list`](https://www.braze.com/docs/api/endpoints/export/segments/get_segment/)
- [`/sends/data_series`](https://www.braze.com/docs/api/endpoints/export/campaigns/get_send_analytics/)
- [`/sessions/data_series`](https://www.braze.com/docs/api/endpoints/export/sessions/get_sessions_analytics/)
- [`/sms/invalid_phone_numbers`](https://www.braze.com/docs/api/endpoints/sms/get_query_invalid_numbers/)
- [`/sms/invalid_phone_numbers/remove`](https://www.braze.com/docs/api/endpoints/sms/post_remove_invalid_numbers/)
- [`/subscription/status/get`](https://www.braze.com/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)
- [`/subscription/user/status`](https://www.braze.com/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/)
- [`/templates/email/create`](https://www.braze.com/docs/api/endpoints/templates/email_templates/post_create_email_template/)
- [`/templates/email/info`](https://www.braze.com/docs/api/endpoints/templates/email_templates/get_see_email_template_information/)
- [`/templates/email/list`](https://www.braze.com/docs/api/endpoints/templates/email_templates/get_list_email_templates/)
- [`/templates/email/update`](https://www.braze.com/docs/api/endpoints/templates/email_templates/post_update_email_template/)
- [`/users/export/global_control_group`](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_global_control_group/)
- [`/users/export/segment`](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_segment/)

### What counts as the same unique audience? {#what-counts-as-the-same-unique-audience}

This applies to the following endpoints: [`/messages/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages/), [`/campaigns/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), [`/canvas/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), [`/campaigns/trigger/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/), and [`/canvas/trigger/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/).

For these endpoints, broadcast requests are considered to target the same unique audience when all of the following match:

- The campaign or Canvas being triggered (the `campaign_id` or `canvas_id` in your API request, if specified)
- The audience being targeted (the segments or filters, or for API campaigns, the `segment_id` in your API request)
- The connected audience filters (the `audience` object in your API request, if specified)

Each unique combination of these attributes counts as a distinct audience, so the additional rate limit for each unique audience applies to each combination independently.

## Batching API requests

Braze APIs are built to support batching. With batching, Braze can take in as much data as possible in a single API call so that you don't need to make a lot of API calls. It's more efficient for Braze to process data in batches than to process data one call at a time. For example, handling 1,000 batched API calls requires less resources than handling 75,000 individual calls. Batching is extremely important for any application that may require more than 75,000 calls per hour.

**Note:**


REST API rate limit increases are considered based on need for customers who are making use of the API batching capabilities.



### Batching requests for Track users endpoint {#batch-user-track}

Each `/users/track` request can contain up to 75 total objects combined across `attributes`, `events`, and `purchases`. Each object can update one user. A single user profile can be updated by multiple objects.

**Legacy rate limits**


For customers on legacy rate limits, each array (`attributes`, `events`, and `purchases`) can contain up to 75 objects independently, for a combined maximum of up to 225 objects per request.



For more information about `/users/track` rate limits, see [POST: Create and update users](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/).

Requests made to this endpoint will generally begin processing in this order:

1. Attributes
2. Events
3. Purchases

### Batching Messaging endpoint requests

A single request to the [Messaging endpoints](https://www.braze.com/docs/api/endpoints/messaging/) can reach any one of the following:

- Up to 50 specific `external_ids`, each with individual message parameters
- A segment of any size created in the Braze dashboard, specified by its `segment_id`
- Users who match additional audience filters of any size, defined in the request as a [connected audience](https://www.braze.com/docs/api/objects_filters/connected_audience/) object

### Example batch request

The following example uses `external_id` to make one API call for email and SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## Monitoring your rate limits

Every single API request sent to Braze returns the following information in the response headers:

| Header Name             | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | The maximum number of requests that you can make in a specified interval (your rate limit). |
| `X-RateLimit-Remaining` | The number of requests remaining in the current rate limit window.                          |
| `X-RateLimit-Reset`     | The time at which the current rate limit window resets in UTC epoch seconds.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

This information is intentionally included in the header of the response to the API request rather than the Braze dashboard. This allows your system to better react in real time as you're interacting with our API. For example, if the `X-RateLimit-Remaining` value drops below a certain threshold, you might want to slow sending to make sure all transactional emails go out. Or, if it reaches zero, you might want to pause all sending until the time specified in `X-RateLimit-Reset` elapses.

**Note:**


HTTP headers will be returned in all lowercase characters. This behavior aligns with the HTTP/2 protocol that mandates all header field names must be lowercase. This differs from HTTP/1.X where header names were case-insensitive but were commonly written in various capitalizations.



If you have questions about API limits, contact your customer success manager or open a [support ticket](https://www.braze.com/docs/braze_support/).

**Tip:**


You can use the [API usage dashboard](https://www.braze.com/docs/user_guide/analytics/dashboards/api_usage/) to view and compare incoming traffic against your rate limits.



### Optimal delay between endpoints

**Note:**


We recommend that you allow for a 5-minute delay between consecutive endpoint calls to minimize errors.



Understanding the optimal delay between endpoints is crucial when making consecutive calls to the Braze API. Problems arise when endpoints depend on the successful processing of other endpoints, and if called too soon, could raise errors. For example, if you're assigning users an alias through our `/user/alias/new` endpoint, and then hitting that alias to send a custom event through our `/users/track` endpoint, how long should you wait?

Under normal conditions, the time for our data eventual consistency to occur is 10-100ms (1/10 of a second). However, there can be some cases where it takes longer for that consistency to occur, so we recommend that you allow for a 5-minute delay between making subsequent calls to minimize the probability of error.

### Rate limit reset

Rate limits reset on the clock hour, not on a rolling window. For example, if the limit is 250,000 requests per hour, you could make 50,000 requests between 10:00 PM and 10:59 PM and another 250,000 requests between 11:00 PM and 11:59 PM, because the counter resets at the top of each hour.