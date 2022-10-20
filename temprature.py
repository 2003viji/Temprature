# This program is for finding the temprature (cel->fahr) and (fahr->cel)

#Celsius to fahrenheit

cel=float(input("Enter the celsius value :"))
print(cel*1.8+32)


#fahrenheit to celsius


fahr=float(input("Enter the fahrenheit  value :"))
val=fahr-32
print(round((val*(round((5/9),4))),4))

