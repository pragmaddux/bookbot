import sys
from stats import get_num_words, get_num_letters, return_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)

def main():
    #return_sorted("./books/frankenstein.txt")
    if (len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    return_sorted(filepath)

main()
