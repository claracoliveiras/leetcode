def containsDuplicate(nums):
    set_nums = set(nums)

    if len(nums) != len(set_nums):
        return True
    return False
    

nums = [1,2,3,4]
print(containsDuplicate(nums))
