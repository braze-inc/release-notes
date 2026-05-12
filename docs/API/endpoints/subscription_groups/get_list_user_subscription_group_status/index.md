<div id='api_cijbnmfqdwpg' class='api_div'>
<h1 id="list-users-subscription-group-status">List user’s subscription group status</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/subscription/status/get</p>
</div>

<blockquote>
  <p>Use this endpoint to get the subscription state of a user in a subscription group.</p>
</blockquote>

<p>These groups will be available on the <strong>Subscription Group</strong> page. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.</p>

<p>If you want to see examples or test this endpoint for <strong>Email Subscription Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2" class="seeme">See me in Postman</a></div>

<p>If you want to see examples or test this endpoint for <strong>SMS Subscription Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557" class="seeme">See me in Postman</a></div>

<p>If you want to see examples or test this endpoint for <strong>WhatsApp Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">subscription.status.get</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

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
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required*</td>
      <td>String</td>
      <td>The <code class="language-plaintext highlighter-rouge">external_id</code> of the user (must include at least one and at most 50 <code class="language-plaintext highlighter-rouge">external_ids</code>). <br /><br />When both an <code class="language-plaintext highlighter-rouge">external_id</code> and <code class="language-plaintext highlighter-rouge">email</code>/<code class="language-plaintext highlighter-rouge">phone</code> are submitted, only the <code class="language-plaintext highlighter-rouge">external_id</code>(s) provided will be applied to the result query.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">email</code></td>
      <td>Required*</td>
      <td>String</td>
      <td>The email address of the user. It can be passed as an array of strings with a maximum of 50.<br /><br /> Submitting both an email address and phone number (with no <code class="language-plaintext highlighter-rouge">external_id</code>) will result in an error.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">phone</code></td>
      <td>Required*</td>
      <td>String in <a href="https://en.wikipedia.org/wiki/E.164">E.164</a> format</td>
      <td>The phone number of the user. If email is not included, you must include at least one phone number (with a maximum of 50).<br /><br /> Submitting both an email address and phone number (with no <code class="language-plaintext highlighter-rouge">external_id</code>) will result in an error.</td>
    </tr>
  </tbody>
</table>

<p class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" role="presentation">*One of <code class="language-plaintext highlighter-rouge">external_id</code> or <code class="language-plaintext highlighter-rouge">email</code> or <code class="language-plaintext highlighter-rouge">phone</code> is required for each user.</p>

<ul>
  <li>For SMS and WhatsApp subscription groups, either <code class="language-plaintext highlighter-rouge">external_id</code> or <code class="language-plaintext highlighter-rouge">phone</code> is required.  When both are submitted, only the <code class="language-plaintext highlighter-rouge">external_id</code> is used for querying and the phone number is applied to that user.</li>
  <li>For email subscription groups, either <code class="language-plaintext highlighter-rouge">external_id</code> or <code class="language-plaintext highlighter-rouge">email</code> is required.  When both are submitted, only the <code class="language-plaintext highlighter-rouge">external_id</code> is used for the query and the email address is applied to that user.</li>
</ul>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&amp;external_id[]=1&amp;external_id[]=2
</pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&amp;phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&amp;email=example@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>All successful responses will return <code class="language-plaintext highlighter-rouge">Subscribed</code>, <code class="language-plaintext highlighter-rouge">Unsubscribed</code>, or <code class="language-plaintext highlighter-rouge">Unknown</code> depending on status and user history with the subscription group.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"1"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unsubscribed"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"2"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Subscribed"</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Important:</strong></p>

<p>This endpoint returns the subscription group status independently of the user’s global subscription state. If a user is globally unsubscribed, the Braze dashboard shows them as unsubscribed from each subscription group. However, this endpoint still returns the last saved subscription group status (for example, <code class="language-plaintext highlighter-rouge">Subscribed</code>) because the global subscription state supersedes individual subscription groups without overwriting them.<br /><br />Braze preserves individual subscription group states so that if the user globally resubscribes, each subscription group reverts to its previously saved status. To determine a user’s effective subscription state, check both their global subscription status and the subscription group status returned by this endpoint.</p>

</div>
