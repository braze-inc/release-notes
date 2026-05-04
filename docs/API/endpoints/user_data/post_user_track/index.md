<div id='api_dyzkdfuujuym' class='api_div'>
<h1 id="create-and-update-users">Create and update users</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/track</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to record custom events and purchases and update user profile attributes.</p>
</blockquote>

<p><strong>Note:</strong></p>

<p>Each custom attribute sent in a request to <code class="language-plaintext highlighter-rouge">/users/track</code> consumes a data point. For more information, see <a href="/docs/user_guide/data/infrastructure/data_points/">Data points</a>.</p>

<p>Braze processes the data passed through the API at face value, and you should only pass deltas (changing data) to minimize unnecessary data point logging.</p>

<h2 id="need-to-update-users-in-bulk">Need to update users in bulk?</h2>

<p>Use the <a href="/docs/api/endpoints/user_data/post_user_track_bulk/"><code class="language-plaintext highlighter-rouge">/users/track/bulk</code> endpoint</a> to send larger batches and reduce request volume.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.track</code> permission.</p>

<p>Customers using the API for server-to-server calls may need to allowlist <code class="language-plaintext highlighter-rouge">rest.iad-01.braze.com</code> if they’re behind a firewall.</p>

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
  </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"events"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"purchases"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">purchase</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="request-parameters">Request parameters</h3>

<p><strong>Important:</strong></p>

<p>For each request component listed in the following table, you must include one of <code class="language-plaintext highlighter-rouge">external_id</code>, <code class="language-plaintext highlighter-rouge">user_alias</code>, <code class="language-plaintext highlighter-rouge">braze_id</code>, <code class="language-plaintext highlighter-rouge">email</code>, or <code class="language-plaintext highlighter-rouge">phone</code>.</p>

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
      <td>See <a href="/docs/api/objects_filters/user_attributes_object/#migrating-push-tokens">user attributes object</a></td>
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

<h3 id="identifier-resolution">Identifier resolution</h3>

<p>Each request object must include at least one identifier. The following table describes how Braze determines which identifier to use for user profile lookup.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" role="presentation">
  <thead>
    <tr>
      <th>Identifier type</th>
      <th>Identifiers</th>
      <th>Behavior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Primary</td>
      <td><code class="language-plaintext highlighter-rouge">external_id</code>, <code class="language-plaintext highlighter-rouge">user_alias</code>, <code class="language-plaintext highlighter-rouge">braze_id</code></td>
      <td>Used for user profile lookup. Only one primary identifier is allowed per request object—including more than one causes that object to be rejected.</td>
    </tr>
    <tr>
      <td>Secondary</td>
      <td><code class="language-plaintext highlighter-rouge">email</code>, <code class="language-plaintext highlighter-rouge">phone</code></td>
      <td>Used for user profile lookup <strong>only</strong> when no primary identifier is present. If both <code class="language-plaintext highlighter-rouge">email</code> and <code class="language-plaintext highlighter-rouge">phone</code> are included without a primary identifier, <code class="language-plaintext highlighter-rouge">email</code> takes precedence.</td>
    </tr>
  </tbody>
</table>

<p>When a primary identifier is present, any <code class="language-plaintext highlighter-rouge">email</code> or <code class="language-plaintext highlighter-rouge">phone</code> values in the same request object are treated as profile attributes—not as identifiers for user lookup. For example, if a request includes both an <code class="language-plaintext highlighter-rouge">external_id</code> and an <code class="language-plaintext highlighter-rouge">email</code>:</p>

<ul>
  <li>Braze looks up the user profile by <code class="language-plaintext highlighter-rouge">external_id</code>.</li>
  <li>The <code class="language-plaintext highlighter-rouge">email</code> value is set (or updated) as an attribute on the resolved profile.</li>
</ul>

<p><strong>Important:</strong></p>

<p>Including a primary identifier that doesn’t match any existing profile can create a duplicate profile even when <code class="language-plaintext highlighter-rouge">email</code> or <code class="language-plaintext highlighter-rouge">phone</code> in the same request match an existing profile. For more information, see <a href="#how-do-i-avoid-creating-duplicate-user-profiles">How do I avoid creating duplicate user profiles?</a>.</p>

<h2 id="example-requests">Example requests</h2>

<h3 id="update-a-user-profile-by-email-address">Update a user profile by email address</h3>

<p>You can update a user profile by email address using the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint.</p>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
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
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="update-a-user-profile-by-phone-number">Update a user profile by phone number</h3>

<p>You can update a user profile by phone number using the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint. This endpoint only works if you include a valid phone number.</p>

<p><strong>Important:</strong></p>

