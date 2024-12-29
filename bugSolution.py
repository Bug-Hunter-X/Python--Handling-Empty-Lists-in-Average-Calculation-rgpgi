def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")  # Raise exception for clarity
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

try:
    my_numbers = []
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")

my_numbers = [10, 20, 0, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}") 