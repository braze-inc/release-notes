<div id='api_jwmfoqjuhdcx' class='api_div'>
<h1 id="list-integrations">List integrations</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/cdi/integrations</p>
</div>

<blockquote>
  <p>Use this endpoint to return a list of existing integrations.</p>
</blockquote>

<p><strong>Note:</strong></p>

<p>To use this endpoint, you’ll need to generate an API key with the <code class="language-plaintext highlighter-rouge">cdi.integration_list</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="query-parameters">Query parameters</h2>

<p>Each call to this endpoint will return 10 items. For a list with more than 10 integrations, use the <code class="language-plaintext highlighter-rouge">Link</code> header to retrieve the data on the next page as shown in the example response.</p>

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
      <td>Determines the pagination of the integration list.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<h3 id="without-cursor">Without cursor</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="with-cursor">With cursor</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response body.</p>

<p><strong>Note:</strong></p>

<p>The <code class="language-plaintext highlighter-rouge">Link</code> header won’t exist if there are less than or equal to 10 integrations in total. For calls without a cursor, <code class="language-plaintext highlighter-rouge">prev</code> will not show. When looking at the last page of items, <code class="language-plaintext highlighter-rouge">next</code> will not show.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>Link: &lt;/cdi/integrations?cursor=c2tpcDow&gt;; rel="prev",&lt;/cdi/integrations?cursor=c2tpcDoxMDA=&gt;; rel="next"
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"integration_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">integration</span><span class="w"> </span><span class="err">ID</span><span class="p">,</span><span class="w">
      </span><span class="nl">"app_group_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">ID</span><span class="p">,</span><span class="w">
      </span><span class="nl">"integration_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">integration</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
      </span><span class="nl">"integration_type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">integration</span><span class="w"> </span><span class="err">type</span><span class="p">,</span><span class="w">
      </span><span class="nl">"integration_status"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">integration</span><span class="w"> </span><span class="err">status</span><span class="p">,</span><span class="w">
      </span><span class="nl">"contact_emails"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">contact</span><span class="w"> </span><span class="err">email(s)</span><span class="p">,</span><span class="w">
      </span><span class="nl">"last_updated_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">timestamp</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">synced</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
      </span><span class="nl">"warehouse_type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">data</span><span class="w"> </span><span class="err">warehouse</span><span class="w"> </span><span class="err">type</span><span class="p">,</span><span class="w">
      </span><span class="nl">"last_job_start_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">timestamp</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">sync</span><span class="w"> </span><span class="err">run</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
      </span><span class="nl">"last_job_status"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">sync</span><span class="w"> </span><span class="err">run</span><span class="p">,</span><span class="w">
      </span><span class="nl">"next_scheduled_run"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">timestamp</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">next</span><span class="w"> </span><span class="err">scheduled</span><span class="w"> </span><span class="err">sync</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">400 Invalid cursor</code></td>
      <td>Check that your <code class="language-plaintext highlighter-rouge">cursor</code> is valid.</td>
    </tr>
  </tbody>
</table>

<p>For additional status codes and associated error messages, refer to <a href="/docs/api/errors/#fatal-errors">Fatal errors &amp; responses</a>.</p>

</div>
