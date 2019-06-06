def classifyEdges(g_nodes, g_from, g_to, g_weight):
    import sys
    distance = {}
    parent = {}
    g_map = {}
    queue = []
    visited = []
    for i in range(len(g_from)):
        if g_from[i] in g_map:
            g_map[g_from[i]].update({g_to[i]: int(g_weight[i])})
        else:
            g_map[g_from[i]] = {g_to[i]: int(g_weight[i])}

    city_list = set(g_from + g_to)
    for i in city_list:
        parent[i] = None
        distance[i] = sys.maxsize

    distance[1] = 0

    queue.append(1)

    while queue:
        current = queue.pop(0)
        visited.append(current)
        try:
            for i in g_map[current].keys():
                if i not in visited:
                    queue.append(i)
                curDist = distance[current] + g_map[current][i]
                if distance[i] > curDist:
                    distance[i] = curDist
                    parent[i] = current
        except KeyError:
            x = 1
            # print(current, ":no outgoing city")

    no_nodes = g_nodes
    s2d = distance[g_nodes]
    path = []
    while g_nodes != 1:
        path.insert(0, g_nodes)
        g_nodes = parent[g_nodes]
    path.insert(0, 1)
    result = []
    for i in range(1,no_nodes+1):
        if i in path:
            result.append("YES")
        else:
            result.append("NO")
    return result
