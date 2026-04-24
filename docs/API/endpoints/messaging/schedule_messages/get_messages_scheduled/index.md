<div id='api_ozgcyojvdnbc' class='api_div'>
<h1 id="list-upcoming-scheduled-campaigns-and-canvases">List upcoming scheduled campaigns and Canvases</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/messages/scheduled_broadcasts</p>
</div>

<blockquote>
  <p>Use this endpoint to return a JSON list of information about scheduled campaigns and entry Canvases between now and a designated <code class="language-plaintext highlighter-rouge">end_time</code> specified in the request.</p>
</blockquote>

<p>Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint include campaigns and Canvases created and scheduled in the Braze dashboard.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">messages.schedule_broadcasts</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">end_time</code></td>
      <td>Required</td>
      <td>String in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> format</td>
      <td>End date of the range to retrieve upcoming scheduled campaigns and Canvases. This is treated as midnight in UTC time by the API.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
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
  </span><span class="nl">"scheduled_broadcasts"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">scheduled</span><span class="w"> </span><span class="err">broadcast</span><span class="p">,</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="err">(stings)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
      </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">broadcast</span><span class="w"> </span><span class="err">type</span><span class="w"> </span><span class="err">either</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">Campaign</span><span class="p">,</span><span class="w">
      </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">tag</span><span class="w"> </span><span class="err">names</span><span class="w"> </span><span class="err">formatted</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">strings</span><span class="p">,</span><span class="w">
      </span><span class="nl">"next_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">next</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">formatted</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w"> </span><span class="err">may</span><span class="w"> </span><span class="err">also</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">zone</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">local/intelligent</span><span class="w"> </span><span class="err">delivery</span><span class="p">,</span><span class="w">
      </span><span class="nl">"schedule_type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">schedule</span><span class="w"> </span><span class="err">type</span><span class="p">,</span><span class="w"> </span><span class="err">either</span><span class="w"> </span><span class="err">local_time_zones</span><span class="p">,</span><span class="w"> </span><span class="err">intelligent_delivery</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">company's</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">zone</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
