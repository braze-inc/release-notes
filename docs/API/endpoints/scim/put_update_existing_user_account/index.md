<div id='api_yuvprftjtmbh' class='api_div'>
<h1 id="update-dashboard-user-account">Update dashboard user account</h1>
<div class="api_type"><div class="method put ">put</div>
<p>/scim/v2/Users/{id}</p>
</div>

<blockquote>
  <p>Use this endpoint to update an existing dashboard user account by specifying the resource <code class="language-plaintext highlighter-rouge">id</code> returned by the SCIM <a href="/docs/api/endpoints/scim/post_create_user_account/"><code class="language-plaintext highlighter-rouge">POST</code></a> method.</p>
</blockquote>

<p>It allows you to update of given and family names, permissions (for setting permissions at the company, workspace, and team level) and department.</p>

<p>For security reasons, <code class="language-plaintext highlighter-rouge">userName</code> (email address) cannot be updated through this endpoint. If you want to change the <code class="language-plaintext highlighter-rouge">userName</code> (email address) for a user, contact <a href="/docs/support_contact/">Support</a>.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f9a1642-988e-4011-8fb8-db4340ea1ac7" class="seeme">See me in Postman</a></div>

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
      <td><code class="language-plaintext highlighter-rouge">id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The user’s resource ID. This parameter is returned by the  <code class="language-plaintext highlighter-rouge">POST</code> <code class="language-plaintext highlighter-rouge">/scim/v2/Users/</code> or <code class="language-plaintext highlighter-rouge">GET</code>  <code class="language-plaintext highlighter-rouge">/scim/v2/Users?filter=userName eq "user@test.com"</code> methods.</td>
    </tr>
  </tbody>
</table>

