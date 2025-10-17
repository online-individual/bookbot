def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_letters(text):
    convert_to_lowercase = text.lower()
    counts = {}
    for ch in convert_to_lowercase:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_on(counts):
    return counts["num"]

def sorted_letters(counts):
    dicts_sorted = []
    for char, num in counts.items():
        if char.isalpha():
            dicts_sorted.append({"char": char, "num": num})
    dicts_sorted.sort(reverse = True, key = sort_on)
    return dicts_sorted
