# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.


from math import floor

def make_readable(seconds):

    # hr = floor(seconds / 3600)
    # seconds -= hr * 3600
    # min = floor(seconds / 60)
    # seconds -= min * 60

    hr = floor(seconds / 3600)
    min = floor(seconds / 60 % 60)
    seconds = floor(seconds % 60)

    return f'{hr:02d}:{min:02d}:{seconds:02d}'

    # return f"{hr:02d}:{min:02d}:{seconds:02d}"


    # hr = int((seconds - seconds % 3600) / 3600)
    # seconds -= hr * 3600
    # min = int((seconds - seconds % 60) / 60)
    # # seconds -= min * 60


# import datetime

# def make_readable(seconds):
#     return str(datetime.timedelta(seconds=seconds))


# def make_readable(seconds):
#     min, sec = divmod(seconds, 60)
#     hr, min = divmod(min, 60)
#     return f"{hr:02d}:{min:02d}:{sec:02d}"



print(make_readable(359999))
print(make_readable(86399))
print(make_readable(366))
print(make_readable(3666))
