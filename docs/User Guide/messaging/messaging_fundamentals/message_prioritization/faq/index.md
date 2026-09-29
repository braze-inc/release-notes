# Frequently asked questions

> This article provides answers to frequently asked questions about Message Prioritization.

## General

### How are ties in priority broken between messages that match the same prioritization rule? {#how-are-ties-in-priority-broken-between-messages-in-the-same-category}

Campaigns and Canvases break ties differently.

For campaigns, if multiple messages match the same prioritization rule, Braze prioritizes the campaign whose retry window ends soonest. For recurring campaigns, the send time is calculated as the next occurrence as of midnight in company time. For campaigns scheduled in local time, Braze assumes a send time in company time.

For Canvases, if multiple messages match the same prioritization rule, Braze prioritizes the Canvas that the user entered first. This way, all steps in the same Canvas keep the same relative priority against other campaigns and Canvases.

### Can a high-priority opted-in message lose room in a frequency cap to a message that isn't opted in? {#priority-frequency-cap-faq}

Yes. Ranking applies only among opted-in messages on the same cap. A message that follows frequency capping rules but is not opted in can send earlier and count toward the cap. A later opted-in message, including one at Priority 1, cannot send after that cap is reached.

If those messages should compete on priority, opt the earlier send into Message Prioritization. If it should not count toward the cap, opt it out of frequency capping and select **Don't count this Campaign toward the frequency capping send limit** (or **Don't count this Canvas toward the frequency capping send limit** for Canvases). For an example, see [Opted-in and not opted-in messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization#opted-in-and-not-opted-in-messages).

### How can I make sure a message always attempts to send? {#how-can-i-make-sure-a-message-is-always-sent}

Opt the message out of Message Prioritization first, then opt it out of frequency capping. You can't turn off frequency capping while a message is opted in to Message Prioritization. After both are off, the message always attempts to send on its schedule or trigger.

After you turn **Frequency Capping** off, choose whether the send still counts toward the cap:

- **Count this Campaign toward the frequency capping send limit** (or **Count this Canvas toward the frequency capping send limit** for Canvases): The message always attempts to send, but it still counts toward the cap and can block other messages, including opted-in ones.
- **Don't count this Campaign toward the frequency capping send limit** (or **Don't count this Canvas toward the frequency capping send limit** for Canvases): The message always attempts to send and doesn't count toward the cap. Use this for legal and transactional messages.

For those delivery-setting steps, see [Delivery rules](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-rules). Identify these messages before you configure; see [Plan your setup](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization#plan-your-setup).

### When are messages actually prioritized? Is there a schedule?

Each message is prioritized based on when it is expected to send. There is no universal evaluation time for opted-in messages.

### How does Braze predict when a future message sends?

Braze predicts future send timing differently for each message type:

- **Scheduled campaigns:** Braze uses the time each campaign is expected to send. For scheduled campaigns that use Intelligent Timing, Braze uses each user's optimal send time for that campaign occurrence.
- **Action-based campaigns:** Braze uses the time each triggered message is expected to send, including any configured delay between trigger and send.
- **Canvas steps:** Braze uses the user's Canvas entry or current Canvas position, plus the timing of downstream steps. For Canvas Message steps that use Intelligent Timing, after a user enters that step, Braze uses the per-user send time it calculates for that user. For following Message steps on the same deterministic path, Braze uses that Intelligent Timing send time when determining later expected send timing. Before a user reaches the step with Intelligent Timing, prediction remains best-effort.

### My message was scheduled to send already, but it hasn't yet because of rate limiting or other delays. What does this mean for prioritizing other campaigns? {#message-sent-priority-faq}

While your message is still processing, Braze treats it as sent at its originally scheduled time when deciding whether other opted-in messages can send. When that message does ultimately send, Braze uses the actual send time.

### My message was selected to send but aborted last-minute. What does that mean for prioritization? {#message-abort-faq}

When a message is selected to send, Braze assumes it was sent at its originally scheduled time. In general for Message Prioritization, avoid using Liquid aborts. If a message is aborted due to [`abort_message` Liquid logic](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), Braze assumes it was sent to that user and prioritizes future campaigns accordingly.

Let's say you have two messages: Message 1 and Message 2. If Message 1 isn't selected to send because a higher-priority Message 2 is expected later, this doesn't guarantee that Message 2 actually sends. Message 2 can still abort for any reason, including:

- Liquid abort messages
- The user no longer being in the segment
- A frequency cap reached by a message that isn't opted in to Message Prioritization

If Message 2 aborts, Braze doesn't immediately try Message 1 again. If Message 1 has a retry window, Braze tries it again the next day.

A user can receive a lower-priority message but not a higher-priority one on the same frequency capping rule when:

- The higher-priority message was frequency capped by a different rule.
- The higher-priority message conflicted with another, future campaign of even higher priority for a different frequency capping rule.
- At the time of the lower-priority message send, the user was not in the audience for the higher-priority message.
- Both messages should have been able to send, but a message that is not opted in sent before the higher-priority campaign could send and used the frequency cap. This is expected unless you opt that message in to Message Prioritization or exclude it from the cap. See [Opted-in and not opted-in messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization#opted-in-and-not-opted-in-messages).

### How does Intelligent Timing work with Message Prioritization?

For campaigns, Message Prioritization uses each user's optimal send time for the current occurrence. For Canvas Message steps, Braze uses each user's calculated send time after the user reaches the step, and reflects that timing in following Message steps on the same deterministic path. For details, see [Intelligent Timing](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization#intelligent-timing).

### Is there any reporting or analytics functionality specific to Message Prioritization?

Yes. For abort meaning, Report Builder metrics, Currents events, and how to diagnose ranking outcomes, see [Message Prioritization reporting](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/message_prioritization/reporting).

Braze also provides Message Prioritization-related events in Currents and data sharing for supported channels, including email, LINE, push notifications, SMS, webhooks, and WhatsApp. These include Message Prioritization aborts and frequency cap aborts, logged as the `users.messages.<channel>.Abort` event, as well as retry events that show when a message was later retried within the configured retry window, logged as the `users.messages.<channel>.Retry` event.

You can also use Messaging Observability and existing [Braze reporting functionality](https://www.braze.com/docs/user_guide/analytics/reports) to monitor the health and performance of your opted-in campaigns and Canvases.

## Reporting

### My prioritized message won a ranking but still didn't send. What happened?

Message Prioritization is evaluated in real time when each message attempts to send. Braze checks the current message against a predicted list of higher-ranked messages and doesn't select it to send if sending now would block any of them. That prediction is not always accurate. If a lower-ranked message isn't selected to send because a higher-ranked message is expected later, the higher-ranked message itself may still not send. Common causes include:

- A Liquid [`abort_message`](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) tag canceling the send based on template logic
- The user leaving the target segment before the send
- A frequency cap reached by a message that isn't opted in

If the higher-ranked message later aborts, it doesn't count toward the frequency cap. Braze does not keep a list of lower-ranked messages that weren't selected to send because of that higher-ranked send, and it does not send them automatically when the higher-ranked message aborts. If those lower-ranked messages have a retry window, Braze retries them each day until the window ends.

A message that isn't opted in works differently: if it sends, it counts toward the cap, even though it was never ranked.

Avoid [`abort_message` Liquid](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) on messages opted into Message Prioritization.

### A Canvas Message step was aborted by Message Prioritization. What happens to that user's Canvas journey?

By default, when a Message step in a Canvas is aborted (including by Message Prioritization), the user advances to later steps.
