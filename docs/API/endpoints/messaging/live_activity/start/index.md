<div id='api_fveczujpwbkw' class='api_div'>
<h1 id="start-live-activity">Start Live Activity</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/messages/live_activity/start</p>
</div>

<blockquote>
  <p>Use this endpoint to remotely start <a href="/docs/developer_guide/push_notifications/live_notifications/?sdktab=swift">Live Activities</a> displayed in your iOS app. This endpoint requires additional setup.</p>
</blockquote>

<p>After you create a Live Activity, you can make a POST request to remotely start your activity for any given segment. For more information about Apple’s Live Activities, see <a href="https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications">Starting and updating Live Activities with ActivityKit push notifications</a>.</p>

<p>If <code class="language-plaintext highlighter-rouge">content-available</code> isn’t set, the default Apple Push Notification service (APNs) priority is 10. If <code class="language-plaintext highlighter-rouge">content-available</code> is set, this priority is 5. Refer to <a href="/docs/api/objects_filters/messaging/apple_object">Apple push object</a> for more details.</p>

<p><strong>Tip:</strong></p>

<p>To end a Live Activity, use the <a href="/docs/api/endpoints/messaging/live_activity/update/"><code class="language-plaintext highlighter-rouge">/messages/live_activity/update</code></a> endpoint with <code class="language-plaintext highlighter-rouge">end_activity</code> set to <code class="language-plaintext highlighter-rouge">true</code>.</p>

<h2 id="arranging-automatic-dismissal">Arranging automatic dismissal</h2>

<p>To arrange automatic dismissal after a Live Activity starts, schedule a follow-up request to the update endpoint from your backend.</p>

<ol>
  <li>Send a <code class="language-plaintext highlighter-rouge">/messages/live_activity/start</code> request with an <code class="language-plaintext highlighter-rouge">activity_id</code> you can reuse later.</li>
  <li>Store that <code class="language-plaintext highlighter-rouge">activity_id</code> and your target end time in your backend scheduler.</li>
  <li>At the target end time, send a <code class="language-plaintext highlighter-rouge">/messages/live_activity/update</code> request with <code class="language-plaintext highlighter-rouge">end_activity</code> set to <code class="language-plaintext highlighter-rouge">true</code>.</li>
  <li>Configure dismissal behavior in the same update request. For details, see the <a href="/docs/api/endpoints/messaging/live_activity/update/"><code class="language-plaintext highlighter-rouge">/messages/live_activity/update</code></a> endpoint.</li>
  <li>Verify send and outcome events in the <a href="/docs/user_guide/administrative/app_settings/message_activity_log_tab/">Message Activity Log</a>.</li>
</ol>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need to complete the following:</p>

<ul>
  <li>Generate an API key with the <code class="language-plaintext highlighter-rouge">messages.live_activity.start</code> permission.</li>
  <li><a href="/docs/developer_guide/push_notifications/live_notifications/?tab=local&amp;sdktab=swift#swift_create-an-activity">Create a Live Activity</a> using the Braze Swift SDK.</li>
</ul>

<p><strong>Important:</strong></p>

