<div id='api_hxzuqezyqvfl' class='api_div'>
<h1 id="create-scheduled-messages">Create scheduled messages</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/messages/schedule/create</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to schedule a campaign, Canvas, or other message to be sent at a designated time and provides you with an identifier to reference that message for updates.</p>
</blockquote>

<p>If you’re targeting a segment, a record of your request will be stored in the <a href="https://dashboard.braze.com/app_settings/developer_console/activitylog/">Developer Console</a> after all scheduled messages have been sent.</p>

<p><strong>Tip:</strong></p>

<p>If you’re interested in sending messages immediately to designated users, use the <a href="/docs/api/endpoints/messaging/send_messages/post_send_messages"><code class="language-plaintext highlighter-rouge">/messages/send</code> endpoint</a> instead.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">messages.schedule.create</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">You</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">need</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">least</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">'segment_id'</span><span class="p">,</span><span class="w"> </span><span class="err">'external_user_ids'</span><span class="p">,</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">'audience'</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">Including</span><span class="w"> </span><span class="err">'segment_id'</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">members</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">segment</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">Including</span><span class="w"> </span><span class="err">'external_user_ids'</span><span class="w"> </span><span class="err">and/or</span><span class="w"> </span><span class="err">'user_aliases'</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">those</span><span class="w"> </span><span class="err">users</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">Including</span><span class="w"> </span><span class="err">both</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">Segment</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">provided</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">they</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">segment</span><span class="w">
  </span><span class="nl">"broadcast"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">broadcast</span><span class="w"> </span><span class="err">--</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">false</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="mi">8</span><span class="err">/</span><span class="mi">31</span><span class="err">/</span><span class="mi">17</span><span class="p">,</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">true</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">specified</span><span class="p">,</span><span class="w">
  </span><span class="nl">"external_user_ids"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">external</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"user_aliases"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="p">,</span><span class="w">
  </span><span class="nl">"audience"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">connected</span><span class="w"> </span><span class="err">audience</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">connected</span><span class="w"> </span><span class="err">audience</span><span class="p">,</span><span class="w">
  </span><span class="nl">"campaign_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"send_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"override_messaging_limits"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">bool)</span><span class="w"> </span><span class="err">ignore</span><span class="w"> </span><span class="err">frequency</span><span class="w"> </span><span class="err">capping</span><span class="w"> </span><span class="err">rules</span><span class="p">,</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
  </span><span class="nl">"recipient_subscription_state"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">use</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">who</span><span class="w"> </span><span class="err">have</span><span class="w"> </span><span class="err">opted</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">('opted_in')</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">who</span><span class="w"> </span><span class="err">have</span><span class="w"> </span><span class="err">subscribed</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">opted</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">('subscribed')</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">all</span><span class="w"> </span><span class="err">users</span><span class="p">,</span><span class="w"> </span><span class="err">including</span><span class="w"> </span><span class="err">unsubscribed</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">('all')</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">latter</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">useful</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">transactional</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">messaging.</span><span class="w"> </span><span class="err">Defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">'subscribed'</span><span class="p">,</span><span class="w">
  </span><span class="nl">"schedule"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"time"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">datetime</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">UTC</span><span class="p">,</span><span class="w">
    </span><span class="nl">"in_local_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">bool)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"at_optimal_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">bool)</span><span class="p">,</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"apple_push"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">apple</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"android_push"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">android</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"kindle_push"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">kindle/fireOS</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"web_push"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">web</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"webhook"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">webhook</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"content_card"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">content</span><span class="w"> </span><span class="err">card</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"sms"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">SMS</span><span class="w"> </span><span class="err">object)</span><span class="w">
  </span><span class="p">}</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">broadcast</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>You must set <code class="language-plaintext highlighter-rouge">broadcast</code> to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to <code class="language-plaintext highlighter-rouge">false</code>. <br /><br /> If <code class="language-plaintext highlighter-rouge">broadcast</code> is set to <code class="language-plaintext highlighter-rouge">true</code>, a recipients list cannot be included. However, use caution when setting <code class="language-plaintext highlighter-rouge">broadcast: true</code>, as unintentionally setting this flag may cause you to send your message to a larger-than-expected audience.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external_user_ids</code></td>
      <td>Optional</td>
      <td>Array of strings</td>
      <td>See <a href="/docs/api/objects_filters/user_attributes_object/#braze-user-profile-fields">external user identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_aliases</code></td>
      <td>Optional</td>
      <td>Array of user alias objects</td>
      <td>See <a href="/docs/api/objects_filters/user_alias_object/">user alias object</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">audience</code></td>
      <td>Optional</td>
      <td>Connected audience object</td>
      <td>See <a href="/docs/api/objects_filters/connected_audience/">connected audience</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">segment_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">segment identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">campaign_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">campaign identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">send_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">send identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">override_messaging_limits</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Ignore frequency capping for campaigns, defaults to false</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">recipient_subscription_state</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Use this to send messages to only users who have opted in (<code class="language-plaintext highlighter-rouge">opted_in</code>), only users who have subscribed or are opted in (<code class="language-plaintext highlighter-rouge">subscribed</code>) or to all users, including unsubscribed users (<code class="language-plaintext highlighter-rouge">all</code>). <br /><br />Using <code class="language-plaintext highlighter-rouge">all</code> users is useful for transactional email messaging. Defaults to <code class="language-plaintext highlighter-rouge">subscribed</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">schedule</code></td>
      <td>Required</td>
      <td>Schedule object</td>
      <td>See <a href="/docs/api/objects_filters/schedule_object/">schedule object</a></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">messages</code></td>
      <td>Optional</td>
      <td>Messaging object</td>
      <td>See <a href="/docs/api/objects_filters/#messaging-objects">available messaging objects</a>.</td>
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
69
70
71
72
73
74
75
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<h3 id="example-success-response">Example success response</h3>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"dispatch_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">dispatch</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
    </span><span class="nl">"schedule_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">schedule</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
