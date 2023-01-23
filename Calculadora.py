a=int(input("Introduce un digito= "))
b=int(input("Introduce un digito= "))
potencia=input("Quieres elevarlo a algo? [Si/No] = ")
print(potencia)

if potencia=="Si":
    potencia2=int(input("Introduce un digito= "))
elif potencia=="No":
    potencia2=int(1)
else:
 print("Pero bueno tu eres tonto")

sign=input("Introduce el tipo de operacion (+,-,/,*) = ") 

if sign == "+":
    print(pow((a+b),potencia2))
elif sign == "-":
    print(pow((a-b),potencia2))     
elif sign == "/":
     print(pow((a/b),potencia2))
elif sign =="*":
     print(pow((a*b),potencia2))
else:
  print("Que coño haces")