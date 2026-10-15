import unittest

from oss2_engine.classifier import classify_issue


class ClassifierTests(unittest.TestCase):
    def test_docs(self):
        self.assertEqual(classify_issue("Fix README typo").category, "documentation")

    def test_testing(self):
        self.assertEqual(classify_issue("Increase test coverage").category, "testing")

    def test_bugfix(self):
        self.assertEqual(classify_issue("Fix login bug").category, "bugfix")

    def test_other(self):
        self.assertEqual(classify_issue("Refactor module").category, "other")

    def test_beginner_label(self):
        self.assertTrue(classify_issue("Update docs", ["good first issue"]).beginner_friendly)

    def test_invalid_title(self):
        with self.assertRaises(ValueError):
            classify_issue(" ")

    def test_invalid_labels(self):
        with self.assertRaises(TypeError):
            classify_issue("Valid", [42])


if __name__ == "__main__":
    unittest.main()
