programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}
#Retrieving itmes from the dictionary.
print(programming_dictionary["Bug"])

#Adding itmes to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary.
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in the dictionary.
programming_dictionary["Bug"] = "Yo"
print(programming_dictionary)

#Loop through a dictionary.
for thing in programming_dictionary:
  print(thing) #prints the keys only
  print(key) #prints the keys in the dictionary
  print(programming_dictionary[key]) #print the keys with the values
