import re
from collections import Counter

def clean_text(text):
    return re.findall(r'\b\w+\b', text.lower())

def get_word_frequencies(filename):
    word_counts = Counter()
    total_words = 0
    with open(filename, 'r') as file:
        for line in file:
            words = clean_text(line)
            word_counts.update(words)
            total_words += len(words)
    return word_counts, total_words

def display_and_save_report(word_counts, total_words, report_filename, top_n):
    top_words = word_counts.most_common(top_n)

    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        print(f"{word} - {count} {'time' if count == 1 else 'times'}")
        
    with open(report_filename, 'w') as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")

filename = "sample.txt"
report_filename = "word_count_report.txt"

user_input = input("Enter the paragraph:\n")
with open(filename, 'w') as file:
    file.write(user_input)

try:
    top_n = int(input("How many top common words do you want to display? "))
except ValueError:
    print("Invalid number. Defaulting to top 5.")
    top_n = 5

word_counts, total_words = get_word_frequencies(filename)
display_and_save_report(word_counts, total_words, report_filename, top_n)

