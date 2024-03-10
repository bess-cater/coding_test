s1 = "ky"
s2 = "ainwkckifykxlribaypk"

import copy
#? Dictionary takes one by one... instead decide HOW MUCH of each letter
#print(''.join(sorted(s1)))
v = 0



import re
#? To find all occurences!
len_ = len(s1)
def perm(s1, s2):
    check_ = {k:v for k, v in zip(set(s1), [s1.count(x) for x in set(s1)])}
    print(check_)
    if s1[0] in s2:
        indeces = [i for i in range(len(s2)) if s2[i] == s1[0]]
        for index in indeces:
        #? If it is the first index.... like [ab], [abbhf]
            if index !=0:
                start = index -len_+1 
            else: start = 0
            for i in range(start, index +1):
                new_check_ = copy.deepcopy(check_)            
                check = s2[i:i+len(s1)]
                for a in check:
                    if a in check_.keys():
                        if new_check_[a]==0:
                            continue
                        new_check_[a]-=1
                print(new_check_)
                if sum(new_check_.values())==0:
                    return True

    return False

print(perm(s1, s2))
