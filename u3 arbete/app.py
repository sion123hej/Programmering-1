print("Hej välkommen!")


try: 
    age = int(input("Hur gammal är du?"))
    print("du är",age, "gammal")

except:
    print("Du måste skriva din ålder i siffror")





height = float(input("Hur lång är du: "))

if height <= 140: 
    print("Du är för kort")
elif height >= 141:
    print("Du får åka med")




try:
 weight = float(input("Hur mycket väger du?"))
 length = float(input("Hur lång är du?"))
 print("Din bmi är" ,weight / (length ** 2) )
except:
 print("skriv med siffror")



radie = float(input("Ange radien"))
print("Radien är", radie * radie * 3.14)


times = int(input("Skriv hur många tärnngar du vill kasta"))
for i in range(times):   
   print(i)
    
import random 

print(random.randint(1,6))

