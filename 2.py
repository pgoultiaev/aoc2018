from util import readinput
from collections import Counter

input = readinput(2).read().split('\n')


def solve1(data):
    pairs = 0
    triples = 0
    for line in data:
        counts = list(Counter(line).values())
        if 2 in counts:
            pairs = pairs + 1
        if 3 in counts:
            triples = triples + 1
    return pairs * triples


def word_diff(word1, word2):
    diff_chars = [char for i, char in enumerate(word1) if word2[i] != char]
    return len(diff_chars)


def solve2(data):
    for word1 in data:
        for word2 in data:
            if word_diff(word1, word2) == 1:
                return ('').join(
                    [c for i, c in enumerate(word1) if word2[i] == c])


print(solve1(input))
print(solve2(input))
