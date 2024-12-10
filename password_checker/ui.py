from typing import Dict

class PasswordCheckerUI:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.feedback_messages = {
            "length": "Use at least 8 characters",
            "has_uppercase": "Include uppercase letters",
            "has_lowercase": "Include lowercase letters",
            "has_numbers": "Include numbers",
            "has_special": "Include special characters",
            "has_sequential": "Avoid sequential numbers",
            "has_repeating": "Avoid repeating characters"
        }

    def run(self):
        """Runs the password checker interface."""
        while True:
            self._print_header()
            
            password = self._get_password()
            if password.lower() == 'quit':
                break
                
            self._analyze_and_display(password)
            
            choice = input("\nPress Enter to check another password (or type 'quit' to exit)...")
            if choice.lower() == 'quit':
                break
            print("\n" * 2)  # Add some spacing between checks

    def _print_header(self):
        """Prints the application header."""
        print("=" * 50)
        print("Password Strength Checker".center(50))
        print("=" * 50)
        print("\nEnter 'quit' to exit\n")

    def _get_password(self) -> str:
        """Gets password input from user."""
        return input("Enter password to check: ")

    def _analyze_and_display(self, password: str):
        """Analyzes password and displays results."""
        score, checks, strength = self.analyzer.analyze_password(password)
        
        print("\nStrength:", self._get_colored_strength(strength))
        print("\nScore:", self._create_strength_bar(score))
        
        self._display_feedback(checks)
        self._display_tips()

    def _get_colored_strength(self, strength: str) -> str:
        """Returns strength label with ANSI color coding."""
        colors = {
            "Weak": "\033[91m",    # Red
            "Fair": "\033[93m",    # Yellow
            "Good": "\033[94m",    # Blue
            "Strong": "\033[92m"   # Green
        }
        return f"{colors.get(strength, '')}{strength}\033[0m"

    def _create_strength_bar(self, score: int) -> str:
        """Creates a visual representation of password strength."""
        total_bars = 10
        filled_bars = int((score / 10) * total_bars)
        
        bar = "█" * filled_bars + "░" * (total_bars - filled_bars)
        return f"[{bar}] {score}/10"

    def _display_feedback(self, checks: Dict[str, bool]):
        """Displays feedback based on check results."""
        print("\nFeedback:")
        for check, passed in checks.items():
            if check in ["has_sequential", "has_repeating"]:
                if passed:  # For negative checks, True means the issue was found
                    print(f"❌ {self.feedback_messages[check]}")
            elif not passed:
                print(f"❌ {self.feedback_messages[check]}")

    def _display_tips(self):
        """Displays general password security tips."""
        print("\nTips for a strong password:")
        tips = [
            "Mix uppercase and lowercase letters",
            "Include numbers and special characters",
            "Make it at least 8 characters long",
            "Avoid common patterns and sequences",
            "Use unique passwords for different accounts"
        ]
        for tip in tips:
            print(f"• {tip}")