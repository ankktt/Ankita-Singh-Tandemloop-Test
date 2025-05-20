# Prompt the user to enter a number
a = int(input("Enter a number: "))

# If input is even, subtract 1 to make it odd; otherwise, keep as is
if a % 2 == 0:
    limit = a - 1
else:
    limit = a

# Initialize counter and first odd number
count = 0
num = 1

# Loop until we print 'limit' odd numbers
while count < limit:
    # Print the current odd number
    print(num, end="")

    # Increase counter
    count += 1

    # Add comma and space after the number, unless it's the last one
    if count < limit:
        print(", ", end="")

    # Prepare next odd number
    num += 2
