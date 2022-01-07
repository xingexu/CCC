N = int(input())

amount = []
letters = []
decoded = []

for i in range (0,N):
    line = input().split(" ")
    num = int(line[0])
    amount.append(num)
    letter = line[1]
    letters.append(letter)

for i in range(0,N):
    decoded.append(amount[i]*letters[i])

print(*decoded,sep="\n")