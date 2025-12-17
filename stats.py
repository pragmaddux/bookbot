def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())
    print(f"Found {num_words} total words")

def get_num_letters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    num_letters = {}
    for char in file_contents:
        char_lower = char.lower()
        if char_lower.isalpha():
            if char_lower not in num_letters:
                num_letters[char_lower] = 1
            else:
                num_letters[char_lower] += 1
    return num_letters

def sort_char_counts(counts_dict):
    """
    Takes a dictionary of characters and their counts and returns a sorted list of dictionaries.
    """
    # Convert the dictionary items into a list of tuples (char, count)
    items_list = list(counts_dict.items())

    # Sort the list of tuples based on the count (the second element of the tuple)
    # The 'key=lambda x: x[1]' sorts by the second element, and 'reverse=True' sorts in descending order
    sorted_items = sorted(items_list, key=lambda x: x[1], reverse=True)

    # Convert the sorted list of tuples into the desired list of dictionaries
    sorted_list_of_dicts = [{"char": char, "num": count} for char, count in sorted_items]

    return sorted_list_of_dicts

def return_sorted(filepath):
    num_words = get_num_words(filepath)
    char_counts = get_num_letters(filepath)
    sorted_list_of_chars = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list_of_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("================ END ================")