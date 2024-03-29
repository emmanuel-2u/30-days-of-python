import numbers

def is_numeric(num):
    return isinstance(num, numbers.Number)

def add_nums(*nums):
    for num in nums:
        if not is_numeric(num):
            return 'All arguments must be a number'
    return sum(nums)

print(add_nums(20, 30, 'string', 40))
print(add_nums(20, 30, 40))