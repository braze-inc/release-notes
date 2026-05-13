<div id='api_nsyjrverlrlc' class='api_div'>
<h1 id="export-campaign-details">Export campaign details</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/campaigns/details</p>
</div>

<blockquote>
  <p>Use this endpoint to retrieve relevant information on a specified campaign, which can be identified by the <code class="language-plaintext highlighter-rouge">campaign_id</code>.</p>
</blockquote>

<p>If you want to retrieve Canvas data, refer to the <a href="/docs/api/endpoints/export/canvas/get_canvas_details/">Export Canvas details</a> endpoint.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aad2a811-7237-43b1-9d64-32042eabecd9" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">campaigns.details</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">campaign_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">campaign API identifier</a>.<br /><br /> The <code class="language-plaintext highlighter-rouge">campaign_id</code> for API campaigns can be found on the <a href="/docs/user_guide/administer/global/workspace_settings/apis_and_identifiers/">API Keys</a> page and the <strong>Campaign Details</strong> page within your dashboard; or you can use the <a href="#campaign-list-endpoint">Export campaigns list endpoint</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">post_launch_draft_version</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>For messages that have a post-launch draft, setting this to <code class="language-plaintext highlighter-rouge">true</code> shows any draft changes available. Defaults to <code class="language-plaintext highlighter-rouge">false</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_has_translatable_content</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>When set to <code class="language-plaintext highlighter-rouge">true</code>, the API response includes a <code class="language-plaintext highlighter-rouge">has_translatable_content</code> field for each message. Defaults to <code class="language-plaintext highlighter-rouge">false</code>.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/details?campaign_id={{campaign_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="responses">Responses</h2>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"created_at"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">created</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
    </span><span class="nl">"updated_at"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">updated</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
    </span><span class="nl">"archived"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">archived</span><span class="p">,</span><span class="w">
    </span><span class="nl">"draft"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">draft</span><span class="p">,</span><span class="w">
    </span><span class="nl">"enabled"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">active</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">not</span><span class="p">,</span><span class="w">
    </span><span class="nl">"has_post_launch_draft"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">post-launch</span><span class="w"> </span><span class="err">draft</span><span class="p">,</span><span class="w">
    </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
    </span><span class="nl">"description"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">description</span><span class="p">,</span><span class="w">
    </span><span class="nl">"schedule_type"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">type</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">scheduling</span><span class="w"> </span><span class="err">action</span><span class="p">,</span><span class="w">
    </span><span class="nl">"channels"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">channels</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">via</span><span class="p">,</span><span class="w">
    </span><span class="nl">"first_sent"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">hour</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">first</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
    </span><span class="nl">"last_sent"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">hour</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
    </span><span class="nl">"tags"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">tag</span><span class="w"> </span><span class="err">names</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="p">,</span><span class="w">
    </span><span class="nl">"teams"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">names</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Teams</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="p">,</span><span class="w">
    </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"message_variation_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="err">//</span><span class="w"> </span><span class="err">&lt;=This</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">actual</span><span class="w"> </span><span class="err">id</span><span class="w">
            </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">channel</span><span class="w"> </span><span class="err">type</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">either</span><span class="w"> </span><span class="err">email</span><span class="p">,</span><span class="w"> </span><span class="err">ios_push</span><span class="p">,</span><span class="w"> </span><span class="err">webhook</span><span class="p">,</span><span class="w"> </span><span class="err">content_card</span><span class="p">,</span><span class="w"> </span><span class="err">in-app_message</span><span class="p">,</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">sms</span><span class="p">,</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">dashboard</span><span class="w"> </span><span class="err">(for</span><span class="w"> </span><span class="err">example</span><span class="p">,</span><span class="w"> </span><span class="s2">"Variation 1"</span><span class="err">)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"has_translatable_content"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">translatable</span><span class="w"> </span><span class="err">content</span><span class="w"> </span><span class="err">(only</span><span class="w"> </span><span class="err">present</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">`include_has_translatable_content`</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="kc">true</span><span class="err">);</span><span class="w"> </span><span class="err">`</span><span class="kc">true</span><span class="err">`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">locales</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">configured</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">contains</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">least</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">translation</span><span class="w"> </span><span class="err">tag;</span><span class="w"> </span><span class="err">`</span><span class="kc">false</span><span class="err">`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">no</span><span class="w"> </span><span class="err">locales</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">configured</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">no</span><span class="w"> </span><span class="err">translation</span><span class="w"> </span><span class="err">tags</span><span class="w"> </span><span class="err">detected;</span><span class="w"> </span><span class="err">`</span><span class="kc">null</span><span class="err">`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">detection</span><span class="w"> </span><span class="err">could</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">completed</span><span class="p">,</span><span class="w">
            </span><span class="err">...</span><span class="w"> </span><span class="err">channel-specific</span><span class="w"> </span><span class="err">fields</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">following</span><span class="w"> </span><span class="err">messages</span><span class="w"> </span><span class="err">section</span><span class="w"> </span><span class="err">...</span><span class="w">
        </span><span class="p">}</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"conversion_behaviors"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">conversion</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">behaviors</span><span class="w"> </span><span class="err">assigned</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="p">,</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">following</span><span class="w"> </span><span class="err">conversions</span><span class="w"> </span><span class="err">behavior</span><span class="w"> </span><span class="err">section.</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="messages-by-channel">Messages by channel</h3>

