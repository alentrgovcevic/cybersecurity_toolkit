import hashlib
import requests # You might need: pip install requests

class PasswordManager:
    def __init__(self, password, confirm_password):
        self.password = password
        self.confirm_password = confirm_password

    def validate_match(self):
        """Check if both passwords match (Standard UI logic)"""
        return self.password == self.confirm_password

    def check_pwned_api(self):
        """
        Senior Dev Move: Checks if the password exists in known data breaches.
        Uses K-Anonymity (only sends first 5 chars of hash for privacy).
        """
        sha1_password = hashlib.sha1(self.password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1_password[:5], sha1_password[5:]
        
        try:
            url = f"https://api.pwnedpasswords.com/range/{prefix}"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                # Search the results for our suffix
                hashes = (line.split(':') for line in response.text.splitlines())
                for h, count in hashes:
                    if h == suffix:
                        return int(count) # Found! Returns how many times it was leaked.
            return 0
        except Exception:
            return -1 # API Error or Timeout

    def secure_hash(self):
        """
        Securely hashes the password using SHA-256.
        In production, we would use bcrypt with a 'salt'.
        """
        return hashlib.sha256(self.password.encode()).hexdigest()

    def get_full_analysis(self):
        # 1. Match Check
        if not self.validate_match():
            return {"status": "error", "message": "Passwords do not match."}

        # 2. Breach Check
        leaks = self.check_pwned_api()
        
        # 3. Final Report
        return {
            "status": "success",
            "pwned_count": leaks,
            "sha256_hash": self.secure_hash(),
            "is_compromised": leaks > 0,
            "security_warning": "🚨 This password was found in a breach!" if leaks > 0 else "✅ No known breaches."
        }
