import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.language_expert import LanguageExpert

class TestLanguageExpert(unittest.TestCase):
    def test_formalize_query(self):
        le = LanguageExpert()
        query = "develop a web app"
        formalized_query = le.formalize_query(query)
        self.assertEqual(formalized_query, "Formalized query: develop a web app")

if __name__ == '__main__':
    unittest.main()


