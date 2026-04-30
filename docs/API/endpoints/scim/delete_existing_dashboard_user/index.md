<div id='api_rzjzplfsqodn' class='api_div'>
<h1 id="remove-dashboard-user-account">Remove dashboard user account</h1>
<div class="api_type"><div class="method delete ">delete</div>
<p>/scim/v2/Users/{id}</p>
</div>

<blockquote>
  <p>Use this endpoint to permanently delete an existing dashboard user by specifying the resource <code class="language-plaintext highlighter-rouge">id</code> returned by the SCIM <a href="/docs/api/endpoints/scim/post_create_user_account/"><code class="language-plaintext highlighter-rouge">POST</code></a> method.</p>
</blockquote>

<p>This is similar to deleting a user in the <strong>Company Users</strong> section of the Braze dashboard.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need a SCIM token. You’ll use your service origin as the <code class="language-plaintext highlighter-rouge">X-Request-Origin</code> header. For more information, refer to <a href="/docs/scim/automated_user_provisioning/">Automated user provisioning</a>.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

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
      <td><code class="language-plaintext highlighter-rouge">id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The user’s resource ID. This parameter is returned by the  <code class="language-plaintext highlighter-rouge">POST</code> <code class="language-plaintext highlighter-rouge">/scim/v2/Users/</code> or <code class="language-plaintext highlighter-rouge">GET</code>  <code class="language-plaintext highlighter-rouge">/scim/v2/Users?filter=userName eq "user@test.com"</code> methods.</td>
    </tr>
  </tbody>
</table>

<h2 id="request-body">Request body</h2>

<div class="language-http highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="err">Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="example-request">Example request</h2>
<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> DELETE <span class="s1">'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR-SCIM-TOKEN-HERE'</span> <span class="se">\</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<h3 id="example-error-response">Example error response</h3>

<div class="language-http highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre><span class="k">HTTP</span><span class="o">/</span><span class="m">1.1</span> <span class="m">204</span> <span class="ne">Not Found</span>
<span class="na">Content-Type</span><span class="p">:</span> <span class="s">text/html; charset=UTF-8</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<p>If a developer with this ID doesn’t exist in Braze, the endpoint will respond with:</p>
<div class="language-http highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre><span class="k">HTTP</span><span class="o">/</span><span class="m">1.1</span> <span class="m">404</span> <span class="ne">Not Found</span>
<span class="na">Content-Type</span><span class="p">:</span> <span class="s">text/html; charset=UTF-8</span>

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
</pre></td></tr></tbody></table></code></pre></div></div>
</div>
