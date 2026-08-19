class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n=len(nums)
        unique=sorted(set(nums))
        mapp={}
        for i,val in enumerate(unique):
            mapp[val]=i+1
        tree=[0]*(n+1)
        def query(i):
            ans=0
            while i>0:
                ans+=tree[i]
                i-=i&(-i)
            return ans

        def update(i,val):
            while i<=n:
                tree[i]+=val
                i+=i&(-i)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            rank=mapp[nums[i]]
            ans[i]=query(rank-1)
            update(rank,1)
        return ans
