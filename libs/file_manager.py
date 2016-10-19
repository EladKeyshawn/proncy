# get proper text from file and simply prepare for analysis

import word_analyzer
import sys


def translate_words(words):
    translated_words = []
    print words
    for word in words:
        # word = str(word)
        # word = word.lower
        word = str(word).lower()
        word = word.replace('\'', '')
        trans_word = word_analyzer.start_analyzing(word)
        translated_words.append(trans_word)

    # translated_words = repr([x.encode(sys.stdout.encoding) for x in translated_words]).decode('string-escape')
    print words
    for word in translated_words:
        print word

    return translated_words


def get_data_from_txt(filename):
    translated_contents = []
    with open(filename) as f:
        contents = f.readlines()  # contents is list of strings containing lines
        print contents

        for line in contents:
            words = line[: -1].split()  # words is list of strings containing seperate words
            trans_words = translate_words(words)  # passing our words for translation getting translated version
            space = " "
            trans_line = space.join(trans_words)
            translated_contents.append(trans_line)

    print translated_contents
    return translated_contents


def test_file_manager():
    filename = "files/example.txt"
    translated_contents = get_data_from_txt(filename)


test_file_manager()
