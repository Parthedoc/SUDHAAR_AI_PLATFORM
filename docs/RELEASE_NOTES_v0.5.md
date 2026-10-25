# Release notes — SUDHAAR v0.5

## Critical fixes

1. **Chat avatar crash fixed.** The prior `st.chat_message(..., avatar="o")` value was interpreted as an image/file path by Streamlit, which produced `FileNotFoundError: No such file or directory: 'o'`. This version does not pass custom avatar glyphs, allowing Streamlit's built-in user/assistant avatars.
2. **Sidebar re-open control restored.** The prior CSS hid the entire Streamlit toolbar/header action container, which also hid the sidebar-expand control. This version hides only the Deploy button and main menu while retaining pointer events and visibility for expanded/collapsed sidebar controls.
3. **Light-theme controls improved.** Select menus, labels, text areas, and widget labels use theme-aware contrast.
4. **Navigation persistence retained.** Pages are represented by stable IDs in session state; appearance and language preferences use their own stable widget keys.

## Validation

- Python syntax compilation passed.
- Existing safety/retrieval tests passed.
- Added static regression tests ensure the invalid custom avatar parameter and header-hiding CSS do not return.
- A live browser test is still required on the user's Windows machine because Streamlit frontend state and local browser rendering cannot be fully reproduced in this build environment.