<p>The <code class="language-plaintext highlighter-rouge">messages</code> response will contain information about each message. The following includes example message responses for each channel:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"content_cards"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
    </span><span class="nl">"extras"</span><span class="p">:</span><span class="w"> </span><span class="err">(hash)</span><span class="w"> </span><span class="err">any</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">provided;</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">present</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">least</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pair</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">been</span><span class="w"> </span><span class="err">set</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"email"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
    </span><span class="nl">"extras"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">extras</span><span class="p">,</span><span class="w">
    </span><span class="nl">"subject"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">subject</span><span class="p">,</span><span class="w">
    </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">HTML</span><span class="w"> </span><span class="err">body</span><span class="p">,</span><span class="w">
    </span><span class="nl">"from"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">address</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">display</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
    </span><span class="nl">"reply_to"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">reply-to</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">different</span><span class="w"> </span><span class="err">than</span><span class="w"> </span><span class="s2">"from"</span><span class="w"> </span><span class="err">address</span><span class="p">,</span><span class="w">
    </span><span class="nl">"title"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="p">,</span><span class="w">
    </span><span class="nl">"amp_body"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">AMP</span><span class="w"> </span><span class="err">HTML</span><span class="w"> </span><span class="err">body</span><span class="p">,</span><span class="w">
    </span><span class="nl">"preheader"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">preheader</span><span class="p">,</span><span class="w">
    </span><span class="nl">"custom_plain_text"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">plain</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w">
    </span><span class="nl">"should_inline_css"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">there</span><span class="w"> </span><span class="err">should</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">inline</span><span class="w"> </span><span class="err">CSS</span><span class="p">,</span><span class="w">
    </span><span class="nl">"should_whitespace_header"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">there</span><span class="w"> </span><span class="err">should</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">whitespace</span><span class="w"> </span><span class="err">header</span><span class="p">,</span><span class="w">
    </span><span class="nl">"email_headers"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">headers</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>The response format depends on the type of in-app message. Survey in-app messages return <code class="language-plaintext highlighter-rouge">type</code> and <code class="language-plaintext highlighter-rouge">data</code> fields. Other in-app message types (slideup, modal, and fullscreen) return <code class="language-plaintext highlighter-rouge">name</code>, <code class="language-plaintext highlighter-rouge">message</code>, and <code class="language-plaintext highlighter-rouge">extras</code> fields.</p>

