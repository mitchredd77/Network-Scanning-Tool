from port_scanner import menu, ports_scan, check_IP_input, check_port_num
import socket


if __name__ == '__main__':
    choices = menu()
    ports_scan(choices[0], choices[1], choices[2])