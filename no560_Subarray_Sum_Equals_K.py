# My solution (very slow=>O(n^2))
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_nums = nums.copy()
        m=len(nums)
        sum_dict = collections.defaultdict(list)
        sum_dict[sum_nums[0]].append(0)
        for i in range(1,m):
            sum_nums[i]+=sum_nums[i-1]
            sum_dict[sum_nums[i]].append(i)

        ans=0
        ans+=len(sum_dict[k])
        for i in range(m):
            ans+=sum(a>i for a in sum_dict[sum_nums[i]+k])
        return(ans)
#%% Elegant solution
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m=len(nums)
        sum_cnt = collections.defaultdict(int)
        sum_cnt[0]=1
        ans=0
        cur_sum=0
        for i in range(m):
            cur_sum+=nums[i]
            ans+=sum_cnt[cur_sum-k]
            sum_cnt[cur_sum]+=1
        return(ans)
#%% Brute force Java version
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            for (int end = start + 1; end <= nums.length; end++) {
                int sum = 0;
                for (int i = start; i < end; i++)
                    sum += nums[i];
                if (sum == k)
                    count++;
            }
        }
        return count;
    }
}
#%% Using Cumulative Sum Java version
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int[] sum = new int[nums.length + 1];
        sum[0] = 0;
        for (int i = 1; i <= nums.length; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        for (int start = 0; start < nums.length; start++) {
            for (int end = start + 1; end <= nums.length; end++) {
                if (sum[end] - sum[start] == k)
                    count++;
            }
        }
        return count;
    }
}
#%% Without Space Java version
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum=0;
            for (int end = start; end < nums.length; end++) {
                sum+=nums[end];
                if (sum == k)
                    count++;
            }
        }
        return count;
    }
}
#%% Approach 4: Using Hashmap Java version
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, sum = 0;
        HashMap < Integer, Integer > map = new HashMap < > ();
        map.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k))
                count += map.get(sum - k);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}
