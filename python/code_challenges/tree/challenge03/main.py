from challenge03 import conver_to_BTS,print_BTS


# test cases
nums1 = [0, -3, -10, 5, 9]
tree1 = conver_to_BTS(nums1)
print(print_BTS(tree1))  # Expected Output: [0, -3, 9, -10, None, 5]

nums2 = [3, 1]
tree2 = conver_to_BTS(nums2)
print(print_BTS(tree2))  
