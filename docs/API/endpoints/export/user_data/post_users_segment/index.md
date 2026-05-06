<div id='api_mhqyummxmkkk' class='api_div'>
<h1 id="export-user-profile-by-segment">Export user profile by segment</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/export/segment</p>
</div>

<blockquote>
  <p>Use this endpoint to export all the users within a segment.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>When using this endpoint, note the following:<br /><br />1. The <code class="language-plaintext highlighter-rouge">fields_to_export</code> field in this API request is <strong>required</strong>.<br />2. The fields for <code class="language-plaintext highlighter-rouge">custom_events</code>, <code class="language-plaintext highlighter-rouge">purchases</code>, <code class="language-plaintext highlighter-rouge">campaigns_received</code>, and <code class="language-plaintext highlighter-rouge">canvases_received</code> only contain data from the last 90 days.</p>

<p>User data is exported as multiple files of user JSON objects separated by new lines (such as one JSON object per line). Data is exported to an automatically generated URL or to an S3 bucket if this integration is already set up.</p>

<p><strong>Important:</strong></p>

<p><strong>Export output format</strong>: When an export is successful and you have not configured cloud storage credentials, the HTTP response includes a URL to download a compressed archive (ZIP or GZIP file). When cloud storage credentials (S3, Azure, or Google Cloud Storage) are configured, Braze writes the export directly to your bucket, and the response does not include a download URL. If the export fails, you receive an email notification instead. Setting up cloud storage credentials reduces the likelihood of failures for large exports.</p>

<p>Note that a company may run at most one export per segment using this endpoint at a given time. Wait for your export to complete before trying again.</p>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">users.export.segment</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="credentials-based-response-details">Credentials-based response details</h2>

<p>If you have added your <a href="/docs/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3">S3</a>, <a href="/docs/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/">Azure</a>, or <a href="/docs/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/">Google Cloud Storage</a> credentials to Braze, then each file is uploaded to your bucket as a ZIP file with the key format that looks like <code class="language-plaintext highlighter-rouge">segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip</code>. If using Azure, make sure that you have the <strong>Make this the default data export destination</strong> box checked in the Azure partner overview page in Braze. Generally, Braze creates 1 file per 5,000 users to optimize processing. Exporting smaller segments within a large workspace may result in multiple files. You can then extract the files and concatenate all of the <code class="language-plaintext highlighter-rouge">json</code> files to a single file if needed. If you specify an <code class="language-plaintext highlighter-rouge">output_format</code> of <code class="language-plaintext highlighter-rouge">gzip</code>, then the file extension is <code class="language-plaintext highlighter-rouge">.gz</code> instead of <code class="language-plaintext highlighter-rouge">.zip</code>.</p>

<p><strong>Export pathing breakdown for ZIP</strong></p>

<p><strong>ZIP format:</strong>
<code class="language-plaintext highlighter-rouge">bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip</code></p>

<p><strong>Example ZIP:</strong>
<code class="language-plaintext highlighter-rouge">braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip</code></p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" role="presentation">
  <thead>
    <tr>
      <th>Property</th>
      <th>Details</th>
      <th>Shown in Example as</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">bucket-name</code></td>
      <td>Fixed based on your bucket name.</td>
      <td><code class="language-plaintext highlighter-rouge">braze.docs.bucket</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">segment-export</code></td>
      <td>Fixed.</td>
      <td><code class="language-plaintext highlighter-rouge">segment-export</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">SEGMENT_ID</code></td>
      <td>Included in the export request.</td>
      <td><code class="language-plaintext highlighter-rouge">abc56c0c-rd4a-pb0a-870pdf4db07q</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">YYYY-MM-dd</code></td>
      <td>The date the successful callback is received.</td>
      <td><code class="language-plaintext highlighter-rouge">2019-04-25</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">RANDOM_UUID</code></td>
      <td>A random UUID generated by Braze at the time of the request.</td>
      <td><code class="language-plaintext highlighter-rouge">d9696570-dfb7-45ae-baa2-25e302r2da27</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">TIMESTAMP_WHEN_EXPORT_STARTED</code></td>
      <td>Unix time (seconds since 2017-01-01:00:00:00Z) that the export was requested in UTC.</td>
      <td><code class="language-plaintext highlighter-rouge">1556044807</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">filename</code></td>
      <td>Random per file.</td>
      <td><code class="language-plaintext highlighter-rouge">114f0226319130e1a4770f2602b5639a</code></td>
    </tr>
  </tbody>
