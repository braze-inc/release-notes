<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

<div id='api_irkkkbzedhuu' class='api_div'>
<h3 id="variation">Variation</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p><span class="calculation-line">Calculation: Count</span></p>

</div>

<div id='api_ruirmjvmmrlz' class='api_div'>
<h3 id="emailable">Emailable</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p><span class="calculation-line">Calculation: Count</span></p>

</div>

<div id='api_djzsegbscuak' class='api_div'>
<h3 id="audience-">Audience %</h3>

<div class="api_tags" data-tags="Percentage" data-tags-lower="percentage"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p><span class="calculation-line">Calculation: (Number of Recipients in Variant) / (Unique Recipients)</span></p>

</div>

<div id='api_nmhftkxbhdwp' class='api_div'>
<h3 id="unique-recipients">Unique Recipients</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>This number is received from Braze.</p>

<p><span class="calculation-line">Calculation: Count</span></p>

</div>

<div id='api_twybaxfqbajp' class='api_div'>
<h3 id="sends">Sends</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>This metric is provided by Braze.</p>

<p><span class="calculation-line">Calculation: Count</span></p>

</div>

<div id='api_cvlgvgnbygnf' class='api_div'>
<h3 id="messages-sent">Messages Sent</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>This metric is provided by Braze.</p>

<p><span class="calculation-line">Calculation: Count</span></p>

</div>

<div id='api_osmucikoiroy' class='api_div'>
<h3 id="deliveries">Deliveries</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>For emails, <em>Deliveries</em> is the total number of messages (Sends) successfully sent to and received by emailable parties.</p>

<p><span class="calculation-line">Calculation: (Sends) - (Bounces) </span></p>

</div>

<div id='api_ndxrniosxzrz' class='api_div'>
<h3 id="deliveries-">Deliveries %</h3>

<div class="api_tags" data-tags="Percentage" data-tags-lower="percentage"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p><span class="calculation-line">Calculation: (Sends - Bounces) / (Sends) </span></p>

</div>

<div id='api_ucvakcjiqyyi' class='api_div'>
<h3 id="bounces">Bounces</h3>

<div class="api_tags" data-tags="Count, Percentage" data-tags-lower="count, percentage"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>For email, <em>Bounce %</em> or <em>Bounce Rate</em> is the percentage of messages that were unsuccessfully sent or designated as “returned” or “not received” from send services used or not received by the intended emailable users.</p>

<p>An email bounce for customers using SendGrid consists of hard bounces, spam (<code class="language-plaintext highlighter-rouge">spam_report_drops</code>), and emails sent to invalid addresses (<code class="language-plaintext highlighter-rouge">invalid_emails</code>).</p>

<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Bounces</i>:</b> Count</li>
        <li><b><i>Bounce %</i> or <i>Bounce Rate %</i>:</b> (Bounces) / (Sends)</li>
    </ul>
</span>

</div>

<div id='api_qaqnfahapbad' class='api_div'>
<h3 id="hard-bounce">Hard Bounce</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>When an email hard bounces or is marked as spam, Braze marks the email address as invalid but does not update the user’s <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/">subscription status</a>. Braze stops any future sends to that email address. To remove an email address from your hard bounce list, use the <a href="/docs/api/endpoints/email/post_remove_hard_bounces">Remove hard bounced emails endpoint</a>.</p>

<p><span class="calculation-line">Calculation: Count </span></p>

</div>

<div id='api_qvucbbzckdcp' class='api_div'>
<h3 id="soft-bounce">Soft Bounce</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>If an email receives a soft bounce, we will usually retry within 72 hours, but the number of retry attempts varies from receiver to receiver.</p>

<p>While soft bounces aren’t tracked in your campaign analytics, you can monitor the soft bounces in the <a href="/docs/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/">Message Activity Log</a> or exclude these users from your sending with the <a href="/docs/user_guide/audience/segments/segmentation_filters#soft-bounced">Soft Bounced segment filter</a>. In the Message Activity Log, you can also see the reason for the soft bounces and understand possible discrepancies between the “sends” and “deliveries” for your email campaigns.</p>

<p><span class="calculation-line">Calculation: Count </span></p>

</div>

<div id='api_zvaaxyagawpi' class='api_div'>
<h3 id="spam">Spam</h3>

<div class="api_tags" data-tags="Count, Percentage" data-tags-lower="count, percentage"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Spam</i>:</b> Count</li>
        <li><b><i>Spam %</i> or <i>Spam Rate %</i>:</b> (Marked as Spam) / (Sends)</li>
    </ul>
</span>

</div>

