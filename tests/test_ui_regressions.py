from pathlib import Path
import re
import unittest

APP = Path(__file__).resolve().parents[1] / "app.py"
SOURCE = APP.read_text(encoding="utf-8")

class UIRegressionTests(unittest.TestCase):
    def test_chat_messages_do_not_pass_custom_glyph_as_avatar_path(self):
        # In this Streamlit build, a plain character like "o" can be treated as an image path.
        self.assertNotRegex(SOURCE, r"st\.chat_message\([^\n]*avatar\s*=")
        self.assertIn('user-bubble-row-v6', SOURCE)
        self.assertIn('assistant-heading-v6', SOURCE)
        self.assertNotIn('st.chat_message(', SOURCE)
        self.assertIn('st.chat_input(', SOURCE)

    def test_css_does_not_hide_header_action_container(self):
        self.assertNotIn('[data-testid="stHeaderActionElements"], #MainMenu, footer{{display:none!important;}}', SOURCE)
        self.assertIn('[data-testid="stAppDeployButton"], #MainMenu, footer{{display:none!important;}}', SOURCE)

    def test_voice_and_document_tools_are_visible_in_chat_tabs(self):
        self.assertIn('st.tabs([\"📎  Attach documents\", \"🎙  Voice message\"])', SOURCE)
        self.assertIn('st.audio_input(', SOURCE)
        self.assertIn('Or upload a voice note', SOURCE)
        self.assertIn('Transcribe & ask SUDHAAR', SOURCE)

    def test_sidebar_controls_are_explicitly_kept_visible(self):
        self.assertIn('[data-testid="stSidebarCollapsedControl"]', SOURCE)
        self.assertIn('[data-testid="stSidebarCollapseButton"]', SOURCE)
        self.assertIn('pointer-events:auto!important', SOURCE)


    def test_language_change_preserves_page_independently_of_translated_radio(self):
        self.assertIn('"active_page"', SOURCE)
        self.assertIn('def preserve_active_page_on_language_change()', SOURCE)
        self.assertIn('on_change=preserve_active_page_on_language_change', SOURCE)
        self.assertIn('key="nav_radio_widget", on_change=sync_active_page_from_radio', SOURCE)
        self.assertIn('st.session_state["nav_radio_widget"] = active_page', SOURCE)

    def test_navigation_callbacks_update_canonical_page(self):
        self.assertIn('st.session_state["active_page"] = target', SOURCE)
        self.assertIn('st.session_state["active_page"] = "chat"', SOURCE)

if __name__ == "__main__":
    unittest.main()
