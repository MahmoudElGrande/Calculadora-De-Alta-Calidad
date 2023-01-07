#Suma
a=int(input("Introduce un digito= "))
b=int(input("Introduce un digito= "))
sign=input("Introduce el tipo de operacion (+,-,/,*) = ") 
if sign == "+":
    print(a+b)
elif sign == "-":
    print(a-b)     
elif sign == "/":
     print(a/b)
elif sign =="*":
     print(a*b)
else:
  print("Que coño haces")

