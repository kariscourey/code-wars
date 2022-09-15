# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7

# Places
    # 1234
    # 1 in 1000s, 2 in 100s, 3 in 10s, 4 in 1s


def string_to_number(s):

#     return int(s)

    # str_to_int = [0,1,2,3,4,5,6,7,8,9]

    # Lookup table
    str_to_int = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }


    final_number = 0
    power = 0

    for char in s[::-1]:
        if char == "-":
            final_number = -final_number
        else:
            final_number += str_to_int[char] * 10 ** power


    # for char in s[::-1]:
    #     if char == "-":
    #         final_number = -final_number
    #     else:
    #         final_number += * (10 ** power)
    #     power += 1
    # return final_number

    # for i in s[::-1]:
    #     if i == "-":
    #         final_number = -final_number
    #     else:
    #         number = int(i) * (10 ** power)
    #         final_number += number
    #     power += 1

    # return final_number

#     is_negative = s[0] == "-"

#     if is_negative:
#         s_adj = s[1::]
#     else:
#         s_adj = s
#     for i in s_ajd[::-1]:
#         number += int(i) * 10 ** power
#         index += 1

#     if is_negative:
#         return number * -1
#     else:
#         return number

#     return number
