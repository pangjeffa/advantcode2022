

import re

with open("./input2.txt", "r") as f:
    sacks = [val -38 if val < 97 else val -96 for val in (ord(set(x).intersection(set(y),set(z)).pop()) for x,y,z in (res.split('\n') for res in re.findall('([a-zA-Z]+\n[a-zA-Z]+\n[a-zA-Z]+)',f.read())))]


print(sum(sacks))