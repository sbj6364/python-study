text = "X-DSPAM-Confidence: 0.8475"

pos = text.find(':')
value = float(text[pos+2:])
print(value)