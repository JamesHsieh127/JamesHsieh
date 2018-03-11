name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
sender = dict()

for line in handle:
    if not line.startswith("From:"):continue
    #line = line.rstrip()
    #print (line)
    words = line.split()
    #print (words)
    mail = words[1]
    sender[mail] = sender.get(mail, 0) +1

bigcount = None
bigword = None
for key, value in sender.items():
    if (bigcount == None) or (value > bigcount):
        bigcount = value
        bigword = key
print(bigword, bigcount)
