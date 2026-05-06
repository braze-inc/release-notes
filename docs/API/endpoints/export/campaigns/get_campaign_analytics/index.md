<div id='api_zhypwlsifidd' class='api_div'>
<h1 id="export-campaign-analytics">Export campaign analytics</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/campaigns/data_series</p>
</div>

<blockquote>
  <p>Use this endpoint to retrieve a daily series of various stats for a campaign over time.</p>
</blockquote>

<p>Data returned includes how many messages were sent, opened, clicked, or converted by messaging channel.</p>

<p><strong>Note:</strong></p>

<p>Counts from this endpoint won’t always exactly match  or aggregates you build from <a href="/docs/user_guide/data/distribution/braze_currents/">Currents</a>. Dashboard metrics and API time series use different aggregation windows and definitions than raw Currents events.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">campaigns.data_series</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">campaign_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">campaign API identifier</a>.<br /><br /> The <code class="language-plaintext highlighter-rouge">campaign_id</code> for API campaigns can be found on the <a href="/docs/user_guide/administer/global/workspace_settings/apis_and_identifiers/">API Keys</a> page and the <strong>Campaign Details</strong> page within your dashboard, or you can use the <a href="/docs/api/endpoints/export/campaigns/get_campaigns/">List campaigns endpoint</a>.</td>
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
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&amp;length=7&amp;ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="responses">Responses</h2>

<h3 id="multichannel-response">Multichannel response</h3>

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
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"data"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"time"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions1_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions2_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions3_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions1"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions2"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions3"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"unique_recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">float)</span><span class="w">
            </span><span class="nl">"messages"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="nl">"ios_push"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                      </span><span class="nl">"variation_api_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"sent"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"direct_opens"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">direct</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"total_opens"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">total</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"bounces"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">bounces</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"body_clicks"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">clicks</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">],</span><span class="w">
                </span><span class="nl">"android_push"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                      </span><span class="nl">"variation_api_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"sent"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"direct_opens"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">direct</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"total_opens"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">total</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"bounces"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">bounces</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"body_clicks"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">clicks</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">],</span><span class="w">
                </span><span class="nl">"webhook"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                      </span><span class="nl">"variation_api_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">errors</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">],</span><span class="w">
                </span><span class="nl">"email"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                      </span><span class="nl">"variation_api_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"opens"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"unique_opens"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"unique_clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"unsubscribes"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unsubscribes</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"bounces"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">bounces</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"delivered"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">delivered</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"reported_spam"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">reported</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">spam</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">],</span><span class="w">
                </span><span class="nl">"sms"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                      </span><span class="nl">"variation_api_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"sent_to_carrier"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">carrier</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"delivered"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">delivered</span><span class="w"> </span><span class="err">messages</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"rejected"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">rejected</span><span class="w"> </span><span class="err">messages</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"delivery_failed"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">failed</span><span class="w"> </span><span class="err">deliveries</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">clicks</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">shortened</span><span class="w"> </span><span class="err">links</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"opt_out"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">opt</span><span class="w"> </span><span class="err">outs</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"help"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">help</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">received</span><span class="w">
                  </span><span class="p">}</span><span class="w">
                </span><span class="p">],</span><span class="w">
                </span><span class="nl">"whats_app"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                      </span><span class="nl">"variation_api_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"delivered"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">delivered</span><span class="w"> </span><span class="err">messages</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"failed"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">failed</span><span class="w"> </span><span class="err">deliveries</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"read"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">opened</span><span class="w"> </span><span class="err">messages</span><span class="w">
                    </span><span class="p">},</span><span class="w">
                </span><span class="p">],</span><span class="w">
                </span><span class="nl">"content_cards"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                  </span><span class="p">{</span><span class="w">
                    </span><span class="nl">"variation_api_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"total_clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">total</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"total_dismissals"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">total</span><span class="w"> </span><span class="err">dismissals</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"total_impressions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">total</span><span class="w"> </span><span class="err">impressions</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"unique_clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"unique_dismissals"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">dismissals</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"unique_impressions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">impressions</span><span class="w">
                  </span><span class="p">}</span><span class="w">
                </span><span class="p">],</span><span class="w">
                </span><span class="err">...</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">}</span><span class="w">
    </span><span class="p">],</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="multivariate-response">Multivariate response</h3>

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
62
63
64
65
66
67
68
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"data"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"time"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
            </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"conversions_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
            </span><span class="nl">"messages"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
               </span><span class="nl">"trigger_in_app_message"</span><span class="p">:</span><span class="w"> </span><span class="p">[{</span><span class="w">
                    </span><span class="nl">"variation_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"impressions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">impressions</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"first_button_clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">first</span><span class="w"> </span><span class="err">button</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"second_button_clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">button</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"unique_recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">recipients</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions1"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions1_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions2"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">third</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions2_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">third</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions3"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">fourth</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions3_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">fourth</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="w">
      			</span><span class="p">},</span><span class="w"> </span><span class="p">{</span><span class="w">
      				</span><span class="nl">"variation_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
      				</span><span class="nl">"impressions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">impressions</span><span class="p">,</span><span class="w">
      				</span><span class="nl">"clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
      				</span><span class="nl">"first_button_clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">first</span><span class="w"> </span><span class="err">button</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
      				</span><span class="nl">"second_button_clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">button</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"unique_recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">recipients</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions1"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions1_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions2"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">third</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions2_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">third</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions3"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">fourth</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions3_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">fourth</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="w">
      			</span><span class="p">},</span><span class="w"> </span><span class="p">{</span><span class="w">
      				</span><span class="nl">"variation_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
      				</span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
      				</span><span class="nl">"unique_recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">recipients</span><span class="p">,</span><span class="w">
      				</span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions1"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions1_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions2"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">third</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions2_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">third</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions3"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">fourth</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                    </span><span class="nl">"conversions3_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">fourth</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="w">
      				</span><span class="nl">"enrolled"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">enrolled</span><span class="w"> </span><span class="err">users</span><span class="w">
      			</span><span class="p">}]</span><span class="w">
      		</span><span class="p">},</span><span class="w">
      		</span><span class="nl">"conversions_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"conversions1_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"conversions2_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"conversions3_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"conversions1"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"conversions2"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"conversions3"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"unique_recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="p">,</span><span class="w">
      		</span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">float)</span><span class="w">
         </span><span class="p">}],</span><span class="w">
         </span><span class="err">...</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>The possible message types are: <code class="language-plaintext highlighter-rouge">email</code>, <code class="language-plaintext highlighter-rouge">trigger_in_app_message</code>, <code class="language-plaintext highlighter-rouge">webhook</code>, <code class="language-plaintext highlighter-rouge">android_push</code>, <code class="language-plaintext highlighter-rouge">ios_push</code>, <code class="language-plaintext highlighter-rouge">kindle_push</code>, and <code class="language-plaintext highlighter-rouge">web_push</code>. All push message types will have the same statistics shown for <code class="language-plaintext highlighter-rouge">android_push</code>.</p>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
