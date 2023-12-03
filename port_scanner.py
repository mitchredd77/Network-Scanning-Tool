import socket
import time
import ipaddress

def ports_scan(target_ip, min_port, max_port):
    starttime = time.time()
    print("Beginning Scan")
    for port in range(min_port, max_port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = scanner.connect_ex((target_ip, port))
        print(f"{port} Scanned")
    if(conn == 0):
        print ('Port %d: OPEN' %(port))
    scanner.close()

    endtime = time.time()
    totaltime = endtime - starttime
    print('Total Time: %s' %(totaltime))

def check_IP_input(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        return ip_address
    except ValueError:
        print('''That is an invalid ip address, it should be:
              ******ex: 192.168.89.200)*******************
                    PLEASE TRY AGAIN''')
        raise ValueError

def check_port_num(port):
    if (port >= 1) and (port <= 65535):
        return port
    else:
        raise ValueError('''
              ************************************
              That is not a port number in between
                  1 and 65535, please try again
              ************************************
              ''')
        
def menu():
    while True:
        try:
            input('''
                     This is a penetration testing tool and needs to be handled car. 
                     Please select ENTER IF you agree to use the tool responsibly. 
                     You're on your own!''')
            target_ip = input('''
                                *********************************************
                                  Please specify the host IP that you want to scan: 
                                ***********************************Here:  ''')
            target_ip = check_IP_input(target_ip)
    
            min_port = int(input('''
                                    ****************************************
                                    Please enter min port number you would 
                                    like to scan, such as min port = 1, 
                                    max port = 65535(bottom of range 1 - 65535) 
                                    *******************************Here:  '''))
            min_port = check_port_num(min_port)
            max_port = int(input('''
                                    ****************************************
                                    Please enter max port number you would 
                                    like to scan, such as min port = 1, 
                                    max port = 65535(top of range 65535)  
                                    *******************************Here:  '''))
            max_port = check_port_num(max_port)
            return target_ip, min_port, max_port
        except ValueError:
            input('''               
                                    Submitted an incorrect value, please try again
                                    PRESS ENTER TO CONTINUE
                                    ''')
        
        
    

