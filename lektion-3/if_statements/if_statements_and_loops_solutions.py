# -*- coding: utf-8 -*-
"""
Solutions – Lab 2 (Python)
"""

def ex_1_1():
    card1, card2, card3, card4, card5 = 4, 2, 7, 1, 11
    result = card1 + card2 + card3 + card4 + card5
    return result


def ex_1_2():
    card1, card2, card3, card4, card5 = 4, 2, 7, 1, 11
    total = card1 + card2 + card3 + card4 + card5
    return "busted" if total > 21 else "safe"


def ex_1_3():
    card1, card2, card3 = 4, 2, 7
    total = card1 + card2 + card3
    if total < 21:
        return "safe"
    elif total > 21:
        return "busted"
    else:
        return "black jack"


def ex_1_4():
    dealer1, dealer2, dealer3 = 1, 6, 7
    total = dealer1 + dealer2 + dealer3
    if total < 17:
        return "pick"
    elif 17 <= total < 21:
        return "stop"
    elif total == 21:
        return "black jack"
    else:
        return "busted"


def ex_2_1():
    my_fruit = "plum"
    match my_fruit:
        case "banana":
            return "The banana is yellow."
        case "apple":
            return "The apple is green."
        case "kiwi":
            return "The kiwi is green."
        case "plum":
            return "The plum is purple."


def ex_2_2():
    my_fruit = "pear"
    match my_fruit:
        case "banana":
            return "The banana is yellow."
        case "apple":
            return "The apple is green."
        case "kiwi":
            return "The kiwi is green."
        case "plum":
            return "The plum is purple."
        case _:
            return "That is an unknown fruit."


def ex_3_1():
    number = 481
    for _ in range(10):
        number += 6
    return number


def ex_3_2():
    number = 551
    for _ in range(10):
        number -= 8
    return number


def ex_3_3():
    numbers = []
    for i in range(22, 46):
        if i % 2 == 0:
            numbers.append(str(i))
    return ",".join(numbers)


def ex_4_1():
    value = 10
    steps = 0
    while value < 481:
        value += 6
        steps += 1
    return steps


def ex_4_2():
    value = 551
    steps = 0
    while value > 0:
        value -= 8
        steps += 1
    return steps


def ex_4_3():
    numbers = []
    i = 28
    while i <= 63:
        if i % 5 == 0 or i % 7 == 0:
            numbers.append(str(i))
        i += 1
    return ",".join(numbers)
