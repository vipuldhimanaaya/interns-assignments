import difflib
# making a func to read the file using with so that we don't need to use close()
def read_word_file(file_path):
    with open(file_path, 'r') as file:
        return [word.strip() for word in file]

# function to compare two lists of words and print out differences
def approximate_search(query, word_list, k=3):
    suggestions = difflib.get_close_matches(query, word_list, n=k, cutoff=0.4)
    return suggestions



def main():
    file_path = "D:\CODING WORK\Language (python)\Fundamentals\Projects\WordsSuggestions.py\word_list.txt" 
    word_list = read_word_file(file_path)


    while True:
        user_input = input("Input >> ").strip().lower()

        if not user_input:
            break

        suggestions = approximate_search(user_input, word_list)

        if suggestions:
            print("Output >>", ', '.join(suggestions))
        else:
            print("No suggestions found.")

if __name__ == "__main__":
    main()


