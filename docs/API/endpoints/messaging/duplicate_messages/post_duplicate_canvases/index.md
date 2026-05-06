<div id='api_rcnankcfhruv' class='api_div'>
<h1 id="duplicate-canvases-using-the-api">Duplicate Canvases using the API</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/canvas/duplicate</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to duplicate Canvases. This API endpoint is similar to <a href="/docs/user_guide/engagement_tools/messaging_fundamentals/duplicating">duplicating Canvases in the Braze dashboard</a>.</p>
</blockquote>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you must generate an API key with the <code class="language-plaintext highlighter-rouge">canvas.duplicate</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is limited to 100 API calls per minute.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"canvas_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">Canvas</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">resulting</span><span class="w"> </span><span class="err">Canvas</span><span class="p">,</span><span class="w">
  </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">description</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">resulting</span><span class="w"> </span><span class="err">Canvas</span><span class="p">,</span><span class="w">
  </span><span class="nl">"tag_names"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">tags</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">resulting</span><span class="w"> </span><span class="err">Canvas</span><span class="p">,</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">canvas_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>See <a href="https://www.braze.com/docs/api/identifier_types/">Canvas identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The name of the resulting Canvas.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">description</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The description field for the resulting Canvas.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">tag_names</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The tags for the resulting Canvas. These must be existing tags. If you add new tags in the request, they will overwrite any tags that were on the original Canvas.</td>
    </tr>
  </tbody>
</table>

<h2 id="response">Response</h2>

<p>This endpoint will return a <code class="language-plaintext highlighter-rouge">202</code> status code, and the Canvas creation will occur asynchronously. You can use the <a href="/docs/user_guide/administrative/app_settings/company_settings/security_settings">Security event download</a> to see records of when Canvases were duplicated and by which API key.</p>

</div>
