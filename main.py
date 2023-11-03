import os
import re
from arithmetic_arranger import arithmetic_arranger

# Constants for messages
WELCOME_MESSAGE = "🙋 Welcome to the Arithmetic Arranger!"
EXIT_MESSAGE = "🚪 Type 'quit' to exit at any time."
HELP_MESSAGE = "❓ Need help? Type 'help'."
SETTINGS_MESSAGE = "⚙️ Type 'settings' to change initial configurations."
PROBLEM_COUNT_QUERY = ("How would you like to enter problems?\n"
                       "1️⃣\tOne by one\n"
                       "2️⃣\tAll at once\n"
                       "Choose '1' or '2': ")
PROBLEM_COUNT_ERROR = "Oops! Please choose '1' for one by one or '2' for all at once: "
SHOW_ANSWERS_QUERY = "Do you want to see the answers right away? (y/n): "
SHOW_ANSWERS_ERROR = "Just type 'y' for yes or 'n' for no: "
HELP_INFO = (
    "📘 Help Info:\n"
    "- Enter arithmetic problems to solve them.\n"
    "- If you chose 'All at once' mode, you can enter up to five problems.\n"
    "- Format for problems: number operator number (e.g., 3 + 4).\n"
    "- Valid operators: '+' and '-'.\n")

# Function to get user input
def getUserInput(problem_count=1):
    problems = []
    while len(problems) < problem_count:
        user_input = input(f"Enter problem {len(problems) + 1}: ")
        regexp = r"(\d+)\s*([+-])\s*(\d+)"
        if re.match(regexp, user_input):
            formatted_problem = " ".join(re.match(regexp, user_input).groups())
            print(f"Your input: {formatted_problem}")
            confirm = input(
                "Press 'Enter' to confirm, or type 'edit' to modify: ").strip(
                ).lower()
            if confirm == 'edit':
                continue
            problems.append(formatted_problem)
        else:
            print(
                "The input does not match the expected format (number operator number). Please try again."
            )
    return problems

# Function to get initial configuration
def getInitialConfiguration():
    # Get problem count choice
    problem_count_choice = input(PROBLEM_COUNT_QUERY).strip()
    while problem_count_choice not in ['1', '2']:
        problem_count_choice = input(PROBLEM_COUNT_ERROR).strip()

    problem_count = 1 if problem_count_choice == '1' else 5

    # Get show answers choice
    show_answers_choice = input(SHOW_ANSWERS_QUERY).strip().lower()
    while show_answers_choice not in ['y', 'n']:
        show_answers_choice = input(SHOW_ANSWERS_ERROR).strip().lower()

    show_answers = show_answers_choice == 'y'

    return problem_count, show_answers

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Welcome message
print(WELCOME_MESSAGE)
print(EXIT_MESSAGE)
print(HELP_MESSAGE)
print(SETTINGS_MESSAGE)
print("")

# Initial configuration setup
problem_count, show_answers = getInitialConfiguration()

# Main loop
isRunning = True
while isRunning:
    user_problems = getUserInput(problem_count)
    if any('quit' in problem.lower() for problem in user_problems):
        print("👋 Exiting the calculator. Goodbye!")
        isRunning = False
    elif any('help' in problem.lower() for problem in user_problems):
        print(HELP_INFO)
    elif any('settings' in problem.lower() for problem in user_problems):
        # Clear the screen before showing settings
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🔧 Changing settings...")
        problem_count, show_answers = getInitialConfiguration()
    else:
        try:
            arranged_problems = arithmetic_arranger(user_problems, show_answers)
            print(arranged_problems)
            print("\n✅ Done! Enter more problems, type 'settings' to change configurations, or type 'quit' to exit.")
        except ValueError as ve:
            print(f"❌ Input error: {ve}")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