<p>If you include a request with both <code class="language-plaintext highlighter-rouge">email</code> and <code class="language-plaintext highlighter-rouge">phone</code>, Braze uses the email as the identifier.</p>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
</pre></td></tr></tbody></table></code></pre></div></div>
<h3 id="set-subscription-groups">Set subscription groups</h3>

<p>This example shows how to create a user and set their subscription group within the user attributes object.</p>

<p>Updating the subscription status with this endpoint updates the user specified by their <code class="language-plaintext highlighter-rouge">external_id</code> (such as User1) and updates the subscription status of any users with the same email as that user (User1).</p>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Note:</strong></p>

<p>For SMS subscription groups, when you set a group’s <code class="language-plaintext highlighter-rouge">subscription_state</code> to <code class="language-plaintext highlighter-rouge">subscribed</code>, you can include the optional <code class="language-plaintext highlighter-rouge">use_double_opt_in_logic</code> parameter set to <code class="language-plaintext highlighter-rouge">true</code> within that subscription group object to enter the user into the <a href="/docs/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in/">SMS double opt-in</a> workflow. If this parameter is omitted or set to <code class="language-plaintext highlighter-rouge">false</code> when <code class="language-plaintext highlighter-rouge">subscription_state</code> is <code class="language-plaintext highlighter-rouge">subscribed</code>, the user is subscribed without entering the double opt-in workflow. This parameter is not applied when <code class="language-plaintext highlighter-rouge">subscription_state</code> is set to other values, such as <code class="language-plaintext highlighter-rouge">unsubscribed</code>.</p>

<h3 id="example-request-to-create-an-alias-only-user">Example request to create an alias-only user</h3>

<p>You can use the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint to create an alias-only user by setting the <code class="language-plaintext highlighter-rouge">_update_existing_only</code> key with a value of <code class="language-plaintext highlighter-rouge">false</code> in the body of the request. If you omit this value, Braze does not create the alias-only user profile. Using an alias-only user ensures that one profile with that alias exists. This is especially helpful when building an integration as it prevents Braze from creating duplicate user profiles.</p>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="responses">Responses</h2>

<p>When using any of the aforementioned API requests, you should receive one of the following three general responses: a <a href="#successful-message">successful message</a>, a <a href="#successful-message-with-non-fatal-errors">successful message with non-fatal errors</a>, or a <a href="#message-with-fatal-errors">message with fatal errors</a>.</p>

<h3 id="successful-message">Successful message</h3>

<p>Successful messages are met with the following response:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"attributes_processed"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">integer)</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">integer</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">external_ids</span><span class="w"> </span><span class="err">with</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">queued</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">processing</span><span class="p">,</span><span class="w">
  </span><span class="nl">"events_processed"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">integer)</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">integer</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">queued</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">processing</span><span class="p">,</span><span class="w">
  </span><span class="nl">"purchases_processed"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">integer)</span><span class="p">,</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">purchases</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">an</span><span class="w"> </span><span class="err">integer</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">number</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">purchases</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">queued</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">processing</span><span class="p">,</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="successful-message-with-non-fatal-errors">Successful message with non-fatal errors</h3>

<p>If your message is successful but has non-fatal errors, such as one invalid event object out of a long list of events, you receive the following response:</p>

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

<p>For success messages, Braze still processes any data not affected by an error in the <code class="language-plaintext highlighter-rouge">errors</code> array.</p>

<h3 id="message-with-fatal-errors">Message with fatal errors</h3>

<p>If your message has a fatal error, you receive the following response:</p>

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

<p>For status codes and associated error messages that Braze returns if your request encounters a fatal error, reference <a href="/docs/api/errors/#fatal-errors">Fatal errors &amp; responses</a>.</p>

<p>If you receive the error “provided external_id is blacklisted and disallowed”, your request may have included a “dummy user.” For more information, refer to <a href="/docs/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking">Spam blocking</a>.</p>

<h3 id="endpoint-specific-errors">Endpoint-specific errors</h3>

