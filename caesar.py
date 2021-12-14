def Caesar(Code, Shift) :
    result = ''
    for i in range(len(Code)):
        char = Code[i]
        result += chr((ord(char) + Shift - 65) % 26 + 65) 
    print("The encrypted text is :",result)

def main():
    Code = input("Enter the code to be encrypted (Capital Only) : ")
    Shift = int(input("Enter the shift key : "))
    Caesar(Code, Shift)
    
if __name__ == '__main__':
    main()