</table>

<p>We strongly suggest setting up your own S3 or Azure credentials when using this endpoint to enforce your own bucket policies on the export. If you do not have your cloud storage credentials, the response to the request provides the URL where a ZIP file containing all the user files can be downloaded. The URL becomes a valid location only after the export is ready.</p>

<p>Be aware that if you do not provide your cloud storage credentials, there is a limitation on the amount of data you can export from this endpoint. Depending on the fields you’re exporting and the number of users, the file transfer may fail if it is too large. A best practice is to specify which fields you want to export using <code class="language-plaintext highlighter-rouge">fields_to_export</code> and specify only the fields you need to keep the size of the transfer lower. If you are getting errors generating the file, consider breaking your user base into more segments based on a random bucket number (for example, create a segment where a random bucket number is less than 1,000 or between 1,000 and 2,000).</p>

<p>In either scenario, you may optionally provide a <code class="language-plaintext highlighter-rouge">callback_endpoint</code> to be notified when the export is ready. If the <code class="language-plaintext highlighter-rouge">callback_endpoint</code> is provided, Braze makes a post request to the provided address when the download is ready. The body of the post is “success”:true. If you have not added S3 credentials to Braze, then the body of the post additionally has the attribute <code class="language-plaintext highlighter-rouge">url</code> with the download URL as the value.</p>

<p>Larger user bases result in longer export times. For example, an app with 20 million users could take an hour or more.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"segment_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">identifier</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">exported</span><span class="p">,</span><span class="w">
  </span><span class="nl">"callback_endpoint"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">endpoint</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">post</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">download</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">available</span><span class="p">,</span><span class="w">
  </span><span class="nl">"fields_to_export"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">name</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">user</span><span class="w"> </span><span class="err">data</span><span class="w"> </span><span class="err">fields</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">may</span><span class="w"> </span><span class="err">also</span><span class="w"> </span><span class="err">export</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">attributes.</span><span class="w"> </span><span class="err">New</span><span class="w"> </span><span class="err">accounts</span><span class="w"> </span><span class="err">must</span><span class="w"> </span><span class="err">specify</span><span class="w"> </span><span class="err">specific</span><span class="w"> </span><span class="err">fields</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w">
  </span><span class="nl">"output_format"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">using</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">own</span><span class="w"> </span><span class="err">S</span><span class="mi">3</span><span class="w"> </span><span class="err">bucket</span><span class="p">,</span><span class="w">  </span><span class="err">specifies</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">format</span><span class="w"> </span><span class="err">as</span><span class="w"> </span><span class="err">'zip'</span><span class="w"> </span><span class="err">or</span><span class="w"> </span><span class="err">'gzip'.</span><span class="w"> </span><span class="err">Defaults</span><span class="w"> </span><span class="err">to</span><span class="w"> </span><span class="err">ZIP</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">format</span><span class="w">
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
      <td><code class="language-plaintext highlighter-rouge">segment_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Identifier for the segment to be exported. See <a href="/docs/api/identifier_types/">segment identifier</a>.<br /><br />The <code class="language-plaintext highlighter-rouge">segment_id</code> for a given segment can be found from the <a href="/docs/user_guide/administer/global/workspace_settings/apis_and_identifiers/">API Keys</a> page within your Braze account or you can use the <a href="/docs/api/endpoints/export/segments/get_segment/">Segment List Endpoint</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">callback_endpoint</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>Endpoint to post a download URL to when the export is available.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">fields_to_export</code></td>
      <td>Required*</td>
      <td>Array of strings</td>
      <td>Name of user data fields to export. You can also export all custom attributes by including <code class="language-plaintext highlighter-rouge">custom_attributes</code> in this parameter. Reference <a href="#fields-to-export">Fields to export</a> for a complete list of fields you can export.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">custom_attributes_to_export</code></td>
      <td>Optional</td>
      <td>Array of strings</td>
      <td>Name of specific custom attribute to export. Up to 500 custom attributes can be exported. To create and manage custom attributes in the dashboard, go to <strong>Data Settings</strong> &gt; <strong>Custom Attributes</strong>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">output_format</code></td>
      <td>Optional</td>
      <td>String</td>
      <td>The output format of your file. Defaults to <code class="language-plaintext highlighter-rouge">zip</code> file format. If you are using your own S3 bucket, you can specify <code class="language-plaintext highlighter-rouge">zip</code> or <code class="language-plaintext highlighter-rouge">gzip</code>.</td>
    </tr>
  </tbody>
