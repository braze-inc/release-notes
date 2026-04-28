<div id='api_pwkafvvuoiui' class='api_div'>
<h1 id="update-translations-for-an-email-template">Update translations for an email template</h1>
<div class="api_type"><div class="method put ">put</div>
<p>/templates/email/translations/</p>
</div>

<blockquote>
  <p>Use this endpoint to update translations for an <a href="/docs/user_guide/messaging/templates/email_templates/">email template</a>. See <a href="/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/">Locales in messages</a> for more information about translation features.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>is currently in early access. Contact your Braze account manager if you’re interested in participating in the early access.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">templates.translations.update</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

<p>There are no path parameters for this endpoint.</p>

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
      <td><code class="language-plaintext highlighter-rouge">template_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of your email template.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">locale_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of the locale.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">translations_map</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The map of the translations for your email template.</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint’s response.</p>

<h2 id="example-request">Example request</h2>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"template_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"e24404b3-3626-4de0-bdec-06935f3aa0ab"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"locale_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"h94404b3-3626-4de0-bdec-06935f3aa0ad"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"translation_map"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"id_0"</span><span class="p">:</span><span class="w"> </span><span class="s2">"¡Hola!"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"id_1"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Me llamo Jacky"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"id_2"</span><span class="p">:</span><span class="w"> </span><span class="s2">"¿Dónde está la biblioteca?"</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>There are four status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">200</code>, <code class="language-plaintext highlighter-rouge">400</code>, <code class="language-plaintext highlighter-rouge">404</code>, and <code class="language-plaintext highlighter-rouge">429</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="example-error-response">Example error response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">400</code> could return the following response body. Refer to <a href="#troubleshooting">Troubleshooting</a> for more information about errors you may encounter.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
	</span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
		</span><span class="p">{</span><span class="w">
			</span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1234567-abc-123-012345678"</span><span class="p">,</span><span class="w">
			</span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"The provided translations yielded errors when parsing. Please contact Braze for more information."</span><span class="w">
		</span><span class="p">}</span><span class="w">
	</span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
