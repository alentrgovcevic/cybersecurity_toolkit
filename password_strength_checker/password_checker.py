import re
import math

def calculate_crack_time(password):
    # Determine the character set size (Pool)
    pool_size = 0
    if re.search(r"[a-z]", password): pool_size += 26
    if re.search(r"[A-Z]", password): pool_size += 26
    if re.search(r"\d", password): pool_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>+=-]", password): pool_size += 32

    if pool_size == 0: return 0, "0 seconds"

    # Calculate entropy (Pool Size ^ Length)
    # combinations = pool_size ** len(password)
    # Using log2 to avoid massive numbers
    entropy_bits = len(password) * math.log2(pool_size)
    combinations = 2 ** entropy_bits

    # Assume a powerful GPU cluster/Botnet doing 100 Billion guesses per second
    guesses_per_second = 100_000_000_000 
    seconds = combinations / guesses_per_second

    # Convert seconds to readable format
    if seconds < 1: return entropy_bits, "Instantly"
    if seconds < 60: return entropy_bits, f"{int(seconds)} seconds"
    if seconds < 3600: return entropy_bits, f"{int(seconds // 60)} minutes"
    if seconds < 86400: return entropy_bits, f"{int(seconds // 3600)} hours"
    if seconds < 31536000: return entropy_bits, f"{int(seconds // 86400)} days"
    
    years = seconds / 31536000
    if years < 1000: return entropy_bits, f"{int(years)} years"
    if years < 1000000: return entropy_bits, f"{int(years // 1000)} thousand years"
    return entropy_bits, "Centuries"

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria checks
    if len(password) >= 12: strength += 1
    else: feedback.append("Increase length to at least 12 characters.")
    
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password): strength += 1
    else: feedback.append("Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password): strength += 1
    else: feedback.append("Add at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>+=-]", password): strength += 1
    else: feedback.append("Add a special character.")
    
    common_patterns = r"(123|abc|qwerty|password|admin|welcome|111|000)"
    if re.search(common_patterns, password.lower()):
        feedback.append("Avoid common sequences (e.g., 'abc', '123', '111').")
    else:
        strength += 1

    # Check for consecutive numerical sequences (e.g., 456, 789)
    has_consecutive = False
    for i in range(len(password) - 2):
        # Check if three characters in a row are consecutive numbers
        chunk = password[i:i+3]
        if chunk.isdigit():
            if int(chunk[1]) == int(chunk[0]) + 1 and int(chunk[2]) == int(chunk[1]) + 1:
                has_consecutive = True
                break

    if has_consecutive:
        feedback.append("Avoid consecutive number sequences (e.g., '456').")
        # Optional: decrease strength if you want to penalize this heavily
        strength -= 1 

    # Calculate Time to Crack
    entropy, crack_time = calculate_crack_time(password)

    levels = {0: "Dangerously Weak", 1: "Weak", 2: "Fair", 3: "Moderate", 4: "Strong", 5: "Very Strong"}
    return levels.get(strength, "Weak"), feedback, crack_time, entropy

if __name__ == "__main__":
    pwd = input("Enter password to analyze: ")
    rating, suggestions, crack_time, entropy = check_password_strength(pwd)
    
    print(f"\n--- Security Analysis ---")
    print(f"Strength Rating: {rating}")
    print(f"Entropy: {entropy:.2f} bits")
    print(f"Estimated Brute-Force Time: {crack_time}")
    print(f"(Assumes 100 Billion guesses/sec)")
    
    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(f"- {s}")
