# https://leetcode.com/problems/permutations/description/

def permute(nums):
    result = []
    permute2(nums, (), result)
    return result

def permute2(nums, perm, result):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not len(nums):
        result.append(perm)
        return
   
    for i, num in enumerate(nums):
        permute2(nums[:i] + nums[i+1:], perm + (num,), result)


if __name__ == '__main__':
    print permute([1, 2, 3])
