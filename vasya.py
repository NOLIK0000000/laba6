def permutations(s):
    result=[]
    used=[False]*len(s)
    def backtrack(current):
        if len(current)==len(s):
            if current not in result:
                result.append(current)
            return
        for i in range(len(s)):
            if not used[i]:
                used[i]=True
                backtrack(current+s[i])
                used[i]=False
    backtrack("")
    return result
print(permutations("abc"))
print(permutations("aab"))
print(permutations("a"))