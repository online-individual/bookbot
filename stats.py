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
