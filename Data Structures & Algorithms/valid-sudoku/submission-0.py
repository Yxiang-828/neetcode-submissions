class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checker:
        #1.is dupe - len(subset)=len(set(subset))
        #2.is valid subset - set(subset).issubset(set(nums))
        #by row
        for line in board:
            suspect=[]
            for stuff in line:
                if stuff!=".":
                    suspect.append(stuff)
            if not self.isGood(suspect, line):
                return False
        #by col
        transpose=[list(core) for core in zip(*board)]
        for line in transpose:
            suspect=[]
            for stuff in line:
                if stuff!=".":
                    suspect.append(stuff)
            if not self.isGood(suspect, line):
                return False
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):

                seen = set()

                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):

                        if board[r][c] == ".":
                            continue

                        if board[r][c] in seen:
                            return False

                        seen.add(board[r][c])
        return True


    def isGood(self,suspect,line):
        if len(suspect)==len(set(suspect)) and set(suspect).issubset(set(line)):
            return True