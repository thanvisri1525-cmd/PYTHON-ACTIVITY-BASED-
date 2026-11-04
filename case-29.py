print("PASSWORD VALIDATION ENGINE")

password = input("Enter your password: ")

has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)

has_special = any(
    not ch.isalnum() and not ch.isspace()
    for ch in password
)

errors = []

if len(password) < 8:
    errors.append("At least 8 characters required.")

if not has_upper:
    errors.append("Include an uppercase letter.")

if not has_lower:
    errors.append("Include a lowercase letter.")

if not has_digit:
    errors.append("Include a digit.")

if not has_special:
    errors.append("Include a special character.")

if errors:
    print("Password is invalid.")
    for error in errors:
        print("-", error)
else:
    print("Password satisfies all rules.")
