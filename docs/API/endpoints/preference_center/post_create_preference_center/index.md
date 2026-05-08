<div id='api_zfokmykckzif' class='api_div'>
<h1 id="create-preference-center">Create preference center</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/preference_center/v1</p>
</div>

<blockquote>
  <p>Use this endpoint to create a preference center to allow users to manage their notification preferences for your email campaigns. Refer to <a href="/docs/user_guide/message_building_by_channel/email/preference_center/overview/#creating-a-preference-center-with-api">Create a preference center with API</a> for steps on how to build an API-generated preference center.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e15d7065-2cbc-4eb3-ae16-32efe43357a6" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">preference_center.update</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-body">Request body</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"preference_center_title"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"preference_center_page_html"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"confirmation_page_html"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"state"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional)</span><span class="w"> </span><span class="err">Choose</span><span class="w"> </span><span class="err">`active`</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">`draft`.</span><span class="w"> </span><span class="err">Defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">`active`</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">specified</span><span class="p">,</span><span class="w">
  </span><span class="nl">"options"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"meta-viewport-content"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="err">(optional)</span><span class="w"> </span><span class="err">Only</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">`content`</span><span class="w"> </span><span class="err">value</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">meta</span><span class="w"> </span><span class="err">tag</span><span class="p">,</span><span class="w">
    </span><span class="nl">"links-tags"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"rel"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="err">(required)</span><span class="w"> </span><span class="err">One</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">following</span><span class="w"> </span><span class="s2">"icon"</span><span class="p">,</span><span class="w"> </span><span class="s2">"shortcut icon"</span><span class="p">,</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="s2">"apple-touch-icon"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="err">(optional)</span><span class="w"> </span><span class="err">Valid</span><span class="w"> </span><span class="err">values</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="s2">"image/png"</span><span class="p">,</span><span class="w"> </span><span class="s2">"image/svg"</span><span class="p">,</span><span class="w"> </span><span class="s2">"image/gif"</span><span class="p">,</span><span class="w"> </span><span class="s2">"image/x-icon"</span><span class="p">,</span><span class="w"> </span><span class="s2">"image/svg+xml"</span><span class="p">,</span><span class="w"> </span><span class="s2">"mask-icon"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"sizes"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="err">(optional)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"color"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="err">(optional)</span><span class="w"> </span><span class="err">Use</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">type=</span><span class="s2">"mask-icon"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"href"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="p">,</span><span class="w"> </span><span class="err">(required)</span><span class="w">
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
      <th>Data Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The name of the preference center that meets the following requirements: <br />- Only contains letters, numbers, hyphens, and underscores <br />- Does not have spaces</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">preference_center_title</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The title for the preference center and confirmation pages. If a title is not specified, the title of the pages will default to “Preference Center”.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">preference_center_page_html</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The HTML for the preference center page.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">confirmation_page_html</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The HTML for the confirmation page.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">state</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Choose <code class="language-plaintext highlighter-rouge">active</code> or <code class="language-plaintext highlighter-rouge">draft</code>. Defaults to <code class="language-plaintext highlighter-rouge">active</code> if not specified.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">options</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>Attributes: <br /><code class="language-plaintext highlighter-rouge">meta-viewport-content</code>: When present, a <code class="language-plaintext highlighter-rouge">viewport</code> meta tag will be added to the page with <code class="language-plaintext highlighter-rouge">content= &lt;value of attribute&gt;</code>.<br /><br /> <code class="language-plaintext highlighter-rouge">link-tags</code>: Set a favicon for the page. When set, a <code class="language-plaintext highlighter-rouge">&lt;link&gt;</code> tag with a rel attribute is added to the page.</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>The preference center name can’t be edited after it’s created.</p>

<h3 id="liquid-tags">Liquid tags</h3>

<p>Refer to the following Liquid tags that can be included in your HTML to generate a user’s subscription state on the preference center page.</p>

