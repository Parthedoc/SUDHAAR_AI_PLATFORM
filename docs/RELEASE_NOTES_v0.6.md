# SUDHAAR v0.6 release notes

## Chat and knowledge
- Default chat focus is automatic intent selection. Short topical prompts such as “alcohol” are treated as requests for a general overview.
- A factual question is answered directly even if the user previously selected a listening-oriented mode. Explicit emotional-sharing language remains eligible for supportive listening.
- Weighted retrieval prioritises exact substance terms in titles/tags.
- Added source-linked starter entries for alcohol, tobacco/nicotine, cannabis, opioids and general psychoactive drugs.

## Interaction
- Full-width assistant answers and right-aligned user turns.
- The chat composer is pinned using Streamlit chat input.
- A chat-adjacent attachment panel supports PDF/DOCX/TXT/Markdown and audio file upload, plus microphone recording where supported.
- Optional local transcription uses faster-whisper; the user can review the transcript before sending.

## Limitations
- Local Ollama model quality depends on device resources and model capability.
- Knowledge-base entries are starter summaries, not a complete or clinically reviewed medical resource.
- Audio transcription requires the optional package and can download a speech model on first use.
- Source coverage and translation quality need ongoing validation by reliable sources and fluent speakers.
- No clinical efficacy or safety claim is made.
