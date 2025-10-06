import sys
from stats import get_total_words, get_char_count, sorted_dict

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        content = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")
        sys.exit(1)

    num_words = get_total_words(content)
    char_dict = get_char_count(content)
    sorted_list = sorted_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
