fname = input("Enter file name: ")
fh = open(fname)
cnt = 0
value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    cnt = cnt + 1
    i = line.find(':')
    num = float(line[i+2:])
    value += num
ave = value / cnt
print("Average spam confidence:", ave)