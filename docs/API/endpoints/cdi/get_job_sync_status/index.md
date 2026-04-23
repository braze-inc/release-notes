<div id='api_vdfhszzdwbqr' class='api_div'>
<h1 id="list-job-sync-status">List job sync status</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/cdi/integrations/{integration_id}/job_sync_status</p>
</div>

<blockquote>
  <p>Use this endpoint to return a list of past sync statuses for a given integration.</p>
</blockquote>

<p><strong>Note:</strong></p>

<p>To use this endpoint, you’ll need to generate an API key with the <code class="language-plaintext highlighter-rouge">cdi.integration_job_status</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">integration_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Integration ID.</td>
    </tr>
  </tbody>
</table>

<h2 id="query-parameters">Query parameters</h2>

<p>Each call to this endpoint will return 10 items. For an integration with more than 10 syncs, use the <code class="language-plaintext highlighter-rouge">Link</code> header to retrieve the data on the next page as shown in the following example response.</p>

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
      <td>Determines the pagination of the sync status.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<h3 id="without-cursor">Without cursor</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="with-cursor">With cursor</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response body.</p>

<p><strong>Note:</strong></p>

<p>The <code class="language-plaintext highlighter-rouge">Link</code> header won’t exist if there are less than or equal to 10 syncs in total. For calls without a cursor, <code class="language-plaintext highlighter-rouge">prev</code> will not show. When looking at the last page of items, <code class="language-plaintext highlighter-rouge">next</code> will not show.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre>Link: &lt;/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow&gt;; rel="prev",&lt;/cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=&gt;; rel="next"
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
        </span><span class="nl">"job_status"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">sync</span><span class="p">,</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">below</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">explanation</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">different</span><span class="w"> </span><span class="err">statuses</span><span class="p">,</span><span class="w">
        </span><span class="nl">"sync_start_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">sync</span><span class="w"> </span><span class="err">started</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
        </span><span class="nl">"sync_finish_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">sync</span><span class="w"> </span><span class="err">finished</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_timestamp_synced"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">UPDATED_AT</span><span class="w"> </span><span class="err">timestamp</span><span class="w"> </span><span class="err">processed</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">sync</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
        </span><span class="nl">"rows_synced"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">rows</span><span class="w"> </span><span class="err">successfully</span><span class="w"> </span><span class="err">synced</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">Braze</span><span class="p">,</span><span class="w">
        </span><span class="nl">"rows_failed_with_errors"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">rows</span><span class="w"> </span><span class="err">failed</span><span class="w"> </span><span class="err">because</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">errors</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>job_status</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">running</code></td>
      <td>The job is currently running.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">success</code></td>
      <td>All rows synced successfully.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">partial</code></td>
      <td>Some rows failed to sync due to errors.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">error</code></td>
      <td>No rows were synced.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">config_error</code></td>
      <td>There was an error in integration configuration. Check your integration setup.</td>
    </tr>
  </tbody>
</table>

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
    <tr>
      <td><code class="language-plaintext highlighter-rouge">400 Invalid integration ID</code></td>
      <td>Check that your <code class="language-plaintext highlighter-rouge">integration_id</code> is valid.</td>
    </tr>
  </tbody>
</table>

<p>For additional status codes and associated error messages, please refer to <a href="/docs/api/errors/#fatal-errors">Fatal errors &amp; responses</a>.</p>

</div>
