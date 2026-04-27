<div id='api_jdlhdomxezmh' class='api_div'>
<h1 id="schedule-api-triggered-canvases">Schedule API-triggered Canvases</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/canvas/trigger/schedule/create</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to schedule Canvas messages via API-triggered delivery, allowing you to decide what action should trigger the message to be sent.</p>
</blockquote>

<p>You can pass in <code class="language-plaintext highlighter-rouge">context</code> that will be templated into the messages sent by the first steps of the Canvas.</p>

<p>Note that to send messages with this endpoint, you must have a <a href="/docs/api/identifier_types/#canvas-api-identifier">Canvas ID</a>, created when you build a Canvas.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4bc75890-b807-405d-b226-5aca284e6b7d" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">canvas.trigger.schedule.create</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"canvas_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">Including</span><span class="w"> </span><span class="err">'recipients'</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">provided</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">ids</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">they</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign's</span><span class="w"> </span><span class="err">segment</span><span class="w">
  </span><span class="nl">"recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">recipients</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">any</span><span class="w"> </span><span class="err">keys</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">conflict</span><span class="w"> </span><span class="err">between</span><span class="w"> </span><span class="err">these</span><span class="w"> </span><span class="err">trigger</span><span class="w"> </span><span class="err">properties</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">those</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">Recipients</span><span class="w"> </span><span class="err">Object</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">value</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">Recipients</span><span class="w"> </span><span class="err">Object</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">used</span><span class="w">
  </span><span class="nl">"audience"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">connected</span><span class="w"> </span><span class="err">audience</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">connected</span><span class="w"> </span><span class="err">audience</span><span class="p">,</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">Including</span><span class="w"> </span><span class="err">'audience'</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">audience</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">If</span><span class="w"> </span><span class="err">'recipients'</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">'audience'</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">provided</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">broadcast</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">'</span><span class="kc">false</span><span class="err">'</span><span class="p">,</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">entire</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">targeted</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="w">
  </span><span class="nl">"broadcast"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">broadcast</span><span class="w"> </span><span class="err">--</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">false</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="mi">8</span><span class="err">/</span><span class="mi">31</span><span class="err">/</span><span class="mi">17</span><span class="p">,</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">true</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="s2">"recipients"</span><span class="w"> </span><span class="err">object</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">omitted</span><span class="p">,</span><span class="w">
  </span><span class="nl">"context"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">personalization</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">first</span><span class="w"> </span><span class="err">step</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">all</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">send;</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">trigger</span><span class="w"> </span><span class="err">properties</span><span class="p">,</span><span class="w">
  </span><span class="nl">"schedule"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"time"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">datetime</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
    </span><span class="nl">"in_local_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">bool)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"at_optimal_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">bool)</span><span class="p">,</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">canvas_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">Canvas identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">recipients</code></td>
      <td>Optional</td>
      <td>Array of recipients objects</td>
      <td>See <a href="/docs/api/objects_filters/recipient_object/">recipients object</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">audience</code></td>
      <td>Optional</td>
      <td>Connected audience object</td>
      <td>See <a href="/docs/api/objects_filters/connected_audience/">connected audience</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">broadcast</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>You must set <code class="language-plaintext highlighter-rouge">broadcast</code> to true when sending a message to an entire segment that a campaign or Canvas targets. This parameter defaults to false (as of August 31, 2017). <br /><br /> If <code class="language-plaintext highlighter-rouge">broadcast</code> is set to true, a <code class="language-plaintext highlighter-rouge">recipients</code> list cannot be included. However, use caution when setting <code class="language-plaintext highlighter-rouge">broadcast: true</code>, as unintentionally setting this flag may cause you to send your message to a larger than expected audience.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">context</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>Personalization key-value pairs for all users in this send. See <a href="/docs/user_guide/messaging/canvas/canvas_components/context/">Canvas context object</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">schedule</code></td>
      <td>Required</td>
      <td>Schedule object</td>
      <td>See <a href="/docs/api/objects_filters/schedule_object/">schedule object</a>.</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "context": {}
    }
  ],
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
  "broadcast": false,
  "context": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<h3 id="example-success-response">Example success response</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
