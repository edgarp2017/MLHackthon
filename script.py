import os
total_count =0

def word_count(word,book):
    global total_count
    count = 0
    with open(book) as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        if word in line:
            count+=1
    f.close()
    total_count = total_count+count
    return str(count) # Because you finished the search without finding

def word_list(genre,book):
    with open(genre) as f:
        datafile = f.readlines()
    for word in datafile:
        word = word.rstrip('\n')
        #print(word)
        f_csv = genre.rstrip('.txt') #saves the csv file as the genre name from the list
        fw = open(f_csv+".csv","a") #opens file
        fw.write(book+"," + word + "," + word_count(word,book)+"\n")
        fw.close


#word_list('Romance.txt','Romance/1569-0.txt')


def Genre_Word_Count(genre):
    global total_count
    folder=genre.rstrip('.txt')
    directory = os.fsencode(folder)
    for file in os.listdir(directory):
        total_count = 0
        book = os.fsdecode(file)
        if book.endswith(".txt"): 
            word_list(genre,folder+"/"+book)
        fw = open(folder+".csv","a") #opens file
        fw.write(book+"," + "Total Count of "+folder+" words," + str(total_count)+"\n")
        fw.write(",,\n")
        fw.close


Genre_Word_Count('Romance.txt') # Name of the file with word list, creat a folder with the same name as word list and put books