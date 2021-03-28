class Solution:
    def originalDigits(self, s: str) -> str:
        s_count = collections.Counter(s)
        ans_digit = [0]*10

        for c, str_dig, pos in [['z','zero',0],['w','two',2],['u','four',4],['x','six',6],['g','eight',8],\
                                ['f','five',5],['r','three',3],\
                                ['v','seven',7],['i','nine',9],\
                                ['o','one',1]]:
            ans_digit[pos]+=s_count[c]
            for char_dig in str_dig:
                s_count[char_dig]-=ans_digit[pos]
        ans_s=''
        for i in range(10):
            ans_s+=str(i)*ans_digit[i]
        return(ans_s)
#%% Other solution
class Solution:
    def originalDigits(self, s: str) -> str:
        counts = collections.Counter(s)
        digit_counts = [
            counts["z"], # 0
            counts["o"] - counts["z"] - counts["w"] - counts["u"], # 1
            counts["w"], # 2
            counts["t"] - counts["w"] - counts["g"], # 3
            counts["u"], # 4
            counts["f"] - counts["u"], # 5
            counts["x"], # 6
            counts["s"] - counts["x"], # 7
            counts["g"], # 8
            counts["i"] - counts["x"] - counts["g"] - counts["f"] + counts["u"], # 9
        ]
        return "".join(str(digit) * count for digit, count in enumerate(digit_counts))