<div id='api_nchdaenywecg' class='api_div'>
<h1 id="view-details-for-preference-center">View details for preference center</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/preference_center/v1/{preferenceCenterExternalID}</p>
</div>

<blockquote>
  <p>Use this endpoint to view the details for your preference centers, including when it was created and updated.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6a47fd7c-2997-4832-aedb-d101a2dd03a5" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">preference_center.get</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

<table role="presentation">
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
      <td><code class="language-plaintext highlighter-rouge">preferenceCenterExternalID</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID for your preference center.</td>
    </tr>
  </tbody>
</table>

<h2 id="request-parameters">Request parameters</h2>

<p>There are no request parameters for this endpoint.</p>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/preference_center_external_id \
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"My Preference Center"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"preference_center_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"preference_center_api_id"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"example_time_created"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"example_time_updated"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"preference_center_title"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Example preference center title"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"preference_center_page_html"</span><span class="p">:</span><span class="w"> </span><span class="s2">"HTML for preference center here"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"confirmation_page_html"</span><span class="p">:</span><span class="w"> </span><span class="s2">"HTML for confirmation page here"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"redirect_page_html"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span><span class="w">
  </span><span class="nl">"preference_center_options"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"meta-viewport-content"</span><span class="p">:</span><span class="w"> </span><span class="s2">"width=device-width, initial-scale=2"</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"state"</span><span class="p">:</span><span class="w"> </span><span class="s2">"active"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
