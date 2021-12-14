import numpy as np

def RowTrans(Code, key):
    numRows = len(key)
    numCols = len(Code)//numRows + 1
    encryptArr = np.array([['0'] * numRows] * numCols)
    keymap = {}
    for i in range(len(key)):
         keymap[key[i]] = i+1
    mapf = sorted(keymap)
    for i in range(numCols):
        for j in range(numRows):
            index = numRows*i + j
            if index < len(Code) and Code[index] != ' ':
                encryptArr[i][j] = Code[index]
            else:
                encryptArr[i][j] = 'Z'
    print(encryptArr)
    output = ''
    for i in range(len(keymap)):
        j = keymap[mapf[i]] - 1
        for k in range(numCols):
            output += encryptArr[k][j]
    print("The Encrypted text is :",output)
    
def main():
    Code = input("Enter the code to be encrypted (Capital Only): ")
    Key = input("Enter the key (Capital Only): ")
    RowTrans(Code, Key)
    
if __name__ == "__main__":
    main()