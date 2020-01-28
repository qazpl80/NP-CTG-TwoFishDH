options_list = ['Encrypt','Decrypt']
def menu(options_list):
    print('Two Fish-DH\n=========')
    for i in range(1,len(options_list)+1):
        print("[{}]".format(i),options_list[i-1])
    print()
    print('[0] Exit')


def encrypt():
    ipaddress = (input('Enter the ip address you want to encrypt'))
    iplist = ipadress.split('.')
    ip1 = iplist[0]
    ip2 = iplist[1]
    ip3 = iplist[2]
    ip4 = iplist[3]
    #Xor stuff later








while True:
    menu(options_list)
    option = int(input("Enter your option: "))
    if (option == 0):
        break;
    elif option == 1:
        encrypt()
    else:
        decrypt()
        
