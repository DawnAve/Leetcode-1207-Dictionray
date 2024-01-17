class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
            # Same effect
            # for x in arr:
            # freq[x] = freq.get(x, 0) + 1
        Set = set()
        for i in dic.values():
            if i in Set:
                return False
            else:
                Set.add(i)
        return True
        
