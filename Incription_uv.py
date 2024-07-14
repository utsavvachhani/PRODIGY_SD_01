def Encrypted_method(password,key):
    length = len(password)
    Encrypted_password = ""
    i=0
    while i<length :
        if password[i] >= 'a' and password[i] <= 'z':
            Encrypted_password += chr(((ord(password[i]) + key - 97) % 26 )+ 97)
        elif password[i] >= 'A' and password[i] <= 'Z':
            Encrypted_password += chr(((ord(password[i]) + key - 65) % 26 )+ 65)
        else :
            Encrypted_password += password[i]
        i+=1
    return Encrypted_password

def Decrypted_method(password,key):
    length = len(password)
    #key=-key
    Decrypted_password = ""
    i=0
    while i<length :
        if password[i] >= 'a' and password[i] <= 'z':
            Decrypted_password += chr(122-(((122-(ord(password[i]) - key )) % 26 )+1)+1)
        elif password[i] >= 'A' and password[i] <= 'Z':
             Decrypted_password += chr(90-(((90-(ord(password[i]) - key )) % 26 )+1)+1)
        else :
            Decrypted_password += password[i]
        i+=1
    return Decrypted_password


password=input("Enter the Password: ")
#print("Your Enter the Password is "+password)
print("Length of Password is "+str(len(password)))
print("\nKey allways in integer number.")
key=int(input("Enter the keyWord : "))
print("Your Enter  Key is "+str(key))

Encrypted_password=Encrypted_method(password,key)
print("Encrypted Password is "+Encrypted_password)
Decrypted_password=Decrypted_method(Encrypted_password,key)
print("Decrypted Password is "+Decrypted_password)