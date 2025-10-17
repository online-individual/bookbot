import sys
from stats import count_words
from stats import count_letters
from stats import sorted_letters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    pass

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    letter_count = count_letters(text)
    total_words = count_words(text)
    ordered_letters = sorted_letters(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for char_data in ordered_letters:
        print(f"{char_data['char']}: {char_data['num']}")
    print("============= END ===============")

main()
