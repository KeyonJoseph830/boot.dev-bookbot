
def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    counts = {}
    for char in text.lower():
      counts[char] = counts.get(char,0) + 1
    return counts
