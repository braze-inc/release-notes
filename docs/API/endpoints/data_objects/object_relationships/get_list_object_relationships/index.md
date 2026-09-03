<div id='api_yqhzcqszgerh' class='api_div' data-search-keywords='list object relationships type_name external_id anchor rel_kind limit offset items to_data_object attributes name total_count has_more next_offset'>
<h1 id="list-object-relationships">List object relationships</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/data_objects/objects/{type_name}/{external_id}/object_relationships</p>
</div>

<blockquote>
  <p>Use this endpoint to list related data objects from one object anchor.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is currently in early access. Your workspace must be enabled before the Data Objects API key permissions appear on <strong>Settings</strong> &gt; <strong>API Keys</strong>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.read</code>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects read bucket with a default limit of 50 requests per minute.</p>

<h2 id="path-parameters">Path parameters</h2>

<p>The following table lists and describes the path parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}/{external_id}/object_relationships</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="List object relationships path parameters">
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
      <td>Source object type</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Source object identifier</td>
    </tr>
  </tbody>
</table>

<h2 id="query-parameters">Query parameters</h2>

<p>The following table lists and describes the query parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/objects/{type_name}/{external_id}/object_relationships</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="List object relationships query parameters">
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
      <td><code class="language-plaintext highlighter-rouge">rel_kind</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Filter by one relationship kind</td>
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
7
8
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acct-123"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"source"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"subaccount"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"limit"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span><span class="p">,</span><span class="w">
  </span><span class="nl">"offset"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example lists the <code class="language-plaintext highlighter-rouge">subaccount</code> records that <code class="language-plaintext highlighter-rouge">acct-123</code> links out to, returning the first page of results.</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> GET <span class="s1">'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&amp;rel_kind=subaccount&amp;limit=100&amp;offset=0'</span> <span class="se">\</span>
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
18
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"items"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"subaccount"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"to_data_object"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acct-456"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Child Account"</span><span class="w"> </span><span class="p">}</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="p">{}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"total_count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w">
  </span><span class="nl">"has_more"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
  </span><span class="nl">"next_offset"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span><span class="w">
  </span><span class="nl">"offset"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">
  </span><span class="nl">"limit"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>With <code class="language-plaintext highlighter-rouge">anchor=target</code>, related objects are returned as <code class="language-plaintext highlighter-rouge">from_data_object</code>.</p>

<h3 id="response-parameters">Response parameters</h3>

<p>The following table lists and describes the fields in a successful response.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="List object relationships response parameters">
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
      <td>List of object relationship records</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].rel_kind</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Relationship kind value</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].to_data_object</code></td>
      <td>Conditional</td>
      <td>Object</td>
      <td>Related object when <code class="language-plaintext highlighter-rouge">anchor=source</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].from_data_object</code></td>
      <td>Conditional</td>
      <td>Object</td>
      <td>Related object when <code class="language-plaintext highlighter-rouge">anchor=target</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].to_data_object.type_name</code></td>
      <td>Conditional</td>
      <td>String</td>
      <td>Related object type name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].to_data_object.external_id</code></td>
      <td>Conditional</td>
      <td>String</td>
      <td>Related object external ID</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].to_data_object.attributes</code></td>
      <td>Conditional</td>
      <td>Object</td>
      <td>Related object attributes</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].from_data_object.type_name</code></td>
      <td>Conditional</td>
      <td>String</td>
      <td>Related object type name</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].from_data_object.external_id</code></td>
      <td>Conditional</td>
      <td>String</td>
      <td>Related object external ID</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].from_data_object.attributes</code></td>
      <td>Conditional</td>
      <td>Object</td>
      <td>Related object attributes</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items[].attributes</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Relationship attributes</td>
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

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="List object relationships errors">
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
      <td>Type or object not found</td>
      <td>Confirm <code class="language-plaintext highlighter-rouge">type_name</code> and <code class="language-plaintext highlighter-rouge">external_id</code> both exist in the workspace.</td>
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
