class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = ""
        for i in range(len(indices)):
            new_s += s[indices.index(i)]
        return new_s
                
                