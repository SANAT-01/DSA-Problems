class Solution:
    def numBusesToDestination(self, routes, S, T):
        route_number=defaultdict(set)
        for idx,route in enumerate(routes):
            for i in route:
                route_number[i].add(idx)
        bfs=[(S,0)]
        seen=set()
        seen.add(S)
        for node,d in bfs:
            if node==T:
                return d
            for lvl in route_number[node]:
                for i in routes[lvl]:
                    if i not in seen:
                        seen.add(i)
                        bfs.append((i,d+1))
                routes[lvl]=[]
        return -1