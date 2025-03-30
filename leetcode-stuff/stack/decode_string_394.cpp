#include <string>
using namespace std;

class Solution {
    int stringToInteger(string s) {
        int ans = 0;
        for (char nxt : s) {
            ans *= 10;
            ans += nxt - '0';
        }
        return ans;
    }

    public:
    string decodeString(string s) {
        string ans = "";
        int prev = 0;
        int repetitions = 0;
        int depth = 0;  // keeps track of # open bracket - # close bracket
        for (int i = 0; i < s.size(); i++) {
            if (depth == 0 && 'a' <= s[i] && s[i] <= 'z') {
            	  // case with lowercase letters
                ans.push_back(s[i]);
                prev = i + 1;
            }
            if (s[i] == '[') {
                depth++;
                if (depth == 1) {  // open bracket for the case "k[s]"
                    repetitions = stringToInteger(s.substr(prev, i - prev));
                    prev = i + 1;
                }
            } else if (s[i] == ']') {
                depth--;
                if (depth == 0) {              // close bracket for the case "k[s]"
                    while (repetitions > 0) {  // add k copies of s
                        ans += decodeString(s.substr(prev, i - prev));
                        repetitions--;
                    }
                    prev = i + 1;
                }
            }
        }
        return ans;
    }
};