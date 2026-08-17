from collections import deque

class Solution:
    def watchedVideosByFriends(self, w: List[List[str]], f: List[List[int]], id: int, l: int) -> List[str]:
        arr=[]
        queue=deque([(id,0)])
        visited=set()
        visited.add(id)
        while queue:
            node,t=queue.popleft()
            if t==l:
                arr.append(node)
                continue
            for ng in f[node]:
                if ng not in visited:
                    visited.add(ng)
                    queue.append((ng,t+1))
        ans={}
        for i in arr:
            for v in w[i]:
                ans[v]=ans.get(v,0)+1
        ans=list(zip(ans.values(),ans.keys()))
        ans.sort()
        return [j for i,j in ans]