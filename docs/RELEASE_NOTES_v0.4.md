# Release notes — SUDHAAR v0.4

## Added
- New companion-first home page with non-judgmental language and three clear entry paths.
- Stable page-ID navigation to prevent settings/language reruns from resetting the active page.
- Midnight and Pearl theme variables for contrast-aware light/dark rendering.
- CSS hover and entrance animations plus scroll-timeline reveals where supported; reduced-motion preference respected.
- CSS rules to hide Streamlit's Deploy toolbar on the local prototype.
- Chat modes: listen, health information, recovery next step, family support, and service discovery.
- Browser speech playback for assistant responses.
- Optional local microphone transcription using faster-whisper.
- PDF, DOCX, TXT and Markdown upload/extraction with per-file size and context limits.
- More useful troubleshooting diagnostics for Ollama status and generation failures.
- Windows setup and run batch files to avoid manual venv activation and PowerShell execution-policy friction.

## Changed
- Default model is `qwen2.5:3b` to match the user's current local install.
- Prompts favour concise, empathetic responses and explicitly prohibit diagnosis, prescriptions, individual detox plans, or unsupported health claims.
- Uploaded documents are treated as unverified user context, not as trusted medical sources.

## Limitations
- The UI uses Streamlit, not a custom React frontend; advanced animation and shell styling are bounded by Streamlit's layout/runtime.
- Voice transcription is optional and downloads a local speech-recognition model on first use.
- Read-aloud availability depends on browser/OS speech voices.
- Medical and crisis wording in all languages requires fluent-speaker and clinical review.
- The app is a hackathon prototype, not a clinically validated service.
