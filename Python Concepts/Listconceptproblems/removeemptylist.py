# Ask the user to enter items separated by spaces
user_input = input("Enter list items separated by spaces: ")
# Convert the input string into a list
my_list = user_input.split()

# Remove empty lists (in this case, just check for '[]' text)
new_list = []

for item in my_list:
    if item != "[]":   # skip empty list representation
        new_list.append(item)

print("Original list:", my_list)
print("List without empty lists:", new_list)

#Input
#Enter list items separated by spaces: 1 [] 2 [] 3 [4,5] hello []
#Original list: ['1', '[]', '2', '[]', '3', '[4,5]', 'hello', '[]']
#List without empty lists: ['1', '2', '3', '[4,5]', 'hello']

