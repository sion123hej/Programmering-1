# uppgift 2
import os
import random


print("Välkommen!")

stop = input("Q om du vill avsluta annat = fortsätt!: ")
 

if stop == "q" or stop == "Q":
     print("Hejdå")
     quit()
else:
   print(stop)
   print("Fortsätt använda programmet då!: ")
 

    # uppgift 3
ord = input("Skriv in ett ord som ska upprepas 10 gånger:")
for i in range(11):
  print(ord)


  #  uppgift 4
for i in range(1,11):
  print(i)

      # uppgift 5
tal = int(input("Ge mig ett tal"))
for i in range(1,(tal)+1):
   print(i)

# uppgift 6
first = [1,2,3,4,5,6,7,8,9,10,11,12]
second = [1,2,3,4,5,6,7,8,9,10,11,12]

for x in first:
  for y in second:
   svar = x * y
   print(x,"x", y , "=" , svar)