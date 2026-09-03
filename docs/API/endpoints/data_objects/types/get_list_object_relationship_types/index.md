<div id='api_ypbndveeceip' class='api_div' data-search-keywords='list object relationship types type_name anchor limit offset items from_type_name to_type_name rel_kind display_name related_type_name total_count has_more next_offset'>
<h1 id="list-object-relationship-types">List object relationship types</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/data_objects/types/{type_name}/object_relationship_types</p>
</div>

<blockquote>
  <p>Use this endpoint to list relationship kinds available for object-to-object links for a given anchor direction.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on <strong>Settings</strong> &gt; <strong>API Keys</strong>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.read</code>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.</p>

<h2 id="path-parameters">Path parameters</h2>

<p>The following table lists and describes the path parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/types/{type_name}/object_relationship_types</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="List object relationship types path parameters">
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

<h2 id="query-parameters">Query parameters</h2>

<p>The following table lists and describes the query parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/types/{type_name}/object_relationship_types</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="List object relationship types query parameters">
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
      <td><code class="language-plaintext highlighter-rouge">anchor</code></td>
      <td>Optional</td>
      <td>String</td>
      <td><code class="language-plaintext highlighter-rouge">source</code> (default) or <code class="language-plaintext highlighter-rouge">target</code></td>
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

<p>This section includes a sample parameter payload and a sample cURL request.</p>

<h3 id="sample-request-payload">Sample request payload</h3>

<p>Use this JSON object as a reference for request parameters.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"source"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"limit"</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span><span class="p">,</span><span class="w">
  </span><span class="nl">"offset"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example lists the object relationship kinds available to the <code class="language-plaintext highlighter-rouge">account</code> type when <code class="language-plaintext highlighter-rouge">account</code> is the source of the relationship.</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> GET <span class="s1">'https://rest.iad-01.braze.com/data_objects/types/account/object_relationship_types?anchor=source&amp;limit=10&amp;offset=0'</span> <span class="se">\</span>
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"items"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"from_type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"to_type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"subaccount"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"display_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"subaccount"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"related_type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"total_count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w">
  </span><span class="nl">"has_more"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
  </span><span class="nl">"next_offset"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span><span class="w">
  </span><span class="nl">"offset"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">
  </span><span class="nl">"limit"</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">related_type_name</code> is the type on the other side of the relationship for the selected <code class="language-plaintext highlighter-rouge">anchor</code>.</p>

<h3 id="response-parameters">Response parameters</h3>

<p>The following table lists and describes the fields in a successful response.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="List object relationship types response parameters">
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
      <td>List of available object relationship types</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].from_type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Source data object type name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].to_type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Target data object type name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].rel_kind</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Relationship kind value</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].display_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Display label for the relationship kind</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].related_type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Opposite-side type for the requested <code class="language-plaintext highlighter-rouge">anchor</code></td>
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

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="List object relationship types errors">
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
      <td>Invalid <code class="language-plaintext highlighter-rouge">anchor</code></td>
      <td>Use <code class="language-plaintext highlighter-rouge">source</code> or <code class="language-plaintext highlighter-rouge">target</code> for <code class="language-plaintext highlighter-rouge">anchor</code>.</td>
    </tr>
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
