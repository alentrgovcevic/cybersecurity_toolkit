from password_lib import PasswordManager 

def run_tool():
    print("--- 🛡️ Advanced Password Security Suite ---")
    
    p1 = input("Enter new password: ")
    p2 = input("Retype password: ")

    # Initialize our professional class
    manager = PasswordManager(p1, p2)

    # 1. Check if they match first
    if not manager.validate_match():
        print("❌ Error: Passwords do not match. Try again.")
        return

    # 2. Run the heavy analysis
    print("\n🔍 Analyzing security and breach history...")
    results = manager.get_full_analysis()

    # 3. Display results to user
    print(f"\nResult: {results['security_warning']}")
    if results['is_compromised']:
        print(f"⚠️ DANGER: This password appeared in {results['pwned_count']} data breaches!")
    
    print(f"🔒 Secure SHA-256 Hash: {results['sha256_hash']}")
    print("-" * 42)

if __name__ == "__main__":
    run_tool()
