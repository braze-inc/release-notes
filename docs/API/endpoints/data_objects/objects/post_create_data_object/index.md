<div id='api_ocumxctzuaif' class='api_div' data-search-keywords='create data object external_id attributes name industry data_object type_name'>
<h1 id="create-data-object">Create data object</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/data_objects/objects/{type_name}</p>
</div>

<blockquote>
  <p>Use this endpoint to create one data object for a type.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on <strong>Settings</strong> &gt; <strong>API Keys</strong>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.create</code>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects write bucket with a default limit of 50 requests per minute.</p>

<h2 id="path-parameters">Path parameters</h2>

<p>The following table lists and describes the path parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Create data object path parameters">
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
      <td>Data object type machine name</td>
    </tr>
  </tbody>
</table>

<h2 id="request-parameters">Request parameters</h2>

<p>The following table lists and describes the JSON request body parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Create data object request parameters">
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
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Object identifier, unique within the type</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">attributes</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Field-name keyed values validated against the type schema</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">display_name</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Display label for the object. When the type has a display-name source field, the value of that field takes precedence. Defaults to <code class="language-plaintext highlighter-rouge">external_id</code></td>
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
  </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acct-new"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"New Account"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"industry"</span><span class="p">:</span><span class="w"> </span><span class="s2">"software"</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example creates an <code class="language-plaintext highlighter-rouge">account</code> record with the identifier <code class="language-plaintext highlighter-rouge">acct-new</code> and sets its <code class="language-plaintext highlighter-rouge">name</code> and <code class="language-plaintext highlighter-rouge">industry</code> attributes.</p>

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
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/data_objects/objects/account'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"data_object"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acct-new"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"New Account"</span><span class="p">,</span><span class="w"> </span><span class="nl">"industry"</span><span class="p">:</span><span class="w"> </span><span class="s2">"software"</span><span class="w"> </span><span class="p">}</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="response-parameters">Response parameters</h3>

<p>The following table lists and describes the fields in a successful response.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Create data object response parameters">
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
      <td><code class="language-plaintext highlighter-rouge">data_object</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Created data object record</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data_object.type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Data object type machine name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data_object.external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Data object identifier</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data_object.attributes</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Stored object attributes keyed by field name</td>
    </tr>
  </tbody>
</table>

<h2 id="errors">Errors</h2>

<p>The following table lists common errors for this endpoint and how to resolve them.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Create data object errors">
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
      <td>Unknown attribute field or invalid attribute type</td>
      <td>Confirm every field in <code class="language-plaintext highlighter-rouge">attributes</code> exists in the type schema and uses the correct data type.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">404</code></td>
      <td>Type not found (<code class="language-plaintext highlighter-rouge">data-object-type-not-found</code>)</td>
      <td>Confirm <code class="language-plaintext highlighter-rouge">type_name</code> exists in the workspace and matches the machine name exactly.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">409</code></td>
      <td>Duplicate object (<code class="language-plaintext highlighter-rouge">duplicate-data-object</code>)</td>
      <td>Use a different <code class="language-plaintext highlighter-rouge">external_id</code>, or use <code class="language-plaintext highlighter-rouge">PUT</code> to replace the existing object.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">422</code></td>
      <td>Record limit reached (<code class="language-plaintext highlighter-rouge">data-object-record-limit-exceeded</code>)</td>
      <td>Reduce object count for the type, or contact Braze support about your workspace limits.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">401</code></td>
      <td>Missing or invalid REST API key</td>
      <td>Verify the <code class="language-plaintext highlighter-rouge">Authorization</code> header uses <code class="language-plaintext highlighter-rouge">Bearer YOUR_REST_API_KEY</code> and that the key is active.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">403</code></td>
      <td>API key lacks permission or request is blocked by allowlist</td>
      <td>Confirm the key has <code class="language-plaintext highlighter-rouge">data_objects.create</code> and that your source IP is on the key allowlist, if configured.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">429</code></td>
      <td>Rate limit exceeded</td>
      <td>Retry after <code class="language-plaintext highlighter-rouge">X-RateLimit-Reset</code> and reduce request frequency.</td>
    </tr>
  </tbody>
</table>
</div>
