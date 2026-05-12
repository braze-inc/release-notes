<div id='api_mzijplaaxvyh' class='api_div'>
<h1 id="send-campaign-messages-using-api-triggered-delivery">Send campaign messages using API-triggered delivery</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/campaigns/trigger/send</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to send immediate, one-off messages to designated users using API-triggered delivery.</p>
</blockquote>

<p>API-triggered delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom using your API.</p>

<p>If you’re targeting a segment, a record of your request is stored in the <a href="https://dashboard.braze.com/app_settings/developer_console/activitylog/">Developer Console</a>. To send messages with this endpoint, you must have a <a href="/docs/api/identifier_types/">campaign ID</a> created when you build an <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery">API-triggered campaign</a>.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need to generate an API key with the <code class="language-plaintext highlighter-rouge">campaigns.trigger.send</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-body">Request body</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
</pre></td></tr></tbody></table></code></pre></div></div>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"campaign_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"send_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">send</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"trigger_properties"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">personalization</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">apply</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">all</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w">
  </span><span class="nl">"broadcast"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">broadcast</span><span class="w"> </span><span class="err">--</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">false</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="mi">8</span><span class="err">/</span><span class="mi">31</span><span class="err">/</span><span class="mi">17</span><span class="p">,</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">true</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="s2">"recipients"</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">omitted</span><span class="p">,</span><span class="w">
  </span><span class="nl">"audience"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">connected</span><span class="w"> </span><span class="err">audience</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">connected</span><span class="w"> </span><span class="err">audience</span><span class="p">,</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">Including</span><span class="w"> </span><span class="err">'audience'</span><span class="w"> </span><span class="err">sends</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">audience</span><span class="w">
  </span><span class="nl">"recipients"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array;</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">provided</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">broadcast</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">`</span><span class="kc">false</span><span class="err">`</span><span class="p">,</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">sends</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">entire</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">targeted</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign)</span><span class="w">
    </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
      </span><span class="err">//</span><span class="w"> </span><span class="err">Either</span><span class="w"> </span><span class="s2">"external_user_id"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"user_alias"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"email"</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">required.</span><span class="w"> </span><span class="err">Requests</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">specify</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">one.</span><span class="w">
      </span><span class="nl">"user_alias"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">receive</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
      </span><span class="nl">"external_user_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">external</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">receive</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
      </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">address</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">receive</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w">
      </span><span class="nl">"prioritization"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array)</span><span class="w"> </span><span class="err">prioritization</span><span class="w"> </span><span class="err">array;</span><span class="w"> </span><span class="err">required</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">using</span><span class="w"> </span><span class="err">email</span><span class="p">,</span><span class="w">
      </span><span class="nl">"trigger_properties"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">personalization</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">apply</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">(these</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="w"> </span><span class="err">override</span><span class="w"> </span><span class="err">any</span><span class="w"> </span><span class="err">keys</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">conflict</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">parent</span><span class="w"> </span><span class="err">trigger_properties)</span><span class="p">,</span><span class="w">
      </span><span class="nl">"send_to_existing_only"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w"> </span><span class="err">can't</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">aliases;</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">`</span><span class="kc">false</span><span class="err">`</span><span class="p">,</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">object</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">also</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">included</span><span class="p">,</span><span class="w">
      </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="w"> </span><span class="err">fields</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">object</span><span class="w"> </span><span class="err">create</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">update</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">given</span><span class="w"> </span><span class="err">value</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">specified</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">profile</span><span class="w"> </span><span class="err">before</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">sent</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">existing</span><span class="w"> </span><span class="err">values</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">overwritten</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"attachments"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array)</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">JSON</span><span class="w"> </span><span class="err">objects</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">define</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">files</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">need</span><span class="w"> </span><span class="err">attached</span><span class="p">,</span><span class="w"> </span><span class="err">defined</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="s2">"file_name"</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="s2">"url"</span><span class="p">,</span><span class="w">
    </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
       </span><span class="nl">"file_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">want</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">attach</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">email</span><span class="p">,</span><span class="w"> </span><span class="err">excluding</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">extension</span><span class="w"> </span><span class="err">(for</span><span class="w"> </span><span class="err">example</span><span class="p">,</span><span class="w"> </span><span class="s2">".pdf"</span><span class="err">).</span><span class="w"> </span><span class="err">Attach</span><span class="w"> </span><span class="err">files</span><span class="w"> </span><span class="err">up</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="mi">2</span><span class="w"> </span><span class="err">MB.</span><span class="w"> </span><span class="err">This</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">required</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">use</span><span class="w"> </span><span class="s2">"attachments"</span><span class="p">,</span><span class="w">
       </span><span class="nl">"url"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">corresponding</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">want</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">attach</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">email.</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">name's</span><span class="w"> </span><span class="err">extension</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">detected</span><span class="w"> </span><span class="err">automatically</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">defined</span><span class="p">,</span><span class="w"> </span><span class="err">which</span><span class="w"> </span><span class="err">should</span><span class="w"> </span><span class="err">return</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">appropriate</span><span class="w"> </span><span class="s2">"Content-Type"</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">response</span><span class="w"> </span><span class="err">header.</span><span class="w"> </span><span class="err">This</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">required</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">use</span><span class="w"> </span><span class="s2">"attachments"</span><span class="p">,</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">]</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">campaign_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">campaign identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">send_id</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">send identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">trigger_properties</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>See <a href="/docs/api/objects_filters/trigger_properties_object/">trigger properties</a>. Personalization key-value pairs apply to all users in this request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">broadcast</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>You must set <code class="language-plaintext highlighter-rouge">broadcast</code> to true when sending a message to the entire segment configured as the campaign’s target audience in the Braze dashboard. This parameter defaults to false (as of August 31, 2017). <br /><br /> If <code class="language-plaintext highlighter-rouge">broadcast</code> is set to true, a <code class="language-plaintext highlighter-rouge">recipients</code> list cannot be included. However, use caution when setting <code class="language-plaintext highlighter-rouge">broadcast: true</code>, as unintentionally setting this flag may cause you to send your message to a larger-than-expected audience.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">audience</code></td>
      <td>Optional</td>
      <td>Connected audience object</td>
      <td>See <a href="/docs/api/objects_filters/connected_audience/">connected audience</a>. When you include <code class="language-plaintext highlighter-rouge">audience</code>, the message is sent only to users who match the defined filters, such as custom attributes and subscription statuses.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">recipients</code></td>
      <td>Optional</td>
      <td>Array</td>
      <td>See <a href="/docs/api/objects_filters/recipient_object/">recipients object</a>.<br /><br />If <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> is <code class="language-plaintext highlighter-rouge">false</code>, an <code class="language-plaintext highlighter-rouge">attributes</code> object must be included.<br /><br />You can update a user’s subscription group status by including <code class="language-plaintext highlighter-rouge">subscription_groups</code> in the nested <code class="language-plaintext highlighter-rouge">attributes</code> object. For more details, refer to <a href="/docs/api/objects_filters/user_attributes_object">User attributes object</a>.<br /><br />If <code class="language-plaintext highlighter-rouge">recipients</code> is not provided and <code class="language-plaintext highlighter-rouge">broadcast</code> is set to true, the message is sent to the entire segment configured as the campaign’s target audience in the Braze dashboard.<br /><br />If <code class="language-plaintext highlighter-rouge">email</code> is the identifier, you must include <a href="/docs/api/endpoints/user_data/post_user_identify#identifying-users-by-email"><code class="language-plaintext highlighter-rouge">prioritization</code></a> in the recipients object.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">attachments</code></td>
      <td>Optional</td>
      <td>Array</td>
      <td>If <code class="language-plaintext highlighter-rouge">broadcast</code> is set to true, then the <code class="language-plaintext highlighter-rouge">attachments</code> list cannot be included.</td>
    </tr>
  </tbody>
