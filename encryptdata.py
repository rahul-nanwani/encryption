import shutil, os, hashlib    #importih os and hashlib

def menu():                  #defining the function menu
    print('1. Encrypt')      #defifn the different choices of the menu
    print('2. Decrypt')
    print('3. Exit')

def encrypt(string):    #creating the function encrypt
    cipher = ''
    for char in string:
        if char.isupper():
            cipher = cipher + chr((ord(char) + 18 - 65) % 26 + 65)  #this operates on uppercase letters
        elif char.islower():
            cipher = cipher + chr((ord(char) + 18 - 97) % 26 + 97)  #this operates in lower case letters
        else:
            cipher = cipher + char   #in cipher = 3 then A will be operated as C

    return cipher #returns the value

def decrypt(string):        #creating the function Decrypt
    cipher = ''
    for char in string:
        if char.isupper():
            cipher = cipher + chr((ord(char) - 18 - 65) % 26 + 65)  #operates on upper case letters
        elif char.islower():
            cipher = cipher + chr((ord(char) - 18 - 97) % 26 + 97)  #operates on lowercase letters
        else:
            cipher = cipher + char  #does not make changes to the integer part of the string

    return cipher

menu()          #a menu function created
ch = int(input('Select an operation: '))        #storing the input in ch variable

while ch != 3:
    if ch == 1:     #acts when ch = 1
        browse = input('Enter the location: ')  #print commands for the encryption process
        code_01 = input('Set a passcode: ')     #print command to ask and store the password
        code_02 = input('Confirm passcode: ')   #to verify the input in password field


        hash = hashlib.sha512()       #calling SHA512
        hash.update(('%s' % (code_01)).encode('utf-8'))     #to pass variable
        password_hash = hash.hexdigest()

        if (code_01 == code_02):  #after the field verifiction in the password tab this statement operates
            shutil.move(browse, 'C:\\EncryptData\\data.txt')        #moves the  file to the given location

            file = open("data.txt", "r")        #opens the file in read only mode
            data = file.readlines()             #reads the data
            data_len = len(data)                #counts the length of data
            mid_len = data_len // 2             #mid defined at 1/2 lento split

            en = open("encoded.txt", "w")       #the ciphered ad hashed data shifts to this location

            i = 0
            while i != data_len:                #increments the value of i till it reaches the end to encode the data
                en.writelines(encrypt(data[i]))
                i += 1

            en.close()                          #closes the data file
            file.close()                        #closes the encoded file

            en_01 = open("encoded.txt", "r")    #opens the encoded file as read only
            split_01 = open("encoded(01).txt", "w") #first half of the encoded data is refered in this file
            en_data_01 = en_01.readlines()      #reads the content of  encoded file
            del en_data_01[mid_len: data_len]   #delets the code away from the mid position
            en_data_01.insert(0, '\n')
            en_data_01.insert(0, password_hash) #the first line pf the encoded data is the hashed password
            split_01.writelines(en_data_01)     #adds data of en data 01 to  split 01
            split_01.close()                    #closes the split 01 file
            en_01.close()                       #closes the en 01 file

            en_02 = open("encoded.txt", "r")    #encoded data file in opened
            split_02 = open("encoded(02).txt", "w")#encoded 02  file  is defined
            en_data_02 = en_02.readlines()      #reads the data of the encoded data file
            del en_data_02[0: mid_len]          #deleats the data previous to mid
            en_data_02.insert(0, '\n')          #shifts the 2nd half of the encoded data
            en_data_02.insert(0, password_hash) #inserts the hashed password in the first lie 0f the en data 02
            split_02.writelines(en_data_02)     #wites the data from en data 02 to split data 02
            split_02.close()                    #closes  the split02 file
            en_02.close()                       #closes the en 02 file

            print('Data encrypted successfully!')
            browse_01 = input('Enter a location to save first file: ')  #asks the location of the 1st half file tbs
            browse_02 = input('Enter a location to save second file: ') #asks the locatin of the 2nd half   file tbs
            shutil.move('C:\\EncryptData\\encoded(01).txt', browse_01)  #moves the given file in the specified location
            shutil.move('C:\\EncryptData\\encoded(02).txt', browse_02)  #moves the given file in the specified loacation
            print('Files saved successfully!')
            os.remove('data.txt')               #removes the data file
            os.remove('encoded.txt')            #removes the encoded file

        else:
            print('Passcodes did not match!')   #when passwords do not match

        break

    elif ch == 2:                               #action when the input is 02
        browse_01 = input('Locate 1st file: ')  #aks for the location for the first file
        browse_02 = input('Locate 2nd file: ')  #asks for the location for the second file

        shutil.move(browse_01, 'C:\\EncryptData\\encoded(01).txt')#moves the file to the given location
        shutil.move(browse_02, 'C:\\EncryptData\\encoded(02).txt')

        en_01 = open("encoded(01).txt", "r")    #opens the specific file in read only format
        en_02 = open("encoded(02).txt", "r")    #opens the specific filein read only format
        data_01 = en_01.readlines()             #reads the data in the specific file
        data_02 = en_02.readlines()
        code_01 = data_01[0]                    #reads the first line of the file
        code_02 = data_02[0]                    #reads the first line of the file
        en_02.close()
        en_01.close()                           #closes the specific  file

        if (code_01 == code_02):                #comparesthe first line of both the files
            code = input('Enter the passcode: ')#reads the password
            hash = hashlib.sha512()             #compares the password by hashing
            hash.update(('%s' % (code)).encode('utf-8'))
            password_hash = hash.hexdigest()
            password = password_hash + '\n'
            if (code_01 == password):           #decodes the file
                del data_01[0]                  #removes the dat 01 and data 02 file
                del data_02[0]
                merge = open("temp.txt", "w")   #creates and opens the file temp .txt
                merge.writelines(data_01)       #writes the data 01 file in merge file
                merge.writelines(data_02)       #wirtes the data 02 file in the merge file
                merge.close()                   #closes the merge  file

                temp = open("temp.txt", "r")    #opens the temp file
                decoded = open("decoded.txt", "w")#creates and opens the file
                data = temp.readlines()         #reads the data of temp to data file
                length = len(data)              #defining length
                i = 0
                while i != length:
                    decoded.writelines(decrypt(data[i]))#decrypts the data one by one line
                    i += 1
                decoded.close()                  #closes the decoded file
                temp.close()                     #coses the temp file

                print('Data decoded successfully!')
                browse = input('Enter a location to save the file: ')#asks for the location to save the data file
                shutil.move('C:\\EncryptData\\decoded.txt', browse)#moves the required file
                print('File saved successfully!') #executes the program
            else:
                print('Incorrect password!')    #when the password is not correct
        else:
            print('Files do not match!')        #when wrong files are inserted
            shutil.move('C:\\EncryptData\\encoded(01).txt', browse_01)
            shutil.move('C:\\EncryptData\\encoded(02).txt', browse_02)
            break

        os.remove("encoded(01).txt")            #removes the specified file
        os.remove("encoded(02).txt")            #removes the specific  file
        os.remove("temp.txt")                   #removes the specific file
        break

    elif ch == 3:
        print('Always keep your data protected.')#when exit fucntion is selected
        break

    else:
        print('Operation Invaild!')             #when value which is not in the menu is entered
        menu()                                  #runs loop again
        ch = int(input('Select an operation: '))#inputs value of ch
