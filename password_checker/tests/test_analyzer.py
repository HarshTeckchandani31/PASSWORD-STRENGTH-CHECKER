import unittest
from password_checker.strength_analyzer import PasswordStrengthAnalyzer

class TestPasswordStrengthAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = PasswordStrengthAnalyzer()

    def test_weak_password(self):
        score, checks, strength = self.analyzer.analyze_password("password")
        self.assertLess(score, 4)
        self.assertEqual(strength, "Weak")
        self.assertTrue(checks["has_lowercase"])
        self.assertFalse(checks["has_uppercase"])

    def test_strong_password(self):
        score, checks, strength = self.analyzer.analyze_password("P@ssw0rd123!")
        self.assertGreaterEqual(score, 8)
        self.assertEqual(strength, "Strong")
        self.assertTrue(all([
            checks["has_uppercase"],
            checks["has_lowercase"],
            checks["has_numbers"],
            checks["has_special"]
        ]))

    def test_sequential_numbers(self):
        score, checks, _ = self.analyzer.analyze_password("password123")
        self.assertTrue(checks["has_sequential"])

    def test_repeating_characters(self):
        score, checks, _ = self.analyzer.analyze_password("passsword")
        self.assertTrue(checks["has_repeating"])

if __name__ == '__main__':
    unittest.main()