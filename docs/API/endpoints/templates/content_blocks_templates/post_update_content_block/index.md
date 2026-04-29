<div id='api_gffjllhdifjz' class='api_div'>
<h1 id="update-content-block">Update Content Block</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/content_blocks/update</p>
</div>

<blockquote>
  <p>Use this endpoint to update a <a href="/docs/user_guide/messaging/design_and_edit/content_blocks/">Content Block</a>.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>
<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">content_blocks.update</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-body">Request body</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
</pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"content_block_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block's</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier.</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">Must</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">less</span><span class="w"> </span><span class="err">than</span><span class="w"> </span><span class="mi">100</span><span class="w"> </span><span class="err">characters</span><span class="p">,</span><span class="w">
  </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">description</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block.</span><span class="w"> </span><span class="err">Must</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">less</span><span class="w"> </span><span class="err">than</span><span class="w"> </span><span class="mi">250</span><span class="w"> </span><span class="err">character</span><span class="p">,</span><span class="w">
  </span><span class="nl">"content"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">HTML</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">text</span><span class="w"> </span><span class="err">content</span><span class="w"> </span><span class="err">within</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="p">,</span><span class="w">
  </span><span class="nl">"state"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">Choose</span><span class="w"> </span><span class="err">`active`</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">`draft`.</span><span class="w"> </span><span class="err">Defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">`active`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">specified</span><span class="p">,</span><span class="w">
  </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">Tags</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">already</span><span class="w"> </span><span class="err">exist</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

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
      <td><code class="language-plaintext highlighter-rouge">content_block_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Your Content Block’s API identifier.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Name of the Content Block. Must be less than 100 characters.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">description</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Description of the Content Block. Must be less than 250 characters.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">content</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>HTML or text content within Content Blocks.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">state</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Choose <code class="language-plaintext highlighter-rouge">active</code> or <code class="language-plaintext highlighter-rouge">draft</code>. Defaults to <code class="language-plaintext highlighter-rouge">active</code> if not specified.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">tags</code></td>
      <td>Optional</td>
      <td>Array of strings</td>
      <td><a href="/docs/user_guide/messaging/governance/tags/">Tags</a> must already exist.</td>
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
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/content_blocks/update'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
  "content_block_id" :"content_block_id",
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"content_block_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">Your</span><span class="w"> </span><span class="err">newly</span><span class="w"> </span><span class="err">generated</span><span class="w"> </span><span class="err">block</span><span class="w"> </span><span class="err">id</span><span class="p">,</span><span class="w">
  </span><span class="nl">"liquid_tag"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">generated</span><span class="w"> </span><span class="err">block</span><span class="w"> </span><span class="err">tag</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
  </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Content</span><span class="w"> </span><span class="err">Block</span><span class="w"> </span><span class="err">was</span><span class="w"> </span><span class="err">created</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="p">,</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">Content cannot be blank</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content must be a string</code></td>
      <td>Make sure your content is encapsulated in quotes (<code class="language-plaintext highlighter-rouge">""</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content must be smaller than 50kb</code></td>
      <td>The content in your Content Block must be less than 50 KB total.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content contains malformed liquid</code></td>
      <td>The Liquid provided is not valid or parsable. Try again with valid Liquid or contact support.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block cannot be referenced within itself</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block description cannot be blank</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block description must be a string</code></td>
      <td>Make sure your Content Block description is encapsulated in quotes (<code class="language-plaintext highlighter-rouge">""</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block description must be shorter than 250 characters</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block name cannot be blank</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block name must be shorter than 100 characters</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block name can only contain alphanumeric characters</code></td>
      <td>Content Block names can include any of the following characters: the letters (capitalized or lowercase) <code class="language-plaintext highlighter-rouge">A</code> through <code class="language-plaintext highlighter-rouge">Z</code>, the numbers <code class="language-plaintext highlighter-rouge">0</code> through <code class="language-plaintext highlighter-rouge">9</code>, dashes <code class="language-plaintext highlighter-rouge">-</code>, and underscores <code class="language-plaintext highlighter-rouge">_</code>. It cannot contain non-alphanumeric characters like emojis, <code class="language-plaintext highlighter-rouge">!</code>, <code class="language-plaintext highlighter-rouge">@</code>, <code class="language-plaintext highlighter-rouge">~</code>, <code class="language-plaintext highlighter-rouge">&amp;</code>, and other “special” characters.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block with this name already exists</code></td>
      <td>Try a different name.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block name cannot be updated for active Content Blocks</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Content Block state must be either active or draft</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Active Content Block can not be updated to Draft. Create a new Content Block.</code></td>
      <td> </td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Tags must be an array</code></td>
      <td>Tags must be formatted as an array of strings, for example <code class="language-plaintext highlighter-rouge">["marketing", "promotional", "transactional"]</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">All tags must be strings</code></td>
      <td>Make sure your tags are encapsulated in quotes (<code class="language-plaintext highlighter-rouge">""</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">Some tags could not be found</code></td>
      <td>To add a tag when creating a Content Block, the tag must already exist in Braze.</td>
    </tr>
  </tbody>
</table>

</div>
