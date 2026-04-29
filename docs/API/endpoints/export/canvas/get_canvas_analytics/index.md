<div id='api_wfegppsmyuur' class='api_div'>
<h1 id="export-canvas-data-series-analytics">Export Canvas data series analytics</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/canvas/data_series</p>
</div>

<blockquote>
  <p>Use this endpoint to export time series data for a Canvas.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">canvas.data_series</code> permission.</p>

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
      <td>Date on which the data export should end. Defaults to time of the request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">starting_at</code></td>
      <td>Optional*</td>
      <td>Datetime <br />(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> string)</td>
      <td>Date on which the data export should begin. <br /><br />* Either <code class="language-plaintext highlighter-rouge">length</code> or <code class="language-plaintext highlighter-rouge">starting_at</code> is required.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">length</code></td>
      <td>Optional*</td>
      <td>String</td>
      <td>Maximum number of days before <code class="language-plaintext highlighter-rouge">ending_at</code> to include in the returned series. Must be between 1 and 14 (inclusive). <br /><br />* Either <code class="language-plaintext highlighter-rouge">length</code> or <code class="language-plaintext highlighter-rouge">starting_at</code> is required.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_variant_breakdown</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Whether or not to include variant statistics (defaults to <code class="language-plaintext highlighter-rouge">false</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_step_breakdown</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Whether or not to include step statistics (defaults to <code class="language-plaintext highlighter-rouge">false</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_deleted_step_data</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Whether or not to include step statistics for deleted steps (defaults to <code class="language-plaintext highlighter-rouge">false</code>).</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&amp;ending_at=2018-05-30T23:59:59-5:00&amp;starting_at=2018-05-28T23:59:59-5:00&amp;include_variant_breakdown=true&amp;include_step_breakdown=true&amp;include_deleted_step_data=true' \
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
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
    </span><span class="nl">"stats"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"time"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"total_stats"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
          </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
          </span><span class="nl">"conversions_by_entry_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">entry</span><span class="w"> </span><span class="err">time</span><span class="p">,</span><span class="w">
          </span><span class="nl">"entries"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">entries</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="nl">"variant_stats"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional)</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"00000000-0000-0000-0000-0000000000000"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variant</span><span class="w"> </span><span class="p">{</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
            </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions_by_entry_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">entry</span><span class="w"> </span><span class="err">time</span><span class="p">,</span><span class="w">
            </span><span class="nl">"entries"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">entries</span><span class="w">
          </span><span class="p">},</span><span class="w">
          </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">variants)</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="nl">"step_stats"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional)</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"00000000-0000-0000-0000-0000000000000"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">step</span><span class="w"> </span><span class="p">{</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">step</span><span class="p">,</span><span class="w">
            </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions_by_entry_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">entry</span><span class="w"> </span><span class="err">time</span><span class="p">,</span><span class="w">
            </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
              </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                </span><span class="p">{</span><span class="w">
                  </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"opens"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"unique_opens"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">clicks</span><span class="w">
                  </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">stats)</span><span class="w">
                </span><span class="p">}</span><span class="w">
              </span><span class="p">],</span><span class="w">
              </span><span class="nl">"sms"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                </span><span class="p">{</span><span class="w">
                  </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"sent_to_carrier"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">carrier</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"delivered"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">delivered</span><span class="w"> </span><span class="err">messages</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"rejected"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">rejected</span><span class="w"> </span><span class="err">messages</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"delivery_failed"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">failed</span><span class="w"> </span><span class="err">deliveries</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">clicks</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">shortened</span><span class="w"> </span><span class="err">links</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"opt_out"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">opt</span><span class="w"> </span><span class="err">outs</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"help"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">help</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">received</span><span class="w">
                </span><span class="p">}</span><span class="w">
              </span><span class="p">],</span><span class="w">
              </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">channels)</span><span class="w">
            </span><span class="p">}</span><span class="w">
          </span><span class="p">},</span><span class="w">
          </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">steps)</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">stats</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">time)</span><span class="w">
    </span><span class="p">]</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
