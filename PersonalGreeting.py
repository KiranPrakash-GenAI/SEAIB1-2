def personal_greeting():
    # Ask user for input
    name = input("What's your name? ")
    age = input("How old are you? ")
    color = input("What's your favorite color? ")

    # Create personalized message
    message = (
        f"\nHello, {name}! 👋\n"
        f"Wow, {age} years old and already making moves!\n"
        f"{color.capitalize()} is a beautiful color — great choice!\n"
        f"Hope you have a colorful and amazing day ahead! 🌈"
    )

    # Display the message
    print(message)

# Run the function
if __name__ == "__main__":
    personal_greeting()