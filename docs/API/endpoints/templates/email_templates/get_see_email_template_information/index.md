<div id='api_hutwqgwsddoh' class='api_div'>
<h1 id="see-email-template-information">See email template information</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/templates/email/info</p>
</div>

<blockquote>
  <p>Use this endpoint to get information on your email templates.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Templates built using the drag-and-drop editor for email are not accepted.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>
<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">templates.email.info</code> permission.</p>

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
      <th>Data Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">email_template_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">email template API identifier</a>.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"email_template_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">Your</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template's</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">Identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"template_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="p">,</span><span class="w">
  </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">description</span><span class="p">,</span><span class="w">
  </span><span class="nl">"subject"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">subject</span><span class="w"> </span><span class="err">line</span><span class="p">,</span><span class="w">
  </span><span class="nl">"preheader"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">preheader</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">generate</span><span class="w"> </span><span class="err">previews</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">some</span><span class="w"> </span><span class="err">clients)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">may</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">HTML</span><span class="p">,</span><span class="w">
  </span><span class="nl">"plaintext_body"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">A</span><span class="w"> </span><span class="err">plaintext</span><span class="w"> </span><span class="err">version</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">body</span><span class="p">,</span><span class="w">
  </span><span class="nl">"should_inline_css"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">Whether</span><span class="w"> </span><span class="err">there</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">inline</span><span class="w"> </span><span class="err">CSS</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">-</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">css</span><span class="w"> </span><span class="err">inlining</span><span class="w"> </span><span class="err">value</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">workspace</span><span class="p">,</span><span class="w">
  </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">Tag</span><span class="w"> </span><span class="err">names</span><span class="p">,</span><span class="w">
  </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">created</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
  </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">updated</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>Images in this response will show in the <code class="language-plaintext highlighter-rouge">body</code> variable as HTML.</p>

</div>