<p>The following errors are specific to the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint and are returned in the <code class="language-plaintext highlighter-rouge">errors</code> array of the response. Use these to troubleshoot issues with individual objects in a request.</p>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Error</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_DEVICE_ID</code></td>
      <td>The <code class="language-plaintext highlighter-rouge">device_id</code> for a token import must be between 8 and 255 bytes.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_EMAIL_SUBSCRIPTION_STATE</code></td>
      <td><code class="language-plaintext highlighter-rouge">email_subscribe</code> must be <code class="language-plaintext highlighter-rouge">subscribed</code>, <code class="language-plaintext highlighter-rouge">unsubscribed</code>, or <code class="language-plaintext highlighter-rouge">opted_in</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_LOCATION_UPDATE</code></td>
      <td><code class="language-plaintext highlighter-rouge">current_location</code> must be an object containing <code class="language-plaintext highlighter-rouge">longitude</code> and <code class="language-plaintext highlighter-rouge">latitude</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_PUSH_SUBSCRIPTION_STATE</code></td>
      <td><code class="language-plaintext highlighter-rouge">push_subscribe</code> must be <code class="language-plaintext highlighter-rouge">subscribed</code>, <code class="language-plaintext highlighter-rouge">unsubscribed</code>, or <code class="language-plaintext highlighter-rouge">opted_in</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_PUSH_TOKEN_APP_ID</code></td>
      <td>The <code class="language-plaintext highlighter-rouge">app_id</code> in a token import must be a valid app identifier from the current workspace.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_PUSH_TOKEN_IMPORT</code></td>
      <td>Token imports must include tokens and exclude <code class="language-plaintext highlighter-rouge">external_id</code> and <code class="language-plaintext highlighter-rouge">braze_id</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_PUSH_TOKEN_STRING</code></td>
      <td>The <code class="language-plaintext highlighter-rouge">token</code> value in a token import must be a string.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_PUSH_TOKEN_VALUE</code></td>
      <td><code class="language-plaintext highlighter-rouge">push_tokens</code> must be an array of objects.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_SUBSCRIPTION_GROUP_ARRAY</code></td>
      <td><code class="language-plaintext highlighter-rouge">subscription_groups</code> must be an array.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_SUBSCRIPTION_GROUP_HASH</code></td>
      <td>Each item in the <code class="language-plaintext highlighter-rouge">subscription_groups</code> array must be a JSON object with <code class="language-plaintext highlighter-rouge">subscription_group_id</code> and <code class="language-plaintext highlighter-rouge">subscription_state</code> keys.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_SUBSCRIPTION_GROUP_ID</code></td>
      <td><code class="language-plaintext highlighter-rouge">subscription_group_id</code> must be a valid subscription group UUID.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BAD_SUBSCRIPTION_GROUP_STATE</code></td>
      <td><code class="language-plaintext highlighter-rouge">subscription_state</code> for a subscription group must be <code class="language-plaintext highlighter-rouge">subscribed</code> or <code class="language-plaintext highlighter-rouge">unsubscribed</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">BLACKLISTED_EXTERNAL_USER_ID</code></td>
      <td>The provided <code class="language-plaintext highlighter-rouge">external_id</code> is blocklisted and disallowed.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">EMAIL_BAD_FORMAT</code></td>
      <td>The value provided for <code class="language-plaintext highlighter-rouge">email</code> is not a valid email address.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">EXTERNAL_USER_ID_TOO_LARGE</code></td>
      <td>The <code class="language-plaintext highlighter-rouge">external_id</code> exceeds the maximum allowed length of 987 bytes.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">INVALID_ATTRIBUTE_EMAIL_SUBSCRIPTION_INFO</code></td>
      <td><code class="language-plaintext highlighter-rouge">email_subscription_info</code> is not a valid attribute.</td>
    </tr>
  </tbody>
</table>

<h2 id="frequently-asked-questions">Frequently asked questions</h2>

<h3 id="what-happens-when-multiple-profiles-with-the-same-email-address-are-found">What happens when multiple profiles with the same email address are found?</h3>
<p>If the <code class="language-plaintext highlighter-rouge">external_id</code> exists, Braze prioritizes the most recently updated profile with an external ID for updates. If the <code class="language-plaintext highlighter-rouge">external_id</code> doesn’t exist, Braze prioritizes the most recently updated profile for updates.</p>

<h3 id="what-happens-if-no-profile-with-the-email-address-exists">What happens if no profile with the email address exists?</h3>
<p>Braze creates a profile and an email-only user and sets the email field to test@braze.com, as noted in the example request for updating a user profile by email address. Braze does not create an alias.</p>

<h3 id="how-do-you-use-userstrack-to-import-legacy-user-data">How do you use <code class="language-plaintext highlighter-rouge">/users/track</code> to import legacy user data?</h3>
<p>You may submit data through the Braze API for a user who has not yet used your mobile app to generate a user profile. If the user subsequently uses the application, all information following their identification using the SDK is merged with the existing user profile you created using the API call. Any user behavior recorded anonymously by the SDK before identification is lost upon merging with the existing API-generated user profile.</p>

<p>The segmentation tool includes these users regardless of whether they have engaged with the app. If you want to exclude users uploaded using the User API who have not yet engaged with the app, add the <code class="language-plaintext highlighter-rouge">Session Count &gt; 0</code> filter.</p>

