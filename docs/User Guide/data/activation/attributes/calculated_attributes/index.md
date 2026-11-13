# Calculated attributes

> Calculated attributes let you create profile attributes from raw event data using a no-code formula builder. Instead of asking developers to define and maintain these attributes, you can create them directly in Braze if the required events are already tracked.





**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





A calculated attribute is a custom attribute generated from a formula. The formula is built from three parts:

| Part | Description |
| --- | --- |
| Aggregation | Sum, average, maximum, minimum, count, distinct count, first, last, or most common |
| Event and property | From supported event sources |
| Time frame | When the event occurred, as a relative lookback or a fixed date range of up to 2 years (730 days) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Calculated attribute formula parts" }

After you activate the calculated attribute, Braze writes it to the user profile and you can use it for segmentation.

## Early access capabilities

In early access, you can:

- Create a calculated attribute from scratch using an aggregation, a purchase or eCommerce event, and a time period
- Save and activate the attribute so Braze can calculate values and store them on user profiles
- Refresh values once per day
- Segment using the calculated attribute
- Deactivate calculated attributes you no longer want to use

Each workspace can have up to 25 active calculated attributes at a time. Drafts and deactivated attributes don't count toward this limit. If you reach the limit, deactivate one before activating another.

**Note:**


Custom events are not yet available as an event source during early access.



## Use cases

Use calculated attributes to continuously compute a meaningful value for each user from recent behavior—especially when a pattern over time is a better indicator than a single event.

| Use case | Example formula | Business value |
| --- | --- | --- |
| Total amount of money spent | **Aggregation:** Sum<br>**Event:** eCommerce order placed, with a property for total value | Identify high-value customers or recent spenders |
| Average order value | **Aggregation:** Average<br>**Event:** eCommerce order placed, with a property for total value | Spot customers whose typical order size is rising or falling |
| Number of orders placed | **Aggregation:** Count<br>**Event:** eCommerce order placed | Find frequent buyers for loyalty or retention messaging |
| Most recent purchase date | **Aggregation:** Last<br>**Event:** Purchase | Target users based on how recently they bought |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Calculated attributes use cases" }

## Set up calculated attributes

1. Go to **Data Settings** > **Calculated Attributes**, and then select **Create calculated attribute**.
2. Choose the aggregation you want to use for your formula. See [Supported aggregations](#supported-aggregations) for the available options.
3. Select a criterion (your event).
4. Optionally, add an event property and nested event property.
   - For nested event properties, specify the data type (for example, string or number).
   - If using eCommerce recommended events, use the exact property naming structure for those events. See [eCommerce recommended events](https://www.braze.com/docs/user_guide/data/activation/events/recommended_events/ecommerce_events).
5. Set the time range for the calculation. Choose a relative lookback (for example, the last 30 days) or a fixed date range. Either option can span up to 2 years (730 days).
6. Save the calculated attribute as a draft, or activate it to begin processing and daily refreshes.

**Note:**


A calculated attribute must be activated before it can be used in a segment. After activation, the output is written to each eligible user's profile as an attribute value. That value can then be used in segmentation.



## Supported aggregations {#supported-aggregations}

Choose the aggregation based on the kind of customer insight you want to capture:

| Aggregation | Description |
| --- | --- |
| Average | Typical value over the time frame, such as average order value |
| Sum | Total value over the time frame, such as total amount spent |
| Maximum | Highest value over the time frame, such as a high score |
| Minimum | Lowest value over the time frame |
| Count | How many times an event occurred |
| Distinct count | How many unique values occurred for a property |
| First | Earliest value in the time frame |
| Last | Most recent value in the time frame |
| Most common | Most frequent value, such as a preferred category |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported aggregations" }

## Statuses

A calculated attribute can show one of the following statuses:

| Status | Description |
| --- | --- |
| Active | The attribute is enabled and participating in refreshes. |
| Inactive | The attribute isn't currently active. This includes drafts you haven't activated yet and attributes you've deactivated. Braze doesn't run daily refreshes for inactive attributes. |
| Processing | Braze is running the calculation, and user values haven't finished updating. |
| Processing failed | The latest processing attempt didn't succeed, and the calculated attribute values didn't refresh. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Calculated attribute statuses" }

Only **Active** attributes refresh on an ongoing basis and count toward your workspace limit of 25 active calculated attributes. Activate an attribute when you're ready for Braze to keep its profile values up to date, and deactivate it when you no longer want those refreshes.
