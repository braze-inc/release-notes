<div id='api_efkfgzualejn' class='api_div'>
<h1 id="update-existing-email-templates">Update existing email templates</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/templates/email/update</p>
</div>

<blockquote>
  <p>Use this endpoint to update email templates on the Braze dashboard.</p>
</blockquote>

<p>You can access an email template’s <code class="language-plaintext highlighter-rouge">email_template_id</code> by navigating to it on the <strong>Templates &amp; Media</strong> page. The <a href="/docs/api/endpoints/templates/email_templates/post_create_email_template/">Create email template endpoint</a> will also return an <code class="language-plaintext highlighter-rouge">email_template_id</code> reference.</p>

<p>All fields other than the <code class="language-plaintext highlighter-rouge">email_template_id</code> are optional, but you must specify at least one field to update.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>
<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">templates.email.update</code> permission.</p>

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
6
7
8
9
10
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"email_template_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">Your</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template's</span><span class="w"> </span><span class="err">API</span><span class="w"> </span><span class="err">Identifier</span><span class="p">,</span><span class="w">
  </span><span class="nl">"template_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="p">,</span><span class="w">
  </span><span class="nl">"subject"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">subject</span><span class="w"> </span><span class="err">line</span><span class="p">,</span><span class="w">
  </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">may</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">HTML</span><span class="p">,</span><span class="w">
  </span><span class="nl">"plaintext_body"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">A</span><span class="w"> </span><span class="err">plaintext</span><span class="w"> </span><span class="err">version</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">body</span><span class="p">,</span><span class="w">
  </span><span class="nl">"preheader"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">preheader</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">generate</span><span class="w"> </span><span class="err">previews</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">some</span><span class="w"> </span><span class="err">clients</span><span class="p">,</span><span class="w">
  </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">Strings)</span><span class="w"> </span><span class="err">Tags</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">already</span><span class="w"> </span><span class="err">exist</span><span class="p">,</span><span class="w">
  </span><span class="nl">"should_inline_css"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">Boolean)</span><span class="w"> </span><span class="err">If</span><span class="w"> </span><span class="err">`</span><span class="kc">true</span><span class="err">`</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">`inline_css`</span><span class="w"> </span><span class="err">feature</span><span class="w"> </span><span class="err">will</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">applied</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">template.</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">email_template_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Your <a href="/docs/api/identifier_types/">email template’s API identifier</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">template_name</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Name of your email template.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">subject</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Email template subject line.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">body</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Email template body that may include HTML.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">plaintext_body</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A plaintext version of the email template body.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">preheader</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Email preheader used to generate previews in some clients.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">tags</code></td>
      <td>Optional</td>
      <td>String</td>
      <td><a href="/docs/user_guide/messaging/governance/tags/">Tags</a> must already exist.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">should_inline_css</code></td>
      <td>Optional</td>
      <td>Boolean</td>
      <td>Enables or disables the <code class="language-plaintext highlighter-rouge">inline_css</code> feature per template. If not provided, Braze will use the default setting for the AppGroup. One of <code class="language-plaintext highlighter-rouge">true</code> or <code class="language-plaintext highlighter-rouge">false</code> is expected.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<p>The following table lists possible returned errors and their associated troubleshooting steps, if applicable.</p>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Error</th>
      <th>Troubleshooting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Template name is required</td>
      <td>Enter a template name.</td>
    </tr>
    <tr>
      <td>Tags must be an array</td>
      <td>Tags must be formatted as an array of strings, for example <code class="language-plaintext highlighter-rouge">["marketing", "promotional", "transactional"]</code>.</td>
    </tr>
    <tr>
      <td>All tags must be strings</td>
      <td>Make sure your tags are encapsulated in quotes (<code class="language-plaintext highlighter-rouge">""</code>).</td>
    </tr>
    <tr>
      <td>Some tags could not be found</td>
      <td>To add a tag when creating an email template, the tag must already exist in Braze.</td>
    </tr>
    <tr>
      <td>Invalid value for <code class="language-plaintext highlighter-rouge">should_inline_css</code>. One of <code class="language-plaintext highlighter-rouge">true</code> or <code class="language-plaintext highlighter-rouge">false</code> was expected</td>
      <td>This parameter only accepts boolean values (true or false). Make sure the value for <code class="language-plaintext highlighter-rouge">should_inline_css</code> is not encapsulated in quotes (<code class="language-plaintext highlighter-rouge">""</code>), which causes the value to be sent as a string instead.</td>
    </tr>
  </tbody>
</table>

</div>
