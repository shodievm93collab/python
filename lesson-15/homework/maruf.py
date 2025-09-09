import sqlite3

def main():
# Ma'lumotlar bazasi fayliga ulaning (yoki yarating).
conn = sqlite3.connect('star_trek_roster.db')
kursor = conn.cursor()

# Ro'yxat jadvalini yarating
kursor.execute('''
AGAR MAVJUD BO'lmasa JADVAL YARATING Roster (
TEXT nomi,
Turlar TEXT,
Yoshi INTEGER
)
''')

# Dastlabki ma'lumotlarni kiriting
roster_data = [
('Benjamin Sisko', 'Inson', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Neris', 'Bajoran', 29)
]
cursor.executemany('Rosterga INSERT INTO (Ism, tur, yosh) VALUES (?, ?, ?)', roster_data)
conn.commit()

# Jadzia Dax nomini Ezri Daxga yangilang
kursor.execute('''
Ro'yxatni YANGILASH
SET nomi =?
QAYERDA Ism =?
''', ('Ezri Dax', 'Jadzia Dax'))
conn.commit()

# Bajoran deb tasniflangan har bir kishining ismini va yoshini tanlang
kursor.execute('''
TANLANGAN ism, yosh ro'yxatidan QAYERDA Turlar =?
''', ('Bajoran',))

bajorans = cursor.fetchall()
print("Bajoranslar ro'yxatda:")
bajoranlarda ism, yosh uchun:
chop etish(f"Ism: {ism}, Yoshi: {age}")

# Tozalash
cursor.close()
conn.close()

agar __name__ == "__asosiy__":
asosiy()
