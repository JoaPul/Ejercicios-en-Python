def plusMinus(arr):
    po = 0
    neg = 0
    ze = 0
    for i in arr:
        if i > 0:
            po += 1
        elif i < 0:
            neg += 1
        else:
            ze = 1
    po = '{:.6f}'.format(po/len(arr))
    neg = '{:.6f}'.format(neg/len(arr))
    ze = '{:.6f}'.format(ze/len(arr))
    return po, neg, ze


# print(plusMinus([1, 1, 0, -1, -1]))
