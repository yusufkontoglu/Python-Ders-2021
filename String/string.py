# String formatlama

isim = 'Yusuf'
yas = 18
isOnline = True

# print('Benim ismim '+ name +'. '+ str(yas) +' yaşındayım. Çemviriçiyim.')

# {} .format
result = 'Benim ismim {} {} yaşındayım. {}'.format(isim, yas, isOnline)

# {0} .format
result = 'Benim ismim {0} {1} yaşındayım. {2}'.format(isim, yas, isOnline)

# {param} .format
result = 'Benim ismim {i} {y} yaşındayım. {o}'.format(i = isim, y = yas, o = isOnline)

# f" {param}
result = f'Benim ismim {isim} {yas} yaşındayım. {isOnline}'

#print(result)

# Metodlar

text = "Benim ismim Yusuf. 18 yaşındayım."

# count
result = text.count('i')

# upper()
result = text.upper()

# lower()
result = text.lower()

# title()
result = text.title()

# capitalize()
result = text.capitalize()

# strip()
result = text.strip()

# split()
result = text.split('.')

# join(param)
splittedText = text.split('.')
result = '.'.join(splittedText)

# find(param)
result = text.find('Yusuf')

# startswith(param)
result = text.startswith('B')

# endwith(param)
result = text.endswith('f')

# replace(param, param)
result = text.replace('ı','i').replace('ş','s')

# center(param, param)
result = text.center(64,'#')

result = text[0:15] + text[15:]

print(result)