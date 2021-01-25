#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    dict = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if (m == 1 or n == 1):
            return 1
        if (m == 2 and n == 2):
            return 2
        key = ('%s,%s'%(m,n))
        if key in self.dict:
            return self.dict[key]
        
        value = self.uniquePaths(self,m-1,n) + self.uniquePaths(self,m, n-1)
        self.dict[key] = value
        return value

oo = Solution
print(oo.uniquePaths(oo,2,3))
# @lc code=end

