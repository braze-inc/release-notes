<div id='api_ewgbtsqxioch' class='api_div'>
<h1 id="export-segment-list">Export segment list</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/segments/list</p>
</div>

<blockquote>
  <p>Use this endpoint to export a list of segments, each of which will include its name, Segment API identifier, and whether it has analytics tracking enabled.</p>
</blockquote>

<p>The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">segments.list</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

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
      <td><code class="language-plaintext highlighter-rouge">page</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>The page of segments to return, defaults to 0 (returns the first set of up to 100).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">sort_direction</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>- Sort creation time from newest to oldest: pass in the value <code class="language-plaintext highlighter-rouge">desc</code>.<br /> - Sort creation time from oldest to newest: pass in the value <code class="language-plaintext highlighter-rouge">asc</code>. <br /><br />If <code class="language-plaintext highlighter-rouge">sort_direction</code> is not included, the default order is oldest to newest.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&amp;sort_direction=desc' \
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"segments"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Segment</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
            </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
            </span><span class="nl">"analytics_tracking_enabled"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">analytics</span><span class="w"> </span><span class="err">tracking</span><span class="w"> </span><span class="err">enabled</span><span class="p">,</span><span class="w">
            </span><span class="nl">"tags"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">tag</span><span class="w"> </span><span class="err">names</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">formatted</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">strings</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="err">...</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
