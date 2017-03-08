import fileinput
from collections import defaultdict, Counter
from nltk import word_tokenize, pos_tag
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
    posWordCounter = defaultdict(Counter)
    for line in fileinput.input():
        words = word_tokenize(line.strip().lower())
        wordsWithPos = pos_tag(words)
        for word, pos in wordsWithPos:
            if word_is_valid(word):
                posWordCounter[pos][word] += 1

    for pos, wordCounter in posWordCounter.items():
        print("{}:".format(pos))
        for word, count in wordCounter.most_common(5):
            print("%s: %d" % (word, count), end=' ')
        print()
        print()
