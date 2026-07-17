<div id='api_rxxzeuqerlft' class='api_div' data-search-keywords='prerequisites app_id apple certificate jwt_key_id jwt_team_id jwt_bundle_id apns_gateway firebase credential huawei app_secret kindle client_id client_secret message'>
<h1 id="update-push-credentials">Update push credentials</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/apps/push_credential/update</p>
<div class="coreclass core_endpoint "><a href="/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to programmatically update the push credentials for a single app, so you can manage credentials without using the dashboard UI.</p>
</blockquote>

<p>Each request updates the push credentials for one app and one push platform. Credential files, such as the iOS authentication key or the Firebase service account, are passed as <a href="https://en.wikipedia.org/wiki/Base64">Base64</a>-encoded strings inside the JSON request body.</p>

<p>This endpoint supports the following push platforms:</p>

<table class="reset-td-br-1 reset-td-br-2" aria-label="Supported push platforms">
  <thead>
    <tr>
      <th>Platform</th>
      <th>Credentials</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS (APNs)</td>
      <td><code class="language-plaintext highlighter-rouge">.p8</code> authentication key only. <code class="language-plaintext highlighter-rouge">.p12</code> and <code class="language-plaintext highlighter-rouge">.pem</code> certificates aren’t supported by this endpoint.</td>
    </tr>
    <tr>
      <td>Android (Firebase Cloud Messaging)</td>
      <td>Service account JSON</td>
    </tr>
    <tr>
      <td>Android (Huawei Mobile Services)</td>
      <td>App ID and app secret</td>
    </tr>
    <tr>
      <td>Kindle (Amazon Device Messaging)</td>
      <td>Client ID and client secret</td>
    </tr>
  </tbody>
</table>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with the <code class="language-plaintext highlighter-rouge">apps.push_credential</code> permission.</p>

<h2 id="request-body">Request body</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
</pre></td></tr></tbody></table></code></pre></div></div>

<p>Include one platform object per request: <code class="language-plaintext highlighter-rouge">apple</code>, <code class="language-plaintext highlighter-rouge">firebase</code>, <code class="language-plaintext highlighter-rouge">huawei</code>, or <code class="language-plaintext highlighter-rouge">kindle</code>.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"app_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">key</span><span class="w"> </span><span class="err">found</span><span class="w"> </span><span class="err">under</span><span class="w"> </span><span class="err">Settings</span><span class="w"> </span><span class="err">&gt;</span><span class="w"> </span><span class="err">App</span><span class="w"> </span><span class="err">Settings</span><span class="p">,</span><span class="w">
  </span><span class="nl">"apple"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"certificate"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Base</span><span class="mi">64</span><span class="err">-encoded</span><span class="w"> </span><span class="err">.p</span><span class="mi">8</span><span class="w"> </span><span class="err">authentication</span><span class="w"> </span><span class="err">key</span><span class="p">,</span><span class="w">
    </span><span class="nl">"jwt_key_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">key</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">.p</span><span class="mi">8</span><span class="w"> </span><span class="err">authentication</span><span class="w"> </span><span class="err">key</span><span class="p">,</span><span class="w">
    </span><span class="nl">"jwt_team_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">Apple</span><span class="w"> </span><span class="err">Developer</span><span class="w"> </span><span class="err">team</span><span class="w"> </span><span class="err">ID</span><span class="p">,</span><span class="w">
    </span><span class="nl">"jwt_bundle_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">app's</span><span class="w"> </span><span class="err">bundle</span><span class="w"> </span><span class="err">ID</span><span class="p">,</span><span class="w">
    </span><span class="nl">"apns_gateway"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">either</span><span class="w"> </span><span class="s2">"prod"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"dev"</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"app_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">key</span><span class="w"> </span><span class="err">found</span><span class="w"> </span><span class="err">under</span><span class="w"> </span><span class="err">Settings</span><span class="w"> </span><span class="err">&gt;</span><span class="w"> </span><span class="err">App</span><span class="w"> </span><span class="err">Settings</span><span class="p">,</span><span class="w">
  </span><span class="nl">"firebase"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"credential"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Base</span><span class="mi">64</span><span class="err">-encoded</span><span class="w"> </span><span class="err">Firebase</span><span class="w"> </span><span class="err">service</span><span class="w"> </span><span class="err">account</span><span class="w"> </span><span class="err">JSON</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"app_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">key</span><span class="w"> </span><span class="err">found</span><span class="w"> </span><span class="err">under</span><span class="w"> </span><span class="err">Settings</span><span class="w"> </span><span class="err">&gt;</span><span class="w"> </span><span class="err">App</span><span class="w"> </span><span class="err">Settings</span><span class="p">,</span><span class="w">
  </span><span class="nl">"huawei"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"app_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">Huawei</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">ID</span><span class="p">,</span><span class="w">
    </span><span class="nl">"app_secret"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">Huawei</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">secret</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"app_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">key</span><span class="w"> </span><span class="err">found</span><span class="w"> </span><span class="err">under</span><span class="w"> </span><span class="err">Settings</span><span class="w"> </span><span class="err">&gt;</span><span class="w"> </span><span class="err">App</span><span class="w"> </span><span class="err">Settings</span><span class="p">,</span><span class="w">
  </span><span class="nl">"kindle"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"client_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">Amazon</span><span class="w"> </span><span class="err">Device</span><span class="w"> </span><span class="err">Messaging</span><span class="w"> </span><span class="err">client</span><span class="w"> </span><span class="err">ID</span><span class="p">,</span><span class="w">
    </span><span class="nl">"client_secret"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">Amazon</span><span class="w"> </span><span class="err">Device</span><span class="w"> </span><span class="err">Messaging</span><span class="w"> </span><span class="err">client</span><span class="w"> </span><span class="err">secret</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="request-parameters">Request parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Request parameters">
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
      <td><a href="/docs/api/identifier_types#app-identifier"><code class="language-plaintext highlighter-rouge">app_id</code></a></td>
      <td>Required</td>
      <td>String</td>
      <td>The app identifier API key for the app you want to update. Find it in the dashboard under <strong>Settings</strong> &gt; <strong>App Settings</strong>, next to the <strong>API Key</strong> field.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">apple</code></td>
      <td>Required*</td>
      <td>Object</td>
      <td>The iOS (APNs) credentials.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">firebase</code></td>
      <td>Required*</td>
      <td>Object</td>
      <td>The Android (Firebase Cloud Messaging) credentials.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">huawei</code></td>
      <td>Required*</td>
      <td>Object</td>
      <td>The Android (Huawei Mobile Services) credentials.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">kindle</code></td>
      <td>Required*</td>
      <td>Object</td>
      <td>The Kindle (Amazon Device Messaging) credentials.</td>
    </tr>
  </tbody>
