def valid_anagram(s:str,t:str)->bool:
    return sorted(s) == sorted(t) 



    '''
    seen = set(nums1)
    ans=set()
    for x in nums2:
        if x in seen:
            ans.add(x)
    return list(ans)
    '''