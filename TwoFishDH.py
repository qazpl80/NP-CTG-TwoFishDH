import random
#KprA = A = a^al mod p			KprB = B = a^b mod p
#KpubA = B^al = (a^b)^al mod p		KpubB = A^b = (a^al)^b mod p
#KAB = B^al = (a^b)^al mod p		KAB = A^b = (a^al)^b mod p

def PHTe(dh,a,b):
    ainv = ((a+b) % (2**dh))
    binv = ((a+(2*b)) % (2**dh))
    return ainv,binv  

def PHTd(dh,ainv,binv):
    a = (((2*ainv) - binv) % (2**dh))
    b = ((binv - ainv) % (2 **dh))
    return a,b

def dh():
    mod = 7
    base = 9
    a = random.randint(0,255)
    b = random.randint(0,255)
    s1 = (base**a) % mod
    s2 = (base**b) % mod
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

def myXAND(x, y): 
    reslt = 0 # Initialize result 
  
    # Assuming 32-bit Integer 
    for i in range(31, -1, -1): 
          
        # Find current bits in x and y 
        b1 = x & (1 << i) 
        b2 = y & (1 << i) 
        b1 = min(b1, 1) 
        b2 = min(b2, 1) 
  
        # If both are 1 then 0  
        # else xor is same as OR 
        xANDBit = 0
        if (b1 & b2):
            xANDBit = 0
        else: 
            xANDBit = (b1 | b2)
  
        # Update result 
        reslt <<= 1; 
        reslt |= xANDBit 
    return reslt

def myXOR(x, y): 
    res = 0 # Initialize result 
  
    # Assuming 32-bit Integer 
    for i in range(31, -1, -1): 
          
        # Find current bits in x and y 
        b1 = x & (1 << i) 
        b2 = y & (1 << i) 
        b1 = min(b1, 1) 
        b2 = min(b2, 1) 
  
        # If both are 1 then 0  
        # else xor is same as OR 
        xoredBit = 0
        if (b1 & b2): 
            xoredBit = 0
        else: 
            xoredBit = (b1 | b2) 
  
        # Update result 
        res <<= 1; 
        res |= xoredBit 
    return res


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
        xorkey0 = random.randint(0,255)
        xorkey1 = random.randint(0,255)
        xorkey2 = random.randint(0,255)
        xorkey3 = random.randint(0,255)

        #Split IP Address into 4 parts
        ipaddress = input('Enter the ip address you want to encrypt: ')
        iplist = ipaddress.split('.')
        ip1 = int(iplist[0])
        ip2 = int(iplist[1])
        ip3 = int(iplist[2])
        ip4 = int(iplist[3])

        #XOR of xorkey and IP Address
        x0 = ip1 
        y0 = xorkey0
        fxor1 = myXOR(x0,y0)

        x1 = ip2
        y1 = xorkey1
        fxor2 = myXOR(x1,y1)

        x2 = ip3
        y2 = xorkey2
        fxor3 = myXOR(x2,y2)

        x3 = ip4
        y3 = xorkey3
        fxor4 = myXOR(x3,y3)
        print(fxor1 ,fxor2, fxor3, fxor4)

        dh = dh()
        print(dh)
        #PHT using DH as modulus and IP Address into per 2 bytes
        ainv , binv = PHTe(dh,fxor1,fxor2)
        ipa1 = ainv
        ipa2 = binv
        cinv , dinv = PHTe(dh,fxor3,fxor4)
        ipa3 = cinv
        ipa4 = dinv

        Sxor1 = myXOR(ipa1,xorkey0)
        Sxor2 = myXOR(ipa2,xorkey1)
        Sxor3 = myXOR(ipa3,xorkey2)
        Sxor4 = myXOR(ipa4,xorkey3)
        print(fxor1)
        print(Sxor1)
        Encrypt = str(Sxor1) + '.' + str(Sxor2) + '.' + str(Sxor3) + '.' + str(Sxor4)
        print(Encrypt)
       
    elif option == 2:
        ipaddr = input('Enter the ip address you want to decrypt (must be immediate, do not close interface): ')
        diplist = ipaddress.split('.')
        dip1 = int(diplist[0])
        dip2 = int(diplist[1])
        dip3 = int(diplist[2])
        dip4 = int(diplist[3])
        #reverse xor 
        Rxor1 = myXAND(dip1,xorkey0)
        Rxor2 = myXAND(dip2,xorkey1)
        Rxor3 = myXAND(dip3,xorkey2)
        Rxor4 = myXAND(dip4,xorkey3)
        print(Rxor1)
        #reverse pht
        ra , rb = PHTd(dh,Rxor1,Rxor2)
        dipa1 = ra
        dipa2 = rb
        rc , rd = PHTd(dh, Rxor3,Rxor4)
        dipa3 = rc
        dipa4 = rd

        #reverse xor
        opa1 = myXAND(dipa1,xorkey0)
        opa2 = myXAND(dipa2,xorkey1)
        opa3 = myXAND(dipa3,xorkey2)
        opa4 = myXAND(dipa3,xorkey3)
        decrypt = str(opa1) + "." + str(opa2) +'.' + str(opa3) + '.' +  str(opa4)
        print(opa1)
        print(decrypt)
    else:
        print("Invalid Option")
        continue

































