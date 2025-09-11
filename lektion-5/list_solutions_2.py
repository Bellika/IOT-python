# ----------------------                                                                                                                                                                                                  13:14:56
# Globals
# ----------------------
array2 = ["potato", "carrot", "onion", "leek", "cabbage"]
array1 = [47, 98, -13, 0, -412, 499, 3, 1200]


def ex_1_1():
    return array2[1]


def ex_1_2():
    return f"{array2[0]}-{array2[-1]}"


def ex_1_3():
    return array1 + array2


def ex_1_4():
    return sorted(array2)


def ex_1_5():
    return sorted(array1)


def ex_1_6():
    return [item.upper() for item in array2]


def ex_1_7():
    return [num for num in array1 if num > 0]


def array_average(arr):
    return round(sum(arr) / len(arr)) if arr else 0


def ex_1_8():
    return array_average(array1)


def ex_2_1():
    my_array = array1.copy()
    my_array[0], my_array[-1] = my_array[-1], my_array[0]
    return my_array


def ex_2_2():
    my_array = ex_2_1()
    my_array[2:4] = [False, False]
    return my_array


def ex_2_3():
    my_array = ex_2_2()
    my_array[3:5] = ["MEGA"]
    return my_array
