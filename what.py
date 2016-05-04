fname = raw_input("Enter file name: ")
fh = open(fname)
ls = list()
for line in fh:
    list_of_words = line.split()
    for word in list_of_words:
        if word not in ls:
            ls.append(word)
ls.sort()
print ls
