import unittest
from sudhaar.ui_localization import translate_text

class UILocalizationTests(unittest.TestCase):
    def test_home_heading_translates_for_core_locales(self):
        self.assertEqual(translate_text("Ask anything. Start anywhere.", "hi"), "कुछ भी पूछें। यहीं से शुरुआत करें।")
        self.assertNotEqual(translate_text("Ask anything. Start anywhere.", "bn"), "Ask anything. Start anywhere.")
        self.assertNotEqual(translate_text("Ask anything. Start anywhere.", "ta"), "Ask anything. Start anywhere.")

    def test_widget_label_translates(self):
        self.assertEqual(translate_text("Interface language / इंटरफ़ेस भाषा", "hi"), "इंटरफ़ेस भाषा")
        self.assertNotEqual(translate_text("Health Library", "mr"), "Health Library")

    def test_html_fragment_translation(self):
        html = '<div><h1>Ask anything. Start anywhere.</h1><p>What would feel helpful right now?</p></div>'
        translated = translate_text(html, "hi")
        self.assertIn("कुछ भी पूछें", translated)
        self.assertIn("इस समय आपको किस तरह की मदद उपयोगी लगेगी?", translated)

    def test_user_content_is_not_implicitly_translated_by_exact_function(self):
        answer = "Alcohol is a psychoactive substance and can affect many parts of the body."
        self.assertEqual(translate_text(answer, "hi", fragments=False), answer)


    def test_streamlit_wrapper_translates_display_without_changing_option_values(self):
        import sys
        from types import SimpleNamespace
        from unittest.mock import patch
        from sudhaar.ui_localization import install_streamlit_localization

        rendered = []
        fake = SimpleNamespace(
            session_state={"ui_language_label": "हिन्दी (Hindi)"},
            markdown=lambda text, **kwargs: rendered.append(("markdown", text, kwargs)),
            selectbox=lambda label, options, **kwargs: (label, options, kwargs.get("format_func", str)(options[0])),
        )
        with patch.dict(sys.modules, {"streamlit": fake}):
            install_streamlit_localization(fake)
            fake.markdown('<div><h1>Ask anything. Start anywhere.</h1></div>', unsafe_allow_html=True)
            label, options, first_display_value = fake.selectbox("Appearance", ["Midnight", "Pearl"], key="theme_mode")

        self.assertIn("कुछ भी पूछें", rendered[0][1])
        self.assertEqual(label, "रूप-रंग")
        self.assertEqual(options, ["Midnight", "Pearl"])
        self.assertEqual(first_display_value, "Midnight")

    def test_language_columns_remain_aligned_for_regional_languages(self):
        # Guards against accidentally assigning Punjabi/Urdu/Odia/Assamese strings to the wrong locale.
        self.assertEqual(translate_text("Home", "ur"), "صفحۂ آغاز")
        self.assertEqual(translate_text("Home", "or"), "ମୂଳପୃଷ୍ଠା")
        self.assertEqual(translate_text("Home", "as"), "হোম")
        self.assertEqual(translate_text("＋ New chat", "pa"), "＋ ਨਵੀਂ ਗੱਲਬਾਤ")

    def test_translation_coverage_exists_for_every_interface_locale(self):
        from sudhaar.i18n import LANGUAGES
        for language_label, code in LANGUAGES.items():
            if code != "en":
                with self.subTest(language=language_label):
                    self.assertNotEqual(translate_text("Home", code), "Home")
                    self.assertNotEqual(translate_text("Feedback", code), "Feedback")

if __name__ == "__main__":
    unittest.main()
