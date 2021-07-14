#include <iostream>
#include <string>
#include <unordered_map>
using namespace std; 
class Solution {
public:
    //https://www.cnblogs.com/grandyang/p/9190143.html
    string customSortString(string order, string str) {
        string res = "";
        unordered_map<char, int> m;
        for (char c : str) 
            m[c]++;
        
        for (char c : order) {
            res += string(m[c], c);
            m[c] = 0;
        }
        for (auto a : m) {
            res += string(a.second, a.first);
        }
        return res;        
    }
};

int main() {

    Solution foo = Solution();
    string ans = foo.customSortString("cba","abcd");
    cout<<"output "<<ans<<endl;
    return 0;
}