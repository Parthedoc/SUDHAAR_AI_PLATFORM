# SUDHAAR v0.9 — Navigation persistence fix

## Fixed
- The selected page now lives in canonical session state (`active_page`) independent of the translated navigation widget.
- Changing the interface language captures the current page before Streamlit reruns.
- The radio widget is re-synchronised from the stable page ID before it is rendered, preventing locale changes from resetting the app to Home.
- Navigation changes and the New Chat action update the canonical and widget state together.

## Validation
- Python source compiled successfully.
- All 30 automated tests passed, including new navigation-preservation regression checks.

## Notes
This fixes the navigation state logic in code. As with any Streamlit app, verify language switching on the target Windows/browser setup.
