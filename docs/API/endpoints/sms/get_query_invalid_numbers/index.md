<div id='api_wlmjgarnevwb' class='api_div'>
<h1 id="query-invalid-phone-numbers">Query invalid phone numbers</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/sms/invalid_phone_numbers</p>
</div>

<blockquote>
  <p>Use this endpoint to pull a list of phone numbers that have been marked “invalid” within a certain time frame. See <a href="/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers">Invalid Phone Number Handling</a> documentation for more information.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">sms.invalid_phone_numbers</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">start_date</code></td>
      <td>Optional <br />(see note)</td>
      <td>String in YYYY-MM-DD format</td>
      <td>Start date of the range to retrieve invalid phone numbers, must be earlier than <code class="language-plaintext highlighter-rouge">end_date</code>. This is treated as midnight in UTC time by the API.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">end_date</code></td>
      <td>Optional <br />(see note)</td>
      <td>String in YYYY-MM-DD format</td>
      <td>End date of the range to retrieve invalid phone numbers. This is treated as midnight in UTC time by the API.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">limit</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>Optional field to limit the number of results returned. Defaults to 100, maximum is 500.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">offset</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>Optional beginning point in the list to retrieve from.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">phone_numbers</code></td>
      <td>Optional <br />(see note)</td>
      <td>Array of Strings in e.164 format</td>
      <td>If provided, we will return the phone number if it has been found to be invalid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">reason</code></td>
      <td>Optional <br />(see note)</td>
      <td>String</td>
      <td>Available values are “provider_error” (provider error indicates phone cannot receive SMS) or “deactivated” (phone number has been deactivated). If omitted, all reasons are returned.</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>You must provide either a <code class="language-plaintext highlighter-rouge">start_date</code> and an <code class="language-plaintext highlighter-rouge">end_date</code> OR <code class="language-plaintext highlighter-rouge">phone_numbers</code>. If you provide all three, <code class="language-plaintext highlighter-rouge">start_date</code>, <code class="language-plaintext highlighter-rouge">end_date</code>, and <code class="language-plaintext highlighter-rouge">phone_numbers</code>, we prioritize the given phone numbers and disregard the date range.</p>

<p>If your date range has more than the <code class="language-plaintext highlighter-rouge">limit</code> number of invalid phone numbers, you will need to make multiple API calls with increasing the <code class="language-plaintext highlighter-rouge">offset</code> each time until a call returns either fewer than <code class="language-plaintext highlighter-rouge">limit</code> or zero results.</p>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&amp;end_date=2019-02-01&amp;limit=100&amp;offset=1&amp;phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>
<p>Entries are listed in descending order.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"sms"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"phone"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">phone</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">e.</span><span class="mi">164</span><span class="w"> </span><span class="err">format</span><span class="p">,</span><span class="w">
      </span><span class="nl">"invalid_detected_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">invalid</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">detected</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
      </span><span class="nl">"reason"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"provider_error"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"phone"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">phone</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">e.</span><span class="mi">164</span><span class="w"> </span><span class="err">format</span><span class="p">,</span><span class="w">
      </span><span class="nl">"invalid_detected_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">invalid</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">detected</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
      </span><span class="nl">"reason"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"deactivated"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"phone"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">phone</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">e.</span><span class="mi">164</span><span class="w"> </span><span class="err">format</span><span class="p">,</span><span class="w">
      </span><span class="nl">"invalid_detected_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">invalid</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">detected</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
      </span><span class="nl">"reason"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"provider_error"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>
</div>
