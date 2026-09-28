class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents=list(range(n+1))
        def find(x):
            if x != parents[x]:
                parents[x]=find(parents[x])
            return parents[x]
        size=[1]*n
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx==rooty:
                return False
            if size[rootx]>size[rooty]:
                parents[rooty]=rootx
                size[rootx]+=size[rooty]
            elif size[rooty]>size[rootx]:
                parents[rootx]=rooty
                size[rooty]+=size[rootx]
            else:
                parents[rootx]=rooty
                size[rooty]+=size[rootx]
            return True
        count=n
        for x,y in edges:
            if union(x,y):
                count-=1
        return count
        




            