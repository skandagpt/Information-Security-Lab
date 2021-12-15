def CodePairs(Code):
    CharList = list(Code.strip())
    n = len(CharList)
    pairList = []
    i ,j = 0,0
    temp = []
    
    while j < n:
        if not temp:
            temp.append(CharList[j])
            i += 1
            j += 1
            
        elif i < 2 and temp[0] != CharList[j]:
            temp.append(CharList[j])
            i += 1
            j += 1
            
        elif i < 2 and temp[0] == CharList[j]:
            temp.append('X')
            i += 1
            
        else:
            pairList.append("".join(temp))
            temp = []
            i = 0
            
    if len(temp) < 2:
        temp.append('Z')
    pairList.append("".join(temp))
            
    return pairList
    
def KeyMatrix(Key):
    alpha = [0 for i in range(26)]
    alpha[9] += 1
    Matrix = [['#']*5 for i in range(5)]
    for char in Key:
        for i in range(5):
            for j in range(5):
                if alpha[ord(char)%65] == 0 and Matrix[i][j] == '#': 
                    Matrix[i][j] = char
                    alpha[ord(char)%65] += 1
                    continue

    for K in range(len(alpha)):
        for i in range(5):
            for j in range(5):
                if alpha[K] == 0 and Matrix[i][j] == '#':
                    Matrix[i][j] = chr(K+65) 
                    alpha[K] += 1
                    break
    return Matrix
   
def search(char, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if char == matrix[i][j]:
                return i,j 
    return 0,0    
       
def Encrypt(pairs, matrix):
    output = ''
    for pair in pairs:
        x1, y1 = search(pair[0], matrix)
        x2, y2 = search(pair[1], matrix)
        output += matrix[x1][y2] + matrix[x2][y1]
    print(output)
        

def main():
    Code = input("Enter the code to be encrypted (Capital Only) : ")
    Key = input("Enter the key (Capital Only) : ")
    print(KeyMatrix(Key))
    pairs = CodePairs(Code)
    Encrypt(pairs, KeyMatrix(Key))
    
if __name__ == "__main__":
    main()