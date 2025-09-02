
"""
if - Statements (and some loops)

In THIS FILE you should write your code.
Compare with the solutions in `answers.py`.

Run with:
    python if_statements_exercises.py
"""

def ex_1_1():
    """
    Exercise 1.1 (1p)
    Create five variables: card1, card2, card3, card4, card5.
    Assign them the values 4, 2, 7, 1, 11.
    Add them up and store the result in a variable called result.
    Return result.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.1 not implemented")


def ex_1_2():
    """
    Exercise 1.2 (1p)
    Use an if-statement to check if the sum of card1..card5 is greater than 21.
    Create a variable status:
      - "busted" if the sum > 21
      - otherwise "safe"
    Return status.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.2 not implemented")


def ex_1_3():
    """
    Exercise 1.3 (1p)
    Compare the sum of card1..card3 with 21 and return a string:
      - "safe" if sum < 21
      - "busted" if sum > 21
      - "black jack" if sum == 21
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.3 not implemented")


def ex_1_4():
    """
    Exercise 1.4 (2p)
    Create dealer1, dealer2, dealer3 = 1, 6, 7.
    Decide what the dealer should do:
      - sum < 17        -> "pick"
      - 17 <= sum < 21  -> "stop"
      - sum == 21       -> "black jack"
      - sum > 21        -> "busted"
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 1.4 not implemented")


def ex_2_1():
    """
    Exercise 2.1 (1p)
    Create a variable my_fruit and set it to "plum".
    Use match/case (Python 3.10+) to build a text about the fruit's color:
      - banana -> "The banana is yellow."
      - apple  -> "The apple is green."
      - kiwi   -> "The kiwi is green."
      - plum   -> "The plum is purple."
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 2.1 not implemented")


def ex_2_2():
    """
    Exercise 2.2 (1p)
    Extend match/case with a default (case _).
    Set my_fruit = "pear" and return:
      "That is an unknown fruit."
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 2.2 not implemented")


def ex_3_1():
    """
    Exercise 3.1 (1p)
    Use a for-loop to increase 481 by 6 ten times.
    Return the result.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 3.1 not implemented")


def ex_3_2():
    """
    Exercise 3.2 (1p)
    Use a for-loop to decrease 551 by 8 ten times.
    Return the result.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 3.2 not implemented")


def ex_3_3():
    """
    Exercise 3.3 (3p)
    Use a for-loop to build a string with all even numbers in the range
    22..45, separated by commas. No extra comma at the end.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 3.3 not implemented")


def ex_4_1():
    """
    Exercise 4.1 (1p)
    Use a while-loop to increase 10 by 6 until the value is at least 481.
    Return the number of steps.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 4.1 not implemented")


def ex_4_2():
    """
    Exercise 4.2 (1p)
    Use a while-loop to subtract 8 from 551 until the value is <= 0.
    Return the number of steps.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 4.2 not implemented")


def ex_4_3():
    """
    Exercise 4.3 (3p)
    Use a while-loop to create a comma-separated string of all numbers
    between 28..63 that are divisible by 5 or 7.
    """
    # TODO: Write your code here
    raise NotImplementedError("Exercise 4.3 not implemented")


def _run_and_print(fn, label):
    try:
        result = fn()
        print(f"{label}: {result}")
    except NotImplementedError:
        print(f"{label}: (not implemented)")


def main():
    print("Running Lab exercises...\n")
    _run_and_print(ex_1_1, "1.1")
    _run_and_print(ex_1_2, "1.2")
    _run_and_print(ex_1_3, "1.3")
    _run_and_print(ex_1_4, "1.4")
    _run_and_print(ex_2_1, "2.1")
    _run_and_print(ex_2_2, "2.2")
    _run_and_print(ex_3_1, "3.1")
    _run_and_print(ex_3_2, "3.2")
    _run_and_print(ex_3_3, "3.3")
    _run_and_print(ex_4_1, "4.1")
    _run_and_print(ex_4_2, "4.2")
    _run_and_print(ex_4_3, "4.3")


if __name__ == "__main__":
    main()
