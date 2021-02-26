fname = input("Enter file name: ")
fh = open(fname)

words = list()
ans = list()
for line in fh:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)

    for word in words:
        if word in ans:
            continue
        ans.append(word)
ans = sorted(ans)
print(ans)

