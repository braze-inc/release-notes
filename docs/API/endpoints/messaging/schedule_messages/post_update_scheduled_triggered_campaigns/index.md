<div id='api_resaaobxstfy' class='api_div'>
<h1 id="update-scheduled-api-triggered-campaigns">Update scheduled API-triggered campaigns</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/campaigns/trigger/schedule/update</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to update scheduled API-triggered campaigns created in the dashboard, allowing you to decide what action should trigger the message to be sent.</p>
</blockquote>

<p>You can pass in <code class="language-plaintext highlighter-rouge">trigger_properties</code> that Braze templates into the message itself.</p>

<p>Note that to send messages with this endpoint, you must have a campaign ID, created when you build an <a href="/docs/api/api_campaigns/">API-Triggered Campaign</a>.</p>

<p>Any schedule completely overwrites the one you provided in the create schedule request or previous update schedule requests. For example, if you originally set the schedule to <code class="language-plaintext highlighter-rouge">"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}</code> and then later update it to <code class="language-plaintext highlighter-rouge">"schedule" : {"time" : "2015-02-20T14:14:47"}</code>, Braze sends the message at the specified time in UTC, not in the user’s local time.</p>

<p>Scheduled triggers that are updated close to or during the time they were supposed to be sent are updated with best efforts so that Braze can apply last-second changes to all, some, or none of your targeted users. Updates aren’t applied if the original schedule used local time and the original time has already passed in any time zone.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">campaigns.trigger.schedule.update</code> permission.</p>

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
  </span><span class="nl">"campaign_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">campaign_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">campaign identifier</a></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">schedule_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The <code class="language-plaintext highlighter-rouge">schedule_id</code> to update (obtained from the response to create a schedule).</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
