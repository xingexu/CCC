bigX = 0
bigY = 0
littleX = 100
littleY = 100
num = int(input())
for i in range(num):
    currentline = input().split(",")
    currentX=int(currentline[0])
    currentY=int(currentline[1])
    if currentX >= bigX:
        bigX=currentX+1
    if currentX <=littleX:
        littleX = currentX-1
    if currentY >= bigY:
        bigY=currentY+1
    if currentY <=littleY:
        littleY = currentY-1
print(str(littleX) + "," + str(littleY))
print(str(bigX) + "," + str(bigY))
