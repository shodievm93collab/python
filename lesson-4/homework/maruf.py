# 1. Lug'atni qiymat bo'yicha tartiblang. Lug'atni qiymat bo'yicha saralash (o'sish va pasayish) uchun Python skriptini yozing.

my_dict = {'yabloko': 3, 'banan': 1, 'vishnya': 4, 'apelsin': 2}
sorted_asc = dict(saralangan(my_dict.items(), key=lambda elementi: item[1]))
sorted_desc = dict(sorted(my_dict.items(), key=lambda elementi: item[1], teskari=Rost))
print("Sortirovka po vozrastaniyu:")
chop etish (tartiblangan_ko'tarish)

print("\nSortirovka uchun ubyvaniyu:")
chop etish (tartiblangan_kadr)



# 2. Lug'atga kalit qo'shing. Lug'atga kalit qo'shish uchun Python skriptini yozing.

d = {0: 10, 1: 20}
d[2] = 30
chop etish (d)

# 3. Bir nechta lug'atlarni birlashtiring. Yangi lug'at yaratish uchun quyidagi lug'atlarni birlashtirish uchun Python skriptini yozing.

dic1 = {1: 10, 2: 20}
dic2 = {3:30, 4:40}
dic3 = {5: 50, 6: 60}


natija = {}
d uchun (dic1, dic2, dic3):
natija. yangilash(d)
chop etish (natija)



# 4. Kvadratchalar bilan lug'at yarating. (x, x*x) ko'rinishida raqamni (1 va n oralig'ida) o'z ichiga olgan lug'at yaratish va chop etish uchun Python skriptini yozing.

n = 5
kvadratlar = {x: x*x diapazondagi x uchun(1, n+1)}
chop etish (kvadratchalar)



# 5. Kvadratchalar lug'ati (1 dan 15 gacha). Lug'atni chop etish uchun Python skriptini yozing, bu erda kalitlar 1 dan 15 gacha bo'lgan raqamlar (ikkalasi ham kiritilgan) va qiymatlar kalitlarning kvadratidir.

kvadratlar = {x: x**2 diapazondagi x uchun(1, 16)}
chop etish (kvadratchalar)


# 1. To'plam yarating. To'plam yaratish uchun Python dasturini yozing.

my_set = {1, 2, 3, 4, 5}
chop etish (mening_setim)


# 2. To'plam ustida takrorlash. To'plamlarni takrorlash uchun Python dasturini yozing.

my_set = {'olma', 'banan', 'gilos'}
my_setdagi element uchun:
chop etish (element)


# 3. To'plamga a'zo(lar)ni qo'shing. To'plamga a'zo(lar)ni qo'shish uchun Python dasturini yozing.

my_set = {1, 2, 3}
my_set.add(4)
print("4 qo'shgandan keyin:", my_set)
my_set.update([5, 6, 7])
print("5, 6, 7 qo'shgandan keyin:", my_set)



# 4. To'plamdan element(lar)ni olib tashlang. Berilgan to'plamdan element(lar)ni olib tashlash uchun Python dasturini yozing.


my_set = {1, 2, 3, 4, 5}

my_set.remove(3)
print("olib tashlash(3):", my_set)


my_set.discard(10)
print("discard(10):", my_set)


o'chirildi = my_set.pop()
print(f"pop(): {o'chirildi}, o'rnating: {mening_set}")

my_set.clear()
print("clear():", my_set)



#. 5. To'plamda mavjud bo'lsa, elementni olib tashlang. Agar to'plamda mavjud bo'lsa, to'plamdan elementni olib tashlash uchun Python dasturini yozing.
my_set = {1, 2, 3, 4, 5}

element = 3

my_setdagi element bo'lsa:
my_set.remove(element)
print(f"{element} olib tashlandi: {my_set}")
boshqa:
print(f"{element} to'plamda yo'q: {my_set}")
