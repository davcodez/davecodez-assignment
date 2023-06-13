def build_pyramid(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        asterisks = '*' * (2 * i + 1)
        print(spaces + asterisks)

# Prompt the user for the height of the pyramid
height = int(input("Enter the height of the pyramid: "))

# Build the pyramid
build_pyramid(height)
