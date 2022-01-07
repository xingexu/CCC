last4digits=''
for i in range(4):
    n=input()
    last4digits=last4digits+n
if (last4digits[0:1]=='8' or last4digits[0:1]=='9') and (last4digits[3:4]=='8' or last4digits[3:4]=='9') and (last4digits[1:2]==last4digits[2:3]):
    print('ignore')
else:
    print('answer')