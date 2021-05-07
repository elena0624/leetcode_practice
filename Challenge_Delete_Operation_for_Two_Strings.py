class Solution: # My solution. very fast
    def minDistance(self, word1: str, word2: str) -> int:
        w1_dict=collections.defaultdict(list)
        for i in range(len(word1)):
            w1_dict[word1[i]].append(i)
        w2_ls=[]
        for i in range(len(word2)):
            w2_ls.extend(w1_dict[word2[i]][::-1])
        if not w2_ls:
            return(len(word1)+len(word2))
        # 參考300題
        ans_ls=[w2_ls[0]]

        for i in range(1,len(w2_ls)):
            if w2_ls[i]>ans_ls[-1]:
                ans_ls.append(w2_ls[i])
            elif w2_ls[i]<ans_ls[0]:
                ans_ls[0]=w2_ls[i]
            elif w2_ls[i] in ans_ls:
                continue
            else:
                l=0
                r=len(ans_ls)-1
                while l<r:
                    m=(l+r)//2
                    if w2_ls[i]>ans_ls[m]:# >m，因為找找比x大的，m也不用考慮了
                        l=m+1
                    else:#<m 因為要找比x大的,所以m也要考慮
                        r=m
                ans_ls[r]=w2_ls[i]
        # 共同最長是len(ans_ls)

        return(len(word1)+len(word2)-2*len(ans_ls))
#%% Revise my solution using packages
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_dict=collections.defaultdict(list)
        for i in range(len(word1)):
            w1_dict[word1[i]].append(i)
        w2_ls=[]
        for i in range(len(word2)):
            w2_ls.extend(w1_dict[word2[i]][::-1])
        if not w2_ls:
            return(len(word1)+len(word2))
        # 參考300題
        ans_ls=[w2_ls[0]]

        for i in range(1,len(w2_ls)):
            if w2_ls[i]>ans_ls[-1]:
                ans_ls.append(w2_ls[i])
            else:
                ans_ls[bisect.bisect_left(ans_ls,w2_ls[i])]=w2_ls[i]
        # 共同最長是len(ans_ls)

        return(len(word1)+len(word2)-2*len(ans_ls))
#%% elegant python solution for #5
def minDistance(self, w1, w2):
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (w1[i] == w2[j]))
    return m + n - 2 * dp[m][n]
#%% Official java solution1
public class Solution {
    public int minDistance(String s1, String s2) {
        return s1.length() + s2.length() - 2 * lcs(s1, s2, s1.length(), s2.length());
    }
    public int lcs(String s1, String s2, int m, int n) {
        if (m == 0 || n == 0)
            return 0;
        if (s1.charAt(m - 1) == s2.charAt(n - 1))
            return 1 + lcs(s1, s2, m - 1, n - 1);
        else
            return Math.max(lcs(s1, s2, m, n - 1), lcs(s1, s2, m - 1, n));
    }
}
#%% Official java solution2
public class Solution {
    public int minDistance(String s1, String s2) {
        int[][] memo = new int[s1.length() + 1][s2.length() + 1];
        return s1.length() + s2.length() - 2 * lcs(s1, s2, s1.length(), s2.length(), memo);
    }
    public int lcs(String s1, String s2, int m, int n, int[][] memo) {
        if (m == 0 || n == 0)
            return 0;
        if (memo[m][n] > 0)
            return memo[m][n];
        if (s1.charAt(m - 1) == s2.charAt(n - 1))
            memo[m][n] = 1 + lcs(s1, s2, m - 1, n - 1, memo);
        else
            memo[m][n] = Math.max(lcs(s1, s2, m, n - 1, memo), lcs(s1, s2, m - 1, n, memo));
        return memo[m][n];
    }
}
#%% Official java solution3
public class Solution {
    public int minDistance(String s1, String s2) {
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        for (int i = 0; i <= s1.length(); i++) {
            for (int j = 0; j <= s2.length(); j++) {
                if (i == 0 || j == 0)
                    continue;
                if (s1.charAt(i - 1) == s2.charAt(j - 1))
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return s1.length() + s2.length() - 2 * dp[s1.length()][s2.length()];
    }
}
#%% Official java solution4
public class Solution {
    public int minDistance(String s1, String s2) {
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        for (int i = 0; i <= s1.length(); i++) {
            for (int j = 0; j <= s2.length(); j++) {
                if (i == 0 || j == 0)
                    dp[i][j] = i + j;
                else if (s1.charAt(i - 1) == s2.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = 1 + Math.min(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[s1.length()][s2.length()];
    }
}
#%% Official java solution5
public class Solution {
    public int minDistance(String s1, String s2) {
        int[] dp = new int[s2.length() + 1];
        for (int i = 0; i <= s1.length(); i++) {
            int[] temp=new int[s2.length()+1];
            for (int j = 0; j <= s2.length(); j++) {
                if (i == 0 || j == 0)
                    temp[j] = i + j;
                else if (s1.charAt(i - 1) == s2.charAt(j - 1))
                    temp[j] = dp[j - 1];
                else
                    temp[j] = 1 + Math.min(dp[j], temp[j - 1]);
            }
            dp=temp;
        }
        return dp[s2.length()];
    }
}
