'''
Longest Word
--------------------------------------------------------
Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
Recall the split(' ') method, which returns a list of words of the string.
'''

string = input().split(" ")
strlst = []
for s in string:
    strlst.append(len(s))
mx = max(strlst)
i = strlst.index(mx)
print(string[i])
