<div id='api_ernidwhphame' class='api_div'>
<h1 id="view-all-translations-for-a-content-block">View all translations for a Content Block</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/content_blocks/translations</p>
</div>

<blockquote>
  <p>Use this endpoint to view all the translations for a <a href="/docs/user_guide/messaging/design_and_edit/content_blocks/">Content Block</a>. See <a href="/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/">Locales in messages</a> for more information about translation features.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>This endpoint is currently in early access. Contact your Braze account manager if you’re interested in participating in the early access.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">content_blocks.translations.get</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">content_block_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of your Content Block.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">locale_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A locale UUID to filter the responses.</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>All translation IDs are considered universal unique identifiers (UUIDs), which can be found in the GET endpoint’s response.</p>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations?content_block_id={content_block_id}&amp;locale_id={locale_uuid}' \
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
31
32
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
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"translation_map"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="nl">"id_0"</span><span class="p">:</span><span class="w"> </span><span class="s2">"你好"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"id_1"</span><span class="p">:</span><span class="w"> </span><span class="s2">"我的名字是 Jacky"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"id_2"</span><span class="p">:</span><span class="w"> </span><span class="s2">"圖書館在哪裡?"</span><span class="w">
            </span><span class="p">},</span><span class="w">
            </span><span class="nl">"locale"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="nl">"uuid"</span><span class="p">:</span><span class="w"> </span><span class="s2">"a1b12345-cd35-1234-5678-abcdefa99r3f"</span><span class="p">,</span><span class="w">
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
4
5
6
7
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
	</span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
		</span><span class="p">{</span><span class="w">
			</span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"This message does not support multi-language."</span><span class="w">
		</span><span class="p">}</span><span class="w">
	</span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
