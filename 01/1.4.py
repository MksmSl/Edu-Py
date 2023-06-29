print('Enter the initial number: ', end='')
a=input()
a=int(a)
b=a//100
c=(a-b*100)//10
d=(a-b*100-c*10)
e=d*100+c*10+b
print('The reverse number is:', e)