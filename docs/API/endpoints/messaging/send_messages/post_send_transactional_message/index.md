<div id='api_pduffnqmbtxz' class='api_div'>
<h1 id="send-transactional-emails-using-api-triggered-delivery">Send transactional emails using API-triggered delivery</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/transactional/v1/campaigns/{campaign_id}/send</p>
</div>

<blockquote>
  <p>Use this endpoint to send immediate, one-off transactional messages to a designated user.</p>
</blockquote>

<p>This endpoint is used alongside the creation of a Braze <a href="/docs/api/api_campaigns/transactional_campaigns">Transactional Email campaign</a> and corresponding campaign ID.</p>

<p><strong>Important:</strong></p>

<p>Transactional Email is currently available as part of select Braze packages. Contact your Braze customer success manager for more details.</p>

<p>Similar to the <a href="/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/">Send triggered campaign endpoint</a>, this campaign type allows you to house message content inside of the Braze dashboard while dictating when and to whom a message is sent via your API. Unlike the Send triggered campaign endpoint, which accepts an audience or segment to send messages to, a request to this endpoint must specify a single user either by <code class="language-plaintext highlighter-rouge">external_user_id</code> or <code class="language-plaintext highlighter-rouge">user_alias</code>, as this campaign type is purpose-built for 1:1 messaging of alerts like order confirmations or password resets.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cec874e1-fa51-42a6-9a8d-7fc57d6a63bc" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need to generate an API key with the <code class="language-plaintext highlighter-rouge">transactional.send</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

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
      <td>ID of the campaign</td>
    </tr>
  </tbody>
</table>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"external_send_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">following</span><span class="w"> </span><span class="err">request</span><span class="w"> </span><span class="err">parameters</span><span class="p">,</span><span class="w">
  </span><span class="nl">"trigger_properties"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">personalization</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">apply</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w">
  </span><span class="nl">"recipient"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="err">//</span><span class="w"> </span><span class="err">Either</span><span class="w"> </span><span class="s2">"external_user_id"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"user_alias"</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">required.</span><span class="w"> </span><span class="err">Requests</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">specify</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">one.</span><span class="w">
      </span><span class="nl">"user_alias"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">User</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">User</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">receive</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_user_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">External</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">receive</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
      </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">fields</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">object</span><span class="w"> </span><span class="err">create</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">update</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">given</span><span class="w"> </span><span class="err">value</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">specified</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">profile</span><span class="w"> </span><span class="err">before</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">existing</span><span class="w"> </span><span class="err">values</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">overwritten</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">external_send_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A Base64 compatible string. Validated against the following regex:<br /><br /> <code class="language-plaintext highlighter-rouge">/^[a-zA-Z0-9-_+\/=]+$/</code> <br /><br />This optional field allows you to pass an internal identifier for this particular send, which is included in events sent from the Transactional HTTP event postback. When passed, this identifier is also used as a deduplication key, which Braze stores for 24 hours. <br /><br />Passing the same identifier in another request does not result in a new instance of a send by Braze for 24 hours.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">trigger_properties</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>See <a href="/docs/api/objects_filters/trigger_properties_object/">trigger properties</a>. Personalization key-value pairs that apply to the user in this request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">recipient</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>The user you are targeting this message to. Can contain <code class="language-plaintext highlighter-rouge">attributes</code> and a single <code class="language-plaintext highlighter-rouge">external_user_id</code> or <code class="language-plaintext highlighter-rouge">user_alias</code>.<br /><br />Note that if you provide an external user ID that doesn’t already exist in Braze, passing any fields to the <code class="language-plaintext highlighter-rouge">attributes</code> object creates this user profile in Braze and sends this message to the newly created user. <br /><br />If you send multiple requests to the same user with different data in the <code class="language-plaintext highlighter-rouge">attributes</code> object, <code class="language-plaintext highlighter-rouge">first_name</code>, <code class="language-plaintext highlighter-rouge">last_name</code>, and <code class="language-plaintext highlighter-rouge">email</code> attributes are updated synchronously and templated into your message. Custom attributes don’t have this same protection, so proceed with caution when updating a user through this API and passing different custom attribute values in quick succession.</td>
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
</pre></td><td class="rouge-code"><pre>curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer YOUR-REST-API-KEY' \
  -d '{
        "external_send_id" : YOUR_BASE64_COMPATIBLE_ID
        "trigger_properties": {
          "example_string_property": YOUR_EXAMPLE_STRING,
          "example_integer_property": YOUR_EXAMPLE_INTEGER
        },
        "recipient": {
          "external_user_id": TARGETED_USER_ID_STRING
        }
      }' \
  https://rest.iad-01.braze.com/transactional/v1/campaigns/{campaign_id}/send
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>The Send transactional email endpoint responds with the message’s <code class="language-plaintext highlighter-rouge">dispatch_id</code> which represents the instance of this message send. This identifier can be used along with events from the Transactional HTTP event postback to trace the status of an individual email sent to a single user.</p>

