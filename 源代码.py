#简单的端口扫描器，用于检查目标主机的TCP端口是否开放

import socket   #导入Python的socket库，用于网络通信。
import time     #导入time库，用于在扫描每个端口之间添加延迟。


def port_scan(host, port):        #定义一个名为port_scan的函数，它接受两个参数：host（目标主机的IP地址）和port（要检查的端口号）
    try:  #开始一个try块，用于捕获在尝试连接端口时可能发生的异常
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建一个新的socket对象，用于IPv4网络通信和TCP协议
        sock.settimeout(1)   #设置socket的超时时间为1秒，这意味着如果连接尝试在1秒内没有响应，将引发一个socket.timeout异常
        result = sock.connect_ex((host, port))  #尝试连接到目标主机的指定端口，并返回一个错误码。connect_ex方法在连接成功时返回0，否则返回错误码
        if result == 0:   #如果result为0，表示连接成功，端口是开放的
            print(f"Port {port} is open")    #打印出开放的端口号
        sock.close()   #关闭socket连接
    except socket.timeout:  #如果发生socket.timeout异常，表示连接尝试超时
        print(f"Port {port} connection timed out")   #打印出超时的端口号
    except socket.gaierror:   #如果发生socket.gaierror异常，表示地址相关的错误
        print(f"Port {port} address-related error")   #打印出地址相关的错误信息
    except socket.error as e:   #如果发生其他socket错误，捕获异常并打印错误信息
        print(f"Other socket error for port {port}: {e}")   #打印出其他socket错误和对应的错误信息


host = input("请输入目标主机IP: ")   #从用户那里获取目标主机的IP地址
for port in range(1, 1025):   #循环从1到1024（包含1，不包含1025），因为这些是常见的TCP端口号
    port_scan(host, port)   #对每个端口调用port_scan函数进行检查
    time.sleep(0.5)   #在扫描每个端口后暂停0.5秒，以减少对目标主机的负载


import socket
import time


def port_scan(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.timeout:
        print(f"Port {port} connection timed out")
    except socket.gaierror:
        print(f"Port {paort} address-related error")
    except socket.error as e:
        print(f"Other socket error for port {port}: {e}")


host = input("请输入目标主机IP: ")
for port in range(1, 1025):
    port_scan(host, port)
    time.sleep(0.5)