<div id='api_umurfhfpbojw' class='api_div' data-search-keywords='look up request processing status results group_id status received done processing final_completion_time'>
<h1 id="look-up-request-processing-status">Look up request processing status</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/users/track/status</p>
</div>

<blockquote>
  <p>Use this endpoint to check whether Braze has finished processing a group of asynchronous <a href="/docs/api/endpoints/user_data/post_user_track"><code class="language-plaintext highlighter-rouge">/users/track</code> endpoint</a> requests.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>This endpoint is in beta. If you’re interested in participating in the beta, contact your Braze account manager.</p>

<p>A successful response from <code class="language-plaintext highlighter-rouge">/users/track</code> means Braze received your request and queued it for processing. To confirm that processing has finished, include the same <code class="language-plaintext highlighter-rouge">group_id</code> in each related <code class="language-plaintext highlighter-rouge">/users/track</code> request, then call this endpoint with that <code class="language-plaintext highlighter-rouge">group_id</code>. When the group’s <code class="language-plaintext highlighter-rouge">status</code> is <code class="language-plaintext highlighter-rouge">completed</code>, you can safely take actions that depend on that data, such as triggering a Canvas or launching a campaign.</p>

<p>For the full workflow, group ID requirements, limits, and retention, see <a href="/docs/api/endpoints/user_data/post_user_track#track-request-processing-status">Track request processing status</a>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics">API key</a> with the <code class="language-plaintext highlighter-rouge">users.track.status</code> permission. The <code class="language-plaintext highlighter-rouge">users.track</code> permission doesn’t include access to this endpoint.</p>

<p>Any API key in the workspace with the <code class="language-plaintext highlighter-rouge">users.track.status</code> permission can look up any group in that workspace, regardless of which API key sent the <code class="language-plaintext highlighter-rouge">/users/track</code> requests.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="query-parameters">Query parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Query parameters">
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
      <td><code class="language-plaintext highlighter-rouge">group_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The group ID you included in your <code class="language-plaintext highlighter-rouge">/users/track</code> requests. Include one <code class="language-plaintext highlighter-rouge">group_id</code> per request.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/users/track/status?group_id=loyalty_backfill_2026-09-23' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
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
  </span><span class="nl">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"group_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w">
      </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">processing</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">group</span><span class="p">,</span><span class="w"> </span><span class="err">either</span><span class="w"> </span><span class="s2">"processing"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"completed"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"received"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">/users/track</span><span class="w"> </span><span class="err">requests</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">accepted</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">group</span><span class="p">,</span><span class="w">
      </span><span class="nl">"done"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">accepted</span><span class="w"> </span><span class="err">requests</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">finished</span><span class="w"> </span><span class="err">processing</span><span class="p">,</span><span class="w">
      </span><span class="nl">"processing"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">accepted</span><span class="w"> </span><span class="err">requests</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">still</span><span class="w"> </span><span class="err">processing</span><span class="p">,</span><span class="w">
      </span><span class="nl">"final_completion_time"</span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="kc">null</span><span class="err">)</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">request</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">finished</span><span class="w"> </span><span class="err">processing</span><span class="p">,</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">format</span><span class="w"> </span><span class="err">(UTC).</span><span class="w"> </span><span class="err">This</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="kc">null</span><span class="w"> </span><span class="err">until</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="s2">"completed"</span><span class="err">.</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>The <code class="language-plaintext highlighter-rouge">results</code> array contains one object when Braze finds the group. It’s empty when the group doesn’t exist in the workspace or its 24-hour retention period has ended. Braze returns an empty <code class="language-plaintext highlighter-rouge">results</code> array for both cases, so an empty array doesn’t tell you whether a group ever existed.</p>