<h3 id="example-responses">Example responses</h3>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"dispatch_id"</span><span class="p">:</span><span class="w"> </span><span class="err">A</span><span class="w"> </span><span class="err">randomly-generated</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">instance</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">send</span><span class="w">
    </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="err">Current</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">Object</span><span class="w"> </span><span class="err">containing</span><span class="w"> </span><span class="err">additional</span><span class="w"> </span><span class="err">information</span><span class="w"> </span><span class="err">about</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">instance</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<p>The endpoint may also return an error code and a human-readable message in some cases, most of which are validation errors. Here are some common errors you may get when making invalid requests.</p>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Error</th>
      <th>Troubleshooting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">The campaign is not a transactional campaign. Only transactional campaigns may use this endpoint</code></td>
      <td>The campaign ID provided is not for a transactional campaign.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">The external reference has been queued.  Please retry to obtain send_id.</code></td>
      <td>The external_send_id has been created recently, try a new external_send_id if you are intending to send a new message.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Campaign does not exist</code></td>
      <td>The campaign ID provided does not correspond to an existing campaign.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">The campaign is archived. Unarchive the campaign in order for trigger requests to take effect.</code></td>
      <td>The campaign ID provided corresponds to an archived campaign.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">The campaign is paused. Resume the campaign in order for trigger requests to take effect.</code></td>
      <td>The campaign ID provided corresponds to a paused campaign.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">campaign_id must be a string of the campaign api identifier</code></td>
      <td>The campaign ID provided is not a valid format.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Error authenticating credentials</code></td>
      <td>The API key provided is invalid</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Invalid whitelisted IPs </code></td>
      <td>The IP address sending the request is not on the IP whitelist (if it is being used)</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">You do not have permission to access this resource</code></td>
      <td>The API key used does not have permission to take this action</td>
    </tr>
  </tbody>
</table>

<p>Most endpoints at Braze have a rate limit implementation that returns a 429 response code if you make too many requests. The transactional sending endpoint has a paid hourly allotment measured in units (for example, 50,000 units per hour, depending on your package). There is no separate per-endpoint rate limit for this endpoint: you can send beyond your allotted volume, but only the allotted volume is covered by SLA; requests above that allotment still send but are not covered by SLA. Requests to this endpoint count toward your <a href="/docs/api/api_limits/">overall external API rate limit</a>. If you exceed that limit (for example, 250,000 requests per hour across all endpoints), Braze returns 429 and throttles requests until the limit resets. The transactional volume count resets each hour. Contact Braze Support if you need more information about this functionality.</p>

<h2 id="transactional-http-event-postback">Transactional HTTP event postback</h2>

<p>All transactional emails are complemented with event status postbacks sent as an HTTP request back to your specified URL. This will allow you to evaluate the message status in real-time and take action to reach the user on another channel if the message goes undelivered, or fallback to an internal system if Braze is experiencing latency.</p>

