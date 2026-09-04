<div id='api_neztyesmuxup' class='api_div' data-search-keywords='create user relationship braze_id rel_kind attributes role user_relationship type_name external_id user'>
<h1 id="create-user-relationship">Create user relationship</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/data_objects/objects/{type_name}/{external_id}/users</p>
</div>

<blockquote>
  <p>Use this endpoint to link one Braze user to one data object.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on <strong>Settings</strong> &gt; <strong>API Keys</strong>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.user_relationships.create</code>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.</p>

<h2 id="path-parameters">Path parameters</h2>

<p>The following table lists and describes the path parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}/{external_id}/users</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Create user relationship path parameters">
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
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Object identifier</td>
    </tr>
  </tbody>
</table>

<h2 id="request-parameters">Request parameters</h2>

<p>The following table lists and describes the JSON request body parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}/{external_id}/users</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Create user relationship request parameters">
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
      <td><code class="language-plaintext highlighter-rouge">braze_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Braze user ID</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">rel_kind</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Relationship kind</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">attributes</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>Relationship attributes</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<p>This section includes a sample JSON payload and a sample cURL request.</p>

<h3 id="sample-request-payload">Sample request payload</h3>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"braze_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"507f1f77bcf86cd799439011"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account_user"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"role"</span><span class="p">:</span><span class="w"> </span><span class="s2">"owner"</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example links a user to <code class="language-plaintext highlighter-rouge">acct-123</code> as an <code class="language-plaintext highlighter-rouge">account_user</code> and records their <code class="language-plaintext highlighter-rouge">role</code> as <code class="language-plaintext highlighter-rouge">owner</code>.</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
10
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>This section includes a sample successful response and the response fields.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">201</code> could return the following response body.</p>

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
  </span><span class="nl">"user_relationship"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acct-123"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account_user"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"user"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"braze_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"507f1f77bcf86cd799439011"</span><span class="w"> </span><span class="p">},</span><span class="w">
    </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"role"</span><span class="p">:</span><span class="w"> </span><span class="s2">"owner"</span><span class="w"> </span><span class="p">}</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="response-parameters">Response parameters</h3>

<p>The following table lists and describes the fields in a successful response.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Create user relationship response parameters">
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
      <td><code class="language-plaintext highlighter-rouge">user_relationship</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Created user relationship record</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_relationship.type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Data object type machine name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_relationship.external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Data object identifier</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_relationship.rel_kind</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Relationship kind value</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_relationship.user</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Linked user object</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_relationship.user.braze_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Braze user identifier</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_relationship.attributes</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Relationship attributes</td>
    </tr>
  </tbody>
</table>

<h2 id="errors">Errors</h2>

<p>The following table lists common errors for this endpoint and how to resolve them.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Create user relationship errors">
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
      <td>Unknown <code class="language-plaintext highlighter-rouge">rel_kind</code> for the type or schema validation error</td>
      <td>Confirm <code class="language-plaintext highlighter-rouge">rel_kind</code> is valid for the object type and <code class="language-plaintext highlighter-rouge">attributes</code> match the relationship schema.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">404</code></td>
      <td>Type or object not found</td>
      <td>Confirm <code class="language-plaintext highlighter-rouge">type_name</code> and <code class="language-plaintext highlighter-rouge">external_id</code> both exist in the workspace.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">409</code></td>
      <td>Duplicate relationship (<code class="language-plaintext highlighter-rouge">duplicate-user-relationship</code>)</td>
      <td>Use <code class="language-plaintext highlighter-rouge">PUT</code> to replace the existing relationship, or delete it before creating again.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">422</code></td>
      <td>Objects-per-user limit reached (<code class="language-plaintext highlighter-rouge">data-objects-per-user-limit-exceeded</code>) or users-per-object limit reached (<code class="language-plaintext highlighter-rouge">users-per-data-object-limit-exceeded</code>)</td>
      <td>Reduce the relationship count for the user or the object, or contact Braze support about your workspace limits.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">401</code></td>
      <td>Missing or invalid REST API key</td>
      <td>Verify the <code class="language-plaintext highlighter-rouge">Authorization</code> header uses <code class="language-plaintext highlighter-rouge">Bearer YOUR_REST_API_KEY</code> and that the key is active.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">403</code></td>
      <td>API key lacks permission or request is blocked by allowlist</td>
      <td>Confirm the key has <code class="language-plaintext highlighter-rouge">data_objects.user_relationships.create</code> and that your source IP is on the key allowlist, if configured.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">429</code></td>
      <td>Rate limit exceeded</td>
      <td>Retry after <code class="language-plaintext highlighter-rouge">X-RateLimit-Reset</code> and reduce request frequency.</td>
    </tr>
  </tbody>
</table>
</div>
