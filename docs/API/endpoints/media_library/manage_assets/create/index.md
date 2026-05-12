<div id='api_vvbbngoixkoo' class='api_div'>
<h1 id="upload-an-asset-to-the-media-library">Upload an asset to the media library</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/media_library/create</p>
</div>

<blockquote>
  <p>Use this endpoint to add an asset to the <a href="https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library">Braze media library</a> using either an externally hosted URL (<code class="language-plaintext highlighter-rouge">asset_url</code>) or binary file data sent in the request body (<code class="language-plaintext highlighter-rouge">asset_file</code>). This endpoint supports images and ZIP files that contain images.</p>
</blockquote>

<p><strong>Tip:</strong></p>

<p>You can also call this endpoint through the <a href="/docs/user_guide/brazeai/mcp_server/">Braze MCP server</a> using the <a href="/docs/user_guide/brazeai/mcp_server/available_api_functions/#media-library"><code class="language-plaintext highlighter-rouge">create_media_library_asset</code></a> function. This lets AI tools like Claude and Cursor upload assets to your media library through natural language prompts.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">media_library.create</code> permission.</p>

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
  </span><span class="nl">"asset_url"</span><span class="p">:</span><span class="w"> </span><span class="s2">"https://cdn.example.com/assets/cat.jpg"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cat Graphic"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>Example request body for <code class="language-plaintext highlighter-rouge">asset_file</code>:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"asset_file"</span><span class="p">:</span><span class="w"> </span><span class="err">&lt;BINARY</span><span class="w"> </span><span class="err">FILE</span><span class="w"> </span><span class="err">DATA&gt;</span><span class="p">,</span><span class="w">
  </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cat Graphic"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>The request body includes the following parameters:</p>

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
      <td><code class="language-plaintext highlighter-rouge">asset_url</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A publicly accessible URL for the asset to be uploaded into Braze.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">asset_file</code></td>
      <td>Optional</td>
      <td>Binary</td>
      <td>Binary file data.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>A name to appear in the media library for this asset.</td>
    </tr>
  </tbody>
</table>

<p><strong>Important:</strong></p>

<p><code class="language-plaintext highlighter-rouge">asset_url</code> and <code class="language-plaintext highlighter-rouge">asset_file</code> are mutually exclusive, you must only include one of them in your API request.</p>

<h3 id="uploaded-file-names">Uploaded file names</h3>

<p>This section explains how the endpoint assigns names to uploaded files based on whether you include the <code class="language-plaintext highlighter-rouge">name</code> parameter.</p>

<h4 id="single-file-uploads">Single file uploads</h4>

<table class="reset-td-br-1 reset-td-br-2" role="presentation" style="table-layout: fixed; width: 100%;">
  <thead>
    <tr>
      <th>Scenario</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code> provided</td>
      <td>The <code class="language-plaintext highlighter-rouge">name</code> value is used as the asset name in the media library.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code> excluded</td>
      <td>The original filename from the URL or uploaded file is used.</td>
    </tr>
  </tbody>
</table>

<h4 id="zip-file-uploads">ZIP file uploads</h4>

<table class="reset-td-br-1 reset-td-br-2" role="presentation" style="table-layout: fixed; width: 100%;">
  <thead>
    <tr>
      <th>Scenario</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code> provided</td>
      <td>The <code class="language-plaintext highlighter-rouge">name</code> value is used as a prefix, with an incrementing number appended as a suffix (for example, “My File 1”, “My File 2”, “My File 3”).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">name</code> excluded</td>
      <td>Each file retains its original filename from within the ZIP file.</td>
    </tr>
  </tbody>
</table>

<h2 id="example-request">Example request</h2>

<p>This section includes two example <code class="language-plaintext highlighter-rouge">curl</code> requests, one for adding an asset using a URL and another using binary file data.</p>

<p>This request shows an example of adding an asset to the media library using an <code class="language-plaintext highlighter-rouge">asset_url</code>.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
</pre></td></tr></tbody></table></code></pre></div></div>

