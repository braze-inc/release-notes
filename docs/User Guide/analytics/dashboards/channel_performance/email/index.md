# Email performance dashboards

> The Email Performance and Email Insights dashboards show aggregate email metrics across campaigns and Canvases.

For filters, time-period comparison, and other settings that apply across channels, see [Channel performance dashboards](https://www.braze.com/docs/channel_performance).

## Prerequisites

To view these dashboards, you need the "View Usage Data" or "View Dashboard Reports" [permission](https://www.braze.com/docs/user_guide/administer/global/user_management/permissions) for your workspace.

## Email performance dashboard {#email-performance-dashboard}

View your email performance dashboard by going to **Analytics** > **Email Performance**, and selecting the date range for the period you want to view data. Your date range can be up to one year in the past.

![Email performance dashboard displaying email channel engagement from the last thirty days.](https://www.braze.com/docs/assets/img_archive/email_performance_dashboard_1.png?6f51d7e3f0dd384a3a2614be9cf5d77c)

![An example email campaign with 335,630 sends, with an average of 11,187.667 per day.](https://www.braze.com/docs/assets/img_archive/email_performance_dashboard_2.png?c69633137073334f4c8ac2caa3e37def){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

### How metrics are calculated {#how-metrics-are-calculated}

The calculations for different metrics in the  performance dashboard are the same as those on an individual message level (such as campaign analytics). On this dashboard, the metrics are aggregated across all campaigns and Canvases for the date range you've selected. 

 Each tile also shows the [comparison to the last period](#comparing-time-periods).


| Metric | Type | Calculation |
| --- | --- | ---- |
| Sends | Count | Total number of sends across each day in the date range |
| Delivery rate | Rate | (Total number of deliveries across each day in the date range) / (Total number of sends across each day in the date range) |
| Bounce rate | Rate | (Total number of bounces across each day in the date range) / (Total number of sends across each day in the date range) |
| Unsubscribe rate | Rate | (Total number of unique unsubscribes across each day in the date range) / (Total number of deliveries for a date range)<br><br>This uses unique unsubscribes, which is also used in Campaign Analytics, Overview, and Report Builder. These unsubscribes are logged across all sources (such as the REST API, CSV imports, emails, and list unsubscribes). The unsubscribe rates in Campaign and Canvas analytics are unsubscribes that occur as a result of an unsubscribe click on a Braze-delivered email.  |
| Unique open rate | Rate | (Total number of unique opens across each day in the date range) / (Total number of deliveries for a date range) |
| Other opens rate | Rate | (Total number of total other opens across each day in the date range) / (Total number of deliveries for date range)<br><br>Other opens includes emails that haven't been identified as machine opens, such as when a user opens an email. This metric is non-unique and is a sub-metric of total opens.  |
| Unique click rate | Rate | (Total number of unique clicks across each day in the date range) / (Total number of deliveries for a date range) |
| Unique click to open rate | Rate | (Total number of unique clicks across each day in the date range) / (Total number of unique opens across each day in the date range) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="How metrics are calculated" }

## Email insights dashboard {#email-insights-dashboard}

The email insights dashboard tracks where and when your customers are interacting with your emails. These reports can provide rich and granular data on how to optimize your emails to drive greater engagement. The email insights dashboard includes up to the last six months of data. To access the dashboard, go to **Analytics** > **Email Performance** > **Email Insights**.

### Engagement by Device

The **Engagement by Device** report provides a breakdown of what devices your users are using to engage with your email. This data tracks email engagement across mobile, desktop, tablet, and other device types. This data is based on the user agent string passed from your users' devices.

**Note:**


If you use CloudFront as your CDN, make sure your users' user agent is passed along to the ESP. Otherwise, every user agent will be "Amazon Cloudfront".



The “Other” category includes any user string that cannot be identified as desktop, mobile, or tablet. For example, television, car, video game console, OTT (over-the-top or streaming), and similar. This may also include null or empty values.

To better understand what is in this "Other" category, you can extract the user agents using either of these options:

1. [Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents) sends you the exact user agent string retrieved from your users' devices.
2. Use the [Query Builder](https://www.braze.com/docs/user_guide/analytics/reports/query_builder) to use SQL or [generate SQL with Operator](https://www.braze.com/docs/user_guide/analytics/reports/query_builder#generating-sql-with-operator) to view the user agents.

![Engagement by Device report that shows the number of clicks for mobile, desktop, tablet, and other devices. The most number of clicks occurs on mobile devices.](https://www.braze.com/docs/assets/img/engagement_by_device_type.png?5a5e8fbdc8837e2756a99e6131eeabfc){: style="max-width:70%;"}

For email opens, Braze separates Google Image Proxy, Apple Image Proxy, and Yahoo Mail Proxy. These services cache and load all embedded images in an email before it’s delivered to the recipient. As a result, this triggers an email open from the mailbox provider’s servers rather than the recipient’s server, which can lead to inflated email opens. These services enhance privacy, security, performance, and efficiency when loading images. This can also contain real opens from recipients, as these proxy services mask the user agent, and Braze categorizes proxy data using the user agent.

![Engagement by Device report that shows the number of clicks for Mobile, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy, and Other. The most number of opens occurs on mobile devices.](https://www.braze.com/docs/assets/img/engagement_by_device_type_proxy.png?db5429af343befdb3af3d7cf26d0ae3c){: style="max-width:70%;"}

### Engagement by Mailbox Provider

The **Engagement by Mailbox Provider** report displays the top mailbox providers contributing to your clicks or opens. You can select specific premier mailbox providers to view specific receiving domains. For example, if Microsoft is listed on this report as one of your top mailbox provider metrics, you can further view details for their receiving domains, such as "outlook.com", "hotmail.com", "live.com", and more.

![An example Engagement by Mailbox Provider report with Google, Apple iCloud, Yahoo, Microsoft, and Mail.Ru Group and their corresponding number of clicks.](https://www.braze.com/docs/assets/img_archive/mailbox_provider_time_engagement.png?784f80e08b3491b19ebfb5b7a1f10809){: style="max-width:70%;"}

### Time of Engagement

The **Time of Engagement** report displays data on when users are engaging with your emails. This can help answer questions such as which weekday or what time sees the highest engagement from your customers. With these insights, you can experiment with the best day or time to send your messages to drive higher engagement. Note that these times are based on your company’s time zone.

The **Day of the week** engagement report breaks down opens or clicks by day of the week. 

![An example Day of the week engagement report with the most clicks on Monday and Wednesday.](https://www.braze.com/docs/assets/img_archive/time_engagement.png?a5e54677fee5f9c0cfbbad9b2c847775)

The **Time of the day** engagement report breaks down opens or clicks by each hour in a 24-hour time window.

![An example Time of the day engagement report with the opens or clicks from 12 am to 11 pm.](https://www.braze.com/docs/assets/img_archive/time_engagement_day.png?e3b7db8e1491bded5f6f3acd7fecda4f)

For more information on analytics for your emails, check out [Email reporting](https://www.braze.com/docs/user_guide/channels/email/reporting).

## Frequently asked questions {#frequently-asked-questions}

### Why does my email dashboard display more Other Opens than Unique Opens? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

For the _Unique Opens_ metric, Braze deduplicates any repeat opens registered by a given user (whether they include _Machine Opens_ or _Other Opens_) so that only a single _Unique Open_ is incremented if a user opens multiple times. For _Other Opens_, Braze does not deduplicate.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/channel_performance"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Channel performance dashboards</span></span></div></a></li><li><a href="/docs/user_guide/analytics/dashboards/channel_performance/sms_mms_rcs"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">SMS/MMS/RCS performance</span></span></div></a></li><li><a href="/docs/user_guide/analytics/dashboards/channel_performance/push"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Push performance</span></span></div></a></li><li><a href="/docs/user_guide/channels/email/reporting"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Email reporting</span></span></div></a></li></ul>
