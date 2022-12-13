with open('input.txt') as f:
    pairs = [(a.split('-'), b.split('-')) for a,b  in (p.split(',') for p in (f.read().split('\n')))]

count = 0
for eachTupple in pairs:
    a, b = eachTupple[0], eachTupple[1]
    a1,a2 = a
    if int(a[0]) >= int(b[0]) or int(a[1]) <= int(b[1]):
        count+=1
    if int(b[0]) >= int(a[0]) or int(b[1]) <= int(a[1]):
        count+=1
    
print(count)
