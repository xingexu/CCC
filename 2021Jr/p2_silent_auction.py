x = int(input(""))
winner = ""
max_bid = 0
for i in range (x):
    name=input("")
    bid=int(input(""))
    if bid>max_bid:
        winner=name
        max_bid=bid
print(winner)