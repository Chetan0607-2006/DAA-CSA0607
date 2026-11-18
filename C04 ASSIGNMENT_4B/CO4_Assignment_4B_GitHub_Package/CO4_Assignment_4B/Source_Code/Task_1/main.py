# Task 1: Word wrap; squared unused-space penalty (assumption: equation absent in supplied DOCX).
def wrap(words,width):
    n=len(words); dp=[float('inf')]*(n+1); nxt=[-1]*(n+1); dp[n]=0
    for i in range(n-1,-1,-1):
        length=0
        for j in range(i,n):
            length+=len(words[j])+(j>i)
            if length>width: break
            penalty=0 if j==n-1 else (width-length)**2
            if penalty+dp[j+1]<dp[i]:dp[i]=penalty+dp[j+1];nxt[i]=j+1
        print('DP suffix',i,'minimum penalty',dp[i],'next',nxt[i])
    if dp[0]==float('inf'):raise ValueError('word exceeds width')
    lines=[];i=0
    while i<n:
        j=nxt[i];line=' '.join(words[i:j]);unused=width-len(line)
        lines.append((line,unused,0 if j==n else unused**2));i=j
    return dp[0],lines
if __name__=='__main__':
    words='dynamic programming creates efficient document layouts'.split()
    for width in (12,16,20):
        print('\nWIDTH',width)
        try:
            cost,lines=wrap(words,width)
            for line,unused,penalty in lines:print(repr(line),'unused',unused,'penalty',penalty)
            print('TOTAL',cost)
        except ValueError as e:print('Boundary:',e)
    try:wrap(['extraordinary'],5)
    except ValueError as e:print('Expected boundary error:',e)
