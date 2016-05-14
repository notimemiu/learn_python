name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith('From '):
        t = line.split()
        sender = t[1]
        counts[sender] = counts.get(sender,0) + 1

bigcount = None
bigsender = None
for sender,count in counts.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        bigsender = sender

print bigsender, bigcount