<h4 id="surveys">Surveys</h4>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">description</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">in-app</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">type</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="s2">"survey"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"pages"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"header"</span><span class="p">:</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                         </span><span class="nl">"text"</span><span class="p">:</span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">display</span><span class="w"> </span><span class="err">text</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">header</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">survey</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="nl">"choices"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                       </span><span class="nl">"choice_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">choice</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
                       </span><span class="nl">"text"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">display</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w">
                       </span><span class="nl">"custom_attribute_key"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">key</span><span class="p">,</span><span class="w">
                       </span><span class="nl">"custom_attribute_value"</span><span class="p">:</span><span class="w"> </span><span class="err">(sting)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">value</span><span class="p">,</span><span class="w">
                       </span><span class="nl">"deleted"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">deleted</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">live</span><span class="w"> </span><span class="err">campaign</span><span class="w">
                    </span><span class="p">},</span><span class="w">
                    </span><span class="err">...</span><span class="w">
                </span><span class="p">]</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">]</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h4 id="slideup-modal-fullscreen-in-app-messages">Slideup, modal, fullscreen in-app messages</h4>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"in_app_message"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">optional)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w">
    </span><span class="nl">"extras"</span><span class="p">:</span><span class="w"> </span><span class="err">(hash</span><span class="p">,</span><span class="w"> </span><span class="err">optional)</span><span class="w"> </span><span class="err">any</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">provided;</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">present</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">least</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pair</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">been</span><span class="w"> </span><span class="err">set</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">description</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">channel</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="s2">"ios_push"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"android_push"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
    </span><span class="nl">"alert"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">alert</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w">
    </span><span class="nl">"extras"</span><span class="p">:</span><span class="w"> </span><span class="err">(hash)</span><span class="w"> </span><span class="err">any</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">provided</span><span class="p">,</span><span class="w">
    </span><span class="nl">"title"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">alert</span><span class="w"> </span><span class="err">title</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w">
    </span><span class="nl">"action"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">action</span><span class="w"> </span><span class="err">link</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">click</span><span class="p">,</span><span class="w">
    </span><span class="nl">"image_url"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">image</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">Android</span><span class="w"> </span><span class="err">notification</span><span class="w"> </span><span class="err">image</span><span class="p">,</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">iOS</span><span class="w"> </span><span class="err">notification</span><span class="w"> </span><span class="err">image</span><span class="p">,</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">Web</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">icon</span><span class="w"> </span><span class="err">image</span><span class="p">,</span><span class="w">
    </span><span class="nl">"large_image_url"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">web</span><span class="w"> </span><span class="err">notification</span><span class="w"> </span><span class="err">image</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">Android</span><span class="w"> </span><span class="err">Chrome</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">Windows</span><span class="w"> </span><span class="err">web</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">actions;</span><span class="w"> </span><span class="kc">null</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">other</span><span class="w"> </span><span class="err">cases</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sms"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">payload</span><span class="w"> </span><span class="err">body</span><span class="p">,</span><span class="w">
  </span><span class="nl">"from"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">numbers</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="p">,</span><span class="w">
  </span><span class="nl">"subscription_group_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">id</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">targeted</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">SMS</span><span class="w"> </span><span class="err">message</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"webhook"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"url"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">webhook</span><span class="p">,</span><span class="w">
    </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">payload</span><span class="w"> </span><span class="err">body</span><span class="p">,</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">content</span><span class="w"> </span><span class="err">type</span><span class="p">,</span><span class="w">
    </span><span class="nl">"headers"</span><span class="p">:</span><span class="w"> </span><span class="err">(hash)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">specified</span><span class="w"> </span><span class="err">request</span><span class="w"> </span><span class="err">headers</span><span class="p">,</span><span class="w">
    </span><span class="nl">"method"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">HTTP</span><span class="w"> </span><span class="err">method</span><span class="p">,</span><span class="w"> </span><span class="err">either</span><span class="w"> </span><span class="err">POST</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">GET</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h4 id="template-messages">Template messages</h4>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"whats_app"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"subscription_group_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">selected</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">WhatsApp</span><span class="w"> </span><span class="err">message</span><span class="w">
  </span><span class="nl">"from"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">numbers</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="p">,</span><span class="w">
  </span><span class="nl">"template_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">WhatsApp</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
  </span><span class="nl">"template_language_code"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">language</span><span class="w"> </span><span class="err">code</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">WhatsApp</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
  </span><span class="nl">"header_variables"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">present</span><span class="p">,</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">Liquid</span><span class="w"> </span><span class="err">variables</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">inserted</span><span class="w"> </span><span class="err">into</span><span class="w"> </span><span class="err">header</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">WhatsApp</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
  </span><span class="nl">"body_variables"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">present</span><span class="p">,</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">Liquid</span><span class="w"> </span><span class="err">variables</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">inserted</span><span class="w"> </span><span class="err">into</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">WhatsApp</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
  </span><span class="nl">"button_variables"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">present</span><span class="p">,</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">Liquid</span><span class="w"> </span><span class="err">variables</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">inserted</span><span class="w"> </span><span class="err">into</span><span class="w"> </span><span class="err">buttons</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">WhatsApp</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h4 id="response-messages">Response messages</h4>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"whats_app"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"subscription_group_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">ID</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">selected</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">WhatsApp</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
  </span><span class="nl">"from"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">numbers</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">group</span><span class="p">,</span><span class="w">
  </span><span class="nl">"layout"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">WhatsApp</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">(text</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">media</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">quick-reply)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"header_text"</span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">optional)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">present</span><span class="p">,</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">header</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
  </span><span class="nl">"body_text"</span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">optional)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">present</span><span class="p">,</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
  </span><span class="nl">"footer_text"</span><span class="p">:</span><span class="w"> </span><span class="err">(string</span><span class="p">,</span><span class="w"> </span><span class="err">optional)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">text</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">present</span><span class="p">,</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">footer</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="p">,</span><span class="w">
  </span><span class="nl">"buttons"</span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">list</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">button</span><span class="w"> </span><span class="err">objects</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">being</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">(</span><span class="p">{</span><span class="nl">"text"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">text</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">button</span><span class="p">}</span><span class="err">)</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">description</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">channel</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">control</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">for</span><span class="p">,</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"control"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="conversion-behaviors">Conversion behaviors</h3>

