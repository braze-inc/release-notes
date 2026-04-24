<div id='api_zajtsjjyljnt' class='api_div'>
<h1 id="remove-external-id">Remove external ID</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/external_ids/remove</p>
</div>

<blockquote>
  <p>Use this endpoint to remove your users’ old deprecated external IDs.</p>
</blockquote>

<p>You can send up to 50 external IDs per request.</p>

<p><strong>Warning:</strong></p>

<p>This endpoint completely removes the deprecated ID and cannot be undone. Using this endpoint to remove deprecated <code class="language-plaintext highlighter-rouge">external_ids</code> that are still associated with users in your system can permanently prevent you from finding those users’ data.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.external_ids.remove</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"external_ids"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">external</span><span class="w"> </span><span class="err">identifiers</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">remove)</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="request-parameters">Request parameters</h3>

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
      <td><code class="language-plaintext highlighter-rouge">external_ids</code></td>
      <td>Required</td>
      <td>Array of strings</td>
      <td>External identifiers for the users to remove.</td>
    </tr>
  </tbody>
</table>

<h2 id="request-example">Request example</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Important:</strong></p>

<p>Only deprecated IDs can be removed; attempting to remove a primary external ID will result in an error.</p>

<h2 id="response">Response</h2>

<p>The response will confirm all successful removals, as well as unsuccessful removals with the associated errors. Error messages in the <code class="language-plaintext highlighter-rouge">removal_errors</code> field will reference the index in the array of the original request.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre>{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) &lt;minor error message&gt;
}
</pre></td></tr></tbody></table></code></pre></div></div>

<p>The <code class="language-plaintext highlighter-rouge">message</code> field will return <code class="language-plaintext highlighter-rouge">success</code> for any valid request. More specific errors are captured in the <code class="language-plaintext highlighter-rouge">removal_errors</code> array. The <code class="language-plaintext highlighter-rouge">message</code> field returns an error in the case of:</p>
<ul>
  <li>Invalid API key</li>
  <li>Empty <code class="language-plaintext highlighter-rouge">external_ids</code> array</li>
  <li><code class="language-plaintext highlighter-rouge">external_ids</code> array with more than 50 items</li>
  <li>Rate limit hit (more than 1,000 requests/minute)</li>
</ul>

</div>
