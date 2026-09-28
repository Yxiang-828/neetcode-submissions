class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #for a valid tree, 1. need to have no cycles, 2. need to only have one connected component, not 0 not >1
        parent=list(range(n+1))
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        size=[1]*n
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx==rooty:
                return False
            if size[rootx]>size[rooty]:
                parent[rooty]=rootx
                size[rootx]+=size[rooty]
            else:
                parent[rootx]=rooty
                size[rooty]+=size[rootx]
            return True
        count=0
        for x,y in edges:
            if not union(x,y):
                return False
            

        
        if len(edges)<n-1:
            return False
        return True