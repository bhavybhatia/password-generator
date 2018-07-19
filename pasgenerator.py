import random
chars="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*"
len=int(input("Enter Length of password : "))
n=int(input("Enter number of passwords you want : "))
passwords=''
for i in range(n):
  passwords=''
  for c in range(len):
    passwords+=random.choice(chars)

  print(passwords)
