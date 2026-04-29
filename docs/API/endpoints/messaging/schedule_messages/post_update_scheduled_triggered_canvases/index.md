<div id='api_tzevcrssxuch' class='api_div'>
<h1 id="update-scheduled-api-triggered-canvases">Update scheduled API-triggered Canvases</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/canvas/trigger/schedule/update</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to update scheduled API-triggered Canvases that were created in the dashboard.</p>
</blockquote>

<p>This allows you to decide what action triggers the message to send. You can pass in <code class="language-plaintext highlighter-rouge">trigger_properties</code> that Braze templates into the message itself.</p>

<p>Note that to send messages with this endpoint, you must have a Canvas ID, created when you build a <a href="/docs/api/identifier_types/#canvas-api-identifier">Canvas</a>.</p>

<p>Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests.</p>
<ul>
  <li>For example, if you originally provide <code class="language-plaintext highlighter-rouge">"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}</code> and then in your update you provide <code class="language-plaintext highlighter-rouge">"schedule" : {"time" : "2015-02-20T14:14:47"}</code>, Braze sends your message at the provided time in UTC, not in the user’s local time.</li>
  <li>Scheduled triggers that you update close to or during the time they were supposed to send are updated with best efforts, so Braze may apply last-second changes to all, some, or none of your targeted users.</li>
</ul>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">canvas.trigger.schedule.update</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"canvas_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"schedule_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">`schedule_id`</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">update</span><span class="w"> </span><span class="err">(obtained</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">response</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">create</span><span class="w"> </span><span class="err">schedule)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"schedule"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="err">//</span><span class="w"> </span><span class="err">required</span><span class="p">,</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">create</span><span class="w"> </span><span class="err">schedule</span><span class="w"> </span><span class="err">documentation</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">schedule_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The <code class="language-plaintext highlighter-rouge">schedule_id</code> to update (obtained from the response to create schedule).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">schedule</code></td>
      <td>Required</td>
      <td>Object</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
