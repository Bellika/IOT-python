# ----------------------
# Globals
# ----------------------
array2 = ["potato", "carrot", "onion", "leek", "cabbage"]
array1 = [47, 98, -13, 0, -412, 499, 3, 1200]


def ex_1_1():
    return array2[1]


def ex_1_2():
    return array2[0] + "-" + array2[-1]


def ex_1_3():
    array3 = []
    for item in array1:
        array3.append(item)
    for item in array2:
        array3.append(item)
    return array3


def ex_1_4():
    array21 = []
    for item in array2:
        array21.append(item)
    for i in range(len(array21)):
        for j in range(i + 1, len(array21)):
            if array21[i] > array21[j]:
                array21[i], array21[j] = array21[j], array21[i]
    return array21


    array21 = array2.copy()
    array21.sort()
    return array21


def ex_1_5():
    array11 = []
    for item in array1:
        array11.append(item)
    for i in range(len(array11)):
        for j in range(i + 1, len(array11)):
            if array11[i] < array11[j]:
                array11[i], array11[j] = array11[j], array11[i]
    return array11

    array11 = array1.copy()
    
    array11.sort()
    return array11



def ex_1_6():
    array22 = []
    for item in array2:
        array22.append(item.upper())
    return array22


def ex_1_7():
    array12 = []
    for item in array1:
        if item > 0:
            array12.append(item)
    return array12


def array_average(arr):
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
    if count == 0:
        return 0
    return round(total / count)


def ex_1_8():
    return array_average(array1)


def ex_2_1():
    my_array = []
    for item in array1:
        my_array.append(item)
    # swap first and last
    tmp = my_array[0]
    my_array[0] = my_array[-1]
    my_array[-1] = tmp
    return my_array


def ex_2_2():
    my_array = ex_2_1()
    my_array[2] = False
    my_array[3] = False
    return my_array


def ex_2_3():
    my_array = ex_2_2()
    # remove 4th and 5th
    del my_array[3:5]
    # insert "MEGA" after 3rd
    my_array.insert(3, "MEGA")
    return my_array
