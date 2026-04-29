<div id='api_hlkexobzcjpx' class='api_div'>
<h1 id="identify-users">Identify users</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/identify</p>
</div>

<blockquote>
  <p>Use this endpoint to identify an unidentified (alias-only, email-only, or phone number-only) user using the provided external ID.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58" class="seeme">See me in Postman</a></div>

<h2 id="how-it-works">How it works</h2>

<p>Calling <code class="language-plaintext highlighter-rouge">/users/identify</code> combines a user profile that is identified by an alias (alias-only profile), email address (email-only profile), or phone number (phone number-only profile) with a user profile that has an <code class="language-plaintext highlighter-rouge">external_id</code> (identified profile), then removes the alias-only profile.</p>

<p>Identifying a user requires an <code class="language-plaintext highlighter-rouge">external_id</code> to be included in the following objects:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">aliases_to_identify</code></li>
  <li><code class="language-plaintext highlighter-rouge">emails_to_identify</code></li>
  <li><code class="language-plaintext highlighter-rouge">phone_numbers_to_identify</code></li>
</ul>

<p>If there isn’t a user with that <code class="language-plaintext highlighter-rouge">external_id</code>, the <code class="language-plaintext highlighter-rouge">external_id</code> is added to the aliased user’s record, and the user is considered identified. Users can have only one alias for a specific label. If a user already exists with the <code class="language-plaintext highlighter-rouge">external_id</code> and has an existing alias with the same label as the alias-only profile, then the user profiles are not combined.</p>

<p><strong>Tip:</strong></p>

<p>To prevent unexpected loss of data when identifying users, we highly recommend that you first refer to <a href="/docs/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present">data collection best practices</a> to learn about capturing user data when alias-only user information is already present.</p>

<h3 id="merging-behavior">Merging behavior</h3>

<p>By default, this endpoint merges the following list of fields found <strong>exclusively</strong> on the anonymous user to the identified user.</p>

<p><strong>List of fields that are merged</strong></p>

<ul>
  <li>First name</li>
  <li>Last name</li>
  <li>Email</li>
  <li>Gender</li>
  <li>Date of birth</li>
  <li>Phone number</li>
  <li>Time zone</li>
  <li>Home city</li>
  <li>Country</li>
  <li>Language</li>
  <li>Session count (the sum of sessions from both profiles)</li>
  <li>Date of first session (Braze picks the earlier date of the two dates)</li>
  <li>Date of last session (Braze picks the later date of the two dates)</li>
  <li>Custom attributes</li>
  <li>Custom event and purchase event data</li>
  <li>Custom event and purchase event properties for “X times in Y days” segmentation (where X&lt;=50 and Y&lt;=30)</li>
  <li>Segmentable custom events summary
    <ul>
      <li>Event count (the sum from both profiles)</li>
      <li>Event first occurred (Braze picks the earlier date of the two dates)</li>
      <li>Event last occurred (Braze picks the later date of the two dates)</li>
    </ul>
  </li>
  <li>In-app purchase total in cents (the sum from both profiles)</li>
  <li>Total number of purchases (the sum from both profiles)</li>
  <li>Date of first purchase (Braze picks the earlier date of the two dates)</li>
  <li>Date of last purchase (Braze picks the later date of the two dates)</li>
  <li>App summaries</li>
  <li>Last_X_at fields (Braze updates the fields if the orphaned profile fields are more recent)</li>
  <li>Campaign summaries (Braze picks the most recent date fields)</li>
  <li>Workflow summaries (Braze picks the most recent date fields)</li>
  <li>Message and message engagement history</li>
  <li>Custom event and purchase event count and first date and last date timestamps
    <ul>
      <li>These merged fields update “for X events in Y days” filters. For purchase events, these filters include “number of purchases in Y days” and “money spent in last Y days”.</li>
    </ul>
  </li>
  <li>Session data if the app exists on both user profiles
    <ul>
      <li>For example, if our target user doesn’t have an app summary for “ABCApp” but our original user does, the target user has the “ABCApp” app summary on their profile after the merge.</li>
    </ul>
  </li>
</ul>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.identify</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
   </span><span class="nl">"aliases_to_identify"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">identify</span><span class="w"> </span><span class="err">objects)</span><span class="p">,</span><span class="w">
   </span><span class="nl">"emails_to_identify"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">identify</span><span class="w"> </span><span class="err">objects)</span><span class="w"> </span><span class="err">User</span><span class="w"> </span><span class="err">emails</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">identify</span><span class="p">,</span><span class="w">
   </span><span class="nl">"phone_numbers_to_identify"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">alias</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">identify</span><span class="w"> </span><span class="err">objects)</span><span class="w"> </span><span class="err">User</span><span class="w"> </span><span class="err">phone</span><span class="w"> </span><span class="err">numbers</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">identify</span><span class="p">,</span><span class="w">
