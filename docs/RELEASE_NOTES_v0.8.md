# SUDHAAR v0.8 — Interface localization update

## What changed
- Added a centralized runtime UI-localization layer that translates app-authored labels and copy based on the sidebar's selected interface language.
- Covers common headings, page navigation, prompts, widgets, button labels, tooltips, chat controls, upload/voice labels and HTML card copy through curated phrase translations.
- Preserves selected-option internal values, page identifiers, URLs, user messages and long generated answers.
- Keeps original medical-source passages/citations intact where possible; these are source content, not UI chrome.
- Added automated tests for home heading, widget labels, HTML snippets and locale coverage.

## Important limitation
This is a broad phrase-based UI translation layer, not automatic translation of arbitrary content. Some less-common text and official source excerpts may remain in English or the source language. All translations must be reviewed by fluent speakers, especially for medical and crisis language, before a public pilot.
