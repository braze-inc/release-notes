<div id='api_odksxwjkuucw' class='api_div'>
<h1 id="query-hard-bounced-emails">Query hard bounced emails</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/email/hard_bounces</p>
</div>

<blockquote>
  <p>Use this endpoint to pull a list of email addresses that have “hard bounced” your email messages within a certain time frame.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">email.hard_bounces</code> permission.</p>

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
      <td>Optional*</td>
      <td>String in YYYY-MM-DD format</td>
      <td>*One of <code class="language-plaintext highlighter-rouge">start_date</code> or <code class="language-plaintext highlighter-rouge">email</code> is required. This is the start date of the range to retrieve hard bounces and must be earlier than <code class="language-plaintext highlighter-rouge">end_date</code>. This is treated as midnight in UTC time by the API.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">end_date</code></td>
      <td>Required</td>
      <td>String in YYYY-MM-DD format</td>
      <td>End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API.</td>
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
      <td><code class="language-plaintext highlighter-rouge">email</code></td>
      <td>Optional*</td>
      <td>String</td>
      <td>*One of <code class="language-plaintext highlighter-rouge">start_date</code> or <code class="language-plaintext highlighter-rouge">email</code> is required. If provided, we’ll return whether or not the user has hard bounced. Check that the email strings are formatted properly.</td>
    </tr>
  </tbody>
</table>

<p><strong>Important:</strong></p>

<p>You must provide an <code class="language-plaintext highlighter-rouge">end_date</code>, and either an <code class="language-plaintext highlighter-rouge">email</code> or a <code class="language-plaintext highlighter-rouge">start_date</code>. If you provide all three, <code class="language-plaintext highlighter-rouge">start_date</code>, <code class="language-plaintext highlighter-rouge">end_date</code>, and an <code class="language-plaintext highlighter-rouge">email</code>, we prioritize the emails given and disregard the date range.</p>

<p>If your date range has more than the <code class="language-plaintext highlighter-rouge">limit</code> number of hard bounces, you will need to make multiple API calls, each time increasing the <code class="language-plaintext highlighter-rouge">offset</code> until a call returns either fewer than <code class="language-plaintext highlighter-rouge">limit</code> or zero results. Including <code class="language-plaintext highlighter-rouge">offset</code> and <code class="language-plaintext highlighter-rouge">limit</code> parameters with <code class="language-plaintext highlighter-rouge">email</code> can return an empty response.</p>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&amp;end_date=2019-02-01&amp;limit=100&amp;offset=1' \
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"emails"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">hard</span><span class="w"> </span><span class="err">bounced</span><span class="p">,</span><span class="w">
      </span><span class="nl">"hard_bounced_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">hard</span><span class="w"> </span><span class="err">bounced</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">hard</span><span class="w"> </span><span class="err">bounced</span><span class="p">,</span><span class="w">
      </span><span class="nl">"hard_bounced_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">hard</span><span class="w"> </span><span class="err">bounced</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">hard</span><span class="w"> </span><span class="err">bounced</span><span class="p">,</span><span class="w">
      </span><span class="nl">"hard_bounced_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">hard</span><span class="w"> </span><span class="err">bounced</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>
</div>
