# Custom event extended history

> By default, Braze keeps 30 days of custom event history for segmentation. To segment using custom event data that goes as far back as two years, turn on 2-year history for a custom event and use it in a [calculated filter](https://www.braze.com/docs/user_guide/audience/segments/calculated_filters).





**Important:**


 is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.





## How extended event history works

Every custom event in your workspace is available in calculated filters with up to 30 days of history. 

When you turn on 2-year history for a custom event, Braze processes and backfills up to two years of that event's past data so you can use it in longer time windows. Some of your custom events may already show 2-year history, because Braze turned it on for all events used in your existing Segment Extensions. Those events count toward your workspace limit.

| History setting | Lookback available in calculated filters | Setup needed |
| --- | --- | --- |
| 30 days (default) | Up to 30 days | None—you can set up a filter and use it right away |
| 2 years | Up to 2 years | Turn on 2-year history, then wait for processing to finish before using a longer lookback |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Custom event history settings" }

**Note:**


You only need to turn on 2-year history once per custom event. After processing finishes, you can use that event and any of its properties in as many calculated filters as you like, without waiting for processing again.



## Turn on 2-year history for a custom event

1. Go to **Data Settings** > **Custom Events**.
2. Find the custom event you want to use. The **History** column shows whether the event currently has **30 days** or **2 years** of history.
3. Select the actions menu for the event, then select **Turn on 2-year history**.
4. Confirm your selection.

While the event's history is processed, a processing icon appears next to the event. When processing finishes, the **History** column shows **2 years**, and the person who turned it on receives an email confirming the event is ready to use.

## Add a custom event to a calculated filter

On the calculated filter creation page, select **Performed a Custom Event** from the criterion dropdown, then choose a custom event.

- If 2-year history is turned on for this event, you can enter a time frame longer than the past 30 days.
- If 2-year history isn't turned on, you are prompted to turn it on from the **Custom Events** page.

Calculated filters refresh on a set schedule. If you change an existing calculated filter to a longer time window after processing finishes, the filter uses the extended history the next time it refreshes.

## Turn off 2-year history

When you turn off 2-year history, the event returns to 30 days of history and frees up one slot toward your workspace limit.

You can't unarchive a calculated filter that uses a time window longer than 30 days for that event until you turn 2-year history on again.

## How long processing takes

After turning on 2-year history, you can't access more than 30 days of that event's data until it finishes processing. Plan for this delay before building calculated filters you need on a deadline. You only need to turn on 2-year history once per custom event.

- **Start time:** Processing begins shortly after you turn on 2-year history, typically within an hour.
- **Duration:** Most custom events finish within a few hours, and many finish within minutes. Events with very high volume or many properties can take around 12 hours.
- **Notification:** The person who turned on 2-year history receives an email notification when processing is complete. You can also check the **History** column on the **Custom Events** page.

You can keep using the event's most recent 30 days of data in calculated filters while processing runs.

**Tip:**


Turn on 2-year history a day or more before you plan to launch a campaign or Canvas that relies on a long lookback window.



If processing fails, an error icon appears next to the event. Contact your customer success manager for help.

## Usage limits

- Each workspace can turn on 2-year history for up to 100 custom events.
- If you reach the limit, turn off 2-year history for an event you no longer need before turning it on for another.

## Frequently asked questions

### Do I need to turn on 2-year history separately for each event property?

No. Turning on 2-year history for a custom event covers all of its properties.

### Do I need to turn this on for the same event each time I use it in a calculated filter?

No. After an event has 2-year history, every calculated filter in the workspace can use it with the extended lookback window.

### Can I use an event in a calculated filter while processing is still running?

Yes, but with a time window of 30 days or less. Longer time windows become available after processing finishes.

### Does this affect Segment Extensions?

No. Segment Extensions continue to work as they do today.
