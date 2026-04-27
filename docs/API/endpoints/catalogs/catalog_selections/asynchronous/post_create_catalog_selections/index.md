<div id='api_xjvmzfjjurrn' class='api_div'>
<h1 id="create-catalog-selection">Create catalog selection</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/catalogs/{catalog_name}/selections</p>
</div>

<blockquote>
  <p>Use this endpoint to create a selection in your catalog.</p>
</blockquote>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">catalogs.create_selection</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

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
      <td><code class="language-plaintext highlighter-rouge">catalog_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Name of the catalog.</td>
    </tr>
  </tbody>
</table>

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
      <td><code class="language-plaintext highlighter-rouge">selection</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>An object that contains selection criteria. See <a href="/docs/api/objects_filters/catalog_selection_object/">catalog selection object</a> for a full breakdown of the object and its fields.</td>
    </tr>
  </tbody>
</table>

<h3 id="selection-object-parameters">Selection object parameters</h3>

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
      <td><code class="language-plaintext highlighter-rouge">name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The name of the catalog selection.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">description</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A description of the catalog selection.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>A unique identifier for the selection.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">source</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The source of the catalog data. For Shopify catalogs, use <code class="language-plaintext highlighter-rouge">"Shopify"</code>. Accepted values are <code class="language-plaintext highlighter-rouge">"Shopify"</code> and <code class="language-plaintext highlighter-rouge">"Braze"</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">filters</code></td>
      <td>Optional</td>
      <td>Array</td>
      <td>An array of filter objects to apply to the catalog items. You can specify up to four filters per request. If no filters are provided, all items from the catalog are included.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">results_limit</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>The maximum number of results to return. Must be a number between 1 and 50.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">sort_field</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The field to sort results by. This must be paired with <code class="language-plaintext highlighter-rouge">sort_order</code>. If both <code class="language-plaintext highlighter-rouge">sort_field</code> and <code class="language-plaintext highlighter-rouge">sort_order</code> are not present, the results are randomized.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">sort_order</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The order to sort results. Accepted values are <code class="language-plaintext highlighter-rouge">"asc"</code> (ascending) or <code class="language-plaintext highlighter-rouge">"desc"</code> (descending). This must be paired with <code class="language-plaintext highlighter-rouge">sort_field</code>. If both <code class="language-plaintext highlighter-rouge">sort_field</code> and <code class="language-plaintext highlighter-rouge">sort_order</code> are not present, the results are randomized.</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>The <code class="language-plaintext highlighter-rouge">sort_field</code> and <code class="language-plaintext highlighter-rouge">sort_order</code> parameters must be used together. If you provide one without the other, or if you omit both parameters, the selection results are returned in a randomized order.</p>

<h2 id="example-request">Example Request</h2>

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
12
13
14
15
16
17
18
19
20
21
22
23
24
25
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="filter-operators">Filter operators</h3>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Field type</th>
      <th>Supported operators</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">string</code></td>
      <td><code class="language-plaintext highlighter-rouge">equals</code>, <code class="language-plaintext highlighter-rouge">does not equal</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">number</code></td>
      <td><code class="language-plaintext highlighter-rouge">equals</code>, <code class="language-plaintext highlighter-rouge">does not equal</code>, <code class="language-plaintext highlighter-rouge">greater than</code>, <code class="language-plaintext highlighter-rouge">less than</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">boolean</code></td>
      <td><code class="language-plaintext highlighter-rouge">is</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">time</code></td>
      <td><code class="language-plaintext highlighter-rouge">before</code>, <code class="language-plaintext highlighter-rouge">after</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">array</code></td>
      <td><code class="language-plaintext highlighter-rouge">includes value</code>, <code class="language-plaintext highlighter-rouge">does not include value</code></td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>The API supports a maximum of four filters per selection request. In the Braze dashboard, you can add up to 10 filters per selection. Filters are applied in the order they appear in the array.</p>

<h2 id="response">Response</h2>

<p>There are three status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">202</code>, <code class="language-plaintext highlighter-rouge">400</code>, and <code class="language-plaintext highlighter-rouge">404</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">202</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="example-error-response">Example error response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">400</code> could return the following response body. Refer to <a href="#troubleshooting">Troubleshooting</a> for more information about errors you may encounter.</p>

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
  </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"catalog-not-found"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Could not find catalog"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"parameters"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"catalog_name"</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"parameter_values"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"restaurants"</span><span class="w">
      </span><span class="p">]</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Invalid Request"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<p>The following table lists possible returned errors and their associated troubleshooting steps.</p>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Error</th>
      <th>Troubleshooting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">catalog-not-found</code></td>
      <td>Check that the catalog name is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">company-size-limit-already-reached</code></td>
      <td>The catalog storage size limit is reached.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">selection-limit-reached</code></td>
      <td>The catalog selections limit is reached.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-selection</code></td>
      <td>Check that the selection is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">too-many-filters</code></td>
      <td>Check if the selection has too many filters.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">selection-name-already-exists</code></td>
      <td>Check if the selection name already exists in the catalog.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">selection-has-invalid-filter</code></td>
      <td>Check if the selection filter is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">selection-invalid-results-limit</code></td>
      <td>Check if the selection results limit is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-sorting</code></td>
      <td>Check if the selection sorting is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-sort-field</code></td>
      <td>Check if the selection sort field is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-sort-order</code></td>
      <td>Check if the selection sort order is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">selection-contains-too-many-arrays</code></td>
      <td>Check if the selection contains more than one field with <code class="language-plaintext highlighter-rouge">array</code> type. Only one is supported.</td>
    </tr>
  </tbody>
</table>

</div>
