<div id='api_asmeodsqnfvj' class='api_div'>
<h1 id="create-catalog">Create catalog</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/catalogs</p>
</div>

<blockquote>
  <p>Use this endpoint to create a catalog.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">catalogs.create</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

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
      <td><code class="language-plaintext highlighter-rouge">catalogs</code></td>
      <td>Required</td>
      <td>Array</td>
      <td>An array that contains catalog objects. Only one catalog object is allowed for this request.</td>
    </tr>
  </tbody>
</table>

<h3 id="catalog-object-parameters">Catalog object parameters</h3>

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
      <td>The name of the catalog that you want to create.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">description</code></td>
      <td>Required</td>
      <td>String</td>
      <td>The description of the catalog that you want to create.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">fields</code></td>
      <td>Required</td>
      <td>Array</td>
      <td>An array of objects where the object contains keys <code class="language-plaintext highlighter-rouge">name</code> and <code class="language-plaintext highlighter-rouge">type</code>.</td>
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
</pre></td><td class="rouge-code"><pre>curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<p>There are two status code responses for this endpoint: <code class="language-plaintext highlighter-rouge">201</code> and <code class="language-plaintext highlighter-rouge">400</code>.</p>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">201</code> could return the following response body.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"catalogs"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="s2">"My Restaurants"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"fields"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"id"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Name"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"City"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cuisine"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Rating"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"number"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Loyalty_Program"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"boolean"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"object"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top_Dishes"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"array"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Created_At"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"time"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"restaurants"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"num_items"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">
      </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-11-02T20:04:06.879+00:00"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h3 id="example-error-response">Example error response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">400</code> could return the following response body. Refer to <a href="#troubleshooting">Troubleshooting</a> for more information about errors you may encounter.</p>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"catalog-name-already-exists"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"A catalog with that name already exists"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"parameters"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"name"</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"parameter_values"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="s2">"restaurants"</span><span class="w">
      </span><span class="p">]</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Invalid Request"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="troubleshooting">Troubleshooting</h2>

<p>The following table lists possible returned errors and their associated troubleshooting steps.</p>

<table class="reset-td-br-1 reset-td-br-2" role="presentation">
  <thead>
    <tr>
      <th>Error</th>
      <th>Troubleshooting</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">catalog-array-invalid</code></td>
      <td><code class="language-plaintext highlighter-rouge">catalogs</code> must be an array of objects.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">catalog-name-already-exists</code></td>
      <td>Catalog with that name already exists.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">catalog-name-too-large</code></td>
      <td>Character limit for a catalog name is 250.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">description-too-long</code></td>
      <td>Character limit for description is 250.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">field-names-not-unique</code></td>
      <td>The same field name is referenced twice.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">field-names-too-large</code></td>
      <td>Character limit for a field name is 250.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">id-not-first-column</code></td>
      <td>The <code class="language-plaintext highlighter-rouge">id</code> must be the first field in the array. Check that the type is a string.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-catalog-name</code></td>
      <td>Catalog name can only include letters, numbers, hyphens, and underscores.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-field-names</code></td>
      <td>Fields can only include letters, numbers, hyphens, and underscores.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-field-types</code></td>
      <td>Make sure the field types are valid.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid-fields</code></td>
      <td><code class="language-plaintext highlighter-rouge">fields</code> is not formatted correctly.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">too-many-catalog-atoms</code></td>
      <td>You can only create one catalog per request.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">too-many-fields</code></td>
      <td>Number of fields limit is 500.</td>
    </tr>
  </tbody>
</table>

</div>