<h4 id="user-subscription-state">User subscription state</h4>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Liquid</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">{{subscribed_state.${email_global}}}</code></td>
      <td>Get the global email subscribed state for the user (such as “opted_in”, “subscribed”, or “unsubscribed”.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">{{subscribed_state.${&lt;subscription_group_id&gt;}}}</code></td>
      <td>Get the subscribed state of the specified subscription group for the user (such as “subscribed” or “unsubscribed”).</td>
    </tr>
  </tbody>
</table>

<h4 id="form-inputs-and-action">Form inputs and action</h4>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Liquid</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">{% form_field_name :email_global_state %}</code></td>
      <td>Indicates that a specific form input element corresponds to the user’s global email subscribed state. The user’s selection state should be “opted_in”, “subscribed”, or “unsubscribed” when the form is submitted with selection data for the global email subscribed state. If it’s a checkbox, the user will either be “opted_in” or “unsubscribed”. For a hidden input, the “subscribed” state will also be valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">{% form_field_name :subscription_group &lt;subscription_group_id&gt; %}</code></td>
      <td>Indicates that a specific form input element corresponds to a given subscription group. The user’s selection state should be either “subscribed” or “unsubscribed” when the form is submitted with selection data for a specific subscription group.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">{{preference_center_submit_url}}</code></td>
      <td>Generates URL for form submission.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-responses">Example responses</h2>

<h3 id="create-preference-center-1">Create preference center</h3>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre>{
  "preference_center_api_id": "preference_center_api_id_example",
  "liquid_tag": "{{preference_center.${MyPreferenceCenter2022-09-22}}}",
  "created_at": "2022-09-22T18:28:07+00:00",
  "message": "success"
}
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="html-with-form-inputs">HTML with form inputs</h3>

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
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
</pre></td><td class="rouge-code"><pre>&lt;!doctype html&gt;
&lt;html lang="en"&gt;
  &lt;head&gt;
    &lt;meta name="robots" content="noindex" /&gt;
    &lt;title&gt;Email Preferences&lt;/title&gt;
    &lt;script type="text/javascript"&gt;
      window.onload = () =&gt; {
        const globalUnsubscribed = '{{subscribed_state.${email_global}}}' == "unsubscribed";
        const globalSubscribedValue = '{{subscribed_state.${email_global}}}' == "opted_in" ? "opted_in" : "subscribed";
        const idStates = [
          // input format: [API_ID, '{{subscribed_state.${API_ID}}}' == "subscribed"][]
          ['3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec', '{{subscribed_state.${3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec}}}' == 'subscribed'],['7d89bdc3-4aa1-4592-8b8a-4c8b7161c875', '{{subscribed_state.${7d89bdc3-4aa1-4592-8b8a-4c8b7161c875}}}' == 'subscribed'],['5444d32e-2815-4258-964c-b9690d4ccb94', '{{subscribed_state.${5444d32e-2815-4258-964c-b9690d4ccb94}}}' == 'subscribed']
        ];

        const setState = (id, subscribed) =&gt; {
          document.querySelector(`#checkbox-${id}`).checked = subscribed;
          document.querySelector(`#value-${id}`).value = subscribed ? "subscribed" : "unsubscribed";
        };
        const setGlobal = (unsubscribed) =&gt; {
          document.querySelector(`#checkbox-global`).checked = unsubscribed;
          document.querySelector(`#value-global`).value = unsubscribed ? "unsubscribed" : globalSubscribedValue;
          idStates.forEach(([id]) =&gt; {
            document.querySelector(`#checkbox-${id}`).disabled = unsubscribed;
          });
        };

        idStates.forEach(([id, state]) =&gt; {
          setState(id, state);
          document.querySelector(`#checkbox-${id}`).onchange = ((e) =&gt; {
            setState(id, e.target.checked);
          });
        });
        setGlobal(globalUnsubscribed);
        document.querySelector(`#checkbox-global`).onchange = ((e) =&gt; {
          setGlobal(e.target.checked);
        });
      };
    &lt;/script&gt;
    &lt;style&gt;
      body {
        background: #fff;
        margin: 0;
      }
      @media (max-width: 600px) {
        .main-container {
          margin-top: 0;
          width: 100%;
        }
        .main-container .content .email-input {
          width: 100%;
        }
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body class="vsc-initialized" style="margin: 0" bgcolor="#fff"&gt;
    &lt;div
      class="main-container"
      style="
        background-color: #fff;
        color: #333335;
        font-family:
          Sailec W00 Medium,
          helvetica,
          arial,
          sans-serif;
        margin-left: auto;
        margin-right: auto;
        margin-top: 30px;
        width: 600px;
        padding: 15px 0 5px;
      "
    &gt;
      &lt;div class="content" style="margin-left: 20px; margin-right: 20px"&gt;

        &lt;div&gt;
          &lt;h1
            style="color: #3accdd; font-size: 27px; font-weight: 400; margin-bottom: 40px; margin-top: 0"
            align="center"
          &gt;
            Manage Email Preferences
          &lt;/h1&gt;
          &lt;p class="intro-text" style="font-size: 14px; margin-bottom: 20px" align="center"&gt;
            Select the emails that you want to receive.
          &lt;/p&gt;
        &lt;/div&gt;

        &lt;form action="{{ preference_center_submit_url }}" method="post" accept-charset="UTF-8"&gt;
          &lt;div&gt;
            &lt;h3 style="font-size: 15px; margin-bottom: 15px; margin-left: 5px; margin-top: 40px"&gt;
              Email Address: &lt;span class="displayed-email" style="font-weight: 400"&gt;{{${email_address}}}&lt;/span&gt;
            &lt;/h3&gt;
          &lt;/div&gt;
          &lt;div class="subscription-groups-holder" style="margin-bottom: 20px"&gt;&lt;div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);"&gt;
  &lt;label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;"&gt;
    &lt;input type="checkbox" id="checkbox-3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec" class="sub_group" style="margin-right: 4px;"&gt;
    &lt;input type="hidden" name="{% form_field_name :subscription_group 3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec %}" id="value-3d2ae07a-f2ff-4318-bdff-e394f2d3a4ec" /&gt;
    Sub Group 1
  &lt;/label&gt;
  &lt;p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;"&gt;

  &lt;/p&gt;
&lt;/div&gt;
&lt;div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);"&gt;
  &lt;label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;"&gt;
    &lt;input type="checkbox" id="checkbox-7d89bdc3-4aa1-4592-8b8a-4c8b7161c875" class="sub_group" style="margin-right: 4px;"&gt;
    &lt;input type="hidden" name="{% form_field_name :subscription_group 7d89bdc3-4aa1-4592-8b8a-4c8b7161c875 %}" id="value-7d89bdc3-4aa1-4592-8b8a-4c8b7161c875" /&gt;
    Sub Group 2
  &lt;/label&gt;
  &lt;p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;"&gt;

  &lt;/p&gt;
