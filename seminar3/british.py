import os
import re
import random
import argparse


def shuffle(text, is_shuffle=True):
    def get_modified_word(word: list, is_shuffle: bool) -> list:
        tmp = word[1:-1]

        if is_shuffle:
            random.shuffle(tmp)
        else:
            tmp = sorted(tmp)

        word[1:-1] = tmp
        return word

    pattern = '[\w\d-]+'

    res = list(text)
    for m in re.finditer(pattern, text):
        res[m.start():m.end()] = get_modified_word(list(text[m.start():m.end()]), is_shuffle)

    return ''.join(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text')
    parser.add_argument('--is_shuffle', type=bool)
    parser.add_argument('--filename')
    args = parser.parse_args()

    if args.filename and os.path.exists(args.filename):
        text, is_shuffle = 'Привет, Рустам', True
    else:
        text, is_shuffle = args.text, args.is_shuffle

    print(shuffle(text, is_shuffle))
