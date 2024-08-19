from collections import defaultdict
import operator
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords from nltk
nltk.download('stopwords')

# Load the English stopwords list
stop_words = stopwords.words('english')
print(stop_words)

def count_words_in_file(filename):
    word_count = defaultdict(int)
    
    with open(filename, 'r') as file:
        text = file.read()
        
        # Use regular expression to split the text into words based on spaces, newlines, commas, and question marks
        words = re.split(r'[ \n,?.]+', text)
        
        for word in words:
            if word=="we":
                print(word)
                print('we' in stop_words)
                print(word not in stop_words)
            if word:  # Check if the word is not empty
                if word.lower() not in stop_words:
                    word_count[word.lower()] += 1  # Convert to lowercase for case-insensitive counting
    
    return dict(word_count)

def compare_word_counts(new_count, old_count):
    word_diff = {}
    
    all_words = set(new_count.keys()).union(set(old_count.keys()))
    
    for word in all_words:
        new_freq = new_count.get(word, 0)
        old_freq = old_count.get(word, 0)
        diff = new_freq - old_freq
        word_diff[word] = diff
    
    return word_diff

def return_sorted_words(word_diff):
    # Sort the word difference dictionary by absolute values of the differences in descending order
    sorted_word_diff = sorted(word_diff.items(), key=lambda item: abs(item[1]), reverse=True)
    
    words=[]
    wordscount=[]

    # Print the sorted words with their differences
    for word, count in sorted_word_diff:
        words.append(word)
        wordscount.append(word+": "+str(count))

        # print(str(word,": ",diff))

    return(words,wordscount)


# Count words in both files
new_word_counts = count_words_in_file('text_new.txt')
old_word_counts = count_words_in_file('text_old.txt')


sorted_new,sorted_newcount=return_sorted_words(new_word_counts)
sorted_old,sorted_oldcount=return_sorted_words(old_word_counts)


print("")
print("NEW SPEECH")
print(sorted_newcount[1:20])
print("OLD SPEECH")
print(sorted_oldcount[1:20])


# sorted_new_filtered=[]
# for i in range(len(sorted_new)):
#     if sorted_new[i] not in sorted_old:
#         sorted_new_filtered.append(sorted_newcount[i])

# sorted_old_filtered=[]
# for i in range(len(sorted_old)):
#     if sorted_old[i] not in sorted_new:
#         sorted_old_filtered.append(sorted_oldcount[i])

print("")
print("")
print("")
print("")

# print(sorted_new_filtered[1:20])
# print("")
# print(sorted_old_filtered[1:20])


print(("we" in stop_words))


