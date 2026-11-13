<div id='api_hmjlsicpbpkt' class='api_div' data-search-keywords='create and update users message errors type'>
<h1 id="create-and-update-users">Create and update users</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/users/track</p>
<div class="coreclass core_endpoint "><a href="/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to record custom events and purchases and update user profile attributes.</p>
</blockquote>

<p><strong>Note:</strong></p>

<p>Each custom attribute sent in a request to <code class="language-plaintext highlighter-rouge">/users/track</code> consumes a data point. For more information, see <a href="/docs/user_guide/data/infrastructure/data_points">Data points</a>.</p>

<p>Braze processes the data passed through the API at face value, and you should only pass deltas (changing data) to minimize unnecessary data point logging.</p>

<p><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59">View in Postman</a></p>

<div class="api-reference light-mode" id="endpoint-reference">
  <div id="scalar-users_track"></div>
</div>

<script>
  (function () {
    // Update the integrity hash whenever the pinned version changes.
    var scalarSrc = "https://cdn.jsdelivr.net/npm/@scalar/api-reference@1.76.2/dist/browser/standalone.js";
    var scalarIntegrity = "sha384-mCh2A/B6vkfhiHyzwBZm7lbFmEK5fE/96Kbtk+RH1zei1P/XEt0I2MCiG6WfZdor";
    var specUrl = "/docs/assets/api/openapi/users_track.yaml";
    var baseUrl = "/docs";
    var mountSelector = "#" + "scalar-users_track";

    // Scalar renders tooltips in its own containers at the end of <body>.
    var brandVariables = [
      ".api-reference.light-mode, .api-reference .light-mode, body > .scalar-app {",
      "  --scalar-color-accent: #801ed7;",
      "  --scalar-color-1: #212123;",
      "  --scalar-color-2: #475467;",
      "  --scalar-border-color: #dddde2;",
      "  --scalar-font: \"Aribau Grotesk API Reference\", \"Aribau Grotesk Regular Fallback\", Arial, Helvetica, sans-serif;",
      "  --scalar-font-code: \"Roboto Mono\", \"Roboto Mono Fallback\", monospace;",
      "}"
    ].join("\n");

    function loadScalar() {
      if (window.Scalar && typeof window.Scalar.createApiReference === "function") {
        return Promise.resolve(window.Scalar);
      }
      if (!window.__brazeScalarPromise) {
        window.__brazeScalarPromise = new Promise(function (resolve, reject) {
          var script = document.createElement("script");
          script.src = scalarSrc;
          script.integrity = scalarIntegrity;
          script.crossOrigin = "anonymous";
          script.addEventListener("load", function () { resolve(window.Scalar); });
          script.addEventListener("error", reject);
          document.body.appendChild(script);
        });
      }
      return window.__brazeScalarPromise;
    }

    function countLeadingSpaces(line) {
      var match = line.match(/^ */);
      return match ? match[0].length : 0;
    }

    function isBlockScalarKey(line) {
      return /^(\s*)(?:"[^"]+"|'[^']+'|[A-Za-z0-9_.-]+):\s*[|>][+-]?\s*$/.test(line);
    }

    function isYamlKeyLine(trimmedLine, indent, blockIndent) {
      if (indent > blockIndent) { return false; }
      if (/^(?:"[^"]+"|'[^']+'|[A-Za-z0-9_.-]+):\s*/.test(trimmedLine)) { return true; }
      if (/^-\s+(?:"[^"]+"|'[^']+'|[A-Za-z0-9_.-]+):\s*/.test(trimmedLine)) { return true; }
      return false;
    }

    function sanitizeYamlBlockScalars(rawYaml) {
      var lines = rawYaml.replace(/\r\n/g, "\n").split("\n");
      var blockIndent = null;
      var contentIndent = null;

      for (var i = 0; i < lines.length; i += 1) {
        var line = lines[i];
        var trimmed = line.trim();
        var indent = countLeadingSpaces(line);

        if (blockIndent !== null) {
          if (trimmed === "") {
            continue;
          }

          if (isYamlKeyLine(trimmed, indent, blockIndent)) {
            blockIndent = null;
            contentIndent = null;
          } else if (indent < contentIndent) {
            lines[i] = " ".repeat(contentIndent) + trimmed;
            continue;
          }
        }

        if (blockIndent === null && isBlockScalarKey(line)) {
          blockIndent = indent;
          contentIndent = indent + 2;
        }
      }

      return lines.join("\n");
    }

    // Liquid is disabled for the YAML assets, so resolve the site.baseurl
    // token here before Scalar renders the Markdown links.
    function loadSpec() {
      return fetch(specUrl, { credentials: "same-origin" }).then(function (response) {
        if (!response.ok) { throw new Error("Failed to load " + specUrl); }
        return response.text();
      }).then(function (rawSpec) {
        var withBaseUrl = rawSpec.replace(/\{\{\s*site\.baseurl\s*\}\}/g, baseUrl);
        return sanitizeYamlBlockScalars(withBaseUrl);
      });
    }

    // Every spec lists the docs home page as `info.license`, which Scalar shows
    // as a "Braze Documentation" link that repeats the site navigation.
    function withoutLicense(specText) {
      return specText.replace(/^ {2}license:\n(?: {4}.*\n)*/m, "");
    }

    function specTitle(specText) {
      var match = specText.match(/^ {2}title: (.*)$/m);
      return match ? match[1].trim() : "";
    }

    // The page already shows the endpoint name as its title, so the spec title
    // labels the intro instead, and the operation summary is dropped so Scalar
    // heads the operation with its route.
    function forReference(specText) {
      return withoutLicense(specText)
        .replace(/^ {2}title: .*$/m, "  title: About this endpoint")
        .replace(/^( {4}(?:get|post|put|patch|delete):\n) {6}summary: .*\n/m, "$1");
    }

    // The REST API answers CORS preflight requests only for GET and POST, so a
    // browser can't send PUT, PATCH, or DELETE.
    function usesPreflightedMethod(specText) {
      return /^ {4}(put|patch|delete):\s*$/m.test(specText);
    }

    // Lists the description headings, request body, and responses in the page
    // TOC. Scalar's own title and operation headings are left out.
    // Scalar's headings sit under the page h1, so screen readers hear them one
    // level deeper: the intro title and the operation route at level 2, the
    // description headings at their tag level plus one, and Body and Responses
    // at level 3.
    function markTocHeadings(root, title) {
      var signature = [];
      var main = root.querySelector("main[aria-label]");
      if (main && title) { main.setAttribute("aria-label", "API documentation for " + title); }
      root.querySelectorAll("h1").forEach(function (heading) {
        heading.setAttribute("role", "heading");
        heading.setAttribute("aria-level", "2");
      });
      root.querySelectorAll('h2[id*="/description/"], h3[id*="/description/"]').forEach(function (heading) {
        var level = Number(heading.tagName.charAt(1));
        heading.setAttribute("role", "heading");
        heading.setAttribute("aria-level", String(level + 1));
        heading.setAttribute("data-toc-level", String(level));
        heading.setAttribute("data-toc-label", heading.textContent.trim());
        signature.push(heading.id);
      });
      root.querySelectorAll('h3:not([id*="/description/"])').forEach(function (heading) {
        heading.setAttribute("role", "heading");
        heading.setAttribute("aria-level", "2");
      });
      root.querySelectorAll("h4").forEach(function (heading) {
        var text = heading.textContent.trim();
        var section = /^Body\b/.test(text) ? { id: "endpoint-request-body", label: "Request body" }
          : text === "Responses" ? { id: "endpoint-responses", label: "Responses" }
          : null;
        heading.setAttribute("role", "heading");
        heading.setAttribute("aria-level", "3");
        if (section) {
          heading.id = section.id;
          heading.setAttribute("data-toc-level", "2");
          heading.setAttribute("data-toc-label", section.label);
          signature.push(section.id);
        }
      });
      return signature.join(",");
    }

    function headingSlug(text) {
      return text.trim().toLowerCase().replace(/[^\w\- ]+/g, "").replace(/ /g, "-");
    }

    // Finds the element a fragment points to: an element with that id, or a
    // description heading whose Scalar id ends in that slug or whose text
    // slugs to it.
    function findAnchorTarget(root, fragment) {
      if (!fragment) { return null; }
      var exact = document.getElementById(fragment);
      if (exact) { return exact; }
      var headings = root.querySelectorAll('[id*="/description/"]');
      for (var i = 0; i < headings.length; i += 1) {
        var heading = headings[i];
        if (heading.id.split("/description/").pop() === fragment || headingSlug(heading.textContent) === fragment) {
          return heading;
        }
      }
      return null;
    }

    function scrollToFragment(root, fragment) {
      var target = findAnchorTarget(root, fragment);
      if (target && root.contains(target)) {
        target.scrollIntoView();
        return true;
      }
      return false;
    }

    function resolveFragmentLinks(root) {
      document.addEventListener("click", function (evt) {
        var link = evt.target && evt.target.closest ? evt.target.closest('a[href^="#"]') : null;
        if (!link) { return; }
        var fragment = decodeURIComponent(link.getAttribute("href").substring(1));
        if (!fragment || document.getElementById(fragment)) { return; }
        if (scrollToFragment(root, fragment)) {
          evt.preventDefault();
          history.pushState(null, "", "#" + encodeURIComponent(fragment));
        }
      });
      window.addEventListener("hashchange", function () {
        scrollToFragment(root, decodeURIComponent(window.location.hash.substring(1)));
      });
    }

    function syncTocWithReference(root, title) {
      var lastSignature = "";
      var settleTimer = null;
      new MutationObserver(function () {
        clearTimeout(settleTimer);
        settleTimer = setTimeout(function () {
          var signature = markTocHeadings(root, title);
          if (signature === lastSignature) { return; }
          var isFirstRender = lastSignature === "";
          lastSignature = signature;
          document.dispatchEvent(new CustomEvent("api-reference:rendered"));
          if (isFirstRender && window.location.hash) {
            scrollToFragment(root, decodeURIComponent(window.location.hash.substring(1)));
          }
        }, 200);
      }).observe(root, { childList: true, subtree: true });
    }

    // Log engagement to Braze via the Web SDK loaded site-wide in analytics.html.
    // Tracking must never break the page, so guard every call.
    function brazeLog(eventName, properties) {
      try {
        if (window.braze && typeof window.braze.logCustomEvent === "function") {
          window.braze.logCustomEvent(eventName, properties || {});
          if (typeof window.braze.requestImmediateDataFlush === "function") {
            window.braze.requestImmediateDataFlush();
          }
        }
      } catch (err) { /* no-op */ }
    }

    // Readers can type their own values into the Test Request window, and its
    // buttons repeat the request URL, so labels from outside the reference drop URLs.
    function labelOf(el, fromReference) {
      var text = (el.getAttribute("aria-label") || el.innerText || el.textContent || "").replace(/\s+/g, " ").trim();
      if (!fromReference) { text = text.replace(/https?:\/\/\S*/g, "").trim(); }
      return text.slice(0, 80);
    }

    function statusOf(el) {
      var match = (el.textContent || "").match(/\b([1-5](?:\d\d|XX))\b/);
      return match ? match[1] : "";
    }

    function referenceEvent(name, properties) {
      var props = {
        page_url: window.location.pathname,
        page_title: document.title,
        spec: specUrl.split("/").pop()
      };
      Object.keys(properties || {}).forEach(function (key) { props[key] = properties[key]; });
      brazeLog(name, props);
    }

    var openMenu = "";
    var testRequestEndpoint = "";

    function trackOption(target) {
      var label = labelOf(target, openMenu === "server");
      if (openMenu === "server") {
        referenceEvent("api_server_selected", { server: label });
      } else if (openMenu === "code_language") {
        referenceEvent("api_code_language_selected", { language: label });
      } else if (openMenu === "request_example") {
        referenceEvent("api_request_example_selected", { example: label });
      } else if (openMenu === "schema_variant") {
        referenceEvent("api_schema_variant_selected", { variant: label });
      } else {
        referenceEvent("api_test_request_button_clicked", { button: label });
      }
      openMenu = "";
    }

    function inResponses(target) {
      var heading = document.getElementById("endpoint-responses");
      return !!heading && !!(heading.compareDocumentPosition(target) & Node.DOCUMENT_POSITION_FOLLOWING);
    }

    function trackTestRequestClick(target) {
      var label = labelOf(target, false);
      openMenu = "test_request";
      if (target.tagName === "INPUT") { return; }
      if (/^Send\b/.test(label)) {
        referenceEvent("api_send_request_clicked", { endpoint: testRequestEndpoint });
      } else if (/^Close Client/.test(label)) {
        referenceEvent("api_close_test_request_clicked", { endpoint: testRequestEndpoint });
      } else if (target.getAttribute("role") === "tab") {
        referenceEvent("api_test_request_tab_clicked", { tab: label });
      } else {
        referenceEvent("api_test_request_button_clicked", { button: label });
      }
    }

    function trackReferenceButton(target) {
      var label = labelOf(target, true);
      openMenu = "";
      if (target.classList.contains("scalar-card-checkbox-input")) {
        referenceEvent("api_response_schema_toggle_clicked", { shown: target.checked });
      } else if (target.tagName === "INPUT" || target.classList.contains("ask-agent-scalar-send")) {
        return;
      } else if (target.classList.contains("show-api-client-button")) {
        var endpoint = target.textContent.match(/\((\w+) ([^)]+)\)/);
        testRequestEndpoint = endpoint ? endpoint[1].toUpperCase() + " " + endpoint[2] : "";
        referenceEvent("api_test_request_clicked", { endpoint: testRequestEndpoint });
      } else if (/^Server:/.test(label)) {
        openMenu = "server";
        referenceEvent("api_server_menu_clicked");
      } else if (target.classList.contains("client-libraries__select") || target.getAttribute("data-testid") === "client-picker") {
        openMenu = "code_language";
        referenceEvent("api_code_language_menu_clicked");
      } else if (target.classList.contains("client-libraries")) {
        referenceEvent("api_code_language_clicked", { language: label });
      } else if (target.getAttribute("data-testid") === "example-picker") {
        openMenu = "request_example";
        referenceEvent("api_request_example_menu_clicked");
      } else if (target.classList.contains("composition-selector")) {
        openMenu = "schema_variant";
        referenceEvent("api_schema_variant_menu_clicked");
      } else if (target.classList.contains("anchor-copy-button") || target.classList.contains("copy-link-trailing")) {
        referenceEvent("api_copy_link_clicked", { target: label });
      } else if (label === "Copy as Markdown") {
        referenceEvent("api_copy_as_markdown_clicked");
      } else if (target.classList.contains("security-requirement-badge") || /^Authentication Required/.test(label)) {
        referenceEvent("api_authentication_details_clicked");
      } else if (target.classList.contains("parameter-item-trigger") && inResponses(target)) {
        referenceEvent("api_response_details_clicked", { status: statusOf(target) });
      } else if (target.classList.contains("parameter-item-trigger")) {
        referenceEvent("api_parameter_details_clicked", { parameter: label });
      } else if (target.getAttribute("role") === "tab" && target.classList.contains("tab")) {
        referenceEvent("api_response_example_tab_clicked", { status: statusOf(target) });
      } else {
        referenceEvent("api_reference_button_clicked", { button: label });
      }
    }

    var specForDownload = "";

    // Scalar's download button exports the spec as rendered, with the intro
    // title and without the summary and license, so it saves the spec as written.
    function downloadSpec() {
      var link = document.createElement("a");
      link.href = URL.createObjectURL(new Blob([specForDownload], { type: "application/yaml" }));
      link.download = specUrl.split("/").pop();
      document.body.appendChild(link);
      link.click();
      link.remove();
      setTimeout(function () { URL.revokeObjectURL(link.href); }, 0);
    }

    // The Swagger-era event names stay, so existing reports keep working.
    function trackReferenceClicks() {
      if (window.__openapiTrackingBound) { return; }
      window.__openapiTrackingBound = true;
      document.addEventListener("click", function (evt) {
        var target = evt.target && evt.target.closest ? evt.target.closest("a, button, [role=option], input") : null;
        if (!target) { return; }
        var inReference = !!target.closest(".api-reference");
        var inScalar = inReference || !!target.closest(".scalar-app");
        var page = window.location.pathname;
        var href = target.getAttribute("href") || "";
        var label = target.getAttribute("aria-label") || "";
        if (href.indexOf("/assets/api/openapi/") !== -1 || /^Download OpenAPI Document/.test(label)) {
          if (inReference && !href && specForDownload) {
            evt.preventDefault();
            evt.stopPropagation();
            downloadSpec();
          }
          brazeLog("docs_api_spec_download_click", { spec_url: href || specUrl, page: page });
        } else if (href.indexOf("/api/openapi_schema_validation") !== -1) {
          brazeLog("docs_api_validation_guide_click", { page: page });
        } else if (inReference && /^Copy .+ code$/.test(label)) {
          brazeLog("docs_api_copy_code_click", {
            block_type: /JSON/.test(label) ? "response" : "request",
            spec: specUrl.split("/").pop(),
            page: page
          });
        } else if (!inScalar) {
          return;
        } else if (target.tagName === "A" && href.indexOf("/braze_support") !== -1) {
          referenceEvent("api_braze_support_clicked", { link_url: href });
        } else if (target.tagName === "A") {
          referenceEvent("api_reference_link_clicked", {
            link_url: inReference ? href : href.split("?")[0],
            link_text: labelOf(target, inReference)
          });
        } else if (target.getAttribute("role") === "option") {
          trackOption(target);
        } else if (target.closest(".scalar-app-layout")) {
          trackTestRequestClick(target);
        } else if (inReference) {
          trackReferenceButton(target);
        }
      }, true);
      document.addEventListener("submit", function (evt) {
        if (evt.target && evt.target.closest && evt.target.closest(".api-reference .agent-button-container")) {
          referenceEvent("api_ask_ai_agent_submitted");
        }
      }, true);
      document.addEventListener("keydown", function (evt) {
        if (evt.key === "Enter" && (evt.metaKey || evt.ctrlKey) && evt.target && evt.target.closest && evt.target.closest(".scalar-app-layout")) {
          referenceEvent("api_send_request_clicked", { endpoint: testRequestEndpoint, via: "shortcut" });
        }
      }, true);
    }

    trackReferenceClicks();

    Promise.all([loadScalar(), loadSpec()]).then(function (results) {
      var root = document.querySelector(mountSelector);
      specForDownload = results[1];
      syncTocWithReference(root, specTitle(results[1]));
      resolveFragmentLinks(root);
      results[0].createApiReference(mountSelector, {
        content: forReference(results[1]),
        layout: "modern",
        showSidebar: false,
        hideSearch: true,
        hideModels: true,
        orderSchemaPropertiesBy: "preserve",
        documentDownloadType: "yaml",
        defaultHttpClient: { targetKey: "shell", clientKey: "curl" },
        telemetry: false,
        persistAuth: false,
        hideClientButton: true,
        hideTestRequestButton: usesPreflightedMethod(results[1]),
        hideDarkModeToggle: true,
        forceDarkModeState: "light",
        showDeveloperTools: "never",
        urlRouting: false,
        withDefaultFonts: false,
        customCss: brandVariables
      });
    }).catch(function (error) {
      console.error("[api-reference]", error);
    });
  })();
</script>

<h2 id="need-to-update-users-in-bulk">Need to update users in bulk?</h2>

<p>Use the <a href="/docs/api/endpoints/user_data/post_user_track_bulk/"><code class="language-plaintext highlighter-rouge">/users/track/bulk</code> endpoint</a> to send larger batches and reduce request volume.</p>

<h2 id="track-request-processing-status">Track request processing status</h2>

<p><strong>Important:</strong></p>

<p>Request processing status is in beta. If you’re interested in participating in the beta, contact your Braze account manager.</p>

<p>Braze processes <code class="language-plaintext highlighter-rouge">/users/track</code> requests asynchronously. A successful response means Braze received your request and queued it for processing, but the data might not be on the user profile yet. To confirm when processing finishes, add a <code class="language-plaintext highlighter-rouge">group_id</code> to your requests and check the group’s status with the <a href="/docs/api/endpoints/user_data/get_users_track_status"><code class="language-plaintext highlighter-rouge">/users/track/status</code> endpoint</a>.</p>

<p>Use request processing status to do the following:</p>

<ul>
  <li>Confirm that attribute or subscription updates are on a profile before you trigger a Canvas or campaign that depends on them</li>
  <li>Confirm that a backfill or import has finished before you launch messaging to the affected users</li>
  <li>Keep a record that high-priority updates, such as consent changes, finished processing</li>
</ul>

<h3 id="how-it-works">How it works</h3>

<ol>
  <li>Choose a <code class="language-plaintext highlighter-rouge">group_id</code> for a set of related requests. For example, use one <code class="language-plaintext highlighter-rouge">group_id</code> for every request in a backfill, or a unique <code class="language-plaintext highlighter-rouge">group_id</code> for a single request you want to confirm.</li>
  <li>Include the <code class="language-plaintext highlighter-rouge">group_id</code> at the top level of each <code class="language-plaintext highlighter-rouge">/users/track</code> request body. Braze counts each accepted request toward the group.</li>
  <li>Call the <a href="/docs/api/endpoints/user_data/get_users_track_status"><code class="language-plaintext highlighter-rouge">/users/track/status</code> endpoint</a> with the <code class="language-plaintext highlighter-rouge">group_id</code>. When the group’s <code class="language-plaintext highlighter-rouge">status</code> is <code class="language-plaintext highlighter-rouge">completed</code>, Braze has finished processing every request in the group.</li>
</ol>

<p>If you send another request with the same <code class="language-plaintext highlighter-rouge">group_id</code> after the group is <code class="language-plaintext highlighter-rouge">completed</code>, the group’s status returns to <code class="language-plaintext highlighter-rouge">processing</code> until Braze finishes processing the new request.</p>

<p>Braze tracks status for each group as a whole. A group is <code class="language-plaintext highlighter-rouge">completed</code> when Braze finishes processing all requests in the group, including requests where Braze rejected some objects. Braze lists rejected objects in the <code class="language-plaintext highlighter-rouge">errors</code> array of each <code class="language-plaintext highlighter-rouge">/users/track</code> response.</p>

<p>Status tracking is available only for the <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint. Braze doesn’t track status for requests to the <a href="/docs/api/endpoints/user_data/post_user_track_bulk"><code class="language-plaintext highlighter-rouge">/users/track/bulk</code> endpoint</a> or the <a href="/docs/api/endpoints/user_data/post_user_track_synchronous"><code class="language-plaintext highlighter-rouge">/users/track/sync</code> endpoint</a>.</p>

<h3 id="group-id-requirements">Group ID requirements</h3>

<p>A <code class="language-plaintext highlighter-rouge">group_id</code> must be 1 to 128 characters and can contain only letters, numbers, periods (<code class="language-plaintext highlighter-rouge">.</code>), underscores (<code class="language-plaintext highlighter-rouge">_</code>), tildes (<code class="language-plaintext highlighter-rouge">~</code>), and hyphens (<code class="language-plaintext highlighter-rouge">-</code>).</p>

<p>Group IDs are scoped to a workspace. The same <code class="language-plaintext highlighter-rouge">group_id</code> in two workspaces refers to two separate groups.</p>

<p>Use a new <code class="language-plaintext highlighter-rouge">group_id</code> for each set of requests you want to track. Reusing a <code class="language-plaintext highlighter-rouge">group_id</code> adds requests to the existing group and doesn’t extend its retention period.</p>

<h3 id="limits-and-retention">Limits and retention</h3>

<table class="reset-td-br-1 reset-td-br-2" aria-label="Request processing status limits">
  <thead>
    <tr>
      <th>Limit</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Retention</td>
      <td>24 hours<br /><br />Braze retains group status for 24 hours from the time of the first request with a <code class="language-plaintext highlighter-rouge">group_id</code>. After the retention period, the <code class="language-plaintext highlighter-rouge">/users/track/status</code> endpoint returns an empty <code class="language-plaintext highlighter-rouge">results</code> array for that <code class="language-plaintext highlighter-rouge">group_id</code>.</td>
    </tr>
    <tr>
      <td>Requests per group</td>
      <td>6,000,000</td>
    </tr>
    <tr>
      <td>Active groups per workspace</td>
      <td>100,000. A group is active until its retention period ends.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">/users/track/status</code> rate limit</td>
      <td>1,500 requests per minute per workspace. This limit is separate from the <code class="language-plaintext highlighter-rouge">/users/track</code> rate limit.</td>
    </tr>
  </tbody>
</table>

<h3 id="status-tracking-errors">Status tracking errors</h3>

<p>Braze can’t track a request’s status in some cases, such as when your workspace has reached its maximum number of active groups. When this happens, the <code class="language-plaintext highlighter-rouge">/users/track</code> response is still successful and Braze still processes the request’s attributes, events, and purchases. The response includes an entry in the <code class="language-plaintext highlighter-rouge">errors</code> array that describes why Braze isn’t tracking the request:</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><table class="rouge-table"><tbody><tr><td class="rouge-gutter gl"><pre class="lineno">1
2
3
4
5
6
7
8
</pre></td><td class="rouge-code"><pre><span class="p">{</span><span class="w">
  </span><span class="nl">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"success"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="w">
    </span><span class="p">{</span><span class="w">
      </span><span class="nl">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"request_status_group_full"</span><span class="w">
    </span><span class="p">}</span><span class="w">
  </span><span class="p">]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></pre></td></tr></tbody></table></code></pre></div></div>

<table class="reset-td-br-1 reset-td-br-2" aria-label="Status tracking errors">
  <thead>
    <tr>
      <th>Error type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">invalid_group_id</code></td>
      <td>The <code class="language-plaintext highlighter-rouge">group_id</code> isn’t a string, is empty, is longer than 128 characters, or contains characters that aren’t allowed. For more information, see <a href="#group-id-requirements">Group ID requirements</a>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">request_status_active_group_limit_exceeded</code></td>
      <td>Your workspace has reached its limit of active groups. Wait for existing groups to expire, or send the request without a <code class="language-plaintext highlighter-rouge">group_id</code>.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">request_status_group_full</code></td>
      <td>The group has reached its limit of requests. Use a new <code class="language-plaintext highlighter-rouge">group_id</code> for additional requests.</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">request_status_not_tracked</code></td>
      <td>Braze couldn’t track the request. For example, the group’s retention period has ended or status tracking isn’t enabled for your workspace.</td>
    </tr>
  </tbody>
</table>

<h2 id="frequently-asked-questions">Frequently asked questions</h2>

<h3 id="what-happens-when-multiple-profiles-with-the-same-email-address-are-found">What happens when multiple profiles with the same email address are found?</h3>
<p>If the <code class="language-plaintext highlighter-rouge">external_id</code> exists, Braze prioritizes the most recently updated profile with an external ID for updates. If the <code class="language-plaintext highlighter-rouge">external_id</code> doesn’t exist, Braze prioritizes the most recently updated profile for updates.</p>

<h3 id="what-happens-if-no-profile-with-the-email-address-exists">What happens if no profile with the email address exists?</h3>
<p>Braze creates a profile and an email-only user and sets the email field to test@example.com, as noted in the example request for updating a user profile by email address. Braze does not create an alias.</p>

<h3 id="how-do-you-use-userstrack-to-import-legacy-user-data">How do you use <code class="language-plaintext highlighter-rouge">/users/track</code> to import legacy user data?</h3>
<p>You may submit data through the Braze API for a user who has not yet used your mobile app to generate a user profile. If the user subsequently uses the application, all information following their identification using the SDK is merged with the existing user profile you created using the API call. Any user behavior recorded anonymously by the SDK before identification is lost upon merging with the existing API-generated user profile.</p>

<p>The segmentation tool includes these users regardless of whether they have engaged with the app. If you want to exclude users uploaded using the User API who have not yet engaged with the app, add the <code class="language-plaintext highlighter-rouge">Session Count &gt; 0</code> filter.</p>

<h3 id="how-do-i-avoid-creating-duplicate-user-profiles">How do I avoid creating duplicate user profiles?</h3>

<p>Duplicate profiles can occur when a request includes a primary identifier (such as <code class="language-plaintext highlighter-rouge">external_id</code>) that doesn’t match any existing profile, alongside an <code class="language-plaintext highlighter-rouge">email</code> or <code class="language-plaintext highlighter-rouge">phone</code> value that does match an existing profile. Because primary identifiers are used for user lookup, Braze creates a new profile for the unrecognized <code class="language-plaintext highlighter-rouge">external_id</code> instead of updating the existing email-only or phone-only profile.</p>

<p>To avoid duplicates:</p>

<ul>
  <li>When transitioning users from email-only or phone-only profiles to identified profiles, use the <a href="/docs/api/endpoints/user_data/post_user_identify"><code class="language-plaintext highlighter-rouge">/users/identify</code> endpoint</a> to assign an <code class="language-plaintext highlighter-rouge">external_id</code> to the existing profile, rather than sending both to <code class="language-plaintext highlighter-rouge">/users/track</code>.</li>
  <li>If duplicates already exist, merge them using the <a href="/docs/api/endpoints/user_data/post_users_merge"><code class="language-plaintext highlighter-rouge">/users/merge</code> endpoint</a>.</li>
</ul>

<h3 id="how-does-userstrack-handle-duplicate-events">How does <code class="language-plaintext highlighter-rouge">/users/track</code> handle duplicate events?</h3>

<p>Each event object in the events array represents a single occurrence of a custom event by a user at a designated time. This means each event ingested into Braze has its own event ID, so “duplicate” events are treated as separate, unique events.</p>

<h3 id="how-does-userstrack-handle-invalid-nested-custom-attributes">How does <code class="language-plaintext highlighter-rouge">/users/track</code> handle invalid nested custom attributes?</h3>

<p>When a nested custom attribute contains any invalid values (such as invalid time formats or null values), Braze drops all nested custom attribute updates in the request from processing. This applies to all nested structures within that specific attribute. To help ensure successful processing, verify that all values within nested custom attributes are valid before sending.</p>

<h3 id="are-requests-to-userstrack-guaranteed-to-be-processed-in-order">Are requests to <code class="language-plaintext highlighter-rouge">/users/track</code> guaranteed to be processed in order?</h3>

<p>When you make multiple separate API calls to <code class="language-plaintext highlighter-rouge">/users/track</code> in rapid succession, Braze cannot guarantee that requests are processed in the exact order they are sent or received. This is because Braze uses asynchronous processing to maximize speed and flexibility.</p>

<p>For example, if you send multiple update requests for the same user within seconds of each other—some with null attribute values and others with valid values—the requests containing null values may be processed after requests with valid values, even if sent earlier. This can result in attribute values appearing to revert or not reflect the most recently sent update.</p>

<p>To avoid race conditions when updating user data:</p>

<ul>
  <li><strong>Batch updates in a single request:</strong> Include all attribute updates for a user in one API call rather than making separate consecutive calls.</li>
  <li><strong>Add delays between requests:</strong> If you must make separate calls for the same user, add a delay (a few seconds) between requests to allow the first request to complete processing before the next one is sent.</li>
  <li><strong>Avoid overlapping updates for the same field:</strong> If two requests update the same attribute with different values, send those updates in one request or separate them with a delay to reduce the chance of out-of-order results.</li>
  <li><strong>Confirm processing before the next request (beta):</strong> Include a <code class="language-plaintext highlighter-rouge">group_id</code> in the first request, and wait until the <a href="/docs/api/endpoints/user_data/get_users_track_status"><code class="language-plaintext highlighter-rouge">/users/track/status</code> endpoint</a> returns <code class="language-plaintext highlighter-rouge">completed</code> before you send the dependent request. For more information, see <a href="#track-request-processing-status">Track request processing status</a>.</li>
</ul>

<p>For more information about race conditions and best practices, see <a href="/docs/user_guide/messaging/ab_testing/concepts/race_conditions">Race conditions</a>.</p>

<h3 id="how-do-i-know-when-braze-has-finished-processing-my-request">How do I know when Braze has finished processing my request?</h3>

<p>Include a <code class="language-plaintext highlighter-rouge">group_id</code> in your <code class="language-plaintext highlighter-rouge">/users/track</code> requests, then call the <a href="/docs/api/endpoints/user_data/get_users_track_status"><code class="language-plaintext highlighter-rouge">/users/track/status</code> endpoint</a> with that <code class="language-plaintext highlighter-rouge">group_id</code>. When the group’s <code class="language-plaintext highlighter-rouge">status</code> is <code class="language-plaintext highlighter-rouge">completed</code>, Braze has finished processing every request in the group. This feature is in beta. For more information, see <a href="#track-request-processing-status">Track request processing status</a>.</p>

<h3 id="how-often-should-i-check-a-groups-status">How often should I check a group’s status?</h3>

<p>Poll the <code class="language-plaintext highlighter-rouge">/users/track/status</code> endpoint at a regular interval, such as every few seconds, and stop when the group’s <code class="language-plaintext highlighter-rouge">status</code> is <code class="language-plaintext highlighter-rouge">completed</code>. Keep your polling within the endpoint’s rate limit of 1,500 requests per minute per workspace.</p>

<h3 id="why-is-my-group-still-processing">Why is my group still processing?</h3>

<p>A group stays in <code class="language-plaintext highlighter-rouge">processing</code> until Braze finishes processing every accepted request in the group. If a request fails during processing, Braze retries it, and the group stays in <code class="language-plaintext highlighter-rouge">processing</code> until the retry succeeds. If you add requests to a group after it’s <code class="language-plaintext highlighter-rouge">completed</code>, its status returns to <code class="language-plaintext highlighter-rouge">processing</code>. In rare cases, a group can stay in <code class="language-plaintext highlighter-rouge">processing</code> until its retention period ends. If a group stays in <code class="language-plaintext highlighter-rouge">processing</code> for much longer than your usual processing time, contact Braze Support.</p>

<h3 id="why-does-userstrackstatus-return-an-empty-results-array">Why does <code class="language-plaintext highlighter-rouge">/users/track/status</code> return an empty <code class="language-plaintext highlighter-rouge">results</code> array?</h3>

<p>The <code class="language-plaintext highlighter-rouge">results</code> array is empty when Braze doesn’t find the group in your workspace. This happens when the group’s 24-hour retention period has ended, the <code class="language-plaintext highlighter-rouge">group_id</code> doesn’t match the one in your requests, or you sent the requests to a different workspace. It also happens when Braze didn’t track any requests for that <code class="language-plaintext highlighter-rouge">group_id</code>. Check each <code class="language-plaintext highlighter-rouge">/users/track</code> response for <a href="#status-tracking-errors">status tracking errors</a>.</p>

<h3 id="why-is-my-userstrack-response-slower-than-i-expect">Why is my <code class="language-plaintext highlighter-rouge">/users/track</code> response slower than I expect?</h3>

<p>Successful <code class="language-plaintext highlighter-rouge">/users/track</code> calls are usually accepted quickly, but Braze still processes attribute, event, and purchase updates asynchronously. Perceived latency can increase when payloads are large or when network routing to your <a href="/docs/api/basics#endpoints">REST endpoint</a> is slow. If you need a synchronous acknowledgment per user or stricter ordering between calls, see <a href="/docs/api/endpoints/user_data/post_user_track_synchronous"><code class="language-plaintext highlighter-rouge">/users/track/sync</code></a> (<strong>limited beta</strong>).</p>

<h3 id="why-does-userstrack-return-429-too-many-requests">Why does <code class="language-plaintext highlighter-rouge">/users/track</code> return <code class="language-plaintext highlighter-rouge">429 Too Many Requests</code>?</h3>

<p>When your request volume exceeds the <a href="#rate-limit">rate limit</a>, <code class="language-plaintext highlighter-rouge">/users/track</code> returns an HTTP <code class="language-plaintext highlighter-rouge">429 Too Many Requests</code> response. To resume sending requests:</p>

<ol>
  <li>Pause requests for the number of seconds specified in the <code class="language-plaintext highlighter-rouge">X-RateLimit-Retry-After</code> response header.</li>
  <li>Resume requests at a lower rate to reduce the likelihood of another <code class="language-plaintext highlighter-rouge">429</code> response.</li>
  <li>Combine updates when possible, and follow the <a href="#rate-limit">request object limit for your account</a>.</li>
  <li>Use the <a href="/docs/user_guide/analytics/dashboards/api_usage">API usage dashboard</a> to identify request spikes and <code class="language-plaintext highlighter-rouge">429</code> response trends. For workspace defaults and other endpoint limits, see <a href="/docs/api/api_limits">API rate limits</a>.</li>
</ol>

<p>For non-<code class="language-plaintext highlighter-rouge">429</code> responses on supported contracts, use the <code class="language-plaintext highlighter-rouge">X-RateLimit-*</code> response headers described in <a href="#rate-limit-headers-for-monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau">Rate limit headers for Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU</a> to check the remaining requests in the current window.</p>

<h3 id="why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error">Why do I get <code class="language-plaintext highlighter-rouge">400 Bad Request</code> with a bad syntax or parse error?</h3>

<p>An HTTP <code class="language-plaintext highlighter-rouge">400</code> with a syntax or parse error typically means the request body is not valid JSON. Common causes include trailing commas, comments inside JSON, single-quoted strings, an extra opening <code class="language-plaintext highlighter-rouge">{</code> before the payload, or sending a non-JSON body while the <code class="language-plaintext highlighter-rouge">Content-Type</code> header is <code class="language-plaintext highlighter-rouge">application/json</code>. Validate payloads with a JSON linter before sending, confirm your HTTP client JSON-encodes objects (rather than concatenating raw strings), and confirm the body is UTF-8 encoded. For other <code class="language-plaintext highlighter-rouge">400</code> responses (for example, payload size and per-request object limits), refer to <a href="/docs/api/errors#fatal-errors">Fatal errors &amp; responses</a> and the <a href="#endpoint-specific-errors">Endpoint-specific errors</a> table on this page.</p>

<h2 id="monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau">Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU</h2>

<p>For customers on new pricing, rate limits are enforced at the company level. Customers can set workspace rate limits for hourly limits, but burst limits are still shared between all workspaces.</p>

<p>For customers who have purchased Monthly Active Users CY 24-25, Universal MAU, Web MAU, or Mobile MAU, Braze manages different rate limits on its <code class="language-plaintext highlighter-rouge">/users/track</code> endpoint:</p>
<ul>
  <li>Hourly rate limits are set according to the expected data ingestion activity on your account, which may correspond to the number of monthly active users you have purchased, industry, seasonality, or other factors.</li>
  <li>In addition to the hourly limit, Braze enforces a burst limit on the number of requests that can be sent every three seconds.</li>
  <li>Each request may batch up to 75 updates combined across attribute, event, or purchase objects.</li>
</ul>

<p>Current limits based on expected ingestion can be found in the dashboard under <strong>Settings</strong> &gt; <strong>APIs and Identifiers</strong> &gt; <strong>API Usage Dashboard</strong>. We may modify rate limits to protect system stability or allow for increased data throughput on your account. Please contact Braze Support or your customer success manager for questions or concerns regarding the hourly or per-second request limit and the needs of your business.</p>

<h3 id="rate-limit-headers-for-monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau">Rate limit headers for Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU</h3>

<p>All non-rate-limited (such as non-<code class="language-plaintext highlighter-rouge">429</code>) responses contain the following HTTP response headers that indicate the state of the hourly rate limit window to the client. Use these headers to manage your request rate:</p>

<table class="reset-td-br-1 reset-td-br-2" aria-label="Rate limit headers for Monthly Active Users CY 24-25, Universal MAU, Web MAU, and Mobile MAU">
  <thead>
    <tr>
      <th>Header name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">X-RateLimit-Limit</code></td>
      <td>The number of requests allowed per time period</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">X-RateLimit-Remaining</code></td>
      <td>The approximate number of requests remaining within a window</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">X-RateLimit-Reset</code></td>
      <td>The number of seconds remaining before the current window resets</td>
    </tr>
  </tbody>
</table>

<p>Note that the <code class="language-plaintext highlighter-rouge">RateLimit-Limit</code>, <code class="language-plaintext highlighter-rouge">RateLimit-Remaining</code>, and <code class="language-plaintext highlighter-rouge">RateLimit-Reset</code> headers are not returned when you hit an HTTP <code class="language-plaintext highlighter-rouge">429</code> error. When the error occurs, those headers are replaced with an <code class="language-plaintext highlighter-rouge">X-RateLimit-Retry-After</code> header that returns an integer indicating the number of seconds before you can start making requests.</p>

<p>You can <a href="/docs/assets/api/openapi/users_track.yaml">download the OpenAPI document</a> and use it to validate schemas. To learn how, see <a href="/docs/api/openapi_schema_validation/">Use OpenAPI schemas for request validation</a>.</p>

</div>
