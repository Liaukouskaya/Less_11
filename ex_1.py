# 11.1 create the generator of geometric progression
a = int(input())
b = int(input())
len_of_generator = int(input())
member_of_geometric_progression = [a*b**(i-1) for i in range(1, len_of_generator+1)] >> int
print(member_of_geometric_progression)
