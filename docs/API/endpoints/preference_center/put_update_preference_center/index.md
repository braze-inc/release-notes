<div id='api_lsttuhggrfff' class='api_div'>
<h1 id="update-preference-center">Update preference center</h1>
<div class="api_type"><div class="method put ">put</div>
<p>/preference_center/v1/{preferenceCenterExternalID}</p>
</div>

<blockquote>
  <p>Use this endpoint to update a preference center.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#bf1b43db-3f1b-461f-ad9a-2fbe35b804d7" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">preference_center.update</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-parameters">Path parameters</h2>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Path parameters">
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
      <td><code class="language-plaintext highlighter-rouge">preferenceCenterExternalID</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID for your preference center.</td>
    </tr>
  </tbody>
</table>

<h2 id="request-body">Request body</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
</pre></td><td class="rouge-code"><pre>Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
</pre></td></tr></tbody></table></code></pre></div></div>

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
</pre></td><td class="rouge-code"><pre>{
  "name": "preference_center_name",
  "preference_center_title": "string",
  "preference_center_page_html": "string",
  "confirmation_page_html": "string",
  "options": {
    "unknown macro": {links-tags}
  "options": {
    "meta-viewport-content": "string", (optional) Only the `content` value of the meta tag,
    "links-tags": [
      {
        "rel": "string", (required) One of: "icon", "shortcut icon", or "apple-touch-icon",
        "type": "string", (optional) Valid values: "image/png", "image/svg", "image/gif", "image/x-icon", "image/svg+xml", "mask-icon",
        "sizes": "string", (optional),
        "color": "string", (optional) Use when type="mask-icon",
        "href": "string", (required)
      }
    ]
  }
}
</pre></td></tr></tbody></table></code></pre></div></div>

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
      <td><code class="language-plaintext highlighter-rouge">preference_center_page_html</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The HTML for the preference center page.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">preference_center_title</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The title for the preference center and confirmation pages. If a title is not specified, the title of the pages will default to “Preference Center”.</td>
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
      <td>Choose <code class="language-plaintext highlighter-rouge">active</code> or <code class="language-plaintext highlighter-rouge">draft</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">options</code></td>
      <td>Optional</td>
      <td>Object</td>
      <td>Attributes: <br /><code class="language-plaintext highlighter-rouge">meta-viewport-content</code>: When present, a <code class="language-plaintext highlighter-rouge">viewport</code> meta tag will be added to the page with <code class="language-plaintext highlighter-rouge">content= &lt;value of attribute&gt;</code>.<br /><br /> <code class="language-plaintext highlighter-rouge">link-tags</code>: Set a favicon for the page. When set, a <code class="language-plaintext highlighter-rouge">&lt;link&gt;</code> tag with a rel attribute is added to the page.</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/preference_center/v1/{preferenceCenterExternalId}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "name": "Example",
  "preference_center_title": "Example Preference Center Title",
  "preference_center_page_html": "HTML for preference center here",
  "confirmation_page_html": "HTML here with a message to users here",
  "state": "active"
}
'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="example-response">Example response</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
</pre></td><td class="rouge-code"><pre>{
  "preference_center_api_id": "8efc52aa-935e-42b7-bd6b-98f43bb9b0f1",
  "created_at": "2022-09-22T18:28:07Z",
  "updated_at": "2022-09-22T18:32:07Z",
  "message": "success"
}
</pre></td></tr></tbody></table></code></pre></div></div>

</div>
