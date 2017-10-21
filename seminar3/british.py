import os
import re
import random
import argparse
import codecs


def shuffle(text, is_shuffle=True):
    def get_modified_word(word: list, is_shuffle: bool) -> list:
        tmp = word[1:-1]

        if is_shuffle:
            random.shuffle(tmp)
        else:
            tmp = sorted(tmp)

        word[1:-1] = tmp
        return word

    pattern = r'[\w\d-]+'

    res = list(text)
    for m in re.finditer(pattern, text):
        res[m.start():m.end()] = get_modified_word(list(text[m.start():m.end()]), is_shuffle)

    return ''.join(res)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text')
    parser.add_argument('-is', '--is_shuffle', type=bool)
    parser.add_argument('-f', '--filename')
    args = parser.parse_args()

    if args.filename and os.path.exists(args.filename):
        text = codecs.open(args.filename, encoding='utf-8').read()
    else:
        text, is_shuffle = args.text, args.is_shuffle

    is_shuffle = args.is_shuffle

    print(shuffle(text, is_shuffle))
