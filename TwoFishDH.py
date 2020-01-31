
def menu(options_list):
    print('Two Fish-DH\n=========')
    print("1. Select Option 1 to Encrypt")
    print("2. Select Option 2 to Decrypt")
    print('[0] Exit')


def encrypt():
    ipaddress = (input('Enter the ip address you want to encrypt'))
    iplist = ipaddress.split('.')
    ip1 = iplist[0]
    ip2 = iplist[1]
    ip3 = iplist[2]
    ip4 = iplist[3]
    #Convert to binary
    ippart1 = int(ip1);
    n=int(input('please enter the no. in decimal format: '))
    x=n
    k=[]
    while (n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2   
    k.append(0)
    string=""
    for j in k[::-1]:
        string=string+str(j)
    print('The binary no. for %d is %s'%(x, string))
    #Xor stuff later
    #
    #a = "11011111101100110110011001011101000"
    #b = "11001011101100111000011100001100001"
    #y = int(a,2) ^ int(b,2)
    #print '{0:b}'.format(y)
    #Some xor stuff as reference





while True:
    menu(options_list)
    option = int(input("Enter your option: "))
    if (option == 0):
        break;
    elif option == 1:
        encrypt()
    else:
        decrypt()
        
