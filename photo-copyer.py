photo1 = open(input('Enter Hardisk: ')+':\\\\Users\\\\'+input('Enter user name: ')+'\\\\'+input('whare is the File? ')+'\\\\'+input('Enter File name: ')+'\\\\'+input('Enter Photo name: '), 'rb')
count = int(input('\nHow much of copy do you need? '))
copy_file = input('\nEnter Hardisk: ')+':\\\\Users\\\\'+input('Enter user name: ')+'\\\\'+input('whare is the File? ')+'\\\\'+input('Enter File name: ')+'\\\\' * count
photo2 = input('Enter copy photo name: ')

for i in range(1, count+1):
   i = open(copy_file+photo2+str(i)+'.png', 'wb')
   i.write(photo1.read())
   i.close()

photo1.close()
print('\nDone!')
   
