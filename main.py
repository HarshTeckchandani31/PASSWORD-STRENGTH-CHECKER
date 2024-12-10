from password_checker.strength_analyzer import PasswordStrengthAnalyzer
from password_checker.ui import PasswordCheckerUI

def main():
    analyzer = PasswordStrengthAnalyzer()
    ui = PasswordCheckerUI(analyzer)
    ui.run()

if __name__ == "__main__":
    main()