from generator import UsernameGenerator

def get_yes_no_input(prompt):
    """Gets a simple 'y' or 'n' answer from the user."""
    while True:
        choice = input(f"{prompt} (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def get_number_of_usernames():
    """Gets the number of usernames to generate from the user."""
    while True:
        try:
            num = int(input("How many usernames would you like to generate? "))
            if num > 0:
                return num
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_menu():
    """Displays the main menu of generation options."""
    print("\n" + "="*30)
    print("  Powerful Username Generator")
    print("="*30)
    print("1. Generate 'Adjective + Noun' usernames (e.g., SilentPhoenix)")
    print("2. Generate 'Gamer' usernames (e.g., xX_Gamer_Xx)")
    print("3. Exit")
    print("-"*30)
    while True:
        choice = input("Choose a style (1-3): ")
        if choice in ['1', '2', '3']:
            return choice
        print("Invalid choice. Please select a valid option.")

def main():
    """Main function to run the username generator application."""
    gen = UsernameGenerator()
    
    # Check if word lists were loaded successfully
    if not all([gen.adjectives, gen.nouns, gen.prefixes, gen.suffixes]):
        print("\nCould not start the generator because one or more word lists are empty or missing.")
        print("Please check the 'data' directory and its files.")
        return

    while True:
        choice = display_menu()

        if choice == '3':
            print("Goodbye!")
            break

        # Get user preferences for generation
        num_to_generate = get_number_of_usernames()
        add_nums = get_yes_no_input("Add random numbers to the end?")
        use_separator = get_yes_no_input("Use underscore '_' as a separator?")
        use_leet = get_yes_no_input("Convert to 1337 (leet) speak?")
        
        print("\n--- Generated Usernames ---")
        for _ in range(num_to_generate):
            if choice == '1':
                username = gen.generate_adj_noun(add_nums, use_leet, use_separator)
            elif choice == '2':
                username = gen.generate_gamer_tag(add_nums, use_leet, use_separator)
            
            print(username)
        print("---------------------------\n")
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()