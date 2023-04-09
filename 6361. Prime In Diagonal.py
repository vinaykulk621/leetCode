class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        primes = [True] * (4*10**6 + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(4*10**6 ** 0.5) + 1):
            if primes[i]:
                for j in range(i ** 2, 4*10**6 + 1, i):
                    primes[j] = False

        primes=[x for x in range(2, 4*10**6 + 1) if primes[x]]

        i,lar=0,0
        while i<len(nums):
            if nums[i][i] in primes:
                if nums[i][i]>=lar:
                    lar=nums[i][i]
            if nums[i][len(nums)-i-1] in primes:
                if nums[i][len(nums)-i-1]>=lar:
                    lar=nums[i][len(nums)-i-1]
            i+=1
        return lar
