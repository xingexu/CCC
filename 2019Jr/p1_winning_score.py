a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

acounter = a3*3 + a2*2 + a1
bcounter = b3*3 + b2*2 + b1

if acounter>bcounter:
    print("A")

elif bcounter>acounter:
    print("B")

else:
    print("T")
