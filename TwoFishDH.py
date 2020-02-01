#import ipaddress
import random
#KprA = A = a^al mod p			KprB = B = a^b mod p
#KpubA = B^al = (a^b)^al mod p		KpubB = A^b = (a^al)^b mod p
#KAB = B^al = (a^b)^al mod p		KAB = A^b = (a^al)^b mod p


xorkey0 = random.randint(0,255)
xorkey1 = random.randint(0,255)
xorkey2 = random.randint(0,255)
xorkey3 = random.randint(0,255)

def PHTe():
    a = random.randint(0,255)
    b = random.randint(0,255)
    ainv = ((a+b) mod 2**32)
    binv = ((a+2b) mod 2**32)


dh()
def dh(c):
    if c == 'encrypt':
        mod = 23
        base = 9
        a = random.randint(1,9999)
        b = random.randint(1,9999)

        s1 = (base**a) % mod

        s2 = (base**b) % mod

        John = (s1**b) % mod
    
        Doe = (s2**a) % mod

    else:



     
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

ipaddress = (input('Enter the ip address you want to encrypt: '))
iplist = ipaddress.split('.')
ip1 = int(iplist[0])
ip2 = int(iplist[1])
ip3 = int(iplist[2])
ip4 = int(iplist[3])
n= int(input('Please enter the private key (number): '))

x0 = ip1 
y0 = xorkey0
print(xorkey0)
print(myXOR(x0,y0))

x1 = ip2
y1 = xorkey1
print(xorkey1)
print(myXOR(x1,y1))

x2 = ip3
y2 = xorkey2
print(xorkey2)
print(myXOR(x2,y2))

x3 = ip4
y3 = xorkey3
print(xorkey3)
print(myXOR(x3,y3))



#def menu(options_list):
#    print('Two Fish-DH\n=========')
#    print("1. Select Option 1 to Encrypt")
#    print("2. Select Option 2 to Decrypt")
#    print('[0] Exit')


#def encrypt():
#    ipaddress = (input('Enter the ip address you want to encrypt'))
#    iplist = ipaddress.split('.')
#    ip1 = iplist[0]
#    ip2 = iplist[1]
#    ip3 = iplist[2]
#    ip4 = iplist[3]
#    n= int(input('Please enter the private key (number): '))

#while True:
#    menu(options_list)
#    option = int(input("Enter your option: "))
#    if (option == 0):
#        break;
#    elif option == 1:
#        encrypt()
#    else:
#        decrypt()
        


































