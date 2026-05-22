# # print("hello world")

# # start excercise 1

# # a = 10
# # b = 20
# # print(a + b)

# # end excercise 1


# # start excercise 2
# # a = 2
# # b = 2
# # print(a * b)
# # end excercise 2

# # умови в пайтоні

# # age = 10

# # if умова є true:
# #   виконай код який знаходиться в тілі if
# # if age >= 18:
# #     print("age is greater than 18")




# # if age >= 18:
# #     print("age is greater than 18")
# # else:
# #     print("age is less than 18")


# # age = int(input("enter your age: "))

# # print(type(age))

# # if age >= 18:
# #     print("age is greater than 18")
# # else:
# #     print("age is less than 18")

# # if age > 18:
# #     print("age is greater than 18")
# # elif age < 18:
# #     print("age is less than 18")
# # else:
# #     print("age is equal to 18")


# # age > 20 and age < 30

# # age = int(input("enter your age: "))

# # if age > 20 and age < 30:
# #     print("age is between 20 and 30")
# # elif age > 30 and age < 40:
# #     print("age is between 30 and 40")
# # elif age > 40 and age < 50:
# #     print("age is between 40 and 50")
# # else:
# #     print("age is less than 20 or greater than 50")

# day = 4

# if day == 1:
#     print("monday")
# elif day == 2:
#     print("tuesday")
# elif day == 3:
#     print("wednesday")
# elif day == 4:
#     print("thursday")
# elif day == 5:
#     print("friday")
# elif day == 6:
#     print("saturday")
# elif day == 7:
#     print("sunday")


# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit) #виводить кожен фрукт з списку fruits
#     if fruit == "banana": #якщо фрукт є бананом, то завершуємо цикл
#         break


# numbers = [1, 2, 3, 4, 5]
# print()
# print(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]) #виводить суму всіх чисел з списку numbers
# totalSum = 0
# totalSum += numbers[0]
# totalSum += numbers[1]
# totalSum += numbers[2]
# totalSum += numbers[3]
# totalSum += numbers[4]
# totalSum = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
# print(totalSum) #виводить суму всіх чисел з списку numbers



# for number in numbers:
#     totalSum += number #додає кожне число з списку numbers до змінної totalSum

# numbers = [1, 2, 3, 4, 5]
# totalSum = 1
# for number in numbers:
#     totalSum *= number

# print(totalSum) #виводить суму всіх чисел з списку numbers


# numbers = [1, 2, 3, 4, 5]
# totalSum = 1
# for number in numbers:
#     if number % 2 == 0:
#         totalSum *= number

# print(totalSum)