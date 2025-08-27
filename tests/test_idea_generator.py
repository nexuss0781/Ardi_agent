import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.idea_generator import IdeaGenerator

class TestIdeaGenerator(unittest.TestCase):
    def setUp(self):
        self.idea_gen = IdeaGenerator()
        self.test_file = "/home/ubuntu/ardi_agent/idea.md"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_generate_features(self):
        clarified_content = "Clarified objectives for: Develop a task management app."
        features = self.idea_gen.generate_features(clarified_content)
        self.assertIn("Comprehensive feature analysis based on: Clarified objectives for: Develop a task management app.", features)
        self.assertIn("- User Authentication (Login, Logout, Registration)", features)

    def test_save_idea_content(self):
        content = "Test idea content."
        self.idea_gen.save_idea_content(content)
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, "r") as f:
            read_content = f.read()
        self.assertEqual(read_content, content)

if __name__ == '__main__':
    unittest.main()


