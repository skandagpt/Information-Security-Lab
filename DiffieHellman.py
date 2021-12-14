import random
def primitiveKey(num):
    arr = [0 for i in range(1,num)]
    des = [1 for i in range(1, num)]
    while arr != des:
        arr = [0 for i in range(1,num)]
        alpha = random.randint(1,num-1)
        for i in range(1,num):
            k = (alpha**i)%num
            # print(alpha, k)
            arr[k-1] += 1
            if arr[k-1] > 1:
                break    
    return alpha

def DiffieHellman():
    q = int(input('Enter any Prime Number: '))
    alpha = primitiveKey(q)
    print("Enter the private key of A and B (private keys < q)")
    Xa, Xb = map(int, input().split())
    Ya = (alpha**Xa)%q
    Yb = (alpha**Xb)%q
    print('The public key of A is :', Ya)
    print('The public key of B is :', Yb)
    k1 = (Yb**Xa)%q
    k2 = (Ya**Xb)%q
    print('The secret key of A is:', k1)
    print('The secret key of B is:', k2)
    if k1 == k2:
        print('Key Exchanged successfully')
    else:
        print('Exchange Failed')

def main():
    DiffieHellman()

if __name__ == '__main__':
    main()
    
    
    