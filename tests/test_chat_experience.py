import unittest
from unittest.mock import patch
import sudhaar.ai_engine as ai_engine
from sudhaar.ai_engine import (
    retrieve,
    is_general_information_query,
    is_topic_only_query,
    resolve_response_mode,
    answer_question,
)


class ChatExperienceTests(unittest.TestCase):
    def test_topic_only_alcohol_is_educational(self):
        self.assertTrue(is_general_information_query("alcohol"))
        self.assertTrue(is_topic_only_query("alcohol"))

    def test_health_question_is_educational(self):
        self.assertTrue(is_general_information_query("Explain alcohol and its health risks"))

    def test_factual_question_overrides_listening_mode(self):
        self.assertEqual(resolve_response_mode("alcohol", "listen"), "health")
        self.assertEqual(resolve_response_mode("What is cannabis?", "family"), "health")

    def test_emotional_sharing_is_not_misclassified(self):
        query = "I'm scared and I need someone to listen"
        self.assertFalse(is_general_information_query(query))
        self.assertEqual(resolve_response_mode(query, "auto"), "listen")

    def test_service_query_routes_to_services(self):
        query = "Find a de-addiction helpline"
        self.assertFalse(is_general_information_query(query))
        self.assertEqual(resolve_response_mode(query, "auto"), "services")

    def test_alcohol_query_retrieves_alcohol_specific_source_first(self):
        result = retrieve("alcohol", top_k=3)
        self.assertTrue(result)
        self.assertIn("Alcohol", result[0]["title"])

    def test_health_risks_query_retrieves_alcohol_source(self):
        result = retrieve("alcohol health risks effects", top_k=3)
        self.assertTrue(any("Alcohol" in item["title"] for item in result))

    def test_tobacco_query_retrieves_tobacco_source(self):
        result = retrieve("tobacco and nicotine health risks", top_k=3)
        self.assertTrue(any("Tobacco" in item["title"] for item in result))

    def test_cannabis_query_retrieves_cannabis_source(self):
        result = retrieve("cannabis effects", top_k=3)
        self.assertTrue(any("Cannabis" in item["title"] for item in result))

    def test_topic_only_prompt_forces_health_mode_and_drops_emotional_history(self):
        captured = {}
        def fake_chat(messages):
            captured["messages"] = messages
            return "Alcohol is a psychoactive substance found in alcoholic drinks."
        status = {"server": True, "model": True, "model_name": "qwen2.5:3b", "installed": ["qwen2.5:3b"], "error": ""}
        with patch.object(ai_engine, "ollama_status", return_value=status), patch.object(ai_engine, "_ollama_chat", side_effect=fake_chat):
            answer, sources, mode, error = answer_question(
                "alcohol", response_language="English", conversation_mode="listen",
                history=[{"role": "user", "content": "I'm scared and need someone to listen"},
                         {"role": "assistant", "content": "I'm sorry you feel that way."}],
            )
        self.assertIn("Alcohol is", answer)
        self.assertEqual(mode, "live")
        self.assertEqual(error, "")
        self.assertEqual(len(captured["messages"]), 2, "A bare topic should not inherit prior emotional chat history.")
        self.assertIn("Conversation mode: The user wants health information", captured["messages"][0]["content"])
        self.assertIn("only a topic word/short phrase", captured["messages"][-1]["content"])


if __name__ == "__main__":
    unittest.main()
