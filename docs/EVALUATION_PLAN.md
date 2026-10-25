# SUDHAAR evaluation plan — v0.7

This is an engineering/usability evaluation, not a clinical validation study.

## Functional smoke tests

- Change interface language while on Chat, Library, Support and Preferences; confirm page selection remains stable.
- Change Midnight/Pearl appearance; confirm all text and widget values retain adequate contrast, and page/session remains.
- Ask a normal educational question; confirm a response and relevant source list display.
- Ask an out-of-scope medical question; confirm the assistant states limits rather than inventing specifics.
- Ask about immediate danger/self-harm using reviewed synthetic test text; confirm the separate safety route appears. Record false positives/negatives.
- Upload TXT, DOCX and text-based PDF; confirm excerpts are passed only with that user message and uploads rotate to a fresh uploader key after send.
- Record a short audio note with faster-whisper installed; verify local transcription, review-before-send, and direct transcribe-and-ask flows.
- Click Listen / Stop on a response; confirm browser/OS voice availability and stop behaviour.
- Test keyboard navigation and reduced-motion preference. Test a narrow/mobile viewport if time permits.

## AI quality checks

Build a manually reviewed set of questions across the first supported languages. For each, record retrieved source relevance, factual claims, source citations, tone, language naturalness, ambiguity, and safety handling. Ask a qualified professional to review any clinical scenarios before real-world use.

Suggested early engineering targets (not clinical cutoffs):
- At least 80% of labelled questions retrieve a relevant passage.
- At least 90% of factual claims in a small reviewed test set are supported by a cited passage.
- All predefined critical scenarios trigger the intended message in the test set; still report the limits of phrase-based detection.
- No API keys or personal health data in the Git repository.

## Privacy checks

- No chat history in a database or log file by default.
- Uploaded document text, transcripts and support plans are not persisted by application code.
- Confirm no user-provided document is added to the approved knowledge base.
- Verify no cloud API is called for AI generation; the target endpoint is the local Ollama service.
- Review all provider/browser behaviour before calling the app fully private; this prototype is not formally audited.
