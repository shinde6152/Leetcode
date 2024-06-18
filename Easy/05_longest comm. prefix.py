# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def common_prefix(strs):

    mn, mx = min(strs), max(strs)

    for i in range(len(mn)):
        if mn[i] != mx[i]: return mn[:i]
             
        return mn

common_prefix(["flower","flow","flight"])

















