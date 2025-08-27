import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.clarification_agent import ClarificationAgent

class TestClarificationAgent(unittest.TestCase):
    def setUp(self):
        self.clar_agent = ClarificationAgent()
        self.test_file = "/home/ubuntu/ardi_agent/clarify.md"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_clarify_objectives(self):
        query = "Develop a task management app."
        clarified_content = self.clar_agent.clarify_objectives(query)
        self.assertIn("Clarified objectives for: Formalized query: Develop a task management app.", clarified_content)
        self.assertTrue(self.clar_agent.get_clarification_todo()["Audience"])
        self.assertTrue(self.clar_agent.get_clarification_todo()["Comprehensive"])

    def test_save_clarified_content(self):
        content = "Test clarified content."
        self.clar_agent.save_clarified_content(content)
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as f:
            read_content = f.read()
        self.assertEqual(read_content, content)

if __name__ == '__main__':
    unittest.main()


