<div id='api_cyvtymcbrjnn' class='api_div' data-search-keywords='create or replace object relationships in bulk records type_name object_id rel_kind related_type_name related_object_id attributes since source_import_id status record_count errors index id parameter message'>
<h1 id="create-or-replace-object-relationships-in-bulk">Create or replace object relationships in bulk</h1>
<div class="api_type"><div class="method put ">put</div>
<p>/data_objects/object_relationships</p>
</div>

<blockquote>
  <p>Use this endpoint to create or replace up to 50 object-to-object relationships in one request.</p>
</blockquote>

<p><strong>Important:</strong></p>

<p>Data Objects is generally available, but your workspace must be provisioned for Accounts before you can use this endpoint. To request provisioning, go to <strong>Data Settings</strong> &gt; <strong>Accounts</strong> and complete the questionnaire. For details, see <a href="/docs/user_guide/data/activation/accounts#step-1-enable-accounts">Enable Accounts</a>.</p>

<p>Braze accepts the request and processes it in the background. A <code class="language-plaintext highlighter-rouge">202</code> response means the batch is queued, not applied. To change one relationship and see the change right away, use <a href="/docs/api/endpoints/data_objects/object_relationships/put_replace_object_relationship">Replace object relationship</a>. For when to use each, see <a href="/docs/api/endpoints/data_objects#bulk-endpoints">Bulk endpoints</a>.</p>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you need an <a href="/docs/api/basics#rest-api-key-permissions">API key</a> with <code class="language-plaintext highlighter-rouge">data_objects.object_relationships.bulk_upsert</code>. The single-record permissions, such as <code class="language-plaintext highlighter-rouge">data_objects.object_relationships.create</code>, don’t grant access to this endpoint.</p>

<h2 id="rate-limit">Rate limit</h2>

<p>This endpoint is in the Data Objects bulk write bucket with a default limit of 1,000 requests per minute per workspace. The limit is shared across all six bulk endpoints and with Cloud Data Ingestion syncs of data objects, and is separate from the single-record write limit.</p>

<h2 id="request-parameters">Request parameters</h2>

<p>The following table lists and describes the JSON request body parameters for the <code class="language-plaintext highlighter-rouge">/data_objects/object_relationships</code> endpoint.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Create or replace object relationships in bulk request parameters">
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
      <td><code class="language-plaintext highlighter-rouge">records</code></td>
      <td>Required</td>
      <td>Array</td>
      <td>The object relationships to create or replace. Must contain 1 to 50 records. Braze rejects any other top-level field.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">records[].type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Type of the source object</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">records[].object_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Identifier of the source object</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">records[].rel_kind</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Name of the relationship type. To list valid values, use <a href="/docs/api/endpoints/data_objects/types/get_list_object_relationship_types">List object relationship types</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">records[].related_type_name</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Type of the target object</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">records[].related_object_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Identifier of the target object</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">records[].attributes</code></td>
      <td>Required</td>
      <td>Object</td>
      <td>Relationship attributes, keyed by field name. Send <code class="language-plaintext highlighter-rouge">{}</code> if the relationship type has none.</td>
    </tr>
  </tbody>
</table>

<h3 id="how-braze-processes-the-batch">How Braze processes the batch</h3>

<ul>
  <li>Validation is all-or-nothing. If any record fails validation, Braze rejects the whole request with <code class="language-plaintext highlighter-rouge">400</code>, stores nothing, and lists every error. Fix the errors and resend the whole request.</li>
  <li>Lookups happen during processing. Braze checks whether the types, relationship type, and objects exist, and whether the attributes match the relationship type’s fields, when it processes the batch. A request that returns <code class="language-plaintext highlighter-rouge">202</code> can still produce failures for individual records later. See <a href="#processing-failures">Processing failures</a>.</li>
  <li>Records are ordered by receipt time. Braze stamps every record with the time it received the request, so don’t send <code class="language-plaintext highlighter-rouge">updated_at</code>. Braze rejects a request that includes it. When two requests change the same relationship, the one Braze received later wins, and Braze skips an older write that arrives afterward.</li>
  <li>Relationships can wait on their objects. A relationship whose source or target object doesn’t exist yet waits instead of failing right away. Braze retries for about 40 hours (10 attempts). If the object still doesn’t exist after that, the record fails with <code class="language-plaintext highlighter-rouge">data-object-dependency-not-found</code>.</li>
</ul>

<h2 id="example-request">Example request</h2>

<p>This section includes a sample JSON payload and a sample cURL request.</p>

<h3 id="sample-request-payload">Sample request payload</h3>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"records"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"contact"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"object_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"contact-001"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"rel_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"works_at"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"related_type_name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"account"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"related_object_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"acct-001"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"attributes"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="nl">"since"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2024-01-15T00:00:00Z"</span><span class="p">}</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="sample-curl-request">Sample cURL request</h3>

<p>This example links <code class="language-plaintext highlighter-rouge">contact-001</code> to <code class="language-plaintext highlighter-rouge">acct-001</code> with the <code class="language-plaintext highlighter-rouge">works_at</code> relationship type and records when the relationship started.</p>

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
</pre></td><td class="rouge-code"><pre>curl <span class="nt">--location</span> <span class="nt">--request</span> PUT <span class="s1">'https://rest.iad-01.braze.com/data_objects/object_relationships'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Authorization: Bearer YOUR_REST_API_KEY'</span> <span class="se">\</span>
<span class="nt">--header</span> <span class="s1">'Content-Type: application/json'</span> <span class="se">\</span>
<span class="nt">--data-raw</span> <span class="s1">'{
  "records": [
    {
      "type_name": "contact",
      "object_id": "contact-001",
      "rel_kind": "works_at",
      "related_type_name": "account",
      "related_object_id": "acct-001",
      "attributes": {"since": "2024-01-15T00:00:00Z"}
    }
  ]
}'</span>
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>This section includes a sample successful response and the response fields.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">202</code> could return the following response body.</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"source_import_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"api-20261022T153012123456-9f3a1c2b"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"status"</span><span class="p">:</span><span class="w"> </span><span class="s2">"queued"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"record_count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="response-parameters">Response parameters</h3>

