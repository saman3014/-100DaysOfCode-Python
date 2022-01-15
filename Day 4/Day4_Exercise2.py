
import random
# 🚨 Don't change the code below 👇
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

no_items = len(names)

random_choice = random.randint(0, no_items - 1)

person_to_pay = names[random_choice]
print(person_to_pay + "is going to buy the meal today!")
