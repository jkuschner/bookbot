import sys
from stats import word_count, character_count, sorted_chars

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def print_report(path):
    book_text = get_book_text(path)
    char_counts = character_count(book_text)
    sorted = sorted_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    for count in sorted:
        if count['char'].isalpha():
            print(f"{count['char']}: {count['num']}")
    print("============= END ===============")
    

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1])
    

main()