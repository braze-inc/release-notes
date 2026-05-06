<div id='api_qvkcassfpntp' class='api_div'>
<h1 id="replace-catalog-items">Replace catalog items</h1>
<div class="api_type"><div class="method put ">put</div>
<p>/catalogs/{catalog_name}/items</p>
</div>

<blockquote>
  <p>Use this endpoint to replace multiple items in your catalog.</p>
</blockquote>

<p>If a catalog item doesn’t exist, this endpoint will create the item in your catalog. Each request can support up to 50 catalog items. This endpoint is asynchronous.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">catalogs.replace_items</code> permission.</p>

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
      <td>An array that contains item objects. Each object must have an ID. The item objects should contain fields that exist in the catalog. Up to 50 item objects are allowed per request.</td>
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
26
27
28
29
30
</pre></td><td class="rouge-code"><pre>curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
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
12
13
14
15
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"invalid-fields"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Some of the fields given do not exist in the catalog"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"parameters"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"id"</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"parameter_values"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"restaurant1"</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">ids-not-string</code></td>
      <td>Confirm that each item ID is a string.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ids-not-unique</code></td>
      <td>Check that each item ID is unique.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ids-too-large</code></td>
      <td>Character limit for each item ID is 250 characters.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">item-array-invalid</code></td>
      <td><code class="language-plaintext highlighter-rouge">items</code> must be an array of objects.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items-missing-ids</code></td>
      <td>Some items don’t have item IDs. Confirm that each item has an ID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">items-too-large</code></td>
      <td>Item values can’t exceed 5,000 characters.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-ids</code></td>
      <td>Supported characters for item ID names are letters, numbers, hyphens, and underscores.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-fields</code></td>
      <td>Confirm that all fields you are sending in the API request already exist in the catalog. This is not related to the ID field mentioned in the error.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-keys-in-value-object</code></td>
      <td>Item object keys can’t include <code class="language-plaintext highlighter-rouge">.</code> or <code class="language-plaintext highlighter-rouge">$</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">too-deep-nesting-in-value-object</code></td>
      <td>Item objects can’t have more than 50 levels of nesting.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">request-includes-too-many-items</code></td>
      <td>Your request has too many items. The item limit per request is 50.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">unable-to-coerce-value</code></td>
      <td>Item types can’t be converted.</td>
    </tr>
  </tbody>
</table>

</div>