</table>

<p>* Include exactly one platform object per request.</p>

<h3 id="ios-apns-parameters">iOS (APNs) parameters</h3>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="iOS (APNs) parameters">
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
      <td><code class="language-plaintext highlighter-rouge">certificate</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The Base64-encoded <code class="language-plaintext highlighter-rouge">.p8</code> authentication key. Only <code class="language-plaintext highlighter-rouge">.p8</code> authentication keys are supported; <code class="language-plaintext highlighter-rouge">.p12</code> and <code class="language-plaintext highlighter-rouge">.pem</code> certificates aren’t supported by this endpoint.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">jwt_key_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The key ID for the <code class="language-plaintext highlighter-rouge">.p8</code> authentication key.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">jwt_team_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Your Apple Developer team ID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">jwt_bundle_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Your app’s bundle ID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">apns_gateway</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The APNs environment. Available values are <code class="language-plaintext highlighter-rouge">prod</code> and <code class="language-plaintext highlighter-rouge">dev</code>.</td>
    </tr>
  </tbody>
</table>

<h3 id="android-firebase-cloud-messaging-parameters">Android (Firebase Cloud Messaging) parameters</h3>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Android (Firebase Cloud Messaging) parameters">
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
      <td><code class="language-plaintext highlighter-rouge">credential</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The Base64-encoded Firebase service account JSON.</td>
    </tr>
  </tbody>
</table>

<h3 id="android-huawei-mobile-services-parameters">Android (Huawei Mobile Services) parameters</h3>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Android (Huawei Mobile Services) parameters">
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
      <td><code class="language-plaintext highlighter-rouge">app_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Your Huawei app ID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">app_secret</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Your Huawei app secret.</td>
    </tr>
  </tbody>
</table>

<h3 id="kindle-amazon-device-messaging-parameters">Kindle (Amazon Device Messaging) parameters</h3>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Kindle (Amazon Device Messaging) parameters">
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
      <td><code class="language-plaintext highlighter-rouge">client_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Your Amazon Device Messaging client ID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">client_secret</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Your Amazon Device Messaging client secret.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-requests">Example requests</h2>

<h3 id="ios-apns">iOS (APNs)</h3>

<p>The <code class="language-plaintext highlighter-rouge">apple.certificate</code> value must be Base64-encoded, and <code class="language-plaintext highlighter-rouge">apple.apns_gateway</code> must be set to either <code class="language-plaintext highlighter-rouge">prod</code> or <code class="language-plaintext highlighter-rouge">dev</code>.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "apple": {
    "certificate": "{BASE64_ENCODED_STRING}",
    "jwt_key_id": "{YOUR_KEY_ID}",
    "jwt_team_id": "{YOUR_TEAM_ID}",
    "jwt_bundle_id": "{YOUR_BUNDLE_ID}",
    "apns_gateway": "prod"
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="android-firebase-cloud-messaging">Android (Firebase Cloud Messaging)</h3>

<p>The <code class="language-plaintext highlighter-rouge">firebase.credential</code> value must be Base64-encoded.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "firebase": {
    "credential": "{BASE64_ENCODED_STRING}"
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="android-huawei-mobile-services">Android (Huawei Mobile Services)</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
10
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "huawei": {
    "app_id": "{YOUR_HUAWEI_APP_ID}",
    "app_secret": "{YOUR_HUAWEI_APP_SECRET}"
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="kindle-amazon-device-messaging">Kindle (Amazon Device Messaging)</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
10
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "kindle": {
    "client_id": "{YOUR_ADM_CLIENT_ID}",
    "client_secret": "{YOUR_ADM_CLIENT_SECRET}"
  }
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="example-response">Example response</h2>

<p>If the credentials are updated successfully, you’ll receive a response with the status code <code class="language-plaintext highlighter-rouge">201</code>.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
