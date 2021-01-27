# asal sayi

number = int(input('Sayi giriniz:   '))
asalmi = True

for num in range(2,number):
    if number % num == 0:
        asalmi = False
        break

if asalmi:
    print('sayı asal')
else:
    print('sayı asal değil')