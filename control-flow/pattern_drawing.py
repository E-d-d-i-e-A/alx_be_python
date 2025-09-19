# Drawing Patterns with Nested Loops
# This program draws a square pattern using nested loops

def main():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Draw the pattern using while loop and for loop
    row = 0
    while row < size:
        # Use for loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        
        # Print newline after each row
        print()
        
        # Move to next row
        row += 1

if __name__ == "__main__":
    main()
