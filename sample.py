import os

# --- Basic Arithmetic Functions ---
def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides two numbers, handles division by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# --- String Manipulation Functions ---
def reverse_string(s):
    """Reverses a given string."""
    return s[::-1]

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]

# --- List Operations Functions ---
def find_max(numbers):
    """Finds the maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    """Finds the minimum number in a list."""
    if not numbers:
        return None
    return min(numbers)

def sum_list(numbers):
    """Calculates the sum of numbers in a list."""
    return sum(numbers)

# --- File Handling Functions ---
def write_to_file(filename, content):
    """Writes content to a specified file."""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return f"Content written to {filename}"
    except IOError as e:
        return f"Error writing to file: {e}"

def read_from_file(filename):
    """Reads content from a specified file."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except IOError as e:
        return f"Error reading from file: {e}"

# --- Main execution block ---
if __name__ == "__main__":
    print("--- Arithmetic Operations ---")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"12 / 3 = {divide(12, 3)}")
    print(f"10 / 0 = {divide(10, 0)}")

    print("\n--- String Operations ---")
    my_string = "Hello World"
    print(f"Original string: '{my_string}'")
    print(f"Reversed string: '{reverse_string(my_string)}'")
    print(f"'Madam' is a palindrome: {is_palindrome('Madam')}")
    print(f"'Python' is a palindrome: {is_palindrome('Python')}")

    print("\n--- List Operations ---")
    my_list = [10, 5, 20, 15, 8]
    print(f"List: {my_list}")
    print(f"Maximum: {find_max(my_list)}")
    print(f"Minimum: {find_min(my_list)}")
    print(f"Sum: {sum_list(my_list)}")

    print("\n--- File Operations ---")
    test_filename = "test_data.txt"
    file_content = "This is a test line.\nAnother line of text."
    print(write_to_file(test_filename, file_content))
    print(f"Content of '{test_filename}':\n{read_from_file(test_filename)}")

    # Clean up the created file
    if os.path.exists(test_filename):
        os.remove(test_filename)
        print(f"Cleaned up: '{test_filename}' removed.")
