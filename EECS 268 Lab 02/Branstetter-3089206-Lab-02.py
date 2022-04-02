'''
Author: Clayton Branstetter
KUID: 3089206
Date: 02/07/2022
Lab: lab#02
Last modified: 02/12/2022
Purpose: Moby Dick
'''


def build_count(text):
    # put all the words in a list
    lines = text.split('\n')
    text_words = []
    for line in lines:
        text_words += line.split()
    # clean words
    cleaned_words = [clean_word(word) for word in text_words]
    # dictionary word:occurrence
    dict_words = {}
    # update occurrences of each word
    for word in cleaned_words:
        if word not in dict_words:
            dict_words[word] = 1
        else:
            dict_words[word] += 1
    return dict_words


def clean_word(word):
    # list characters to remove
    l = ['!', '?', ':', ';', ',', '|', '.', '--', ' ', '"']
    # convert word to lower-case
    cl_word = word.lower()
    for element in l:
        while element in cl_word:
            cl_word = cl_word.replace(element, '')
        if "'" in cl_word:
            if cl_word[0] == "'":
                cl_word.replace("'", '')
            if cl_word[-1] == "'":
                cl_word.replace("'", "")
    return cl_word


def unique_words(word_counts):
    list_words = []
    for element in word_counts:
        if word_counts[element] == 1:
            list_words.append(element)
    return list_words


def main():
    print('===========Welcome to the word counter!===========')
    file = input('Enter a file name: ')

    with open(file) as input_text:  # open the input file
        dict_text = build_count(input_text.read())
    print(f'The file {file} has been processed.')

    with open('word_data.txt', 'w') as wd:  # create word_data.txt file
        for word, count in dict_text.items():
            wd.write(word+'\t'+str(count)+'\n')

    with open('unique_data.txt', 'w') as ud:  # create unique_data.txt file
        unique_w = unique_words(dict_text)
        ud.write('\n'.join(unique_w))
    print('Output stored in word_data.txt and unique_words.txt')
    print('Exiting...')


main()
