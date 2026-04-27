<div id='api_wzhmmwqwhidn' class='api_div'>
<h1 id="send-canvas-messages-using-api-triggered-delivery">Send Canvas messages using API-triggered delivery</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/canvas/trigger/send</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to send Canvas messages with API-triggered delivery.</p>
</blockquote>

<p>API-triggered delivery allows you to store message content in the Braze dashboard while dictating when a message is sent, and to whom using your API.</p>

<p>Before you can send messages with this endpoint, you must have a <a href="/docs/api/identifier_types/#canvas-api-identifier">Canvas ID</a> (which is created when you build a Canvas).</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need to generate an API key with the <code class="language-plaintext highlighter-rouge">canvas.trigger.send</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-body">Request body</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
</pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"canvas_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"context"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">personalization</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">apply</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">all</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w">
  </span><span class="nl">"broadcast"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">Broadcast</span><span class="w"> </span><span class="err">--</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">false</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="mi">8</span><span class="err">/</span><span class="mi">31</span><span class="err">/</span><span class="mi">17</span><span class="p">,</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">true</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">`recipients`</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">omitted</span><span class="p">,</span><span class="w">
  </span><span class="nl">"audience"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">connected</span><span class="w"> </span><span class="err">audience</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">connected</span><span class="w"> </span><span class="err">audience</span><span class="p">,</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">Including</span><span class="w"> </span><span class="err">'audience'</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">audience</span><span class="w">
  </span><span class="nl">"recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array;</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">provided</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">broadcast</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">'</span><span class="kc">false</span><span class="err">'</span><span class="p">,</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">sends</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">entire</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">targeted</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas)</span><span class="w">
    </span><span class="p">[{</span><span class="w">
      </span><span class="err">//</span><span class="w"> </span><span class="err">Either</span><span class="w"> </span><span class="s2">"external_user_id"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"user_alias"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"email"</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">required.</span><span class="w"> </span><span class="err">Requests</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">specify</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">one.</span><span class="w">
      </span><span class="nl">"user_alias"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">receive</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_user_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">external</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">receive</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
      </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">address</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">receive</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
      </span><span class="nl">"prioritization"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array)</span><span class="w"> </span><span class="err">prioritization</span><span class="w"> </span><span class="err">array;</span><span class="w"> </span><span class="err">required</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">using</span><span class="w"> </span><span class="err">email</span><span class="p">,</span><span class="w">
      </span><span class="nl">"context"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">personalization</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">apply</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">(these</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">override</span><span class="w"> </span><span class="err">any</span><span class="w"> </span><span class="err">keys</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">conflict</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">parent</span><span class="w"> </span><span class="err">`context`)</span><span class="w">
      </span><span class="nl">"send_to_existing_only"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w"> </span><span class="err">can't</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">aliases</span><span class="w">
      </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">fields</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">object</span><span class="w"> </span><span class="err">create</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">update</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">given</span><span class="w"> </span><span class="err">value</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">specified</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">profile</span><span class="w"> </span><span class="err">before</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">existing</span><span class="w"> </span><span class="err">values</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">overwritten</span><span class="w">
    </span><span class="p">}],</span><span class="w">
    </span><span class="err">...</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="request-parameters">Request parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" role="presentation">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Required</th>
      <th>Data Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">canvas_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">Canvas identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">context</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>This includes Canvas entry properties. Personalization key-value pairs apply to all users in this request. The context object can be up to 50 KB.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">broadcast</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>You must set <code class="language-plaintext highlighter-rouge">broadcast</code> to true when sending a message to the entire segment configured as the Canvas’s target audience in the Braze dashboard. This parameter defaults to false (as of August 31, 2017). <br /><br /> If <code class="language-plaintext highlighter-rouge">broadcast</code> is set to true, a <code class="language-plaintext highlighter-rouge">recipients</code> list cannot be included. However, use caution when setting <code class="language-plaintext highlighter-rouge">broadcast: true</code>, as unintentionally setting this flag may cause you to send your message to a larger-than-expected audience.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">audience</code></td>
      <td>Optional</td>
      <td>Connected audience object</td>
      <td>See <a href="/docs/api/objects_filters/connected_audience/">Connected audience</a>. When you include <code class="language-plaintext highlighter-rouge">audience</code>, the message is sent only to users who match the defined filters, such as custom attributes and subscription statuses.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">recipients</code></td>
      <td>Optional</td>
      <td>Array</td>
      <td>See <a href="/docs/api/objects_filters/recipient_object/">Recipients object</a>. <br /><br />If not provided and <code class="language-plaintext highlighter-rouge">broadcast</code> is set to <code class="language-plaintext highlighter-rouge">true</code>, the message is sent to the entire segment configured as the Canvas’s target audience in the Braze dashboard.<br /><br /> The <code class="language-plaintext highlighter-rouge">recipients</code> array may contain up to 50 objects, with each object containing a single <code class="language-plaintext highlighter-rouge">external_user_id</code> string and a <code class="language-plaintext highlighter-rouge">canvas_entry_properties</code> object. This call requires an <code class="language-plaintext highlighter-rouge">external_user_id</code>, <code class="language-plaintext highlighter-rouge">user_alias</code>, or <code class="language-plaintext highlighter-rouge">email</code>. Requests must specify only one. <br /><br />If <code class="language-plaintext highlighter-rouge">email</code> is the identifier, you must include <a href="/docs/api/endpoints/user_data/post_user_identify#identifying-users-by-email"><code class="language-plaintext highlighter-rouge">prioritization</code></a> in the recipients object.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response-details">Response details</h2>

