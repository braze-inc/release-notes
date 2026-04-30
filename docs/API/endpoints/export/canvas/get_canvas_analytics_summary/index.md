<div id='api_opblpmcbtudb' class='api_div'>
<h1 id="export-canvas-data-summary-analytics">Export Canvas data summary analytics</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/canvas/data_summary</p>
</div>

<blockquote>
  <p>Use this endpoint to export rollups of time series data for a Canvas, providing a concise summary of Canvas results.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">canvas.data_summary</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">canvas_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">Canvas API identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ending_at</code></td>
      <td>Required</td>
      <td>Datetime <br />(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> string)</td>
      <td>End date for the data export. Defaults to the time of the request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">starting_at</code></td>
      <td>Optional*</td>
      <td>Datetime <br />(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> string)</td>
      <td>Start date for the data export. <br /><br />* Either <code class="language-plaintext highlighter-rouge">length</code> or <code class="language-plaintext highlighter-rouge">starting_at</code> is required.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">length</code></td>
      <td>Optional*</td>
      <td>String</td>
      <td>Maximum number of days before <code class="language-plaintext highlighter-rouge">ending_at</code> included in the returned series. Must be between 1 and 14 (inclusive). <br /><br />* Either <code class="language-plaintext highlighter-rouge">length</code> or <code class="language-plaintext highlighter-rouge">starting_at</code> is required.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_variant_breakdown</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Whether to include variant statistics (defaults to <code class="language-plaintext highlighter-rouge">false</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_step_breakdown</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Whether to include step statistics (defaults to <code class="language-plaintext highlighter-rouge">false</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_deleted_step_data</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Whether to include step statistics for deleted steps (defaults to <code class="language-plaintext highlighter-rouge">false</code>).</td>
    </tr>
  </tbody>
</table>

<p><strong>Important:</strong></p>

<p><strong>Time zone alignment:</strong> Braze Dashboard analytics are aggregated daily in your company’s configured time zone in the dashboard. Make sure your timestamps align with your company’s time zone so that your stats match the dashboard. For example, if your company time is UTC+2, then the timestamp should be 12AM UTC+2.</p>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&amp;ending_at=2018-05-30T23:59:59-05:00&amp;starting_at=2018-05-28T23:59:59-05:00&amp;length=5&amp;include_variant_breakdown=true&amp;include_step_breakdown=true&amp;include_deleted_step_data=true' \
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
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
    </span><span class="nl">"total_stats"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
      </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
      </span><span class="nl">"conversions_by_entry_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">entry</span><span class="w"> </span><span class="err">time</span><span class="p">,</span><span class="w">
      </span><span class="nl">"entries"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">entries</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"variant_stats"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional)</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"00000000-0000-0000-0000-0000000000000"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variant</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
        </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
        </span><span class="nl">"entries"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">entries</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">variants)</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"step_stats"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional)</span><span class="w"> </span><span class="p">{</span><span class="w">
      </span><span class="nl">"00000000-0000-0000-0000-0000000000000"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">step</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">step</span><span class="p">,</span><span class="w">
        </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions_by_entry_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">entry</span><span class="w"> </span><span class="err">time</span><span class="p">,</span><span class="w">
        </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"android_push"</span><span class="p">:</span><span class="w"> </span><span class="err">(name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">channel)</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
              </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
              </span><span class="nl">"opens"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
              </span><span class="nl">"influenced_opens"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">total</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">opens</span><span class="w"> </span><span class="err">(includes</span><span class="w"> </span><span class="err">both</span><span class="w"> </span><span class="err">direct</span><span class="w"> </span><span class="err">opens</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">influenced</span><span class="w"> </span><span class="err">opens)</span><span class="p">,</span><span class="w">
              </span><span class="nl">"bounces"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">bounces</span><span class="w">
              </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">stats</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">channel)</span><span class="w">
            </span><span class="p">}</span><span class="w">
          </span><span class="p">],</span><span class="w">
          </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">channels)</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">steps)</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">successful</span><span class="w"> </span><span class="err">completion</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Important:</strong></p>

<p><strong><code class="language-plaintext highlighter-rouge">influenced_opens</code> field:</strong> In the API response, the <code class="language-plaintext highlighter-rouge">influenced_opens</code> field represents the total number of opens (both direct and influenced opens combined). In the Braze dashboard, ‘influenced opens’ refers only to influenced opens, excluding direct opens. This is due to a legacy naming convention in the API.</p>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
