# ============================================
# TASK-3: Password Complexity Checker
# ============================================

import re


def check_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special character check
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!, @, #, $, etc.).")

    # Password strength
    if score <= 2:
        strength = "WEAK"
    elif score == 3 or score == 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return score, strength, feedback


# Main Program
print("=" * 55)
print("          PASSWORD COMPLEXITY CHECKER")
print("=" * 55)

password = input("\nEnter your password: ")

score, strength, feedback = check_password(password)

print("\n" + "-" * 55)
print("Password Analysis")
print("-" * 55)

print("Length              :", len(password))
print("Uppercase Letter    :", "Yes" if re.search(r"[A-Z]", password) else "No")
print("Lowercase Letter    :", "Yes" if re.search(r"[a-z]", password) else "No")
print("Number              :", "Yes" if re.search(r"[0-9]", password) else "No")
print("Special Character   :", "Yes" if re.search(r"[^A-Za-z0-9]", password) else "No")

print("\nScore               :", score, "/ 5")
print("Password Strength   :", strength)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("- " + item)
else:
    print("\nExcellent! Your password satisfies all basic complexity criteria.")

print("\n" + "=" * 55)