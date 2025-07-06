def check_even_odd():
    numbers = []

    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Number {i+1}: "))
        numbers.append(num)

    print("\nResults:")
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")

# Run it
check_even_odd()