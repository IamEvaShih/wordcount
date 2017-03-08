import fileinput
from collections import Counter
from nltk import word_tokenize
import string
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))
stopwords.update(string.punctuation)


def word_is_valid(word):
    if word in stopwords:
        return False
    if word.isalnum():
        return True
    if all(char in string.punctuation for char in word):
        return False
    return True


if __name__ == '__main__':
    wordCounter = Counter()
    for line in fileinput.input():
        words = word_tokenize(line.strip().lower())
        wordCounter.update(filter(word_is_valid, words))

    for word, count in wordCounter.most_common(20):
        print("%s: %d" % (word, count))
