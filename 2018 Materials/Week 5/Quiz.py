def min_list(ls):
    final = []
    for ls1 in ls:
        temp = ls1[0]
        for item in ls1:
            if item < temp:
                temp = item
        final.append(temp)
    return final

print(min_list([[100], [1,7], [8,0,-1]]))