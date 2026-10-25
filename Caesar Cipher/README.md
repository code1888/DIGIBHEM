# 🔐 Caesar Cipher Encryption and Decryption

## TASK-1

### Project Title

**Caesar Cipher Encryption and Decryption Tool**

### Student Name

**Shubham Rajendra Dubele**

---

## 📌 Project Overview

The **Caesar Cipher** is one of the simplest and most well-known encryption techniques. It is a substitution cipher in which each letter in a message is shifted by a fixed number of positions in the alphabet.

This project implements the Caesar Cipher algorithm using **Python**. The program allows the user to enter a message and a shift value and then perform either encryption or decryption.

---

## 🎯 Objective

The main objective of this project is to:

* Implement the Caesar Cipher algorithm using Python.
* Encrypt a plain-text message using a user-defined shift value.
* Decrypt an encrypted message.
* Understand the basic concept of substitution-based encryption.
* Develop an interactive command-line cryptography application.

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **IDE:** Visual Studio Code
* **Algorithm:** Caesar Cipher
* **Interface:** Command Line Interface (CLI)

---

## ✨ Features

* 🔒 Encrypt text using Caesar Cipher.
* 🔓 Decrypt encrypted text.
* 🔢 User-defined shift value.
* 🔤 Supports uppercase letters.
* 🔡 Supports lowercase letters.
* ␠ Preserves spaces.
* 🔣 Preserves numbers and special characters.
* ⚠️ Handles invalid shift input.
* 🔄 Provides a menu-driven interface.

---

## 📂 Project Structure

```text
Caesar-Cipher-Project/
│
├── caesar_cipher.py
├── README.md
│
└── screenshots/
    └── output.png
```

---

## 🔐 How Caesar Cipher Works

The Caesar Cipher shifts every alphabetic character by a fixed number of positions.

For example, with a shift value of **3**:

```text
A → D
B → E
C → F
D → G
E → H
...
X → A
Y → B
Z → C
```

### Example

Original message:

```text
Hello World
```

Shift value:

```text
3
```

Encrypted message:

```text
Khoor Zruog
```

Decryption of:

```text
Khoor Zruog
```

with shift `3` gives:

```text
Hello World
```

---

## 🧮 Encryption Formula

The encryption operation can be represented as:

```text
E(x) = (x + k) mod 26
```

Where:

* `x` = position of the character
* `k` = shift value
* `26` = number of letters in the English alphabet

---

## 🧮 Decryption Formula

The decryption operation is:

```text
D(x) = (x - k) mod 26
```

Where:

* `x` = position of the encrypted character
* `k` = shift value

---

## 🚀 How to Run the Project

### Step 1: Install Python

Check whether Python is installed:

```bash
python3 --version
```

Example:

```text
Python 3.13.0
```

---

### Step 2: Open the Project Folder

```bash
cd Caesar-Cipher-Project
```

---

### Step 3: Run the Program

On Linux/macOS:

```bash
python3 caesar_cipher.py
```

On Windows:

```bash
python caesar_cipher.py
```

---

## 💻 Program Menu

When the program starts, it displays:

```text
==================================================
       CAESAR CIPHER
   Encryption & Decryption Tool
==================================================

Choose an option:
1. Encrypt Message
2. Decrypt Message
3. Exit
```

---

## 🔒 Encryption Example

Input:

```text
Enter your choice: 1
Enter message: Hello World
Enter shift value: 3
```

Output:

```text
Original Message : Hello World
Shift Value      : 3
Encrypted Message: Khoor Zruog
```

---

## 🔓 Decryption Example

Input:

```text
Enter your choice: 2
Enter encrypted message: Khoor Zruog
Enter shift value: 3
```

Output:

```text
Encrypted Message: Khoor Zruog
Shift Value      : 3
Decrypted Message: Hello World
```

---

## 🔄 Working Process

```text
              ┌─────────────────┐
              │   Start Program │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Select Option  │
              └────────┬────────┘
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      ┌──────────────┐    ┌──────────────┐
      │   Encrypt    │    │   Decrypt    │
      └──────┬───────┘    └──────┬───────┘
             │                   │
             └─────────┬─────────┘
                       ▼
              ┌─────────────────┐
              │ Enter Message   │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Enter Shift     │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Apply Caesar    │
              │ Cipher Formula  │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Display Result  │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Continue / Exit │
              └─────────────────┘
```

---

## 📸 Screenshots

Add screenshots of your program output inside the `screenshots` folder.

Recommended screenshot:

```text
screenshots/output.png
```

The screenshot should show:

* Caesar Cipher program menu
* Input message
* Shift value
* Encrypted message
* Decrypted message

---

## 🧪 Test Cases

| Test Case | Input         | Shift | Expected Output |
| --------- | ------------- | ----: | --------------- |
| 1         | `Hello`       |     3 | `Khoor`         |
| 2         | `World`       |     3 | `Zruog`         |
| 3         | `ABC`         |     3 | `DEF`           |
| 4         | `XYZ`         |     3 | `ABC`           |
| 5         | `Hello World` |     5 | `Mjqqt Btwqi`   |

---

## ⚠️ Limitations

The Caesar Cipher has a very small key space because there are only 26 possible shifts for the English alphabet.

Therefore:

* It can be easily broken using brute-force attacks.
* It is not suitable for protecting sensitive information.
* It should be used mainly for educational purposes.

---

## 🎓 Learning Outcomes

After completing this project, the following concepts are understood:

* Basic cryptography concepts.
* Substitution ciphers.
* Encryption and decryption.
* Character manipulation in Python.
* ASCII/Unicode character conversion.
* Modular arithmetic.
* Functions in Python.
* User input and menu-driven programs.
* Basic cybersecurity concepts.

---

## ✅ Result

The **Caesar Cipher Encryption and Decryption Tool** was successfully implemented using Python.

The program can:

1. Accept a message from the user.
2. Accept a shift value.
3. Encrypt the message.
4. Decrypt the encrypted message.
5. Display the result through a command-line interface.


