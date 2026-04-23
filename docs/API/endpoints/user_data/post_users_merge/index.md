<div id='api_iwtftqqtrzlm' class='api_div'>
<h1 id="merge-users">Merge users</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/merge</p>
</div>

<blockquote>
  <p>Use this endpoint to merge one user into another user.</p>
</blockquote>

<p>Up to 50 merges may be specified per request. This endpoint is asynchronous.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.merge</code> permission.</p>

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
  </span><span class="nl">"merge_updates"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">objects)</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">merge_updates</code></td>
      <td>Required</td>
      <td>Array</td>
      <td>An object array. Each object should contain an <code class="language-plaintext highlighter-rouge">identifier_to_merge</code> object and an <code class="language-plaintext highlighter-rouge">identifier_to_keep</code> object, which should each reference a user either by <code class="language-plaintext highlighter-rouge">external_id</code>,  <code class="language-plaintext highlighter-rouge">user_alias</code>, <code class="language-plaintext highlighter-rouge">phone</code>, or <code class="language-plaintext highlighter-rouge">email</code>.</td>
    </tr>
  </tbody>
</table>

<h3 id="merge-behavior">Merge behavior</h3>

<p>The behavior documented below is true for all Braze features that <strong>are not</strong> powered by Snowflake. User merges won’t be reflected for the <strong>Messaging History</strong> tab, Segment Extensions, Query Builder, and Currents.</p>

<p><strong>Important:</strong></p>

<p>The endpoint does not guarantee the sequence of <code class="language-plaintext highlighter-rouge">merge_updates</code> objects being updated.</p>

<p>This endpoint merges the following fields if they’re not found on the target user.</p>

<ul>
  <li>First name</li>
  <li>Last name</li>
  <li>Email addresses (unless they are <a href="/docs/user_guide/data/infrastructure/field_level_encryption/">encrypted</a>)</li>
  <li>Gender</li>
  <li>Date of birth</li>
  <li>Phone number</li>
  <li>Time zone</li>
  <li>Home city</li>
  <li>Country</li>
  <li>Language</li>
  <li>Device information</li>
  <li>Session count (the sum of sessions from both profiles)</li>
  <li>Date of first session (Braze picks the earlier date of the two dates)</li>
  <li>Date of last session (Braze picks the later date of the two dates)</li>
  <li>Custom attributes (Braze retains existing custom attributes on the target profile and includes custom attributes that didn’t exist on the target profile)</li>
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
  <li>Campaign interaction data (Braze picks the most recent date fields)</li>
  <li>Workflow summaries (Braze picks the most recent date fields)</li>
  <li>Message and message engagement history</li>
  <li>Braze merges session data only if the app exists on both user profiles.</li>
</ul>

<p><strong>Note:</strong></p>

<p>When merging users, using the <code class="language-plaintext highlighter-rouge">/users/merge</code> endpoint works the same way as using the <a href="https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser"><code class="language-plaintext highlighter-rouge">changeUser()</code> method</a>.</p>

<h4 id="custom-event-date-and-purchase-event-date-behavior">Custom event date and purchase event date behavior</h4>

<p>These merged fields update “for X events in Y days” filters. For purchase events, these filters include “number of purchases in Y days” and “money spent in last Y days”.</p>

<h3 id="merging-users-by-email-or-phone-number">Merging users by email or phone number</h3>

<p>If an <code class="language-plaintext highlighter-rouge">email</code> or <code class="language-plaintext highlighter-rouge">phone</code> is specified as an identifier, you must include an additional <code class="language-plaintext highlighter-rouge">prioritization</code> value in the identifier. The <code class="language-plaintext highlighter-rouge">prioritization</code> should be an ordered array specifying which user to merge if multiple users are found. This means if more than one user matches from a prioritization, then merging does not occur.</p>

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

<h2 id="example-requests">Example requests</h2>

<h3 id="basic-request">Basic request</h3>

<p>This is a basic request body to show the pattern of the request.</p>

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
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/users/merge'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="merging-unidentified-user">Merging unidentified user</h3>

<p>The following request would merge the most recently updated unidentified user with email address <code class="language-plaintext highlighter-rouge">john.smith@braze.com</code> into the user with an external ID <code class="language-plaintext highlighter-rouge">john</code>. In this example, using <code class="language-plaintext highlighter-rouge">most_recently_updated</code> filters the query to one unidentified user. So, if there were two unidentified users with this email address, only one would get merged into the user who has an external ID <code class="language-plaintext highlighter-rouge">john</code>.</p>

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
12
13
14
15
16
17
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/users/merge'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="merging-unidentified-user-into-identified-user">Merging unidentified user into identified user</h3>

<p>This next example merges the most recently updated unidentified user with email address <code class="language-plaintext highlighter-rouge">john.smith@braze.com</code> into the most recently updated identified user with email address <code class="language-plaintext highlighter-rouge">john.smith@braze.com</code>.</p>

<p>Using <code class="language-plaintext highlighter-rouge">most_recently_updated</code> filters the queries to one user (one unidentified user for <code class="language-plaintext highlighter-rouge">identifier_to_merge</code>, and one identified user for the <code class="language-plaintext highlighter-rouge">identifier_to_keep</code>).</p>

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
12
13
14
15
16
17
18
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/users/merge'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="merging-an-unidentified-user-without-including-the-most_recently_updated-prioritization">Merging an unidentified user without including the most_recently_updated prioritization</h3>

<p>If there are two unidentified users with the mail address <code class="language-plaintext highlighter-rouge">john.smith@braze.com</code>, this example request doesn’t merge any users because there are two unidentified users with that email address. This request only works if there is only one unidentified user with the email address <code class="language-plaintext highlighter-rouge">john.smith@braze.com</code>.</p>

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
12
13
14
15
16
17
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/users/merge'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>There are two status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">202</code> and <code class="language-plaintext highlighter-rouge">400</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">202</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="example-error-response">Example error response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">400</code> could return the following response body. Refer to <a href="#troubleshooting">Troubleshooting</a> for more information about errors you may encounter.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"'merge_updates' must be an array of objects"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<p>The following table lists possible error messages that may occur.</p>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Error</th>
      <th>Troubleshooting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">'merge_updates' must be an array of objects</code></td>
      <td>Check that <code class="language-plaintext highlighter-rouge">merge_updates</code> is an array of objects.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">a single request may not contain more than 50 merge updates</code></td>
      <td>You can only specify up to 50 merge updates in a single request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string</code></td>
      <td>Check the identifiers in your request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'</code></td>
      <td>Check that <code class="language-plaintext highlighter-rouge">merge_updates</code> only contains the two objects <code class="language-plaintext highlighter-rouge">identifier_to_merge</code> and <code class="language-plaintext highlighter-rouge">identifier_to_keep</code>.</td>
    </tr>
  </tbody>
</table>

</div>