<h3 id="how-do-i-avoid-creating-duplicate-user-profiles">How do I avoid creating duplicate user profiles?</h3>

<p>Duplicate profiles can occur when a request includes a primary identifier (such as <code class="language-plaintext highlighter-rouge">external_id</code>) that doesn’t match any existing profile, alongside an <code class="language-plaintext highlighter-rouge">email</code> or <code class="language-plaintext highlighter-rouge">phone</code> value that does match an existing profile. Because primary identifiers are used for user lookup, Braze creates a new profile for the unrecognized <code class="language-plaintext highlighter-rouge">external_id</code> instead of updating the existing email-only or phone-only profile.</p>

<p>To avoid duplicates:</p>

<ul>
  <li>When transitioning users from email-only or phone-only profiles to identified profiles, use the <a href="/docs/api/endpoints/user_data/post_user_identify/"><code class="language-plaintext highlighter-rouge">/users/identify</code> endpoint</a> to assign an <code class="language-plaintext highlighter-rouge">external_id</code> to the existing profile, rather than sending both to <code class="language-plaintext highlighter-rouge">/users/track</code>.</li>
  <li>If duplicates already exist, merge them using the <a href="/docs/api/endpoints/user_data/post_users_merge/"><code class="language-plaintext highlighter-rouge">/users/merge</code> endpoint</a>.</li>
</ul>

<h3 id="how-does-userstrack-handle-duplicate-events">How does <code class="language-plaintext highlighter-rouge">/users/track</code> handle duplicate events?</h3>

<p>Each event object in the events array represents a single occurrence of a custom event by a user at a designated time. This means each event ingested into Braze has its own event ID, so “duplicate” events are treated as separate, unique events.</p>

<h3 id="how-does-userstrack-handle-invalid-nested-custom-attributes">How does <code class="language-plaintext highlighter-rouge">/users/track</code> handle invalid nested custom attributes?</h3>

<p>When a nested custom attribute contains any invalid values (such as invalid time formats or null values), Braze drops all nested custom attribute updates in the request from processing. This applies to all nested structures within that specific attribute. To help ensure successful processing, verify that all values within nested custom attributes are valid before sending.</p>

<h2 id="monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau">Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU</h2>

<p>For customers on new pricing, rate limits are enforced at the company level. Customers can set workspace rate limits for hourly limits, but burst limits are still shared between all workspaces.</p>

<p>For customers who have purchased Monthly Active Users CY 24-25, Universal MAU, Web MAU, or Mobile MAU, Braze manages different rate limits on its <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint:</p>
<ul>
  <li>Hourly rate limits are set according to the expected data ingestion activity on your account, which may correspond to the number of monthly active users you have purchased, industry, seasonality, or other factors.</li>
  <li>In addition to the hourly limit, Braze enforces a burst limit on the number of requests that can be sent every three seconds.</li>
  <li>Each request may batch up to 75 updates combined across attribute, event, or purchase objects.</li>
</ul>

<p>Current limits based on expected ingestion can be found in the dashboard under <strong>Settings</strong> &gt; <strong>APIs and Identifiers</strong> &gt; <strong>API Usage Dashboard</strong>. We may modify rate limits to protect system stability or allow for increased data throughput on your account. Please contact Braze Support or your customer success manager for questions or concerns regarding the hourly or per-second request limit and the needs of your business.</p>

<h3 id="rate-limit-headers-for-monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau">Rate limit headers for Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU</h3>

<p>All non-rate-limited (such as non-<code class="language-plaintext highlighter-rouge">429</code>) responses contain the following HTTP response headers that indicate the state of the hourly rate limit window to the client. Use these headers to manage your request rate:</p>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Header name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">X-RateLimit-Limit</code></td>
      <td>The number of requests allowed per time period</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">X-RateLimit-Remaining</code></td>
      <td>The approximate number of requests remaining within a window</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">X-RateLimit-Reset</code></td>
      <td>The number of seconds remaining before the current window resets</td>
    </tr>
  </tbody>
</table>

<p>Note that the <code class="language-plaintext highlighter-rouge">RateLimit-Limit</code>, <code class="language-plaintext highlighter-rouge">RateLimit-Remaining</code>, and <code class="language-plaintext highlighter-rouge">RateLimit-Reset</code> headers are not returned when you hit an HTTP <code class="language-plaintext highlighter-rouge">429</code> error. When the error occurs, those headers are replaced with an <code class="language-plaintext highlighter-rouge">X-Ratelimit-Retry-After</code> header that returns an integer indicating the number of seconds before you can start making requests.</p>

</div>
