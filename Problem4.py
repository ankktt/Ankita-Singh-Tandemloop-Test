# List of numbers to be checked
nums = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Create an empty dictionary to store the result
result = {}

# Start checking for multiples from 1 to 9
i = 1
while i <= 9:
    count = 0  # Initialize counter for each i

    # Manually loop through all numbers in the list
    j = 0
    while j < len(nums):
        if nums[j] % i == 0:
            count += 1
        j += 1

    # Store the count in the dictionary
    result[i] = count
    i += 1  # Move to the next number from 1 to 9

# Print the final dictionary
print(result)
