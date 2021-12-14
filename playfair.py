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
            
    if temp:
        temp.append('Z')
        pairList.append("".join(temp))
            
    print(pairList)
    
def KeyMatrix(Code, Key):
    Matrix = [['A']*5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            Matrix[i][j] = char for char in SetCharList    

def main():
    Code = input("Enter the code to be encrypted (Capital Only) : ")
    Key = input("Enter the key (Capital Only) : ")
    CodePairs(Code)
    
if __name__ == "__main__":
    main()