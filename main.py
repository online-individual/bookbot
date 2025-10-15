def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    total_words = count_words(text)
    print(f"Found {total_words} total words.")

main()
