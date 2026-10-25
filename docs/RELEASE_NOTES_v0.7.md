# SUDHAAR v0.7 — chat intent, voice and upload refinement

## What changed

- Direct factual intent now wins over a previously selected listening mode. A short topic such as “alcohol” is treated as a request for general knowledge, not as evidence that the user is distressed or personally uses the substance.
- One- or two-word topical prompts do not inherit the last emotional-support exchange as conversation history; this reduces the chance of a generic empathy-only answer.
- General health prompts explicitly request a direct definition, major effects/risks and support pathways when relevant. Responses should not include internal reasoning or self-talk.
- Source retrieval uses weighted matches, so topic-specific titles/tags rank ahead of incidental mentions.
- Upload and voice tools are visible in dedicated tabs directly above the composer rather than hidden inside a collapsed expander.
- Voice supports microphone recording or a user-uploaded audio file; users can review a transcript or ask SUDHAAR directly from the transcript.
- Chat responses use the full main content width; user prompts are right-aligned.
- Local-only Ollama remains the default; no cloud AI API key is required.

## Still prototype limitations

- This is not a medical service and has not been clinically validated.
- Voice transcription requires the optional `faster-whisper` package and local compute; voice/TTS language quality depends on the available model/Windows voices.
- Source summaries and service contact information need ongoing verification and clinical review.
- Audio/file processing and keyword safety routing need more extensive testing before a real-person pilot.
