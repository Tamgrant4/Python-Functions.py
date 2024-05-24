# Q1 Task 1

def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers."""
  return x / y

# Task 2

def get_user_input():
  """Prompts the user for operation and numbers, handling invalid input."""
  while True:
    # Get operation
    operation = input("Enter operation (+, -, *, /): ")

    # Validate operation
    if operation not in "+-*/":
      print("Invalid operation. Please use +, -, *, or /.")
      continue

    # Get numbers
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      return operation, num1, num2  # Return all three values
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

# Example usage (assuming functions from Task 1 are defined)
operation, num1, num2 = get_user_input()

if operation == "+":
  result = add(num1, num2)
elif operation == "-":
  result = subtract(num1, num2)
# ... (similar logic for multiply and divide)

# Task 3

def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers, handling division by zero."""
  if y == 0:
    print("Error: Cannot divide by zero.")
    return None  # Indicate error
  else:
    return x / y

def get_user_input():
  """Prompts the user for operation and numbers, handling invalid input."""
  while True:
    # Get operation
    operation = input("Enter operation (+, -, *, /): ")

    # Validate operation
    if operation not in "+-*/":
      print("Invalid operation. Please use +, -, *, or /.")
      continue

    # Get numbers
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      return operation, num1, num2  # Return all three values
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

def main():
  """Prompts the user for input, performs the calculation, and displays the result."""
  while True:
    operation, num1, num2 = get_user_input()

    # Perform calculation based on operation
    result = None
    if operation == "+":
      result = add(num1, num2)
    elif operation == "-":
      result = subtract(num1, num2)
    elif operation == "*":
      result = multiply(num1, num2)
    else:
      result = divide(num1, num2)

    # Display the result or error message
    if result is not None:
      print(f"Result: {result}")
    else:
      continue  # Skip to the next iteration if division by zero occurred

if __name__ == "__main__":
  main()

# Q 2 Task 1

def add_to_shopping_list(shopping_list):
  """Prompts the user for an item and adds it to the shopping list."""
  item = input("Enter an item to add to the shopping list (or 'done' to finish): ")
  while item.lower() != "done":
    shopping_list.append(item)  # Add item to the list
    item = input("Enter another item (or 'done' to finish): ")
  print("Shopping list updated!")

# Task 2

def add_to_shopping_list(shopping_list):
  """Prompts the user for items to add and allows removal."""
  item = input("Enter an item to add (or 'done' to finish): ")
  while item.lower() != "done":
    shopping_list.append(item)  # Add item to the list
    item = input("Enter another item (or 'done' to finish): ")
    print("Shopping list updated!")

    # Option to remove items
    remove_item = input("Do you want to remove an item (y/n)? ")
    if remove_item.lower() == "y":
      item_to_remove = input("Enter the item to remove: ")
      if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f"Item '{item_to_remove}' removed from the list.")
      else:
        print(f"Item '{item_to_remove}' not found in the list.")

def main():
  """Initializes the shopping list and calls the add/remove function."""
  shopping_list = []
  add_to_shopping_list(shopping_list)

  # Display the final shopping list
  if shopping_list:
    print("\nYour shopping list:")
    for item in shopping_list:
      print(f"- {item}")
  else:
    print("\nYour shopping list is empty.")

if __name__ == "__main__":
  main()

# Task 3

def add_to_shopping_list(shopping_list):
  """Prompts the user for items to add and allows removal."""
  # ... (code for adding items and optional removal)

def print_shopping_list(shopping_list):
  """Prints the shopping list in a numbered format."""
  if shopping_list:
    print("\nYour shopping list:")
    for i, item in enumerate(shopping_list, start=1):
      print(f"{i}. {item}")
  else:
    print("\nYour shopping list is empty.")

def main():
  """Initializes the shopping list, calls add/remove, and prints the list."""
  shopping_list = []
  add_to_shopping_list(shopping_list)
  print_shopping_list(shopping_list)

if __name__ == "__main__":
  main()

# Q 3 

# task 1

def calculate_average(grades):
  """Calculates the average grade for a list of grades."""
  if not grades:
    return None  # Handle empty list case (optional)
  return sum(grades) / len(grades)

# Task 2

def find_highest_lowest(grades):
  """Finds the highest and lowest grades in a list."""
  if not grades:
    return None, None  # Handle empty list case (optional)
  return max(grades), min(grades)

# Task 3

def categorize_grade(grade):
  """Categorizes a grade into a letter grade (A, B, C, etc.)."""
  if grade >= 90:
    return "A"
  elif grade >= 80:
    return "B"
  elif grade >= 70:
    return "C"
  elif grade >= 60:
    return "D"
  else:
    return "F"

# Q 4 

# Task 1

# Sample questions and answers (replace with your own)
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "In what year was the Declaration of Independence signed?"
]
answers = ["Paris", "Jupiter", "1776"]

# Task 2

def quiz(questions, answers):
  """Conducts a quiz and takes user's answers."""
  score = 0
  for i, (question, answer) in enumerate(zip(questions, answers)):
    user_answer = input(f"Question {i+1}: {question} \nYour answer: ")
    if user_answer.lower() == answer.lower():
      print("Correct!")
      score += 1
    else:
      print(f"Incorrect. The answer is {answer}.")
  return score

# Example usage
total_questions = len(questions)
quiz_score = quiz(questions, answers)
print(f"You scored {quiz_score} out of {total_questions} questions.")

# Task 3

def quiz(questions, answers):
  """Conducts a quiz, takes user's answers, and provides feedback."""
  # ... (code from Task 2)

  if score == total_questions:
    print("Excellent work! You got all the answers correct.")
  elif score > total_questions / 2:
    print("Great job! You answered most questions correctly.")
  else:
    print("Don't worry, keep practicing! You can improve your score next time.")
  return score

# Q 5

# Task 1

def log_activities(activities, durations):
  """Logs fitness activities and their durations."""
  if len(activities) != len(durations):
    print("Error: Activity list and duration list must have the same length.")
    return

  activity_log = []
  for activity, duration in zip(activities, durations):
    activity_log.append({"activity": activity, "duration": duration})
  return activity_log

# Sample activities and durations (replace with your actual data)
activities = ["Running", "Yoga", "Strength Training"]
durations = [30, 20, 45]

activity_log = log_activities(activities, durations)
print(activity_log)  # Output: [{'activity': 'Running', 'duration': 30}, {'activity': 'Yoga', 'duration': 20}, {'activity': 'Strength Training', 'duration': 45}]

# Task 2

def estimate_calories_burned(activity, duration):
  """Estimates calories burned based on activity and duration (using a base rate of 3.5 calories/minute)."""
  calories_per_minute = 3.5  # You can adjust this base rate based on activity intensity
  return calories_per_minute * duration

# Example usage
activity = "Swimming"
duration = 45
calories_burned = estimate_calories_burned(activity, duration)
print(f"{activity} for {duration} minutes burned approximately {calories_burned} calories.")

# Task 3

def summarize_activity_log(activity_log):
  """Provides a summary report of all activities and total calories burned."""
  total_calories = 0
  print("Your Activity Summary:")
  for entry in activity_log:
    activity = entry["activity"]
    duration = entry["duration"]
    calories_burned = estimate_calories_burned(activity, duration)
    total_calories += calories_burned
    print(f"- {activity} for {duration} minutes: {calories_burned} calories burned")
  print(f"Total calories burned: {total_calories} calories")

# Example usage (assuming activity_log is defined from Task 1)
summarize_activity_log(activity_log)