</table>

<p><strong>Note:</strong></p>

<p>If <code class="language-plaintext highlighter-rouge">custom_attributes</code> is included in the <code class="language-plaintext highlighter-rouge">fields_to_export</code> parameter, all custom attributes are exported regardless of what is in <code class="language-plaintext highlighter-rouge">custom_attributes_to_export</code>. If your goal is to export specific attributes, <code class="language-plaintext highlighter-rouge">custom_attributes</code> should not be included in the <code class="language-plaintext highlighter-rouge">fields_to_export</code> parameter. Instead, use the <code class="language-plaintext highlighter-rouge">custom_attributes_to_export</code> parameter.</p>

<h2 id="example-request-to-export-all-custom-attributes">Example request to export all custom attributes</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
9
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases", "custom_attributes"],
  "output_format" : "zip"
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="example-request-to-export-specific-custom-attributes">Example request to export specific custom attributes</h2>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "custom_attributes_to_export" : ["allergies", "favorite_food"],
  "output_format" : "zip"
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="fields-to-export">Fields to export</h2>

<p>The following is a list of valid <code class="language-plaintext highlighter-rouge">fields_to_export</code>. Using <code class="language-plaintext highlighter-rouge">fields_to_export</code> to minimize the data returned can improve the response time of this API endpoint:</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" role="presentation">
  <thead>
    <tr>
      <th>Field to export</th>
      <th>Data type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">apps</code></td>
      <td>Array</td>
      <td>Apps this user has logged sessions for, which includes the fields:<br /><br />- <code class="language-plaintext highlighter-rouge">name</code>: app name<br />- <code class="language-plaintext highlighter-rouge">platform</code>: app platform, such as iOS, Android, or Web<br />- <code class="language-plaintext highlighter-rouge">version</code>: app version number or name <br />- <code class="language-plaintext highlighter-rouge">sessions</code>: total number of sessions for this app<br />- <code class="language-plaintext highlighter-rouge">first_used</code>: date of first session<br />- <code class="language-plaintext highlighter-rouge">last_used</code>: date of last session<br /><br />All fields are strings.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">attributed_campaign</code></td>
      <td>String</td>
      <td>Data from <a href="/docs/partners/message_orchestration/">attribution integrations</a>, if set up. Identifier for a particular ad campaign.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">attributed_source</code></td>
      <td>String</td>
      <td>Data from <a href="/docs/partners/message_orchestration/">attribution integrations</a>, if set up. Identifier for the platform the ad was on.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">attributed_adgroup</code></td>
      <td>String</td>
      <td>Data from <a href="/docs/partners/message_orchestration/">attribution integrations</a>, if set up. Identifier for an optional sub-grouping below campaign.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">attributed_ad</code></td>
      <td>String</td>
      <td>Data from <a href="/docs/partners/message_orchestration/">attribution integrations</a>, if set up. Identifier for an optional sub-grouping below campaign and ad group.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">push_subscribe</code></td>
      <td>String</td>
      <td>User’s push subscription status.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">email_subscribe</code></td>
      <td>String</td>
      <td>User’s email subscription status.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">braze_id</code></td>
      <td>String</td>
      <td>Device-specific unique user identifier set by Braze for this user.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">country</code></td>
      <td>String</td>
      <td>User’s country using <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> standard.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">created_at</code></td>
      <td>String</td>
      <td>Date and time for when the user profile was created, in ISO 8601 format.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">created_from</code></td>
      <td>String</td>
      <td>Method used to create the user profile (for example, SDK, REST API, or CSV import).</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">custom_attributes</code></td>
      <td>Object</td>
      <td>Custom attribute key-value pairs for this user.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">custom_events</code></td>
      <td>Array</td>
      <td>Custom events attributed to this user in the last 90 days.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">devices</code></td>
      <td>Array</td>
      <td>Information about the user’s device, which could include the following depending on platform:<br /><br />- <code class="language-plaintext highlighter-rouge">model</code>: Device’s model name<br />- <code class="language-plaintext highlighter-rouge">os</code>: Device’s operating system<br />- <code class="language-plaintext highlighter-rouge">carrier</code>: Device’s service carrier, if available<br />- <code class="language-plaintext highlighter-rouge">idfv</code>: (iOS) Braze device identifier, the Apple Identifier for Vendor, if exists<br />- <code class="language-plaintext highlighter-rouge">idfa</code>: (iOS) Identifier for Advertising, if exists<br />- <code class="language-plaintext highlighter-rouge">device_id</code>: (Android) Braze device identifier<br />- <code class="language-plaintext highlighter-rouge">google_ad_id</code>: (Android) Google Play Advertising Identifier, if exists<br />- <code class="language-plaintext highlighter-rouge">roku_ad_id</code>: (Roku) Roku Advertising Identifier<br />- <code class="language-plaintext highlighter-rouge">ad_tracking_enabled</code>: If ad tracking is enabled on the device, can be true or false</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">dob</code></td>
      <td>String</td>
      <td>User’s date of birth in the format <code class="language-plaintext highlighter-rouge">YYYY-MM-DD</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">email</code></td>
      <td>String</td>
      <td>User’s email address.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external_id</code></td>
      <td>String</td>
      <td>Unique user identifier for identified users.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">first_name</code></td>
      <td>String</td>
      <td>User’s first name.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">gender</code></td>
      <td>String</td>
      <td>User’s gender. Possible values are:<br /><br />- <code class="language-plaintext highlighter-rouge">M</code>: male<br />- <code class="language-plaintext highlighter-rouge">F</code>: female<br />- <code class="language-plaintext highlighter-rouge">O</code>: other<br />- <code class="language-plaintext highlighter-rouge">N</code>: not applicable<br />- <code class="language-plaintext highlighter-rouge">P</code>: prefer not to say<br />- <code class="language-plaintext highlighter-rouge">nil</code>: unknown</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">home_city</code></td>
      <td>String</td>
      <td>User’s home city.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">language</code></td>
      <td>String</td>
      <td>User’s language in ISO-639-1 standard.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">last_coordinates</code></td>
      <td>Array of floats</td>
      <td>User’s most recent device location, formatted as <code class="language-plaintext highlighter-rouge">[longitude, latitude]</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">last_name</code></td>
      <td>String</td>
      <td>User’s last name.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">phone</code></td>
      <td>String</td>
      <td>User’s phone number in the format that was imported into Braze. For example, if a request to add a phone number comes in as <code class="language-plaintext highlighter-rouge">1234567890</code>, then it is exported in the same format.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">purchases</code></td>
      <td>Array</td>
      <td>Purchases this user has made in the last 90 days.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">push_tokens</code></td>
      <td>Array</td>
      <td>Information about the user’s push tokens.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">random_bucket</code></td>
      <td>Integer</td>
      <td>User’s <a href="/docs/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event">random bucket number</a>, used to create uniformly distributed segments of random users.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">time_zone</code></td>
      <td>String</td>
      <td>User’s time zone in the same format as the IANA Time Zone Database.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">total_revenue</code></td>
      <td>Float</td>
      <td>Total revenue attributed to this user. Total revenue is calculated based on purchases the user made during conversion windows for the campaigns and Canvases they received.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">uninstalled_at</code></td>
      <td>Timestamp</td>
      <td>Date and time the user uninstalls the app. Omitted if the app has not been uninstalled.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">user_aliases</code></td>
      <td>Object</td>
      <td><a href="/docs/api/objects_filters/user_alias_object#user-alias-object-specification">User aliases object</a> containing the <code class="language-plaintext highlighter-rouge">alias_name</code> and <code class="language-plaintext highlighter-rouge">alias_label</code>, if exists.</td>
    </tr>
  </tbody>
