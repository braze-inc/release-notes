<div id='api_spbdyktldfea' class='api_div' data-search-keywords='duplicate canvases using the api'>
<h1 id="duplicate-canvases-using-the-api">Duplicate Canvases using the API</h1>
<div class="api_type"><div class="method post ">post</div>
<p>/canvas/duplicate</p>
<div class="coreclass core_endpoint "><a href="/docs/core_endpoints">core endpoint</a></div></div>

<blockquote>
  <p>Use this endpoint to duplicate Canvases. This API endpoint is similar to <a href="/docs/user_guide/messaging/governance/duplicating">duplicating Canvases in the Braze dashboard</a>.</p>
</blockquote>

<div class="openapi-explorer" data-spec-url="/docs/assets/api/openapi/messaging_duplicate_messages_post_duplicate_canvases.yaml">
  
    <h2 id="endpoint-reference">Endpoint reference</h2>
    <p>
      This reference is generated from the OpenAPI specification for this
      endpoint. To run the endpoint, copy the generated cURL example and send
      it from your terminal or Postman. You can also download the raw OpenAPI
      spec for this page at <a href="/docs/assets/api/openapi/messaging_duplicate_messages_post_duplicate_canvases.yaml">/docs/assets/api/openapi/messaging_duplicate_messages_post_duplicate_canvases.yaml</a>. Use this
      spec to validate that your requests include the correct parameters, fields,
      and structure before you send them. To learn how, see
      <a href="/docs/api/openapi_schema_validation/">Use OpenAPI schemas for request validation</a>.
    </p>
  
  <div id="swagger-ui-messaging_duplicate_messages_post_duplicate_canvases" class="openapi-explorer__ui"></div>
</div>
<link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui.css" crossorigin="anonymous" />

