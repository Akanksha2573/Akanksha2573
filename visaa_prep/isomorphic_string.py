def isIsomorphic(N, s, t):
    map_s_to_t = {}
    map_t_to_s = {}  
    for i in range(N):
        if s[i] in map_s_to_t:
            if map_s_to_t[s[i]] != t[i]:
                return "false"
        else:
            map_s_to_t[s[i]] = t[i]
        if t[i] in map_t_to_s:
            if map_t_to_s[t[i]] != s[i]:
                return "false"
        else:
            map_t_to_s[t[i]] = s[i]
    return "true"
N = int(input())  
s = input().strip()  
t = input().strip()  
print(isIsomorphic(N, s, t))
