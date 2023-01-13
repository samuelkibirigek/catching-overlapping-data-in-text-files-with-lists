with open("file1.txt") as file_1:
    file1_list = file_1.readlines()
    f1_list = [int(n.strip("\n")) for n in file1_list]

with open("file2.txt") as file_2:
    file2_list = file_2.readlines()
    f2_list = [int(n.strip("\n")) for n in file2_list]

result = [n for n in f1_list if n in f2_list]

# Write your code above 👆

print(result)
