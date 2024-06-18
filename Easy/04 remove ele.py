# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

def remove_ele(nums,val):
    new_nums=[]
    new_nums2=[]
    temp_list=[]
    for i in nums:
        if i == val:
            i="_"
            new_nums.append(i)
        else:
            new_nums.append(i)
    for i in new_nums:
        if isinstance(i,int):
            new_nums2.append(i)
        elif isinstance(i,str):
            
            temp_list.append(i)
    new_nums2.extend(temp_list)

    print(new_nums2)


remove_ele([3,2,2,3],3)