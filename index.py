import os
import requests, json, csv
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
from deep_translator import GoogleTranslator

# # crie um programa que leia data.csv e exiba seu índice e conteúdo na tela
# # dica: use enumerate()
# # dica: use open() e .readlines()
# # dica: use print() e .format()
# # dica: use for
# # dica: use split()


def translate(string):
    return GoogleTranslator(source='auto', target='en').translate(string)



# Write a function to summarize a array of strings using nltk
def summarize(string):
    # get the first 3 words of the summary
    first_words = string.split(' ')[:5]
    summary = ' '.join(first_words).replace(' ', '_').replace(',', '-')
    return summary


def writeFiles(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='\n')
        for i, row in enumerate(reader):

            print(row)
            translated = translate(row[0])
            filename = summarize(translated)

            if len(filename) == 0:
                return

            title = translated.split('.')
            title.pop(0)

            with open('./generated/{}.py'.format(filename), 'w') as f2:
                f2.write('# {}'.format(''.join(title)))
                f2.close()
            i += 1


def countFiles():
    return len(os.listdir('./generated'))

if __name__ == '__main__':
    writeFiles('./data/index.csv')
    print(countFiles())

       


