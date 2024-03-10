import copy
import re

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_ = len(s1)
        check_ = {k:v for k, v in zip(set(s1), [s1.count(x) for x in set(s1)])}
        print(check_)
        if s1[0] in s2:
            index_ = s2.index(s1[0])
        #? If it is the first index.... like [ab], [abbhf]
            if index_ !=0:
                start = index_ -len_+1 
            else: start = 0
            #if goes up to the end!
            end = len(s2)-len(s1)
                        
            for i in range(start, end+1):
                new_check_ = copy.deepcopy(check_) 
                if i+len(s1)>=len(s2):
                    check = s2[i:]  
                else:      
                    check = s2[i:i+len(s1)] #sliding window!
                print("WIndow:  ", check)
                for a in check:
                    if a in check_.keys():
                        if new_check_[a]==0:
                            continue
                        new_check_[a]-=1
                #print(new_check_)
                if sum(new_check_.values())==0:
                    return True

            return False

if __name__ == "__main__":
    new_ = Solution()
    s1 = "bab"
    s2 = "eidbaooo"
    answer = new_.checkInclusion(s1, s2)
    print(answer)
