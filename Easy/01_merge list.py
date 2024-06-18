# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


def merge_list(list1,list2):
    list3=[]
    list3.extend(list1)
    list3.extend(list2)
    list3.sort()
    print(list3,"  Sorted list")

merge_list([1,2,4],[1,3,4])