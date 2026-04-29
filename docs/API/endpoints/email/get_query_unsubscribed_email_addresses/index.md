<div id='api_ywrmcugtwenn' class='api_div'>
<h1 id="query-list-of-unsubscribed-email-addresses">Query list of unsubscribed email addresses</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/email/unsubscribes</p>
</div>

<blockquote>
  <p>Use this endpoint to return the latest emails that have unsubscribed during the time period from <code class="language-plaintext highlighter-rouge">start_date</code> to <code class="language-plaintext highlighter-rouge">end_date</code>. For a full subscription state history, use <a href="/docs/user_guide/data/distribution/braze_currents/">Currents</a> to track this data.</p>
</blockquote>

<p>You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">email.unsubscribe</code> permission.</p>

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
      <td>Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">end_date</code></td>
      <td>Optional <br />(see note)</td>
      <td>String in YYYY-MM-DD format</td>
      <td>End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API.</td>
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
      <td><code class="language-plaintext highlighter-rouge">sort_direction</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Pass in the value <code class="language-plaintext highlighter-rouge">asc</code> to sort unsubscribes from oldest to newest. Pass in <code class="language-plaintext highlighter-rouge">desc</code> to sort from newest to oldest. If <code class="language-plaintext highlighter-rouge">sort_direction</code> is not included, the default order is newest to oldest.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">email</code></td>
      <td>Optional <br />(see note)</td>
      <td>String</td>
      <td>If provided, we will return whether or not the user has unsubscribed.</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>You must provide an <code class="language-plaintext highlighter-rouge">end_date</code>, as well as either an <code class="language-plaintext highlighter-rouge">email</code> or a <code class="language-plaintext highlighter-rouge">start_date</code>.</p>

<p>If your date range has more than <code class="language-plaintext highlighter-rouge">limit</code> number of unsubscribes, you will need to make multiple API calls, each time increasing the <code class="language-plaintext highlighter-rouge">offset</code> until a call returns either fewer than <code class="language-plaintext highlighter-rouge">limit</code> or zero results.</p>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&amp;end_date=2020-02-01&amp;limit=1&amp;offset=1&amp;sort_direction=desc&amp;email=example@braze.com' \
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
      </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">been</span><span class="w"> </span><span class="err">unsubscribed</span><span class="p">,</span><span class="w">
      </span><span class="nl">"unsubscribed_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">unsubscribed</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">been</span><span class="w"> </span><span class="err">unsubscribed</span><span class="p">,</span><span class="w">
      </span><span class="nl">"unsubscribed_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">unsubscribed</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">been</span><span class="w"> </span><span class="err">unsubscribed</span><span class="p">,</span><span class="w">
      </span><span class="nl">"unsubscribed_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">unsubscribed</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>
</div>