&lt;/div&gt;
&lt;div class="row" style="border-top-width: 1px; border-top-color: #dddde2; border-top-style: solid; background-color: #fff; padding: 15px 10px 14px;border-bottom: 1px solid rgb(221, 221, 226);"&gt;
  &lt;label style="color: #27368f; cursor: pointer; font-size: 15px; font-weight: 700;"&gt;
    &lt;input type="checkbox" id="checkbox-5444d32e-2815-4258-964c-b9690d4ccb94" class="sub_group" style="margin-right: 4px;"&gt;
    &lt;input type="hidden" name="{% form_field_name :subscription_group 5444d32e-2815-4258-964c-b9690d4ccb94 %}" id="value-5444d32e-2815-4258-964c-b9690d4ccb94" /&gt;
    Sub Group 3
  &lt;/label&gt;
  &lt;p class="subscription-group" style="font-size: 13px; line-height: 1.4em; min-height: 20px; padding-right: 20px; margin: 0 0 3px 23px;"&gt;

  &lt;/p&gt;
&lt;/div&gt;
&lt;/div&gt;

          &lt;div class="unsub-all" style="cursor: pointer; font-size: 13px; margin-bottom: 20px" align="center"&gt;
            &lt;label&gt;
              &lt;input type="checkbox" id="checkbox-global" /&gt;
              &lt;input
                type="hidden"
                id="value-global"
                name="{% form_field_name :email_global_state %}"
              /&gt;
              &lt;i&gt; Unsubscribe from all of the above types of emails &lt;/i&gt;
            &lt;/label&gt;
          &lt;/div&gt;

          &lt;div&gt;
            &lt;input
              class="save"
              type="submit"
              value="Save"
              style="
                background-color: rgb(71, 204, 163);
                color: #fff;
                cursor: pointer;
                display: block;
                font-size: 16px;
                text-align: center;
                text-decoration: none;
                width: 200px;
                margin: 0 auto 20px;
                padding: 12px;
                border-style: none;
              "
            /&gt;
          &lt;/div&gt;
        &lt;/form&gt;
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/body&gt;
&lt;/html&gt;
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
