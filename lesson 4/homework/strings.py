
data = {
    'math': 88,
    'english': 75,
    'science': 93,
    'history': 82
}

asc_sorted = dict(sorted(data.items(), key=lambda item: item[1]))
print("Ascending order:")
print(asc_sorted)

desc_sorted = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("\nDescending order:")
print(desc_sorted)



my_dict = {0: 10, 1: 20}
my_dict [2]=30
print(my_dict)


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

united_dict = dic1|(dic2)|(dic3)
print(united_dict)



n = int(input("Enter a number: "))

squares_dict = {x: x*x for x in range(1, n+1)}

print("Generated Dictionary:")
print(squares_dict)



squares_dict = {x: x**2 for x in range(1, 16)}

print("Dictionary of squares from 1 to 15:")
print(squares_dict)



my_set = {1, 2, 3, 4, 5}

print("Created set:")
print(my_set)



my_set = {'apple', 'banana', 'cherry', 'date', 'banana'}

print("Iterating over the set:")
for item in my_set:
    print(item)



my_set = {'apple', 'banana'}

my_set.add('cherry')

print(my_set)


my_set = {'apple', 'banana'}

my_set.update(['date', 'fig', 'grape'])

print(my_set)



my_set = {'apple', 'banana', 'cherry', 'date'}

my_set.remove('banana')

my_set.discard('fig')  

removed_item = my_set.pop()

print("Updated set after removals:")
print(my_set)

print("\nItem removed using pop():", removed_item)




my_set = {'apple', 'peach', 'banana', 'cherry'}

item_to_remove = 'banana'

if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"'{item_to_remove}' has been removed.")
else:
    print(f"'{item_to_remove}' is not in the set.")


print("Updated set:")
print(my_set)
