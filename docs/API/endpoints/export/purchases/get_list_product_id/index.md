<div id='api_vuyeaavkokbe' class='api_div'>
<h1 id="export-product-ids">Export product IDs</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/purchases/product_list</p>
</div>

<blockquote>
  <p>Use this endpoint to return a paginated lists of product IDs.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">purchases.product_list</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-parameters">Request parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Request parameters">
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
      <td><code class="language-plaintext highlighter-rouge">page</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The page of your product list that you want to view.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>https://rest.iad-01.braze.com/purchases/product_list?page=1
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"products"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="s2">"product_name"</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">product</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>

**Tip:**


For help with CSV and API exports, visit [Export troubleshooting](https://www.braze.com/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/).