</table>

<h3 id="recipient-resolution-behavior">Recipient resolution behavior</h3>

<p>This section discusses how Braze picks a user profile for sending and what happens when one profile is not selected.</p>

<p>A user’s subscription group status can be updated using the inclusion of a <code class="language-plaintext highlighter-rouge">subscription_groups</code> parameter within the <code class="language-plaintext highlighter-rouge">attributes</code> object. For more details, refer to <a href="/docs/api/objects_filters/user_attributes_object/#migrating-push-tokens">User attributes object</a>.</p>

<h4 id="recipient-limits-and-profile-creation">Recipient limits and profile creation</h4>

<p>Learn more about how recipient limits and profile creation work for this endpoint.</p>

<ul>
  <li>The <code class="language-plaintext highlighter-rouge">recipients</code> array may contain up to 50 objects, with each object containing a single <code class="language-plaintext highlighter-rouge">external_user_id</code> string and a <code class="language-plaintext highlighter-rouge">trigger_properties</code> object.</li>
  <li>When <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> is <code class="language-plaintext highlighter-rouge">true</code> (the default), Braze sends the message only to existing users.</li>
  <li>When <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> is <code class="language-plaintext highlighter-rouge">false</code> and an <code class="language-plaintext highlighter-rouge">attributes</code> object is provided, Braze creates a new user if one doesn’t exist.</li>
  <li><strong>Net-new profiles need <code class="language-plaintext highlighter-rouge">attributes</code> with <code class="language-plaintext highlighter-rouge">send_to_existing_only: false</code>.</strong> Braze runs the pre-send create or update from the <code class="language-plaintext highlighter-rouge">attributes</code> object in the same recipient. If you set <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> to <code class="language-plaintext highlighter-rouge">false</code> but omit <code class="language-plaintext highlighter-rouge">attributes</code> (or send an empty object), Braze does not hydrate profile data the same way, so you do not get the combined “create or update user, then send” behavior this pattern is meant for.</li>
  <li><strong>Email and SMS addressing.</strong> For most Email or SMS API-triggered sends to someone who is not already in Braze, include the delivery fields you need inside <code class="language-plaintext highlighter-rouge">attributes</code> (for example <code class="language-plaintext highlighter-rouge">email</code>, or the phone attributes your workspace uses for SMS). You can also set subscription group membership or subscription status there when opt-in state must change in the same call.</li>
  <li><strong>Campaign eligibility.</strong> After the profile exists or updates, that user must still match the campaign’s dashboard target audience and channel send rules (for example opted in for email) or Braze does not send the message.</li>
  <li>Setting <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> to <code class="language-plaintext highlighter-rouge">false</code> is not supported for user aliases. New alias-only users can’t be created through this endpoint. To send to an alias-only user, that user must already exist in Braze.</li>
