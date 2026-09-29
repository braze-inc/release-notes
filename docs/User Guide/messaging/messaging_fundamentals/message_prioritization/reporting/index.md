# Message Prioritization reporting

> After you opt campaigns or Canvases into Message Prioritization, use this page to read ranking outcomes, understand available Report Builder metrics, and decide what to change when the mix looks wrong.

For how ranking, look-ahead, and retry windows work, see [Message Prioritization](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization).

## What an abort means

A Message Prioritization abort means your prioritization rules allocated frequency cap capacity to a higher-ranked message instead of this one.

Each opted-in message that shares a [frequency capping](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping) rule follows this sequence:

1. If sending it won't prevent a higher-priority message from sending within the cap, it sends.
2. Otherwise, if a retry window is set, Braze tries it again the next day.
3. If it never sends (no retry window, or retries are exhausted), it is logged as a Message Prioritization abort.

The same user can record more than one Message Prioritization abort in a date range if multiple opted-in messages never send.

### How this abort differs from other aborts

Knowing which abort type applies tells you where to look and how to read the outcome.

| Abort | What it means |
| --- | --- |
| Message Prioritization abort | Prioritization rules stop this send. In Report Builder, this is *Message Prioritization Aborts*. In [Messaging Observability](https://www.braze.com/docs/user_guide/analytics/dashboards/dashboard_builder/messaging_observability), this is `Aborted due to priority`. In Currents, `abort_type` is `deprioritized`. |
| Frequency cap abort | The user already reached the maximum for a frequency capping rule, leaving no capacity to allocate. In Messaging Observability, this is `Frequency capped`. In Currents, `abort_type` is `frequency_capped`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="How Message Prioritization aborts differ from other aborts" }

## Where to look

Different surfaces give you different levels of detail into the same ranking outcomes.

| Surface | What it shows |
| --- | --- |
| Report Builder | *Message Prioritization Aborts*, *Message Prioritization Abort Rate*, *Total Retry Attempts*, and *Average Retries per Message* |
| Campaign and Canvas analytics | *Message Prioritization Aborts* |
| Messaging Observability | `Aborted due to priority` |
| Currents | `users.messages.<channel>.Abort` and `users.messages.<channel>.Retry` for email, LINE, push, SMS, webhooks, and WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Where Message Prioritization outcomes appear" }

Messaging History does not log Message Prioritization aborts or retries. Use Report Builder, Messaging Observability, or Currents to investigate ranking aborts.

## Metrics

These four metrics are available in Report Builder.

| Metric | Definition | Formula |
| --- | --- | --- |
| *Message Prioritization Aborts* | Number of messages that didn't send because they were aborted by priority rules. Includes messages with no retry window and messages that exhausted their retries. | Count |
| *Message Prioritization Abort Rate* | Percentage of send and abort outcomes that were aborted by priority rules. One user can contribute more than one abort. | *Message Prioritization Aborts* / (*Messages Sent* + *Message Prioritization Aborts*) |
| *Total Retry Attempts* | Number of times messages with a retry window were scheduled to try sending again after being aborted by priority rules or frequency caps. A retry can still lose and never send. | Count |
| *Average Retries per Message* | Average number of retries per message across all sends, including those not opted into Message Prioritization. | *Total Retry Attempts* / *Messages Sent* |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Message Prioritization metrics" }

