# 🛡️ Cybersecurity Python Toolkit

A collection of practical security tools developed to demonstrate core cybersecurity concepts, automation, and risk assessment.

## 🛠️ Integration & Scaling
All tools in this repository are designed with **modular architecture**. 
- **JSON Output:** Functions return structured dictionaries, making them ready for REST API integration (FastAPI/Flask).
- **Extensible:** The Port Scanner uses a Class-based approach, allowing it to be imported into larger monitoring dashboards.
- **Decoupled Logic:** Input/Output logic is separated from the security analysis engines.


---

## 🔑 Project 1: Password Strength & Entropy Analyzer
This tool evaluates the strength of a password not just by "rules," but by calculating the mathematical difficulty of cracking it.

### Features
*   **Heuristic Pattern Detection:** Identifies common sequences (e.g., `abc123`, `qwerty`) and consecutive numerical strings (e.g., `456`) that dictionary attacks prioritize.
*   **Entropy Calculation:** Uses $E = L \cdot \log_2(R)$ to determine the bits of entropy.
*   **Risk Assessment:** Estimates "Time to Crack" based on a high-speed offline brute-force attack (100 Billion guesses/sec).
*   **Actionable Feedback:** Provides specific security recommendations to the user.

### Technical Concepts Applied
*   **Regular Expressions (Regex):** For complex pattern matching.
*   **Information Theory:** Applying Shannon entropy to password security.
*   **Defensive Programming:** Validating user input and handling edge cases.

### How to Run
```bash
python password_check.py

### 🛡️ Advanced Password Security (v2.0)
The Password Analyzer has been upgraded to a production-ready class:
- **Pwned-API Integration:** Uses K-Anonymity to check if passwords have been compromised in historical data breaches without exposing the plain-text password.
- **Secure Hashing:** Implements SHA-256 hashing (industry standard for data integrity).
- **Matching Logic:** Includes validation for "Retype Password" workflows.
- **REST-Ready:** Returns dictionary objects for easy integration into web frameworks like Flask or FastAPI.


