def sum_two_smallest_numbers(numbers):
    min_val = min(numbers)
    numbers.remove(min(numbers))
    return min(numbers) + min_val

lst = [19, 5, 42, 2, 77]
print(sum_two_smallest_numbers(lst))

# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])

# def sum_two_smallest_numbers(num_list):
#     num_list.sort()
#     return num_list[0] + num_list[1]

# def sum_two_smallest_numbers(numbers):
#     smallest1 = None
#     smallest2 = None
#     for n in numbers:
#         if not smallest1 or n < smallest1:
#             smallest2 = smallest1
#             smallest1 = n
#         elif not smallest2 or n < smallest2:
#             smallest2 = n
#     return smallest1 + smallest2
