def determine_age_category():
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative.")
        elif age < 13:
            print("You are a child.")
        elif 13 <= age < 20:
            print("You are a teenager.")
        elif 20 <= age < 60:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    
    except ValueError:
        print("Please enter a valid number.")

# Run the function
determine_age_category()