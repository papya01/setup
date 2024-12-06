def fibonacci_up_to_value(max_value):

    if max_value < 0:
        return []

    fib_series = [0, 1]
    while fib_series[-1] + fib_series[-2] <= max_value:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

try:
    print("Choose an option:")
    print("1. Generate Fibonacci series up to a specific number of terms.")
    print("2. Generate Fibonacci series up to a specific maximum value.")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        num_terms = int(input("Enter the number of terms: "))
        if num_terms > 0:
            print("Please enter a  integer.")
        else:
            series = fibonacci_up_to_terms(num_terms)
            print(f"Fibonacci series with {num_terms} terms: {series}")

    elif choice == 2:
        max_value = int(input("Enter the maximum value: "))
        if max_value < 0:
            print("Please enter a non-negative value.")
        else:
            series = fibonacci_up_to_value(max_value)
            print(f"Fibonacci series up to {max_value}: {series}")
    else:
        print("Invalid choice! Please choose 1 or 2.")

except ValueError:
    print("Invalid input! Please enter an integer.")

