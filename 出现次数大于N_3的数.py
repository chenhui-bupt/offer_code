"""
出现次数大于N_3的数
"""
def MoreThanN_3(arr):
    tmp1 = tmp2 = None
    cnt1 = cnt2 = 0

    for num in arr:
        if num == tmp1:
            cnt1 += 1
        elif num == tmp2:
            cnt2 += 1
        else:
            if tmp1 and tmp2:
                cnt1 -= 1
                cnt2 -= 1
                if cnt1 == 0:
                    tmp1 = None
                if cnt2 == 0:
                    tmp2 = None
            else:
                if not tmp1:
                    tmp1 = num
                    cnt1 = 1
                elif not tmp2:
                    tmp2 = num
                    cnt2 = 1
    cnt1 = 0
    cnt2 = 0
    res = []
    for num in arr:
        if num == tmp1:
            cnt1 += 1
        if num == tmp2:
            cnt2 += 1
    if cnt1 > len(arr)//3:
        res.append(tmp1)
    if cnt2 > len(arr)//3:
        res.append(tmp2)
    return res

arr = [1 ,2 ,3 ,3 ,5 ,2 ,2 ,3 ,3 ,3 ,5 ,6 ,2 ,2 ,2 ,3 , 3]
res = MoreThanN_3(arr)
print(res)





