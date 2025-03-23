from stats import print_num_words
from stats import get_num_chars
from stats import print_sorted_list
import sys

def get_book_text(path_to_file):
    file_contents = None

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(sys.argv[1])
    char_dict = get_num_chars(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print_num_words(content)
    print("--------- Character Count -------")
    print_sorted_list(char_dict)
    print("============= END ===============")

main()