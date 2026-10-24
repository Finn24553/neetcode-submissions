
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elem={}
        for x in nums:
            if x in elem:
                elem[x]+=1
            else:
                elem[x]=1
        resultados=(sorted(elem, key=elem.get)[-k:])
        return resultados
        