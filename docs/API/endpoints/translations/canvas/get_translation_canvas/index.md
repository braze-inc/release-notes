<div id='api_tvsdzqianwpo' class='api_div'>
<h1 id="view-translation-for-a-canvas">View translation for a Canvas</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/canvas/translations</p>
</div>

<blockquote>
  <p>Use this endpoint to preview a translated message for a Canvas. See <a href="/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/">Locales in messages</a> for more information about translation features.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>is currently in early access. Contact your Braze account manager if you’re interested in participating in the early access.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">canvas.translations.get</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="query-parameters">Query parameters</h2>

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
      <td><code class="language-plaintext highlighter-rouge">workflow_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of the Canvas.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">step_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of your Canvas step.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">message_variation_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of your message variation.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">locale_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The ID (UUID) of the locale.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">post_launch_draft_version</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>When <code class="language-plaintext highlighter-rouge">true</code> returns the latest draft version instead of the latest live published version. Defaults to <code class="language-plaintext highlighter-rouge">false</code> returning the latest live version.</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint’s response.</p>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?workflow_id={workflow_id}&amp;step_id={step_id}&amp;message_variation_id={message_variation_id}&amp;locale_id={locale_uuid}&amp;post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>There are four status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">200</code>, <code class="language-plaintext highlighter-rouge">400</code>, <code class="language-plaintext highlighter-rouge">404</code>, and <code class="language-plaintext highlighter-rouge">429</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response header and body.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"translations"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"translation_map"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="nl">"id_0"</span><span class="p">:</span><span class="w"> </span><span class="s2">"¡Hola!"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"id_1"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Me llamo Jacky"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"id_2"</span><span class="p">:</span><span class="w"> </span><span class="s2">"¿Dónde está la biblioteca?"</span><span class="w">
            </span><span class="p">},</span><span class="w">
            </span><span class="nl">"locale"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="nl">"uuid"</span><span class="p">:</span><span class="w"> </span><span class="s2">"c7c12345-te35-1234-5678-abcdefa99r3f"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"es-MX"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"country"</span><span class="p">:</span><span class="w"> </span><span class="s2">"MX"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"language"</span><span class="p">:</span><span class="w"> </span><span class="s2">"es"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"locale_key"</span><span class="p">:</span><span class="w"> </span><span class="s2">"es-mx"</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">}</span><span class="w">
    </span><span class="p">]</span><span class="w">
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
	</span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
		</span><span class="p">{</span><span class="w">
			</span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"The provided locale code does not exist."</span><span class="w">
		</span><span class="p">}</span><span class="w">
	</span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
