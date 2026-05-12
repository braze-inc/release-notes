<div id='api_jvlhypcmklkt' class='api_div'>
<h1 id="export-custom-events-analytics">Export custom events analytics</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/events/data_series</p>
</div>

<blockquote>
  <p>Use this endpoint to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">events.data_series</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">event</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The name of the custom event for which to return analytics.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">length</code></td>
      <td>Required</td>
      <td>Integer</td>
      <td>Maximum number of units (days or hours) before <code class="language-plaintext highlighter-rouge">ending_at</code> to include in the returned series. Must be between 1 and 100 (inclusive).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">unit</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Unit of time between data points. Can be <code class="language-plaintext highlighter-rouge">day</code> or <code class="language-plaintext highlighter-rouge">hour</code>, defaults to <code class="language-plaintext highlighter-rouge">day</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ending_at</code></td>
      <td>Optional</td>
      <td>Datetime <br />(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> string)</td>
      <td>Date on which the data series should end. Defaults to time of the request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">app_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>App API identifier retrieved from the <a href="/docs/user_guide/administer/global/workspace_settings/apis_and_identifiers/">API Keys</a> page to limit analytics to a specific app.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">segment_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">Segment API identifier</a>. Segment ID indicating the analytics-enabled segment for which event analytics should be returned.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&amp;length=24&amp;unit=hour&amp;ending_at=2014-12-10T23:59:59-05:00&amp;app_id={{app_identifier}}&amp;segment_id={{segment_identifier}}' \
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
            </span><span class="nl">"time"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">point</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">-</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">extended</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">unit</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="s2">"hour"</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">unit</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="s2">"day"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"count"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">occurrences</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">provided</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">event</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="err">...</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="fatal-export">Fatal error response codes</h3>

<p>For status codes and associated error messages that will be returned if your request encounters a fatal error, reference <a href="/docs/api/errors/#fatal-errors">Fatal errors &amp; responses</a>.</p>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
