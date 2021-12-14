import random

def gcd(a,b):
    while b:
        a,b = b , a%b
    return a

def alphatonum(Code):
    n = len(Code)
    res = 0
    for i in range(n):
        curr = ord(Code[i])%65
        res = res*10 + curr
    return res

def numtoalph(msg):
    res = ''
    while msg:
        imp = msg%10
        msg = msg//10
        strmsg = chr(imp + 65)
        res = strmsg + res
    return res
        

def rsa():
    p = int(input("Enter a prime number: "))
    q = int(input("Enter second prime number: "))
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while e < phi:
        if gcd(e,phi) == 1:
            break
        else:
            e += 1
    k = random.randint(1,50)
    d = 0
    fo = True
    while fo :
        temp = (e*d)%phi
        if temp != 1:
            d += 1
        else:
            fo = False
    code = input('Enter message to be encrypted (CAPITAL only): ')
    msg = alphatonum(code)
    # print(msg)
    Encrypt = pow(msg, e, n)
    # print(Encrypt)
    Emsg = numtoalph(Encrypt)
    print('Encrypted message is: ', Emsg)
    dmsg = pow(Encrypt, d, n)
    DM = numtoalph(dmsg)
    print('The decrypted code is:', DM)
def main():
    rsa()
    
if __name__ == '__main__':
    main()
    
    