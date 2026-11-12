# Conversational Agents

> Conversational Agents is a channel that lets your users talk with an AI agent to complete tasks you define. You create conversational workflows that describe what the agent should do for your brand. For example, a workflow can help a user purchase items based on their preferences.

**Important:**


Conversational Agents is currently in beta. Contact your Braze account manager if you're interested in participating in this beta.<br><br>Before you deploy to production, consult your legal team about the implications of using conversational AI.



## How it works

A conversational workflow is a task you want an agent to complete. Each workflow includes a purpose, channel settings, a target audience, and natural-language steps. In a step, add tools so the agent can search catalogs, set attributes, log events, or call webhooks.

After you create workflows, see [Settings](#settings) for brand guidelines and channel behavior. Use [Preview a conversation](#preview-a-conversation), [Create simulations](#create-simulations), and [Review conversation history](#review-conversation-history) to test the experience and review tool calls.

## Set up the web chat widget

To show the Conversational Agents chat widget on your site, complete the following steps in the Braze Web SDK.

### Step 1: Set up SDK authentication

Enable [SDK authentication](https://www.braze.com/docs/developer_guide/sdk_integration/authentication) for your web app.

### Step 2: Install the Web SDK

Install either of the following:

| Option | Details |
| --- | --- |
| npm | Install the latest [`@braze/web-sdk`](https://www.npmjs.com/package/@braze/web-sdk) package. |
| CDN | Load the conversational build: `https://js.appboycdn.com/web-sdk/latest/braze.conversational.min.js` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Web SDK install options" }

### Step 3: Initialize with user-supplied JavaScript enabled

In your `initialize` call, set `allowUserSuppliedJavascript: true`:

```javascript
braze.initialize("{YOUR_API_KEY}", {
  baseUrl: "{YOUR_SDK_ENDPOINT}",
  allowUserSuppliedJavascript: true
});
```

Replace `{YOUR_API_KEY}` with your Web SDK API key and `{YOUR_SDK_ENDPOINT}` with your SDK endpoint.

### Step 4: Enable the chat widget

Before you open a session, call `braze.automaticallyManageChat()`:

```javascript
braze.automaticallyManageChat();
braze.openSession();
```

## Create a conversational workflow

Use a conversational workflow to define a task, choose channels and an audience, and tell the agent what to do in each step.

### Step 1: Set up workflow details

Go to **Agents** > **Conversational Agents**, then set up the details for your workflow:

1. Enter a name for the workflow.
2. Enter a purpose that describes what this workflow does. The agent uses the purpose and the conversation history to choose which workflow to use, so describe when the workflow applies. For example, "The user has questions about event times or refunds."
3. Select the channels this workflow is enabled for. Supported channels are SMS, RCS, WhatsApp, and Web.
   - For web, select which web apps this workflow is enabled for.
   - For SMS, RCS, and WhatsApp, select which [subscription groups](https://www.braze.com/docs/user_guide/audience/subscription_preferences/subscription_groups) this workflow is enabled for.
4. Select the [segments](https://www.braze.com/docs/user_guide/audience/segments) a user must belong to in order to access this workflow.

**Note:**


Workflows aren't tied to a Canvas. A subscription group or web app can have several workflows, and the agent moves between them during a conversation. To limit a workflow to users who received a specific Canvas message, create a segment of those users and select it for the workflow. To test with a small audience first, use a segment of a small subset of users.



For SMS, RCS, and WhatsApp, some inbound message triggers can block the agent. On the [Settings](#settings) page, review the triggers that may block agents for each subscription group.

### Step 2: Write workflow steps

Add the steps the agent should take to complete the workflow. A workflow can have up to 10 steps. Each step needs an instruction, which can be up to 5,000 characters.

For steps with a single goal, write the instruction in one to three short sentences. Keep the rules clear, and end with an explicit question or confirmation so the agent knows how to phrase its next response to the user.

### Step 3: Add tools to steps

Steps can include tools the agent uses while it works. In the **Instructions** of a step, tools are inserted by entering `/` and appear as tags in the instruction. A step can reference up to 10 tools.

![The instruction text box in a workflow step, with the slash menu open to insert a tool.](https://www.braze.com/docs/assets/img/conversational_agents/add_tools.png?a46ee28b57fe62457dfc01a8ace261e6){: width="1424" height="936" style="max-width:80%;height:auto;"}

## Tools

You can add any of these tools to a step:

| Tool | Description |
| --- | --- |
| [Search knowledge sources](#search-knowledge-sources) | Query a [catalog](https://www.braze.com/docs/user_guide/data/activation/catalogs) through a knowledge source. |
| [Set workflow attribute](#set-a-workflow-attribute) | Store a value that is scoped to this workflow. |
| [Get workflow attribute](#get-a-workflow-attribute) | Retrieve a workflow attribute set in an earlier step. |
| [Log custom event](#log-a-custom-event) | Log a Braze [custom event](https://www.braze.com/docs/user_guide/data/activation/events/custom_events). |
| [Set custom attribute](#set-a-custom-attribute) | Set a [custom attribute](https://www.braze.com/docs/user_guide/data/activation/attributes/custom_attributes) on the user. |
| [Get custom attribute](#get-a-custom-attribute) | Retrieve a custom attribute from the user. |
| [Get user attribute](#get-a-user-attribute) | Retrieve a standard user profile field. |
| [Call webhook](#call-a-webhook) | Send an HTTP request to an external endpoint. |
| [Get webhook response](#get-a-webhook-response) | Retrieve a field extracted from a previous webhook response. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Supported tools" }

### Search knowledge sources

Use this tool to help the agent query and understand a Braze catalog. Create knowledge sources for catalogs such as:

- Product catalog
- FAQ
- Size charts

First, create the knowledge source on the [Knowledge sources](https://www.braze.com/docs/user_guide/brazeai/agents/knowledge_sources) page. Then, in the instruction text box, enter `/` and select **Search knowledge sources**. Select an existing conversational knowledge source tool, or select **Create new search tool**.

When you create a new tool, enter a name and description, then select a knowledge source. After you select a knowledge source, choose which fields the agent can access.

### Set a workflow attribute

Use this tool to set an attribute the agent can reuse later in the same workflow. Workflow attributes are scoped to the workflow they are set in. Use them as custom event properties, custom attribute values, and webhook parameters.

When you create the attribute, you can optionally add **Allowed values**:

- Leave allowed values empty to let the agent set any value of that type based on the conversation.
- Add allowed values to limit the agent to a subset you define. Use this when later tools (such as **Call webhook**, **Log custom event**, or **Set custom attribute**) should reuse a controlled value instead of an open-ended agent choice.

In **Instruction**, enter `/` and select **Set workflow attribute**. Select an existing workflow attribute, or select **Create new attribute**.

When you create a new attribute, enter a name and description, then select the type. After you select the type, optionally add allowed values. Each allowed value needs a value of up to 100 characters and a description of up to 250 characters. Values must be unique, and an attribute can have up to 250 allowed values.

With allowed values, the agent chooses one of your values even when the user words it differently. For example, if a `skin_type` attribute allows only `dry` and `oily`, and a user describes their skin with a synonym for dry, the agent sets `dry`. Without allowed values, the agent chooses a value from the attribute description and your step instructions, which it usually follows but may not follow strictly.

To save a controlled value to a user profile, use two tools in the same step:

1. Use **Set workflow attribute** to set the attribute after the user confirms their answer.
2. Use **Set custom attribute**, and select **Workflow attribute** as the source for the custom attribute value.

### Get a workflow attribute

Use this tool to retrieve the value of a workflow attribute set in an earlier step.

### Log a custom event

Use this tool to log a Braze custom event. In the instruction text box, enter `/` and select **Log custom event**. Select an existing log custom event tool, or select **Create new custom event tool**.

When you create a new tool, select the custom event, then enter a name and description. Choose the event properties to send with the custom event. Each custom event property can use one of the following sources:

| Source | Description |
| --- | --- |
| Agent | The agent decides the value based on the instructions and tool description. |
| Workflow attribute | The property uses a workflow attribute the agent set in an earlier step. |
| Custom attribute | The property uses a custom attribute on the user. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom event property sources" }

You don't have to set a value for every property. Some property types aren't supported.

Select **Required** if the tool should fail when the property value is blank.

To send a user into a Canvas, log a custom event that the Canvas uses as an [entry property](https://www.braze.com/docs/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties).

### Set a custom attribute

Use this tool to set a custom attribute on the user. In the instruction text box, enter `/` and select **Set custom attribute**. Select an existing set custom attribute tool, or select **Create new custom attribute tool**.

When you create a new tool, enter a name and description, then select the custom attribute the tool should set. A custom attribute can use one of the following sources:

| Source | Description |
| --- | --- |
| Agent | The agent decides the value based on the instructions and tool description. |
| Workflow attribute | The user attribute uses a workflow attribute the agent set in an earlier step. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom attribute sources" }

**Note:**


Custom attributes are set asynchronously. If the agent reads a custom attribute after setting it, the value may still be stale.



### Get a custom attribute

Use this tool to retrieve a custom attribute.

### Get a user attribute

Use this tool to retrieve a standard user profile field. In the instruction text box, enter a forward-slash (`/`) and select **Get user attribute**. Choose one of the following fields:

- **External ID**
- **Braze ID**
- **Email**
- **First name**
- **Last name**
- **Phone**

### Call a webhook

Use this tool to call a webhook. In the instruction text box, enter `/` and select **Call webhook**. Select an existing webhook tool, or select **Create new webhook**.

When you create a new tool, enter a name and description, then add variables. Variables let you include personalized values in the webhook URL, body, or headers.

A variable can use one of the following sources:

| Source | Description |
| --- | --- |
| Agent | The agent decides the value based on the instructions and description. |
| Workflow attribute | The variable uses a workflow attribute the agent set in an earlier step. |
| Custom attribute | The variable uses a custom attribute on the user. |
| User profile | The variable uses a user profile field: external ID, Braze ID, email, first name, last name, or phone. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook variable sources" }

After you set variables, choose the request method. The following request methods are supported:

- `GET`
- `POST`
- `PUT`
- `PATCH`
- `DELETE`

Then enter the URL. To use variables in the URL, reference them with `{{variable_name}}` syntax. For example:


```text
https://myurl.com/create/{{user_id}}
```


Next, set the request body. Leave the body empty, or enter a string that can include `{{variable_name}}` placeholders. For most APIs, send a JSON body. For example:


```json
{
  "user": {
    "id": "{{external_id}}",
    "favorite_color": "{{favorite_color}}",
    "is_called_by_agent": true
  }
}
```


You can also set headers using variables. For credentials, create [Connected Content credentials](https://www.braze.com/docs/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types) in the dashboard and reference them in this tool.

Webhook responses can be large, so you can extract only the fields the workflow needs. Create response fields with a [JMESPath](https://jmespath.org/tutorial.html) expression that points to a value in the response body. The response body must be valid JSON for those fields to extract successfully. Reference those fields later with the [Get webhook response](#get-a-webhook-response) tool.

### Get a webhook response

Use this tool to reference a webhook response field extracted from a previous **Call webhook** step.

## Settings

Configure brand guidelines and channel behavior for Conversational Agents. Go to **Agents** > **Conversational Agents**, then select **Settings**.

### Brand guidelines

Select [brand guidelines](https://www.braze.com/docs/user_guide/administer/global/workspace_settings/brand_guidelines) for the agent to follow in its responses. Create and manage guidelines from **Content** > **Brand Guidelines**, then choose one here.

### Web settings

Set an **Opening message**. This is the first message users see when they start a web conversation.

### SMS, RCS, and WhatsApp settings

Configure the following:

| Setting | Description |
| --- | --- |
| **Daily turn limit** | The maximum number of turns per user per day for messaging channels. |
| **AI disclosure message** | Text that opens the agent's first reply in every SMS, RCS, and WhatsApp conversation. You can reword it, but you can't turn it off. Leave the field blank to use the default message. |
| **Triggers that may block agents** | A list of inbound message triggers on each subscription group enabled in a workflow. If an inbound message activates one of these triggers, the conversational agent does not respond. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Messaging channel settings" }

Triggers that may take priority include:

- [Keyword triggers](https://www.braze.com/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing)
- Action-based campaigns
- Action-based Canvas entry
- Canvas action path
- Canvas exit

## Preview a conversation {#preview-a-conversation}

There are two ways to preview:

- When you edit a saved workflow, preview that workflow only. Preview is unavailable until you save a new workflow.
- On the **Settings** page, preview the experience for a web app or subscription group. Optionally, select **Include draft workflows** to test draft workflows before you make them active.

In both cases, preview as a specific user.

**Note:**


Preview mode does not log custom attributes or custom events.



## Create simulations

A simulation tests your workspace's conversational workflows without a real user. Create cases that describe a scenario and the outcomes you expect. A simulated user follows that scenario. When the conversation ends, a grader checks the conversation and tool calls against those outcomes. Mock webhook responses so the cases stay predictable.

Go to **Agents** > **Conversational Agents**, then select **Simulations**.

### Create a case

On the **Cases** tab, select **Create case**, then set up the following:

| Field | Description |
| --- | --- |
| **Case name** | A unique name for the case. |
| **Workflows** | The workflows the conversation can enter. Select at least one. |
| **User** | The user the conversation runs as, in test mode. Search by email, phone number, or external user ID. |
| **User's first message** | The first message the simulated user sends. |
| **What the user wants, how they behave, and what they know** | The scenario. The simulated user knows only what you write here. For example, a user who's frustrated about a refund, or a user who wants to book an appointment. |
| **Expected outcomes** | One checkable statement for each thing the agent should do or say, such as "The agent gives the user a support email address." You can add up to 10. |
| **Webhook responses** | Optional. Turn on **Mock response for** a webhook, then enter fixed values to return instead of calling your endpoint. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Simulation case fields" }

Create a case for each scenario you want to test, such as a frustrated user, a user who wants to book, and a user with a refund question.

### Run a simulation and review results

Select **Run simulation**, choose the cases to run, then select **Start run**. Review past runs on the **Runs** tab.

**Important:**


Braze calls any webhook that a case doesn't mock. To avoid calling your endpoints, mock each webhook the workflows use.



Each case in a run shows the conversation between the simulated user and the agent, and a result for each expected outcome with an explanation:

- **Passed**
- **Failed**
- **Inconclusive**, when the conversation doesn't contain enough evidence to decide

A case fails if any outcome fails. If no outcome fails but any is inconclusive, the case is inconclusive. Otherwise, the case passes.

## Review conversation history {#review-conversation-history}

On the **Conversational Agents** page, select **Conversation history**. This page shows conversations with real users and conversations from preview.

Use conversation history to review tool calls and confirm the agent behaves as expected.

![The Conversation history page, showing a user conversation and the agent's tool calls.](https://www.braze.com/docs/assets/img/conversational_agents/conversation_history.png?80246489bc9e5eaa5887aff7183bdcbc){: width="717" height="1452" style="max-width:60%;height:auto;"}

## Example

Flash & Thread, a fictional clothing retail brand, might use this two-step shopping workflow. 

- **Step 1:** Asks the user what product category they're shopping for.
- **Step 2:** Uses the **Set workflow attribute** tool to capture a **product_category** attribute as a string. This attribute records the product category the user says they're shopping for today from **Step 1**.

![Two workflow steps for a shopping example. Step 1 asks for a product category. Step 2 sets the product_category workflow attribute and confirms the selection.](https://www.braze.com/docs/assets/img/conversational_agents/workflow_steps_example.png?9fe0099e609992a0e6fd8658fe6e1cbd){: width="1024" height="765" style="max-width:80%;height:auto;"}