<p>The <code class="language-plaintext highlighter-rouge">conversion_behaviors</code> array contains information about each conversion event behavior set for the campaign. These behaviors are in order as set by the campaign. For example, Conversion Event A is the first item in the array, Conversion Event B is the second, and so on. The following lists example conversion event behavior responses:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Clicks Email"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"window"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">seconds</span><span class="w"> </span><span class="err">during</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">can</span><span class="w"> </span><span class="err">convert</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="mi">86400</span><span class="p">,</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="mi">24</span><span class="w"> </span><span class="err">hours</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Opens Email"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"window"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">seconds</span><span class="w"> </span><span class="err">during</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">can</span><span class="w"> </span><span class="err">convert</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="mi">86400</span><span class="p">,</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="mi">24</span><span class="w"> </span><span class="err">hours</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Makes Any Purchase"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"window"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">seconds</span><span class="w"> </span><span class="err">during</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">can</span><span class="w"> </span><span class="err">convert</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="mi">86400</span><span class="p">,</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="mi">24</span><span class="w"> </span><span class="err">hours</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Makes Specific Purchase"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"window"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">seconds</span><span class="w"> </span><span class="err">during</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">can</span><span class="w"> </span><span class="err">convert</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="mi">86400</span><span class="p">,</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="mi">24</span><span class="w"> </span><span class="err">hours</span><span class="p">,</span><span class="w">
    </span><span class="nl">"product"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">product</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="s2">"Feline Body Armor"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Performs Custom Event"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"window"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">seconds</span><span class="w"> </span><span class="err">during</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">can</span><span class="w"> </span><span class="err">convert</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="mi">86400</span><span class="p">,</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="mi">24</span><span class="w"> </span><span class="err">hours</span><span class="p">,</span><span class="w">
    </span><span class="nl">"custom_event_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="s2">"Used Feline Body Armor"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Upgrades App"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"window"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">seconds</span><span class="w"> </span><span class="err">during</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">can</span><span class="w"> </span><span class="err">convert</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="mi">86400</span><span class="p">,</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="mi">24</span><span class="w"> </span><span class="err">hours</span><span class="p">,</span><span class="w">
    </span><span class="nl">"app_ids"</span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="kc">null</span><span class="err">)</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">ids</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="p">[</span><span class="s2">"12345"</span><span class="p">,</span><span class="w"> </span><span class="s2">"67890"</span><span class="p">],</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">`</span><span class="kc">null</span><span class="err">`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="s2">"Track sessions for any app"</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">selected</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">UI</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Starts Session"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"window"</span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">seconds</span><span class="w"> </span><span class="err">during</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">can</span><span class="w"> </span><span class="err">convert</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">event</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="mi">86400</span><span class="p">,</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="mi">24</span><span class="w"> </span><span class="err">hours</span><span class="p">,</span><span class="w">
    </span><span class="nl">"app_ids"</span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="kc">null</span><span class="err">)</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">ids</span><span class="p">,</span><span class="w"> </span><span class="err">such</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="p">[</span><span class="s2">"12345"</span><span class="p">,</span><span class="w"> </span><span class="s2">"67890"</span><span class="p">],</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">`</span><span class="kc">null</span><span class="err">`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="s2">"Track sessions for any app"</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">selected</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">UI</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