<style>
  .openapi-explorer {
    --braze-bg: #ffffff;
    --braze-bg-muted: #f8f4ff;
    --braze-surface: #f4f4f7;
    --braze-border: #dddde2;
    --braze-text: #212123;
    --braze-text-muted: #475467;
    --braze-link: #801ed7;
    --braze-accent: #801ed7;
    --braze-accent-strong: #300266;
    --braze-accent-soft: #c9c4ff;
    --braze-success: #169b72;
    --braze-warning: #c48d3c;
    --braze-danger: #c6132c;
    --braze-code-bg: #24173b;
    --braze-code-text: #ffffff;
    --braze-code-accent: #b9f7cb;
    margin: 1.5rem 0 2rem;
    color: var(--braze-text);
  }
  .openapi-explorer__ui {
    background: var(--braze-bg);
    border: 1px solid var(--braze-border);
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(48, 2, 102, 0.08);
    overflow: hidden;
  }
  .openapi-explorer .swagger-ui,
  .openapi-explorer .swagger-ui * {
    box-sizing: border-box;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
  }
  .openapi-explorer .swagger-ui {
    font-family: "Lato", "Helvetica Neue", Arial, sans-serif;
    letter-spacing: normal;
    line-height: 1.4;
  }
  .openapi-explorer--minimal {
    margin-top: 0.5rem;
  }
  .openapi-explorer .swagger-ui .topbar { display: none; }
  .openapi-explorer .swagger-ui .information-container {
    padding: 1.25rem 1.5rem;
    background: var(--braze-bg-muted);
    border-bottom: 1px solid var(--braze-border);
  }
  .openapi-explorer .swagger-ui .info .title {
    color: var(--braze-accent-strong);
    font-weight: 700;
  }
  .openapi-explorer .swagger-ui .info p,
  .openapi-explorer .swagger-ui .info li,
  .openapi-explorer .swagger-ui .info td,
  .openapi-explorer .swagger-ui .parameter__name,
  .openapi-explorer .swagger-ui .response-col_status,
  .openapi-explorer .swagger-ui .response-col_description,
  .openapi-explorer .swagger-ui .responses-inner h4,
  .openapi-explorer .swagger-ui .responses-inner h5 {
    color: var(--braze-text);
  }
  .openapi-explorer .swagger-ui .scheme-container {
    background: var(--braze-bg);
    box-shadow: none;
    border-bottom: 1px solid var(--braze-border);
    padding: 0.85rem 1.5rem;
  }
  .openapi-explorer .swagger-ui .scheme-container .schemes > label {
    color: var(--braze-text-muted);
  }
  .openapi-explorer .swagger-ui .scheme-container .schemes {
    display: none;
  }
  .openapi-explorer .swagger-ui .opblock-tag {
    border-bottom: 1px solid var(--braze-border);
    color: var(--braze-accent-strong);
    background: var(--braze-bg-muted);
    margin: 0;
    padding: 14px 20px;
  }
  .openapi-explorer .swagger-ui .opblock {
    border: 1px solid var(--braze-border);
    border-radius: 10px;
    box-shadow: none;
    margin: 0 0 16px;
    background: var(--braze-bg);
  }
  .openapi-explorer .swagger-ui .opblock .opblock-summary {
    border-bottom-color: var(--braze-border);
  }
  .openapi-explorer .swagger-ui .opblock.opblock-get {
    border-left: 4px solid #169b72;
  }
  .openapi-explorer .swagger-ui .opblock.opblock-post {
    border-left: 4px solid #801ed7;
  }
  .openapi-explorer .swagger-ui .opblock.opblock-put,
  .openapi-explorer .swagger-ui .opblock.opblock-patch {
    border-left: 4px solid #23a8b7;
  }
  .openapi-explorer .swagger-ui .opblock.opblock-delete {
    border-left: 4px solid #c6132c;
  }
  .openapi-explorer .swagger-ui .opblock-summary-method {
    border-radius: 999px;
    padding: 6px 12px;
    min-width: 72px;
    font-weight: 700;
  }
  .openapi-explorer .swagger-ui .btn,
  .openapi-explorer .swagger-ui select,
  .openapi-explorer .swagger-ui input[type="text"],
  .openapi-explorer .swagger-ui input[type="password"],
  .openapi-explorer .swagger-ui input[type="search"],
  .openapi-explorer .swagger-ui textarea {
    border-radius: 8px;
    border-color: var(--braze-border);
    color: var(--braze-text);
  }
  .openapi-explorer .swagger-ui .responses-table .response-col_status {
    font-weight: 700;
  }
  .openapi-explorer .swagger-ui table {
    width: 100% !important;
    border-collapse: collapse !important;
  }
  .openapi-explorer .swagger-ui table thead tr th,
  .openapi-explorer .swagger-ui table tbody tr td {
    text-align: left;
    vertical-align: middle;
    padding: 12px 10px !important;
  }
  .openapi-explorer .swagger-ui table th,
  .openapi-explorer .swagger-ui table td {
    padding: 12px 10px !important;
    /* Wrap only at word boundaries so words never split mid-character. */
    word-break: normal;
    overflow-wrap: break-word;
  }
  /* Keep inline code tokens (such as parameter names like segment_id) on a
     single line so they stay legible instead of breaking across two lines. */
  .openapi-explorer .swagger-ui table th code,
  .openapi-explorer .swagger-ui table td code {
    white-space: nowrap;
    word-break: normal;
    overflow-wrap: normal;
  }
  .openapi-explorer .swagger-ui .responses-table .response-col_status,
  .openapi-explorer .swagger-ui .responses-table .response-col_links,
  .openapi-explorer .swagger-ui .responses-table .response-col_description {
    text-align: left !important;
    vertical-align: middle !important;
  }
  .openapi-explorer .swagger-ui .responses-table .response-col_status {
    width: 11%;
    min-width: 72px;
  }
  .openapi-explorer .swagger-ui .responses-table .response-col_description {
    width: auto;
  }
  /* Remove the always-empty Links column from native response tables. */
  .openapi-explorer .swagger-ui .responses-table .response-col_links {
    display: none;
  }
  .openapi-explorer .swagger-ui .response-control-media-type__accept-message {
    color: var(--braze-text-muted);
  }
  .openapi-explorer .swagger-ui table thead tr th,
  .openapi-explorer .swagger-ui .parameter__type,
  .openapi-explorer .swagger-ui .parameter__deprecated,
  .openapi-explorer .swagger-ui .prop-format {
    color: var(--braze-text-muted);
  }
  .openapi-explorer .swagger-ui a {
    color: var(--braze-link);
  }
  .openapi-explorer .swagger-ui .highlight-code,
  .openapi-explorer .swagger-ui .microlight,
  .openapi-explorer .swagger-ui .curl,
  .openapi-explorer .swagger-ui .opblock-body pre {
    background: var(--braze-code-bg);
    border-radius: 8px;
    color: var(--braze-code-text);
  }
  .openapi-explorer .swagger-ui .opblock-body pre code,
  .openapi-explorer .swagger-ui .microlight code,
  .openapi-explorer .swagger-ui .hljs {
    color: var(--braze-code-text) !important;
    background: transparent !important;
    text-shadow: none !important;
  }
  .openapi-explorer .swagger-ui .hljs-string,
  .openapi-explorer .swagger-ui .hljs-attr,
  .openapi-explorer .swagger-ui .hljs-number,
  .openapi-explorer .swagger-ui .hljs-literal {
    color: var(--braze-code-accent) !important;
  }
  .openapi-explorer .swagger-ui .hljs * {
    background: transparent !important;
  }
  .openapi-explorer .swagger-ui ::selection {
    background: rgba(128, 30, 215, 0.35);
    color: var(--braze-code-text);
  }
  .openapi-explorer .swagger-ui .tab li button.tablinks {
    color: var(--braze-text-muted);
  }
  .openapi-explorer .swagger-ui .tab li.active button.tablinks {
    color: var(--braze-accent-strong);
    font-weight: 700;
  }
  .openapi-explorer .swagger-ui .model-box,
  .openapi-explorer .swagger-ui section.models,
  .openapi-explorer .swagger-ui .model-container {
    background: var(--braze-surface);
    border-color: var(--braze-border);
  }
  @media (prefers-color-scheme: dark) {
    .openapi-explorer {
      --braze-bg: #17101f;
      --braze-bg-muted: #211430;
      --braze-surface: #261938;
      --braze-border: #473458;
      --braze-text: #f6f2ff;
      --braze-text-muted: #c9bddb;
      --braze-link: #c9c4ff;
      --braze-accent: #c9c4ff;
      --braze-accent-strong: #ffffff;
      --braze-accent-soft: #7d62a2;
      --braze-code-bg: #0e0a16;
      --braze-code-text: #ffffff;
      --braze-code-accent: #b9f7cb;
      box-shadow: none;
    }
  }
  html[data-theme="dark"] .openapi-explorer,
  body.dark .openapi-explorer,
  body.dark-mode .openapi-explorer {
    --braze-bg: #17101f;
    --braze-bg-muted: #211430;
    --braze-surface: #261938;
    --braze-border: #473458;
    --braze-text: #f6f2ff;
    --braze-text-muted: #c9bddb;
    --braze-link: #c9c4ff;
    --braze-accent: #c9c4ff;
    --braze-accent-strong: #ffffff;
    --braze-accent-soft: #7d62a2;
    --braze-code-bg: #0e0a16;
    --braze-code-text: #ffffff;
    --braze-code-accent: #b9f7cb;
  }
  /* Copy-to-clipboard button injected on each example code block. The extra
     top padding reserves a gutter so the button never overlaps the code. */
  .openapi-explorer .opblock-description-wrapper pre,
  .openapi-explorer .renderedMarkdown pre {
    position: relative;
    padding-top: 2.75em;
  }
  .openapi-explorer .openapi-copy-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    z-index: 2;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 700;
    line-height: 1.4;
    color: var(--braze-code-text);
    background: rgba(128, 30, 215, 0.9);
    border: 1px solid var(--braze-accent-soft);
    border-radius: 6px;
    cursor: pointer;
  }
  .openapi-explorer .openapi-copy-btn:hover {
    background: var(--braze-accent);
  }
  .openapi-explorer .openapi-copy-btn:focus-visible {
    outline: 2px solid var(--braze-accent-soft);
    outline-offset: 2px;
  }
  .openapi-explorer .openapi-copy-btn[data-copied="true"] {
    background: var(--braze-success);
  }
  /* Response status codes table: equal-width columns so the Meaning and
     resolution columns get enough room and the table reads evenly. */
  .openapi-explorer table.openapi-response-table {
    table-layout: fixed;
    width: 100%;
  }
  .openapi-explorer table.openapi-response-table th,
  .openapi-explorer table.openapi-response-table td {
    width: 25%;
    vertical-align: top;
    word-break: normal;
    overflow-wrap: break-word;
  }
  /* Allow long inline code tokens (such as the Authorization header) to wrap
     inside the equal-width response cells instead of overflowing them. Short
     tokens still stay on one line because they fit without breaking. */
  .openapi-explorer table.openapi-response-table th code,
  .openapi-explorer table.openapi-response-table td code {
    white-space: normal;
    overflow-wrap: break-word;
  }