<p>Message-sending endpoint responses include the message’s <code class="language-plaintext highlighter-rouge">dispatch_id</code> for reference back to the dispatch of the message. The <code class="language-plaintext highlighter-rouge">dispatch_id</code> is the ID of the message dispatch (unique ID for each “transmission” sent from the Braze platform). Check out <a href="/docs/help/help_articles/data/dispatch_id/">Dispatch ID behavior</a> for more information.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">201</code> could return the following response body. If the Canvas is archived, stopped, or paused, the Canvas is not sent through this endpoint.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre>{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
</pre></td></tr></tbody></table></code></pre></div></div>

<p>If your Canvas is archived, you see this <code class="language-plaintext highlighter-rouge">notice</code> message: “The Canvas is archived. Unarchive the Canvas to ensure trigger requests will take effect.” If your Canvas is not active, you see this <code class="language-plaintext highlighter-rouge">notice</code> message: “The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.”</p>

<p>If your request encounters a fatal error, refer to <a href="/docs/api/errors/#fatal-errors">Errors and responses</a> for the error code and description.</p>

<h2 id="considerations">Considerations</h2>

<p>Consider the following when making API calls to send Canvas messages using API-triggered delivery:</p>

<ul>
  <li><strong>Sending to existing users</strong>: When <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> is set to <code class="language-plaintext highlighter-rouge">true</code> (the default), the message is sent only to existing users in Braze.</li>
  <li><strong>Creating new users</strong>: When <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> is set to <code class="language-plaintext highlighter-rouge">false</code>, you must include an <code class="language-plaintext highlighter-rouge">attributes</code> object. If a user with the specified ID does not exist, Braze creates a user with that ID and attributes before sending the message.</li>
  <li><strong>User alias limitation</strong>: The <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> flag cannot be used with user aliases. To send to an alias-only user, the user must already exist in Braze.</li>
  <li><strong>Segment targeting</strong>: The <code class="language-plaintext highlighter-rouge">segment_id</code> parameter is not supported for this endpoint. To target a segment, configure the segment in the Canvas’s target audience settings in the Braze dashboard and use <code class="language-plaintext highlighter-rouge">broadcast: true</code>, or use the <code class="language-plaintext highlighter-rouge">audience</code> parameter with <a href="/docs/api/objects_filters/connected_audience/">Connected Audience</a> filters.</li>
  <li><strong>Combined targeting</strong>: When you include both the <code class="language-plaintext highlighter-rouge">recipients</code> parameter and configure a target segment in the dashboard, the message is sent only to user profiles that are specified in the API call and also match the segment’s filters.</li>
  <li><strong>Server-to-server calls</strong>: If you’re making server-to-server calls, you may need to allowlist the appropriate API URL if you’re behind a firewall.</li>
</ul>

<h2 id="attributes-object-for-canvas">Attributes object for Canvas</h2>

<p>Use the messaging object <code class="language-plaintext highlighter-rouge">attributes</code> to add, create, or update attributes and values for a user before sending them an API-triggered Canvas using the <code class="language-plaintext highlighter-rouge">canvas/trigger/send</code> endpoint. This API call processes the user attributes object before it processes and sends the Canvas. This helps minimize the risk of issues caused by <a href="/docs/user_guide/messaging/ab_testing/concepts/race_conditions/">race conditions</a>. However, by default, subscription groups cannot be updated this way.</p>

<p><strong>Note:</strong></p>

<p>Looking for the campaign version of this endpoint? Check out <a href="/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/">Sending campaign messages using API-triggered delivery</a>.</p>

</div>