There's no target abort rate to aim for. A high rate on a high-ranked message might mean your prioritization rules are doing their job—or it might mean the shared cap is too tight for your send volume. Use [Diagnose what you're seeing](#diagnose-what-youre-seeing) to figure out which.

## Set up a monitoring report

Use Report Builder to review opted-in campaigns and Canvases together.

1. Go to **Analytics** > **Report Builder**.
2. Select **Create report**.
3. In **Rows**, select **Campaigns and Canvases**.
4. In **Columns**, select **Customize Metrics**. Add *Messages Sent*, *Message Prioritization Aborts*, *Message Prioritization Abort Rate*, *Total Retry Attempts*, and *Average Retries per Message*.
5. Set the date range in **Report content**.
6. Add the campaigns and Canvases you opted into Message Prioritization. To filter that set, use a tag you already apply to those messages.
7. Select **Save and run**.
8. Re-run the report weekly.

For Report Builder controls and metric availability, see [Report Builder](https://www.braze.com/docs/user_guide/analytics/reports/report_builder).

## Diagnose what you're seeing

Match what you see in your report to a likely cause, then use the recommended action to adjust your setup.

| What you see | Likely cause | What to change |
| --- | --- | --- |
| High abort rate on a high-ranked campaign or Canvas | The message shares a cap with a high-volume higher-ranked send, a message outside Message Prioritization used the cap, or look-ahead could not see the later send. | Check volume from higher-ranked opted-in messages and from messages not opted into Message Prioritization on that cap. If the send is in a Canvas, check [boundary steps](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization#evaluating-canvases) that stop look-ahead. Add a [frequency capping rule filtered by category](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization#frequency-capping-rules) if one category is using every send. If a later send is acceptable, set or lengthen a [retry window](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization#retry-windows). |
| High retries and high final aborts | The cap stays full for the whole retry window, or the retry window collides with a recurring send. | Lengthen the retry window, lower volume on higher-ranked sends, or change the cap. For recurring campaigns, the retry window must be shorter than the gap between sends. See [Retry windows](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization#retry-windows). |
| Zero aborts across opted-in messages | The messages don't share a frequency capping rule, aren't opted in, or the cap is high enough that ranking never has to choose. | Confirm the campaigns and Canvases are opted in and share a frequency capping rule. If they are, audit which messages are competing under that cap. Zero aborts is expected when send volume is low. |
| Lower-ranked send went out, higher-ranked did not | The higher-ranked message counts toward a different frequency capping rule, an even higher-ranked future send, audience mismatch, or a message outside Message Prioritization used the cap earlier. | See [Can a high-priority opted-in message lose room in a frequency cap to a message that isn't opted in?](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization/faq#priority-frequency-cap-faq) and [My message was selected to send but aborted last-minute](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization/faq#message-abort-faq). |
| Aborts on a message that must always attempt to send | The message may have been accidentally opted into Message Prioritization. Only opt in messages that can send late or occasionally not send. Transactional, legal, or time-critical messages should always attempt to send regardless of ranking. | Opt the message out of Message Prioritization and frequency capping. See [How can I make sure a message always attempts to send?](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization/faq#how-can-i-make-sure-a-message-is-always-sent). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Diagnose Message Prioritization outcomes" }

## Currents

Ranking outcomes appear in Currents as `users.messages.<channel>.Abort` and `users.messages.<channel>.Retry` for email, LINE, push, SMS, webhooks, and WhatsApp.

`Abort` includes more than ranking. To isolate Message Prioritization ranking aborts, filter on `abort_type: deprioritized`. Frequency cap aborts on the same cap use `abort_type: frequency_capped` and are not ranking outcomes. See [Abort types](https://www.braze.com/docs/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#abort-types) for more details.

`Retry` events appear when a message is scheduled to retry within its retry window, not necessarily when it sends. See [Message engagement events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/messaging_fundamentals/message_prioritization"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Message Prioritization</span><span class="guide_tile_description">How ranking, look-ahead, and retry windows work</span></span></div></a></li><li><a href="/docs/user_guide/messaging/messaging_fundamentals/frequency_capping"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Rate limiting and frequency capping</span><span class="guide_tile_description">How frequency caps limit send volume across channels</span></span></div></a></li><li><a href="/docs/user_guide/analytics/reports/report_builder"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Report Builder</span><span class="guide_tile_description">Build custom reports for campaigns and Canvases</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Abort messages</span><span class="guide_tile_description">Use Liquid to cancel a message before it sends</span></span></div></a></li><li><a href="/docs/user_guide/analytics/dashboards/dashboard_builder/messaging_observability"><div class="guide_tile guide_tile_has_description"><span class="guide_tile_text"><span class="guide_tile_title">Messaging Observability</span><span class="guide_tile_description">Monitor delivery health and aborted sends</span></span></div></a></li></ul>
