<div id='api_dsipdtzlkgyi' class='api_div'>
<h1 id="list-users-subscription-groups">List user’s subscription groups</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/subscription/user/status</p>
</div>

<blockquote>
  <p>Use this endpoint to list and get the subscription groups with the history of a certain user.</p>
</blockquote>

<p>If you want to see examples or test this endpoint for <strong>Email Subscription Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d1c3b617-22f1-47bf-9ee8-499526824470" class="seeme">See me in Postman</a></div>

<p>If you want to see examples or test this endpoint for <strong>SMS Subscription Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666" class="seeme">See me in Postman</a></div>

<p>If you want to see examples or test this endpoint for <strong>WhatsApp Groups</strong>:</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#54bd7ca8-60d9-4654-aff5-406479f3c666" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">subscription.groups.get</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-parameters">Request parameters</h2>

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
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The <code class="language-plaintext highlighter-rouge">external_id</code> of the user (must include at least one and at most 50 <code class="language-plaintext highlighter-rouge">external_ids</code>).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">email</code></td>
      <td>Required*</td>
      <td>String</td>
      <td>The email address of the user, can be passed as an array of strings. Must include at least one email address (with a maximum of 50).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">phone</code></td>
      <td>Required*</td>
      <td>String in <a href="https://en.wikipedia.org/wiki/E.164">E.164</a> format</td>
      <td>The phone number of the user. Must include at least one phone number (with a maximum of 50).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">limit</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>The limit on the maximum number of results returned. Default (and maximum) <code class="language-plaintext highlighter-rouge">limit</code> is 100.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">offset</code></td>
      <td>Optional</td>
      <td>Integer</td>
      <td>Number of templates to skip before returning the rest of the templates that fit the search criteria.</td>
    </tr>
  </tbody>
</table>

<p><strong>Tip:</strong></p>

<p>If there are multiple users (multiple <code class="language-plaintext highlighter-rouge">external_ids</code>) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).</p>

<h2 id="example-request">Example request</h2>

<p><code class="language-plaintext highlighter-rouge">https://rest.iad-03.braze.com/subscription/user/status?external_id[]=1&amp;external_id[]=2</code></p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&amp;limit=100&amp;offset=1&amp;phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/user/status?external_id={{external_id}}&amp;email=example@braze.com&amp;limit=100&amp;offset=0' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="example-response">Example response</h2>

<p>Only subscription groups that have had a subscription status update in a user’s history will be included in a successful response. This means that newly created subscription groups will not be listed.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"users"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"email"</span><span class="p">:</span><span class="w"> </span><span class="s2">"test@example.com"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"phone"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50505050"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"external_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"20500"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"subscription_groups"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                </span><span class="p">{</span><span class="w">
                  </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ec2fcc919fca"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ActivationGroup"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"email"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Subscribed"</span><span class="w">
                </span><span class="p">},</span><span class="w">
                </span><span class="p">{</span><span class="w">
                  </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"7d7af9dd5556"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ReactivationGroup"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"email"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Subscribed"</span><span class="w">
                </span><span class="p">},</span><span class="w">
                </span><span class="p">{</span><span class="w">
                  </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"a5e84fd16220"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"MarketingGroup"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sms"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unsubscribed"</span><span class="w">
                </span><span class="p">},</span><span class="w">
                </span><span class="p">{</span><span class="w">
                  </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"64d8cad9176c"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"TransactionalGroup"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sms"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unsubscribed"</span><span class="w">
                </span><span class="p">},</span><span class="w">
                </span><span class="p">{</span><span class="w">
                  </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b2134cd63942"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"BankerMarketingGroup"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"channel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sms"</span><span class="p">,</span><span class="w">
                  </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Subscribed"</span><span class="w">
                </span><span class="p">}</span><span class="w">
            </span><span class="p">]</span><span class="w">
        </span><span class="p">}</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"total_count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