<h3 id="response-parameters">Response parameters</h3>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Response parameters">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Data Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">group_id</code></td>
      <td>String</td>
      <td>The group ID from your request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">status</code></td>
      <td>String</td>
      <td><code class="language-plaintext highlighter-rouge">processing</code> if Braze is still processing any accepted request in the group. <code class="language-plaintext highlighter-rouge">completed</code> if Braze has finished processing every accepted request in the group.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">received</code></td>
      <td>Integer</td>
      <td>The number of <code class="language-plaintext highlighter-rouge">/users/track</code> requests with this <code class="language-plaintext highlighter-rouge">group_id</code> that Braze accepted for status tracking. Braze counts a request as soon as it accepts it.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">done</code></td>
      <td>Integer</td>
      <td>The number of accepted requests that Braze has finished processing.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">processing</code></td>
      <td>Integer</td>
      <td>The number of accepted requests that Braze is still processing. This equals <code class="language-plaintext highlighter-rouge">received</code> minus <code class="language-plaintext highlighter-rouge">done</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">final_completion_time</code></td>
      <td>String or null</td>
      <td>The time Braze finished processing the last request in the group, in ISO 8601 format (UTC) with millisecond precision. <code class="language-plaintext highlighter-rouge">null</code> while <code class="language-plaintext highlighter-rouge">status</code> is <code class="language-plaintext highlighter-rouge">processing</code>.</td>
    </tr>
  </tbody>
</table>

<p>A <code class="language-plaintext highlighter-rouge">completed</code> status means Braze finished processing every request in the group, including requests where Braze rejected some objects. This endpoint reports request counts only and doesn’t report results for individual attributes, events, or purchases. To find rejected objects, check the <code class="language-plaintext highlighter-rouge">errors</code> array in each <code class="language-plaintext highlighter-rouge">/users/track</code> response.</p>

<h2 id="example-responses">Example responses</h2>

<h3 id="group-still-processing">Group still processing</h3>

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
  </span><span class="nl">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"group_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"loyalty_backfill_2026-09-23"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"processing"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"received"</span><span class="p">:</span><span class="w"> </span><span class="mi">4</span><span class="p">,</span><span class="w">
      </span><span class="nl">"done"</span><span class="p">:</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w">
      </span><span class="nl">"processing"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w">
      </span><span class="nl">"final_completion_time"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="group-completed">Group completed</h3>

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
  </span><span class="nl">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"group_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"loyalty_backfill_2026-09-23"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"completed"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"received"</span><span class="p">:</span><span class="w"> </span><span class="mi">4</span><span class="p">,</span><span class="w">
      </span><span class="nl">"done"</span><span class="p">:</span><span class="w"> </span><span class="mi">4</span><span class="p">,</span><span class="w">
      </span><span class="nl">"processing"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">
      </span><span class="nl">"final_completion_time"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2026-09-23T18:58:57.123Z"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="group-not-found-or-expired">Group not found or expired</h3>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<p>The following table lists errors this endpoint can return and how to resolve them.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Troubleshooting">
  <thead>
    <tr>
      <th>Status code</th>
      <th>Error message</th>
      <th>Troubleshooting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">400</code></td>
      <td><code class="language-plaintext highlighter-rouge">Invalid group_id</code></td>
      <td>Include exactly one <code class="language-plaintext highlighter-rouge">group_id</code> query parameter. The value must be 1 to 128 characters and contain only letters, numbers, periods (<code class="language-plaintext highlighter-rouge">.</code>), underscores (<code class="language-plaintext highlighter-rouge">_</code>), tildes (<code class="language-plaintext highlighter-rouge">~</code>), and hyphens (<code class="language-plaintext highlighter-rouge">-</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">403</code></td>
      <td><code class="language-plaintext highlighter-rouge">Access Denied</code></td>
      <td>Use an API key with the <code class="language-plaintext highlighter-rouge">users.track.status</code> permission.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">403</code></td>
      <td><code class="language-plaintext highlighter-rouge">API request status is not enabled for this app group.</code></td>
      <td>Request status tracking isn’t enabled for your workspace. Contact your Braze account manager.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">429</code></td>
      <td>Rate limit exceeded</td>
      <td>Wait for your rate limit window to reset before sending more requests. For more information, see <a href="#rate-limit">Rate limit</a>.</td>
    </tr>
  </tbody>
</table>

<p>For other status codes and error messages, see <a href="/docs/api/errors#fatal-errors">Fatal errors &amp; responses</a>.</p>

</div>