<p>The following table lists and describes the fields in a successful response.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3 reset-td-br-4" aria-label="Create or replace object relationships in bulk response parameters">
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
      <td><code class="language-plaintext highlighter-rouge">source_import_id</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The identifier Braze generated for this request. Every request is its own import.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">status</code></td>
      <td>Required</td>
      <td>String</td>
      <td>Always <code class="language-plaintext highlighter-rouge">queued</code>. The batch is accepted and waiting to be processed.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">record_count</code></td>
      <td>Required</td>
      <td>Integer</td>
      <td>The number of records in the request</td>
    </tr>
  </tbody>
</table>

<h2 id="processing-failures">Processing failures</h2>

<p>Braze doesn’t return these codes from the endpoint. It records them for individual records when it processes a queued batch.</p>

<table class="reset-td-br-1 reset-td-br-2" aria-label="Create or replace object relationships in bulk processing failure codes">
  <thead>
    <tr>
      <th>Code</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data-object-type-not-found</code></td>
      <td><code class="language-plaintext highlighter-rouge">type_name</code> or <code class="language-plaintext highlighter-rouge">related_type_name</code> names no active type in the workspace.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data-object-relationship-type-not-found</code></td>
      <td><code class="language-plaintext highlighter-rouge">rel_kind</code> names no active relationship type for these types.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data-object-schema-mismatch</code></td>
      <td><code class="language-plaintext highlighter-rouge">attributes</code> don’t match the relationship type’s fields. The message names every attribute at fault.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data-object-ingestion-rejected</code></td>
      <td>Any other rejection.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">data-object-dependency-not-found</code></td>
      <td>The source or target object was still missing after about 40 hours of retries.</td>
    </tr>
  </tbody>
</table>

<h2 id="errors">Errors</h2>

<p>A <code class="language-plaintext highlighter-rouge">400</code> response means Braze stored nothing. Each error has an <code class="language-plaintext highlighter-rouge">id</code>, a <code class="language-plaintext highlighter-rouge">message</code>, the <code class="language-plaintext highlighter-rouge">parameter</code> at fault when there is one, and, for record-level errors, the record’s <code class="language-plaintext highlighter-rouge">index</code> (its 0-based position in <code class="language-plaintext highlighter-rouge">records</code>).</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="nl">"index"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"schema-mismatch"</span><span class="p">,</span><span class="w"> </span><span class="nl">"parameter"</span><span class="p">:</span><span class="w"> </span><span class="s2">"rel_kind"</span><span class="p">,</span><span class="w"> </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"rel_kind is required"</span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<p>The following table lists common errors for this endpoint and how to resolve them.</p>

<table class="reset-td-br-1 reset-td-br-2 reset-td-br-3" aria-label="Create or replace object relationships in bulk errors">
  <thead>
    <tr>
      <th>Status</th>
      <th>Cause</th>
      <th>Guidance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">400</code></td>
      <td>Invalid request (<code class="language-plaintext highlighter-rouge">invalid-request</code>): the body isn’t a JSON object or is malformed JSON, <code class="language-plaintext highlighter-rouge">records</code> is missing or has fewer than 1 or more than 50 entries, or the body contains a field Braze sets (<code class="language-plaintext highlighter-rouge">source_type</code>, <code class="language-plaintext highlighter-rouge">source_import_id</code>, <code class="language-plaintext highlighter-rouge">source_chunk_id</code>, or <code class="language-plaintext highlighter-rouge">record_type</code>)</td>
      <td>Send a JSON object whose only field is <code class="language-plaintext highlighter-rouge">records</code>, with 1 to 50 records.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">400</code></td>
      <td>Schema mismatch (<code class="language-plaintext highlighter-rouge">schema-mismatch</code>): a record is missing a required field, has an unrecognized field (including <code class="language-plaintext highlighter-rouge">updated_at</code>), or has a field of the wrong type or an empty string</td>
      <td>Fix every listed record and resend the whole request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">401</code></td>
      <td>Missing or invalid REST API key</td>
      <td>Verify the <code class="language-plaintext highlighter-rouge">Authorization</code> header uses <code class="language-plaintext highlighter-rouge">Bearer YOUR_REST_API_KEY</code> and that the key is active.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">403</code></td>
      <td>API key lacks permission or request is blocked by allowlist</td>
      <td>Confirm the key has <code class="language-plaintext highlighter-rouge">data_objects.object_relationships.bulk_upsert</code> and that your source IP is on the key allowlist, if configured.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">404</code></td>
      <td>Data Objects isn’t enabled for your company</td>
      <td>Confirm your workspace is provisioned for Accounts.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">429</code></td>
      <td>Rate limit exceeded</td>
      <td>Retry after <code class="language-plaintext highlighter-rouge">X-RateLimit-Reset</code> and reduce request frequency.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">500</code></td>
      <td>The batch couldn’t be accepted (<code class="language-plaintext highlighter-rouge">internal-error</code>)</td>
      <td>Braze accepted nothing, so it’s safe to retry the request.</td>
    </tr>
  </tbody>
</table>
</div>
