import re

text = 'Hello World!'
text = text.lower()
reg = re.compile('[^a-zA-Z ]')
print(reg.sub('', text))

dict = {}
for let in text:
    if dict.setdefault(let):
        dict[let] = dict.setdefault(let) + 1
    else:
        dict[let] = 1
print(dict)
max = 0
for k in dict.values():
    if k > max:
        max = k
new_dict = {}
for i, k in dict.items():
    if (k == max):# and i.isalpha():
        new_dict[i] = k
l = list(new_dict.keys())
l.sort()
print(l[0])
