<div id='api_roxybbaiiwog' class='api_div'>
<h1 id="export-canvas-details">Export Canvas details</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/canvas/details</p>
</div>

<blockquote>
  <p>Use this endpoint to export metadata about a Canvas, such as the name, time created, current status, and more.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5188873c-13a3-4aaf-a54b-9fa1daeac5f8" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">canvas.details</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">canvas_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">Canvas API Identifier</a></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">post_launch_draft_version</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>For Canvases that have a post-launch draft, setting this to <code class="language-plaintext highlighter-rouge">true</code> shows any draft changes available. Defaults to <code class="language-plaintext highlighter-rouge">false</code>.</td>
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
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/details?canvas_id={{canvas_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="responses">Responses</h2>

<p><strong>Note:</strong></p>

<p>All Canvas steps have a <code class="language-plaintext highlighter-rouge">next_paths</code> field, which is an array of <code class="language-plaintext highlighter-rouge">{name, next_step_id}</code> data. For Message steps, the <code class="language-plaintext highlighter-rouge">next_step_ids</code> field will be present, but will not contain data for other Canvas steps.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">created</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
  </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">updated</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
  </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">description</span><span class="p">,</span><span class="w">
  </span><span class="nl">"archived"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">archived</span><span class="p">,</span><span class="w">
  </span><span class="nl">"draft"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">draft</span><span class="p">,</span><span class="w">
  </span><span class="nl">"enabled"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">active</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">not</span><span class="p">,</span><span class="w">
  </span><span class="nl">"has_post_launch_draft"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">post-launch</span><span class="w"> </span><span class="err">draft</span><span class="p">,</span><span class="w">
  </span><span class="nl">"schedule_type"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">type</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">scheduling</span><span class="w"> </span><span class="err">action</span><span class="p">,</span><span class="w">
  </span><span class="nl">"first_entry"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">first</span><span class="w"> </span><span class="err">entry</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
  </span><span class="nl">"last_entry"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">entry</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
  </span><span class="nl">"channels"</span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">step</span><span class="w"> </span><span class="err">channels</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">Canvas</span><span class="p">,</span><span class="w">
  </span><span class="nl">"variants"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
      </span><span class="nl">"first_step_ids"</span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifiers</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">first</span><span class="w"> </span><span class="err">steps</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">variant</span><span class="p">,</span><span class="w">
      </span><span class="nl">"first_step_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">first</span><span class="w"> </span><span class="err">step</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">variant</span><span class="w"> </span><span class="err">(deprecated</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">November</span><span class="w"> </span><span class="mi">2017</span><span class="p">,</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">variant</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">first</span><span class="w"> </span><span class="err">step)</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">variations)</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">tag</span><span class="w"> </span><span class="err">names</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="p">,</span><span class="w">
  </span><span class="nl">"teams"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">names</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Teams</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Canvas</span><span class="p">,</span><span class="w">
  </span><span class="nl">"steps"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">step</span><span class="p">,</span><span class="w">
      </span><span class="s2">"type"</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">type</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">component</span><span class="p">,</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">step</span><span class="p">,</span><span class="w">
      </span><span class="nl">"next_step_ids"</span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">IDs</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">next</span><span class="w"> </span><span class="err">steps</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">full</span><span class="w"> </span><span class="err">steps</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">Message</span><span class="w"> </span><span class="err">steps</span><span class="p">,</span><span class="w">
      </span><span class="nl">"next_paths"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">objects)</span><span class="w">
      </span><span class="err">//</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">Decision</span><span class="w"> </span><span class="err">Splits</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">property</span><span class="w"> </span><span class="err">should</span><span class="w"> </span><span class="err">evaluate</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="s2">"Yes"</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"No"</span><span class="w">
      </span><span class="err">//</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">Audience</span><span class="w"> </span><span class="err">Path</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">Action</span><span class="w"> </span><span class="err">Paths</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">property</span><span class="w"> </span><span class="err">should</span><span class="w"> </span><span class="err">evaluate</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">group</span><span class="w"> </span><span class="err">name</span><span class="w">
      </span><span class="err">//</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">Experiment</span><span class="w"> </span><span class="err">Paths</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">property</span><span class="w"> </span><span class="err">should</span><span class="w"> </span><span class="err">evaluate</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">path</span><span class="w"> </span><span class="err">name</span><span class="w">
      </span><span class="err">//</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">other</span><span class="w"> </span><span class="err">steps</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">property</span><span class="w"> </span><span class="err">should</span><span class="w"> </span><span class="err">evaluate</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="s2">"null"</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">step</span><span class="p">,</span><span class="w">
        </span><span class="nl">"next_step_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">IDs</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">next</span><span class="w"> </span><span class="err">steps</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">full</span><span class="w"> </span><span class="err">steps</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">Message</span><span class="w"> </span><span class="err">steps</span><span class="p">,</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="nl">"channels"</span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">strings)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">channels</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">step</span><span class="p">,</span><span class="w">
      </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"message_variation_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="p">{</span><span class="w">  </span><span class="err">//</span><span class="w"> </span><span class="err">&lt;=This</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">actual</span><span class="w"> </span><span class="err">id</span><span class="w">
              </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">channel</span><span class="w"> </span><span class="err">type</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">(for</span><span class="w"> </span><span class="err">example</span><span class="p">,</span><span class="w"> </span><span class="s2">"email"</span><span class="err">)</span><span class="p">,</span><span class="w">
              </span><span class="nl">"has_translatable_content"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">has</span><span class="w"> </span><span class="err">translatable</span><span class="w"> </span><span class="err">content</span><span class="w"> </span><span class="err">(only</span><span class="w"> </span><span class="err">present</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">`include_has_translatable_content`</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="kc">true</span><span class="err">);</span><span class="w"> </span><span class="err">`</span><span class="kc">true</span><span class="err">`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">locales</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">configured</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">contains</span><span class="w"> </span><span class="err">at</span><span class="w"> </span><span class="err">least</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">translation</span><span class="w"> </span><span class="err">tag;</span><span class="w"> </span><span class="err">`</span><span class="kc">false</span><span class="err">`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">no</span><span class="w"> </span><span class="err">locales</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">configured</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">no</span><span class="w"> </span><span class="err">translation</span><span class="w"> </span><span class="err">tags</span><span class="w"> </span><span class="err">detected;</span><span class="w"> </span><span class="err">`</span><span class="kc">null</span><span class="err">`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">detection</span><span class="w"> </span><span class="err">could</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">completed</span><span class="p">,</span><span class="w">
              </span><span class="err">//</span><span class="w"> </span><span class="err">channel-specific</span><span class="w"> </span><span class="err">fields</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">message</span><span class="p">,</span><span class="w"> </span><span class="err">see</span><span class="w"> </span><span class="err">Campaign</span><span class="w"> </span><span class="err">Details</span><span class="w"> </span><span class="err">endpoint</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">Response</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">example</span><span class="w"> </span><span class="err">message</span><span class="w"> </span><span class="err">responses</span><span class="w">
          </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="err">...</span><span class="w"> </span><span class="err">(more</span><span class="w"> </span><span class="err">steps)</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="messages-by-channel">Messages by channel</h3>

