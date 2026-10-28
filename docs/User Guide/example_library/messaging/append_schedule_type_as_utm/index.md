# Add delivery schedule type to link UTM parameters

> The Braze REST API returns the delivery schedule type of a campaign or Canvas as `schedule_type`. This example uses a Content Block to retrieve that value through Connected Content, then references that Content Block from an email link template so every link in the message carries the value as a query parameter.

## About this example

MovieCanon, a fictional movie streaming service, sends scheduled, action-based, and API-triggered email. The analytics team wants to compare click performance by delivery type in their web analytics tool, without asking the marketing team to enter a UTM value by hand for each campaign.

[Supported personalization tags](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) don't include delivery schedule type. Use `schedule_type` from the [Export campaign details](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details) and [Export Canvas details](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_details) endpoints instead, with values such as `time_based`, `action_based`, or `api_triggered`.

This example combines the following Braze features:

- Connected Content calls the export endpoint for the message that's currently rendering and saves the response.
- A Content Block wraps that call so it's maintained in one place and returns only the `schedule_type` value.
- An email link template uses the Content Block as a query parameter value, so the parameter is appended to the links in your email.

Use the same approach for other campaign or Canvas metadata returned by these endpoints, such as `name` or `tags`.

## Considerations

- Confirm link templates are available. If **Email Link** is missing from **Templates** in your dashboard, contact your customer success manager to have the feature turned on.
- Use this pattern for workspaces with many campaigns. If you send a small number of campaigns, entering a static query parameter value in each message avoids the API dependency entirely.
- Treat the REST API key as a secret. Store it as a Connected Content credential rather than pasting it into message or Content Block bodies, and never share it in screenshots, tickets, or exported message HTML. If a key is exposed, create a replacement key and remove the old one.
- Use the correct Liquid tag for Canvas. In a Canvas Message step, `{{campaign.${api_id}}}` returns the step ID. Call the Canvas endpoint with `{{canvas.${api_id}}}` and the `canvas_id` parameter. For a full mapping of these attributes, see [Campaign and Canvas attributes across sources](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources).
- Plan for API volume. Braze doesn't rate limit Connected Content itself, so request volume scales with your sends and can exceed your recipient count. A single email can be rendered more than once (HTML, plain text, and AMP). Both export endpoints draw on a [shared limit](https://www.braze.com/docs/api/api_limits#requests-with-shared-rate-limits) of 250,000 requests per hour across many REST endpoints. Because `schedule_type` is identical for every recipient of a message, set `:cache_max_age` to reduce calls. See [Caching responses](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).
- Keep the rendered value on a single line. Query parameter values can't contain line breaks or spaces, so strip whitespace from your Content Block output. Otherwise, the URL can be malformed and the click may not be tracked as expected.
- Expect an empty value when calls fail. If the endpoint is unreachable, Braze renders an empty string, so the link is still clickable but the parameter has no value.
- Keep sensitive data out of query strings. Query parameters are visible to recipients and are often passed to third-party analytics tools.
- Plan for plain-text clicks separately. Link templates aren't applied to plain text, so clicks from the plain text version of an email won't include these parameters.

## Setup

### Step 1: Create a REST API key with export permissions

