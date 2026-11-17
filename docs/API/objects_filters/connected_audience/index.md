# Connected audience object

> A connected audience is a dynamic audience filter you define inline within your API request, so you can target the right users at send time without creating or managing segments in the Braze dashboard.

Instead of pre-building a segment for every possible audience combination, you pass filter criteria directly in your API call. Depending on the endpoint, this object is passed as `audience` or `custom_audience`. Braze evaluates each user against those criteria in real time and delivers the message only to users who match. This means a single campaign, Canvas, or API-only message definition can serve an unlimited number of audience variations, driven entirely by your business logic.

**Important:**


Braze validates connected audience filters. Requests with incorrectly typed values or unknown custom event names return an error. Test your audience payloads before you rely on them in production. For details, see [Filter validation](#filter-validation).



## How it works

1. Define your message by either creating an API-triggered campaign or Canvas in the Braze dashboard, or define message content entirely inline using the [messaging objects](https://www.braze.com/docs/api/objects_filters#messaging-objects) in your API request. Use [trigger properties](https://www.braze.com/docs/api/objects_filters/trigger_properties_object) or [Canvas context](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context) for dynamic personalization.
2. Call a supported endpoint and include your connected audience filters in the `audience` parameter, or in `custom_audience` for `/messages/live_activity/start`. You can filter on custom attributes, subscription status, session history, segment membership, campaign engagement, and more. For the full list, see [Connected audience filters](#connected-audience-filters).
3. Braze evaluates the filters at send time, delivering the message only to users who match your criteria.

**Tip:**


A `campaign_id` isn't required when using the `audience` parameter. The [`/messages/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages) and [`/messages/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages) endpoints let you define message content inline without a pre-created campaign. However, if you want to track campaign-level metrics (such as sends, clicks, or bounces) on the dashboard, include a `campaign_id`.



Because the audience is defined per request, your backend systems can trigger contextually relevant messages in response to any business event (a price change, a weather alert, a live score update) without dashboard intervention.

### Compatible endpoints

You can use the connected audience object on these endpoints:

- [`/messages/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages)
- [`/campaigns/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)
- [`/canvas/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [`/messages/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/campaigns/trigger/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)
- [`/canvas/trigger/schedule/create`](https://www.braze.com/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [`/messages/live_activity/start`](https://www.braze.com/docs/api/endpoints/messaging/live_activity/start) (uses `custom_audience`)

Note that the `audience` parameter does not support array of objects.

## Use cases

Use connected audiences for scenarios where your back-end systems detect an event and need to notify a dynamically determined set of users:

| Category | Example |
| --- | --- |
| Weather alerts | A weather data provider detects a severe weather event and sends push notifications to users whose `preferred_city` attribute matches the affected area. |
| Sports and live events | A sports app sends real-time score updates or match alerts to users whose `favorite_team` attribute matches one of the teams playing. |
| Content and entertainment | A streaming service notifies users whose `favorite_shows` array includes a series title whenever a new episode is released. |
| E-commerce | An online retailer sends price-drop or back-in-stock alerts to users whose `wishlisted_products` array includes the relevant product ID. |
| Travel | A travel app sends flight-delay notifications to users whose `booked_flight` attribute matches the affected flight number. |
| Financial services | A trading platform alerts users whose `watchlist` array includes a stock ticker that has crossed a price threshold. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Use cases" }

In each case, a single campaign or API-only message definition handles all variations. Your backend determines the filter values and passes them in the API request, so you don't need to create a separate segment or campaign for each product, show, team, or location.

## Example request

The following example uses the [`/campaigns/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) endpoint to target users who have favorited a specific show and are opted in to push notifications:

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": true
}
```

Set `broadcast` to `true` when you omit `recipients` and target with `audience`. For [`/campaigns/trigger/send`](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), `broadcast` is required to send to a connected audience without a recipients list. If `broadcast` is `true`, don't include a `recipients` list.

## Object body

The connected audience object is composed of either a single connected audience filter or several connected audience filters combined with `AND` and `OR` operators.

**Multiple filter example:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Connected audience filters

Combine multiple filters with `AND` and `OR` operators to create a connected audience filter.

### Considerations

Connected audiences support the filters listed on this page. To filter on anything else, incorporate it into an audience segment and then specify that segment in the `segment_id` parameter for the [`/messages/send` endpoint](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). When using other endpoints, you must add the segment to the API-triggered campaign or Canvas in the Braze dashboard first.


### Custom attribute filter

This filter allows you to segment based on a user's custom attribute. These filters contain up to three fields:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Allowed comparisons by data type

The custom attribute's data type determines the comparisons that are valid for a given filter.

| Custom attribute type | Allowed comparisons |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Allowed comparisons by data type" }

#### Attribute comparison caveats

| Comparison | Additional considerations |
| --- | --- |
| `value` | The `value` is not required when using the `exists` or `does_not_exist` comparisons. `value` must be an ISO 8601 datetime string when using the `before` and `after` comparisons. |
|`matches_regex` | When using the `matches_regex` comparison, the value passed must be a string. To read more about using regular expressions with Braze, refer to [Regular expressions](https://www.braze.com/docs/user_guide/audience/segments/regex) and [Custom attribute data types](https://www.braze.com/docs/developer_guide/analytics#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Attribute comparison caveats" }

#### Multi-value comparisons

Both `is_any_of` and `is_none_of` support matching against multiple values in a single comparison. These comparisons work with both string and array custom attributes.

- `is_any_of`: Matches users whose attribute value equals any of the provided values. The `value` can be a single string or an array of strings.
- `is_none_of`: Matches users whose attribute value does not match any of the provided values. The `value` can be a single string or an array of strings. Note that users without the attribute on their profile always qualify for this comparison.

For array attributes:

- `includes_value` can also accept an array of values to check if the user's array contains any of the specified values.
- When using `is_any_of` or `is_none_of` with array attributes, they function the same as `includes_value` and `does_not_include_value` respectively.

**Tip:**


For multi-value matching, use `is_any_of` rather than `includes_value`.



#### Custom attribute examples

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```

#### Multi-value comparison examples

##### `is_any_of` with an array of strings

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_color",
    "comparison": "is_any_of",
    "value": ["red", "blue", "green"]
  }
}
```

##### `is_none_of` with an array of strings

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscription_tier",
    "comparison": "is_none_of",
    "value": ["bronze", "silver"]
  }
}
```

##### `includes_value` with an array (array attribute)

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscribed_products",
    "comparison": "includes_value",
    "value": ["1001", "1002", "1003"]
  }
}
```

This matches users whose `subscribed_products` array contains any of the values `"1001"`, `"1002"`, or `"1003"`.

### Push subscription filter

This filter allows you to segment based on a user's push subscription status.

#### Filter body

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Allowed comparisons:** `is`, `is_not`
- **Allowed values:** `opted_in`, `subscribed`, `unsubscribed`

### Email subscription filter

This filter allows you to segment based on a user's email subscription status.

#### Filter body

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Allowed comparisons:** `is`, `is_not`
- **Allowed values:** `opted_in`, `subscribed`, `unsubscribed`

### Last used app filter

This filter allows you to segment based on when the user last used the app. These filters contain two fields:

#### Filter body

```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Allowed comparisons:** `after`, `before`
- **Allowed values:** datetime (ISO 8601 string)

### Additional filters

You can also filter on the following. Each filter takes a `comparison` and, in most cases, a `value`, using the same structure as the filters described earlier. The comparisons available depend on the filter, and an unsupported comparison returns an error. The example values show the format Braze expects.

| Filter | Targets | Example value |
| --- | --- | --- |
| `country_filter` | The user's country. | `US` |
| `language_filter` | The user's language. | `en` |
| `locale_filter` | The user's locale. | `en_US` |
| `email_filter` | The user's email address. | `user@example.com` |
| `external_user_id_filter` | The user's external ID. | `external-user-123` |
| `phone_number_filter` | The user's phone number. | `+15555550123` |
| `device_gaid_filter` | The user's Google advertising ID. | `device-gaid-123` |
| `device_idfa_filter` | The user's identifier for advertisers. | `device-idfa-123` |
| `device_idfv_filter` | The user's identifier for vendors. | `device-idfv-123` |
| `has_push_filter` | Whether the user has a push token. | `true` |
| `has_background_push_filter` | Whether the user has a background push token. | `true` |
| `has_email_filter` | Whether the user has an email address. | `true` |
| `email_subscription_status_filter` | The user's email subscription status. | `subscribed` |
| `push_subscription_status_filter` | The user's push subscription status. | `subscribed` |
| `hard_bounce_filter` | Whether the user's email address hard bounced. | `true` |
| `session_count_filter` | The number of sessions the user has logged. | `5` |
| `first_session_since_filter` | When the user first logged a session. | `2025-01-01T00:00:00Z` |
| `last_session_since_filter` | When the user last logged a session. | `2025-01-01T00:00:00Z` |
| `created_at_filter` | When the user profile was created. | `2025-01-01T00:00:00Z` |
| `custom_event` | Whether the user performed a custom event. | `Watched Show` |
| `custom_event_last_performed` | When the user last performed a custom event. | `2025-01-01T00:00:00Z` |
| `custom_events_first_since_filter` | When the user first performed a custom event. | `2025-01-01T00:00:00Z` |
| `segment_membership_filter` | Whether the user belongs to a segment. | `00000000-0000-0000-0000-000000000001` |
| `received_campaign_filter` | Whether the user received a campaign. | `00000000-0000-0000-0000-000000000001` |
| `average_order_value_calculated_attribute_filter` | The user's average order value. | `100.5` |
| `customer_lifetime_value_calculated_attribute_filter` | The user's lifetime value. | `100.5` |
| `refund_value_calculated_attribute_filter` | The user's total refund value. | `100.5` |
| `revenue_value_calculated_attribute_filter` | The user's total revenue value. | `100.5` |
| `last_order_placed_calculated_attribute_filter` | When the user last placed an order. | `2025-01-01T00:00:00Z` |
| `total_orders_calculated_attribute_filter` | The user's total number of orders. | `5` |
| `total_cancelled_orders_calculated_attribute_filter` | The user's total number of canceled orders. | `5` |
| `random_number_filter` | The random bucket number assigned to the user. | `5` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Additional filters" }

Custom event filters require the name of a custom event that already exists in the workspace.

### Nested custom attribute filter

Use this filter to segment based on a property inside a [nested custom attribute](https://www.braze.com/docs/user_guide/data/activation/attributes/nested_custom_attribute_support).

#### Filter body

```json
{
  "nested_custom_attribute":
  {
    "custom_attribute_name": (String) the name of the nested custom attribute,
    "nested_property_name": (String) the name of the property within that attribute,
    "comparison_type": (String) the data type of the property,
    "comparison": (String) one of the allowed comparisons for that data type,
    "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
  }
}
```

- **Allowed comparison types:** `boolean`, `day_of_year`, `number`, `string`, `time`
- The `value` isn't required when using the `exists` or `does_not_exist` comparisons.

## Filter validation

Braze validates each filter before it builds the audience. When a filter fails validation, the request returns an error and Braze doesn't send the message.

| Filter | Rule | Error message |
| --- | --- | --- |
| `custom_attribute` on a number attribute | The `value` must be a number (`5`, not `"5"`). | `Value must be a number for the attribute {ATTRIBUTE_NAME}.` |
| `custom_attribute` on a boolean attribute | The `value` must be `true` or `false`, not a string. | `Value must be a boolean for the attribute {ATTRIBUTE_NAME}.` |
| Custom event filters | The event name must already exist in the workspace. | `Couldn't find a custom event matching {CUSTOM_EVENT_NAME} in workspace {WORKSPACE_ID} for company {COMPANY_ID}.` |
| Any filter | The comparison must be valid for that filter type. | `Invalid comparison {COMPARISON} for {FILTER} filter.` |
| Any filter | The `value` is required unless the comparison is `exists` or `does_not_exist`. | `You must specify a value.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filter validation" }
