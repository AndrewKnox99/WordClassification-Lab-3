"""
Andrew Knox
CSC 391 - Data Mining
Lab 3 - Word Classification

Keyword extraction: USE RAKE ALGORITHM, from nltk (natural language tool kit)

"""

import re

#Retrieved from StackOverflow: https://stackoverflow.com/questions/46759492/syllable-count-in-python
#Takes in a single word string, not a sentence, and returns the syllable count of the string
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

#Method returns the Flesch reading ease score of a passage
#Params: syllableCount -> Number of syllables in passage
#        wordCount     -> Number of words in passage
#        sentenceCount -> Number of sentences in passage
def fleschEaseScore(sentenceCount, wordCount, syllableCount):
    score = 206.835 - 1.015 * (wordCount/sentenceCount) - 84.6 * (syllableCount/wordCount)
    return score

#Takes in a long string passage, then returns a tuple containg:
#[Sentence count, word count, syllable count] for the passage
def getValuesForFleshScore(longInput):
    sentenceCount, wordCount, syllableCount = 0, 0, 0
    longInput = re.split(' |\n', longInput)
    for word in longInput:
        if word.endswith('.'):
            sentenceCount += 1
        wordCount += 1
        syllableCount += syllable_count(word)
    return (sentenceCount, wordCount, syllableCount)