</span><span class="p">}</span><span class="err">,</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="request-parameters">Request parameters</h3>

<p>You can add up to 50 user aliases per request. You can associate multiple additional user aliases with a single <code class="language-plaintext highlighter-rouge">external_id</code>.</p>

<p><strong>Important:</strong></p>

<p>One of the following is required: <code class="language-plaintext highlighter-rouge">aliases_to_identify</code>, <code class="language-plaintext highlighter-rouge">emails_to_identify</code>, or <code class="language-plaintext highlighter-rouge">phone_numbers_to_identify</code> per request. For example, you can use this endpoint to identify users by email by using <code class="language-plaintext highlighter-rouge">emails_to_identify</code> in your request.</p>

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
      <td><code class="language-plaintext highlighter-rouge">aliases_to_identify</code></td>
      <td>Required</td>
      <td>Array of aliases to identify object</td>
      <td>See <a href="/docs/api/objects_filters/aliases_to_identify/">alias to identify object</a> and <a href="/docs/api/objects_filters/user_alias_object/">user alias object</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">emails_to_identify</code></td>
      <td>Required</td>
      <td>Array of aliases to identify object</td>
      <td>Required if <code class="language-plaintext highlighter-rouge">email</code> is specified as the identifier. Email addresses to identify users. See <a href="#identifying-users-by-email">Identifying users by email</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">phone_numbers_to_identify</code></td>
      <td>Required</td>
      <td>Array of aliases to identify object</td>
      <td>Phone numbers to identify users.</td>
    </tr>
  </tbody>
</table>

<h3 id="identifying-users-by-email-addresses-and-phone-numbers">Identifying users by email addresses and phone numbers</h3>

<p>If an email address or phone number is specified as an identifier, you must also include <code class="language-plaintext highlighter-rouge">prioritization</code> in the identifier.</p>

<p>The <code class="language-plaintext highlighter-rouge">prioritization</code> must be an array specifying which user to merge if there are multiple users found. <code class="language-plaintext highlighter-rouge">prioritization</code> is an ordered array, meaning if more than one user matches from a prioritization, then merging does not occur.</p>

<p>The allowed values for the array are:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">identified</code></li>
  <li><code class="language-plaintext highlighter-rouge">unidentified</code></li>
  <li><code class="language-plaintext highlighter-rouge">most_recently_updated</code> (refers to prioritizing the most recently updated user)</li>
  <li><code class="language-plaintext highlighter-rouge">least_recently_updated</code> (refers to prioritizing the least recently updated user)</li>
</ul>

<p>Only one of the following options may exist in the prioritization array at a time:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">identified</code> refers to prioritizing a user with an <code class="language-plaintext highlighter-rouge">external_id</code></li>
  <li><code class="language-plaintext highlighter-rouge">unidentified</code> refers to prioritizing a user without an <code class="language-plaintext highlighter-rouge">external_id</code></li>
</ul>

<p><strong>Note:</strong></p>

<p>A merge does not occur if the email address or phone number matches multiple users. This includes cases where one of those users has the same <code class="language-plaintext highlighter-rouge">external_id</code> as the one specified in the request. In these cases, the endpoint returns <code class="language-plaintext highlighter-rouge">"message": "success"</code>, but the user profiles are not combined. To avoid this, verify that the email address or phone number is associated only with unidentified users before calling this endpoint.</p>

<h2 id="request-example">Request example</h2>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="case-sensitivity">Case sensitivity</h3>

<p>The <code class="language-plaintext highlighter-rouge">alias_name</code> field is case-sensitive. A request that returns a <code class="language-plaintext highlighter-rouge">201</code> status code only confirms the request syntax was valid—it does not confirm the alias was matched. If the capitalization of <code class="language-plaintext highlighter-rouge">alias_name</code> in your request doesn’t exactly match the alias stored on the user profile, the operation will silently fail and the <code class="language-plaintext highlighter-rouge">external_id</code> won’t be assigned. For example, if the stored alias is <code class="language-plaintext highlighter-rouge">JimJones@example.com</code>, a request with <code class="language-plaintext highlighter-rouge">jimjones@example.com</code> will return success but produce no result.</p>

<p><strong>Tip:</strong></p>

<p>For more information on <code class="language-plaintext highlighter-rouge">alias_name</code> and <code class="language-plaintext highlighter-rouge">alias_label</code>, check out our <a href="/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases">user aliases</a> documentation.</p>

<h2 id="response">Response</h2>

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
