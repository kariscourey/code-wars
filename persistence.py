def persistence(n):

    if len(str(n)) > 1:

        while product > 10:

            product = 1

            for i in str(n):
                product *= int(i)

        return product

    else:
        return 0

print(persistence(39))
