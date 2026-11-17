# Task 4: Word break - flawed vs corrected decision

def word_break(text,words,correct=True):
    dp=[False]*(len(text)+1);dp[0]=True
    for i in range(1,len(text)+1):
        for j in range(i):
            if (not correct or dp[j]) and text[j:i] in words:
                dp[i]=True;break
    return dp
if __name__=='__main__':
    print('Task 4 failing case: text=xyzcat, dictionary={cat}')
    print('Faulty states:',word_break('xyzcat',{'cat'},False))
    print('Fixed states:',word_break('xyzcat',{'cat'},True))
    print('Regression:',word_break('applepie',{'apple','pie'},True)[-1])
