"""
a dictionary where the keys are the words and the values
are the number of times each word appears in the list.

UNDERSTAND:
>> input: list of string
>> output: dictionary <string, int>

happy case:
>> input: words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
>> output: {'apple': 3, 'banana': 2, 'orange': 1}

edge cases:
>> empty list --> return empty dictionary
>> list of not strings

runtime and space expectations:
>> none

PLAN:
1. create a dictionary called counts
2. iterate through the list of words
3. update the value at the current key/word
   3a. get the value at key/word
   3b. if it exists, insert value + 1
   3c. else insert 1
4. return dictionary
"""

# IMPLEMENT
def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

        # if word in counts:
        #     counts[word] += 1
        # else:
        #     counts[word] = 1

    return counts


words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(count_words(words))