<h2 id="request-body">Request body</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-KEY
</pre></td></tr></tbody></table></code></pre></div></div>
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"schemas"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"urn:ietf:params:scim:schemas:core:2.0:User"</span><span class="p">],</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"givenName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"familyName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"User"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"department"</span><span class="p">:</span><span class="w"> </span><span class="s2">"finance"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"permissions"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"companyPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"manage_company_settings"</span><span class="p">],</span><span class="w">
        </span><span class="nl">"roles"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"roleName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test Role"</span><span class="w">
            </span><span class="p">},</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"roleId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2519dafcdba238ae7"</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">],</span><span class="w">
        </span><span class="nl">"appGroup"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"appGroupName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test Workspace"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"appGroupPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"basic_access"</span><span class="p">,</span><span class="s2">"send_campaigns_canvases"</span><span class="p">],</span><span class="w">
                </span><span class="nl">"team"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                         </span><span class="nl">"teamName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test Team"</span><span class="p">,</span><span class="w">
                         </span><span class="nl">"teamPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"admin"</span><span class="p">]</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">]</span><span class="w">
            </span><span class="p">},</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"appGroupName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Other Test Workspace"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"appGroupPermissionSets"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                        </span><span class="nl">"appGroupPermissionSetName"</span><span class="p">:</span><span class="w">  </span><span class="s2">"Test Permission Set"</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">]</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">]</span><span class="w">
   </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="request-parameters">Request parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" role="presentation">
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Required</th>
      <th>Data type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">schemas</code></td>
      <td>Required</td>
      <td>Array of strings</td>
      <td>Expected SCIM 2.0 schema name for user object.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code></td>
      <td>Required</td>
      <td>JSON object</td>
      <td>This object contains the user’s given name and family name.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">department</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Valid department string from the <a href="/docs/scim_api_appendix/#department-strings">department string documentation</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">permissions</code></td>
      <td>Required</td>
      <td>JSON object</td>
      <td>Permissions object as described in the <a href="/docs/scim_api_appendix/#permissions-object">permissions object documentation</a>.</td>
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
28
29
30
31
32
33
34
35
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> PUT <span class="s1">'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR-SCIM-TOKEN-HERE'</span> <span class="se">\</span>
<span class="nt">--data</span> raw <span class="s1">'{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Test Role"
            },
            {
                "roleId": "2519dafcdba238ae7"
            }
        ],
        "appGroup": [
            {
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaign_canvases"],
                "team": [
                    {
                         "teamName": "Test Team",
                         "teamPermissions": ["admin"]
                    }
                ]
            }
        ]
    }
}
</span></pre></td></tr></tbody></table></code></pre></div></div>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"schemas"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"urn:ietf:params:scim:schemas:core:2.0:User"</span><span class="p">],</span><span class="w">
    </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"dfa245b7-24195aec-887bb3ad-602b3340"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"userName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"user@test.com"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"givenName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"familyName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"User"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"department"</span><span class="p">:</span><span class="w"> </span><span class="s2">"finance"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"lastSignInAt"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Thursday, January 1, 1970 12:00:00 AM"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"permissions"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
        </span><span class="nl">"companyPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"manage_company_settings"</span><span class="p">],</span><span class="w">
        </span><span class="nl">"roles"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"roleName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test Role"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"roleId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"519dafcdba23dfaae7"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"appGroup"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                        </span><span class="nl">"appGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"241adcd25789fabcded"</span><span class="p">,</span><span class="w">
                        </span><span class="nl">"appGroupName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Some Workspace"</span><span class="p">,</span><span class="w">
                        </span><span class="nl">"appGroupPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"basic_access"</span><span class="p">,</span><span class="w"> </span><span class="s2">"publish_cards"</span><span class="p">],</span><span class="w">
                        </span><span class="nl">"team"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                            </span><span class="p">{</span><span class="w">
                                </span><span class="nl">"teamId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2519dafcdba238ae7"</span><span class="p">,</span><span class="w">
                                </span><span class="nl">"teamName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Some Team"</span><span class="p">,</span><span class="w">
                                </span><span class="nl">"teamPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"export_user_data"</span><span class="p">]</span><span class="w">
                            </span><span class="p">}</span><span class="w">
                        </span><span class="p">]</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">]</span><span class="w">
            </span><span class="p">},</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"roleName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Another Test Role"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"roleId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"23125dad23dfaae7"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"appGroup"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                        </span><span class="nl">"appGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"241adcd25adfabcded"</span><span class="p">,</span><span class="w">
                        </span><span class="nl">"appGroupName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Production Workspace"</span><span class="p">,</span><span class="w">
                        </span><span class="nl">"appGroupPermissionSets"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                            </span><span class="p">{</span><span class="w">
                                </span><span class="nl">"appGroupPermissionSetName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"A Permission Set"</span><span class="p">,</span><span class="w">
                                </span><span class="nl">"appGroupPermissionSetId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"dfa385109bc38"</span><span class="p">,</span><span class="w">
                                </span><span class="nl">"permissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"basic_access"</span><span class="p">,</span><span class="s2">"publish_cards"</span><span class="p">]</span><span class="w">
                            </span><span class="p">}</span><span class="w">
                        </span><span class="p">]</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">]</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">],</span><span class="w">
        </span><span class="nl">"appGroup"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
            </span><span class="p">{</span><span class="w">
                </span><span class="nl">"appGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"241adcd25789fabcded"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"appGroupName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test Workspace"</span><span class="p">,</span><span class="w">
                </span><span class="nl">"appGroupPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"basic_access"</span><span class="p">,</span><span class="s2">"send_campaigns_canvases"</span><span class="p">],</span><span class="w">
                </span><span class="nl">"team"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
                    </span><span class="p">{</span><span class="w">
                         </span><span class="nl">"teamId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2519dafcdba238ae7"</span><span class="p">,</span><span class="w">
                         </span><span class="nl">"teamName"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Test Team"</span><span class="p">,</span><span class="w">
                         </span><span class="nl">"teamPermissions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"admin"</span><span class="p">]</span><span class="w">
                    </span><span class="p">}</span><span class="w">
                </span><span class="p">]</span><span class="w">
            </span><span class="p">}</span><span class="w">
        </span><span class="p">]</span><span class="w">
    </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="error-states">Error states</h3>
<p>If a user with this ID doesn’t exist in Braze, the endpoint will respond with:</p>

<div class="language-http highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre><span class="k">HTTP</span><span class="o">/</span><span class="m">1.1</span> <span class="m">404</span> <span class="ne">Not Found</span>
<span class="na">Content-Type</span><span class="p">:</span> <span class="s">text/html; charset=UTF-8</span>

{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "detail": "User not found",
    "status": 404
}
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
