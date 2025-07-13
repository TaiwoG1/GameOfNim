import sys
import math

def get_integer_input(prompt):
    """
    Prompts the user for an integer input and validates it.
    Continuously prompts until a valid integer is entered.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Input cannot be empty. Please enter a valid integer.")
                continue
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number (integer).")

def check_game_end(current_value, reduction_number, player_who_just_played):
    """
    Checks if the game should end based on the current number of stones.
    Returns True if the game ends, False otherwise.
    """
    if current_value <= 0:
        print(f"\n--- Game Over ---")
        print(f"The number of stones has reached {current_value} (0 or less).")
        print(f"{player_who_just_played} took the last stone. \n{player_who_just_played} Loses")
        return True
    elif current_value == 1:#current_value < reduction_number:
        print(f"\n--- Game Over ---")
        print(f"The number of stones has reached {current_value}.")#print(f"The number {current_value} is now less than the reduction amount ({reduction_number}).")
        print(f"{player_who_just_played} made the last move.\n{player_who_just_played}  Wins!")
        return True
    return False

def run_game_of_nim():
    """
    Runs the turn-based iterative reduction game.
    """
    print("--- Welcome to the Turn-Based Iterative Stone Reduction Game ---")
    print("Players (Computer and User) will take turns eliminating stones from a basket of stones")
    print("A minimum of 1 stones must be removed at each round")
    print("Only a certain maximum number of stones can be eliminated in one go, \"Reduction number\"")
    print("The game ends when the number of stones become 0 or 1")
    print("Whoever takes the last stone loses. \n(Pro-tip: Ensure you leave the last stone for your opponent)")
    print("-" * 60)

    initial_number = get_integer_input("Please enter the starting number of stones in the basket: ")
    if initial_number <= 0:
        print("The starting number of stones must be a positive integer. Exiting game.")
        return

    reduction_number = get_integer_input("Please enter the maximum reduction number of stones in one go: ")
    if reduction_number <= 0:
        print("The reduction number of stones must be a positive integer. Exiting game.")
        return
    if reduction_number > initial_number:
        print("The reduction number cannot be greater than the starting number of stones. Exiting game.")
        return

    current_value = initial_number
    turn_counter = 1
    print(f"\nGame Start: Total current number of stones = {initial_number}, Maximum Reduction Amount of stones = {reduction_number}")
    print(f"Current number of stones: {current_value}\n")

    while True:
        # --- Computer's Turn ---
        print(f"--- Turn {turn_counter} ---")
        print(f"Computer's Turn:")
        #computer_move = current_value - reduction_number
        #print(f"Computer performs: ({current_value} - {reduction_number}) = {computer_move}")
        computer_moving = (current_value-1)%(reduction_number+1)
        current_value = current_value - computer_moving
        print(f"Computer removes: ({computer_moving}) stones")
        

        print(f"Current number of stones after Computer's turn: {current_value}")
        if check_game_end(current_value, reduction_number, "Computer"):
            break

        # --- User's Turn ---
        print(f"\nUser's Turn:")
        print(f"The current number of stones is {current_value}\nThe maximum stones removable at a go is {reduction_number}")

        # For this turn-based game, the user removes any number of stones they deem fit
        # in order to NOT end up with the last stone

        while True:
            try:
                user_value = get_integer_input(f"How many stones would you like to remove(1-{reduction_number})? Enter your answer: ")
                if user_value <= reduction_number and user_value > 0:
                    # User's input is correct, proceed with the actual deduction
                    current_value = current_value - user_value
                    break
                else:
                    print("That's not in the appropriate range. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a whole number (integer).")

        print(f"Current number of stones after User's turn: {current_value}")
        if check_game_end(current_value, reduction_number, "User"):
            break

        turn_counter += 1
        print("-" * 50) # Separator for turns
        print("-" * 50) # Separator for turns

if __name__ == "__main__":
    run_game_of_nim()
