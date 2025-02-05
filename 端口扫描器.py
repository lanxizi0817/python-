# 导入socket库:
import socket
#服务器

# 创建一个socket:          AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    # 监听端口:
    s.bind(('127.0.0.1', 9999))
    #开始监听
    s.listen()     #s用于监听   c用于与连接的客户端通信
    c,addr = s.accept()     #accept()会等待并返回一个客户端的连接
    with c:
        print(addr,"connected.")

        while True:
            data = c.recv(1024)
            if not data:
                break
            c.sendall(data)


#客户端

# import socket
# with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
#     s.connect(( , ))
#     s.send()
#     s.recv()
#     s.close()