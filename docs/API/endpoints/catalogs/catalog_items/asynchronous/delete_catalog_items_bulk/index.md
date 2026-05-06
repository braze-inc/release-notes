<div id='api_vnamqnxmvmgo' class='api_div'>
<h1 id="delete-multiple-catalog-items">Delete multiple catalog items</h1>
<div class="api_type"><div class="method delete ">delete</div>
<p>/catalogs/{catalog_name}/items</p>
</div>

<blockquote>
  <p>Use this endpoint to delete multiple items in your catalog.</p>
</blockquote>

<p>Each request can support up to 50 items. This endpoint is asynchronous.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">catalogs.delete_items</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">items</code></td>
      <td>Required</td>
      <td>Array</td>
      <td>An array that contains item objects. The item objects should contain an <code class="language-plaintext highlighter-rouge">id</code> referencing the items Braze should delete. Up to 50 item objects are allowed per request.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

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
</pre></td><td class="rouge-code"><pre>curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"items-missing-ids"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"There are 1 item(s) that do not have ids"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"parameters"</span><span class="p">:</span><span class="w"> </span><span class="p">[],</span><span class="w">
      </span><span class="nl">"parameter_values"</span><span class="p">:</span><span class="w"> </span><span class="p">[]</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">ids-too-large</code></td>
      <td>Item IDs can’t be more than 250 characters.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ids-not-unique</code></td>
      <td>Check that the item IDs are unique in the request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ids-not-strings</code></td>
      <td>Item IDs must be of type string.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items-missing-ids</code></td>
      <td>Some items don’t have item IDs. Check that each item has an item ID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-ids</code></td>
      <td>Item IDs can only include letters, numbers, hyphens, and underscores.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">request-includes-too-many-items</code></td>
      <td>Your request has too many items. The item limit per request is 50.</td>
    </tr>
  </tbody>
</table>

</div>
