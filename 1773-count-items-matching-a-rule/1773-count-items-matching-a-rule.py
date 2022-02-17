class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        s = 0
        for i in range(len(items)):
            if ruleKey == "type":
                if ruleValue == items[i][0]:
                    s += 1
            if ruleKey == "color":
                if ruleValue == items[i][1]:
                    s += 1
            if ruleKey == "name":
                if ruleValue == items[i][2]:
                    s += 1 
        return s
       