</ul>

<h4 id="email-identifier-and-prioritization-ties">Email identifier and prioritization ties</h4>

<p>When you identify recipients by email, Braze uses <code class="language-plaintext highlighter-rouge">prioritization</code>. Braze sends only when <code class="language-plaintext highlighter-rouge">prioritization</code> returns one profile.</p>

<ul>
  <li>If you use <code class="language-plaintext highlighter-rouge">email</code> as the identifier, Braze resolves the recipient using <code class="language-plaintext highlighter-rouge">prioritization</code>.</li>
  <li>If <code class="language-plaintext highlighter-rouge">prioritization</code> returns a tie, Braze does not send.</li>
  <li>Braze sends after the tie is broken and <code class="language-plaintext highlighter-rouge">prioritization</code> returns one profile. For example, if profile updates change one user’s ordering fields, Braze sends once <code class="language-plaintext highlighter-rouge">prioritization</code> can uniquely identify a profile (see <a href="#retry-behavior-and-send_to_existing_only">Retry behavior and <code class="language-plaintext highlighter-rouge">send_to_existing_only</code></a>).</li>
  <li>Braze also does not send when <code class="language-plaintext highlighter-rouge">prioritization</code> returns no profiles.</li>
</ul>

<h4 id="retry-behavior-and-send_to_existing_only">Retry behavior and send_to_existing_only</h4>

<p>Learn what happens when <code class="language-plaintext highlighter-rouge">prioritization</code> does not return exactly one profile.</p>

<ul>
  <li>When <code class="language-plaintext highlighter-rouge">prioritization</code> does not return exactly one user profile, Braze retries resolution up to 40 times. This retry behavior is expected.</li>
  <li>The <code class="language-plaintext highlighter-rouge">send_to_existing_only</code> setting does not change <code class="language-plaintext highlighter-rouge">prioritization</code> tie behavior. The same tie and retry behavior applies whether this setting is <code class="language-plaintext highlighter-rouge">true</code> or <code class="language-plaintext highlighter-rouge">false</code>.</li>
</ul>

<p><strong>Note:</strong></p>

<p>The <code class="language-plaintext highlighter-rouge">segment_id</code> parameter is not supported for this endpoint. To target a segment, configure the segment in the campaign’s target audience settings in the Braze dashboard and use <code class="language-plaintext highlighter-rouge">"broadcast": true</code>, or use the <code class="language-plaintext highlighter-rouge">audience</code> parameter with <a href="/docs/api/objects_filters/connected_audience/">Connected Audience</a> filters.</p>

<h2 id="example-request">Example request</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
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
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response-details">Response details</h2>

<p>Message-sending endpoint responses include the message’s <code class="language-plaintext highlighter-rouge">dispatch_id</code> for reference back to the dispatch of the message. The <code class="language-plaintext highlighter-rouge">dispatch_id</code> is the ID of the message dispatch, a unique ID for each transmission sent from Braze. When using this endpoint, you receive a single <code class="language-plaintext highlighter-rouge">dispatch_id</code> for an entire batched set of users. For more information on <code class="language-plaintext highlighter-rouge">dispatch_id</code> check out our documentation on <a href="/docs/help/help_articles/data/dispatch_id/">Dispatch ID behavior</a>.</p>

<p>If your request encounters a fatal error, refer to <a href="/docs/api/errors/#fatal-errors">Errors and responses</a> for the error code and description.</p>

<h2 id="attributes-object-for-campaigns">Attributes object for campaigns</h2>

<p>Braze has a messaging object called <code class="language-plaintext highlighter-rouge">attributes</code> that lets you add, create, or update attributes and values for a user before you send them an API-triggered campaign. Using the <code class="language-plaintext highlighter-rouge">campaign/trigger/send</code> endpoint as this API call processes the user attributes object before it processes and sends the campaign. This helps minimize the risk of there being issues caused by <a href="/docs/user_guide/messaging/ab_testing/concepts/race_conditions/">race conditions</a>.</p>

<p><strong>Tip:</strong></p>

<p>Looking for the Canvas version of this endpoint? Check out <a href="/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint">Sending Canvas messages using API-triggered delivery</a>.</p>

</div>
