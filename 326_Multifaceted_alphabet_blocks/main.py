import time
import sys


def get_histogram(word_list, blocks):
    # dictionary containing letters and their count
    histogram = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    for word in word_list:
        b = blocks[:]
        found = False
        for letter in word:
            for block in b:
                if letter in block:
                    found = True
                    break
            if found:
                b.remove(block)
                found = False
            else:
                histogram[letter] += 1
    return histogram


def best_letters(word_list, excludes=[]):
    hist = get_histogram(word_list, excludes)
    sorted_hist = sorted(hist, key=hist.get, reverse=True)
    print("Remaining: %d" % hist[sorted_hist[0]])
    if hist[sorted_hist[0]] == 0:
        return None
    else:
        return sorted_hist


def find_new_block(word_list, blocks=[]):
    if blocks == []:
        best = best_letters(word_list)
        return [best[0]]
    else:
        N = len(blocks)
        best = best_letters(word_list, blocks)
        if best:
            lim = N + 1
            return best[0:lim]


def main(filename):
    print("Input file is %s" % filename)
    with open(filename, "r") as file:
        word_list = file.read().split("\r\n")

    max_word = ""
    for word in word_list:
        if len(word) > len(max_word):
            max_word = word
    print(
        "Read input data. Longest word is %s (%d letters)" % (max_word, len(max_word))
    )

    blocks = []
    start = time.time()
    new_block = find_new_block(word_list)
    while new_block:
        blocks.append(new_block)
        new_block = find_new_block(word_list, blocks)
    end = time.time()
    print("Found %d blocks in %f seconds." % (len(blocks), end - start))
    with open("solution.txt", "w") as file:
        for block in blocks:
            file.write("".join(block) + "\r\n")


if __name__ == "__main__":
    main(sys.argv[1])
