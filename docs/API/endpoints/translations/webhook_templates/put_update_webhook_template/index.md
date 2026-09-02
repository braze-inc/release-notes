<div id='api_qvwdcwthunjh' class='api_div' data-search-keywords='update translations for a webhook template message'>
<h1 id="update-translations-for-a-webhook-template">Update translations for a webhook template</h1>
<div class="api_type"><div class="method put ">put</div>
<p>/templates/webhook/translations</p>
</div>

<blockquote>
  <p>Use this endpoint to update translations for a <a href="/docs/user_guide/messaging/templates/webhook_templates">webhook template</a>. For more information about translation features, see <a href="/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages">Multi-language messages</a>.</p>
</blockquote>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with the <code class="language-plaintext highlighter-rouge">templates.translations.update</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

<p>There are no path parameters for this endpoint.</p>

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
      <td><code class="language-plaintext highlighter-rouge">template_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of your webhook template.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">locale_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The UUID of the locale to update. The locale must be configured for the webhook template.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">translation_map</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>An object containing the updated translations.</td>
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
10
11
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> PUT <span class="s1">'https://rest.iad-03.braze.com/templates/webhook/translations'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
  "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
  "locale_id": "a14404b3-3626-4de0-bdec-06935f3aa0ad",
  "translation_map": {
    "id_0": "¡Hola!",
    "id_1": "¿Te gustaría comprar esto?"
  }
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>There are five status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">200</code>, <code class="language-plaintext highlighter-rouge">400</code>, <code class="language-plaintext highlighter-rouge">403</code>, <code class="language-plaintext highlighter-rouge">404</code>, and <code class="language-plaintext highlighter-rouge">429</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> returns the following empty response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
</pre></td><td class="rouge-code"><pre><span class="p">{}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="example-error-response">Example error response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">400</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Locale not found"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
