<div id='api_hujdwkksijkg' class='api_div'>
<h1 id="update-scheduled-messages">Update scheduled messages</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/messages/schedule/update</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to update scheduled messages.</p>
</blockquote>

<p>This endpoint accepts updates to either the <code class="language-plaintext highlighter-rouge">schedule</code> or <code class="language-plaintext highlighter-rouge">messages</code> parameter or both. Your request must contain at least one of those two keys.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f61edf74-4467-4551-b9c4-a4b8d188cd7a" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">messages.schedule.update</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"schedule_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">`schedule_id`</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">update</span><span class="w"> </span><span class="err">(obtained</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">response</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">create</span><span class="w"> </span><span class="err">schedule)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"schedule"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="err">//</span><span class="w"> </span><span class="err">optional</span><span class="p">,</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">create</span><span class="w"> </span><span class="err">schedule</span><span class="w"> </span><span class="err">documentation</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="err">//</span><span class="w"> </span><span class="err">optional</span><span class="p">,</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">available</span><span class="w"> </span><span class="err">messaging</span><span class="w"> </span><span class="err">objects</span><span class="w"> </span><span class="err">documentation</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>
<h2 id="request-parameters">Request parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Request parameters">
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
      <td><code class="language-plaintext highlighter-rouge">schedule_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The <code class="language-plaintext highlighter-rouge">schedule_id</code> to update (obtained from the response to create schedule).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">schedule</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>See <a href="/docs/api/objects_filters/schedule_object/">schedule object</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">messages</code></td>
      <td>Optional</td>
      <td>Object</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T20:30:36Z"
   },
  "messages": {
    "apple_push": {
      "alert": "Updated Message!",
      "badge": 1
    },
    "android_push": {
      "title": "Updated title!",
      "alert": "Updated message!"
    },
    "sms": {
      "subscription_group_id": "subscription_group_identifier",
      "message_variation_id": "message_variation_identifier",
      "body": "This is my SMS body.",
      "app_id": "app_identifier"
    }
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
