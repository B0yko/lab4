#Task 1
n = int(input("Enter the number of elements in the list (n): "))
numbers = []
for i in range(n):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)
total_sum = sum(numbers)
average = total_sum / n
print("Sum of the numbers:", total_sum)
print("Average of the numbers:", average)

#Task 2
n1 = int(input("Enter the number of elements in the list (n): "))
list = []
for i in range(n1):
    number1 = float(input(f"Enter number {i+1}: "))
    list.append(number1)
m = int(input("Enter the number you will multiply by: "))
print(list)

miltiplied_list = [element * m for element in list]
print(miltiplied_list)

#Task 3
str1 = "spam"
str2 = "ni ! "

a = " The Knights who say , " + str2
print("a) Result:", a)
b = 3 * str1 + 2 * str2
print("b) Result:", b)
c = str1[1]
print("c) Result:", c)
d = str1[1: 3]
print("d) Result:", d)
e = str1[2] + str2[: 2]
print("e) Result:", e)
f = str1 + str2[-1]
print("f) Result:", f)
g = str1.upper()
print("g) Result:", g)
h = str2.upper() * 3
print("h) Result:", h)

#Task 4
print("Task a output: ")
for ch in "ardvark ":
    print(ch)

print("Task b output: ")
for w in " Now is the winter of our discontent . . . " . split():
    print(w)

print("Task c output: ")
for w in "Mississippi ".split("i"):
    print(w, end=" ")
print()

print("Task d output: ")
msg = " "
for s in " secret ".split("e"):
    msg = msg + s
print(msg)

print("Task e output: ")
msg = " "
for ch in " secret ":
    msg = msg + chr(ord(ch) + 1)
print(msg)

#Task 5
person_info = {
    "first_name": "Oleksandr",
    "last_name": "Kolyada",
    "age": 17,
    "city": "Odesa"
}
print("Task 5: ")
print("First Name:", person_info["first_name"])
print("Last Name:", person_info["last_name"])
print("Age:", person_info["age"])
print("City:", person_info["city"])

#Task 6
glossary = {
    "Loop": "A control flow statement that allows code to be executed repeatedly.",
    "Type": "A classification that specifies which kind of value a variable can hold.",
    "List": "An ordered collection of elements that can be of different data types.",
    "Key": "In a dictionary, the identifier used to access or modify the associated value.",
    "Value": "In a dictionary, the data associated with a given key."
}
print()
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")


