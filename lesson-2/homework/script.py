# Extract Car Names

txt = 'LMaasleitbtui'
txt[::2]

# Extract Car Names

txt = 'LMaasleitbtui'
txt[1::2]

# Quyidagi matndan shaxs qayerdan ekanligini ajrating: txt = "I'm John. I am from London"

txt = "I'm John. I am from London"

parts = txt.split("I'm John. I am from ")
print(parts)

#Foydalanuvchi kiritgan matnni teskari qilib chiqaradigan dastur yozing.

txt = "matn"
txt[::-1]

# 5 ta meva nomidan iborat ro‘yxat yarating va uchinchi mevani chop eting.

fruits = ["olma", "banan", "anor", "nok", "apelsin"]

print("Uchinchi meva:", fruits[2])

# Ikkita sonlar ro‘yxatini yarating va ularni birlashtiring.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Birlashtirilgan ro'yxat:", combined_list)

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
