#Done by Gladys Chua Ling Hui, Tan Yuan Ming and Chua Zhe Yu 
import random
#def functions PHT encrypt and decrypt
def PHTe(a,b,dh):
    
    divided1 = ( a+b)//2**dh
    divided2 = (a+ 2 *b)//2**dh
    ainv = ( a+b) % 2**dh #remainder
    binv =(a+ 2 *b)% 2**dh #remainder
    
    return divided1,divided2,ainv,binv
    
def PHTd(divided1,divided2,ainv,binv,oa,ob):
    ab = (((2**dh) * divided1) + ainv)   #reverse to get original a+b
    abb = ((2**dh)*divided2) + binv #reverse to get original a+2b
    a = ab - ob
    b = abb - ob - oa
    return a,b

#def function for dh to implement into pht
def dh():
    mod = 7
    base = 9
    a = random.randint(0,255)
    b = random.randint(0,255)
    s1 = (base**a) % mod
    dh = (s1**b) % mod
    return dh

#def function for displaymenu
def menu():
    print('Two Fish-DH\n=========')
    print("1. Select Option 1 to Encrypt")
    print("2. Select Option 2 to Decrypt")
    print('[0] Exit\n')

#def functoin for xor
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
   
    return int(xor,2)

#main 
dh = dh()
xorkey0 = random.randint(0,255)
xk0 = xorkey0
xorkey1 = random.randint(0,255)
xk1 = xorkey1
xorkey2 = random.randint(0,255)
xk2 = xorkey2
xorkey3 = random.randint(0,255)
xk3 = xorkey3

#while loop for menu
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
        fxor1 = myXOR(ip1,xk0)
        fxor2 = myXOR(ip2,xk1)
        fxor3 = myXOR(ip3,xk2)
        fxor4 = myXOR(ip4,xk3)


        #PHT using DH as modulus and IP Address into per 2 bytes
        #ainv , binv = PHTe(fxor1,fxor2,dh)
        #cinv , dinv = PHTe(fxor3,fxor4,dh)
        divided1,divided2,ainv , binv = PHTe(fxor1,fxor2,dh)
        divided3,divided4,cinv , dinv = PHTe(fxor3,fxor4,dh)
  
        #XOR again with the same key
        Sxor1 = myXOR(ainv,xk0)
        Sxor2 = myXOR(binv,xk1)
        Sxor3 = myXOR(cinv,xk2)
        Sxor4 = myXOR(dinv,xk3)
        Encrypt = str(Sxor1) + '.' + str(Sxor2) + '.' + str(Sxor3) + '.' + str(Sxor4)
        print("The Encrypted Ip Address is: ",Encrypt,"\n")
       
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
     
        #reverse pht
        ra , rb = PHTd(divided1,divided2,Rxor1,Rxor2,fxor1,fxor2)
        rc , rd = PHTd(divided3,divided4,Rxor3,Rxor4,fxor3,fxor4)
        #reverse xor
        opa1 = myXOR(ra,xk0)
        opa2 = myXOR(rb,xk1)
        opa3 = myXOR(rc,xk2)
        opa4 = myXOR(rd,xk3)
        decrypt = str(opa1) + "." + str(opa2) +'.' + str(opa3) + '.' +  str(opa4)
        print("The decrypted Ip Address is: ",decrypt,"\n")
    else:
        print("Invalid Option")
        continue

































