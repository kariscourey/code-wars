def persistence(n):


    def product_calc(foo):

        product = 1

        for i in str(foo):
            product *= int(i)

        return product

    count = 0

    while n > 10:

        n = product_calc(n)
        count += 1

    return count


# print(persistence(39))
# print(persistence(999))
# print(persistence(4))
print(persistence(1))
print(persistence(38791))
print(persistence(416719))


# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)
