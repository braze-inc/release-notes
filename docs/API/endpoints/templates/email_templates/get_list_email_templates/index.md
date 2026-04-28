<div id='api_xmpyyxhzwsqa' class='api_div'>
<h1 id="list-available-email-templates">List available email templates</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/templates/email/list</p>
</div>

<blockquote>
  <p>Use this endpoint to get a list of available email templates in your Braze account.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>
<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">templates.email.list</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">modified_after</code></td>
      <td>Optional</td>
      <td>String in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> format</td>
      <td>Retrieve only templates updated at or after the given time.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">modified_before</code></td>
      <td>Optional</td>
      <td>String in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> format</td>
      <td>Retrieve only templates updated at or before the given time.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">limit</code></td>
      <td>Optional</td>
      <td>Positive number</td>
      <td>Maximum number of templates to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">offset</code></td>
      <td>Optional</td>
      <td>Positive number</td>
      <td>Number of templates to skip before returning rest of the templates that fit the search criteria.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&amp;modified_before=2020-02-01T01:01:01.000000&amp;limit=1&amp;offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p><strong>Important:</strong></p>

<p>Templates built using the drag-and-drop editor for email are not provided in this response.</p>

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
  </span><span class="nl">"count"</span><span class="p">:</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">templates</span><span class="w"> </span><span class="err">returned</span><span class="w">
  </span><span class="nl">"templates"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="err">template</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">following</span><span class="w"> </span><span class="err">properties</span><span class="p">]</span><span class="err">:</span><span class="w">
    </span><span class="nl">"email_template_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template's</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">Identifier</span><span class="p">,</span><span class="w">
    </span><span class="nl">"template_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="p">,</span><span class="w">
    </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">created</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
    </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">updated</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
    </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">tags</span><span class="w"> </span><span class="err">appended</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">template</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>
</div>



