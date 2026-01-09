import string

total_lines = 0
total_words = 0
freq = {}

with open("text.txt", "r", encoding="utf-8") as f:
    for line in f:
        total_lines += 1
        for word in line.split():
            word = word.strip(string.punctuation).lower()
            if word:
                total_words += 1
                freq[word] = freq.get(word, 0) + 1

with open("analysis.txt", "w", encoding="utf-8") as out:
    out.write(f"Total lines: {total_lines}\n")
    out.write(f"Total words: {total_words}\n")
    out.write("Word frequency:\n")
    for word in sorted(freq):
        out.write(f"{word}: {freq[word]}\n")