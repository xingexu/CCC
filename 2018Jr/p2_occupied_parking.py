spots = int(input())
y_spots = input()
t_spots = input()

count = 0

for i in range(spots):
    if y_spots[i] == "C" and t_spots[i] == "C":
        count=count+1

print(count)