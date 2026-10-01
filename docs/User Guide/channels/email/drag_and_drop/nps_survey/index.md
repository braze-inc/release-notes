# Email NPS survey block

> Use the **NPS Survey** block in the email drag-and-drop editor to ask recipients how likely they are to recommend you. Each score tile (0–10) links to a published [survey landing page](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys). When a recipient selects a score, Braze opens that landing page and records the score on arrival, then they can finish any remaining survey questions.

## Prerequisites

Before you add an email NPS survey block, you need:

| Requirement | Description |
| --- | --- |
| Landing page surveys | Access to [landing page surveys](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys) in your workspace. |
| Published NPS survey | A published survey landing page that includes an [NPS](https://www.braze.com/docs/user_guide/messaging/surveys#standalone-nps-block) form block. Unpublished pages and surveys without an NPS question don't appear in the email block picker. |
| Landing pages permission | Permission to view landing pages so you can select or change the linked survey from the block settings. |
| Drag-and-drop email | An email campaign or Canvas message step that uses the [drag-and-drop editor](https://www.braze.com/docs/user_guide/channels/email/drag_and_drop). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Email NPS survey prerequisites" }

## How it works

1. You add the **NPS Survey** content block to your email and link it to a published survey landing page that includes an NPS question.
2. Recipients see a 0–10 score scale (and editable question labels) in the email.
3. Selecting a score opens the landing page URL with that score attached.
4. Braze records the NPS score when the landing page loads, even if the recipient doesn't complete the rest of the survey. Recipients can still answer any remaining questions on the page. Partial submissions have a six-hour grace period before they appear in results, so recipients can finish the survey first.

![Example flow from an email with an NPS 0–10 score scale to a survey landing page that shows the selected score and an optional follow-up question.](https://www.braze.com/docs/assets/img/email/nps_survey/email_to_landing_page_flow.png?3a3b955094a1b24f9098c30de3268eb2)

## Create an email NPS survey

### Step 1: Publish a survey landing page with NPS

1. Go to **Messaging** > **Landing Pages** and create a survey. For the creation workflow, see [Landing page surveys](https://www.braze.com/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys).
2. Add an **NPS** form block to the survey (and any follow-up questions you want after the score). For multi-step surveys, the NPS question must be on the first step.
3. Publish the landing page. Only published survey landing pages with an active NPS question appear when you configure the email block.

### Step 2: Add the NPS Survey block to your email

1. Create or open an email in a campaign or Canvas using the drag-and-drop editor.
2. Open the **Content** panel and drag **NPS Survey** onto the canvas. The configure sidebar opens automatically. You can add only one **NPS Survey** block per email—after one is on the canvas, the content panel disables adding another.
3. Select **Add survey**, then choose your published NPS survey landing page.
4. Optionally adjust **Tile styles** (font, colors, border, and spacing). These controls unlock after you select a survey.
5. Select **Build Block**.

![Drag-and-drop email editor Content tab showing Basic Blocks, including the NPS Survey block.](https://www.braze.com/docs/assets/img/email/nps_survey/dnd_content_nps_survey_block.png?f7d409c3bdaa5c80d7da663c19ec950a)

### Step 3: Edit labels and finish the email

After you build the block, edit the question text and the low and high scale labels (for example, "Not at all likely" and "Extremely likely") directly on the canvas. Then finish the rest of your email and send a test before launch.

For the full property reference, see [NPS survey](https://www.braze.com/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email#email_nps-survey) in the email editor blocks article.

## Review responses

NPS scores collected from email clicks are survey responses on the linked landing page. Review them from:

- The landing page's survey reporting
- **Messaging** > **Surveys**

Partial submissions, including email NPS scores recorded on landing-page arrival, have a six-hour grace period before they appear in results, so recipients can finish remaining questions. For NPS analytics (promoters, passives, detractors, and score), see [Surveys](https://www.braze.com/docs/user_guide/messaging/surveys#standalone-nps-block).

## Frequently asked questions

### Why don't I see any surveys when I select **Add survey**?

The picker only lists published survey landing pages that include an NPS question. Create and publish a survey landing page with an **NPS** block, then open the picker again.

### Can recipients change their score on the landing page?

Yes. If recipients change their score and then submit the rest of the survey, Braze uses the later score.

### Why is an email NPS score still marked as partially complete?

Braze records the email NPS score when the landing page loads, but the response is partially complete until the recipient selects the final submit control on the survey—even if the survey has no questions. Partial submissions also have a six-hour grace period before they appear in results. For how completed and partially complete responses are counted, see [Surveys](https://www.braze.com/docs/user_guide/messaging/surveys#analytics).

### What if my landing page has more than one NPS question?

The score from the email block is applied to the first NPS question on the survey landing page.

### Can I use more than one NPS Survey block in the same email?

No. Each email message supports one **NPS Survey** block.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Drag-and-drop editor blocks</span></span></div></a></li><li><a href="/docs/user_guide/messaging/landing_pages/create_landing_pages/surveys"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Landing page surveys</span></span></div></a></li><li><a href="/docs/user_guide/messaging/surveys"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Surveys</span></span></div></a></li></ul>
