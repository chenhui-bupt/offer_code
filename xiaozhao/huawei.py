inputstr = "1,2,20,60;2,3,90,60;2,4,30, 100;2,5,50,60;3,5,40,60;3,6,30,60;4,5,100,60;5,6,70,30"
graph = dict()
for line in inputstr.split(';'):
    line = list(map(int, line.split(',')))
    graph[line[0]] = line[1:]
    graph

def cost(s, v):
    return int(s * 8 * 6.5/100 + (v==100) * 0.5)

dp = []
