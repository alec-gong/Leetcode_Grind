from collections import defaultdict

def evaluatediv(s):
    lines = s.splitlines()

    infos = lines[0].split(";")
    graph = defaultdict(list)
    dis = {}
    for info in infos:
        string = info.split(",")
        u, v, w = string
        graph[u].append(v)
        graph[v].append(u)
        dis[(u,v)] = float(w)
        dis[(v,u)] = 1 / float(w) 
    
    def dfs(node, target, visited):
        if node in visited: 
            return 0
        if node == target:
            return 1
        visited.add(node)
        res = 0
        for next in graph[node]:
            res = max(res, dfs(next, target, visited) * dis[(node, next)])
        return res


    res = dfs(lines[1], lines[2], set())
    if res == 0:
        return -1.0
    return res




