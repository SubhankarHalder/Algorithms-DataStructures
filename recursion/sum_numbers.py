def sum_nums(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum_nums(nums[1:])


print(sum_nums([1, 3, 4, 5, 6, 7, 10]))

