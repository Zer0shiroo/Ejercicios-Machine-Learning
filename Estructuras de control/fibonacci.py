n = int(input("Dime un numero"))
x = 1
y=0
z= x
bool = True
print(y)
while(bool):
     if x >= n:
          bool = False
          print(f"La secuencia llega hasta aqui porque tu numero es: {n} y ya se pasaria")
          continue
     print(x)
    
     z = x
     x = x + y
     y = z