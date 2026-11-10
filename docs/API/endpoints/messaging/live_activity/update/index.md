<div id='api_bydzkpmdxkap' class='api_div' data-search-keywords='update live activity'>
<h1 id="update-live-activity">Update Live Activity</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/messages/live_activity/update</p>
</div>

<blockquote>
  <p>Use this endpoint to update and end <a href="/docs/developer_guide/live_notifications/?sdktab=swift">Live Activities</a> displayed by your iOS app. This endpoint requires additional setup.</p>
</blockquote>

<p>After you register a Live Activity, you can pass a JSON payload to update your Apple Push Notification service (APNs). See Apple’s documentation on <a href="https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications">updating your Live Activity with push notification payloads</a> for more information.</p>

<p>If <code class="language-plaintext highlighter-rouge">content-available</code> isn’t set, the default Apple Push Notification service (APNs) priority is 10. If <code class="language-plaintext highlighter-rouge">content-available</code> is set, this priority is 5. Refer to <a href="/docs/api/objects_filters/messaging/apple_object">Apple push object</a> for more details.</p>

<p><strong>Important:</strong></p>

<p>If you start an activity remotely with <code class="language-plaintext highlighter-rouge">/messages/live_activity/start</code>, wait at least 5 minutes before you send the first <code class="language-plaintext highlighter-rouge">/messages/live_activity/update</code> request for that same <code class="language-plaintext highlighter-rouge">activity_id</code>. This delay gives Braze and APNs time to register the new Live Activity and its token mapping. If you send the first update too soon, that update may not apply to the activity.</p>

<p><a href="https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd">View in Postman</a></p>

<div class="api-reference light-mode" id="endpoint-reference">
  <div id="scalar-messaging_live_activity_update"></div>
</div>

<script>
  (function () {
    // Update the integrity hash whenever the pinned version changes.
    var scalarSrc = "https://cdn.jsdelivr.net/npm/@scalar/api-reference@1.76.2/dist/browser/standalone.js";
    var scalarIntegrity = "sha384-mCh2A/B6vkfhiHyzwBZm7lbFmEK5fE/96Kbtk+RH1zei1P/XEt0I2MCiG6WfZdor";
    var specUrl = "/docs/assets/api/openapi/messaging_live_activity_update.yaml";
    var baseUrl = "/docs";
    var mountSelector = "#" + "scalar-messaging_live_activity_update";

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

<p>You can <a href="/docs/assets/api/openapi/messaging_live_activity_update.yaml">download the OpenAPI document</a> and use it to validate schemas. To learn how, see <a href="/docs/api/openapi_schema_validation/">Use OpenAPI schemas for request validation</a>.</p>

</div>
