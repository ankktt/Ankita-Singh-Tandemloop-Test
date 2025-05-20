a = int(input("Enter a number: "))

# Initialize a counter to track how many odd numbers have been printed
count = 0

# Start with the first odd number
num = 1

# Loop until we've printed 'a' odd numbers
while count < a:
    # Print the current odd number without moving to a new line
    print(num, end="")

    # Increment the counter
    count += 1

    # Prepare the next odd number (odd numbers increase by 2)
    num += 2

    # Print a comma and space only if it's not the last number
    if count < a:
        print(", ", end="")
