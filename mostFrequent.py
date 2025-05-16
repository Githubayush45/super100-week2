def most_frequent(numbers):
    max_count = 0  # Highest count found so far
    most_common = numbers[0]  # Start with the first number as most common

    # Go through each number in the list
    for num in numbers:
        count = numbers.count(num)  # Count how many times this number appears

        # If this number appears more than the previous max, update it
        if count > max_count:
            max_count = count
            most_common = num

    return most_common  # Return the number that appeared the most

# Test the function
print(most_frequent([1, 2, 2, 3, 3, 3]))  # 3 appears most frequently
