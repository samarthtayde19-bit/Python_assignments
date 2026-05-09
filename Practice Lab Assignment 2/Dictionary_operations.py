# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}
# write your code here...
print("Original Dictionary:", student)

# Insertion
k = int(input())
v = input()
student[k] = v
print("After Insertion:", student)

# Update
k = int(input())
v = input()
if k in student:
    student[k] = v
print("After Update:", student)

# Deletion
k = int(input())
if k in student:
    del student[k]
print("After Deletion:", student)

# Traversal
print("Traversing Dictionary:")
for key, value in student.items():
    print(key, ":", value)