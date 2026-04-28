<div id='api_emjpfuypxokh' class='api_div'>
<h1 id="list-multiple-catalog-item-details">List multiple catalog item details</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/catalogs/{catalog_name}/items</p>
</div>

<blockquote>
  <p>Use this endpoint to return multiple catalog items and their content.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">catalogs.get_items</code> permission.</p>

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

<h2 id="query-parameters">Query parameters</h2>

<p>Note that each call to this endpoint will return 50 items. For a catalog with more than 50 items, use the <code class="language-plaintext highlighter-rouge">Link</code> header to retrieve the data on the next page as shown in the following example response.</p>

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
      <td><code class="language-plaintext highlighter-rouge">cursor</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Determines the pagination of the catalog items.</td>
    </tr>
  </tbody>
</table>

<h2 id="request-parameters">Request parameters</h2>

<p>There is no request body for this endpoint.</p>

<h2 id="example-requests">Example requests</h2>

<h3 id="without-cursor">Without cursor</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="with-cursor">With cursor</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>There are three status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">200</code>, <code class="language-plaintext highlighter-rouge">400</code>, and <code class="language-plaintext highlighter-rouge">404</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response header and body.</p>

<p><strong>Note:</strong></p>

<p>The <code class="language-plaintext highlighter-rouge">Link</code> header won’t exist if the catalog has less than or equal to 50 items. For calls without a cursor, <code class="language-plaintext highlighter-rouge">prev</code> will not show. When looking at the last page of items, <code class="language-plaintext highlighter-rouge">next</code> will not show.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>Link: &lt;/catalogs/all_restaurants/items?cursor=c2tpcDow&gt;; rel="prev",&lt;/catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=&gt;; rel="next"
</pre></td></tr></tbody></table></code></pre></div></div>

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
31
32
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"items"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"restaurant1"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Restaurant1"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"City"</span><span class="p">:</span><span class="w"> </span><span class="s2">"New York"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Cuisine"</span><span class="p">:</span><span class="w"> </span><span class="s2">"American"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Rating"</span><span class="p">:</span><span class="w"> </span><span class="mi">5</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Loyalty_Program"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Open_Time"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-11-02T09:03:19.967Z"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"restaurant2"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Restaurant2"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"City"</span><span class="p">:</span><span class="w"> </span><span class="s2">"New York"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Cuisine"</span><span class="p">:</span><span class="w"> </span><span class="s2">"American"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Rating"</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Loyalty_Program"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Open_Time"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-11-02T09:03:19.967Z"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"restaurant3"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Restaurant3"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"City"</span><span class="p">:</span><span class="w"> </span><span class="s2">"New York"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Cuisine"</span><span class="p">:</span><span class="w"> </span><span class="s2">"American"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Rating"</span><span class="p">:</span><span class="w"> </span><span class="mi">5</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Loyalty_Program"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
      </span><span class="nl">"Open_Time"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-11-02T09:03:19.967Z"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
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
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"invalid-cursor"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"'cursor' is not valid"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"parameters"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"cursor"</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"parameter_values"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"bad-cursor"</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">invalid-cursor</code></td>
      <td>Check that your <code class="language-plaintext highlighter-rouge">cursor</code> is valid.</td>
    </tr>
  </tbody>
</table>

</div>