<p>You can associate these updates with individual messages using unique identifiers:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">dispatch_id</code>: A unique ID Braze automatically generates for each message.</li>
  <li><code class="language-plaintext highlighter-rouge">external_send_id</code>: A custom identifier you provide, such as an order number, to match updates with your internal systems.</li>
</ul>

<p>For example, If you include <code class="language-plaintext highlighter-rouge">external_send_id: 1234</code> in the request when sending an order confirmation email, all subsequent event postbacks for that email—like <code class="language-plaintext highlighter-rouge">Sent</code> or <code class="language-plaintext highlighter-rouge">Delivered</code>—will include <code class="language-plaintext highlighter-rouge">external_send_id: 1234</code>. This allows you to confirm whether the customer for order #1234 received their order confirmation email.</p>

<h3 id="setting-up-postbacks">Setting up postbacks</h3>

<p>In your Braze dashboard:</p>

<ol>
  <li>Go to <strong>Settings</strong> &gt; <strong>Email Preferences</strong>.</li>
  <li>Under <strong>Transactional Event Status Postback</strong>, enter the URL where Braze should send status updates for your transactional emails.</li>
  <li>Test the postback.</li>
</ol>

<p><img src="/docs/assets/img/transactional_webhook_url.png?567829e92a620f3227cb64ce58d3f634" alt="" /></p>

