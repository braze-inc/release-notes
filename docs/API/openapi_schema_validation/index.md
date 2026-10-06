# Use OpenAPI schemas for request validation

> This reference article explains what OpenAPI schemas are, how they work, and how to use them to confirm that your requests to Braze REST API endpoints are correctly structured before you send them.

Every Braze REST API endpoint page renders an interactive reference generated from an [OpenAPI](https://www.openapis.org/) specification. Each specification includes a *schema*: a precise, machine-readable description of the data an endpoint accepts and returns. You can use that schema to validate your requests, so you catch structural mistakes in your own tooling instead of discovering them from a failed API call.

For a broader overview of how Braze publishes these specifications and the other workflows they support, see [Using Braze OpenAPI specs](https://www.braze.com/docs/api/using_openapi_specs/).

## What an OpenAPI schema is

A schema is the contract for an endpoint's data. In an OpenAPI document, the [Schema Object](https://spec.openapis.org/oas/latest.html#schema-object) defines each field an endpoint uses, including the field's name, data type, whether it's required, its allowed values, and how nested objects and arrays are structured.

OpenAPI schemas are built on [JSON Schema](https://json-schema.org/), a widely adopted standard for describing the shape of JSON data. Because the contract is expressed in a standard, machine-readable format, you can validate a payload against it with off-the-shelf tools rather than checking fields by hand. To learn more about the concepts involved, see [Learn OpenAPI](https://learn.openapis.org/) and [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/).

## How schemas work

A schema describes data using a small set of building blocks. The most common ones are:

- **Type.** The data type of a value, such as `string`, `integer`, `number`, `boolean`, `array`, or `object`. See [Data types](https://swagger.io/docs/specification/data-models/data-types/) in the Swagger documentation.
- **Required fields.** A list of the properties that must be present for the data to be valid.
- **Constraints.** Rules that narrow what a value can be, such as an `enum` of allowed values, a `format` (for example, `date-time`), a string pattern, or minimum and maximum values.
- **Nested structure.** Objects can contain other objects, and arrays declare the schema of the items they hold, so a schema can describe deeply structured payloads.

A validator reads these rules and compares your data against them. If a required field is missing, a value has the wrong type, or a value falls outside its allowed set, the validator reports the specific problem. The [JSON Schema specification](https://json-schema.org/specification) defines this validation behavior in detail.

## How a schema defines a valid request

For endpoints that accept a request body, the specification's request body schema describes exactly what a valid payload looks like. Many Braze endpoints reuse the same request structures, such as user identifiers, messaging objects, and audience filters. For a field-by-field reference on those shared structures, see [Objects and filters](https://www.braze.com/docs/api/objects_filters/). Consider a simplified schema for a request that requires a string `external_id` and an integer `points`, where `points` cannot be negative:

```json
{
  "type": "object",
  "required": ["external_id", "points"],
  "properties": {
    "external_id": { "type": "string" },
    "points": { "type": "integer", "minimum": 0 }
  }
}
```

A payload that satisfies this schema is valid:

```json
{ "external_id": "user-123", "points": 50 }
```

Each of the following payloads is invalid, and a validator explains why:

- `{ "points": 50 }` omits the required `external_id` field.
- `{ "external_id": "user-123", "points": "50" }` sends `points` as a string instead of an integer.
- `{ "external_id": "user-123", "points": -5 }` sends a value that breaks the `minimum` constraint.

By reading the schema first, you know which fields to send, what type each value must be, and which values are allowed, before you make a single call.

## Validate a request against a schema

To validate a payload against an endpoint's schema:

1. Download the spec for the endpoint you want. Each spec is available at a stable, public URL in the format `https://www.braze.com/docs/assets/api/openapi/{spec_filename}.yaml`.
2. Extract the request body schema from the spec.
3. Validate your payload against that schema with a JSON Schema validator, such as [Ajv](https://ajv.js.org/) for JavaScript, or another library from the [JSON Schema tools](https://json-schema.org/tools) list for your language.
4. Fix any field the validator flags as missing, mistyped, or out of range, then send your request.

You can also lint and validate entire specifications with tools such as [Spectral](https://docs.stoplight.io/docs/spectral/), or generate typed request models with [OpenAPI Generator](https://openapi-generator.tech/) so your code produces valid payloads by construction. For step-by-step workflows that use these specs, see [How to use the schemas](https://www.braze.com/docs/api/using_openapi_specs/#how-to-use-the-schemas).

## Why schema validation matters

Validating requests against the schema helps you:

- **Catch errors earlier.** Find missing or mistyped fields in your own environment instead of from a rejected API call.
- **Reduce failed calls.** Send well-formed requests the first time, which lowers retries and troubleshooting.
- **Integrate with confidence.** Rely on a single, machine-readable contract rather than copying request shapes by hand.
- **Automate checks.** Add validation to your tests or CI pipeline so integrations stay correct as your code changes.

## Related resources

Braze documentation:

- [Using Braze OpenAPI specs](https://www.braze.com/docs/api/using_openapi_specs/)
- [API overview](https://www.braze.com/docs/api/basics/)
- [API endpoints](https://www.braze.com/docs/api/endpoints/)
- [Objects and filters](https://www.braze.com/docs/api/objects_filters/)
- [API errors and responses](https://www.braze.com/docs/api/errors/)
- [API rate limits](https://www.braze.com/docs/api/api_limits/)
- [Postman and sample requests](https://www.braze.com/docs/api/postman_collection/)

External references:

- [OpenAPI Initiative](https://www.openapis.org/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [JSON Schema](https://json-schema.org/)
- [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/)
