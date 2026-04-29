<div id='api_hbxdrwitnbtc' class='api_div'>
<h1 id="list-sdk-authentication-keys">List SDK Authentication keys</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/app_group/sdk_authentication/keys</p>
</div>

<blockquote>
  <p>Use this endpoint to retrieve all SDK Authentication keys for your app.</p>
</blockquote>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">sdk_authentication.keys</code> permission.</p>

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
      <th>Data type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">app_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The app API identifier.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> GET <span class="s1">'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR-REST-API-KEY'</span>
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"keys"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"abcdef12-3456-7890-abcd-ef1234567890"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"rsa_public_key"</span><span class="p">:</span><span class="w"> </span><span class="s2">"-----BEGIN PUBLIC KEY-----</span><span class="se">\n</span><span class="s2">MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...</span><span class="se">\n</span><span class="s2">-----END PUBLIC KEY-----"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="s2">"SDK Authentication Key for iOS App"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"is_primary"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"fedcba98-7654-3210-fedc-ba9876543210"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"rsa_public_key"</span><span class="p">:</span><span class="w"> </span><span class="s2">"-----BEGIN PUBLIC KEY-----</span><span class="se">\n</span><span class="s2">qWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...</span><span class="se">\n</span><span class="s2">-----END PUBLIC KEY-----"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="s2">"SDK Authentication Key for Android App"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"is_primary"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response-parameters">Response parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" role="presentation">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Data type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">keys</code></td>
      <td>Array</td>
      <td>Array of SDK Authentication key objects.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">keys[].id</code></td>
      <td>String</td>
      <td>The ID of the SDK Authentication key.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">keys[].rsa_public_key</code></td>
      <td>String</td>
      <td>The RSA public key string.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">keys[].description</code></td>
      <td>String</td>
      <td>Description of the SDK Authentication key.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">keys[].is_primary</code></td>
      <td>Boolean</td>
      <td>Whether this key is the primary SDK Authentication key.</td>
    </tr>
  </tbody>
</table>

<h3 id="validation-rules">Validation rules</h3>

<p>This endpoint has the following validation rules:</p>

<ul>
  <li>The <code class="language-plaintext highlighter-rouge">app_id</code> parameter must be a valid app API identifier.</li>
  <li>The app must exist in your workspace.</li>
</ul>

</div>
