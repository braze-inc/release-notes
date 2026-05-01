<div id='api_ixjlqxrmmgpd' class='api_div'>
<h1 id="export-send-analytics">Export send analytics</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/sends/data_series</p>
</div>

<blockquote>
  <p>Use this endpoint to retrieve a daily series of various stats for a tracked <code class="language-plaintext highlighter-rouge">send_id</code> for API campaigns.</p>
</blockquote>

<p>Braze stores send analytics for 14 days after the send. Campaign conversions will be attributed toward the most recent <code class="language-plaintext highlighter-rouge">send_id</code> that a given user has received from the campaign.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>This endpoint is for API campaigns only. To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">sends.data_series</code> permission.</p>

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
      <td>See <a href="/docs/api/identifier_types/">campaign API identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">send_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">Send API identifier</a>.</td>
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
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&amp;send_id={{send_identifier}}&amp;length=30&amp;ending_at=2014-12-10T23:59:59-05:00' \
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"data"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"time"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
            </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="nl">"ios_push"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                      </span><span class="nl">"variation_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">variation</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"sent"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">sends</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"delivered"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">successfully</span><span class="w"> </span><span class="err">delivered</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"undelivered"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">undelivered</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"delivery_failed"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">rejected</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"direct_opens"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">direct</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"total_opens"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">total</span><span class="w"> </span><span class="err">opens</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"bounces"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">bounces</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"body_clicks"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">clicks</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">dollars</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">revenue</span><span class="w"> </span><span class="err">(USD)</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"unique_recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">unique</span><span class="w"> </span><span class="err">recipients</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign-level</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"conversions_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"conversions1"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"conversions1_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">second</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"conversions2"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">third</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"conversions2_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">third</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"conversions3"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">fourth</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w">
                      </span><span class="nl">"conversions3_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">fourth</span><span class="p">,</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">attributed</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">sent</span><span class="w">
                      </span><span class="p">}</span><span class="w">
                  </span><span class="p">]</span><span class="w">
            </span><span class="p">},</span><span class="w">
        </span><span class="nl">"conversions_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions1_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions2_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions3_by_send_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions1"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions2"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"conversions3"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"unique_recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"revenue"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">float)</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