<h3 id="postback-body">Postback body</h3>

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
  </span><span class="nl">"dispatch_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">randomly-generated</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">instance</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">send)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">Current</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">following</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">table</span><span class="p">,</span><span class="w">
  </span><span class="nl">"metadata"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(object</span><span class="p">,</span><span class="w"> </span><span class="err">additional</span><span class="w"> </span><span class="err">information</span><span class="w"> </span><span class="err">relating</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">execution</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">event)</span><span class="w">
   </span><span class="p">{</span><span class="w">
     </span><span class="nl">"external_send_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">If</span><span class="w"> </span><span class="err">provided</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">pass</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">internal</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">all</span><span class="w"> </span><span class="err">postbacks)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"campaign_api_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">transactional</span><span class="w"> </span><span class="err">campaign)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"received_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">DateTime</span><span class="w"> </span><span class="err">string</span><span class="p">,</span><span class="w"> </span><span class="err">Timestamp</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">received</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">Braze</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"sent"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"enqueued_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">DateTime</span><span class="w"> </span><span class="err">string</span><span class="p">,</span><span class="w"> </span><span class="err">Timestamp</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">enqueued</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">Braze</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"sent"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"executed_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">DateTime</span><span class="w"> </span><span class="err">string</span><span class="p">,</span><span class="w"> </span><span class="err">Timestamp</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">processed</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">Braze</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"sent"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"sent_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">DateTime</span><span class="w"> </span><span class="err">string</span><span class="p">,</span><span class="w"> </span><span class="err">Timestamp</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">ESP</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">Braze</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"sent"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"processed_at"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">DateTime</span><span class="w"> </span><span class="err">string</span><span class="p">,</span><span class="w"> </span><span class="err">Timestamp</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">processed</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">ESP</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"processed"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"delivered_at"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">DateTime</span><span class="w"> </span><span class="err">string</span><span class="p">,</span><span class="w"> </span><span class="err">Timestamp</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">delivered</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user's</span><span class="w"> </span><span class="err">inbox</span><span class="w"> </span><span class="err">provider</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"processed"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"bounced_at"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">DateTime</span><span class="w"> </span><span class="err">string</span><span class="p">,</span><span class="w"> </span><span class="err">Timestamp</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">bounced</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user's</span><span class="w"> </span><span class="err">inbox</span><span class="w"> </span><span class="err">provider</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"bounced"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"aborted_at"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">DateTime</span><span class="w"> </span><span class="err">string</span><span class="p">,</span><span class="w"> </span><span class="err">Timestamp</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">Aborted</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">Braze</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"aborted"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
     </span><span class="nl">"reason"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">reason</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Inbox</span><span class="w"> </span><span class="err">provider</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">unable</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">process</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="s2">"aborted"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"bounced"</span><span class="w"> </span><span class="err">status)</span><span class="p">,</span><span class="w">
   </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h4 id="message-status">Message status</h4>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Status</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">sent</code></td>
      <td>Message successfully dispatched to a Braze email sending partner</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">processed</code></td>
      <td>Email sending partner has successfully received and prepared the message for sending to the user’s inbox provider</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">aborted</code></td>
      <td>Braze was unable to successfully dispatch the message due to the user not having an emailable address, or Liquid abort logic was called in the message body. All aborted events include a <code class="language-plaintext highlighter-rouge">reason</code> field within the metadata object indicating why the message was aborted</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">delivered</code></td>
      <td>Message was accepted by the user’s email inbox provider</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">bounced</code></td>
      <td>Message was rejected by the user’s email inbox provider. All bounced events include a <code class="language-plaintext highlighter-rouge">reason</code> field within the metadata object reflecting the bounce error code provided by the inbox provider</td>
    </tr>
  </tbody>
</table>

<h3 id="example-postback">Example postback</h3>
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
</pre></td><td class="rouge-code"><pre><span class="w">
</span><span class="err">//</span><span class="w"> </span><span class="err">Sent</span><span class="w"> </span><span class="err">Event</span><span class="w">
</span><span class="p">{</span><span class="w">
    </span><span class="nl">"dispatch_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acf471119f7449d579e8089032003ded"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sent"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"received_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-31T18:58:41.000+00:00"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"enqueued_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-31T18:58:41.000+00:00"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"executed_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-31T18:58:41.000+00:00"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"sent_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-31T18:58:42.000+00:00"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"campaign_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"417220e4-5a2a-b634-7f7d-9ec891532368"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_send_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"34a2ceb3cf6184132f3d816e9984269a"</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">

</span><span class="err">//</span><span class="w"> </span><span class="err">Processed</span><span class="w"> </span><span class="err">Event</span><span class="w">
</span><span class="p">{</span><span class="w">
    </span><span class="nl">"dispatch_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acf471119f7449d579e8089032003ded"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"processed"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"processed_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-31T18:58:42.000+00:00"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"campaign_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"417220e4-5a2a-b634-7f7d-9ec891532368"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_send_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"34a2ceb3cf6184132f3d816e9984269a"</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">

</span><span class="err">//</span><span class="w"> </span><span class="err">Aborted</span><span class="w">
</span><span class="p">{</span><span class="w">
    </span><span class="nl">"dispatch_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acf471119f7449d579e8089032003ded"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"aborted"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"reason"</span><span class="p">:</span><span class="w"> </span><span class="s2">"User not emailable"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"aborted_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-31T19:04:51.000+00:00"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"campaign_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"417220e4-5a2a-b634-7f7d-9ec891532368"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_send_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"34a2ceb3cf6184132f3d816e9984269a"</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">

</span><span class="err">//</span><span class="w"> </span><span class="err">Delivered</span><span class="w"> </span><span class="err">Event</span><span class="w">
</span><span class="p">{</span><span class="w">
    </span><span class="nl">"dispatch_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acf471119f7449d579e8089032003ded"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"delivered"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"delivered_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-31T18:27:32.000+00:00"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"campaign_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"417220e4-5a2a-b634-7f7d-9ec891532368"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_send_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"34a2ceb3cf6184132f3d816e9984269a"</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">

</span><span class="err">//</span><span class="w"> </span><span class="err">Bounced</span><span class="w"> </span><span class="err">Event</span><span class="w">
</span><span class="p">{</span><span class="w">
    </span><span class="nl">"dispatch_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acf471119f7449d579e8089032003ded"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"bounced"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"bounced_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-08-31T18:58:43.000+00:00"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"reason"</span><span class="p">:</span><span class="w"> </span><span class="s2">"550 5.1.1 The email account that you tried to reach does not exist"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"campaign_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"417220e4-5a2a-b634-7f7d-9ec891532368"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_send_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"34a2ceb3cf6184132f3d816e9984269a"</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">

</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>