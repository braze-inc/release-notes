<div id='api_migjptmffonn' class='api_div'>
<h1 id="create-and-update-users-synchronous">Create and update users (synchronous)</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/track/sync</p>
<div class="coreclass core_endpoint "><a href="https://www.braze.com/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to record custom events and purchases and update user profile attributes synchronously. This endpoint functions similarly to the <a href="/docs/api/endpoints/user_data/post_user_track"><code class="language-plaintext highlighter-rouge">/users/track</code> endpoint</a>, which updates user profiles asynchronously.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>This endpoint is currently in <strong>limited beta</strong>. Although we’re not adding new customers to the beta right now, let your Braze account manager know if you think this feature could be useful for your Braze integration.</p>

<h2 id="synchronous-and-asynchronous-api-calls">Synchronous and asynchronous API calls</h2>

<p>In an asynchronous call, the API returns the status code <code class="language-plaintext highlighter-rouge">201</code>, indicating that your request was successfully received, understood, and accepted. However, this does not mean that your request has been fully completed.</p>

<p>In a synchronous call, the API returns a status code <code class="language-plaintext highlighter-rouge">201</code>, indicating that your request was successfully received, understood, accepted, and completed. The call response shows select user profile fields as a result of the operation.</p>

<p>This endpoint has a lower rate limit than the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint (see <a href="#rate-limit">rate limit</a> below). Each <code class="language-plaintext highlighter-rouge">/users/track/sync</code> request can contain only  one event object, one attribute object, <strong>or</strong> one purchase object. This endpoint should be reserved for user profile updates where a synchronous call is needed. For a healthy implementation, we recommend using <code class="language-plaintext highlighter-rouge">/users/track/sync</code> and <code class="language-plaintext highlighter-rouge">/users/track</code> together.</p>

<p>For example, if you’re sending consecutive requests for the same user over a short period of time, race conditions are possible with the asynchronous <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint, but with the <code class="language-plaintext highlighter-rouge">/users/track/sync</code> endpoint you can send those requests in sequence, each after receiving a <code class="language-plaintext highlighter-rouge">2XX</code> response.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.track.sync</code> permission.</p>

<p>Customers using the API for server-to-server calls may need to allowlist <code class="language-plaintext highlighter-rouge">rest.iad-01.braze.com</code> if they’re behind a firewall.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>We apply a base speed limit of 500 requests per minute to this endpoint for all customers. Each <code class="language-plaintext highlighter-rouge">/users/track/sync</code> request can contain up to one event object, one attribute object, or one purchase object. Each object (event, attribute, and purchase arrays) can update one user each.</p>

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
  </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"events"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">event</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
  </span><span class="nl">"purchases"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">one</span><span class="w"> </span><span class="err">purchase</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w">
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
      <td>One attributes object</td>
      <td>See <a href="/docs/api/objects_filters/user_attributes_object/#migrating-push-tokens">user attributes object</a></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">events</code></td>
      <td>Optional</td>
      <td>One event object</td>
      <td>See <a href="/docs/api/objects_filters/event_object/">events object</a></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">purchases</code></td>
      <td>Optional</td>
      <td>One purchase object</td>
      <td>See <a href="/docs/api/objects_filters/purchase_object/">purchases object</a></td>
    </tr>
  </tbody>
</table>

<h2 id="responses">Responses</h2>

<p>When using this endpoint’s <a href="#request-parameters">request parameters</a>, you should receive one of the following responses: a successful message or a message with fatal errors.</p>

<h3 id="successful-message">Successful message</h3>

<p>Successful messages return the following response, which includes information about the user profile data that Braze updated.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"users"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request.</span><span class="w"> </span><span class="err">May</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">empty</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">no</span><span class="w"> </span><span class="err">users</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">found</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">_update_existing_only</span><span class="w"> </span><span class="err">key</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">set</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w">
        </span><span class="nl">"custom_attributes"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">result</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request.</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">lists</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">attributes</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w">
        </span><span class="nl">"custom_events"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">result</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request.</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">lists</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w">
        </span><span class="nl">"purchase_events"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">object)</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">purchase</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">result</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request.</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">lists</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">purchase</span><span class="w"> </span><span class="err">events</span><span class="w"> </span><span class="err">from</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">request</span><span class="p">,</span><span class="w">
    </span><span class="p">}</span><span class="err">,</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="message-with-fatal-errors">Message with fatal errors</h3>

<p>If your message has a fatal error, you’ll receive the following response:</p>

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

<h2 id="example-requests-and-responses">Example requests and responses</h2>

<h3 id="update-a-custom-attribute-by-external-id">Update a custom attribute by external ID</h3>

<h4 id="request">Request</h4>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h4 id="response">Response</h4>

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
</pre></td><td class="rouge-code"><pre>{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="update-a-custom-event-by-email">Update a custom event by email</h3>

<h4 id="request-1">Request</h4>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
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
        }
    ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h4 id="response-1">Response</h4>

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
</pre></td><td class="rouge-code"><pre>{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="update-a-purchase-event-by-user-alias">Update a purchase event by user alias</h3>

<h4 id="request-2">Request</h4>

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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h4 id="response-2">Response</h4>

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
</pre></td><td class="rouge-code"><pre>{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="frequently-asked-questions">Frequently asked questions</h2>

<h3 id="should-i-use-the-asynchronous-or-synchronous-endpoint">Should I use the asynchronous or synchronous endpoint?</h3>

<p>For most profile updates, the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint works best because of its higher rate limit and flexibility to let you batch requests. However, the <code class="language-plaintext highlighter-rouge">/users/track/sync</code> endpoint is useful if you’re experiencing race conditions due to rapid, consecutive requests for the same user.</p>

<h3 id="does-the-response-time-differ-from-the-userstrack-endpoint">Does the response time differ from the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint?</h3>

<p>With a synchronous call, the API waits until Braze completes the request to return a response. As a result, synchronous requests take longer on average than asynchronous requests to <code class="language-plaintext highlighter-rouge">/users/track</code>. For the majority of requests, you can expect a response within seconds.</p>

<h3 id="can-i-send-multiple-requests-at-the-same-time">Can I send multiple requests at the same time?</h3>

<p>Yes, as long as the requests are for different users, or each request updates different attributes, events, purchases for one user.</p>

<p>If you’re sending multiple requests for a user, for the same attribute, event, or purchase, Braze recommends waiting for a successful response between each request to prevent race conditions from occurring.</p>

<h3 id="why-doesnt-the-response-value-match-the-one-in-my-original-request">Why doesn’t the response value match the one in my original request?</h3>

<p>Although your request is completed, it’s possible your custom attribute value didn’t update. This can happen when your custom attribute update exceeds the maximum number of characters, exceeds array limits, or if the user does not exist in Braze and you have <code class="language-plaintext highlighter-rouge">_update_existing_only = true</code>.</p>

<p>In these cases, treat the response as an indication that your request, while completed, your desired update has not been made. Troubleshoot with the reasons why this may happen from above.</p>

</div>
