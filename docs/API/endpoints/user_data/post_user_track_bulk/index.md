<div id='api_sfptvkdqhfqa' class='api_div'>
<h1 id="create-and-update-users-bulk">Create and update users (bulk)</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/track/bulk</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<p>Use this endpoint to record custom events and purchases and update user profile attributes in bulk.</p>

<p><strong>Important:</strong></p>

<p>This endpoint is currently in <strong>limited beta</strong>. Although we’re not adding new customers to the beta right now, let your Braze account manager know if you think this feature could be useful for your Braze integration.</p>

<h2 id="when-to-use-this-endpoint">When to use this endpoint</h2>

<p>Like the <a href="/docs/api/endpoints/user_data/post_user_track/"><code class="language-plaintext highlighter-rouge">/users/track</code> endpoint</a>, you can use this endpoint to update user profiles. This endpoint is better suited for bulk updates:</p>

<ul>
  <li><strong>Larger requests:</strong> Send up to 1,000 users per request, so you can make fewer requests for large backfills and syncs.</li>
  <li><strong>Prioritization:</strong> During peak traffic conditions, requests to <code class="language-plaintext highlighter-rouge">/users/track</code> are prioritized over requests to <code class="language-plaintext highlighter-rouge">/users/track/bulk</code>.</li>
</ul>

<p>Use this endpoint when you’re backfilling many user profiles during onboarding, or syncing large volumes of profiles as part of a daily sync.</p>

<p><strong>Note:</strong></p>

<p>The <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint request object limits vary by pricing model and configuration. Use <code class="language-plaintext highlighter-rouge">/users/track/bulk</code> for bulk ingestion.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you must have an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.track.bulk</code> permission.</p>

<p>If you’re making server-to-server calls behind a firewall, you may need to allowlist your Braze REST endpoint (for example, <code class="language-plaintext highlighter-rouge">rest.iad-01.braze.com</code>). For more information, see <a href="/docs/api/basics/#api-definitions">API endpoints</a>.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>For most customers, this endpoint has a base speed limit of 50 requests per second.</p>

<p>Customers on newer contracts may instead have burst (per-second) and steady (per-hour) limits based on contracted monthly active users.</p>

<p>Each <code class="language-plaintext highlighter-rouge">/users/track/bulk</code> request has a payload limit of 2 MB and can include up to 1,000 objects total across attributes, events, and purchases, depending on your account’s bulk rate-limit policy.</p>

<p>Each object can update one user, so a single request can update up to your account’s request object limit of different users. Additionally, each request can contain a maximum of 100 objects per user profile across attributes, events, and purchases.</p>

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
  </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"events"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"purchases"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">purchase</span><span class="w"> </span><span class="err">object)</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="request-parameters">Request parameters</h3>

<p><strong>Important:</strong></p>

<p>For each request object, you must include one of <code class="language-plaintext highlighter-rouge">external_id</code>, <code class="language-plaintext highlighter-rouge">user_alias</code>, <code class="language-plaintext highlighter-rouge">braze_id</code>, <code class="language-plaintext highlighter-rouge">email</code>, or <code class="language-plaintext highlighter-rouge">phone</code>.</p>

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
      <td><code class="language-plaintext highlighter-rouge">attributes</code></td>
      <td>Optional</td>
      <td>Array of attributes objects</td>
      <td>See <a href="/docs/api/objects_filters/user_attributes_object/">user attributes object</a></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">events</code></td>
      <td>Optional</td>
      <td>Array of event objects</td>
      <td>See <a href="/docs/api/objects_filters/event_object/">events object</a></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">purchases</code></td>
      <td>Optional</td>
      <td>Array of purchase objects</td>
      <td>See <a href="/docs/api/objects_filters/purchase_object/">purchases object</a></td>
    </tr>
  </tbody>
</table>

<h2 id="example-requests">Example requests</h2>

<h3 id="bulk-update-user-profiles-in-one-request">Bulk update user profiles in one request</h3>

<p>Update up to your account’s request object limit of user profiles in one request.</p>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    },
    {
      "external_id": "user2",
      "string_attribute": "vegetables",
      "boolean_attribute_1": false,
      "integer_attribute": 25,
      "array_attribute": [
        "broccoli",
        "asparagus"
      ]
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="send-attributes-and-events-in-one-request">Send attributes and events in one request</h3>

<p>Include attributes and events in the same request, up to your account’s total object limit.</p>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    }
  ],
  "events": [
    {
      "external_id": "user2",
      "app_id": "your_app_identifier",
      "name": "rented_movie",
      "time": "2022-12-06T19:20:45+01:00",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="responses">Responses</h2>

<h3 id="successful-message">Successful message</h3>

<p>Successful messages return the following response:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"attributes_processed"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">integer)</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">integer</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">external</span><span class="w"> </span><span class="err">IDs</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">queued</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">processing</span><span class="p">,</span><span class="w">
  </span><span class="nl">"events_processed"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">integer)</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">integer</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">queued</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">processing</span><span class="p">,</span><span class="w">
  </span><span class="nl">"purchases_processed"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">integer)</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">purchases</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">integer</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">purchases</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">queued</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">processing</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="successful-message-with-non-fatal-errors">Successful message with non-fatal errors</h3>

<p>If your request is successful but has non-fatal errors (for example, one invalid event object in a large batch), you receive the following response:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="err">&lt;minor</span><span class="w"> </span><span class="err">error</span><span class="w"> </span><span class="err">message&gt;</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="message-with-fatal-errors">Message with fatal errors</h3>

<p>If your request has a fatal error, you receive the following response:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">&lt;fatal</span><span class="w"> </span><span class="err">error</span><span class="w"> </span><span class="err">message&gt;</span><span class="p">,</span><span class="w">
  </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="err">&lt;fatal</span><span class="w"> </span><span class="err">error</span><span class="w"> </span><span class="err">message&gt;</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="fatal-error-response-codes">Fatal error response codes</h3>

<p>For status codes and associated error messages that Braze returns when your request has a fatal error, see <a href="/docs/api/errors/#fatal-errors">Fatal errors &amp; responses</a>.</p>

<p>If you receive the error “provided external_id is blacklisted and disallowed”, your request may include a “dummy user.” For more information, see <a href="/docs/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking">Spam blocking</a>.</p>

<h2 id="frequently-asked-questions">Frequently asked questions</h2>

<h3 id="should-i-use-this-endpoint-or-userstrack">Should I use this endpoint or <code class="language-plaintext highlighter-rouge">/users/track</code>?</h3>

<p>Use both endpoints based on your use case:</p>

<ul>
  <li>For large backfills and syncs, use <code class="language-plaintext highlighter-rouge">/users/track/bulk</code>.</li>
  <li>For real-time use cases, use <code class="language-plaintext highlighter-rouge">/users/track</code>.</li>
</ul>

<h3 id="what-identifiers-can-i-use-in-userstrackbulk">What identifiers can I use in <code class="language-plaintext highlighter-rouge">/users/track/bulk</code>?</h3>

<p>For each request object, include one of <code class="language-plaintext highlighter-rouge">external_id</code>, <code class="language-plaintext highlighter-rouge">braze_id</code>, <code class="language-plaintext highlighter-rouge">user_alias</code>, <code class="language-plaintext highlighter-rouge">email</code>, or <code class="language-plaintext highlighter-rouge">phone</code>.</p>

<h3 id="can-i-include-attributes-events-and-purchases-in-one-request">Can I include attributes, events, and purchases in one request?</h3>

<p>Yes. Include any mix of attributes, events, and purchases, up to your account’s combined request object limit.</p>

</div>
