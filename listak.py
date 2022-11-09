szamok = [11, 42, 53, 10, 42, 6]
#            0       1         2
szavak = ['cica', 'kutya', 'hörcsög']
print(szamok)
print(szavak[1])

uj_elem = input('új elem a szavak listához: ')
szavak.append(uj_elem)

print(f'a szavak a hozzáadás után: {szavak}')