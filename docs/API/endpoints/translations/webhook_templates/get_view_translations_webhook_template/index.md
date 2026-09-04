<div id='api_pvdnhkflrctg' class='api_div' data-search-keywords='view translations for a webhook template translations translation_map id_0 id_1 locale uuid name country language locale_key message'>
<h1 id="view-translations-for-a-webhook-template">View translations for a webhook template</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/templates/webhook/translations</p>
</div>

<blockquote>
  <p>Use this endpoint to view translations for a <a href="/docs/user_guide/messaging/templates/webhook_templates">webhook template</a>. You can return all configured locales or filter the response by locale. For more information about translation features, see <a href="/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages">Multi-language messages</a>.</p>
</blockquote>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with the <code class="language-plaintext highlighter-rouge">templates.translations.get</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">template_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of your webhook template.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">locale_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The locale UUID to return. If omitted, the response includes all locales configured for the webhook template.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> GET <span class="s1">'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&amp;locale_id={LOCALE_ID}'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<p>Replace <em><code class="language-plaintext highlighter-rouge">TEMPLATE_ID</code></em> with the ID of your webhook template and <em><code class="language-plaintext highlighter-rouge">LOCALE_ID</code></em> with the UUID of the locale you want to return. Omit <code class="language-plaintext highlighter-rouge">locale_id</code> to return all configured locales.</p>

<h2 id="response">Response</h2>

<p>There are five status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">200</code>, <code class="language-plaintext highlighter-rouge">400</code>, <code class="language-plaintext highlighter-rouge">403</code>, <code class="language-plaintext highlighter-rouge">404</code>, and <code class="language-plaintext highlighter-rouge">429</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response body.</p>

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
18
19
20
21
22
23
24
25
26
27
28
29
30
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"translations"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"translation_map"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"id_0"</span><span class="p">:</span><span class="w"> </span><span class="s2">"¡Hola!"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"id_1"</span><span class="p">:</span><span class="w"> </span><span class="s2">"¿Te gustaría comprar esto?"</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="nl">"locale"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"uuid"</span><span class="p">:</span><span class="w"> </span><span class="s2">"c7c12345-de35-1234-5678-abcdefa99a3f"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"es-MX"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"country"</span><span class="p">:</span><span class="w"> </span><span class="s2">"MX"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"language"</span><span class="p">:</span><span class="w"> </span><span class="s2">"es"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"locale_key"</span><span class="p">:</span><span class="w"> </span><span class="s2">"es-mx"</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"translation_map"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"id_0"</span><span class="p">:</span><span class="w"> </span><span class="s2">"你好！"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"id_1"</span><span class="p">:</span><span class="w"> </span><span class="s2">"你想買這個嗎？"</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="nl">"locale"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"uuid"</span><span class="p">:</span><span class="w"> </span><span class="s2">"a1b12345-cd35-1234-5678-abcdefa99a3f"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"zh-HK"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"country"</span><span class="p">:</span><span class="w"> </span><span class="s2">"HK"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"language"</span><span class="p">:</span><span class="w"> </span><span class="s2">"zh"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"locale_key"</span><span class="p">:</span><span class="w"> </span><span class="s2">"zh-hk"</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="example-error-response">Example error response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">400</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Invalid locale ID"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