<p>If the final rendered payload is larger than the corresponding service’s maximum allowed size, the send won’t be successful.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-body">Request body</h2>

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
  </span><span class="nl">"app_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, string) App API identifier retrieved from the Developer Console."</span><span class="p">,</span><span class="w">
  </span><span class="nl">"activity_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, string) Define a custom string as your `activity_id`. You will use this ID when you wish to send update or end events to your Live Activity."</span><span class="p">,</span><span class="w">
  </span><span class="nl">"activity_attributes_type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"activity_attributes"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"content_state"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined."</span><span class="p">,</span><span class="w">
  </span><span class="nl">"stale_date"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI."</span><span class="p">,</span><span class="w">
  </span><span class="nl">"notification"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Should include `notification.alert.title` and `notification.alert.body`"</span><span class="p">,</span><span class="w">
  </span><span class="err">//</span><span class="w"> </span><span class="err">One</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">following:</span><span class="w">
  </span><span class="nl">"external_user_ids"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(optional, array of strings) see external user identifier, maximum 50"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"custom_audience"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(optional, connected audience object) see connected audience"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"segment_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(optional, string) see segment identifier"</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">app_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>App <a href="/docs/api/identifier_types/#the-app-identifier">API identifier</a> retrieved from the <a href="/docs/user_guide/administer/global/workspace_settings/apis_and_identifiers/">API Keys</a> page.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">activity_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Define a custom string as your <code class="language-plaintext highlighter-rouge">activity_id</code>. You will use this ID when you wish to send update or end events to your Live Activity.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">activity_attributes_type</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The activity attributes type you define within <code class="language-plaintext highlighter-rouge">liveActivities.registerPushToStart</code> in your app.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">activity_attributes</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>The static attribute values for the activity type (such as the sports team names, which don’t change).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">content_state</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>You define the <code class="language-plaintext highlighter-rouge">ContentState</code> parameters when you create your Live Activity. Pass the updated values for your <code class="language-plaintext highlighter-rouge">ContentState</code> using this object.<br /><br />The format of this request must match the shape you initially defined.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">stale_date</code></td>
      <td>Optional</td>
      <td>Datetime <br />(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> string)</td>
      <td>This parameter tells the system when the Live Activity content is marked as outdated in the user’s UI.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">notification</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Include an <a href="/docs/api/objects_filters/messaging/apple_object/"><code class="language-plaintext highlighter-rouge">apple_push</code></a> object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. <ul><li>If a <code>notification</code> is included and the user is active on their iPhone when the update is delivered, the updated Live Activity UI will slide down and display like a push notification.</li><li>If a <code>notification</code> is included and the user is not active on their iPhone, their screen will light up to display the updated Live Activity UI on their lock screen.</li><li>The <code>notification alert</code> will not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the <code>alert</code> will be displayed there.</li></ul></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external_user_ids</code></td>
      <td>Optional if <code class="language-plaintext highlighter-rouge">segment_id</code> or <code class="language-plaintext highlighter-rouge">audience</code> is provided</td>
      <td>Array of strings</td>
      <td>See <a href="/docs/api/objects_filters/user_attributes_object/#braze-user-profile-fields">external user ID</a>. Maximum 50 external user IDs.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">segment_id </code></td>
      <td>Optional if <code class="language-plaintext highlighter-rouge">external_user_ids</code> or <code class="language-plaintext highlighter-rouge">audience</code> is provided</td>
      <td>String</td>
      <td>See <a href="/docs/api/identifier_types/">segment identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">custom_audience</code></td>
      <td>Optional if <code class="language-plaintext highlighter-rouge">external_user_ids</code> or <code class="language-plaintext highlighter-rouge">segment_id</code> is provided</td>
      <td>Connected audience object</td>
      <td>See <a href="/docs/api/objects_filters/connected_audience/">connected audience</a>.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

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
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/messages/live_activity/start'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer {YOUR-REST-API-KEY}'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "football-chiefs-bills-2024-01-21",
    "content_state": {
        "teamOneScore": 0,
        "teamTwoScore": 0
    },
    "activity_attributes_type": "FootballActivity",
    "activity_attributes": {
        "team1Name": "Chiefs",
        "team2Name": "Bills"
    },
    "stale_date": "2024-01-22T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "The game is starting! Tune in soon!",
            "title": "Chiefs v. Bills"
        }
    },
    // One of the following required:
    "segment_id": "{YOUR-SEGMENT-API-IDENTIFIER}", // Optional
    "custom_audience": {...}, // Optional
    "external_user_ids": ["user-id1", "user-id2"], // Optional
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>There are two status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">201</code> and <code class="language-plaintext highlighter-rouge">4XX</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>A <code class="language-plaintext highlighter-rouge">201</code> status code is returned if the request was formatted correctly and we received the request. The status code <code class="language-plaintext highlighter-rouge">201</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="example-error-response">Example error response</h3>

<p>The <code class="language-plaintext highlighter-rouge">4XX</code> class of status code indicates a client error. Refer to the <a href="/docs/api/errors/">API errors and responses article</a> for more information about errors you may encounter.</p>

<p>The status code <code class="language-plaintext highlighter-rouge">400</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"error"</span><span class="p">:</span><span class="w"> </span><span class="s2">"</span><span class="se">\n</span><span class="s2">Problem:</span><span class="se">\n</span><span class="s2">  message body does not match declared format</span><span class="se">\n</span><span class="s2">Resolution:</span><span class="se">\n</span><span class="s2">  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
