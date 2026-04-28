<div id='api_iortrrgfzunq' class='api_div'>
<h1 id="export-custom-events-list">Export custom events list</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/events/list</p>
</div>

<blockquote>
  <p>Use this endpoint to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">events.list</code> permission.</p>

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
      <td>The page of event names to return, defaults to 0 (returns the first set of up to 250).</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"events"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"Event A"</span><span class="p">,</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
        </span><span class="s2">"Event B"</span><span class="p">,</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
        </span><span class="s2">"Event C"</span><span class="p">,</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
        </span><span class="err">...</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="fatal-export">Fatal error response codes</h3>

<p>For status codes and associated error messages that will be returned if your request encounters a fatal error, reference <a href="/docs/api/errors/#fatal-errors">Fatal errors &amp; responses</a>.</p>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