<p>This request shows an example of adding an asset to the media library using an <code class="language-plaintext highlighter-rouge">asset_file</code>.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
</pre></td><td class="rouge-code"><pre>curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":&lt;BINARY FILE DATA&gt;, "name":"Cat Graphic"}'
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

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" role="presentation">
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
      <td>“Either asset_url or asset_file must be provided.”</td>
      <td>No asset parameter was provided in the request.</td>
    </tr>
    <tr>
      <td>400</td>
      <td>“Both asset_url and asset_file cannot be provided. Please provide only one.”</td>
      <td>Both asset parameters were provided; only one is allowed.</td>
    </tr>
    <tr>
      <td>403</td>
      <td>“Media Library Public APIs are not enabled for this company.”</td>
      <td>Media library feature is not enabled for this workspace.</td>
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

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" role="presentation">
  <thead>
    <tr>
      <th>Error Code</th>
      <th>HTTP Status</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">UNSUPPORTED_FILE_TYPE</code></td>
      <td>400</td>
      <td>The uploaded file type is not supported. The <code class="language-plaintext highlighter-rouge">meta</code> object includes the <code class="language-plaintext highlighter-rouge">file_type</code> that was rejected.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ASSET_SIZE_EXCEEDS_LIMIT</code></td>
      <td>400</td>
      <td>The file exceeds the maximum allowed size. Images have a 5 MB limit.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">MEDIA_LIBRARY_LIMIT_REACHED</code></td>
      <td>400</td>
      <td>The workspace has reached its maximum number of assets (200 by default for free trial companies, unlimited otherwise). The <code class="language-plaintext highlighter-rouge">meta</code> object includes the current <code class="language-plaintext highlighter-rouge">limit</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ASSET_UPLOAD_FAILED</code></td>
      <td>400</td>
      <td>The asset failed to upload due to processing issues.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ZIP_UPLOAD_ERROR</code></td>
      <td>400</td>
      <td>The ZIP file is corrupted or could not be opened. The <code class="language-plaintext highlighter-rouge">meta</code> object includes the <code class="language-plaintext highlighter-rouge">original_error</code> message.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ZIP_FILE_TOO_LARGE</code></td>
      <td>400</td>
      <td>The total uncompressed size of the ZIP file exceeds the 5 MB limit. The <code class="language-plaintext highlighter-rouge">meta</code> object includes the <code class="language-plaintext highlighter-rouge">zip_file_name</code> and <code class="language-plaintext highlighter-rouge">zip_file_size</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ZIPPED_ENTITY_HAS_NO_NAME</code></td>
      <td>400</td>
      <td>A file entry inside the ZIP has no name. Ensure the ZIP file is not corrupted and add a name for any unnamed file entries.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY</code></td>
      <td>400</td>
      <td>The ZIP file contains nested directories, which are not supported. All files must be at the root level of the ZIP.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">GENERIC_ERROR</code></td>
      <td>500</td>
      <td>An unexpected error occurred during upload. The <code class="language-plaintext highlighter-rouge">meta</code> object includes the <code class="language-plaintext highlighter-rouge">original_error</code> message for debugging. Try again or contact <a href="/docs/support_contact/">Support</a>.</td>
    </tr>
  </tbody>
</table>

<h2 id="response">Response</h2>

<p>There are five status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">200</code>, <code class="language-plaintext highlighter-rouge">400</code>, <code class="language-plaintext highlighter-rouge">403</code>, <code class="language-plaintext highlighter-rouge">429</code>, and <code class="language-plaintext highlighter-rouge">500</code>.</p>

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
    </span><span class="nl">"new_assets"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">asset</span><span class="p">,</span><span class="w">
            </span><span class="nl">"size"</span><span class="p">:</span><span class="w"> </span><span class="err">(Integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">byte</span><span class="w"> </span><span class="err">size</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">asset</span><span class="p">,</span><span class="w">
            </span><span class="nl">"url"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">access</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">asset</span><span class="p">,</span><span class="w">
            </span><span class="nl">"ext"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">extension</span><span class="w"> </span><span class="err">(e.g.</span><span class="p">,</span><span class="w"> </span><span class="s2">"png"</span><span class="p">,</span><span class="w"> </span><span class="s2">"jpg"</span><span class="p">,</span><span class="w"> </span><span class="s2">"gif"</span><span class="err">)</span><span class="w">
        </span><span class="p">}</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">asset</span><span class="p">,</span><span class="w">
            </span><span class="nl">"size"</span><span class="p">:</span><span class="w"> </span><span class="err">(Integer)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">byte</span><span class="w"> </span><span class="err">size</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">asset</span><span class="p">,</span><span class="w">
            </span><span class="nl">"ext"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">extension</span><span class="w"> </span><span class="err">(e.g.</span><span class="p">,</span><span class="w"> </span><span class="s2">"png"</span><span class="p">,</span><span class="w"> </span><span class="s2">"jpg"</span><span class="p">,</span><span class="w"> </span><span class="s2">"gif"</span><span class="err">)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"error"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">error</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">occurred</span><span class="w">
        </span><span class="p">}</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"dashboard_url"</span><span class="p">:</span><span class="w"> </span><span class="err">(String)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">view</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">asset</span><span class="w"> </span><span class="err">in</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">Braze</span><span class="w"> </span><span class="err">dashboard</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
