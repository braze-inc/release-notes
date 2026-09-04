<div id='api_qpituzerfpde' class='api_div' data-search-keywords='list data object types search_term limit offset items type_name metadata display_name_source total_count has_more next_offset'>
<h1 id="list-data-object-types">List data object types</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/data_objects/types</p>
</div>

<blockquote>
  <p>Use this endpoint to list data object types in a workspace.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on <strong>Settings</strong> &gt; <strong>API Keys</strong>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.read</code>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.</p>

<h2 id="query-parameters">Query parameters</h2>

<p>The following table lists and describes the query parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/types</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="List data object types query parameters">
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
      <td><code class="language-plaintext highlighter-rouge">search_term</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Case-insensitive prefix filter on type name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">limit</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>Page size. Default <code class="language-plaintext highlighter-rouge">100</code>. Clamped to <code class="language-plaintext highlighter-rouge">1</code> through <code class="language-plaintext highlighter-rouge">250</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">offset</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>Offset. Default <code class="language-plaintext highlighter-rouge">0</code>. Negative values are floored to <code class="language-plaintext highlighter-rouge">0</code></td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<p>This section includes a sample query-parameter payload and a sample cURL request.</p>

<h3 id="sample-request-payload">Sample request payload</h3>

<p>Use this JSON object as a reference for the query parameters in this request.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"search_term"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acc"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"limit"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w">
  </span><span class="nl">"offset"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example lists the data object types matching the search term <code class="language-plaintext highlighter-rouge">acc</code>, returning two results per page.</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> GET <span class="s1">'https://rest.iad-01.braze.com/data_objects/types?search_term=acc&amp;limit=2&amp;offset=0'</span> <span class="se">\</span>
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
16
17
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"items"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"display_name_source"</span><span class="p">:</span><span class="w"> </span><span class="s2">"name"</span><span class="w"> </span><span class="p">}</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"contact"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"metadata"</span><span class="p">:</span><span class="w"> </span><span class="p">{}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"total_count"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w">
  </span><span class="nl">"has_more"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
  </span><span class="nl">"next_offset"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span><span class="w">
  </span><span class="nl">"offset"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">
  </span><span class="nl">"limit"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">metadata.display_name_source</code> is present when a display-name field is configured for the type.</p>

<h3 id="response-parameters">Response parameters</h3>

<p>The following table lists and describes the fields in a successful response.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="List data object types response parameters">
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
      <td><code class="language-plaintext highlighter-rouge">items</code></td>
      <td>Required</td>
      <td>Array</td>
      <td>List of data object type records</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Data object type machine name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].metadata</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Type metadata object</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">total_count</code></td>
      <td>Required</td>
      <td>Integer</td>
      <td>Total number of matching records</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">has_more</code></td>
      <td>Required</td>
      <td>Boolean</td>
      <td>Whether another page of results is available</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">next_offset</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>Offset for the next page when <code class="language-plaintext highlighter-rouge">has_more</code> is <code class="language-plaintext highlighter-rouge">true</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">offset</code></td>
      <td>Required</td>
      <td>Integer</td>
      <td>Current page offset</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">limit</code></td>
      <td>Required</td>
      <td>Integer</td>
      <td>Page size used by the request</td>
    </tr>
  </tbody>
</table>

<h2 id="errors">Errors</h2>

<p>The following table lists common errors for this endpoint and how to resolve them.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="List data object types errors">
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
      <td>Invalid query parameter type or value</td>
      <td>Ensure <code class="language-plaintext highlighter-rouge">limit</code> and <code class="language-plaintext highlighter-rouge">offset</code> are integers and that all parameter values are valid.</td>
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
