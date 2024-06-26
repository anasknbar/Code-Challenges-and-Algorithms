from challenge02 import Node,breadth_first_values_iterative,compare

# test the following: 

# first_tree represented by (f)

f_one = Node(1)
f_two = Node(2)
f_three = Node(3)

f_one.left = f_two
f_one.right = f_three

# second_tree represented by (s)

s_one = Node(1)
s_two = Node(2)
s_three = Node(3)

s_one.left = s_two
s_one.right = s_three


print(breadth_first_values_iterative(f_one))
print(breadth_first_values_iterative(s_one))

print(compare(f_one,s_one)) 
