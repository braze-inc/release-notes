<div id='api_ldtgxcdjsxhr' class='api_div'>
<h1 id="delete-catalog">Delete catalog</h1>
<div class="api_type"><div class="method delete ">delete</div>
<p>/catalogs/{catalog_name}</p>
</div>

<blockquote>
  <p>Use this endpoint to delete a catalog.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">catalogs.delete</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Path parameters">
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

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>There are two status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">200</code> and <code class="language-plaintext highlighter-rouge">404</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response body:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="example-error-response">Example error response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">404</code> could return the following response body. Refer to <a href="#troubleshooting">Troubleshooting</a> for more information about errors you may encounter.</p>

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

<table class="reset-td-br-1 reset-td-br-2" aria-label="Troubleshooting">
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
  </tbody>
</table>

</div>
