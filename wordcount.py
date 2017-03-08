import fileinput
from collections import Counter
from nltk import word_tokenize
import string

if __name__ == '__main__':
    wordCounter = Counter()
    for line in fileinput.input():
        words = word_tokenize(line.strip())
        wordCounter.update(word for word in words if word not in string.punctuation)

    for word, count in wordCounter.most_common(20):
        print("%s: %d" % (word, count))
