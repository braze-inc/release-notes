# Refresh profile data in Canvas before you send

> When a journey lasts days or weeks, profile data can change after the user entered the Canvas. Use a Context step to look up the matching object on the profile, then branch messaging with Audience Paths or Decision Split.

## About this example

ClaimsJumpr, a fictional insurance brand, starts an action-based Canvas when a policy is 28 days from renewal. Over those 28 days, ClaimsJumpr sends several reminders. A policyholder can change auto-renewal on that policy after they enter, so messages that only use Canvas entry properties can describe the wrong status.

Each user profile stores policies as an array of objects custom attribute (`policies`). Each object includes a unique `policy_id` in the triggering event, and an `auto_renewal` value (`opted_in` or `opted_out`). This example adds a Context step before later Message steps so Liquid reads the current object from `policies`, matching on the `policy_id` from Canvas context (the entry event).

This pattern:

1. Keeps the entry `policy_id` in Canvas context.
2. Uses a Context step and the Liquid `where` filter to select the matching object from `policies`.
3. Stores `auto_renewal` as a context variable (`auto_renewal`) with type **String**.
4. Routes copy with [Audience Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/audience_paths) or [Decision Split](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/decision_split) context variable filters—not with duplicated abort Liquid in this article.

## Considerations

- Test the Canvas in a non-production workspace, including profiles where `auto_renewal` is missing on an object.
- `policy_id` values in `policies` should be unique so `where` returns one object.
- If another Canvas uses a [User Update](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/user_update) step to write `policies` from the same trigger event, the profile may not be updated before the first message. For the first Message step after entry, use the entry context properties. Use this Context step for later steps, after the profile update has had time to apply.
- Context variable names use letters, numbers, and underscores only (up to 100 characters). You can define up to 10 variables per Context step.
- The Liquid in this article is an example. Preview user paths and test sends for your attribute names and values.

## Setup

This example assumes:

| Asset | Details |
| --- | --- |
| Entry | Action-based Canvas on a custom event such as `policy_renewal_window_started`, with event property `policy_id` |
| Custom attribute | `policies` — array of objects, each with `policy_id` and `auto_renewal` |
| Context variable | `auto_renewal` — string (`opted_in` or `opted_out`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Setup" }

### Step 1: Place a Context step before later messages

In the Canvas, add a [Context](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context) step immediately before the Message steps that must reflect the current auto-renewal status. Do not rely on entry properties alone for those later sends.

### Step 2: Define the context variable

In the Context step:

1. Set **Context variable name** to `auto_renewal`.
2. Set the data type to **String**.
3. Enter Liquid that selects the matching policy, then outputs `auto_renewal`. Do not wrap the `assign` source in extra `{{ }}` tags.


```liquid
{% assign matched_policies = custom_attribute.${policies} | where: "policy_id", context.${policy_id} %}
{{ matched_policies[0].auto_renewal }}
```


`context.${policy_id}` is the entry event property, available as a context variable. `where` keeps objects whose `policy_id` matches that value. The Context step stores the first match's `auto_renewal` field.

{: start="4"}
4. Select **Preview** and confirm the value for a test user who has that `policy_id` on `policies`.

For name, type, and Liquid limits, see [Context](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/context) and [Context variables](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

### Step 3: Branch on the context variable

After the Context step, split users with an Audience Paths or Decision Split filter on `auto_renewal` (for example, equals `opted_in` versus `opted_out`). Put the matching reminder on each path.

**Tip:**


For filter setup and data-type matching, see [Context variable filters](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables#context-variable-filters). For how groups are evaluated, see [Audience Paths](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/audience_paths) and [Decision Split](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/decision_split).



If you abort a send in a Message step instead of branching, the user still moves to the next Canvas step. For details, see [Abort messages](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) and [How users advance](https://www.braze.com/docs/user_guide/messaging/canvas/canvas_components/message_step#how-users-advance).

### Step 4: Preview and test

Use [preview user paths](https://www.braze.com/docs/user_guide/messaging/canvas/testing_canvases/preview_user_paths) and test sends for:

- `auto_renewal` of `opted_in` and `opted_out` on the matching object
- A `policy_id` that is not on `policies` (empty or blank context value)
- An object that omits `auto_renewal`

Confirm later reminders match the profile, not only the status from Canvas entry.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/canvas/canvas_components/context"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Context</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/sources/context_variables"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Context variables</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/sources/canvas_entry_properties"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Canvas entry properties</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/canvas_components/audience_paths"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Audience Paths</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/canvas_components/decision_split"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Decision Split</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/canvas_components/message_step"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Message step</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Abort messages</span></span></div></a></li><li><a href="/docs/user_guide/data/activation/attributes/array_of_objects"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Array of objects</span></span></div></a></li><li><a href="/docs/user_guide/messaging/canvas/canvas_components/user_update"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">User Update</span></span></div></a></li></ul>
