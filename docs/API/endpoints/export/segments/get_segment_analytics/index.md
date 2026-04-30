<div id='api_axiuhtudvtmk' class='api_div'>
<h1 id="export-segment-analytics">Export segment analytics</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/segments/data_series</p>
</div>

<blockquote>
  <p>Use this endpoint to retrieve a daily series of the estimated size of a segment over time.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#62d9d142-cdec-4aea-a287-c13efea7415e" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">segments.data_series</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">segment_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">Segment API identifier</a>.<br /><br /> The <code class="language-plaintext highlighter-rouge">segment_id</code> for a given segment can be found on the <a href="/docs/user_guide/administer/global/workspace_settings/apis_and_identifiers/">API Keys</a> page within your Braze account or you can use the <a href="/docs/api/endpoints/export/segments/get_segment/">Export segment list endpoint</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">length</code></td>
      <td>Required</td>
      <td>Integer</td>
      <td>Maximum number of days before <code class="language-plaintext highlighter-rouge">ending_at</code> to include in the returned series. Must be between 1 and 100 (inclusive).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ending_at</code></td>
      <td>Optional</td>
      <td>Datetime <br />(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> string)</td>
      <td>Date on which the data series should end. Defaults to time of the request.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/data_series?segment_id={{segment_identifier}}&amp;length=14&amp;ending_at=2018-06-27T23:59:59-5:00' \
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"data"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"time"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
            </span><span class="nl">"size"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">size</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">date</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="err">...</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
