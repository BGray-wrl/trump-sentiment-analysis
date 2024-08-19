from collections import defaultdict
import operator
import re

def count_words_in_file(filename):
    word_count = defaultdict(int)
    
    with open(filename, 'r') as file:
        text = file.read()
        
        # Use regular expression to split the text into words based on spaces, newlines, commas, and hyphens
        words = re.split(r'[ \n,-?]+', text)
        
        for word in words:
            if word:  # Check if the word is not empty
                word_count[word.lower()] += 1  # Convert to lowercase for case-insensitive counting
    
    return dict(word_count)

def print_top_words(word_count, top_n=50):
    # Sort the word count dictionary by values (frequency) in descending order
    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    
    # Print the top N words
    for word, count in sorted_word_count[:top_n]:
        print(f'{word}: {count}')

def return_top_words(word_count, top_n=2000):
    # Sort the word count dictionary by values (frequency) in descending order
    sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    

    list = []
    # Print the top N words
    for word, count in sorted_word_count[:top_n]:
        if count>=8:
            list.append(word)
    return(list)

# Count words in the file
word_counts_old = count_words_in_file('text_old.txt')
word_counts_conv = count_words_in_file('text_new.txt')

top_100_old=return_top_words(word_counts_old,2000)
top_100_new=return_top_words(word_counts_conv,2000)


# print(top_100_old)

for word in top_100_new:
    if word not in top_100_old:
        print(word)

print("\n and old: \n")
for word in top_100_old:
    if word not in top_100_new:
        print(word)

print(len(word_counts_old))


# return_top_words(word_counts_old)
# print(return_top_words(word_counts_old,50))

# # Print the top 50 words
# print_top_words(word_counts, top_n=100)
