def gridAplha():
    k = 0
    l = 26
    alpha = []
    for j in range(26):
        alpha.append([chr(i%26 + 65) for i in range(k, l)])
        k+=1
        l+=1
    return alpha
    
def keyLength(Code, key):
    n = len(Code)
    while len(key) < n:
        key = key + key
        
    if len(key) >= n:   
        newKey = key[0:n]
        
    return newKey
        
def Encrypt(Code , Key):
    res = ''
    key = keyLength(Code, Key)
    grid = gridAplha()
    for i in range(len(Code)):
        xcoor = ord(Code[i]) - 65
        ycoor = ord(key[i]) - 65
        res += grid[xcoor][ycoor]
    print("The encrypted code is :", res)
    return res

def Decrypt(Res, Key):
    key = keyLength(Res , Key)
    grid = gridAplha()
    Code = ''
    for i in range(len(Res)):
        ycoor = ord(key[i]) - 65
        x = 0
        for item in grid[ycoor]:
            if item == Res[i]:
                Code += grid[0][x]
            else: 
                x += 1
    print('The decrypted code is :',Code)
    
Code = input("Enter the code to be encrypted (Capital Only) :" )
KEY = input("Enter the key (Capital only) :" )
Result = Encrypt(Code, KEY)
Decrypt(Result, KEY)
