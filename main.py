import random
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



dlugosc_hasla  = int(input("Podaj dlugosc hasla"))
haslo = ""
for x in range(dlugosc_hasla):
  x = random.choice(alfabet)
  haslo += x
print(haslo)