#Examines a potential password's strength, if it isn't strong enough, the program will reject it 
password = input("Enter password: ")
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
special = '!@#$%^&*()_+'
nums = '0123456789'
length = len(password)
c, l, s, n = 0, 0, 0, 0

if(len(password) >= 10):
    for i in password:
        if(i in capital):
            c += 1
        if(i in lowercase):
            l += 1
        if(i in special):
            s += 1
        if(i in nums):
            n += 1

if(c >= 1 and l >= 1 and s >= 1 and n >= 1 and c + l + s + n == length):
    print('Password is strong')
else:
    print('Password is weak. Please try again')