<div id='api_mgizcrzsiepg' class='api_div'>
<h3 id="unique-opens">Unique Opens</h3>

<div class="api_tags" data-tags="Count, Percentage" data-tags-lower="count, percentage"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>For email, this is tracked over a seven-day period. This means a single user who opens the same email again after seven days counts as a new unique open. As a result, dashboard unique open counts may be higher than a simple <code class="language-plaintext highlighter-rouge">DISTINCT user_id</code> query on Currents data. To match dashboard counts from Currents, filter for events where <code class="language-plaintext highlighter-rouge">is_unique</code> is <code class="language-plaintext highlighter-rouge">true</code>.</p>

<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unique Opens</i>:</b> Count</li>
        <li><b><i>Unique Opens %</i> or <i>Unique Open Rate</i>:</b> (Unique Opens) / (Deliveries)</li>
    </ul>
</span>

</div>

<div id='api_gamyfiwhtuss' class='api_div'>
<h3 id="unique-clicks">Unique Clicks</h3>

<div class="api_tags" data-tags="Count, Percentage" data-tags-lower="count, percentage"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>This is tracked over a seven-day period for email and measured by <a href="/docs/help/help_articles/data/dispatch_id/">dispatch_id</a>. This includes clicks on Braze-provided unsubscribe links. After seven days, another unique click can count for the same user if they click again. To match dashboard counts from Currents, filter for events where <code class="language-plaintext highlighter-rouge">is_unique</code> is <code class="language-plaintext highlighter-rouge">true</code>.</p>

<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unique Clicks</i>:</b> Count</li>
        <li><b><i>Unique Clicks %</i> or <i>Click Rate</i>:</b> (Unique Clicks) / (Deliveries)</li>
    </ul>
</span>

</div>

<div id='api_mkqilohvejjm' class='api_div'>
<h3 id="unsubscribers-or-unsub">Unsubscribers or Unsub</h3>

<div class="api_tags" data-tags="Count, Percentage" data-tags-lower="count, percentage"></div>

<p><em>Unsubscribes</em> reflect the standard unsubscribe link for Braze. Custom unsubscribe pages won’t increment this metric unless you update users using the API. <strong>Subscription Group Timeseries</strong> still reflects API-driven changes.</p>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Unsubscribers</i> or <i>Unsub</i>:</b> Count</li>
        <li><b><i>Unsubscribers %</i> or <i>Unsub Rate</i>:</b> (Unsubscribes) / (Deliveries)</li>
    </ul>
</span>

</div>

<div id='api_hqvrkiwfdjyg' class='api_div'>
<h3 id="revenue">Revenue</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p><span class="calculation-line">Calculation: Count </span></p>

</div>

<div id='api_wdtnodnpekee' class='api_div'>
<h3 id="primary-conversions-a-or-primary-conversion-event">Primary Conversions (A) or Primary Conversion Event</h3>

<div class="api_tags" data-tags="Count, Percentage" data-tags-lower="count, percentage"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>For email, push, and webhooks, we start tracking conversions after the initial send.</p>

<span class="calculation-line">
    Calculation:
    <ul>
        <li><b><i>Primary Conversions (A)</i> or <i>Primary Conversion Event</i>:</b> Count</li>
        <li><b><i>Primary Conversions (A) %</i> or <i>Primary Conversion Event Rate</i>:</b> (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>

</div>

<div id='api_tozjkldoucmu' class='api_div'>
<h3 id="confidence">Confidence</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

</div>

<div id='api_bclsutfbxnsy' class='api_div'>
<h3 id="machine-opens">Machine Opens</h3>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.</p>

<p><span class="calculation-line">Calculation: Count </span></p>

</div>

<div id='api_qozkiautvdhi' class='api_div'>
<h3 id="other-opens">Other Opens</h3>

<div class="api_tags" data-tags="Count" data-tags-lower="count"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p>Note that a user can also open an email (such as the open counts toward <i>Other Opens</i>) before a <i>Machine Opens</i> count is logged. If a user opens an email once (or more) after a machine open event from a non-Apple Mail inbox, then the amount of times that the user opens the email is calculated toward <i>Other Opens</i> and only once toward <i>Unique Opens</i>.</p>

<p><span class="calculation-line">Calculation: Count </span></p>

</div>

<div id='api_rdanmuakwqhf' class='api_div'>
<h3 id="click-to-open-rate">Click-to-Open Rate</h3>

<div class="api_tags" data-tags="Percentage" data-tags-lower="percentage"></div>

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

<p><span class="calculation-line">Calculation: (Unique Clicks) / (Unique Opens) (for Email)</span></p>

</div>