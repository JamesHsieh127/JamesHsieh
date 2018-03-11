name = raw_input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    if line.startswith ("From "):
        time = line.split()[5].split(":")
        count[time[0]] = count.get(time[0], 0)+1
        #print(count[time])

lst = list()
for key, value in count.items():
    lst.append((key, value))
lst.sort()

for hours, counts in lst:
    print(hours, counts)
