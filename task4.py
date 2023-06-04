def common_elements(n, m):
    
    list1 = [i for i in range(3, 3 * n + 1, 3)]

    list2 = [i for i in range(5, 5 * m + 1, 5)]

    intersection = set(list1) & set(list2)

    return intersection

n = 10  
m = 15  
result = common_elements(n, m)
print(result)