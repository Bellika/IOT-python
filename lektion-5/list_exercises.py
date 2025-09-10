"""
Lab 4 - Arrays
"""

# ----------------------
# Section 1 . Arrays
# ----------------------

# Create array2 that will be used in multiple exercises



def ex_1_1():
    """
    Create a variable `array2` holding an array with the words
    [potato, carrot, onion, leek, cabbage] You can create this globally.
    Return the element on position 1 in array2.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.1 not implemented")


def ex_1_2():
    """
    Use the variable `array2`.
    Concatenate the first and last element as a string.
    Separate the string with a "-"
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.2 not implemented")


def ex_1_3():
    """
    Create an array, `array1`, with the items
    [47, 98, -13, 0, -412, 499, 3, 1200].
    Merge array1 and array2 into a third variable `array3`.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.3 not implemented")


def ex_1_4():
    """
    Create a variable `array21` as a clone of `array2`.
    Sort array21.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.4 not implemented")


def ex_1_5():
    """
    Create a variable `array11` as a clone of `array1`.
    Sort array11 according to its values (smallest first, largest last).
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.5 not implemented")


def ex_1_6():
    """
    Create a variable `array22` holding the same content as `array2` but
    all strings in UPPERCASE. Use list comprehension.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.6 not implemented")


def ex_1_7():
    """
    Create a new array, `array12`.
    It should contain all positive numbers from `array1`.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.7 not implemented")


def array_average(arr):
    """
    Helper function to calculate the average of an array.
    Returns a rounded integer.
    """
    # TODO: Write your code here
    raise NotImplementedError("array_average() not implemented")


def ex_1_8():
    """
    Use `array_average()` to return the rounded average of `array1`.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.8 not implemented")


# ----------------------
# Section 2 . Modify arrays
# ----------------------


def ex_2_1():
    """
    Create a new array `my_array` as a copy of `array1`.
    Switch the first and last element.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 2.1 not implemented")


def ex_2_2():
    """
    In `my_array`, change the 3rd and 4th value to the boolean value False.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 2.2 not implemented")


def ex_2_3():
    """
    Remove the 4th and 5th item in `my_array`.
    Then insert the string "MEGA" after the 3rd item.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 2.3 not implemented")


# ----------------------
# Helper runner for testing
# ----------------------

def _run_and_print(fn, label):
    try:
        result = fn()
        print(f"{label}: {result}")
    except NotImplementedError:
        print(f"{label}: (not implemented)")


def main():
    print("Running Lab 4 - Arrays exercises...\n")
    _run_and_print(ex_1_1, "1.1")
    _run_and_print(ex_1_2, "1.2")
    _run_and_print(ex_1_3, "1.3")
    _run_and_print(ex_1_4, "1.4")
    _run_and_print(ex_1_5, "1.5")
    _run_and_print(ex_1_6, "1.6")
    _run_and_print(ex_1_7, "1.7")
    _run_and_print(ex_1_8, "1.8")
    _run_and_print(ex_2_1, "2.1")
    _run_and_print(ex_2_2, "2.2")
    _run_and_print(ex_2_3, "2.3")


if __name__ == "__main__":
    main()
