from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #return [[*g] for _,g in groupby(sorted(strs, key=sorted), sorted)]
        answer = []
        i=0
        alphabet = []

        for st in strs:
            if not alphabet:
                alphabet.append(list(st))
                answer.append([st])
                continue
            st_ = list(st)
            flag=True
            for alph in alphabet:
                if not st_ and not alph:
                    answer[alphabet.index(alph)].append(st)
                    flag=True
                    break
                alph_= alph.copy()
                if len(alph)!=len(st_):
                    flag=False
                    continue                
                for letter in st_:
                    if letter not in alph_:                
                        flag = False
                        break 
                    else:
                        alph_.remove(letter)
                        flag = True
                        continue
                if flag: #insert word in here~!
                    answer[alphabet.index(alph)].append(st)
                    break
            if not flag:
                alphabet.append(st_)
                answer.append([st])
                continue
        return answer

        
if __name__ == "__main__":
    new_ = Solution()
    a = ["eat","tea","tan","ate","nat","bat", "na", "tnn", "", ""]
    answer = new_.groupAnagrams(a)
    print(answer)