import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r"[A-Z]", password))
    lower_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_criteria = bool(re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\-=/\\|]", password))


    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    
    print("\nPassword Assessment:")
    print(f"✔ Length (>=8): {'Yes' if length_criteria else 'No'}")
    print(f"✔ Uppercase Letter: {'Yes' if upper_criteria else 'No'}")
    print(f"✔ Lowercase Letter: {'Yes' if lower_criteria else 'No'}")
    print(f"✔ Digit: {'Yes' if digit_criteria else 'No'}")
    print(f"✔ Special Character: {'Yes' if special_criteria else 'No'}")

    
    if score == 5:
        print("\n🔐 Password Strength: Excellent ✅")
    elif score >= 4:
        print("\n🟢 Password Strength: Strong")
    elif score == 3:
        print("\n🟡 Password Strength: Medium")
    elif score == 2:
        print("\n🟠 Password Strength: Weak")
    else:
        print("\n🔴 Password Strength: Very Weak ❌")

def main():
    print("🔍 Password Strength Checker")
    password = input("Enter your password: ")
    assess_password_strength(password)

if __name__ == "__main__":
    main()
