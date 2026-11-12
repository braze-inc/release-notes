<div id='api_lihlsasdwngu' class='api_div' data-search-keywords='delete user relationship user external_id rel_kind alias alias_name alias_label deleted'>
<h1 id="delete-user-relationship">Delete user relationship</h1>
<div class="api_type"><div class="method delete ">delete</div>
<p>/data_objects/objects/{type_name}/{object_id}/users</p>
</div>

<blockquote>
  <p>Use this endpoint to remove one user-to-object relationship.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is generally available, but your workspace must be provisioned for Accounts before you can use this endpoint. To request provisioning, go to <strong>Data Settings</strong> &gt; <strong>Accounts</strong> and complete the questionnaire. For details, see <a href="/docs/user_guide/data/activation/accounts#step-1-enable-accounts">Enable Accounts</a>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.user_relationships.delete</code>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects write bucket with a default limit of 1000 requests per minute.</p>

<h2 id="path-parameters">Path parameters</h2>

<p>The following table lists and describes the path parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}/{object_id}/users</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Delete user relationship path parameters">
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
      <td><code class="language-plaintext highlighter-rouge">type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Object type</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">object_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Object identifier</td>
    </tr>
  </tbody>
</table>

<h2 id="request-parameters">Request parameters</h2>

<p>The following table lists and describes the JSON request body parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}/{object_id}/users</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Delete user relationship request parameters">
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
      <td><code class="language-plaintext highlighter-rouge">user</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>The user to relate to the object. Must contain exactly one of <code class="language-plaintext highlighter-rouge">external_id</code>, <code class="language-plaintext highlighter-rouge">braze_id</code>, <code class="language-plaintext highlighter-rouge">alias</code>, <code class="language-plaintext highlighter-rouge">email</code>, or <code class="language-plaintext highlighter-rouge">phone</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user.external_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The user’s external ID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user.braze_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The Braze user ID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user.alias</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>User alias object with <code class="language-plaintext highlighter-rouge">alias_name</code> and <code class="language-plaintext highlighter-rouge">alias_label</code> (both required when used).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user.email</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The user’s email address.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user.phone</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The user’s phone number. Must be convertible to E.164.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">rel_kind</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Relationship kind</td>
    </tr>
  </tbody>
</table>

<h3 id="identifying-the-user">Identifying the user</h3>

<ul>
  <li>Pass exactly one identifier in <code class="language-plaintext highlighter-rouge">user</code>. Zero or more than one non-null identifier returns <code class="language-plaintext highlighter-rouge">400</code>. Null identifier fields alongside one valid identifier are accepted.</li>
  <li>If an email or phone number matches more than one user profile, Braze picks the identified user (one with an <code class="language-plaintext highlighter-rouge">external_id</code>). If there’s still a tie, Braze picks the most recently updated profile.</li>
  <li>Use <code class="language-plaintext highlighter-rouge">external_id</code> where available.</li>
</ul>

<p><strong>Note:</strong></p>

<p>This <code class="language-plaintext highlighter-rouge">DELETE</code> endpoint expects a JSON request body. Validate that your HTTP client sends request bodies on <code class="language-plaintext highlighter-rouge">DELETE</code> calls.</p>

<h2 id="example-request">Example request</h2>

<p>This section includes a sample JSON payload and a sample cURL request.</p>

<h3 id="sample-request-payload">Sample request payload</h3>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"user"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"user-123"</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account_user"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>Alternate example using user alias:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"user"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"alias"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"alias_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"jane@example.com"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"alias_label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"crm_email"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account_user"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example removes the <code class="language-plaintext highlighter-rouge">account_user</code> relationship between the specified user and <code class="language-plaintext highlighter-rouge">acct-123</code>. The user profile and the account record both remain.</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> DELETE <span class="s1">'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
  "user": {
    "external_id": "user-123"
  },
  "rel_kind": "account_user"
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>This section includes a sample successful response and the response fields.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w"> </span><span class="nl">"deleted"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="w"> </span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="response-parameters">Response parameters</h3>

<p>The following table lists and describes the fields in a successful response.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Delete user relationship response parameters">
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
      <td><code class="language-plaintext highlighter-rouge">deleted</code></td>
      <td>Required</td>
      <td>Boolean</td>
      <td>Whether the relationship deletion succeeded</td>
    </tr>
  </tbody>
</table>

<h2 id="errors">Errors</h2>

<p>The following table lists common errors for this endpoint and how to resolve them.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Delete user relationship errors">
  <thead>
    <tr>
      <th>Status</th>
      <th>Cause</th>
      <th>Guidance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">400</code></td>
      <td>Missing or empty <code class="language-plaintext highlighter-rouge">user</code>, no identifier, more than one identifier, blank identifier, malformed <code class="language-plaintext highlighter-rouge">braze_id</code>, <code class="language-plaintext highlighter-rouge">email</code>, or <code class="language-plaintext highlighter-rouge">alias</code>, phone that can’t convert to E.164, or the old top-level <code class="language-plaintext highlighter-rouge">braze_id</code> body</td>
      <td>Send a <code class="language-plaintext highlighter-rouge">user</code> object with exactly one valid identifier.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">400</code></td>
      <td>Unknown <code class="language-plaintext highlighter-rouge">rel_kind</code> for the type</td>
      <td>Confirm <code class="language-plaintext highlighter-rouge">rel_kind</code> is valid for the object type.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">404</code></td>
      <td>Relationship, object, or user not found (<code class="language-plaintext highlighter-rouge">user-not-found</code>)</td>
      <td>Confirm the object, user, and relationship key values all exist.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">401</code></td>
      <td>Missing or invalid REST API key</td>
      <td>Verify the <code class="language-plaintext highlighter-rouge">Authorization</code> header uses <code class="language-plaintext highlighter-rouge">Bearer YOUR_REST_API_KEY</code> and that the key is active.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">403</code></td>
      <td>API key lacks permission or request is blocked by allowlist</td>
      <td>Confirm the key has <code class="language-plaintext highlighter-rouge">data_objects.user_relationships.delete</code> and that your source IP is on the key allowlist, if configured.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">429</code></td>
      <td>Rate limit exceeded</td>
      <td>Retry after <code class="language-plaintext highlighter-rouge">X-RateLimit-Reset</code> and reduce request frequency.</td>
    </tr>
  </tbody>
</table>
</div>
