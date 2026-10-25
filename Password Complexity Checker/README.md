# 🔐 Password Complexity Checker

## TASK-3

### Project Title

**Password Complexity Checker**

## 📌 Project Overview

The **Password Complexity Checker** is a Python-based tool that evaluates the basic complexity of a password.

The program checks whether the password contains:

* Sufficient length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Based on these criteria, the program calculates a score and classifies the password as **Weak, Medium, or Strong**. It also provides suggestions to improve the password.

---

## 🎯 Objective

The main objectives of this project are:

* To understand password security concepts.
* To check the complexity of a user-provided password.
* To identify missing password requirements.
* To provide useful feedback for improving passwords.
* To implement password validation using Python.

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Library:** `re` (Regular Expressions)
* **IDE:** Visual Studio Code
* **Interface:** Command Line Interface (CLI)

---

## ✨ Features

* 🔤 Checks uppercase letters.
* 🔡 Checks lowercase letters.
* 🔢 Checks numbers.
* 🔣 Checks special characters.
* 📏 Checks password length.
* 📊 Calculates a complexity score.
* 🔐 Classifies password strength.
* 💡 Provides improvement suggestions.
* ⚠️ Handles passwords that fail one or more criteria.

---

## 📂 Project Structure

```text
Password-Complexity-Checker/
│
├── password_checker.py
├── README.md
│
└── screenshots/
    └── output.png
```

---

## 🔍 Password Criteria

The program evaluates five basic criteria.

| Criteria               | Points |
| ---------------------- | -----: |
| At least 8 characters  |      1 |
| Uppercase letter (A-Z) |      1 |
| Lowercase letter (a-z) |      1 |
| Number (0-9)           |      1 |
| Special character      |      1 |
| **Maximum Score**      |  **5** |

---

## 📊 Password Strength

The password is classified according to its score:

```text
0–2 Points → WEAK
3–4 Points → MEDIUM
5 Points   → STRONG
```

---

## 🧮 Example

### Input

```text
MySecure@123
```

### Analysis

```text
Length              : 12
Uppercase Letter    : Yes
Lowercase Letter    : Yes
Number              : Yes
Special Character   : Yes
```

### Result

```text
Score               : 5 / 5
Password Strength   : STRONG
```

---

## 💻 Sample Output

```text
=======================================================
          PASSWORD COMPLEXITY CHECKER
=======================================================

Enter your password: MySecure@123

-------------------------------------------------------
Password Analysis
-------------------------------------------------------
Length              : 12
Uppercase Letter    : Yes
Lowercase Letter    : Yes
Number              : Yes
Special Character   : Yes

Score               : 5 / 5
Password Strength   : STRONG

Excellent! Your password satisfies all basic complexity criteria.

=======================================================
```

---

## 🚀 How to Run

### Step 1: Check Python Installation

Open a terminal and run:

```bash
python3 --version
```

Example:

```text
Python 3.13.0
```

---

### Step 2: Open the Project Directory

```bash
cd Password-Complexity-Checker
```

---

### Step 3: Run the Program

Linux/macOS:

```bash
python3 password_checker.py
```

Windows:

```bash
python password_checker.py
```

---

## 🔄 Working Process

```text
             ┌────────────────────┐
             │    Start Program   │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Enter Password     │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Check Length       │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Check Uppercase    │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Check Lowercase    │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Check Numbers      │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Check Special Char │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Calculate Score    │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Determine Strength │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Display Feedback   │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │       End          │
             └────────────────────┘
```

---

## 🧪 Test Cases

| Test Case | Password       | Expected Strength |
| --------- | -------------- | ----------------- |
| 1         | `password`     | Weak              |
| 2         | `Password`     | Medium            |
| 3         | `Password1`    | Medium            |
| 4         | `Password@1`   | Strong            |
| 5         | `MySecure@123` | Strong            |

---

## 📸 Screenshots

Store the program screenshots in:

```text
screenshots/output.png
```

The screenshot should show:

* Program title
* Entered password
* Password analysis
* Complexity score
* Password strength
* Suggestions, if applicable

---

## 🎓 Learning Outcomes

After completing this project, the following concepts are understood:

* Password security fundamentals.
* Password complexity requirements.
* Python functions.
* Conditional statements.
* Regular expressions.
* String handling.
* User input.
* Score-based classification.
* Basic cybersecurity practices.

---

## ⚠️ Limitations

This tool evaluates **basic password complexity only**.

It does not determine whether a password:

* Has appeared in a data breach.
* Is a commonly used password.
* Is vulnerable to dictionary attacks.
* Is vulnerable to password reuse.
* Has sufficient entropy for a specific security requirement.

Therefore, a password marked **Strong** by this tool is not automatically guaranteed to be secure.

---

## 🔐 Security Note

For real applications, passwords should never be stored as plain text. Applications should use appropriate password hashing mechanisms such as **Argon2id, bcrypt, or scrypt**, along with secure authentication practices.

---

## ✅ Result

The **Password Complexity Checker** was successfully implemented using Python.

The program evaluates a password based on length, uppercase letters, lowercase letters, numbers, and special characters. It calculates a complexity score, determines the password strength, and provides feedback for improvement.

