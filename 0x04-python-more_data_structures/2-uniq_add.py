def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for a in my_list:
        if a not in new_list:
            new_list.append(a)
    for a in new_list:
        sum += a
    return (sum)
