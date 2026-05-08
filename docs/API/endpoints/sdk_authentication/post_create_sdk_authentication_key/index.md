<div id='api_wxvuawoofuba' class='api_div'>
<h1 id="create-sdk-authentication-key">Create SDK Authentication key</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/app_group/sdk_authentication/create</p>
</div>

<blockquote>
  <p>Use this endpoint to create a new SDK Authentication key for your app.</p>
</blockquote>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">sdk_authentication.create</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-body">Request body</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
</pre></td></tr></tbody></table></code></pre></div></div>
<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"app_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"App API identifier"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"rsa_public_key_str"</span><span class="p">:</span><span class="w"> </span><span class="s2">"RSA public key string"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="s2">"description"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"make_primary"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

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
    <tr>
      <td><code class="language-plaintext highlighter-rouge">rsa_public_key_str</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The RSA public key string. Must be a valid RSA public key or it will return an error.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">description</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Description for the SDK Authentication key.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">make_primary</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>If set to <code class="language-plaintext highlighter-rouge">true</code>, this key will be made the primary SDK Authentication key when it is created.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/app_group/sdk_authentication/create'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR-REST-API-KEY'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
  "description": "SDK Authentication Key for iOS App",
  "make_primary": false
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>
<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"key id"</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">id</code></td>
      <td>String</td>
      <td>The ID of the newly created SDK Authentication key.</td>
    </tr>
  </tbody>
</table>

<h3 id="validation-rules">Validation rules</h3>

<p>This endpoint has the following validation rules:</p>

<ul>
  <li>You can have up to 3 SDK Authentication keys per app.</li>
  <li>The RSA public key string must be a valid RSA public key in the proper format.</li>
  <li>The <code class="language-plaintext highlighter-rouge">app_id</code> must be a valid app API identifier.</li>
  <li>The description cannot be empty.</li>
</ul>

</div>
