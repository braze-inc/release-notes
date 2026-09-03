<div id='api_erhwsxvojmho' class='api_div' data-search-keywords='delete object relationship rel_kind related_type_name related_external_id anchor deleted'>
<h1 id="delete-object-relationship">Delete object relationship</h1>
<div class="api_type"><div class="method delete ">delete</div>
<p>/data_objects/objects/{type_name}/{external_id}/object_relationships</p>
</div>

<blockquote>
  <p>Use this endpoint to delete one object-to-object relationship edge.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on <strong>Settings</strong> &gt; <strong>API Keys</strong>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.object_relationships.delete</code>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.</p>

<h2 id="path-parameters">Path parameters</h2>

<p>The following table lists and describes the path parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}/{external_id}/object_relationships</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Delete object relationship path parameters">
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
      <td>URL object type</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>URL object identifier</td>
    </tr>
  </tbody>
</table>

<h2 id="request-parameters">Request parameters</h2>

<p>The following table lists and describes the JSON request body parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}/{external_id}/object_relationships</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Delete object relationship request parameters">
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
      <td><code class="language-plaintext highlighter-rouge">rel_kind</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Relationship kind</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">related_type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Related object type</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">related_external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Related object identifier</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">anchor</code></td>
      <td>Optional</td>
      <td>String</td>
      <td><code class="language-plaintext highlighter-rouge">source</code> (default) or <code class="language-plaintext highlighter-rouge">target</code></td>
    </tr>
  </tbody>
</table>

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
  </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"subaccount"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"related_type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"related_external_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acct-456"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"source"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example removes the <code class="language-plaintext highlighter-rouge">subaccount</code> relationship between <code class="language-plaintext highlighter-rouge">acct-123</code> and <code class="language-plaintext highlighter-rouge">acct-456</code>. Both account records remain.</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> DELETE <span class="s1">'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
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

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Delete object relationship response parameters">
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

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Delete object relationship errors">
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
      <td>Validation error</td>
      <td>Confirm the request body includes valid <code class="language-plaintext highlighter-rouge">rel_kind</code>, <code class="language-plaintext highlighter-rouge">related_type_name</code>, <code class="language-plaintext highlighter-rouge">related_external_id</code>, and <code class="language-plaintext highlighter-rouge">anchor</code> values.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">404</code></td>
      <td>Relationship or endpoint object not found</td>
      <td>Confirm both objects exist and the relationship key values match an existing edge.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">401</code></td>
      <td>Missing or invalid REST API key</td>
      <td>Verify the <code class="language-plaintext highlighter-rouge">Authorization</code> header uses <code class="language-plaintext highlighter-rouge">Bearer YOUR_REST_API_KEY</code> and that the key is active.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">403</code></td>
      <td>API key lacks permission or request is blocked by allowlist</td>
      <td>Confirm the key has <code class="language-plaintext highlighter-rouge">data_objects.object_relationships.delete</code> and that your source IP is on the key allowlist, if configured.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">429</code></td>
      <td>Rate limit exceeded</td>
      <td>Retry after <code class="language-plaintext highlighter-rouge">X-RateLimit-Reset</code> and reduce request frequency.</td>
    </tr>
  </tbody>
</table>
</div>
