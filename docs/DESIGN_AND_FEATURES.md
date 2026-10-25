# SUDHAAR v0.7 — Design and interaction notes

## Product intent

SUDHAAR should feel like a calm, kind place to start a conversation—not a diagnostic screen, government form, or generic productivity dashboard. The app acknowledges a concern first, asks only for details that are necessary, avoids stigma, and gives the user control over whether they want to be heard, learn something, consider a next step, help a family member, or find a service.

The assistant is still an AI and should not imply human feelings, guarantee absolute confidentiality, or encourage a user to depend on it instead of trusted people or qualified care.

## Interaction decisions

- `nav_page` stores stable values such as `home`, `chat`, and `services`; display labels can change without changing the selected page.
- User preferences use stable Streamlit widget keys. Theme/language changes rerun Streamlit, but should preserve the active page and session messages.
- Chat text, transcript, upload contents and support plan are session-only. No database is configured.
- Chat modes alter the AI's response guidance rather than attempt to diagnose the user.
- Document and voice controls are visible in tabs near the composer. The file upload path extracts supported text locally and labels it as unverified. Audio can be transcribed locally, reviewed, or sent directly to the chat. Uploads are not added to the approved source library.
- Voice input is optional and local via faster-whisper. Voice output uses browser speech synthesis.
- CSS provides page/card entrance, hover, and scroll-timeline reveal animations where supported. `prefers-reduced-motion` disables animation for users who prefer reduced motion.
- The Streamlit Deploy toolbar is hidden for this local prototype.

## Theme decisions

Midnight and Pearl share the same CSS tokens: background, panel, input, text, body text, muted text, border, accent, soft accent and warning surface. Components use these tokens to keep light mode readable and prevent hard-coded white text on white backgrounds.

## Remaining limitations

- The design is implemented using Streamlit, so it has less control over the browser shell than a custom React/Next.js frontend. The app can hide the default Deploy toolbar, but Streamlit's underlying layout/runtime remains.
- Scroll reveal uses CSS `animation-timeline: view()` where supported; other browsers use entrance/hover animations.
- Local speech-to-text requires optional install and a first-time model download. Browser speech voices vary by computer/language pack.
- Interface translation coverage is partial and needs a fluent-speaker audit. The LLM may still mistranslate health and safety content.
- Knowledge base and service directory are a starter corpus and need a source-governance process and qualified review.
