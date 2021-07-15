#include <iostream>
#include <vector>
#include <algorithm>
using namespace std; 
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int ans=0;
        int n=nums.size();
        sort(nums.begin(), nums.end());
        for (int i=n-1;i>=0;i--){
            int lo=0;
            int hi=i-1;
            while(lo<hi){
                if(nums[hi]+nums[lo] > nums[i]){
                    ans += hi-lo;
                    hi -= 1;
                }else{
                    lo+=1;
                }
                    
            }
        }
        return ans;
    }
};

int main() {

    Solution foo = Solution();
    vector<int> vect{ 4,2,3,4};
    int ans = foo.triangleNumber(vect);
    cout<<"output "<<ans<<endl;
    return 0;
}