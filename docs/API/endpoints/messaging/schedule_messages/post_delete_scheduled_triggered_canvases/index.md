<div id='api_pvczlanniqad' class='api_div'>
<h1 id="delete-scheduled-api-triggered-canvases">Delete scheduled API-triggered Canvases</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/canvas/trigger/schedule/delete</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>The delete schedule endpoint allows you to cancel a message that you previously scheduled API-triggered Canvases before it has been sent.</p>
</blockquote>

<p>Scheduled messages or triggers that are deleted close to or during the time they were supposed to be sent are updated with best efforts, so Braze may apply last-second deletions to all, some, or none of your targeted users.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">canvas.trigger.schedule.delete</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"canvas_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"schedule_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">`schedule_id`</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">delete</span><span class="w"> </span><span class="err">(obtained</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">response</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">create</span><span class="w"> </span><span class="err">schedule)</span><span class="w">
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
      <td>Required</td>
      <td>String</td>
      <td>The <code class="language-plaintext highlighter-rouge">schedule_id</code> to delete (obtained from the response to create schedule).</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
