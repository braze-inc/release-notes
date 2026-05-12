<div id='api_tokpruqtpxax' class='api_div'>
<h1 id="generate-preference-center-url">Generate preference center URL</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/preference_center/v1/{preferenceCenterExternalID}/url/{userID}</p>
</div>

<blockquote>
  <p>Use this endpoint to generate a URL for a preference center.</p>
</blockquote>

<p>Each preference center URL is unique to each user.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">preference_center.user.get</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<p>This rate limit is fixed and is not configurable.</p>

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
    <tr>
      <td><code class="language-plaintext highlighter-rouge">userID</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The user ID.</td>
    </tr>
  </tbody>
</table>

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
      <td><code class="language-plaintext highlighter-rouge">preference_center_api_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID for your preference center.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The external ID for a user.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"preference_center_url"</span><span class="p">:</span><span class="w"> </span><span class="s2">"https://www.example.com/preferences"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>

**Note:**


This endpoint only generates URLs for the new preference center (such as preference centers created using our API or the drag-and-drop editor).


