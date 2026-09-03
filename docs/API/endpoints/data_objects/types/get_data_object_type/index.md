<div id='api_jxabzllwyhjq' class='api_div' data-search-keywords='get data object type type_name data_object_type metadata display_name_source schema_def type properties name title industry renewal_date format required'>
<h1 id="get-data-object-type">Get data object type</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/data_objects/types/{type_name}</p>
</div>

<blockquote>
  <p>Use this endpoint to return one data object type and its schema definition.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on <strong>Settings</strong> &gt; <strong>API Keys</strong>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.read</code>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.</p>

<h2 id="path-parameters">Path parameters</h2>

<p>The following table lists and describes the path parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/types/{type_name}</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Get data object type path parameters">
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

<h2 id="example-request">Example request</h2>

<p>This section includes a sample path-parameter payload and a sample cURL request.</p>

<h3 id="sample-request-payload">Sample request payload</h3>

<p>Use this JSON object as a reference for the path parameter in this request.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example retrieves the definition of the <code class="language-plaintext highlighter-rouge">account</code> data object type.</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> GET <span class="s1">'https://rest.iad-01.braze.com/data_objects/types/account'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>This section includes a sample successful response and the response fields.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response body.</p>

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
13
14
15
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"data_object_type"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"display_name_source"</span><span class="p">:</span><span class="w"> </span><span class="s2">"name"</span><span class="w"> </span><span class="p">},</span><span class="w">
    </span><span class="nl">"schema_def"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"object"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="nl">"title"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Name"</span><span class="w"> </span><span class="p">},</span><span class="w">
        </span><span class="nl">"industry"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="nl">"title"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Industry"</span><span class="w"> </span><span class="p">},</span><span class="w">
        </span><span class="nl">"renewal_date"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="nl">"format"</span><span class="p">:</span><span class="w"> </span><span class="s2">"date-time"</span><span class="p">,</span><span class="w"> </span><span class="nl">"title"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Renewal date"</span><span class="w"> </span><span class="p">}</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="nl">"required"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"name"</span><span class="p">]</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">schema_def</code> describes allowed object fields. Writes still reject undeclared fields even though this response schema is descriptive.</p>

<h3 id="response-parameters">Response parameters</h3>

<p>The following table lists and describes the fields in a successful response.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Get data object type response parameters">
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
      <td><code class="language-plaintext highlighter-rouge">data_object_type</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Returned data object type record</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data_object_type.type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Data object type machine name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data_object_type.metadata</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Type metadata object</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data_object_type.schema_def</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>JSON schema definition for object attributes</td>
    </tr>
  </tbody>
</table>

<h2 id="errors">Errors</h2>

<p>The following table lists common errors for this endpoint and how to resolve them.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Get data object type errors">
  <thead>
    <tr>
      <th>Status</th>
      <th>Cause</th>
      <th>Guidance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">404</code></td>
      <td>Type not found (<code class="language-plaintext highlighter-rouge">data-object-type-not-found</code>)</td>
      <td>Confirm <code class="language-plaintext highlighter-rouge">type_name</code> exists in the workspace and matches the machine name exactly.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">401</code></td>
      <td>Missing or invalid REST API key</td>
      <td>Verify the <code class="language-plaintext highlighter-rouge">Authorization</code> header uses <code class="language-plaintext highlighter-rouge">Bearer YOUR_REST_API_KEY</code> and that the key is active.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">403</code></td>
      <td>API key lacks permission or request is blocked by allowlist</td>
      <td>Confirm the key has <code class="language-plaintext highlighter-rouge">data_objects.read</code> and that your source IP is on the key allowlist, if configured.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">429</code></td>
      <td>Rate limit exceeded</td>
      <td>Retry after <code class="language-plaintext highlighter-rouge">X-RateLimit-Reset</code> and reduce request frequency.</td>
    </tr>
  </tbody>
</table>
</div>
