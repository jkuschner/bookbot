def word_count(text):
    return len(text.split())

def character_count(text):
    lower_text = text.lower()
    char_counts = {}
    for c in lower_text:
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] += 1
    return char_counts

def sort_on(counts):
    return counts["num"]

def sorted_chars(char_counts):
    sorted = []
    for char in char_counts:
        sorted.append({"char": char, "num": char_counts[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