<p>The following is an example response that includes Canvas messages sent through different channels (email, push, SMS, and in-app messages):</p>

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
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-01T12:00:00Z"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-10T12:00:00Z"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Multi-Channel Engagement"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Complete profile reminder via multiple channels"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"archived"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
  </span><span class="nl">"draft"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
  </span><span class="nl">"enabled"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w">
  </span><span class="nl">"has_post_launch_draft"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w">
  </span><span class="nl">"schedule_type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"date"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"first_entry"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-01T12:00:00Z"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"last_entry"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-10T12:00:00Z"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"channels"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"email"</span><span class="p">,</span><span class="w"> </span><span class="s2">"push"</span><span class="p">,</span><span class="w"> </span><span class="s2">"sms"</span><span class="p">,</span><span class="w"> </span><span class="s2">"in_app_message"</span><span class="p">],</span><span class="w">
  </span><span class="nl">"variants"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Variant 1"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"variant_1_id"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"first_step_ids"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"step_1"</span><span class="p">]</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"engagement"</span><span class="p">,</span><span class="w"> </span><span class="s2">"multi-channel"</span><span class="p">],</span><span class="w">
  </span><span class="nl">"teams"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"Marketing Team"</span><span class="p">],</span><span class="w">
  </span><span class="nl">"steps"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Welcome Email"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"email"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"step_1"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"next_step_ids"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"step_2"</span><span class="p">],</span><span class="w">
      </span><span class="nl">"next_paths"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Next Step"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"next_step_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"step_2"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"channels"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"email"</span><span class="p">],</span><span class="w">
      </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"message_1"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"email"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"subject"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Welcome to Kitchenerie!"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;html&gt;&lt;body&gt;Welcome to the Kitchenerie family, !&lt;/body&gt;&lt;/html&gt;"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-01T12:00:00Z"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-01T12:00:00Z"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Follow-Up Push Notification"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"push"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"step_2"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"next_step_ids"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"step_3"</span><span class="p">],</span><span class="w">
      </span><span class="nl">"next_paths"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Next Step"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"next_step_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"step_3"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"channels"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"push"</span><span class="p">],</span><span class="w">
      </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"message_2"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"push"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"title"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Don't Forget to Complete Your Kitchenerie Profile"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Complete your Kitchenerie profile for access to special offers and local events."</span><span class="p">,</span><span class="w">
          </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-02T12:00:00Z"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-02T12:00:00Z"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Reminder SMS"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sms"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"step_3"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"next_step_ids"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"step_4"</span><span class="p">],</span><span class="w">
      </span><span class="nl">"next_paths"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Next Step"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"next_step_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"step_4"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"channels"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"sms"</span><span class="p">],</span><span class="w">
      </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"message_3"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sms"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Hi , remember to complete Kitchenerie your profile!"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-03T12:00:00Z"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-03T12:00:00Z"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"In-App Message"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"in_app_message"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"step_4"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"next_step_ids"</span><span class="p">:</span><span class="w"> </span><span class="p">[],</span><span class="w">
      </span><span class="nl">"next_paths"</span><span class="p">:</span><span class="w"> </span><span class="p">[],</span><span class="w">
      </span><span class="nl">"channels"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"in_app_message"</span><span class="p">],</span><span class="w">
      </span><span class="nl">"messages"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"message_4"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
          </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"in_app_message"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"header"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Complete Your Kitchenerie Profile"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Complete your Kitchenerie profile to unlock access to savings and local events!"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-04T12:00:00Z"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2023-01-04T12:00:00Z"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
