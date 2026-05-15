<div id='api_bzottevvcnhm' class='api_div'>
<h1 id="create-new-user-alias">Create new user alias</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/alias/new</p>
</div>

<blockquote>
  <p>Use this endpoint to add new user aliases for existing identified users, or to create new unidentified users.</p>
</blockquote>

<p>Up to 50 user aliases may be specified per request.</p>

<p><strong>Adding a user alias for an existing user</strong> requires an <code class="language-plaintext highlighter-rouge">external_id</code> to be included in the new user alias object. If the <code class="language-plaintext highlighter-rouge">external_id</code> is present in the object but there is no user with that <code class="language-plaintext highlighter-rouge">external_id</code>, the alias will not be added to any users. If an <code class="language-plaintext highlighter-rouge">external_id</code> is not present, a user will still be created but will need to be identified later. You can do this using the “Identifying Users” and the <code class="language-plaintext highlighter-rouge">users/identify</code> endpoint.</p>

<p><strong>Creating a new alias-only user</strong> requires the <code class="language-plaintext highlighter-rouge">external_id</code> to be omitted from the new user alias object. After the user is created, use the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint to associate the alias-only user with attributes, events, and purchases, and the <code class="language-plaintext highlighter-rouge">/users/identify</code> endpoint to identify the user with an <code class="language-plaintext highlighter-rouge">external_id</code>.</p>

<h2 id="when-alias_label-and-alias_name-already-exist">When <code class="language-plaintext highlighter-rouge">alias_label</code> and <code class="language-plaintext highlighter-rouge">alias_name</code> already exist</h2>

<p>The combination of <code class="language-plaintext highlighter-rouge">alias_label</code> and <code class="language-plaintext highlighter-rouge">alias_name</code> must be unique across your user base. For more information, see <a href="/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases">User aliases</a>.</p>

<p>If you send a request where the <code class="language-plaintext highlighter-rouge">alias_label</code> and <code class="language-plaintext highlighter-rouge">alias_name</code> pair already exists for any user (whether on the same user or another), the endpoint still returns a successful response (for example, <code class="language-plaintext highlighter-rouge">"aliases_processed": 1</code>, <code class="language-plaintext highlighter-rouge">"message": "success"</code>). In that case, no new alias is added to the user in the request. Because the <code class="language-plaintext highlighter-rouge">alias_label</code> and <code class="language-plaintext highlighter-rouge">alias_name</code> pair is already in use, the request does not make any changes, and it can appear that the alias was never added to the user in question.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.alias.new</code> permission.</p>

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
  </span><span class="nl">"user_aliases"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">new</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">object)</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="request-parameters">Request parameters</h3>

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
      <td><code class="language-plaintext highlighter-rouge">user_aliases</code></td>
      <td>Required</td>
      <td>Array of new user alias objects</td>
      <td>See <a href="/docs/api/objects_filters/user_alias_object/">user alias object</a>.<br /><br /> For more information on <code class="language-plaintext highlighter-rouge">alias_name</code> and <code class="language-plaintext highlighter-rouge">alias_label</code>, check out our <a href="/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases">User Aliases</a> documentation.</td>
    </tr>
  </tbody>
</table>

<h3 id="endpoint-request-body-with-new-user-alias-object-specification">Endpoint request body with new user alias object specification</h3>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"external_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"alias_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"alias_label"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w">
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>When an alias is skipped because the same <code class="language-plaintext highlighter-rouge">alias_label</code> and <code class="language-plaintext highlighter-rouge">alias_name</code> already exist for a user, the response body may still indicate success. See <a href="#when-the-alias-label-and-name-already-exist">When the alias label and name already exist</a> for details.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"aliases_processed"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>

