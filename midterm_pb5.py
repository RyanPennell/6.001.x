#def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here  

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    ans = []
    if target not in aDict.values():
        return ans
    else:
        for index in aDict.keys():
            if target == aDict[index]:
                ans += [index]
        ans.sort()
        return ans
