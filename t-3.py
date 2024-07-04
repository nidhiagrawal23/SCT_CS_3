import re

def assess_password_strength(password):
    # Criteria scores
    length_score = 0
    uppercase_score = 0
    lowercase_score = 0
    number_score = 0
    special_char_score = 0

    # Criteria weights
    length_weight = 1
    uppercase_weight = 1
    lowercase_weight = 1
    number_weight = 1
    special_char_weight = 1

    # Assess length
    if len(password) >= 8:
        length_score = 1

    # Assess presence of uppercase letters
    if re.search(r'[A-Z]', password):
        uppercase_score = 1

    # Assess presence of lowercase letters
    if re.search(r'[a-z]', password):
        lowercase_score = 1

    # Assess presence of numbers
    if re.search(r'[0-9]', password):
        number_score = 1

    # Assess presence of special characters
    if re.search(r'[\W_]', password):
        special_char_score = 1

    # Calculate total score
    total_score = (length_score * length_weight +
                   uppercase_score * uppercase_weight +
                   lowercase_score * lowercase_weight +
                   number_score * number_weight +
                   special_char_score * special_char_weight)

    # Determine password strength
    if total_score == 5:
        strength = "Very Strong"
    elif total_score == 4:
        strength = "Strong"
    elif total_score == 3:
        strength = "Moderate"
    elif total_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "score": total_score,
        "strength": strength,
        "criteria": {
            "length": length_score,
            "uppercase": uppercase_score,
            "lowercase": lowercase_score,
            "number": number_score,
            "special_char": special_char_score
        }
    }

# Get user input
password = input("Enter your password: ")

# Assess the password strength
result = assess_password_strength(password)

# Print the results
print(f"Password Strength: {result['strength']} (Score: {result['score']}/5)")
print("Criteria Breakdown:", result['criteria'])
