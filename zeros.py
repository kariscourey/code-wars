# def move_zeros(lst):

    # moved = []

    # for i in lst:
    #     if i != 0:
    #         moved.append(i)

    # for i in lst:
    #     if i == 0:
    #         moved.append(i)

    # # zeros = lst.count(0)
    # # moved.append(zeros * 0)

    # lst = moved

    # return lst


def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
