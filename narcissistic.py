def narcissistic( value ):
    # Code away

    sum = 0
    string = str(value)

    for i in string:
        sum += int(i) ** len(string)

    return sum == value


def narcissistic2(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
