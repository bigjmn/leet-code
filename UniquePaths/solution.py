# Solve using dynamic programming. Each square can be reached by
# either the square to the left or the square above it (but not both.)
# Add the ways to reach those squares, using 0 if they'r out of range.

def uniquePaths(m, n):
    #create memo
    memo = {}

    #calculate subpath to p, q
    def subpath(p, q):
        #if either is out of range, 0 ways to reach it.
        #only need lower bounds, our iteration won't go above boundary anyway
        if p < 0 or q < 0:
            return 0
        if (p, q) in memo:
            return memo[(p, q)]
        res = subpath(p-1, q)+subpath(p, q-1)
        memo[(p, q)] = res

    #set initial state
    memo[(0,0)] = 1

    #iterate, memoize
    for i in range(m):
        for j in range(n):
            subpath(i, j)

    #get value we want
    return memo[(m-1, n-1)]

#SIMILAR BUT FASTER
def altUniquePaths(m, n):
    memo = {}
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                memo[(i,j)] = 1
                continue
            memo[(i,j)] = memo[(i-1,j)]+memo[(i,j-1)]
    return memo[(m-1,n-1)]
