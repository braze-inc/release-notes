<div id='api_juouamimntwa' class='api_div'>
<h1 id="see-content-block-information">See Content Block information</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/content_blocks/info</p>
</div>

<blockquote>
  <p>Use this endpoint to call information for your existing <a href="/docs/user_guide/messaging/design_and_edit/content_blocks/">Content Blocks</a>.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>
<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">content_blocks.info</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

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
      <td><code class="language-plaintext highlighter-rouge">content_block_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The Content Block identifier. <br /><br />You can find this by either listing Content Block information through an API call or going to the <a href="/docs/user_guide/administer/global/workspace_settings/apis_and_identifiers/">API Keys</a> page, then scrolling to the bottom and searching for your Content Block API identifier.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_inclusion_data</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>When set to <code class="language-plaintext highlighter-rouge">true</code>, the API returns back the Message Variation API identifier of campaigns and Canvases where this Content Block is included, to be used in subsequent calls.  The results exclude archived or deleted campaigns or Canvases.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&amp;include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
  </span><span class="nl">"content_block_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="p">,</span><span class="w">
  </span><span class="nl">"content"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">content</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="p">,</span><span class="w">
  </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">description</span><span class="p">,</span><span class="w">
  </span><span class="nl">"content_type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">content</span><span class="w"> </span><span class="err">type</span><span class="p">,</span><span class="w"> </span><span class="err">html</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w">
  </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">An</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">tags</span><span class="w"> </span><span class="err">formatted</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">strings</span><span class="p">,</span><span class="w">
  </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">created</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
  </span><span class="nl">"last_edited"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">edited</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
  </span><span class="nl">"inclusion_count"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">inclusion</span><span class="w"> </span><span class="err">count</span><span class="p">,</span><span class="w">
  </span><span class="nl">"inclusion_data"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">inclusion</span><span class="w"> </span><span class="err">data</span><span class="p">,</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<p>The following table lists possible returned errors and their associated troubleshooting steps.</p>

<table class="reset-td-br-1 reset-td-br-2" aria-label="Troubleshooting">
  <thead>
    <tr>
      <th>Error</th>
      <th>Troubleshooting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block ID cannot be blank</code></td>
      <td>Make sure that a Content Block is listed in your request and is encapsulated in quotes (<code class="language-plaintext highlighter-rouge">""</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block ID is invalid for this workspace</code></td>
      <td>This Content Block doesn’t exist or is in a different company account or workspace.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block has been deleted—content not available</code></td>
      <td>This Content Block, though it may have existed earlier, has been deleted.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Include Inclusion Data—error</code></td>
      <td>This parameter only accepts boolean values (true or false). Make sure the value for <code class="language-plaintext highlighter-rouge">include_inclusion_data</code> is not encapsulated in quotes (<code class="language-plaintext highlighter-rouge">""</code>), which causes the value to be sent as a string instead. See <a href="#request-parameters">request parameters</a> for details.</td>
    </tr>
  </tbody>
</table>

</div>
