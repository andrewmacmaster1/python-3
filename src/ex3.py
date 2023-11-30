
def count_words(file):
    words = []
    with open(file) as f:
        for row in f:
            row = row.split()
            words.extend(row)
    l = open("files\large-words.txt", "a")
    s = open("files\small-words.txt", "a")   
    for word in set(words):
        if len(word) >= 3:
            destination = l
        else:
            destination = s
        print(word, file=destination)

    return len(set(words))



def ex3():
    total_words = count_words("files\words.txt")
    print(f"Total words: {total_words}.")

ex3()