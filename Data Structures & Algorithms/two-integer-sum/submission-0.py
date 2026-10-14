class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos={}
        ordenados=[]
        for x in range(len(nums)):
            resta=target-nums[x]
            if resta in vistos:
                ordenados=[x,vistos[resta]]
                ordenados.sort()
                return ordenados
            vistos[nums[x]]=x
            
