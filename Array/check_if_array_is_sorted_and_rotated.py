def sorted_array(nums):
    n = len(nums)
    count = 0
    if nums[0] < nums[-1]:
        count += 1
    
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            count += 1
        
        if count > 1:
            return False
        
    return True