# API request log

> Use the API request log to see individual REST API requests that Braze received for your workspace. You can filter requests by date, time, endpoint, response code, and API key, search request bodies, and view or copy the payload of each request.

The API request log complements the [API usage dashboard](https://www.braze.com/docs/user_guide/analytics/dashboards/api_usage), which shows aggregate request volume over time. Use the request log when you need to inspect the requests behind a trend, such as a spike in `4XX` errors from one endpoint.

## Prerequisites

To view the API request log, you need the following [permissions](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) for the workspace:

- View API Usage Dashboard
- View PII

If you have "View API Usage Dashboard" but not "View PII" permission, the **Request Log** tab shows a **Limited access** tag and doesn't display any requests.

## Accessing the request log

You can open the request log from the **APIs and Identifiers** page or from a chart on the API usage dashboard.

### From APIs and Identifiers

Go to **Settings** > **APIs and Identifiers**, then select the **Request Log** tab.

By default, the request log shows requests for today, newest first.

### From the API usage dashboard {#from-api-usage-dashboard}

1. Go to **Settings** > **APIs and Identifiers** > **Dashboard**.
2. In the chart, select a data point.
3. Select **View request logs**.

The request log opens with the time interval of that data point and the endpoint, response code, and API key filters that were applied to the chart. If only part of the interval is within the last 14 days, the request log shows only that part. **View request logs** is unavailable for intervals that fall entirely outside the last 14 days.

To replace the imported chart range, change the date or time in the request log filters.

## Request log columns

Each row in the request log represents one REST API request.

| Column | Description |
|--------|-------------|
| Time | When Braze received the request. |
| Endpoint | The HTTP method and endpoint of the request, such as `POST /users/track`. |
| API key | The name of the API key used for the request. If the key has no name, the log shows the first characters of the key. |
| Response code | The HTTP response code that Braze returned. |
| Details | Select **View payload** to open the request details and payload. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Request log columns" }

## Filtering requests

### Date and time

Use the **Time reference** date field to choose which day to view. You can select any date within the last 14 days.

To narrow results to part of a day:

1. Select **Filters**.
2. Under **Reference range**, select a **Date**, then select **Specify time**.
3. Select a **Scope**:
    - **Time window:** Shows requests between a start time and an end time on the selected date. The window includes the end minute. For example, a window from 09:20 to 09:21 covers two minutes.
    - **Starting at...:** Shows requests from the selected **Timestamp** through the end of the selected date.
4. Select **Apply**.

The time window must end at or after its start time, can't start in the future, and must end within the last 14 days.

### Endpoint, response code, and API key

To filter by request attributes, select **Filters**, then choose one or more values under **Filter by**:

- **Endpoint**
- **Response code**
- **API key**

When you leave a filter empty, the request log includes all values for that filter. Each applied filter appears as a tag on the request log. To remove a filter, remove its tag.

## Searching request bodies

Use the **Search request bodies** field to find requests whose body contains specific text, such as an `external_id` or a custom event name. Search works with any other filters you've applied.

Keep the following in mind when searching:

- Search matches complete words and isn't case-sensitive. For example, searching `purchase` matches `Purchase` but not `purchases`.
- When you enter multiple words, the results only include requests whose body contains all of them.
- Search terms can be up to 256 characters and must contain at least one letter or number.
- Requests without a recorded payload don't appear in search results.

## Viewing a request payload

To view the details of a request, select **View payload** in its row. The **Request payload** panel shows the request's time, endpoint, API key, and response code, followed by the request body.

To copy the request body, select **Copy request body**.

### When a payload is unavailable

If the request body wasn't recorded, the panel shows **Payload unavailable**. This happens when:

- The request body is larger than 8&nbsp;KiB.
- The request body isn't valid JSON.
- The request had no request body.

## Considerations

- The request log retains requests for 14 days. Older requests aren't available.
- The request log only includes REST API requests. SDK requests don't appear in the request log.
- The request log shows up to the 1,000 most recent requests that match your date, time, filters, and search. When more requests match, a message prompts you to narrow your search. To reach older requests, narrow the date or time range, add filters, or refine your search.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/analytics/dashboards/api_usage"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">API usage dashboard</span></span></div></a></li><li><a href="/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/api_usage_alerts"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">API usage alerts</span></span></div></a></li><li><a href="/docs/api/errors"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">API errors and responses</span></span></div></a></li></ul>
