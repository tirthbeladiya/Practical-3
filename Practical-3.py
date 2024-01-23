fh = open('Practical-3.txt','w')
import random
length = 12
password_list='qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM0123456789!@#$%^&*()<>~=+-_*/'
password=''
i=1
while i<=length:
    password = password + random.choice(password_list)
    i+=1
fh.write(str(password))
fh.close()
