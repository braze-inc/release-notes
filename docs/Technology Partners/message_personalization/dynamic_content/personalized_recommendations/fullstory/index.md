# Fullstory

> [Fullstory’s](https://www.fullstory.com/) behavioral data platform helps technology leaders make better, more informed decisions. By injecting digital behavioral data into their analytics stack, Fullstory's patented technology unlocks the power of quality behavioral data at scale–transforming every digital visit into actionable insights. 

*This integration is maintained by Fullstory*

## About this integration

You can leverage Fullstory insights in Braze to build moment-to-moment pictures of a user's website or app experience to deliver hyper-contextual messaging. Fullstory's Session Summary API makes it possible to capture detailed metadata on a user's browsing behavior for use in Braze messaging, which is particularly powerful when leveraged in a multi-step messaging journey like a Canvas. 

The real-time value of Fullstory’s session summary data is best leveraged through Connected Content. By using Connected Content in a Canvas Context step, you can store Fullstory’s data throughout a user's Canvas journey for use in any subsequent Canvas steps. This also avoids the need to write this data to a Braze user profile through custom events or attributes. 

In the following example, Canvas Context data is leveraged in an Agent AI Canvas step to generate the optimal message to encourage a user to pick back up an abandoned cart. However, you can leverage the data to personalize the message directly, to determine the user's journey with audience paths, or to determine the copy or assets used in subsequent messaging steps.

## Prerequisites

Before you start, you need the following:

|Requirement     | Description |                        
|-----------------------|-----------------|
| A Fullstory Session API Authorization Token   | See Step 1 below. |
| A Braze Connected Content Authorization Token enabled | See the note below on Early Access. |
| A Braze Canvas Context step | See the note below on Early Access. |
| Enabled Braze AI Agent step | See the note below on Early Access. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**Important:**


Braze Agents, Canvas Context, and Connected Content Authorization Tokens are all in Early Access. If you're interested in leveraging this solution, speak to your Braze CSM about enabling these tools.



## Integrate Fullstory

### Step 1: Set up Fullstory for Session Summary API enablement {#step-1}

#### Step 1.1: Retrieve the authentication token for the Session Summary API endpoint

To create a [Fullstory API key](https://developer.fullstory.com/server/authentication/):

1. In Fullstory, go to **Settings** > **API Keys**. 
2. Select the **Standard** permission level.
3. Copy the key value immediately, as it appears only once.

#### Step 1.2: Create a session summary profile ID

Following [Fullstory's guidance](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), create a session summary profile using the dedicated endpoint. This is where you define what sort of data you want the session summary response to provide to Braze.

In the response to this request, Fullstory provides a session profile ID. This profile ID is a key component of the Connected Content request body used in the following use case.

### Step 2: Create the Connected Content token authentication

1. In Braze, go to **Settings** > **Workspace Settings** > **Connected Content** > **Add Credential** > **Token Authentication**. 
2. Name the authentication `fullstory`.
3. Add the header key “Authorization”. Supply the header value Fullstory provided in the previous step. 
4. Under **Allowed Domain**, enter **api.fullstory.com**.

![Screenshot of Braze showing the Edit Credential fields](https://www.braze.com/docs/assets/img/fullstory/1.png?751f7b1393b189284af2d40802677629){: style="max-width:50%;"}

## Use cases

### Create dynamic message journeys

Using Fullstory's [Activation Streams](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams), you can trigger Braze Canvases immediately after key user interactions. The power of this integration lies in the unique `client_session_id` (accessible via `{{canvas_entry_properties.${client_session_id}}}`), which the system passes automatically from Fullstory to Braze. This ID acts as a key, allowing Braze to fetch the complete Session Summary of exactly what the user experienced. 

By leveraging Canvas Context steps and Connected Content, you can use this ID to make an API request to Fullstory, retrieve the session data, and store it as a variable for use later in the journey. 

![Braze Canvas Context step showing the context variable "summary_result" being created and populated with a Connected Content call to Fullstory, to retrieve a session summary](https://www.braze.com/docs/assets/img/fullstory/2.png?871dc1d8d51cd61aa349804c15ce7e85)

With the authorization token created earlier, use the following request structure to pull the session summary data. 


```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```


**Note:**


The response is stored as the Liquid tag `{{context.${summary_result}.response}}`. Use this Context tag in subsequent Canvas steps.



At this stage, the Canvas can access the response to the Connected Content call, which contains the entire message payload for a user's session.

**Example payload from Session Summary API**




```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```




You can leverage any of the data available in the object above using the context Liquid tag later in the user's Canvas journey. The following steps show how you can use this data in an [Agent](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step) step.

**Note:**


To avoid unexpected behavior, include an Audience Path step after the Context step, which can drop users out of the context if their Context tag is empty, indicating the Connected Content call failed or otherwise returned no information.

![The Audience Path step in Braze](https://www.braze.com/docs/assets/img/fullstory/3.png?4a476f51e1a300e8296f973e5ab9b1a0)




### Produce appropriate copy

By creating an [Agent step](https://www.braze.com/docs/user_guide/brazeai/agents/creating_agents) in a Canvas triggered by Fullstory, and including the Context step outlined above, you can reference Fullstory’s session summary data in the agent. 

In this example, you use this data to allow the Braze agent to generate appropriate message copy for use in a Content Card, which can encourage the user to return to their abandoned basket.

![Screenshot of the Braze Agent Context creator with the prompt](https://www.braze.com/docs/assets/img/fullstory/4.png?36b85a24e6def3a80e66f359d1a4ae1c)

Use the same name for the Context Liquid tag created in this step as the context Liquid tag used in the AI Agent step created earlier. 

The prompt required for your use case varies. For best practices on creating effective agent prompts, see [Writing Instructions](https://www.braze.com/docs/user_guide/brazeai/agents/reference/#writing-instructions). 

In your Canvas, select an AI Agent step, then select the **Session Context** agent from the dropdown. Save the output as a variable, in this case "message", which you can place into message copy by using the Liquid tag `{{context.${message}.message}}`.

![Screenshot of Braze Agent Context Canvas step with the prompt](https://www.braze.com/docs/assets/img/fullstory/5.png?b3da97bdc625ba1f33475af7cc1aa573)

Create a Message step that leverages the AI Agent-created copy. Use the Liquid tag in this step.

**Important:**


Fullstory's Session Summary API may return sensitive identifiable user data. To ensure compliance while handling PII (personally identifiable information), confirm your Fullstory data capture rules exclude PII before leveraging this use case.


