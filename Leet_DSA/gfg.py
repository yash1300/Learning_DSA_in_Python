 #GFG array question
 
def leaders(self, A, N):
    res = [A[-1]] #Save current leader 
    for i in range(N-2,-1,-1):
        if A[i] >= res[-1]:
            res.append(A[i])
    return res[::-1]

