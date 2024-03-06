from colorama import init, Fore, Back, Style
import time

# Initialize colorama to support ANSI escape sequences on Windows
init()

def colorful_menu(options):
    print(Style.BRIGHT + "Choose an option:")
    for i, option in enumerate(options, start=1):
        print(Fore.GREEN + f"{i}. {option}")
    print(Style.RESET_ALL)

def loading_spinner(duration):
    for _ in range(duration):
        for color in [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]:
            print(color + "Loading... ", end="\r")
            time.sleep(0.2)
    print(Style.RESET_ALL)

def get_user_input(prompt):
    print(Fore.BLUE + prompt)
    user_input = input(Style.RESET_ALL)
    return user_input

def display_error(message):
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "Error: " + message)
    print(Style.RESET_ALL)

def main():
    options = ["Option 1", "Option 2", "Option 3"]
    colorful_menu(options)
    
    try:
        choice = int(get_user_input("Enter your choice: "))
        if choice < 1 or choice > len(options):
            raise ValueError("Invalid choice. Please select a valid option.")
        
        print(Fore.GREEN + f"You've chosen: {options[choice-1]}")
    except ValueError as e:
        display_error(str(e))

    loading_spinner(3)

if __name__ == "__main__":
    main()