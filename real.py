#string 

str1 ="harshada"
str2 ='harshada'
str3 ="""harshada"""
str4 ="harsh'da"
print (str1,str2,str3,str4)

#sting Concatenation
str4 = "harshada"
str5 = "patil"
print(str4 + " " + str5)

#string index

str2 = "harshada"
print(str2[0])
print(str2[4])
print(str2[1])
print(str2[3])

# #string function

str1 = "harshada"
len2 = len(str2)
print (len2)
str6 = "i am learning java"
print (str6.replace ("java","python"))
str = "i am stuading from the imrd"
print(str.endswith("mrd"))
print(str.capitalize())
print(str.find("di"))
print(str.count("r"))
print(str.replace("imrd","youtube"))
print(str.upper())

 #sum of two number

a = 10
b = 20
print("a + b:" )
a = "!!!!!harshu!!!!!!!!"
print (len(a))
print(a)
print(a.upper())
name = "harshada"
print (name)

 #Tuple 

fruits = ("mango","apple","greps","banana")
print ("Tuple:", fruits)

 #Tuple concatenation

frontend = ("html", "css")
backend = ("php", "sql")
fullstack = frontend + backend
print (fullstack)

# Tuple function

name = "Harshada Patil"
print("Original:", name)
print("Upper:", name.upper())
print("lower:", name.lower())
print (len(name))

# if else statement

age = 19
if age >= 18:
    print ("you can able for voting")
else: 
    print ("you can't able for voting")

#list

name = ["mango","apple","greps","banana"]
print (name)

# #List function

a = [1, 2, 3, 4]
a.insert(1,10)
print(a)
a.sort()
print(a)
a.append(5)
print(a)
a.remove(3)
print(a)
a.pop()
print(a)


 # Type Conversion in Python

a = 10          # Integer
b = 5.5         # Float
c = "100"       # String


# # Type Casting
print(a, type(a))
print(b, type(b))
print(c, type(c))


# # Original Types
print(a, type(a))
print(b, type(b))
print(c, type(c))

 # Dictionary 

student = {
    "name" : "harshada",
    "age" : 19 
}
print (student)
print (type(student))
print (student["name"])
print (student["age"])

 # Nested dictionary

student = {
    "name"  : "harshada",
    "student marks" : {
        "phy" : 90,
        "chem": 45,
        "bio": 89

    }
}
print (student)
print (student["student marks"]["bio"])





# # Dictionary Method

print (student.keys())
print (len(list(student.keys())))
print (student.values())
print (student.items())
print (student.get("name"))
student.update({"city" : "shirpur"})

# #set 
# A set can be ignore duplicate value
# set is mutable
collection = { 1, 2,3,3 ,"hello", "world", "hello"}
print (collection)
print (type(collection))
print (len(collection))

set1 = {1,2,3}
set2 = {3,4,5}

print (set1.union(set2))#{1,2,3,4,5}
print (set1.intersection(set2))

# #for loop 
for g in range(3):
    print ("patil")


for g in range(1,6):
        print(g)

# #if statement
age = 13
if age >= 18:
    print ("you can able for voting")
else:
    print ("you can't able for voting")

# condition become true as such loop is reapeted

# # For loop 
for h in range (5):
    print ("harshada")
    
    # print the number is 1 to 50 using for loop

    
# both the while loop and for loop are  print the output as same using diffenet logic  
# print the number is 1 to 50 using for loop

# while loop
# condition become true as such loop is reapeted
       
i = 1
while i <= 100:
    print( i )
    i += 1

    i = 1
    while i <= 5:
        print("harshada")
        i += 1
    

# class     
    # class  student:
    #     name = "harshada"
    #     age = 34
    #     language = "python"

    # print (student.name)
    # print (student.age)
    # print (student.language)

# object calling

    s1= student()
    print (s1.name)
    print (s1.age)
    print (s1.language)
    





