def is_palindrome(input_str):\

    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = ''.join(input_str.split()).lower()

    # Compare the string with its reverse
    return cleaned_str == cleaned_str[::-1]

if __name__ == "__main__":
    # Prompt the user to enter a string
    user_input = input("Enter a string: ")

    # Check if the input string is a palindrome
    if is_palindrome(user_input):
        print(f"The string '{user_input}' is a palindrome.")
    else:
        print(f"The string '{user_input}' is not a palindrome.")