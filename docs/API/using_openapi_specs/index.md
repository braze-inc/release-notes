# Using Braze OpenAPI specs

> This reference article explains how Braze publishes OpenAPI specifications for its REST API endpoints and how you can use the schemas in those specs to speed up your development workflows.

Each Braze REST API endpoint page renders an interactive reference generated from an [OpenAPI](https://www.openapis.org/) specification. The reference shows the endpoint's parameters, request body, response schemas, and example responses in a consistent, structured format. Every spec is also a machine-readable file that you can download and use directly in your own tooling.

**Note:**


The reference on each endpoint page is read-only. It doesn't send live requests from the documentation site. To call an endpoint, copy the generated cURL example or use the downloaded spec in your own client, as described in [How to use the schemas](#how-to-use-the-schemas).



## Where to find a spec

On any REST API endpoint page, find the **Endpoint reference** section. To open the raw specification, use the spec download option in that section. Each file lives at a stable, public URL in the following format:

```
https://www.braze.com/docs/assets/api/openapi/{spec_filename}.yaml
```

Each file is a single, self-contained OpenAPI 3 document for one endpoint. The document includes the request and response schemas that describe the exact shape of the data the endpoint accepts and returns.

## Why the schemas are valuable

A schema is the structured contract for an endpoint: it defines each field's name, data type, whether the field is required, its allowed values, and how objects nest. Because this contract is machine-readable, you can rely on it instead of copying request and response shapes by hand. For the reusable objects and filters that many endpoints share, see [Objects and filters](https://www.braze.com/docs/api/objects_filters/). The schemas help you:

- **Generate client code and SDKs.** Produce typed request and response models, or a full client library, in your preferred language so you don't hand-write request bodies.
- **Validate requests and responses.** Check payloads against the schema before you send them and confirm responses match what you expect, which catches integration bugs early.
- **Mock the API.** Stand up a mock server from the spec so you can build and test against Braze endpoints before you write live integration code.
- **Import into API clients.** Load the spec into tools like Postman or Insomnia to get prefilled requests, parameter descriptions, and autocompletion.
- **Keep integrations in sync.** Compare a stored copy of a spec against the current version to detect when a field is added or changed, then update your integration with confidence.

## How to use the schemas

The following instructions assume you've downloaded a spec file from an endpoint page.

### View and explore a spec

To read a spec in a structured, interactive view, use any OpenAPI viewer:

1. Download the spec file for the endpoint you want.
2. Open [Swagger Editor](https://editor.swagger.io/) or a similar viewer.
3. Paste or upload the file to browse the operation, its parameters, and every schema it defines.

### Generate a client or models

To turn a schema into typed code in your language, use an OpenAPI generator:

1. Install a generator such as [OpenAPI Generator](https://openapi-generator.tech/).
2. Point the generator at the spec file and select your target language.
3. Use the generated request and response models, or the full client, in your application instead of building request bodies manually.

### Validate your payloads

To confirm a request body matches the endpoint's contract before you send it:

1. Extract the request body schema from the spec.
2. Use a JSON Schema validator, or a library in your language, to validate your payload against that schema.
3. Fix any fields the validator flags as missing, mistyped, or out of range.

### Import into Postman or another client

To get prefilled requests and inline field descriptions:

1. In Postman, select **Import**, then choose the downloaded spec file.
2. Postman creates a collection with the endpoint, its parameters, and example values.
3. Add your REST API key and target [REST endpoint](https://www.braze.com/docs/api/basics/#endpoints), then send your request.

### Mock the endpoint

To build against an endpoint before you write live integration code:

1. Load the spec into a mocking tool, such as [Prism](https://github.com/stoplightio/prism).
2. Start the mock server, which returns responses that match the spec's schemas.
3. Point your application at the mock server while you develop, then switch to your live [REST endpoint](https://www.braze.com/docs/api/basics/#endpoints) when you're ready.

## Related resources

- [Use OpenAPI schemas for request validation](https://www.braze.com/docs/api/openapi_schema_validation/)
- [API overview](https://www.braze.com/docs/api/basics/)
- [API endpoints](https://www.braze.com/docs/api/endpoints/)
- [Objects and filters](https://www.braze.com/docs/api/objects_filters/)
- [API errors and responses](https://www.braze.com/docs/api/errors/)
- [API rate limits](https://www.braze.com/docs/api/api_limits/)
- [Postman and sample requests](https://www.braze.com/docs/api/postman_collection/)
