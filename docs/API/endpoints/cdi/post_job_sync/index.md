<div id='api_loxxizcebdqc' class='api_div'>
<h1 id="trigger-a-sync">Trigger a sync</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/cdi/integrations/{integration_id}/sync</p>
</div>

<blockquote>
  <p>Use this endpoint to trigger a sync for a given integration.</p>
</blockquote>

<p><strong>Note:</strong></p>

<p>To use this endpoint, you must generate an API key with the <code class="language-plaintext highlighter-rouge">cdi.integration_sync</code> permission.</p>

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
      <td>Integration ID. This is found in the URL when viewing an integration in the Braze dashboard. The URL format is <code class="language-plaintext highlighter-rouge">https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]</code>.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">202</code> could return the following response body:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">400 Invalid integration ID</code></td>
      <td>Check that your <code class="language-plaintext highlighter-rouge">integration_id</code> is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">404 Integration not found</code></td>
      <td>No integration exists for the given integration ID. Make sure that your integration ID is valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">429 Another job is in progress</code></td>
      <td>There is a sync currently running for this integration. Try again after the sync has completed.</td>
    </tr>
  </tbody>
</table>

<p>For additional status codes and associated error messages, refer to <a href="/docs/api/errors/#fatal-errors">Fatal errors &amp; responses</a>.</p>

</div>