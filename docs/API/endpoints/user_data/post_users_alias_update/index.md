<div id='api_sudvjlzggxao' class='api_div'>
<h1 id="update-user-alias">Update user alias</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/alias/update</p>
</div>

<blockquote>
  <p>Use this endpoint to update existing user aliases.</p>
</blockquote>

<p>Up to 50 user aliases may be specified per request.</p>

<p>Updating a user alias requires <code class="language-plaintext highlighter-rouge">alias_label</code>, <code class="language-plaintext highlighter-rouge">old_alias_name</code>, and <code class="language-plaintext highlighter-rouge">new_alias_name</code> to be included in the update user alias object. If there is no user alias associated with the <code class="language-plaintext highlighter-rouge">alias_label</code> and <code class="language-plaintext highlighter-rouge">old_alias_name</code>, no alias will be updated. If the given <code class="language-plaintext highlighter-rouge">alias_label</code> and <code class="language-plaintext highlighter-rouge">old_alias_name</code> is found, then the <code class="language-plaintext highlighter-rouge">old_alias_name</code> will be updated to the <code class="language-plaintext highlighter-rouge">new_alias_name</code>.</p>

<p><strong>Note:</strong></p>

<p>This endpoint does not guarantee the sequence of <code class="language-plaintext highlighter-rouge">alias_updates</code> objects being updated.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.alias.update</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"alias_updates"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">update</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">object)</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="request-parameters">Request parameters</h3>

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
      <td><code class="language-plaintext highlighter-rouge">alias_updates</code></td>
      <td>Required</td>
      <td>Array of update user alias objects</td>
      <td>See <a href="/docs/api/objects_filters/user_alias_object/">user alias object</a>.<br /><br /> For more information on <code class="language-plaintext highlighter-rouge">old_alias_name</code>, <code class="language-plaintext highlighter-rouge">new_alias_name</code>, and <code class="language-plaintext highlighter-rouge">alias_label</code>, refer to <a href="/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases">User aliases</a>.</td>
    </tr>
  </tbody>
</table>

<h3 id="endpoint-request-body-with-update-user-alias-object-specification">Endpoint request body with update user alias object specification</h3>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"alias_label"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"old_alias_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"new_alias_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

</div>

