class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #every neighbour must be strictly one word diff from you -> len must be same, diff must happen once
        #bfs all neighbours, return count the moment any neighbour hit the endWord
        def isNeighbour(x,y):
            if(len(x)!=len(y)):
                return False
            diff=0
            for i in range(len(x)):
                if x[i]!=y[i]:
                    diff+=1
                if diff>1:
                    return False
            return True if diff==1 else False
        visited=set() #takes index
        n=len(wordList)
        q=deque()
        q.append(beginWord)
        count=0
        while q:
            levelSize=len(q)
            count+=1
            for _ in range(levelSize):
                curr=q.popleft()
                if curr == endWord:
                    return count
                for i in range(n):
                    if i in visited:
                        continue
                    if isNeighbour(curr,wordList[i]):
                        q.append(wordList[i])
                        visited.add(i)
        return 0

