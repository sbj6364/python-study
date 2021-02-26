fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
cnt = 0
lst = list()
address = list()

for line in fh:
    line = line.rstrip()
    lst = line.split()
    if len(lst) < 3 or lst[0] != "From":
        continue
    address.append(lst[1])
    cnt += 1
for i in address:
    print(i)
print("There were", cnt, "lines in the file with From as the first word")