<div id='api_mozszziouqum' class='api_div'>
<h1 id="create-email-template">Create email template</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/templates/email/create</p>
</div>

<blockquote>
  <p>Use this endpoint to create email templates on the Braze dashboard.</p>
</blockquote>

<p>These templates will be available on the <strong>Templates &amp; Media</strong> page. The response from this endpoint includes a field for <code class="language-plaintext highlighter-rouge">email_template_id</code>, which can be used to update the template in subsequent API calls.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>
<p>To use this endpoint, you’ll need an <a href="/docs/api/api_key/">API key</a> with the <code class="language-plaintext highlighter-rouge">templates.email.create</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
   </span><span class="nl">"template_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="p">,</span><span class="w">
   </span><span class="nl">"subject"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">subject</span><span class="w"> </span><span class="err">line</span><span class="p">,</span><span class="w">
   </span><span class="nl">"body"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">body</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">may</span><span class="w"> </span><span class="err">include</span><span class="w"> </span><span class="err">HTML</span><span class="p">,</span><span class="w">
   </span><span class="nl">"plaintext_body"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">A</span><span class="w"> </span><span class="err">plaintext</span><span class="w"> </span><span class="err">version</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">template</span><span class="w"> </span><span class="err">body</span><span class="p">,</span><span class="w">
   </span><span class="nl">"preheader"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">The</span><span class="w"> </span><span class="err">email</span><span class="w"> </span><span class="err">preheader</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">generate</span><span class="w"> </span><span class="err">previews</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">some</span><span class="w"> </span><span class="err">clients</span><span class="p">,</span><span class="w">
   </span><span class="nl">"tags"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">Array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">Strings)</span><span class="w"> </span><span class="err">Tags</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">already</span><span class="w"> </span><span class="err">exist</span><span class="p">,</span><span class="w">
   </span><span class="nl">"should_inline_css"</span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">Boolean)</span><span class="w"> </span><span class="err">If</span><span class="w"> </span><span class="err">`</span><span class="kc">true</span><span class="err">`</span><span class="p">,</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">`inline_css`</span><span class="w"> </span><span class="err">feature</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">on</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">template.</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">template_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Name of your email template.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">subject</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Email template subject line.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">body</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Email template body that may include HTML. Up to 400 KB.</td>
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
      <td>Enables or disables the <code class="language-plaintext highlighter-rouge">inline_css</code> feature per template. If not provided, Braze will use the default setting for the app group. One of <code class="language-plaintext highlighter-rouge">true</code> or <code class="language-plaintext highlighter-rouge">false</code> is expected.</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="example-response">Example response</h2>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"email_template_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"232b6d29-7e41-4106-a0ab-1c4fe915d701"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

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
      <td>Email must have valid Content Block names</td>
      <td>The email might contain Content Blocks that don’t exist in this environment.</td>
    </tr>
    <tr>
      <td>Invalid value for <code class="language-plaintext highlighter-rouge">should_inline_css</code>. One of <code class="language-plaintext highlighter-rouge">true</code> or <code class="language-plaintext highlighter-rouge">false</code> was expected</td>
      <td>This parameter only accepts boolean values (true or false). Make sure the value for <code class="language-plaintext highlighter-rouge">should_inline_css</code> is not encapsulated in quotes (<code class="language-plaintext highlighter-rouge">""</code>), which causes the value to be sent as a string instead.</td>
    </tr>
  </tbody>
</table>

</div>
