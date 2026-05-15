<div id='api_bcjpthhgduvt' class='api_div'>
<h1 id="list-catalogs">List catalogs</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/catalogs</p>
</div>

<blockquote>
  <p>Use this endpoint to return a list of catalogs in a workspace.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d65fb86-ccf7-423f-9eb2-f68ab36df824" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">catalogs.get</code> permission.</p>

<h2 id="rate-limit">Rate limit</h2>

<!---DEFAULT RATE LIMIT-->

<!---Additional if statement for Messaging endpoints-->

<!---Additional if statement for Translation endpoints-->

<!---Additional if statement for /messages/send endpoint-->

<h2 id="path-and-request-parameters">Path and request parameters</h2>

<p>There are no path or request parameters for this endpoint.</p>

<h2 id="example-request">Example request</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
</pre></td><td class="rouge-code"><pre>curl --location --request GET 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

<h3 id="example-success-response">Example success response</h3>

<p>The status code <code class="language-plaintext highlighter-rouge">200</code> could return the following response body.</p>

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
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Created_At"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"time"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"restaurants"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"num_items"</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span><span class="p">,</span><span class="w">
      </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-11-02T20:04:06.879+00:00"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"description"</span><span class="p">:</span><span class="w"> </span><span class="s2">"My Catalog"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"fields"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"id"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string_field"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"string"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"number_field"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"number"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"boolean_field"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"boolean"</span><span class="w">
        </span><span class="p">},</span><span class="w">
        </span><span class="p">{</span><span class="w">
          </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"time_field"</span><span class="p">,</span><span class="w">
          </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"time"</span><span class="w">
        </span><span class="p">}</span><span class="w">
      </span><span class="p">],</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"my_catalog"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"num_items"</span><span class="p">:</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w">
      </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-11-02T09:03:19.967+00:00"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">],</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
