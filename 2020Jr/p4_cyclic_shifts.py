T = input()
S = input()

list = []
for i in range(len(S)):
    list.append(S[i:]+S[:i])

x = False

for i in list:
    if i in T:
        x = True
        break
if x == False:
    print("no")
else:
    print("yes")