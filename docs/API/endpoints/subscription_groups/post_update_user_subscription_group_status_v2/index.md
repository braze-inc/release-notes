<div id='api_vlyjxxgtpeih' class='api_div'>
<h1 id="update-users-subscription-group-status-v2">Update user’s subscription group status (V2)</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/v2/subscription/status/set</p>
</div>

<blockquote>
  <p>Use this endpoint to batch update the subscription state of up to 50 users on the Braze dashboard.</p>
</blockquote>

<p>You can access a subscription group’s <code class="language-plaintext highlighter-rouge">subscription_group_id</code> by navigating to the <strong>Subscription Group</strong> page.</p>

<p>To see examples or test this endpoint for <strong>Email Subscription Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662" class="seeme">See me in Postman</a></div>

<p>To see examples or test this endpoint for <strong>SMS Subscription Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409" class="seeme">See me in Postman</a></div>

<p>To see examples or test this endpoint for <strong>WhatsApp Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">subscription.status.set</code> permission.</p>

<p><strong>Note:</strong></p>

<p>If you’re interested in using this endpoint with <a href="/docs/user_guide/channels/line/message_users/subscription_groups/">LINE subscription groups</a>, contact your customer success manager.</p>

<h2 id="differences-from-v1">Differences from V1</h2>

<p>The V2 endpoint differs from the <a href="/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/">V1 endpoint</a> in the following ways:</p>

<ul>
  <li><strong>Multiple subscription groups</strong>: V2 lets you update multiple subscription groups in a single API request, while V1 supports only one subscription group per request.</li>
  <li><strong>Update both email and SMS in one call</strong>: When using <code class="language-plaintext highlighter-rouge">external_ids</code>, you can update both email and SMS subscription groups for the same users in a single API call. With V1, you must make separate API calls for email and SMS subscription groups.</li>
  <li><strong>Using email or phone identifiers</strong>: If you use <code class="language-plaintext highlighter-rouge">emails</code> or <code class="language-plaintext highlighter-rouge">phones</code> instead of <code class="language-plaintext highlighter-rouge">external_ids</code>, you cannot update both email and SMS subscription groups in the same request. You must make separate API calls—one for email subscription groups and one for SMS subscription groups.</li>
</ul>

<p><strong>Important:</strong></p>

<p><strong>Phone number format</strong>: Phone numbers must be in <a href="https://en.wikipedia.org/wiki/E.164">E.164 format</a> (for example, <code class="language-plaintext highlighter-rouge">+12223334444</code>). Phone numbers that are not in E.164 format are rejected.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"subscription_groups"</span><span class="p">:[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"subscription_group_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="p">,</span><span class="w">
      </span><span class="nl">"subscription_state"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_ids"</span><span class="p">:</span><span class="w"> </span><span class="err">(required*</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="p">,</span><span class="w">
      </span><span class="nl">"emails"</span><span class="p">:</span><span class="w"> </span><span class="err">(required*</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="p">,</span><span class="w">
      </span><span class="nl">"phones"</span><span class="p">:</span><span class="w"> </span><span class="err">(required*</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">E.</span><span class="mi">164</span><span class="w"> </span><span class="err">format)</span><span class="p">,</span><span class="w">
      </span><span class="nl">"use_double_opt_in_logic"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>When creating new users using the <a href="/docs/api/endpoints/user_data/post_user_track/"><code class="language-plaintext highlighter-rouge">/users/track</code> endpoint</a>, you can set subscription groups within the user attributes object, which allows you to create a user and set the subscription group state in one API call.</p>

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
      <td><a href="/docs/api/identifier_types/?tab=subscription%20group%20ids"><code class="language-plaintext highlighter-rouge">subscription_group_id</code></a></td>
      <td>Required</td>
      <td>String</td>
      <td>The <code class="language-plaintext highlighter-rouge">id</code> of your subscription group.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">subscription_state</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Available values are <code class="language-plaintext highlighter-rouge">unsubscribed</code> (not in subscription group) or <code class="language-plaintext highlighter-rouge">subscribed</code> (in subscription group).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external_ids</code></td>
      <td>Required*</td>
      <td>Array of strings</td>
      <td>The <code class="language-plaintext highlighter-rouge">external_id</code> of the user or users,  may include up to 50 <code class="language-plaintext highlighter-rouge">id</code>s.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">emails</code></td>
      <td>Required*</td>
      <td>String or array of strings</td>
      <td>The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50). <br /><br />If multiple users (<code class="language-plaintext highlighter-rouge">external_id</code>) in the same workspace share the same email address, all users that share the email address are updated with the subscription group changes.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">phones</code></td>
      <td>Required*</td>
      <td>String in <a href="https://en.wikipedia.org/wiki/E.164">E.164</a> format</td>
      <td>You can pass user phone numbers as an array of strings. Must include at least one phone number (up to 50). Phone numbers must be in E.164 format (for example, <code class="language-plaintext highlighter-rouge">+12223334444</code>). <br /><br />If multiple users (<code class="language-plaintext highlighter-rouge">external_id</code>) in the same workspace share the same phone number, then all users that share the phone number are updated with the same subscription group changes.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">use_double_opt_in_logic</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Defaults to <code class="language-plaintext highlighter-rouge">false</code> if omitted. For SMS subscription groups, set to <code class="language-plaintext highlighter-rouge">true</code> to enter the user into the <a href="/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/">SMS double opt-in</a> workflow when their subscription status is set to <code class="language-plaintext highlighter-rouge">subscribed</code>. Users entered into the double opt-in workflow in this way receive at most one opt-in prompt reply message per day, regardless of the number of times they are entered into the workflow. If this parameter is omitted or set to <code class="language-plaintext highlighter-rouge">false</code>, users are subscribed without entering the double opt-in workflow. This parameter is not applicable to email subscription groups.</td>
    </tr>
  </tbody>
</table>

<p><strong>Important:</strong></p>

<p><strong>Identifier selection</strong>:</p>
<ul>
  <li>To update both email and SMS subscription groups in a single API call, use <code class="language-plaintext highlighter-rouge">external_ids</code>. You cannot include both <code class="language-plaintext highlighter-rouge">emails</code> and <code class="language-plaintext highlighter-rouge">phones</code> in the same request.</li>
  <li>If you use <code class="language-plaintext highlighter-rouge">emails</code> or <code class="language-plaintext highlighter-rouge">phones</code> instead of <code class="language-plaintext highlighter-rouge">external_ids</code>, make separate API calls—one for email subscription groups and one for SMS subscription groups.</li>
  <li>You can send <code class="language-plaintext highlighter-rouge">emails</code>, <code class="language-plaintext highlighter-rouge">phones</code>, or <code class="language-plaintext highlighter-rouge">external_ids</code> individually.</li>
</ul>

<h3 id="example-requests">Example requests</h3>

<p>The following example uses <code class="language-plaintext highlighter-rouge">external_ids</code> to update both email and SMS subscription groups in a single API call. This is only possible when using <code class="language-plaintext highlighter-rouge">external_ids</code>—you cannot update both email and SMS subscription groups in one call when using <code class="language-plaintext highlighter-rouge">emails</code> or <code class="language-plaintext highlighter-rouge">phones</code>.</p>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="email">Email</h2>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="sms-and-whatsapp">SMS and WhatsApp</h2>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
'
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
