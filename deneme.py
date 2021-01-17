arabalar = [ "bmw", "mercedes", "opel", "mazda" ]

result = len(arabalar)
result = [arabalar[0] , arabalar[-1] ]

index = arabalar.index("mazda")
arabalar[index] = "toyota"
result = arabalar

result = arabalar.count("mercedes")
result = 'mercedes' in arabalar

result = arabalar[-2]
result = arabalar[:3]

arabalar[-2:] = ["toyota", "renault"]
result = arabalar


# arabalar.append("audi")
# arabalar.append("nissan")
result = arabalar + [ "audi", "nissan" ]

arabalar.pop()
result = arabalar

arabalar.reverse()
result = arabalar

#print(result)

studentA = [ 'Yiğit', 'Bilgi', 2010, [70, 60, 70] ]
print(studentA)