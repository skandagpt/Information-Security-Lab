CodeMatrix = [[0] for i in range(3)]
EncryptedCodeMatrix = [[0] for i in range(3)]
KeyMatrix = [[0]*3 for i in range(3)]

def KeyMat(Key):
        k = 0
        for i in range(3):
            for j in range(3):
                KeyMatrix[i][j] = ord(Key[k])%65
                k += 1

def Encrypt(CodeMatrix):
        for i in range(3):
            for j in range(1):
                for k in range(3):
                    EncryptedCodeMatrix[i][j] += KeyMatrix[i][k] * CodeMatrix[k][j]
                EncryptedCodeMatrix[i][j] = EncryptedCodeMatrix[i][j] % 26

def Hill(Code, Key):
    
    KeyMat(Key)
    
    for i in range(3):
        CodeMatrix[i][0] = ord(Code[i]) % 65
        
    Encrypt(CodeMatrix)
    
    Output = []
    
    for i in range(3):
        Output.append(chr(EncryptedCodeMatrix[i][0] + 65))
    
    print("The Encrypted text is :",''.join(Output))
        
def main():
    Code = input("Enter the code to be encrypted (Capital Only) (3 words only) : ")
    Key = input("Enter the key (Capital Only) (9 words only): ")
    Hill(Code, Key)
    
if __name__ == "__main__":
    main()
    