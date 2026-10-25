# SUDHAAR v0.9 — Multilingual interface localization + navigation persistence

**SUDHAAR** = Substance Use De-addiction, Help, Awareness and Recovery.

A local-first, Windows-friendly hackathon prototype for warm, nonjudgmental substance-use education and recovery support. It uses a locally running Ollama model; no paid AI API is required.

## What's new in v0.9

- Fixed a navigation regression where changing the interface language could reset the selected page to Home. The current page is stored independently as a stable page ID and re-synchronised after locale changes.
- Added regression tests for language-change page preservation and navigation callbacks.

## What's new in v0.8

- Interface localization translates app-authored page text, navigation, widget labels, buttons, prompts, tabs, placeholders, notices and common HTML card copy based on the selected interface language. A locale-column alignment bug was corrected so Punjabi, Urdu, Odia and Assamese phrases are mapped to their intended language.
- Underlying widget values and stable page IDs remain unchanged.
- User messages, generated AI answers, URLs, code and source-card passages are preserved rather than blindly translated. Medical-source excerpts may remain in their original source language.
- Translations are hand-curated starter translations and require fluent-speaker review, particularly for medical and crisis wording.

## What's new in v0.7

- Direct factual questions always receive a direct health-education mode, even if a listening mode was previously selected; a topic such as “alcohol” should not be answered only with generic empathy.
- Added WHO-linked starter topics for alcohol, tobacco/nicotine, cannabis, opioids and general psychoactive drugs.
- Weighted search ranks substance-specific titles and tags above incidental matches.
- Chat now uses a wider, conversation-first layout with right-aligned user turns and full-width assistant answers.
- Document and voice controls are visible in dedicated tabs beside the chat composer. Voice recordings and uploaded clips can be transcribed locally, then reviewed or sent directly to SUDHAAR.
- Fixed chat rendering crash, restored sidebar reopen controls, improved light-theme contrast, and added regression tests.

## Core features retained from earlier versions

- Premium Midnight and high-contrast Pearl themes. Main interface, cards, text inputs, chat bubbles, alerts and sidebar use theme-aware CSS variables.
- Hides the Streamlit Deploy/top-toolbar clutter for the local demo.
- Keeps navigation on a stable page ID, so changing a language/theme setting should not throw the user back to Home. Chat history and draft text stay in the active Streamlit session.
- A warmer support companion experience with modes for listening, health information, recovery next steps, family support and service discovery.
- Optional document attachment: text-based PDF, DOCX, TXT and Markdown are extracted locally. The text is treated as unverified user-provided context, not as medical evidence.
- Browser-based read-aloud buttons using built-in speech synthesis; the user can start/stop reading a response.
- Optional local speech-to-text via faster-whisper, using Streamlit's microphone recorder. The first use downloads a multilingual speech model to the computer.
- The app-authored interface has a curated phrase-based translation layer across 13 interface-language choices. Navigation, common page copy, controls, prompts, forms, voice/upload labels and notices translate; original source excerpts and official service names are preserved where needed. Some less-common strings may still fall back to English, and the translations require fluent-speaker review. AI reply language remains a separate preference.
- Expanded source-linked library and government-programme/service directory.
- Session-only support plan and feedback UI; no application database or account system.
- Troubleshooting information for local Ollama status and model errors.

## Windows installation

### 1. Install Ollama and download the model

Install Ollama from https://ollama.com/download/windows, then in PowerShell:

```powershell
ollama pull qwen2.5:3b
ollama list
```

Keep the Ollama Windows app/service running while using SUDHAAR. Test the model once with:

```powershell
ollama run qwen2.5:3b "Reply with exactly: SUDHAAR works"
```

Exit interactive mode with `/bye`. You don't need to keep the interactive `ollama run` chat open; the Ollama background service serves app requests.

### 2. Extract and open SUDHAAR v0.9

Extract this ZIP to a new folder, for example `C:\Users\YOURNAME\Desktop\SUDHAAR_MVP_v9`. Do not overwrite the old working project yet. Open the new folder in VS Code. The folder you open must contain `app.py` and `requirements.txt` directly.

### 3. Set up Python

Run these commands in the VS Code PowerShell terminal, one line at a time:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

If `.venv` already exists in this new folder, skip the first command. If PowerShell activation fails, run the environment's Python directly instead:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

### 4. Configure the local model

Open `.env` in Notepad/VS Code. It should contain:

```dotenv
OLLAMA_BASE_URL=http://127.0.0.1:11434
OLLAMA_MODEL=qwen2.5:3b
SUDHAAR_WHISPER_MODEL=base
```

No OpenAI API key is needed. Ensure `OLLAMA_MODEL` matches a name shown by `ollama list`. Restart Streamlit after changing `.env`.

### 5. Run the app

```powershell
streamlit run app.py
```

Open http://localhost:8501 if the browser doesn't open automatically.

## Voice features

### Read an answer aloud

