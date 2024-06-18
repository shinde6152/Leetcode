# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def return_sum_indices(nums):
    ii=0
    for i in nums:
        print("i ",i)
        for j in range(1,len(nums)+1):
            if i+nums[j]==9:
                print(ii,j)
                break
        ii=ii+1
        break
        

return_sum_indices([2,8,11,7,6])