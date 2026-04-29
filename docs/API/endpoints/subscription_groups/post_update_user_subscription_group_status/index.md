<div id='api_boiehsfspxrv' class='api_div'>
<h1 id="update-users-subscription-group-status">Update user’s subscription group status</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/subscription/status/set</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to batch update the subscription state of up to 50 users on the Braze dashboard.</p>
</blockquote>

<p>You can access a subscription group’s <code class="language-plaintext highlighter-rouge">subscription_group_id</code> by navigating to the <strong>Subscription Group</strong> page.</p>

<p>If you want to see examples or test this endpoint for <strong>Email Subscription Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9" class="seeme">See me in Postman</a></div>

<p>If you want to see examples or test this endpoint for <strong>SMS and RCS Subscription Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">subscription.status.set</code> permission.</p>

<p><strong>Note:</strong></p>

<p>If you’re interested in using this endpoint with <a href="/docs/user_guide/channels/line/message_users/subscription_groups/">LINE subscription groups</a>, contact your customer success manager.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
   </span><span class="nl">"subscription_group_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">id</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="p">,</span><span class="w">
   </span><span class="nl">"subscription_state"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">available</span><span class="w"> </span><span class="err">values</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="s2">"unsubscribed"</span><span class="w"> </span><span class="err">(not</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group)</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"subscribed"</span><span class="w"> </span><span class="err">(in</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group)</span><span class="p">,</span><span class="w">
   </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required*</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">external</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">users</span><span class="p">,</span><span class="w"> </span><span class="err">may</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">up</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="mi">50</span><span class="w"> </span><span class="err">IDs</span><span class="p">,</span><span class="w">
   </span><span class="nl">"phone"</span><span class="p">:</span><span class="w"> </span><span class="err">(required*</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">E.</span><span class="mi">164</span><span class="w"> </span><span class="err">format)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">phone</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">(must</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">least</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">phone</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">most</span><span class="w"> </span><span class="mi">50</span><span class="w"> </span><span class="err">phone</span><span class="w"> </span><span class="err">numbers)</span><span class="p">,</span><span class="w">
   </span><span class="nl">"use_double_opt_in_logic"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">`</span><span class="kc">false</span><span class="err">`;</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">`subscription_state`</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="s2">"subscribed"</span><span class="p">,</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">`</span><span class="kc">true</span><span class="err">`</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">enter</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">into</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">SMS</span><span class="w"> </span><span class="err">double</span><span class="w"> </span><span class="err">opt-in</span><span class="w"> </span><span class="err">workflow</span><span class="p">,</span><span class="w">
   </span><span class="err">//</span><span class="w"> </span><span class="err">SMS</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">RCS</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">-</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">external_id</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">phone</span><span class="w">
 </span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>
<p>* SMS and RCS subscription groups: Braze accepts only <code class="language-plaintext highlighter-rouge">external_id</code> or <code class="language-plaintext highlighter-rouge">phone</code>.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
   </span><span class="nl">"subscription_group_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">id</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="p">,</span><span class="w">
   </span><span class="nl">"subscription_state"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">available</span><span class="w"> </span><span class="err">values</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="s2">"unsubscribed"</span><span class="w"> </span><span class="err">(not</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group)</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"subscribed"</span><span class="w"> </span><span class="err">(in</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group)</span><span class="p">,</span><span class="w">
   </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required*</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">external</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">users</span><span class="p">,</span><span class="w"> </span><span class="err">may</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">up</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="mi">50</span><span class="w"> </span><span class="err">IDs</span><span class="p">,</span><span class="w">
   </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(required*</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">address</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">(must</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">least</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">most</span><span class="w"> </span><span class="mi">50</span><span class="w"> </span><span class="err">emails)</span><span class="p">,</span><span class="w">
   </span><span class="err">//</span><span class="w"> </span><span class="err">Email</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">-</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">external_id</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">email</span><span class="w">
   </span><span class="err">//</span><span class="w"> </span><span class="err">Note</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">sending</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">address</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">linked</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">multiple</span><span class="w"> </span><span class="err">profiles</span><span class="w"> </span><span class="err">updates</span><span class="w"> </span><span class="err">all</span><span class="w"> </span><span class="err">relevant</span><span class="w"> </span><span class="err">profiles</span><span class="w">
 </span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>
<p>* Email subscription groups: You must include either <code class="language-plaintext highlighter-rouge">email</code> or <code class="language-plaintext highlighter-rouge">external_id</code>.</p>

<p>This property should not be used for updating a user’s profile information. Use the <a href="/docs/api/endpoints/user_data/post_user_track/">/users/track</a> property instead.</p>

<p><strong>Tip:</strong></p>

<p><strong>Adding existing users to a subscription group:</strong> This endpoint is the recommended way to backfill or bulk-update subscription group membership for existing users. You can pass up to 50 <code class="language-plaintext highlighter-rouge">external_id</code>s, email addresses, or phone numbers per request. Users can also update their own subscription status through an <a href="/docs/user_guide/channels/email/subscriptions/">email preference center</a> link.</p>

<p><strong>Creating new users with a subscription group:</strong> When creating new users using the <a href="/docs/api/endpoints/user_data/post_user_track/"><code class="language-plaintext highlighter-rouge">/users/track</code></a> endpoint, you can set subscription groups within the user attributes object, which allows you to create a user and set the subscription group state in one API call.</p>

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
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required*</td>
      <td>Array of strings</td>
      <td>The <code class="language-plaintext highlighter-rouge">external_id</code> of the user or users, may include up to 50 <code class="language-plaintext highlighter-rouge">id</code>s.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">email</code></td>
      <td>Required*</td>
      <td>String or array of strings</td>
      <td>The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50). <br /><br />If multiple users (<code class="language-plaintext highlighter-rouge">external_id</code>) in the same workspace share the same email address, then Braze updates all users that share the email address with the subscription group changes.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">phone</code></td>
      <td>Required*</td>
      <td>String in <a href="https://en.wikipedia.org/wiki/E.164">E.164</a> format</td>
      <td>The phone number of the user, can be passed as an array of strings. Must include at least one phone number (up to 50). <br /><br />If multiple users (<code class="language-plaintext highlighter-rouge">external_id</code>) in the same workspace share the same phone number, then Braze updates all users that share the phone number with the same subscription group changes.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">use_double_opt_in_logic</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Applies only to SMS subscription groups; ignored for email and other subscription group types. Defaults to <code class="language-plaintext highlighter-rouge">false</code> if omitted. For SMS subscription groups, set to <code class="language-plaintext highlighter-rouge">true</code> to enter the user into the <a href="/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/">SMS double opt-in</a> workflow when their subscription status is set to <code class="language-plaintext highlighter-rouge">subscribed</code>. Users entered into the double opt-in workflow in this way receive at most one opt-in prompt reply message per day, regardless of the number of times they are entered into the workflow. If this parameter is omitted or set to <code class="language-plaintext highlighter-rouge">false</code>, users are subscribed without entering the double opt-in workflow.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-requests">Example requests</h2>

<h3 id="email">Email</h3>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sms-and-rcs">SMS and RCS</h3>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="example-success-response">Example success response</h2>

<p>The status code <code class="language-plaintext highlighter-rouge">201</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Important:</strong></p>

<p>The endpoint accepts only the <code class="language-plaintext highlighter-rouge">email</code> or <code class="language-plaintext highlighter-rouge">phone</code> value, not both. If you provide both, you receive this response: <code class="language-plaintext highlighter-rouge">{"message":"Either an email address or a phone number should be provided, but not both."}</code></p>

</div>

