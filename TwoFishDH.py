#Done by Gladys Chua Ling Hui, Tan Yuan Ming and Chua Zhe Yu 
import random
#KprA = A = a^al mod p			KprB = B = a^b mod p
#KpubA = B^al = (a^b)^al mod p		KpubB = A^b = (a^al)^b mod p
#KAB = B^al = (a^b)^al mod p		KAB = A^b = (a^al)^b mod p

def PHTe(a,b,dh):
    ainv = ((a+b) % (2**dh))
    binv = ((a+(2*b)) % (2**dh))
    return ainv,binv  

def PHTd(ainv,binv,dh):
    a = (((2*ainv) - binv) % (2**dh))
    b = ((binv - ainv) % (2 **dh))
    return a,b

def dh():
    mod = 7
    base = 9
    a = random.randint(0,255)
    b = random.randint(0,255)
    s1 = (base**a) % mod
    dh = (s1**b) % mod
    return dh

def menu():
    print('Two Fish-DH\n=========')
    print("1. Select Option 1 to Encrypt")
    print("2. Select Option 2 to Decrypt")
    print('[0] Exit')

#x = 10 (0000 1010), y = 4 (0000 0100),
#Operator	Meaning	        Example
#&	Bitwise AND	        x& y = 0 (0000 0000)
#|	Bitwise OR	        x | y = 14 (0000 1110)
#~	Bitwise NOT	        ~x = -11 (1111 0101)
#^	Bitwise XOR 	    x ^ y = 14 (0000 1110)
#>>	Bitwise right shift	x>> 2 = 2 (0000 0010)
#<<	Bitwise left shift	x<< 2 = 40 (0010 1000)

def myXOR(x, y): 
    xb = bin(x)
    yb = bin(y)

    xxb = bin(x)[2:].zfill(8)
    yyb = bin(y)[2:].zfill(8)

    xor = ''
    for i in range(len(xxb)):
        if xxb[i] != yyb[i]:
            xor += '1'
        else:
            xor += '0'
    print(int(xor,2))
    return int(xor,2)

dh = dh()
xorkey0 = random.randint(0,255)
xk0 = xorkey0
xorkey1 = random.randint(0,255)
xk1 = xorkey1
xorkey2 = random.randint(0,255)
xk2 = xorkey2
xorkey3 = random.randint(0,255)
xk3 = xorkey3

while True:
    menu()
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print('Invalid Input, please try again')
        continue
    if option == 0:
        break;
    elif option == 1:

        #Split IP Address into 4 parts
        ipaddress = input('Enter the ip address you want to encrypt: ')
        iplist = ipaddress.split('.')
        ip1 = int(iplist[0])
        ip2 = int(iplist[1])
        ip3 = int(iplist[2])
        ip4 = int(iplist[3])

        ##XOR of xorkey and IP Address
        #fxor1 = myXOR(ip1,xk0)
        #fxor2 = myXOR(ip2,xk1)
        #fxor3 = myXOR(ip3,xk2)
        #fxor4 = myXOR(ip4,xk3)
        #print(fxor1 ,fxor2, fxor3, fxor4)

        #PHT using DH as modulus and IP Address into per 2 bytes
        #ainv , binv = PHTe(fxor1,fxor2,dh)
        #cinv , dinv = PHTe(fxor3,fxor4,dh)
        ainv , binv = PHTe(ip1,ip2,dh)
        cinv , dinv = PHTe(ip1,ip2,dh)
        
        #XOR again with the same key
        Sxor1 = myXOR(ainv,xk0)
        Sxor2 = myXOR(binv,xk1)
        Sxor3 = myXOR(cinv,xk2)
        Sxor4 = myXOR(dinv,xk3)
        Encrypt = str(Sxor1) + '.' + str(Sxor2) + '.' + str(Sxor3) + '.' + str(Sxor4)
        print(Encrypt)
       
    elif option == 2:
        ipaddr = input('Enter the ip address you want to decrypt (must be immediate, do not close interface): ')
        diplist = ipaddr.split('.')
        dip1 = int(diplist[0])
        dip2 = int(diplist[1])
        dip3 = int(diplist[2])
        dip4 = int(diplist[3])
        #reverse xor 
        Rxor1 = myXOR(dip1,xk0)
        Rxor2 = myXOR(dip2,xk1)
        Rxor3 = myXOR(dip3,xk2)
        Rxor4 = myXOR(dip4,xk3)
        print(Rxor1 ,Rxor2, Rxor3, Rxor4)
        #reverse pht
        ra , rb = PHTd(Rxor1,Rxor2,dh)
        rc , rd = PHTd(Rxor3,Rxor4,dh)
        #reverse xor
        #opa1 = myXOR(ra,xk0)
        #opa2 = myXOR(rb,xk1)
        #opa3 = myXOR(rc,xk2)
        #opa4 = myXOR(rd,xk3)
        decrypt = str(ra) + "." + str(rb) +'.' + str(rc) + '.' +  str(rd)
        print(decrypt)
    else:
        print("Invalid Option")
        continue

































