<div id='api_usrycnardsoa' class='api_div'>
<h1 id="list-available-content-blocks">List available Content Blocks</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/content_blocks/list</p>
</div>

<blockquote>
  <p>Use this endpoint to list your existing <a href="/docs/user_guide/messaging/design_and_edit/content_blocks/">Content Blocks</a> information.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>
<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">content_blocks.list</code> permission.</p>

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
      <td>Retrieve only Content Blocks updated at or after the given time.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">modified_before</code></td>
      <td>Optional</td>
      <td>String in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> format</td>
      <td>Retrieve only Content Blocks updated at or before the given time.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">limit</code></td>
      <td>Optional</td>
      <td>Positive Number</td>
      <td>Maximum number of Content Blocks to retrieve. Default to 100 if not provided, with a maximum acceptable value of 1000.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">offset</code></td>
      <td>Optional</td>
      <td>Positive Number</td>
      <td>Number of Content Blocks to skip before returning rest of the templates that fit the search criteria.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&amp;modified_before=2020-02-01T01:01:01.000000&amp;limit=100&amp;offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"count"</span><span class="p">:</span><span class="w"> </span><span class="s2">"integer"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"content_blocks"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"content_block_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="p">,</span><span class="w">
      </span><span class="nl">"content_type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">content</span><span class="w"> </span><span class="err">type</span><span class="p">,</span><span class="w"> </span><span class="err">html</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w">
      </span><span class="nl">"liquid_tag"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Liquid</span><span class="w"> </span><span class="err">tags</span><span class="p">,</span><span class="w">
      </span><span class="nl">"inclusion_count"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">inclusion</span><span class="w"> </span><span class="err">count</span><span class="p">,</span><span class="w">
      </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">created</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
      </span><span class="nl">"last_edited"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">edited</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
      </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">An</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">tags</span><span class="w"> </span><span class="err">formatted</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">strings</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<p>The following table lists possible returned errors and their associated troubleshooting steps.</p>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Error</th>
      <th>Troubleshooting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Modified after time is invalid</code></td>
      <td>The provided date is not a valid or parsable date. Reformat this value as a string in ISO 8601 format (<code class="language-plaintext highlighter-rouge">yyyy-mm-ddThh:mm:ss.ffffff</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Modified before time is invalid</code></td>
      <td>The provided date is not a valid or parsable date. Reformat this value as a string in ISO 8601 format (<code class="language-plaintext highlighter-rouge">yyyy-mm-ddThh:mm:ss.ffffff</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Modified after time must be earlier than or the same as modified before time.</code></td>
      <td>Change the <code class="language-plaintext highlighter-rouge">modified_after</code> value to a time that is earlier than the <code class="language-plaintext highlighter-rouge">modified_before</code> time.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block number limit is invalid</code></td>
      <td>The <code class="language-plaintext highlighter-rouge">limit</code> parameter must be an integer (positive number) greater than 0.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block number limit must be greater than 0</code></td>
      <td>Change the <code class="language-plaintext highlighter-rouge">limit</code> parameter to an integer greater than 0.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block number limit exceeds maximum of 1000</code></td>
      <td>Change the <code class="language-plaintext highlighter-rouge">limit</code> parameter to an integer less than 1000.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Offset is invalid</code></td>
      <td>The <code class="language-plaintext highlighter-rouge">offset</code> parameter must be an integer greater than 0.</td>
    </tr>
    <tr>
      <td>Offset must be greater than 0</td>
      <td>Change the <code class="language-plaintext highlighter-rouge">offset</code> parameter to an integer greater than 0.</td>
    </tr>
  </tbody>
</table>

</div>
