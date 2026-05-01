<div id='api_hgbkudkcbjgb' class='api_div'>
<h1 id="update-live-activity">Update Live Activity</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/messages/live_activity/update</p>
</div>

<blockquote>
  <p>Use this endpoint to update and end <a href="/docs/developer_guide/push_notifications/live_notifications/?sdktab=swift">Live Activities</a> displayed by your iOS app. This endpoint requires additional setup.</p>
</blockquote>

<p>After you register a Live Activity, you can pass a JSON payload to update your Apple Push Notification service (APNs). See Apple’s documentation on <a href="https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications">updating your Live Activity with push notification payloads</a> for more information.</p>

<p>If <code class="language-plaintext highlighter-rouge">content-available</code> isn’t set, the default Apple Push Notification service (APNs) priority is 10. If <code class="language-plaintext highlighter-rouge">content-available</code> is set, this priority is 5. Refer to <a href="/docs/api/objects_filters/messaging/apple_object">Apple push object</a> for more details.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need to complete the following:</p>

<ul>
  <li>Generate an API key with the <code class="language-plaintext highlighter-rouge">messages.live_activity.update</code> permission.</li>
  <li>Register a Live Activity <a href="/docs/developer_guide/push_notifications/live_notifications/?tab=remote&amp;sdktab=swift">remotely</a> or <a href="/docs/developer_guide/push_notifications/live_notifications/?tab=local&amp;sdktab=swift">locally</a> using the Braze Swift SDK.</li>
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
   </span><span class="nl">"app_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, string) App API identifier retrieved from the Developer Console."</span><span class="p">,</span><span class="w">
   </span><span class="nl">"activity_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update."</span><span class="p">,</span><span class="w">
   </span><span class="nl">"content_state"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined."</span><span class="p">,</span><span class="w">
   </span><span class="nl">"end_activity"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(optional, boolean) If true, this request ends the Live Activity."</span><span class="p">,</span><span class="w">
   </span><span class="nl">"dismissal_date"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately."</span><span class="p">,</span><span class="w">
   </span><span class="nl">"stale_date"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI."</span><span class="p">,</span><span class="w">
   </span><span class="nl">"notification"</span><span class="p">:</span><span class="w"> </span><span class="s2">"(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."</span><span class="w">
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
      <td>When you register your Live Activity using <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class"><code class="language-plaintext highlighter-rouge">launchActivity</code></a>, you use the <code class="language-plaintext highlighter-rouge">pushTokenTag</code> parameter to name the Activity’s push token to a custom string.<br /><br />Set <code class="language-plaintext highlighter-rouge">activity_id</code> to this custom string to define which Live Activity you want to update.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">content_state</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>You define the <code class="language-plaintext highlighter-rouge">ContentState</code> parameters when you create your Live Activity. Pass the updated values for your <code class="language-plaintext highlighter-rouge">ContentState</code> using this object.<br /><br />The format of this request must match the shape you initially defined.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">end_activity</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>If <code class="language-plaintext highlighter-rouge">true</code>, this request ends the Live Activity.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">dismissal_date</code></td>
      <td>Optional</td>
      <td>Datetime <br />(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> string)</td>
      <td>This parameter defines the time to remove the Live Activity from the user’s UI. If this time is in the past and <code class="language-plaintext highlighter-rouge">end_activity</code> is <code class="language-plaintext highlighter-rouge">true</code>, the Live Activity will be removed immediately.<br /><br /> If <code class="language-plaintext highlighter-rouge">end_activity</code> is <code class="language-plaintext highlighter-rouge">false</code> or omitted, this parameter only updates the Live Activity.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">stale_date</code></td>
      <td>Optional</td>
      <td>Datetime <br />(<a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601</a> string)</td>
      <td>This parameter tells the system when the Live Activity content is marked as outdated in the user’s UI.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">notification</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>Include an <a href="/docs/api/objects_filters/messaging/apple_object/"><code class="language-plaintext highlighter-rouge">apple_push</code></a> object to define a push notification. The behavior of this push notification depends on if the user is active or if the user is using a proxy device. <ul><li>If a <code>notification</code> is included and the user is active on their iPhone when the update is delivered, the updated Live Activity UI will slide down and display like a push notification.</li><li>If a <code>notification</code> is included and the user is not active on their iPhone, their screen will light up to display the updated Live Activity UI on their lock screen.</li><li>The <code>notification alert</code> will not display as a standard push notification. Additionally, if a user has a proxy device, like an Apple Watch, the <code>alert</code> will be displayed there.</li></ul></td>
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
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> POST <span class="s1">'https://rest.iad-01.braze.com/messages/live_activity/update'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer {YOUR-REST-API-KEY}'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It'</span>s halftime! Let<span class="s1">'s look at the scores",
            "title": "Halftime"
        }
    }
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
