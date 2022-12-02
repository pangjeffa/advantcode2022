
mask = {'A':'ZXY', 'B':'XYZ','C':'YZX'}
pts = {'X':1, 'Y':2, 'Z':3}
outcome = {'X':0,'Y':1,'Z':2}

with open("./input2.txt", "r") as f:
    # print(sum([pts[game[2]]+mask[game[0]].index(game[2])*3 for game in f.read().split('\n')]))
    print(sum([outcome[game[2]]*3 + pts[ mask[game[0]] [outcome[game[2]]] ]for game in f.read().split('\n')]))