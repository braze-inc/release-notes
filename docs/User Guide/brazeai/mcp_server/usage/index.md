# Using the Braze MCP server

> Learn how to interact with your Braze data through natural language using tools like Claude and Cursor. For more general information, see [Braze MCP server].

**Important:**


The locally hosted Braze MCP server (beta) is sunsetting this summer. It will continue to work, but we're no longer adding endpoints or supporting the beta. A remote, Braze-hosted MCP server is coming to Early Access this summer.




## Prerequisites

Before you can use this feature, you'll need to [set up the Braze MCP server].

## Best practices

When using the Braze MCP server through natural-language tools like Claude and Cursor, keep these tips in mind to get the best results:

- LLMs can make mistakes, so always be sure to double-check their answers.
- For data analysis, be clear about the time range you need. Shorter ranges often give more accurate results.
- Use exact [Braze terminology](https://www.braze.com/resources/articles/glossary) so your LLM calls the right function.
- If results seem incomplete, prompt your LLM to continue or dig deeper.
- Try creative prompts! Depending on your MCP client, you may be able to export a CSV or other useful files.

## Usage examples

After [setting up the Braze MCP server], you can interact with Braze through natural language using tools like Claude or Cursor. Here's some examples to get you started:

### What are my available Braze functions?



**Example prompt**

`What are my available Braze functions?`

**Example response**

I checked the Braze MCP server with `list_functions` and found 38 available API functions.

Here are a few examples by category:

- **Campaign analytics and management**
  - `get_campaign_dataseries`
  - `get_campaign_details`
  - `get_campaign_list`
- **Canvas analytics and management**
  - `get_canvas_data_series`
  - `get_canvas_data_summary`
  - `get_canvas_list`
  - `get_canvas_details`
- **Templates**
  - `create_email_template`
- **Content blocks**
  - `create_content_block`
  - `get_content_blocks`
  - `get_content_block_info`
  - `update_content_block`



**Example prompt**

`What are my available Braze functions?`

**Example response**

I'll check your available functions using the Braze MCP server.

- Called `list_functions`

Based on that result, you have 38 Braze API functions organized into categories such as:

- Campaign analytics and management
- Canvas analytics and management
- Templates
- Content blocks

Example functions include:

- `get_campaign_list`
- `get_canvas_list`
- `get_canvas_details`
- `create_email_template`
- `update_content_block`



For more information on the `list_functions` function, see [Available API functions].

### Get details about a Canvas ID



**Example prompt**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response**

I retrieved details for `YOUR-TEST-CANVAS-ID-123` using `get_canvas_details`.

- **Canvas name:** `YOUR-TEST-CANVAS-NAME`
- **ID:** `YOUR-TEST-CANVAS-ID-123`
- **Status:** Draft (not enabled)
- **Created at:** Jan 15, 2026 10:30 AM UTC
- **Last updated:** Jan 16, 2026 02:45 PM UTC
- **Schedule type:** Time-based
- **Primary channel:** Email

Email message details:

- **Subject:** `YOUR-TEST-SUBJECT-LINE`
- **From:** `YOUR-TEST-SENDER@example.com`
- **Message ID:** `YOUR-TEST-MESSAGE-ID-123`



**Example prompt**

`Get details about canvas ID YOUR-TEST-CANVAS-ID-123`

**Example response**

I pulled this Canvas using `get_canvas_details`:

- **Canvas ID:** `YOUR-TEST-CANVAS-ID-123`
- **Canvas name:** `YOUR-TEST-CANVAS-NAME`
- **Status:** Draft
- **Channel:** Email
- **Message ID:** `YOUR-TEST-MESSAGE-ID-123`

Email content summary:

1. Header section with brand image
2. Main headline section
3. Hero section with CTA button
4. Feature section with supporting content



For more information on the `get_canvas_details` function, see [Available API functions].

### Show me my recent Canvases



**Example prompt**

`Show me my recent Canvases`

**Example response**

I checked your available tools with `list_functions`, then used `get_canvas_list` to return your most recently edited Canvases.

Most recent Canvases:

1. **YOUR-TEST-CANVAS-ALPHA**
   - ID: `YOUR-TEST-ID-123`
   - Last edited: Jan 16, 2026 02:45 PM UTC
2. **YOUR-TEST-CANVAS-BETA**
   - ID: `YOUR-TEST-ID-456`
   - Last edited: Jan 15, 2026 11:10 AM UTC
3. **YOUR-TEST-CANVAS-GAMMA**
   - ID: `YOUR-TEST-ID-789`
   - Last edited: Jan 14, 2026 08:25 PM UTC



**Example prompt**

`Show me my recent Canvases`

**Example response**

I'll retrieve your recent Canvas list from the Braze MCP server.

- Called `list_functions`
- Called `get_canvas_list`

Recent Canvases (sorted by most recently edited):

- **Canvas name:** `YOUR-TEST-CANVAS-ALPHA`
  - **Last edited:** Jan 16, 2026 02:45 PM UTC
  - **Canvas ID:** `YOUR-TEST-ID-123`
  - **Tags:** `lifecycle`, `email`
- **Canvas name:** `YOUR-TEST-CANVAS-BETA`
  - **Last edited:** Jan 15, 2026 11:10 AM UTC
  - **Canvas ID:** `YOUR-TEST-ID-456`
  - **Tags:** `promo`



For more information on the `get_canvas_list` function, see [Available API functions].

### Create an email template



**Example prompt**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Example response**

I created your template with `create_email_template`.

- **Template name:** `YOUR-TEST-TEMPLATE-NAME`
- **Template ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **Subject line:** `YOUR-TEST-SUBJECT-LINE`
- **Preheader:** `YOUR-TEST-PREHEADER`
- **Created at:** Jan 16, 2026 03:10 PM UTC

You can now reference `YOUR-TEST-TEMPLATE-ID-123` when creating or updating campaigns and Canvases.



**Example prompt**

`Create an email template named "YOUR-TEST-TEMPLATE-NAME" for onboarding messages.`

**Example response**

I used `create_email_template` and created a new template successfully.

- **Template ID:** `YOUR-TEST-TEMPLATE-ID-123`
- **Template name:** `YOUR-TEST-TEMPLATE-NAME`
- **Subject:** `YOUR-TEST-SUBJECT-LINE`
- **Description:** `Onboarding lifecycle template`

If you'd like, I can also generate a starter HTML body and plain-text fallback for this template.



For more information on the `create_email_template` function, see [Available API functions].

### Update a content block



**Example prompt**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Example response**

I updated your content block using `update_content_block`.

- **Content block ID:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Name:** `YOUR-TEST-CONTENT-BLOCK-NAME`
- **Status:** Updated
- **Updated at:** Jan 16, 2026 03:25 PM UTC

Preview:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`



**Example prompt**

`Update content block "YOUR-TEST-CONTENT-BLOCK-ID-123" with new body copy for our spring promotion.`

**Example response**

I ran `update_content_block` and confirmed the update completed.

- **Content block ID:** `YOUR-TEST-CONTENT-BLOCK-ID-123`
- **Previous version:** `v1`
- **Current version:** `v2`
- **Last updated:** Jan 16, 2026 03:25 PM UTC

Updated content preview:

`YOUR-TEST-CONTENT-BLOCK-BODY-V2`



For more information on the `update_content_block` function, see [Available API functions].

## Disclaimer
<!-- Braze Legal must approve any changes to this content. -->
<!-- Note: Keep these comments under this H2 heading to avoid breaking how headings on certain pages are rendered. -->

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) is a newly introduced open-source protocol that may be susceptible to security issues or vulnerabilities at this time.

Braze MCP Server setup code and instructions are provided by Braze “as is” and without any warranties, and customers use it at their own risk. Braze shall not be responsible for any consequences arising from improper setup, misuse of the MCP, or any potential security issues that may arise. Braze strongly encourages customers to review their configurations carefully and to follow the outlined guidelines to reduce risks associated with the integrity and security of their Braze environment.

For assistance or clarification, please contact [Braze Support](https://www.braze.com/docs/user_guide/administrative/access_braze/support).


