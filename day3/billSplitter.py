print("Bill Splitter")

# ** Take bill amount total input

billAmount = int(input("Enter the bill amount total: "))

# ** Take the number of people

noOfPeople = int(input("How many people are at the table? Enter response as a whole number: "))

# ** Calculate each person's part

splitPerPerson = billAmount / noOfPeople

# ** Print the split

print("Each person must pay:", splitPerPerson)