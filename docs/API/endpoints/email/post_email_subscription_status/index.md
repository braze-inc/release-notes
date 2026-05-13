<div id='api_jwoxlnogxwdf' class='api_div'>
<h1 id="change-email-subscription-status">Change email subscription status</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/email/status</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to set the email subscription state for your users.</p>
</blockquote>

<p>Users can be <code class="language-plaintext highlighter-rouge">opted_in</code>, <code class="language-plaintext highlighter-rouge">unsubscribed</code>, or <code class="language-plaintext highlighter-rouge">subscribed</code> (not specifically opted in or out).</p>

<p>You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded will be automatically set.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">email.status</code> permission.</p>

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
  </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="s2">"example@braze.com"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"subscription_state"</span><span class="p">:</span><span class="w"> </span><span class="s2">"subscribed"</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">email</code></td>
      <td>Required</td>
      <td>String or array</td>
      <td>String email address to modify, or an array of up to 50 email addresses to modify.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">subscription_state</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Either “subscribed”, “unsubscribed”, or “opted_in”.</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