</style>

<script>
  (function () {
    var specPath = "/docs/assets/api/openapi/messaging_duplicate_messages_post_duplicate_canvases.yaml";
    var specUrl = specPath;
    try {
      specUrl = new URL(specPath, window.location.origin).toString();
    } catch (error) {
      specUrl = specPath;
    }
    var baseUrl = "/docs";
    var domId = "#" + "swagger-ui-messaging_duplicate_messages_post_duplicate_canvases";
    var uiInstance = null;
    var specBasename = specPath.split("/").pop();

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

    // Track clicks on the reference links (Postman, spec download, and the
    // schema-validation guide). Bind once per page even with several explorers.
    if (!window.__openapiTrackingBound) {
      window.__openapiTrackingBound = true;
      document.addEventListener("click", function (evt) {
        var link = evt.target && evt.target.closest ? evt.target.closest("a") : null;
        if (!link) { return; }
        var href = link.getAttribute("href") || "";
        var page = window.location.pathname;
        if (link.classList.contains("seeme")) {
          var isSwagger = !!link.closest(".api_reference.swagger");
          brazeLog(isSwagger ? "docs_api_swagger_click" : "docs_api_postman_click", { href: href, page: page });
        } else if (href.indexOf("/assets/api/openapi/") !== -1) {
          brazeLog("docs_api_spec_download_click", { spec_url: href, page: page });
        } else if (href.indexOf("/api/openapi_schema_validation") !== -1) {
          brazeLog("docs_api_validation_guide_click", { page: page });
        }
      }, true);
    }

    // Classify a code block by the nearest preceding heading so copy events can
    // be segmented into request vs. response engagement.
    function blockTypeFor(pre) {
      var node = pre.previousElementSibling;
      while (node) {
        if (/^H[1-6]$/.test(node.tagName)) {
          var text = (node.textContent || "").toLowerCase();
          if (text.indexOf("response") !== -1) { return "response"; }
          if (text.indexOf("request") !== -1 || text.indexOf("example") !== -1) { return "request"; }
          return "other";
        }
        node = node.previousElementSibling;
      }
      return "other";
    }

    function addCopyButtons(root) {
      var blocks = root.querySelectorAll(".opblock-description-wrapper pre, .renderedMarkdown pre");
      Array.prototype.forEach.call(blocks, function (pre) {
        if (pre.querySelector(".openapi-copy-btn")) { return; }
        var blockType = blockTypeFor(pre);
        var button = document.createElement("button");
        button.type = "button";
        button.className = "openapi-copy-btn";
        button.textContent = "Copy";
        button.setAttribute("aria-label", "Copy code to clipboard");
        button.addEventListener("click", function () {
          var code = pre.querySelector("code");
          var text = (code ? code.innerText : pre.innerText) || "";
          text = text.replace(/\s*Copy\s*$/, "");
          function finish() {
            button.textContent = "Copied";
            button.setAttribute("data-copied", "true");
            setTimeout(function () {
              button.textContent = "Copy";
              button.removeAttribute("data-copied");
            }, 2000);
            brazeLog("docs_api_copy_code_click", { block_type: blockType, spec: specBasename, page: window.location.pathname });
          }
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(finish, finish);
          } else {
            finish();
          }
        });
        pre.appendChild(button);
      });
    }

    // Whether the authored description already renders a Markdown table whose
    // header matches the given pattern (for example, a parameters table).
    function descriptionHasTableMatching(root, regex) {
      var tables = root.querySelectorAll(".opblock-description-wrapper table");
      for (var i = 0; i < tables.length; i += 1) {
        var headers = tables[i].querySelectorAll("th");
        for (var j = 0; j < headers.length; j += 1) {
          if (regex.test(headers[j].textContent || "")) { return true; }
        }
      }
      return false;
    }

    // Native responses are "rich" when they document more than one status code
    // or include an example/model, meaning the spec relies on native rendering.
    function nativeResponsesAreRich(root) {
      if (root.querySelectorAll(".responses-inner tr.response").length > 1) { return true; }
      return !!root.querySelector(
        ".responses-inner .highlight-code, .responses-inner .microlight, .responses-inner .model-example, .responses-inner .model-box"
      );
    }

    function hideParameters(root) {
      Array.prototype.forEach.call(root.querySelectorAll(".parameters-container"), function (el) {
        var section = el.closest(".opblock-section");
        if (section) { section.style.display = "none"; }
      });
      Array.prototype.forEach.call(root.querySelectorAll(".opblock-section-header"), function (header) {
        if ((header.textContent || "").trim().toLowerCase() === "parameters") {
          var section = header.closest(".opblock-section");
          if (section) { section.style.display = "none"; }
        }
      });
    }

    // Remove duplicate native sections only when the authored Markdown already
    // covers them, so specs that render fully from the OpenAPI structure (rich
    // native parameters/responses without Markdown tables) are left untouched.
    function hideNativeSections(root) {
      if (descriptionHasTableMatching(root, /parameter/i)) {
        hideParameters(root);
      }
      // Hide native responses when an authored responses/errors table exists, or
      // when the native section is just a thin single-status placeholder (which
      // also removes the always-empty Links column).
      var hasResponseTable = descriptionHasTableMatching(root, /status|error/i);
      if (hasResponseTable || !nativeResponsesAreRich(root)) {
        Array.prototype.forEach.call(root.querySelectorAll(".responses-wrapper"), function (el) {
          el.style.display = "none";
        });
      }
    }

    // Tag the authored "Response status codes" table so its columns render at
    // equal width (keeps the Meaning column from being squeezed).
    function styleResponseTables(root) {
      var tables = root.querySelectorAll(".opblock-description-wrapper table, .renderedMarkdown table");
      Array.prototype.forEach.call(tables, function (table) {
        var firstHeader = table.querySelector("th");
        if (firstHeader && /status code/i.test(firstHeader.textContent || "")) {
          table.classList.add("openapi-response-table");
        }
      });
    }

    function enhanceExplorer() {
      var root = document.querySelector(domId);
      if (!root) { return; }
      hideNativeSections(root);
      addCopyButtons(root);
      styleResponseTables(root);
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

    function isYamlSpec(url) {
      return /\.ya?ml(?:$|[?#])/.test(url);
    }

    async function resolveSpecUrl() {
      if (!isYamlSpec(specUrl)) { return specUrl; }
      return specUrl;
    }

    // Load js-yaml on demand so the spec can be parsed here rather than by
    // Swagger UI. Shared across every explorer on the page, and resolves to
    // null if the CDN is unavailable so rendering still falls back to the URL.
    function loadJsYaml() {
      if (window.jsyaml && typeof window.jsyaml.load === "function") {
        return Promise.resolve(window.jsyaml);
      }
      if (!window.__openapiJsYamlPromise) {
        window.__openapiJsYamlPromise = new Promise(function (resolve) {
          var script = document.getElementById("openapi-explorer-jsyaml");
          if (!script) {
            script = document.createElement("script");
            script.id = "openapi-explorer-jsyaml";
            script.src = "https://unpkg.com/js-yaml@4.1.0/dist/js-yaml.min.js";
            script.crossOrigin = "anonymous";
            document.body.appendChild(script);
          }
          script.addEventListener("load", function () { resolve(window.jsyaml || null); });
          script.addEventListener("error", function () { resolve(null); });
        });
      }
      return window.__openapiJsYamlPromise;
    }

    async function loadResolvedYamlSpec() {
      if (!isYamlSpec(specUrl)) { return null; }

      var yaml = await loadJsYaml();
      if (!yaml || typeof yaml.load !== "function") {
        return null;
      }

      var response = await fetch(specUrl, { credentials: "same-origin" });
      if (!response.ok) { return null; }

      var rawYaml = await response.text();
      // Liquid is disabled for these YAML assets, so resolve the /docs
      // token here. Idempotent: specs that already use absolute URLs are untouched.
      var withBaseUrl = rawYaml.replace(/\{\{\s*site\.baseurl\s*\}\}/g, baseUrl);
      var sanitizedYaml = sanitizeYamlBlockScalars(withBaseUrl);

      try {
        return yaml.load(sanitizedYaml);
      } catch (error) {
        return null;
      }
    }

    async function renderSwaggerUI() {
      if (!window.SwaggerUIBundle) { return false; }

      var resolvedSpecUrl = specUrl;
      var resolvedSpecObject = null;
      try {
        resolvedSpecUrl = await resolveSpecUrl();
        resolvedSpecObject = await loadResolvedYamlSpec();
      } catch (error) {
        resolvedSpecUrl = specUrl;
        resolvedSpecObject = null;
      }

      var swaggerConfig = {
        dom_id: domId,
        deepLinking: false,
        // Expand each operation (parameters, request body, and responses) by
        // default so the full endpoint reference is visible on page load
        // without an extra click.
        docExpansion: "full",
        defaultModelsExpandDepth: 0,
        // Read-only reference: never expose the interactive "Try it out"
        // control and never allow the UI to submit a live request.
        tryItOutEnabled: false,
        supportedSubmitMethods: [],
        syntaxHighlight: { activate: true },
        // After Swagger finishes rendering, hide the duplicate native sections
        // and inject tracked copy buttons. Re-run shortly after to catch any
        // asynchronous sub-renders.
        onComplete: function () {
          enhanceExplorer();
          setTimeout(enhanceExplorer, 200);
          setTimeout(enhanceExplorer, 800);
        },
        presets: [
          window.SwaggerUIBundle.presets.apis,
          window.SwaggerUIStandalonePreset
        ],
        plugins: [window.SwaggerUIBundle.plugins.DownloadUrl],
        layout: "BaseLayout"
      };

      if (resolvedSpecObject) {
        swaggerConfig.spec = resolvedSpecObject;
      } else {
        swaggerConfig.url = resolvedSpecUrl;
      }

      uiInstance = window.SwaggerUIBundle(swaggerConfig);

      return true;
    }

    if (window.SwaggerUIBundle) {
      renderSwaggerUI();
      return;
    }

    if (!document.getElementById("openapi-explorer-bundle")) {
      var bundleScript = document.createElement("script");
      bundleScript.id = "openapi-explorer-bundle";
      bundleScript.src = "https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui-bundle.js";
      bundleScript.crossOrigin = "anonymous";

      var presetScript = document.createElement("script");
      presetScript.id = "openapi-explorer-preset";
      presetScript.src = "https://unpkg.com/swagger-ui-dist@5.17.14/swagger-ui-standalone-preset.js";
      presetScript.crossOrigin = "anonymous";

      var loaded = 0;
      function maybeRender() {
        loaded += 1;
        if (loaded === 2) {
          renderSwaggerUI();
        }
      }
      bundleScript.addEventListener("load", maybeRender);
      presetScript.addEventListener("load", maybeRender);

      document.body.appendChild(bundleScript);
      document.body.appendChild(presetScript);
    } else {
      var existing = document.getElementById("openapi-explorer-bundle");
      if (window.SwaggerUIBundle) {
        renderSwaggerUI();
      } else {
        existing.addEventListener("load", function () {
          renderSwaggerUI();
        });
      }
    }
  })();
</script>

</div>
