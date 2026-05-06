<div id='api_mlofusbhemyz' class='api_div'>
<h1 id="search-existing-dashboard-user-account-by-email">Search existing dashboard user account by email</h1>
<div class="api_type"><div class="method get ">get</div>
<p>scim/v2/Users?filter=userName%20eq%20”user%40test.com”</p>
</div>

<blockquote>
  <p>Use this endpoint to look up an existing dashboard user account by specifying their email in the filter query parameter.</p>
</blockquote>

<p>Note that when the query parameter is URL encoded it will read like this:</p>

<p><code class="language-plaintext highlighter-rouge">/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22</code></p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need a SCIM token. You’ll use your service origin as the <code class="language-plaintext highlighter-rouge">X-Request-Origin</code> header. For more information, refer to <a href="/docs/scim/automated_user_provisioning/">Automated user provisioning</a>.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

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
      <td><code class="language-plaintext highlighter-rouge">userName@example.com</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The user’s email.</td>
    </tr>
  </tbody>
</table>

<h2 id="request-parameters">Request parameters</h2>

<div class="language-http highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="err">Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="example-request">Example request</h2>
<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> GET <span class="se">\ </span><span class="s1">'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@test.com%22'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR-API-KEY-HERE'</span> <span class="se">\</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"schemas"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"urn:ietf:params:scim:api:messages:2.0:ListResponse"</span><span class="p">],</span><span class="w">
    </span><span class="nl">"totalResults"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w">
    </span><span class="nl">"Resources"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"userName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"user@test.com"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"dfa245b7-24195aec-887bb3ad-602b3340"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="nl">"givenName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"familyName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"User"</span><span class="w">
            </span><span class="p">},</span><span class="w">
            </span><span class="nl">"department"</span><span class="p">:</span><span class="w"> </span><span class="s2">"finance"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"lastSignInAt"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Thursday, January 1, 1970 12:00:00 AM"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"permissions"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
                </span><span class="nl">"companyPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"manage_company_settings"</span><span class="p">],</span><span class="w">
                </span><span class="nl">"appGroup"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                        </span><span class="nl">"appGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"241adcd25789fabcded"</span><span class="p">,</span><span class="w">
                        </span><span class="nl">"appGroupName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test Workspace"</span><span class="p">,</span><span class="w">
                        </span><span class="nl">"appGroupPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"basic_access"</span><span class="p">,</span><span class="s2">"send_campaigns_canvases"</span><span class="p">],</span><span class="w">
                        </span><span class="nl">"team"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                            </span><span class="p">{</span><span class="w">
                                </span><span class="nl">"teamId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"241adcd25789fabcded"</span><span class="p">,</span><span class="w">
                                </span><span class="nl">"teamName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test Team"</span><span class="p">,</span><span class="w">
                                </span><span class="nl">"teamPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"admin"</span><span class="p">]</span><span class="w">
                            </span><span class="p">}</span><span class="w">
                        </span><span class="p">]</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">]</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">}</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>