</table>

<h2 id="important-reminders">Important reminders</h2>

<ul>
  <li>The fields for <code class="language-plaintext highlighter-rouge">custom_events</code>, <code class="language-plaintext highlighter-rouge">purchases</code>, <code class="language-plaintext highlighter-rouge">campaigns_received</code>, and <code class="language-plaintext highlighter-rouge">canvases_received</code> contain only data from the last 90 days.</li>
  <li>Both <code class="language-plaintext highlighter-rouge">custom_events</code> and <code class="language-plaintext highlighter-rouge">purchases</code> contain fields for <code class="language-plaintext highlighter-rouge">first</code> and <code class="language-plaintext highlighter-rouge">count</code>. Both of these fields reflect information from all time, and are not limited to data from the last 90 days. For example, if a particular user first did the event 90 days ago, this is accurately reflected in the <code class="language-plaintext highlighter-rouge">first</code> field, and the <code class="language-plaintext highlighter-rouge">count</code> field takes into account events that occurred prior to the last 90 days as well.</li>
  <li>The number of concurrent segment exports a company can run at the endpoint level is capped at 100. Attempts that surpass this limit result in an error.</li>
  <li>Attempting to export a segment a second time while the first export job is still running results in a 429 error.</li>
  <li>A <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/?sdktab=cloud%20storage%20connected#segment-export-api-downloads"><code class="language-plaintext highlighter-rouge">403 Forbidden</code> response</a> often means the export file isn’t ready yet.</li>
