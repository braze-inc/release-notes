# Manage multi-language scenarios

> Decisioning Studio Pro can choose among any number of language variants and still train one model across all of them. This guide covers how language fits that model, who owns translations, and three ways to store language-specific message content.

For how a decision becomes a message, see [Get started with Decisioning Studio Pro](https://www.braze.com/docs/user_guide/brazeai/decisioning_studio/get_started#message-activation-flow).

## How it works

A scenario can include as many languages as your team can produce and maintain, so each customer receives content in the right language.

Decisioning Studio trains one model across the full population. Language limits which variants a customer can receive, and the scenario stays one experiment. A pattern that performs well in one language, such as an offer or a send time, can inform the model for the scenario as a whole. A customer receives only the variants in their own language.

Your team develops and maintains the translations. Decisioning Studio selects among the variants you mark as eligible for a language.

## Prerequisites

Before you set up multi-language decisioning, confirm that:

- You have brand-approved translations for every language the scenario supports.
- Each customer profile has a reliable language attribute, or an equivalent signal, that Decisioning Studio can use to decide which language that customer is eligible for.

## Architectures for language variants

Three setups control which language variant a customer receives. Each one works with an API-triggered Canvas or with API-triggered campaigns. This is determined by where the language-specific content lives and how it is selected. For that send architecture, see [Choose an API-triggered campaign or Canvas](https://www.braze.com/docs/user_guide/example_library/decisioning_studio/api_triggered_campaign_or_canvas).

### Option 1: Every variant in one action bank

This is the most common setup. Add every message variant, in every language, to the action bank. Include a column for the language a customer must have to be eligible for that row. For example, only customers whose language is Spanish are eligible for the Spanish rows. Decisioning Studio uses that column as a guardrail and only chooses among the rows that match the customer's language.

This option fits teams that support up to three languages.

#### Benefits

- All content sits in one action bank, where Decisioning Studio can see it.
- Variants do not have to exist in every language, so message content can differ by language.
- The model can learn from elements that differ by language, such as subject line length or structure.

The action bank gets large as variants or languages grow, because each combination of variant and language is its own row. That is why this setup fits scenarios with three or fewer languages.

### Option 2: One action bank, with translations stored in Braze

The action bank lists variants in a single language. Decisioning Studio recommends from that list for every customer, including customers who speak another language. At send time, Braze reads the customer's language from their profile and loads the matching content from a language-specific source in Braze. Teams usually use a [catalog](https://www.braze.com/docs/user_guide/data/activation/catalogs). Some teams use [multi-language messages](https://www.braze.com/docs/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) instead. Either way, every variant in the action bank needs a matching entry in each language, using the same identifier. For catalogs, that identifier is the item `id`.

This option fits teams with three or more languages that want the translations to live in Braze.

#### Benefits

- The setup can grow to a large number of languages.
- Catalogs or multi-language messages give each team a place to work, separate from a shared action bank.
- Translations stay in Braze, so you can reuse them.

#### Considerations

- Every variant in the single-language action bank needs the same identifier in each language's catalog or locale. That takes coordination across teams.
- The model may learn less about patterns that exist in only one language, because recommendations come from the single-language action bank.

### Option 3: One action bank, with translations in your own tool

This works like option 2, except the language-specific content lives in a translation tool your team owns. Braze fills the message from that tool through an API, rather than from a catalog or multi-language message.

This option fits teams with three or more languages that already run a translation tool and want to connect it to Braze. Confirm that the tool can integrate with an API-triggered Canvas or campaign, and that it can handle your expected send volume. The benefits and tradeoffs in option 2 apply here as well.

## Best practices

- Keep variant coverage equivalent across languages. A gap in one language changes that population's experience, and what the model learns from it, even though one model is trained for the whole scenario.
- Check that translations still match before launch and after every content update. In options 2 and 3, a mismatched item `id` or API response sends the wrong content. Content that shares an identifier but says different things weakens what the model learns and hurts scenario performance.
- Confirm the language attribute. Decisioning Studio uses an attribute on the customer profile in Braze to choose which language a customer should receive. Check that the field is accurate and populated for the eligible audience.
- Choose the architecture for the languages you expect to add later. Changing the pattern after launch usually means rework for every team involved. Include those later languages in the initial design, even if you launch with a subset.

## Frequently asked questions

### Does Decisioning Studio train a separate model per language?

Decisioning Studio trains one model across the whole scenario. Language decides which variants a customer can receive, and the scenario stays one experiment.

### Who is responsible for translations?

Your team develops and maintains translations for all message content. Decisioning Studio selects among the variants you mark as eligible for each language, and your team owns translation quality.

### Can I mix architectures?

Use one architecture per scenario, including languages you might add later. Mixing architectures adds coordination work and makes it harder to tell whether every language is represented fairly in the action bank.

### What happens if a variant is missing in one language?

Decisioning Studio recommends only variants that are eligible for that customer's language. If a variant exists in one language and not another, customers in the language without it have a smaller set of actions, and performance is harder to compare across languages.

Depending on your setup, a missing catalog entry can also pull the content customers receive out of line with the action bank the model learns from. Keep variant sets equivalent across languages.
