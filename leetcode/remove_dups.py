def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    copy_index = 1
    for index in range(1, len(nums)):
        if nums[index] != nums[index - 1]:
            nums[copy_index] = nums[index]
            copy_index += 1
        else:
            nums[copy_index] = nums[index]
        
    print nums
    return copy_index


print removeDuplicates([1, 1, 2])
