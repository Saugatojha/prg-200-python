# created 3 lists 
my_list = ["apple", "banana", "cherry"]
# prints apple and banana as 0 is apple banana is 1 in terms of position
print(my_list[0])
print(my_list[1])
# prints second item
my_list.append("mango")
# by using this with append mango is added
# prints everything
print(my_list)
# opens a csv file
f = open("list.txt", "w")
for i in my_list:
    f.write(i + "\n")
f.close()

f = open("list.txt", "r")
print(f.read())
f.close()


my_tuple = ("red", "green", "blue")

print(my_tuple[0])
print(my_tuple[1])

my_tuple = my_tuple + ("yellow",)
print(my_tuple)

f = open("tuple.txt", "w")
for i in my_tuple:
    f.write(i + "\n")
f.close()

f = open("tuple.txt", "r")
print(f.read())
f.close()


import csv

my_dict = {"name": "John", "age": 20, "grade": "A"}

print(my_dict["name"])
print(my_dict["age"])

my_dict["city"] = "Kathmandu"
print(my_dict)

f = open("dict.csv", "w", newline="")
# open csv file
w = csv.writer(f)
# this creates writer object
w.writerow(["key", "value"])
# write header row
for k, v in my_dict.items():
    w.writerow([k, v])
f.close()

# reads csv file
f = open("dict.csv", "r")
# reads that file
r = csv.reader(f)
for row in r:
    print(row)
    # file closure
f.close()

# creates a set 
my_set = {1, 2, 3}
# using loop we give a range and it prints
for i in my_set:
    print(i)
# adds a new value 4 
my_set.add(4)
print(my_set)
# logic is this converts num to strign and writes each item and prints the file
f = open("set.txt", "w")
for i in my_set:
    f.write(str(i) + "\n")
f.close()

f = open("set.txt", "r")
print(f.read())
f.close()