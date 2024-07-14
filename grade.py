def compute_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Input for the score
score_input = input("Enter the score: ")

try:
    score = float(score_input)
    if 0 <= score <= 100:
        # Compute the grade using the function
        grade = compute_grade(score)
        # Output the grade
        print(f"Grade: {grade}")
    else:
        print("Score must be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
