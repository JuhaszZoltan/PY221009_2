import random

# üres lista létrehozása
lista = []
# a listához hozzáadok 10db, 2számjegyű véletlen számot:
for x in range(10):
    lista.append(random.randint(10, 99))
# lista elemeinek kiírása:
print(lista)


print(f'lista elemeinek száma: {len(lista)}')

# összegzés (szorozatszámítás) tétele:
osszeg:int = 0
for szam in lista:
    osszeg += szam
print(f'lista elemeinek összege: {osszeg}')
print(f'lista elemeinek átlaga: {osszeg/len(lista)}')

# szélsőérték meghatározás tétele:
maxi = 0
for i in range(1, len(lista)):
    if lista[i] > lista[maxi]:
        maxi = i
print(f'a legnagyobb elem idenxe: {maxi}')
print(f'a legnagyobb elem értéke: {lista[maxi]}')

mini = 0
for i in range(1, len(lista)):
    if lista[i] < lista[mini]:
        mini = i
print(f'a legkisebb elem idenxe: {mini}')
print(f'a legkisebb elem értéke: {lista[mini]}')

# megszámlálás tétele:
# (pl.: 3-al osztható számok száma)
db = 0
for szam in lista:
    if szam % 3 == 0:
        db += 1
print(f'3-al osztható számok száma a listában: {db}')

# kiválasztás
    # [!!!CSAK akkor használható,
    # ha a kiválasztott elem BIZTOSAN
    # benne van a sorozatban!!!]

kiv:int = int(input('melyik szám indexe kell? '))
i = 0
while lista[i] != kiv:
    i += 1
print(f'elem indexe: {i}')

# eldöntés
# (pl. van-e 7el osztható elem a listában?)
i = 0
while i < len(lista) and lista[i] % 7 != 0:
    i += 1
if i < len(lista): print('VAN benne 7el osztható szám')
else: print('NINCS benne 7el osztható szám')

# lineáris keresés
# (pl. van-e 7el osztható elem a listában, és ha van, akkor hol?)
i = 0
while i < len(lista) and lista[i] % 7 != 0:
    i += 1
if i < len(lista):
    print('VAN benne 7el osztható szám')
    print(f'ez a {i}. indexű elem')
else: print('NINCS benne 7el osztható szám')

# http://info.nytta.hu/temak/prog/Programozasi_tetelek.pdf