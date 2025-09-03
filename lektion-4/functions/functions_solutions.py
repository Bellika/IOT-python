"""
Lab 3 - Functions

In THIS FILE you should write your code.
Compare with the solutions in `answers.py`.

Run with:
    python functions_lab_exercises.py
"""

import math

# ----------------------
# Section 1: Basic functions
# ----------------------

def ex_1_1():
    """
    Exercise 1.1 (1p)
    Return the sum of all numbers between two chosen numbers.
    """
    # TODO: Write your code here
    def sum_range_num(min_number, max_number):
        return sum(range(min_number, max_number + 1))
    
    return sum_range_num(22, 91)


def ex_1_2():
    """
    Exercise 1.2 (1p)
    Return the color of a given fruit.
    """
    # TODO: Write your code here
    def fruit_color(fruit):
        colors = {
            "banana": "yellow",
            "apple": "green",
            "kiwi": "green",
            "plum": "red"
        }
        return colors.get(fruit, "unknown")
    
    return fruit_color("plum")


def ex_1_3():
    """
    Exercise 1.3 (1p)
    Return a comma-separated string of numbers from range_start to range_stop.
    """
    # TODO: Write your code here
    def print_range(start, stop):
        return ",".join(str(i) for i in range(start, stop + 1))
    
    return print_range(25, 46)


def ex_1_4():
    """
    Exercise 1.4 (1p)
    Return a comma-separated string of numbers from range_start down to range_stop.
    """
    # TODO: Write your code here
    def print_range_reversed(start, stop):
        return ",".join(str(i) for i in range(start, stop - 1, -1))
    
    return print_range_reversed(46, 25)


def ex_1_5():
    """
    Exercise 1.5 (1p)
    Return a comma-separated string of numbers between two values, handling both ascending and descending ranges.
    """
    # TODO: Write your code here
    def print_any_range(start, stop):
        if start <= stop:
            return ",".join(str(i) for i in range(start, stop + 1))
        else:
            return ",".join(str(i) for i in range(start, stop - 1, -1))
    
    return print_any_range(25, 46)


def ex_1_6():
    """
    Exercise 1.6 (1p)
    Return a string repeated a specified number of times.
    """
    # TODO: Write your code here
    def string_repeat(s, times):
        return s * times
    
    return string_repeat("grey", 12)


def ex_1_7():
    """
    Exercise 1.7 (1p)
    Return True if value is strictly between two numbers, otherwise False.
    """
    # TODO: Write your code here
    def in_range(start, stop, value):
        return start < value < stop    
    return in_range(131, 547, 434)


def ex_1_8():
    """
    Exercise 1.8 (1p)
    Convert degrees to radians, rounded to 4 decimals.
    """
    # TODO: Write your code here
    def degrees_to_radians(degrees):
        return round(math.radians(degrees), 4)
    
    return degrees_to_radians(32)


def ex_1_9():
    """
    Exercise 1.9 (1p)
    FizzBuzz from start to stop as a comma-separated string.
    """
    # TODO: Write your code here
    def fizz_buzz(start, stop):
        if stop <= start:
            return "Stop must be greater than start"
        result = []
        for i in range(start, stop + 1):
            if i % 15 == 0:
                result.append("Fizz Buzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return ",".join(result)
    
    return fizz_buzz(1, 30)


# ----------------------
# Section 2: Extra assignments
# ----------------------

def ex_2_1():
    """
    Exercise 2.1 (3p)
    Return sums of player and dealer hands as a formatted string.
    """
    # TODO: Write your code here
    def print_sum(player_hand, dealer_hand):
        return f"Player: {sum(player_hand)}, Dealer: {sum(dealer_hand)}"
    
    return print_sum([4, 10, 3], [3, 6, 11])


def ex_2_2():
    """
    Exercise 2.2 (3p)
    Return player and dealer status based on their hand totals.
    """
    # TODO: Write your code here
    def print_result(player_hand, dealer_hand):
        player_total = sum(player_hand)
        dealer_total = sum(dealer_hand)
        
        if player_total == 21:
            player_status = "black jack"
        elif player_total < 21:
            player_status = "safe"
        else:
            player_status = "busted"
        
        if dealer_total == 21:
            dealer_status = "black jack"
        elif 17 <= dealer_total < 21:
            dealer_status = "stop"
        elif dealer_total < 17:
            dealer_status = "safe"
        else:
            dealer_status = "busted"
        
        return f"Player: {player_status}, Dealer: {dealer_status}"
    
    return print_result([4, 10, 3], [3, 6, 11])


def ex_2_3():
    """
    Exercise 2.3 (3p)
    Calculate money after x years of interest, rounded to 4 decimals.
    """
    # TODO: Write your code here
    def calculate_interest(start_money, years, rate_percent):
        return round(start_money * (1 + rate_percent/100) ** years, 4)
    
    return calculate_interest(745, 31, 5)


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
    print("Running Lab 3 - Functions exercises...\n")
    _run_and_print(ex_1_1, "1.1")
    _run_and_print(ex_1_2, "1.2")
    _run_and_print(ex_1_3, "1.3")
    _run_and_print(ex_1_4, "1.4")
    _run_and_print(ex_1_5, "1.5")
    _run_and_print(ex_1_6, "1.6")
    _run_and_print(ex_1_7, "1.7")
    _run_and_print(ex_1_8, "1.8")
    _run_and_print(ex_1_9, "1.9")
    _run_and_print(ex_2_1, "2.1")
    _run_and_print(ex_2_2, "2.2")
    _run_and_print(ex_2_3, "2.3")


if __name__ == "__main__":
    main()
