# While döngüleri

a = 0
while a <= 10:
    print(a)
    a += 1 # a = a + 1

name = '' # False
while not name.strip():
    name = input('isminizi giriniz: ').strip()
    if name:
        print(f'isminiz {name}')

# For döngüleri

numbers = [1,2,3,4,5]
for num in numbers:
    print(num)


# Tüm listedeki öğrenciler adına belge yazdırma
names = ['Ahmet', 'Mehmet', 'Ali', 'Veli']

for name in names:
    print(f'{name} isimli öğrenci sınavı geçmiştir')

# Döngü metodları

# break continue
i = 0
while i < 9:
    i+=1
    if i % 2 == 0:
        if i == 6:
            continue
        print(i)

# text = 'yazılım dersleri'
for char in text:
    if char == ' ':
        break
    print(char)
print('bitti')

# range(first,last,step)

for num in range(50, 100, 10):
    print(num)
