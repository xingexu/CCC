previous_direction = ""

while True:
    x = input()
    if x =='99999':
        break
    
    y=int(x[0])+int(x[1])
    direction = ""
    if y==0:
        direction = previous_direction
    elif y%2==1:
        direction ="left"
    elif y%2==0:
        direction ="right"
    
        
    print(direction, x[2:])
    previous_direction = direction
