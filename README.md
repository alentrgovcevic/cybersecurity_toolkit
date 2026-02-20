# 🛡️ Cybersecurity Python Toolkit

A collection of practical security tools developed to demonstrate core cybersecurity concepts, automation, and risk assessment.

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


---
