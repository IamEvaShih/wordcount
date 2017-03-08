import fileinput
from collections import Counter

if __name__ == '__main__':
    wordCounter = Counter()
    for line in fileinput.input():
        words = line.strip().split()
        wordCounter.update(words)

    for word, count in wordCounter.most_common(20):
        print("%s: %d" % (word, count))
