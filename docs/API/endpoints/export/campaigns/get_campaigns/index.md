<div id='api_kgbkpkivhoyx' class='api_div'>
<h1 id="export-campaigns-list">Export campaigns list</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/campaigns/list</p>
</div>

<blockquote>
  <p>Use this endpoint to export a list of campaigns, each of which will include its name, campaign API identifier, whether it is an API campaign, and tags associated with the campaign.</p>
</blockquote>

<p>The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f3b0b3ef-04fb-4a31-8570-e6ad88dacb18" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">campaigns.list</code> permission.</p>

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
      <td><code class="language-plaintext highlighter-rouge">page</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>The page of campaigns to return, defaults to 0 (returns the first set of up to 100).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">include_archived</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Whether or not to include archived campaigns, defaults to false.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">sort_direction</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>- Sort creation time from newest to oldest: pass in the value <code class="language-plaintext highlighter-rouge">desc</code>.<br /> - Sort creation time from oldest to newest: pass in the value <code class="language-plaintext highlighter-rouge">asc</code>. <br /><br />If <code class="language-plaintext highlighter-rouge">sort_direction</code> is not included, the default order is oldest to newest.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">last_edit.time[gt]</code></td>
      <td>Optional</td>
      <td>Time</td>
      <td>Filters the results and only returns campaigns that were edited greater than the time provided till now. Format is <code class="language-plaintext highlighter-rouge">yyyy-MM-DDTHH:mm:ss</code>.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/list?page=0&amp;include_archived=false&amp;sort_direction=desc&amp;last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
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
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"campaigns"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Campaign</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">identifier</span><span class="p">,</span><span class="w">
            </span><span class="nl">"last_edited"</span><span class="p">:</span><span class="w"> </span><span class="err">(ISO</span><span class="w"> </span><span class="mi">8601</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">last</span><span class="w"> </span><span class="err">edited</span><span class="w"> </span><span class="err">time</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">message</span><span class="w">
            </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
            </span><span class="nl">"is_api_campaign"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">campaign</span><span class="p">,</span><span class="w">
            </span><span class="nl">"tags"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(array)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">tag</span><span class="w"> </span><span class="err">names</span><span class="w"> </span><span class="err">associated</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">campaign</span><span class="w"> </span><span class="err">formatted</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">strings</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="err">...</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
