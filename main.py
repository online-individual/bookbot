from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    total_words = count_words(text)
    print(f"Found {total_words} total words.")

main()
