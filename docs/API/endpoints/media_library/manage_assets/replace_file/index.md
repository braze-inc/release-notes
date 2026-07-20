<div id='api_ibladivdawee' class='api_div' data-search-keywords='prerequisites asset_id asset_url asset_file message error_code meta info new_image_asset name size url ext'>
<h1 id="replace-an-asset-in-the-media-library">Replace an asset in the media library</h1>
<div class="api_type"><div class="method put ">put</div>
<p>/media_library/replace_file</p>
</div>

<blockquote>
  <p>Use this endpoint to replace the file of an existing asset in the <a href="/docs/user_guide/engagement_tools/templates_and_media/media_library">Braze media library</a> while preserving its asset ID and URL. You can provide the replacement file using either an externally hosted URL (<code class="language-plaintext highlighter-rouge">asset_url</code>) or binary file data sent in the request body (<code class="language-plaintext highlighter-rouge">asset_file</code>).</p>
</blockquote>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with the <code class="language-plaintext highlighter-rouge">media_library.replace</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="request-body">Request body</h2>

<p>When you include <code class="language-plaintext highlighter-rouge">asset_url</code>, the endpoint downloads the file from the URL. When you include <code class="language-plaintext highlighter-rouge">asset_file</code>, the endpoint uses the binary data in the request body.</p>

<p>Example request body for <code class="language-plaintext highlighter-rouge">asset_url</code>:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"asset_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"your-asset-id"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"asset_url"</span><span class="p">:</span><span class="w"> </span><span class="s2">"https://cdn.example.com/assets/cat.jpg"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>Example request body for <code class="language-plaintext highlighter-rouge">asset_file</code>:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"asset_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"your-asset-id"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"asset_file"</span><span class="p">:</span><span class="w"> </span><span class="err">&lt;BINARY</span><span class="w"> </span><span class="err">FILE</span><span class="w"> </span><span class="err">DATA&gt;</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>The request body includes the following parameters:</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Request body">
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
      <td><code class="language-plaintext highlighter-rouge">asset_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The ID of the asset to replace.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">asset_url</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A publicly accessible URL for the replacement file.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">asset_file</code></td>
      <td>Optional</td>
      <td>Binary</td>
      <td>Binary file data for the replacement file.</td>
    </tr>
  </tbody>
</table>

<p><strong>Important:</strong></p>

<p><code class="language-plaintext highlighter-rouge">asset_url</code> and <code class="language-plaintext highlighter-rouge">asset_file</code> are mutually exclusive, you must only include one of them in your API request.</p>

<h3 id="replacement-file-requirements">Replacement file requirements</h3>

<ul>
  <li>The replacement file’s extension must exactly match the extension of the existing asset. For example, you cannot replace a <code class="language-plaintext highlighter-rouge">.png</code> asset with a <code class="language-plaintext highlighter-rouge">.jpg</code> file.</li>
  <li>File replacement is supported for images, SVGs, documents, fonts, contact cards, and code files. Video assets cannot be replaced.</li>
</ul>

<h2 id="example-request">Example request</h2>

<p>This section includes two example <code class="language-plaintext highlighter-rouge">curl</code> requests, one for replacing an asset using a URL and another using binary file data.</p>

<p>This request shows an example of replacing an asset in the media library using an <code class="language-plaintext highlighter-rouge">asset_url</code>.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_url": "https://cdn.example.com/assets/cat.jpg"}'
</pre></td></tr></tbody></table></code></pre></div></div>

<p>This request shows an example of replacing an asset in the media library using an <code class="language-plaintext highlighter-rouge">asset_file</code>.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_file":&lt;BINARY FILE DATA&gt;}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="error-responses">Error responses</h3>

<p>This section lists potential errors and their corresponding messages and descriptions.</p>

<h4 id="validation-errors">Validation errors</h4>

<p>Validation errors return a structure like this:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">Human-readable</span><span class="w"> </span><span class="err">error</span><span class="w"> </span><span class="err">description</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>This table lists possible validation errors.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Validation errors">
  <thead>
    <tr>
      <th>HTTP Status</th>
      <th>Message</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>400</td>
      <td>“asset_id is required.”</td>
      <td>No asset ID was provided in the request.</td>
    </tr>
    <tr>
      <td>400</td>
      <td>“Either file or asset_url is required.”</td>
      <td>Neither <code class="language-plaintext highlighter-rouge">asset_file</code> nor <code class="language-plaintext highlighter-rouge">asset_url</code> was provided; one is required.</td>
    </tr>
  </tbody>
