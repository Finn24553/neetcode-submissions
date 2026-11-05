class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[1]*len(nums)
        der=1
        izq=1
        n=len(nums)

        for i in range(n):
            out[i]=der
            der*=nums[i]

        for j in range(n-1,-1,-1):
            out[j]*=izq
            izq*=nums[j]
        return out
        