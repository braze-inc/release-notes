<div id='api_vrsggejbahmq' class='api_div'>
<h1 id="list-preference-centers">List preference centers</h1>
<div class="api_type"><div class="method get ">get</div>
<p>/preference_center/v1/list</p>
</div>

<blockquote>
  <p>Use this endpoint to list your available preference centers.</p>
</blockquote>

<div class="api_reference postman"><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dd8f6667-5eba-4e19-a29e-ba74644c0b8e" class="seeme">See me in Postman</a></div>

<h2 id="prerequisites">Prerequisites</h2>

<p>To use this endpoint, you’ll need an <a href="/docs/api/basics#rest-api-key/">API key</a> with the <code class="language-plaintext highlighter-rouge">preference_center.list</code> permission.</p>

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
</pre></td><td class="rouge-code"><pre>curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/list \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
</pre></td></tr></tbody></table></code></pre></div></div>

<h2 id="response">Response</h2>

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
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"preference_centers"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"My Preference Center 1"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"preference_center_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"preference_center_api_id"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-08-17T15:46:10Z"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-08-17T15:46:10Z"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"My Preference Center 2"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"preference_center_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"preference_center_api_id"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-08-19T11:13:06Z"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-08-19T11:13:06Z"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"My Preference Center 3"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"preference_center_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"preference_center_api_id"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-08-19T11:30:50Z"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-08-19T11:30:50Z"</span><span class="w">
    </span><span class="p">},</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"My Preference Center 4"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"preference_center_api_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"preference_center_api_id"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"created_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-09-13T20:41:34Z"</span><span class="p">,</span><span class="w">
      </span><span class="nl">"updated_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2022-09-13T20:41:34Z"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

</div>
