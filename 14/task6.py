def longest_words(file):
    with open(file, encoding = 'utf-8') as f:
        words = f.read().split()
    l_word = max(words, key = len)
    l_words = [word for word in words if len(word)==len(l_word)]
    return l_words[0] if len(l_words) == 1 else l_words
