import sys
from stats import get_num_words,get_num_letters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text) 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_letters = get_num_letters(text)
    for letter,count in num_letters.items():
        print(f"{letter}: {count}")
    print("============ END ============")


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()


