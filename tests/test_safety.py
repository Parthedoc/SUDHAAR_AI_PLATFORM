import unittest
from sudhaar.safety import detect_risk
from sudhaar.ai_engine import retrieve

class SUDHAARSafetyTests(unittest.TestCase):
    def test_emergency_english(self):
        self.assertEqual(detect_risk("My friend is unconscious after taking something"), "urgent")

    def test_breathing_difficulty(self):
        self.assertEqual(detect_risk("He cannot breathe"), "urgent")

    def test_self_harm_english(self):
        self.assertEqual(detect_risk("I want to kill myself"), "self_harm")

    def test_regular_health_question_not_routed(self):
        self.assertIsNone(detect_risk("What are general health risks of alcohol use?"))

    def test_hindi_keyword(self):
        self.assertEqual(detect_risk("वह बेहोश है"), "urgent")

    def test_retrieval_finds_deaddiction_support(self):
        results = retrieve("India de-addiction helpline counselling 14446", top_k=3)
        self.assertTrue(any("de-addiction" in x["title"].lower() or "helpline" in x["title"].lower() for x in results))

    def test_retrieval_finds_general_health(self):
        results = retrieve("alcohol health risks", top_k=3)
        self.assertTrue(results)
        self.assertTrue(any("health" in x["title"].lower() for x in results))

if __name__ == "__main__":
    unittest.main()
