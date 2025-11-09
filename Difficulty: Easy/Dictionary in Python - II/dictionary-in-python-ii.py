def pair_sum(arr, sum):
    # code here
    h={}
    for i, num in enumerate(arr):
        comp=sum-num
        if comp in h:
            return True
        h[num]=i
    return False