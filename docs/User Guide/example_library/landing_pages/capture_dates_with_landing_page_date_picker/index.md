# Capture dates with a landing page date picker

> Collect a calendar date on a Braze landing page with a native browser date picker, write it to the user profile as a Time custom attribute, and keep known users on one profile with the landing page Liquid tag.

## About this example

ClaimsJumpr, a fictional insurance brand, asks consumers to share their policy renewal date on a Braze landing page. Free-text date fields produce inconsistent formats that are hard to segment on. ClaimsJumpr uses a [custom form block](https://www.braze.com/docs/user_guide/messaging/landing_pages/custom_form_blocks) with an HTML date input so the browser enforces a consistent calendar value. It then writes that value as a Time custom attribute for retargeting.

This scenario combines:

- A **Custom Code** block on the landing page form
- `registerFormInput`, so the date field validates and submits with the form
- The [landing page JavaScript bridge](https://www.braze.com/docs/user_guide/messaging/landing_pages/javascript_bridge), to set a Time custom attribute
- The [landing page Liquid tag](https://www.braze.com/docs/user_guide/messaging/landing_pages/tracking_users), so known users stay on one profile

Use it when you need a calendar date on the profile for Time-based segmentation or Canvas timing. Prefer a standard [**Short Text**](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages) block when a free-text string is enough.

## Considerations

- **Short Text** form blocks bind only to string custom attributes. To store a date as a Time attribute with date filters (`before`, `after`, and `in less than`), build a custom form block and call `setCustomUserAttribute` with a JavaScript `Date`.
- Create the custom attribute with the Time data type before you test a submission. Passing a `Date` from the bridge matches that data type; see [Custom attribute data types](https://www.braze.com/docs/user_guide/data/activation/custom_data/data_types/?tab=time).
- HTML `<input type="date">` depends on the visitor's browser. Support and UI vary by browser and device (for example, some mobile browsers show a native picker; others may fall back to a text-like field). Test on the browsers your audience uses.
- Writing custom attributes consumes [data points](https://www.braze.com/docs/user_guide/data/data_points/).
- Embed the `{% landing_page_url %}` Liquid tag in the message that drives traffic to the page. Without it, submitting the form can create a new anonymous profile instead of updating the known user.
- Landing pages with forms need a confirmation experience (confirmation landing page, multi-step confirmation step, or post-submit URL). Plan that before you publish.
- If the page uses a [multi-step form](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms), place the **Custom Code** block that calls `registerFormInput` inside the **Form layout** block so the input participates in form submission.
- Test attribute writes and profile linking in a development workspace before you publish to production.

## Setup

### Step 1: Create a Time custom attribute

1. Go to **Data Settings** > **Custom Attributes**.
2. Create a custom attribute such as `policy_renewal_date` with data type **Time**.
3. Use a clear, stable name. Pass the same key to `setCustomUserAttribute` in the custom form block.

### Step 2: Build the landing page form

1. Go to **Messaging** > **Landing Pages** and create a new landing page.
2. Open the drag-and-drop editor and fill in site details (page URL, title, and related settings). See [Create landing pages](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages).
3. Add the standard form fields you need (for example, a **Short Text** field for a license plate number bound to a string custom attribute).
4. Add a **Custom Code** block for the renewal date picker. Paste the HTML, script, and styles from Step 3 into that single block.
5. Add a submit button that submits the form, and configure your confirmation experience.
6. After you've finished composition and confirmation, publish the landing page.

### Step 3: Register the date picker as a custom form input

Paste the following into one **Custom Code** (HTML) block. The script registers the date input with `registerFormInput`, validates that a date is selected, and writes a JavaScript `Date` to `policy_renewal_date` on submit.

```html
<div class="renewal-date-field">
  <label for="policy-renewal-date">Policy renewal date</label>
  <input id="policy-renewal-date" type="date" autocomplete="off" />
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    function parseDateInputValue(value) {
      const parts = value.split("-").map(Number);
      if (parts.length !== 3 || parts.some((n) => Number.isNaN(n))) {
        return null;
      }
      const [year, month, day] = parts;
      // Build a local calendar date so YYYY-MM-DD is not shifted by UTC parsing.
      return new Date(year, month - 1, day);
    }

    window.brazeHelpers.forms.registerFormInput({
      selector: "#policy-renewal-date",
      isRequired: true,
      getValue: (element) => element.value || null,
      onValidate: (value) => Boolean(parseDateInputValue(value)),
      onSubmit: (value) => {
        const date = parseDateInputValue(value);
        if (!date) {
          return;
        }
        window.brazeBridge.getUser().setCustomUserAttribute("policy_renewal_date", date);
      },
    });
  });
</script>

<style>
  .renewal-date-field {
    display: flex;
    flex-direction: column;
    gap: 8px;
    max-width: 280px;
    margin: 0 auto;
    text-align: left;
  }

  .renewal-date-field label {
    font-weight: 600;
  }

  /* Braze adds this class to the registered element when validation fails. */
  #policy-renewal-date.bz-validation-error {
    outline: 3px solid #f94144;
    outline-offset: 2px;
    border-radius: 4px;
  }
</style>
```

The browser's date input returns a `YYYY-MM-DD` string. `getValue` reads that string, and `onValidate` confirms it parses. `onSubmit` converts it to a local `Date` before calling `setCustomUserAttribute`. Braze stores that `Date` as a UTC timestamp without milliseconds. For visitors in time zones ahead of UTC, local midnight can fall on the previous calendar day. Form submission flushes bridge data to Braze after `onSubmit` completes. Leave `requestImmediateDataFlush` out of `onSubmit`.

Replace `policy_renewal_date` with your Time attribute name from Step 1. Adapt the label and styles to your brand.

### Step 4: Link known users from a Braze message

In the email, SMS, or other message that sends consumers to the landing page, insert the landing page Liquid tag so Braze can update the existing profile on submit.


```html
<a href="{% landing_page_url claimsjumpr-renewal-date %}" class="button">Share your renewal date</a>
```


Replace `claimsjumpr-renewal-date` with your landing page URL handle. In the message editor, select **Personalization**, then set **Personalization type** to **Landing Page**.

### Step 5: Test the attribute write

1. Send the message with the landing page Liquid tag to a test user, or open the tagged link from a Braze message.
2. Select a renewal date, submit the form, and check that the confirmation experience appears.
3. Open the test user's profile and verify `policy_renewal_date` is set as a Time value.
4. Optional: build a segment with a Time filter such as `in less than` or `in more than` on `policy_renewal_date` to confirm the attribute is usable for retargeting.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/landing_pages/custom_form_blocks"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Create custom form blocks on landing pages</span></span></div></a></li><li><a href="/docs/user_guide/messaging/landing_pages/javascript_bridge"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">JavaScript bridge for landing pages</span></span></div></a></li><li><a href="/docs/user_guide/messaging/landing_pages/create_landing_pages"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Create landing pages</span></span></div></a></li><li><a href="/docs/user_guide/messaging/landing_pages/tracking_users"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Track users through a form</span></span></div></a></li><li><a href="/docs/user_guide/data/activation/custom_data/data_types"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Custom attribute data types</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=landing%20pages"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Editor blocks (landing pages)</span></span></div></a></li></ul>
