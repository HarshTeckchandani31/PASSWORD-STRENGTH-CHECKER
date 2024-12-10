import re
from typing import Dict, Tuple

class PasswordStrengthAnalyzer:
    def __init__(self):
        self.min_length = 8
        self.special_chars = "!@#$%^&*(),.?\":{}|<>"

    def analyze_password(self, password: str) -> Tuple[int, Dict[str, bool], str]:
        """
        Analyzes password strength and returns a score, checks, and feedback.
        
        Args:
            password: The password to analyze
            
        Returns:
            Tuple containing:
            - Score (0-10)
            - Dictionary of check results
            - Overall strength label
        """
        checks = self._perform_checks(password)
        score = self._calculate_score(checks)
        strength_label = self._get_strength_label(score)
        
        return score, checks, strength_label

    def _perform_checks(self, password: str) -> Dict[str, bool]:
        """Performs individual security checks on the password."""
        return {
            "length": len(password) >= self.min_length,
            "has_uppercase": bool(re.search(r"[A-Z]", password)),
            "has_lowercase": bool(re.search(r"[a-z]", password)),
            "has_numbers": bool(re.search(r"\d", password)),
            "has_special": bool(re.search(f"[{re.escape(self.special_chars)}]", password)),
            "has_sequential": bool(re.search(r"(123|234|345|456|567|678|789|987|876|765|654|543|432|321)", password)),
            "has_repeating": bool(re.search(r"(.)\1{2,}", password))
        }

    def _calculate_score(self, checks: Dict[str, bool]) -> int:
        """Calculates the password strength score based on checks."""
        score = 0
        
        # Add points for positive checks
        if checks["length"]: score += 2
        if checks["has_uppercase"]: score += 2
        if checks["has_lowercase"]: score += 2
        if checks["has_numbers"]: score += 2
        if checks["has_special"]: score += 2
        
        # Subtract points for negative patterns
        if checks["has_sequential"]: score -= 2
        if checks["has_repeating"]: score -= 2
        
        return max(0, min(10, score))

    def _get_strength_label(self, score: int) -> str:
        """Converts numerical score to descriptive strength label."""
        if score >= 8:
            return "Strong"
        elif score >= 6:
            return "Good"
        elif score >= 4:
            return "Fair"
        return "Weak"