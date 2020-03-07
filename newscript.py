import os
import csv
import codecs

def readWordInBook(word, book):
    count = 0

    with codecs.open(book, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            for w in line.split():
                if(w == word):
                    count += 1
    f.close()
    return count

def word_list(genre,book):
    total_count = 0

    with open(genre) as f:
        datafile = f.readlines()

    for word in datafile:
        word = word.strip('\n')
        result = readWordInBook(word, book)
        total_count += result

    return total_count

def readtxtFile(txtFile, otherFile):
    '''Takes the two files that have the keys words
    outputs a dictinary with the the key being the book 
    and the value being an array with the total count 
    of the words that were found'''
    directory = os.fsencode(txtFile.rstrip('.txt'))
    array = [0, 0]
    Books = {}

    for file in os.listdir(directory):
        book = os.fsdecode(file)
        array[0] = word_list(txtFile, txtFile.strip('.txt')+ "/" + book)
        array[1] = word_list(otherFile, txtFile.strip('.txt')+ "/" + book)
        Books[book] = array
    return Books

def writetoCSVFile(dic, genreCSV):
    array = [0, 0]
    with open(genreCSV, 'w', newline='') as file:
        writer = csv.writer(file)
        for key in dic:
            array[0], array[1] = key, str(dic[key])
            writer.writerow(array)

if __name__ == "__main__": 
    #for the Romance Books
    resultForRomance = readtxtFile('Romance Books.txt', 'Horror Books.txt')
    writetoCSVFile(resultForRomance, 'Romance.csv')
    #for the Horror Books
    resultForHorror = readtxtFile('Horror Books.txt', 'Romance Books.txt')
    writetoCSVFile(resultForHorror, 'Horror.csv')