</table>

<h4 id="processing-errors">Processing errors</h4>

<p>Processing errors return a different response with error codes:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">Human-readable</span><span class="w"> </span><span class="err">error</span><span class="w"> </span><span class="err">description</span><span class="p">,</span><span class="w">
  </span><span class="nl">"error_code"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">error</span><span class="w"> </span><span class="err">code</span><span class="p">,</span><span class="w">
  </span><span class="nl">"meta"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>This table lists possible processing errors.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Processing errors">
  <thead>
    <tr>
      <th>Error Code</th>
      <th>HTTP Status</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ASSET_NOT_FOUND</code></td>
      <td>404</td>
      <td>No asset with the given <code class="language-plaintext highlighter-rouge">asset_id</code> exists in this workspace. The <code class="language-plaintext highlighter-rouge">meta</code> object includes <code class="language-plaintext highlighter-rouge">asset_id</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">INVALID_ASSET_URL</code></td>
      <td>400</td>
      <td>The <code class="language-plaintext highlighter-rouge">asset_url</code> value is not a valid URI. The <code class="language-plaintext highlighter-rouge">meta</code> object includes <code class="language-plaintext highlighter-rouge">asset_url</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">EXTENSION_MISMATCH</code></td>
      <td>400</td>
      <td>The replacement file’s extension does not match the existing asset’s extension. The <code class="language-plaintext highlighter-rouge">meta</code> object includes <code class="language-plaintext highlighter-rouge">expected_extension</code> and <code class="language-plaintext highlighter-rouge">received_extension</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">UNSUPPORTED_ASSET_TYPE_FOR_REPLACE</code></td>
      <td>400</td>
      <td>File replacement is not supported for this asset type (for example, video). The <code class="language-plaintext highlighter-rouge">meta</code> object includes <code class="language-plaintext highlighter-rouge">asset_type</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ASSET_SIZE_EXCEEDS_LIMIT</code></td>
      <td>400</td>
      <td>The file exceeds the maximum allowed size. The <code class="language-plaintext highlighter-rouge">meta</code> object includes <code class="language-plaintext highlighter-rouge">size_limit_bytes</code> and <code class="language-plaintext highlighter-rouge">file_size_bytes</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">CORRUPT_FILE</code></td>
      <td>400</td>
      <td>The image file is corrupted or unreadable. The <code class="language-plaintext highlighter-rouge">meta</code> object includes <code class="language-plaintext highlighter-rouge">file_name</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">GENERIC_ERROR</code></td>
      <td>500</td>
      <td>An unexpected error occurred during file replacement. The <code class="language-plaintext highlighter-rouge">meta</code> object includes <code class="language-plaintext highlighter-rouge">original_error</code> for debugging. Try again or contact <a href="/docs/support_contact">Support</a>.</td>
    </tr>
  </tbody>
</table>

<h2 id="response">Response</h2>

<p>There are five status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">200</code>, <code class="language-plaintext highlighter-rouge">400</code>, <code class="language-plaintext highlighter-rouge">404</code>, <code class="language-plaintext highlighter-rouge">429</code>, and <code class="language-plaintext highlighter-rouge">500</code>.</p>

<p>The following JSON shows the expected shape of the response.</p>

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
  </span><span class="nl">"info"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Asset file updated successfully."</span><span class="p">,</span><span class="w">
  </span><span class="nl">"new_image_asset"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">asset</span><span class="p">,</span><span class="w">
    </span><span class="nl">"size"</span><span class="p">:</span><span class="w"> </span><span class="err">(Integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">byte</span><span class="w"> </span><span class="err">size</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">asset</span><span class="p">,</span><span class="w">
    </span><span class="nl">"url"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">access</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">asset</span><span class="p">,</span><span class="w">
    </span><span class="nl">"ext"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">extension</span><span class="w"> </span><span class="err">(e.g.</span><span class="p">,</span><span class="w"> </span><span class="s2">"png"</span><span class="p">,</span><span class="w"> </span><span class="s2">"jpg"</span><span class="p">,</span><span class="w"> </span><span class="s2">"gif"</span><span class="err">)</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
