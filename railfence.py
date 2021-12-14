def Encrypt(Code, Key):
    rails = [[] for i in range(Key)]
    row  = 0
    dirr   = 1

    for char in Code:
        rails[row].append(char)
        row += dirr

        if row == Key-1 or row == 0:
            dirr = -dirr

    res = ''
    for i in rails:
        for j in i:
            res += j
    print("The encrypted code is :",res)
    return res

def Decrypt(Res, Key):
    rails = [[] for i in range(Key)]
    row = 0
    dirr = 1
    
    length = len(Res)
    
    for char in Res:
        rails[row].append(char)
        row += dirr

        if row == Key-1 or row == 0:
            dirr = -dirr
    
    newRail = [[] for i in range(Key)]
    
    i = 0
    k = 0
    for row in rails:
        for j in range(len(row)):
            newRail[i].append(Res[k])
            k += 1
        i += 1
    
    diir = 1
    col = 0
    Code = ''
    
    for i in range(length):
        Code += newRail[col][0]
        newRail[col].remove(newRail[col][0])
        col += diir

        if col == Key-1 or col == 0:
            diir = -diir 
            
    print('The decrypted code is :',Code)
            
Code = input("Enter the code to be encrypted (Capital Only) :" )
KEY = int(input("Enter the key (number only) :" ))
Result = Encrypt(Code, KEY)
Decrypt(Result, KEY)