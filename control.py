# #Arithmetic Operators
# num1 = 34
# num2 = 45
# print(num1 + num2)

# a = 10
# b = 5
# print(a - b)


# x = 5
# y = 15
# print(x * y)

# p = 20
# q = 4
# print(p / q)

# k = 10
# o = 2
# print(k // o)

# m = 4
# n = 3
# print(m ** n)

# e = 10
# f = 10
# print(e % f)


# #Assignment Operators
# b = 10
# b += 5
# print(b)

# a = 20
# a -= 10
# print(a)


# k = 50
# k *= 5
# print(k)


# o = 100
# o /= 5
# print(o)


# j = 15
# j//= 3
# print(j)

# f = 90
# f %= 10
# print(f)

# # comparision operators
# a = 30
# b = 20
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# num1 == num2
# print("waa isku mid")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# num1 != num2
# print("waa kala duwan yihiin")





# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# num1 > num2
# print("num1 is greeter than num2")

# logical operators

# a = 10
# b = 60
# print(a > 50 and b > 50 )
# print(a < 50 or b < 50)

# c = 89
# b = 20
# print(not(c > 50 and b > 50))
# print(not(c > 50 and b < 50))


# #control flow statements
# age = int(input("Enter your age: "))
# if age > 18:
#     print("waa codeyn kartaa")
# elif age == 18:
#     print("waa codeyn kartaa")
# else:
#     print("ma code kartid")


# while True:
#     score = int(input("Enter your score: "))

#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     else:
#             grade = "F"


#     print(f"your grade is :{grade}")

# age = 29
# ticket_price = True
# if age >= 18:
#     print("you can watch the movie")
#     if ticket_price:
#         print("welcome to the movie")
#     else:
#         print("you need to pay for the ticket")

# else:
#     print("you cannot watch the movie")



age = int(input("Enter your age: "))
ticket_price = input("Do you have a ticket? (yes/no) :")
if age >= 18:
    if ticket_price.lower() == "yes":
        print("you can watch the movie")
    else:
        print("you need to pay for the ticket")
else:
    print("you cannot watch the movie")