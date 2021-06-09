"""
Program menghitung luas segitiga
luas_segitiga = alas * tinggi / 2
"""

alas = 10
tinggi = 6
luas_segitga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitga}')

print('\nMembuat fungsi hitung luas segitiga')


def hitung_luas_segitiga(a, t):
    luas = a * t / 2
    return luas


print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 2)}')
