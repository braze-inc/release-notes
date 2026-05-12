<div id='api_onurcnoxnapn' class='api_div'>
<h1 id="export-custom-attributes">Export custom attributes</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/custom_attributes</p>
</div>

<blockquote>
  <p>Use this endpoint to export a list of custom attributes recorded for your app. The attributes are returned in groups of 50, sorted alphabetically.</p>
</blockquote>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">custom_attributes.get</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="query-parameters">Query parameters</h2>

<p>Note that each call to this endpoint will return 50 attributes. For more than 50 attributes, use the <code class="language-plaintext highlighter-rouge">Link</code> header to retrieve the data on the next page as shown in the following example response.</p>

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
      <td>Determines the pagination of the custom attributes.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-requests">Example requests</h2>

<h3 id="without-cursor">Without cursor</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="with-cursor">With cursor</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributes"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"array_length"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span><span class="p">,</span><span class="w"> </span><span class="err">(number)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">maximum</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">length</span><span class="p">,</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="kc">null</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">applicable</span><span class="p">,</span><span class="w">
            </span><span class="nl">"data_type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Number"</span><span class="p">,</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">data</span><span class="w"> </span><span class="err">type</span><span class="p">,</span><span class="w">
            </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="s2">"The attribute description"</span><span class="p">,</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">description</span><span class="p">,</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"The attribute name"</span><span class="p">,</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
            </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Active"</span><span class="p">,</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">status</span><span class="p">,</span><span class="w">
            </span><span class="nl">"tag_names"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"Tag One"</span><span class="p">,</span><span class="w"> </span><span class="s2">"Tag Two"</span><span class="p">]</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">tag</span><span class="w"> </span><span class="err">names</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">formatted</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">strings</span><span class="p">,</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="err">...</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="fatal-export">Fatal error response codes</h3>

<p>For status codes and associated error messages that will be returned if your request encounters a fatal error, reference <a href="/docs/api/errors/#fatal-errors">Fatal errors</a>.</p>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
