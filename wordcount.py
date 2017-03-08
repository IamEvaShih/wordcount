import fileinput
from collections import Counter
from nltk import word_tokenize, pos_tag

if __name__ == '__main__':
    wordCounter = Counter()
    for line in fileinput.input():
        words = word_tokenize(line.strip())
        wordCounter.update(words)

    for word, count in wordCounter.most_common(20):
        print("%s: %d" % (word, count))