Each assistant answer includes **Listen to response** and **Stop** buttons. This uses the browser's built-in speech synthesis. The set of voices depends on voices/language packs installed in Windows and Chrome/Edge; not every language has an installed voice.

### Speak a message to SUDHAAR (optional local transcription)

The chat includes a visible Voice message tab with a microphone recorder and voice-file upload control. To transcribe locally, install the optional speech package into the project's active virtual environment:

```powershell
pip install faster-whisper
```

The first use downloads a multilingual model (`base`, roughly 150 MB class; exact size varies by package/version) and can take time. It transcribes on the local PC, then fills the message box so you can review and edit before sending. If installation fails or the PC is slow, typing remains available. No cloud speech API is configured by this app.

## Document upload

Chat supports `.pdf`, `.docx`, `.txt`, `.md` attachments (maximum 8 MB per file). Text extraction happens locally. Scanned-image PDFs are not OCR'd in this version. Extracted text is included only with the next message and passed to the local Ollama model. Uploaded documents are unverified and must not be treated as medical evidence. Avoid uploading identifiable health records. Attachments are cleared from the next chat-compose run after a message is sent.

## Privacy and medical limitations

- The app does not create user accounts or write chat history to an application database. Conversation is held in the current Streamlit session; stopping/restarting the app or refreshing a disconnected session may clear it.
- Ollama runs locally at `127.0.0.1:11434`. No cloud AI API key or paid inference service is configured.
- If browser speech synthesis is used, speech is handled by the browser/OS; installed voice behaviour can vary.
- Safety keyword routing is a limited prototype rule set. It can miss urgent situations and can incorrectly flag ordinary text; it is not a reliable risk detector.
- SUDHAAR must not diagnose, prescribe, provide an individual detox schedule, or replace clinicians/counsellors. In India, the app lists 112 for emergencies, 14416 for Tele-MANAS, 14446 for de-addiction support, and 1933 for narcotics-related reporting. Verify all service details before public deployment.
- Do not use the prototype as a clinical service. Obtain qualified clinical and privacy review before any real-person pilot.

## Evaluation

Run the lightweight tests:

```powershell
python -m unittest discover -s tests -v
```

The tests cover a few preselected keyword safety cases and retrieval checks only. Passing them does not prove clinical safety or effectiveness.

## Voice input requirements

Voice transcription is optional. After setup, run `.\.venv\Scripts\python.exe -m pip install -r requirements-voice.txt` from PowerShell to install the offline transcriber. The first use can download model files and may be slow on CPU.

## Project structure

```text
SUDHAAR_MVP_v9/
├── app.py
├── requirements.txt
├── requirements-voice.txt  # optional offline voice transcription
├── .env.example
├── .gitignore
├── README.md
├── docs/
│   ├── DESIGN_AND_FEATURES.md
│   └── EVALUATION_PLAN.md
├── sudhaar/
│   ├── ai_engine.py
│   ├── i18n.py
│   ├── safety.py
│   └── data/
│       ├── knowledge_base.json
│       └── resources.json
└── tests/
    ├── test_chat_experience.py
    ├── test_safety.py
    └── test_ui_regressions.py
```


## v0.7 chat experience improvements

- Factual and topic-only prompts (such as `alcohol` or `what are alcohol's health risks?`) are routed to direct educational answers rather than a generic empathy template.
- Weighted retrieval gives substance-specific titles/tags more importance than incidental overlap with general words such as “health”.
- Starter knowledge now includes WHO-linked summaries for alcohol, tobacco/nicotine, cannabis, opioids and general substance-use information. These are prototype summaries, not a clinically reviewed medical reference.
- Chat messages use a wider, conversation-first layout; an attachment panel offers document upload, microphone recording and audio-file upload. Voice transcription is local and requires the optional `faster-whisper` package.
- Uploaded/transcribed content is treated as unverified context. Confirm all sources and safety wording with qualified professionals before any real-user pilot.


## Chat behaviour

The default conversation focus is automatic: factual prompts such as `alcohol`, `what is alcohol`, or `alcohol health risks` receive a direct educational overview. Users can still select a listening/recovery/family/services mode when that is what they need. If the curated source library has no match, the model may give a cautious general educational answer but must not present it as source-verified or invent citations.


## v0.8 interface localization notes

Select the interface language in the sidebar. On the next Streamlit rerun, interface text is translated from a curated phrase table, while internal values remain stable for application logic. AI response language is a separate preference. Original citations and source excerpts are kept faithful to the source. This is not yet a certified translation and should not be used as a substitute for professionally translated medical or crisis information.


## v0.8 interface localization

The sidebar selector now controls the language of app-authored interface copy. The localization layer translates stable labels and known phrases without changing values used by the program. The separate AI reply-language selector controls the response language. Original medical source passages and proper names may remain in the source language to preserve traceability. This is a broad starter localization, not a certified translation: some long-tail phrases may remain English and medical/crisis wording must be reviewed by fluent speakers before public deployment.
