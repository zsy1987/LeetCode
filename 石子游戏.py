class Solution:
    def stoneGame(self, piles):


        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        print(dp)

        return dp[0][length - 1] > 0


#贪心 动态规划
s=Solution()
print(s.stoneGame([3,7,5,8,4,2,1,3,6,9]))
