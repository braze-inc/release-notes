<div id='api_wzgxhqtuwgtv' class='api_div'>
<h1 id="rename-external-id">Rename external ID</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/external_ids/rename</p>
</div>

<blockquote>
  <p>Use this endpoint to rename your users’ external IDs.</p>
</blockquote>

<p>You can send up to 50 rename objects per request.</p>

<p>This endpoint sets a new (primary) <code class="language-plaintext highlighter-rouge">external_id</code> for the user and deprecates their existing <code class="language-plaintext highlighter-rouge">external_id</code>. This means that the user can be identified by either <code class="language-plaintext highlighter-rouge">external_id</code> until the deprecated one is removed. Having multiple external IDs allows for a migration period so that legacy versions of your apps that use the previous external ID naming schema don’t break.</p>

<p>After your old naming schema is no longer in use, we highly recommend removing deprecated external IDs using the <a href="/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove"><code class="language-plaintext highlighter-rouge">/users/external_ids/remove</code> endpoint</a>.</p>

<p><strong>Warning:</strong></p>

<p>Make sure to remove deprecated external IDs with the <code class="language-plaintext highlighter-rouge">/users/external_ids/remove</code> endpoint instead of <code class="language-plaintext highlighter-rouge">/users/delete</code>. Sending a request to <code class="language-plaintext highlighter-rouge">/users/delete</code> with the deprecated external ID deletes the user profile entirely and cannot be undone.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.external_ids.rename</code> permission.</p>

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
  </span><span class="nl">"external_id_renames"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">external</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">rename</span><span class="w"> </span><span class="err">objects)</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">external_id_renames</code></td>
      <td>Required</td>
      <td>Array of external identifier rename objects</td>
      <td>View request example and the following limitations for the structure of the external identifier rename object.</td>
    </tr>
  </tbody>
</table>

<p>Note the following:</p>

<ul>
  <li>The <code class="language-plaintext highlighter-rouge">current_external_id</code> must be the user’s primary ID, and cannot be a deprecated ID.</li>
  <li>The <code class="language-plaintext highlighter-rouge">new_external_id</code> must not already be in use as either a primary ID or a deprecated ID.</li>
  <li>The <code class="language-plaintext highlighter-rouge">current_external_id</code> and <code class="language-plaintext highlighter-rouge">new_external_id</code> cannot be the same.</li>
</ul>

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
10
11
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>The response will confirm all successful renames, as well as unsuccessful renames with any associated errors. Error messages in the <code class="language-plaintext highlighter-rouge">rename_errors</code> field will reference the index of the object in the array of the original request.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre>{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) &lt;minor error message&gt;
}
</pre></td></tr></tbody></table></code></pre></div></div>

<p>The <code class="language-plaintext highlighter-rouge">message</code> field will return <code class="language-plaintext highlighter-rouge">success</code> for any valid request. More specific errors are captured in the <code class="language-plaintext highlighter-rouge">rename_errors</code> array. The <code class="language-plaintext highlighter-rouge">message</code> field returns an error in the case of:</p>

<ul>
  <li>Invalid API key</li>
  <li>Empty <code class="language-plaintext highlighter-rouge">external_id_renames</code> array</li>
  <li><code class="language-plaintext highlighter-rouge">external_id_renames</code> array with more than 50 objects</li>
  <li>Rate limit hit (more than 1,000 requests per minute)</li>
</ul>

<h2 id="frequently-asked-questions">Frequently asked questions</h2>

<h3 id="does-this-impact-mau">Does this impact MAU?</h3>
<p>No, because the number of users stays the same, they have a new <code class="language-plaintext highlighter-rouge">external_id</code>.</p>

<h3 id="does-user-behavior-change-historically">Does user behavior change historically?</h3>
<p>No, because the user is still the same, and all their historical behavior is still connected to them.</p>

<h3 id="can-it-be-run-on-development-or-staging-workspaces">Can it be run on development or staging workspaces?</h3>
<p>Yes. In fact, we highly recommend running a test migration on a staging or development workspace, and ensuring everything has gone smoothly before executing on production data.</p>

<h3 id="does-this-log-data-points">Does this log data points?</h3>
<p>This feature does not log data points.</p>

<h3 id="what-is-the-recommended-deprecation-period">What is the recommended deprecation period?</h3>
<p>We have no hard limit on how long you can keep deprecated external IDs around, but we highly recommend removing them after there is no longer a need to reference users by the deprecated ID.</p>

</div>
