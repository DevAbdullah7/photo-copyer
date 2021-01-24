x = open(input('Enter Hardisk: ')+':\\\\Users\\\\'+input('Enter user name: ')+'\\\\'+input('whare is the File? ')+'\\\\'+input('Enter File name: ')+'\\\\'+input('Enter Photo name: '), 'rb')
k = int(input('How much of copy do you need? '))
l = input('Enter Hardisk: ')+':\\\\Users\\\\'+input('Enter user name: ')+'\\\\'+input('whare is the File? ')+'\\\\'+input('Enter File name: ')+'\\\\' * k
p = input('Enter copy photo name: ')

for i in range(1, k+1):
   i = open(l+p+str(i)+'.png', 'wb')
   i.write(x.read())