</ul>

<h2 id="response">Response</h2>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">status</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">returns</span><span class="w"> </span><span class="err">'success'</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">completed</span><span class="w"> </span><span class="err">without</span><span class="w"> </span><span class="err">errors</span><span class="p">,</span><span class="w">
    </span><span class="nl">"object_prefix"</span><span class="p">:</span><span class="w"> </span><span class="err">(required</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">filename</span><span class="w"> </span><span class="err">prefix</span><span class="w"> </span><span class="err">that</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">used</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">JSON</span><span class="w"> </span><span class="err">file</span><span class="w"> </span><span class="err">produced</span><span class="w"> </span><span class="err">by</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">export</span><span class="p">,</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">example</span><span class="p">,</span><span class="w"> </span><span class="err">'bb</span><span class="mi">8e2</span><span class="err">a</span><span class="mi">91</span><span class="err">-c</span><span class="mi">4</span><span class="err">aa</span><span class="mi">-478</span><span class="err">b-b</span><span class="mi">3</span><span class="err">f</span><span class="mi">2</span><span class="err">-a</span><span class="mi">4</span><span class="err">ee</span><span class="mi">91731</span><span class="err">ad</span><span class="mi">1-1464728599</span><span class="err">'</span><span class="p">,</span><span class="w">
    </span><span class="nl">"url"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">URL</span><span class="w"> </span><span class="err">where</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">segment</span><span class="w"> </span><span class="err">export</span><span class="w"> </span><span class="err">data</span><span class="w"> </span><span class="err">can</span><span class="w"> </span><span class="err">be</span><span class="w"> </span><span class="err">downloaded</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">you</span><span class="w"> </span><span class="err">do</span><span class="w"> </span><span class="err">not</span><span class="w"> </span><span class="err">have</span><span class="w"> </span><span class="err">your</span><span class="w"> </span><span class="err">own</span><span class="w"> </span><span class="err">S</span><span class="mi">3</span><span class="w"> </span><span class="err">credentials</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="null-url"><code class="language-plaintext highlighter-rouge">null</code> URL</h3>

<p>If the response includes <code class="language-plaintext highlighter-rouge">"url": null</code> (or omits a download URL) and you have configured a <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">cloud storage integration</a> such as an Amazon S3 bucket or Azure Blob Storage container, Braze writes the export to your connected bucket or container instead of returning a temporary download URL in the API response. Retrieve the files from your connected cloud storage bucket or container.</p>

<p>If a download URL is returned, it is valid for only a few hours. As such, we highly recommend that you add your own S3 credentials to Braze.</p>

<p>If you see <code class="language-plaintext highlighter-rouge">object_prefix</code> in your API response and no URL to download the data, this means you have an Amazon S3 bucket already set up for this endpoint. Any data exported using this endpoint goes directly to your S3 bucket.</p>

<h2 id="example-user-export-file-output">Example user export file output</h2>

<p>User export object (Braze includes the least data possible—if a field is missing from the object, it should be assumed to be null or empty):</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"external_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"user_aliases"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"alias_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"alias_label"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"braze_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"first_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"last_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"email"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"dob"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user's</span><span class="w"> </span><span class="err">date</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">birth</span><span class="p">,</span><span class="w">
    </span><span class="nl">"home_city"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"country"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">ISO</span><span class="mi">-3166-1</span><span class="w"> </span><span class="err">alpha</span><span class="mi">-2</span><span class="w"> </span><span class="err">standard</span><span class="p">,</span><span class="w">
    </span><span class="nl">"phone"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"language"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">ISO</span><span class="mi">-639-1</span><span class="w"> </span><span class="err">standard</span><span class="p">,</span><span class="w">
    </span><span class="nl">"time_zone"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"last_coordinates"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(array</span><span class="w"> </span><span class="err">of</span><span class="w"> </span><span class="err">float)</span><span class="w"> </span><span class="p">[</span><span class="err">lon</span><span class="p">,</span><span class="w"> </span><span class="err">lat</span><span class="p">],</span><span class="w">
    </span><span class="nl">"gender"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="s2">"M"</span><span class="w"> </span><span class="err">|</span><span class="w"> </span><span class="s2">"F"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"total_revenue"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(float)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributed_campaign"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributed_source"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributed_adgroup"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributed_ad"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
    </span><span class="nl">"push_subscribe"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="s2">"opted_in"</span><span class="w"> </span><span class="err">|</span><span class="w"> </span><span class="s2">"subscribed"</span><span class="w"> </span><span class="err">|</span><span class="w"> </span><span class="s2">"unsubscribed"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"email_subscribe"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="s2">"opted_in"</span><span class="w"> </span><span class="err">|</span><span class="w"> </span><span class="s2">"subscribed"</span><span class="w"> </span><span class="err">|</span><span class="w"> </span><span class="s2">"unsubscribed"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"custom_attributes"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(object)</span><span class="w"> </span><span class="err">custom</span><span class="w"> </span><span class="err">attribute</span><span class="w"> </span><span class="err">key-value</span><span class="w"> </span><span class="err">pairs</span><span class="p">,</span><span class="w">
    </span><span class="nl">"custom_events"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"first"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"count"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"purchases"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"first"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"count"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(int)</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"devices"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"model"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"os"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"carrier"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"idfv"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">iOS</span><span class="w"> </span><span class="err">devices</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">IDFV</span><span class="w"> </span><span class="err">collection</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">enabled</span><span class="p">,</span><span class="w">
        </span><span class="nl">"idfa"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">iOS</span><span class="w"> </span><span class="err">devices</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">IDFA</span><span class="w"> </span><span class="err">collection</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">enabled</span><span class="p">,</span><span class="w">
        </span><span class="nl">"google_ad_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">Android</span><span class="w"> </span><span class="err">devices</span><span class="w"> </span><span class="err">when</span><span class="w"> </span><span class="err">Google</span><span class="w"> </span><span class="err">Play</span><span class="w"> </span><span class="err">Advertising</span><span class="w"> </span><span class="err">Identifier</span><span class="w"> </span><span class="err">collection</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">enabled</span><span class="p">,</span><span class="w">
        </span><span class="nl">"roku_ad_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">included</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">Roku</span><span class="w"> </span><span class="err">devices</span><span class="p">,</span><span class="w">
        </span><span class="nl">"ad_tracking_enabled"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"push_tokens"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"app"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">app</span><span class="w"> </span><span class="err">name</span><span class="p">,</span><span class="w">
        </span><span class="nl">"platform"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"token"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"device_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"notifications_enabled"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w"> </span><span class="err">whether</span><span class="w"> </span><span class="err">foreground</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">notifications</span><span class="w"> </span><span class="err">are</span><span class="w"> </span><span class="err">enabled</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">this</span><span class="w"> </span><span class="err">token.</span><span class="w"> </span><span class="err">`</span><span class="kc">true</span><span class="err">`</span><span class="w"> </span><span class="err">means</span><span class="w"> </span><span class="err">foreground</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">enabled</span><span class="w"> </span><span class="err">for</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">token</span><span class="p">,</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">`</span><span class="kc">false</span><span class="err">`</span><span class="w"> </span><span class="err">means</span><span class="w"> </span><span class="err">foreground</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">disabled</span><span class="w"> </span><span class="err">(for</span><span class="w"> </span><span class="err">example</span><span class="p">,</span><span class="w"> </span><span class="err">background-only).</span><span class="w"> </span><span class="err">This</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">device-level</span><span class="w"> </span><span class="err">and</span><span class="w"> </span><span class="err">doesn't</span><span class="w"> </span><span class="err">indicate</span><span class="w"> </span><span class="err">the</span><span class="w"> </span><span class="err">user's</span><span class="w"> </span><span class="err">global</span><span class="w"> </span><span class="err">push</span><span class="w"> </span><span class="err">subscription</span><span class="w"> </span><span class="err">status</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"apps"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"platform"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"version"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"sessions"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(integer)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"first_used"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_used"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"campaigns_received"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_received"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"engaged"</span><span class="w"> </span><span class="p">:</span><span class="w">
         </span><span class="p">{</span><span class="w">
           </span><span class="nl">"opened_email"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="p">,</span><span class="w">
           </span><span class="nl">"opened_push"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="p">,</span><span class="w">
           </span><span class="nl">"clicked_email"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="p">,</span><span class="w">
           </span><span class="nl">"clicked_triggered_in_app_message"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="w">
          </span><span class="p">},</span><span class="w">
          </span><span class="nl">"converted"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="p">,</span><span class="w">
          </span><span class="nl">"api_campaign_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
          </span><span class="nl">"variation_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">exists</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">it</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">multivariate</span><span class="w"> </span><span class="err">campaign</span><span class="p">,</span><span class="w">
          </span><span class="nl">"variation_api_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">string)</span><span class="w"> </span><span class="err">exists</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">it</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">multivariate</span><span class="w"> </span><span class="err">campaign</span><span class="p">,</span><span class="w">
          </span><span class="nl">"in_control"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(optional</span><span class="p">,</span><span class="w"> </span><span class="err">boolean)</span><span class="w"> </span><span class="err">exists</span><span class="w"> </span><span class="err">only</span><span class="w"> </span><span class="err">if</span><span class="w"> </span><span class="err">it</span><span class="w"> </span><span class="err">is</span><span class="w"> </span><span class="err">a</span><span class="w"> </span><span class="err">multivariate</span><span class="w"> </span><span class="err">campaign</span><span class="w">
        </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"canvases_received"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"api_canvas_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_received_message"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_entered"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"variation_name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"in_control"</span><span class="p">:</span><span class="w"> </span><span class="err">(boolean)</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_exited"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="p">,</span><span class="w">
        </span><span class="nl">"steps_received"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
          </span><span class="p">{</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"api_canvas_step_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"last_received"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="w">
          </span><span class="p">},</span><span class="w">
          </span><span class="p">{</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"api_canvas_step_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"last_received"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="w">
          </span><span class="p">},</span><span class="w">
          </span><span class="p">{</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"api_canvas_step_id"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="p">,</span><span class="w">
            </span><span class="nl">"last_received"</span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w"> </span><span class="err">date</span><span class="w">
          </span><span class="p">}</span><span class="w">
        </span><span class="p">]</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"cards_clicked"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="err">(string)</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
    </span><span class="nl">"created_at"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-07-10 15:00:00.000 UTC"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"external_id"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"A8i3mkd99"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"user_aliases"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"alias_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"user_123"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"alias_label"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"amplitude_id"</span><span class="w">
      </span><span class="p">}</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"braze_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"5fbd99bac125ca40511f2cb1"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"random_bucket"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="mi">2365</span><span class="p">,</span><span class="w">
    </span><span class="nl">"first_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"Jane"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"last_name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"Doe"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"email"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"example@braze.com"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"dob"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"1980-12-21"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"home_city"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"Chicago"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"country"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"US"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"phone"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"+442071838750"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"language"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"en"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"time_zone"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"Eastern Time (US &amp; Canada)"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"last_coordinates"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="mf">41.84157636433568</span><span class="p">,</span><span class="w"> </span><span class="mf">-87.83520818508256</span><span class="p">],</span><span class="w">
    </span><span class="nl">"gender"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"F"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"total_revenue"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="mi">65</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributed_campaign"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"braze_test_campaign_072219"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributed_source"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"braze_test_source_072219"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributed_adgroup"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"braze_test_adgroup_072219"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attributed_ad"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"braze_test_ad_072219"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"push_subscribe"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"opted_in"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"push_opted_in_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-01-26T22:45:53.953Z"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"email_subscribe"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"subscribed"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"custom_attributes"</span><span class="p">:</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"loyaltyId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"37c98b9d-9a7f-4b2f-a125-d873c5152856"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"loyaltyPoints"</span><span class="p">:</span><span class="w"> </span><span class="s2">"321"</span><span class="p">,</span><span class="w">
       </span><span class="nl">"loyaltyPointsNumber"</span><span class="p">:</span><span class="w"> </span><span class="mi">107</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="nl">"custom_events"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Loyalty Acknowledgement"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"first"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2021-06-28T17:02:43.032Z"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2021-06-28T17:02:43.032Z"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"purchases"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"item_40834"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"first"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2021-09-05T03:45:50.540Z"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-06-03T17:30:41.201Z"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"count"</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"devices"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"model"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Pixel XL"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"os"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Android (Q)"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"carrier"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span><span class="w">
        </span><span class="nl">"device_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"312ef2c1-83db-4789-967-554545a1bf7a"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"ad_tracking_enabled"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"push_tokens"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"app"</span><span class="p">:</span><span class="w"> </span><span class="s2">"MovieCanon"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"platform"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Android"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"token"</span><span class="p">:</span><span class="w"> </span><span class="s2">"12345abcd"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"device_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"312ef2c1-83db-4789-967-554545a1bf7a"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"notifications_enabled"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"apps"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"MovieCannon"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"platform"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Android"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"version"</span><span class="p">:</span><span class="w"> </span><span class="s2">"3.29.0"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"sessions"</span><span class="p">:</span><span class="w"> </span><span class="mi">1129</span><span class="p">,</span><span class="w">
        </span><span class="nl">"first_used"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2020-02-02T19:56:19.142Z"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_used"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2021-11-11T00:25:19.201Z"</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"campaigns_received"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Email Unsubscribe"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"api_campaign_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"d72fdc84-ddda-44f1-a0d5-0e79f47ef942"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_received"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-06-02T03:07:38.105Z"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"engaged"</span><span class="p">:</span><span class="w">
        </span><span class="p">{</span><span class="w">
           </span><span class="nl">"opened_email"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="nl">"converted"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w">
        </span><span class="nl">"multiple_converted"</span><span class="p">:</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"Primary Conversion Event - A"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="nl">"in_control"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
        </span><span class="nl">"variation_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Variant 1"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"variation_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1bddc73a-a134-4784-9134-5b5574a9e0b8"</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"canvases_received"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Non Global  Holdout Group 4/21/21"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"api_canvas_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"46972a9d-dc81-473f-aa03-e3473b4ed781"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_received_message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2021-07-07T20:46:24.136Z"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_entered"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2021-07-07T20:45:24.000+00:00"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"variation_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Variant 1"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"in_control"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_entered_control_at"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span><span class="w">
        </span><span class="nl">"last_exited"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2021-07-07T20:46:24.136Z"</span><span class="p">,</span><span class="w">
        </span><span class="nl">"steps_received"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
          </span><span class="p">{</span><span class="w">
            </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Step"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"api_canvas_step_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"43d1a349-c3c8-4be1-9fbe-ce708e4d1c39"</span><span class="p">,</span><span class="w">
            </span><span class="nl">"last_received"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2021-07-07T20:46:24.136Z"</span><span class="w">
          </span><span class="p">},</span><span class="w">
          </span><span class="err">...</span><span class="w">
        </span><span class="p">]</span><span class="w">
      </span><span class="p">}</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">],</span><span class="w">
    </span><span class="nl">"cards_clicked"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
      </span><span class="p">{</span><span class="w">
        </span><span class="nl">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"Loyalty Promo"</span><span class="w">
      </span><span class="p">},</span><span class="w">
      </span><span class="err">...</span><span class="w">
    </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p><strong>Tip:</strong></p>

<p>For help with CSV and API exports, visit <a href="/docs/user_guide/data/distribution/export_braze_data/export_troubleshooting/">Export troubleshooting</a>.</p>

</div>
