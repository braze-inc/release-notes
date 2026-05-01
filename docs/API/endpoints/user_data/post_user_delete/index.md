<div id='api_kvrklnzquvpk' class='api_div'>
<h1 id="delete-users">Delete users</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/delete</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to delete any user profile by specifying a known user identifier.</p>
</blockquote>

<p>Up to 50 <code class="language-plaintext highlighter-rouge">external_ids</code>, <code class="language-plaintext highlighter-rouge">user_aliases</code>, <code class="language-plaintext highlighter-rouge">braze_ids</code>, <code class="language-plaintext highlighter-rouge">email_addresses</code>, or <code class="language-plaintext highlighter-rouge">phone_numbers</code> can be included in a single request. Only one of <code class="language-plaintext highlighter-rouge">external_ids</code>, <code class="language-plaintext highlighter-rouge">user_aliases</code>, <code class="language-plaintext highlighter-rouge">braze_ids</code>, <code class="language-plaintext highlighter-rouge">email_addresses</code>, or <code class="language-plaintext highlighter-rouge">phone_numbers</code> can be included in a single request.</p>

<p>If you have a use case that can’t be solved with bulk user deletion through the API, contact the <a href="/docs/user_guide/administer/personal/braze_support/">Braze Support team</a> for assistance.</p>

<p><strong>Warning:</strong></p>

<p>Deleting user profiles cannot be undone. It will permanently remove users which may cause discrepancies in your data. Learn more about what happens when you <a href="/docs/help/help_articles/api/delete_user/">delete a user profile using the API</a> in our Help documentation.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#22e91d00-d178-4b4f-a3df-0073ecfcc992" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.delete</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"external_ids"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">External</span><span class="w"> </span><span class="err">IDs</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">deleted</span><span class="p">,</span><span class="w">
  </span><span class="nl">"user_aliases"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">objects)</span><span class="w"> </span><span class="err">User</span><span class="w"> </span><span class="err">aliases</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">deleted</span><span class="p">,</span><span class="w">
  </span><span class="nl">"braze_ids"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">identifiers</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">deleted</span><span class="p">,</span><span class="w">
  </span><span class="nl">"email_addresses"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">User</span><span class="w"> </span><span class="err">emails</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">deleted</span><span class="p">,</span><span class="w">
  </span><span class="nl">"phone_numbers"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">User</span><span class="w"> </span><span class="err">phone</span><span class="w"> </span><span class="err">numbers</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">deleted</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">external_ids</code></td>
      <td>Optional</td>
      <td>Array of strings</td>
      <td>External identifiers to be deleted.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_aliases</code></td>
      <td>Optional</td>
      <td>Array of user alias object</td>
      <td><a href="/docs/api/objects_filters/user_alias_object/">User aliases</a> to be deleted.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">braze_ids</code></td>
      <td>Optional</td>
      <td>Array of strings</td>
      <td>Braze user identifiers to be deleted.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">email_addresses</code></td>
      <td>Optional</td>
      <td>Array of strings</td>
      <td>User emails to be deleted. Refer to <a href="#deleting-users-by-email">Deleting users by email</a> for more information.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">phone_numbers</code></td>
      <td>Optional</td>
      <td>Array of strings</td>
      <td>User phone numbers to be deleted.</td>
    </tr>
  </tbody>
</table>

<h3 id="deleting-users-by-email-addresses-and-phone-numbers">Deleting users by email addresses and phone numbers</h3>

<p>If an email address or phone number is specified as an identifier, an additional <code class="language-plaintext highlighter-rouge">prioritization</code> value is required in the identifier. <code class="language-plaintext highlighter-rouge">prioritization</code> must be an ordered array and should specify which user to delete if there are multiple users. This means deleting users will not occur if more than one user matches a prioritization.</p>

<p>The allowed values for the array are:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">identified</code></li>
  <li><code class="language-plaintext highlighter-rouge">unidentified</code></li>
  <li><code class="language-plaintext highlighter-rouge">most_recently_updated</code> (refers to prioritizing the most recently updated user)</li>
</ul>

<p>Only one of the following options may exist in the <code class="language-plaintext highlighter-rouge">prioritization</code> array at a time:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">identified</code> refers to prioritizing a user with an <code class="language-plaintext highlighter-rouge">external_id</code></li>
  <li><code class="language-plaintext highlighter-rouge">unidentified</code> refers to prioritizing a user without an <code class="language-plaintext highlighter-rouge">external_id</code></li>
</ul>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "external_ids": ["external_identifier1", "external_identifier2"],
  "braze_ids": ["braze_identifier1", "braze_identifier2"],
  "user_aliases": [
    {
      "alias_name": "user_alias1", "alias_label": "alias_label1"
    },
    {
      "alias_name": "user_alias2", "alias_label": "alias_label2"
    }
  ],
  "email_addresses": [
    {
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"deleted"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">integer)</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">IDs</span><span class="w"> </span><span class="err">queued</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">deletion</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<h3 id="a-success-response-was-returned-but-the-user-still-appears">A success response was returned but the user still appears</h3>

<p>A successful response confirms the request was queued, not that deletion is complete. Deletion typically finishes in under a second, but it can take up to five minutes for the change to propagate across all caches. If you immediately search for the user in the dashboard or export their data via the API, you may still see results during this propagation window.</p>

<p>If the user still exists after several minutes, verify that the identifier in your request matches the user’s actual profile:</p>

<ul>
  <li><strong><code class="language-plaintext highlighter-rouge">external_ids</code> array:</strong> Confirm each value matches a user’s external ID exactly.</li>
  <li><strong><code class="language-plaintext highlighter-rouge">braze_id</code>:</strong> You can find a user’s <code class="language-plaintext highlighter-rouge">braze_id</code> by exporting their data with the <a href="/docs/api/endpoints/export/user_data/post_users_identifier/"><code class="language-plaintext highlighter-rouge">/users/export/ids</code> endpoint</a> or by exporting a segment to CSV (where the <code class="language-plaintext highlighter-rouge">braze_id</code> appears as “Appboy ID”).</li>
  <li><strong>Alias-only or email-only profiles:</strong> If the profile has no <code class="language-plaintext highlighter-rouge">external_id</code>, create a segment filtering for <strong>External User ID is blank</strong> combined with the known email or phone number, then export to CSV to retrieve the <code class="language-plaintext highlighter-rouge">braze_id</code>.</li>
</ul>

<p>To confirm whether a user has been deleted, call the <a href="/docs/api/endpoints/export/user_data/post_users_identifier/"><code class="language-plaintext highlighter-rouge">/users/export/ids</code> endpoint</a> using the same identifier type you used in the delete request (for example, including the value in <code class="language-plaintext highlighter-rouge">external_ids</code>, <code class="language-plaintext highlighter-rouge">braze_id</code>, or <code class="language-plaintext highlighter-rouge">user_aliases</code>). If the user no longer exists, the response contains <code class="language-plaintext highlighter-rouge">"users": []</code> and may include <code class="language-plaintext highlighter-rouge">"invalid_user_ids"</code> listing that identifier.</p>

</div>
