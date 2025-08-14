# Create a list containing five different fruits and print the third fruit.

fruits = ["olma", "banan", "anor", "nok", "apelsin"]

print("Uchinchi meva:", fruits[2])

# Ikkita sonlar ro‘yxatini yarating va ularni birlashtiring.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Birlashtirilgan ro'yxat:", combined_list)

# Список любимых фильмов
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Pulp Fiction"]

movies_tuple = tuple(favorite_movies)

print("Кортеж фильмов:", movies_tuple)

# Shaharlar ro‘yxatida "Paris" bor yoki yo‘qligini tekshiring va natijani chop eting.

cities = ["London", "New York", "Tokyo", "Paris", "Berlin"]
if "Paris" in cities:
    print("Ro'yxatda Paris bor.")
else:
    print("Ro'yxatda Paris yo'q.")

# Sonlardan iborat ro‘yxatni hech qanday sikl (loop) ishlatmasdan ikki marta takrorlab yangi ro‘yxat yarating.

numbers = [1, 2, 3, 4, 5]

new_list = numbers * 2
print(new_list)


# Sonlardan iborat ro‘yxatda birinchi va oxirgi elementlarning o‘rnini almashtiring.

numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
numbers[3:7]

# Create a list of colors and count how many times "blue" appears in the list.

colors = ["red", "blue", "green", "blue", "yellow", "blue", "purple"]

blue_count = colors.count("blue")

print(f'"blue" appears {blue_count} times in the list.')


# Given a tuple of animals, find the index of "lion".

animals = ("cat", "dog", "lion", "elephant", "tiger")
index_lion = animals.index("lion")

print("Index of 'lion':", index_lion)

# Create two tuples of numbers and merge them into a single tupl
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2

print("Merged tuple:", merged_tuple)

#v Given a list and a tuple, find and print their lengths.

my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3, 4, 5, 6)

list_length = len(my_list)
tuple_length = len(my_tuple)

print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)

# Create a tuple of five numbers and convert it into a list.

my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
print("List:", my_list)

# Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (15, 42, 7, 23, 89, 3)

max_value = max(numbers)
min_value = min(numbers)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

# Create a tuple of words and print it in reverse order.

words = ("apple", "banana", "cherry", "date", "fig")
reversed_words = words[::-1]
print("Reversed tuple:", reversed_words)