1. Go to **Settings** > **APIs and Identifiers** > **API Keys**.
2. Select **Create API Key** and give the key a name.
3. Grant the `campaigns.details` and `canvas.details` [permissions](https://www.braze.com/docs/api/basics#rest-api-key-permissions).
4. Copy the REST endpoint shown on the tab, such as `https://rest.iad-01.braze.com`. Use your own instance's endpoint in the following steps.

### Step 2: Store the key as a Connected Content credential

1. Go to **Settings** > **Connected Content**.
2. Select **Add credential** > **Token authentication**.
3. Name the credential, such as `braze_export_token`.
4. Add the header key `Authorization` with the value `Bearer YOUR-REST-API-KEY`, then set the allowed domain to your REST endpoint.

For more about credentials, see [Using token authentication](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-token-authentication).

### Step 3: Create a Content Block that returns the schedule type

1. Go to **Content** > **Content Blocks**. 
2. Select **Create Content Block** and select **HTML code editor**.
3. In the **HTML** tab, add the following Liquid. The `capture` block and `strip` filter remove the line breaks that make the code readable, so the Content Block renders only the value.


```liquid
{% capture schedule_type %}
{% if canvas.${api_id} == blank %}
{% connected_content
   https://rest.iad-01.braze.com/campaigns/details?campaign_id={{campaign.${api_id}}}
   :auth_credentials braze_export_token
   :cache_max_age 3600
   :save details
%}
{% else %}
{% connected_content
   https://rest.iad-01.braze.com/canvas/details?canvas_id={{canvas.${api_id}}}
   :auth_credentials braze_export_token
   :cache_max_age 3600
   :save details
%}
{% endif %}
{{details.schedule_type}}
{% endcapture %}{{schedule_type | strip}}
```


{: start="4"}
4. Select **Done**, then name the Content Block, such as `braze_schedule_type`. The name populates the **Content Block Liquid Tag** you reference in the next step.
5. Select **Launch Content Block**.

**Note:**


Don't add content after the final tag. Anything that follows it, including a trailing line break, becomes part of the URL when the Content Block is used in a link template.



### Step 4: Create an email link template

1. Go to **Templates** > **Email Link**.
2. Select **Create email link template** and give the template a name, such as `Schedule type UTM`.
3. Set **Template Position** to **After URL**.
4. Add a query parameter with the key you want to report on, such as `utm_content` or `schedule_type`.
5. For the value, enter the Content Block Liquid tag from the previous step: `{{content_blocks.${braze_schedule_type}}}`.
6. In the **Template preview**, confirm the parameter is appended as expected, then select **Save**.

To compare the two template positions, see [Link templates](https://www.braze.com/docs/user_guide/messaging/templates/email_templates/link_template).

### Step 5: Apply the link template to your email

In the **Content** tab of the updated HTML editor or the drag-and-drop editor, select **Link Management** > **Add a Link Template**, select your link template, and then select **Add**.

Start every URL in your message with `http://` or `https://` so Braze recognizes it in **Link Management**. If your workspace uses [link aliasing](https://www.braze.com/docs/user_guide/messaging/templates/email_templates/link_aliasing), you may need to add link templates again after you edit an existing message.

### Step 6: Verify the rendered links

1. In **Preview & Test**, generate a preview and select **View details** to open the [Connected Content debugger](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/debugger). Confirm the response status is `2XX` and that `schedule_type` is present.
2. Open the links in the preview pane and confirm the parameter value has no extra spaces, line breaks, or duplicate `?` characters.
3. Send a test email, or duplicate the campaign and launch it to an internal audience, then confirm the value that reaches your analytics tool.

## Related articles

<ul class="guide_tiles"><li><a href="/docs/user_guide/messaging/templates/email_templates/link_template"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Link templates</span></span></div></a></li><li><a href="/docs/user_guide/messaging/templates/email_templates/faq"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Email and Link Template FAQ</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/content_blocks"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Content Blocks</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Making an API call with Connected Content</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Caching Connected Content responses</span></span></div></a></li><li><a href="/docs/user_guide/messaging/design_and_edit/personalize/sources/campaign_and_canvas_attributes_across_sources"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Campaign and Canvas attributes across sources</span></span></div></a></li><li><a href="/docs/api/endpoints/export/campaigns/get_campaign_details"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Export campaign details</span></span></div></a></li><li><a href="/docs/api/endpoints/export/canvas/get_canvas_details"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">Export Canvas details</span></span></div></a></li><li><a href="/docs/api/api_limits"><div class="guide_tile"><span class="guide_tile_text"><span class="guide_tile_title">API rate limits</span></span></div></a></li></ul>
