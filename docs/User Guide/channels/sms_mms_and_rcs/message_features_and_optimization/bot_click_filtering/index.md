# SMS and RCS bot click filtering

> SMS and RCS bot click filtering enhances campaign analytics and workflows by excluding suspected bot clicks. A “bot click” refers to automated clicks on shortened links in SMS and RCS messages, such as those from web crawlers, Android and iOS link previews, or CPaaS security software. This feature facilitates accurate reporting, segmentation, and orchestration to engage real users. <br><br> For email campaign bot click filtering, refer to [Bot filtering for emails](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/email_preferences/bot_filtering).

## How it works

Braze has a proprietary detection system that uses multiple inputs to identify suspected bot clicks, also known as non-human interactions (NHI). Bot clicks can inflate click rates, skewing engagement metrics. By filtering these, Braze facilitates the capture of reliable data for decision making.

User agent and IP address checks work together. A click is flagged if it matches either check. If both match, Currents records both reasons.




Our system analyzes user agents associated with web crawlers, Android and iOS link previews, or CPaaS security software. A few examples of filtered user agents include `GoogleBot`, `GoogleMessages/20`, `python-requests/2.32.3`, and `Barracuda Sentinel (EE)`.




Braze also checks the IP address of each click against a list of known automated link scanners. Some scanners, such as carrier security systems, open every shortened link as soon as a message is delivered and use the same user agents as regular web browsers. Clicks from these IP addresses are flagged as suspected bot clicks even when the user agent looks like a real browser. Real users on the same browsers are still counted because Braze matches the scanner's IP address, not the browser.




## Affected metrics and workflows

The following Braze metrics and workflows are impacted by bot clicks:

- **_Total Clicks_:** Campaign analytics and Canvas analytics exclude bot clicks, reflecting only human interactions.
- **Segmentation filters:** Segment filters referencing SMS link interactions exclude bot clicks for more accurate retargeting in campaigns and Canvases.
- **Orchestration:** Bot clicks are filtered from action-based triggers and Canvas Action Paths steps that reference SMS link interactions, allowing for triggers to reflect human behavior.
- **Braze Intelligence:**
    - **Optimize with BrazeAI™:** Excludes bot clicks when optimizing variant selection.
    - **Intelligent channel:** Excludes bot clicks when SMS or RCS is selected for accurate channel selection.
    - **Experiment steps:** Excludes bot clicks for reliable experiment outcomes.
    - **Currents data exports:** Includes `is_suspected_bot_click` and `suspected_bot_click_reason` fields to help analyze human versus bot clicks. These fields are available in [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents), [Snowflake Data Sharing](https://www.braze.com/docs/partners/data_and_analytics/data_warehouses/snowflake), and [Query Builder](https://www.braze.com/docs/user_guide/analytics/reports/query_builder).

Unsubscribes from suspected bot clicks are unaffected. Braze processes all unsubscribe requests as usual. 

## Currents fields in SMS click events

Braze includes the following Currents fields for SMS click events:

| Field | Data type | Description |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolean | Indicates if the click is a suspected bot click. For SMS and RCS short-link clicks, Braze evaluates bot detection on every click and populates this field with `true` or `false`. |
| `suspected_bot_click_reason` | String, Array | The reasons a click was flagged as a suspected bot click. Possible values: `User-Agent`, `IP Address`. A click can have more than one reason. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Currents fields in SMS click events" }

## Query Builder template

For help analyzing your data, you can use the pre-built mobile template **SMS click events by bots** in [Query Builder](https://www.braze.com/docs/user_guide/analytics/reports/query_builder/query_templates).

## Frequently asked questions

### How does bot click filtering impact campaign performance?

Bot click filtering runs automatically for SMS and RCS shortened-link clicks. Dashboard click rates exclude suspected bot clicks, so reported rates reflect human interactions rather than automated link previews or crawler traffic.

### Does bot click filtering prevent bots from clicking unsubscribe links?

No. All unsubscribe requests are processed as usual.

### Are link previews included in bot click filtering?

Yes. Link previews (such as Android and iOS link previews) are flagged as bot clicks and filtered out.

### Why did my SMS click rate drop?

The drop reflects removed bot traffic, not lower engagement from real users. If your recipients use a mobile carrier that scans links automatically, Braze filters those scanner clicks by IP address. Your reported click rate may drop from the date this filtering was applied to your account. 

### Are past clicks reclassified?

No. IP-based filtering applies only to clicks recorded after it was turned on. Past clicks and existing campaign and Canvas analytics don't change.
