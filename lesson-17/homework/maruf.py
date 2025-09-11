numpy ni np sifatida import qiling

# 1. Roʻyxatni 1D massiviga aylantiring
original_ro'yxat = [12.23, 13.32, 100, 36.32]
massiv_1d = np.array(original_ro'yxat)
print("1. Asl ro'yxat:", original_ro'yxat)
print("Bir o'lchovli NumPy massivi:", massiv_1d)
chop etish()

# 2. 3x3 matritsa yarating (2 dan 10 gacha)
matrisa_3x3 = np.arange(2, 11).qayta shakllantirish(3,3)
print("2 dan 10 gacha qiymatlarga ega 2. 3x3 matritsa:")
chop etish (matritsa_3x3)
chop etish()

# 3. Null vektor (10) va oltinchi qiymatni yangilang
null_vector = np.zeros(10)
print("3. 10 o'lchamdagi null vektor:")
chop etish (null_vector)

# Eslatma: Oltinchi qiymat indeksi 5 (0ga asoslangan)
null_vector[5] = 11
print("Oltinchi qiymatni 11 ga yangilang:")
chop etish (null_vector)
chop etish()

# 4. 12 dan 38 gacha massiv
arr_12_38 = np.arange(12, 38)
print("4. 12 dan 38 gacha qiymatli massiv:")
chop etish (arr_12_38)
chop etish()

# 5. Massivni Float turiga aylantirish
arr_int = np.array([1, 2, 3, 4])
arr_float = arr_int.astype (float)
print("5. Asl massiv:", arr_int)
print("Float turiga aylantirildi:", arr_float)
chop etish()

# 6. Selsiyni Farengeytga aylantirish
Selsiy = np.massiv([0, 12, 45.21, 34, 99.91])
farengeyt = (selsiy * 9/5) + 32
print("6. Santigrad darajalaridagi qiymatlar:", selsiy)
print("Farengeytdagi qiymatlar:", Farengeyt)
chop etish()

# 7. Massivga qiymatlarni qo'shing
original_arr = np.array([10, 20, 30])
qo'shiladigan_qiymatlar = [40, 50, 60, 70, 80, 90]
new_arr = np.append(original_arr, qo'shiladigan_qiymatlar)
print("7. Asl massiv:", original_arr)
print("Qiymatlar massiv oxiriga qo'shilgandan keyin:", new_arr)
chop etish()

# 8. Massiv statistik funksiyalari
rand_arr = np.random.rand(10) [0,1) ichida # tasodifiy suzuvchi
mean_val = np.mean (rand_arr)
median_val = np.median(rand_arr)
std_dev = np.std (rand_arr)
print("8. Tasodifiy massiv:", rand_arr)
print(f"O'rtacha: {mean_val:.4f}, Median: {median_val:.4f}, Std Dev: {std_dev:.4f}")
chop etish()

# 9. 10x10 massivda min va max ni toping
rand_10x10 = np.random.rand(10, 10)
min_val = np.min(rand_10x10)
max_val = np.max(rand_10x10)
print("9. 10x10 tasodifiy massiv:")
chop etish (rand_10x10)
print(f"Minimal qiymat: {min_val:.4f}, Maksimal qiymat: {max_val:.4f}")
chop etish()

# 10. Tasodifiy qiymatlar bilan 3x3x3 massiv yarating
rand_3d = np.random.rand(3, 3, 3)
print("Tasodifiy qiymatli 10. 3x3x3 massiv:")
chop etish (rand_3d)
