'''
import socket
import select
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('192.168.63.1',9999))

sk.listen(1000)

input = [sk, ]

output = []
other = []

cli_struct = [

    {
    'sock':'',
    'addr':'',
    'package':[]
    }

]
while True:
    r_list, w_list, e_list = select.select(input, [], [], 1)

    # 遍历r_list
    for conn in r_list:
        # 如果是服务端就绪，代表有新的客户端连接
        if conn == sk:
            # 接收新的客户端的连接请求
            cli, addr = conn.accept()
            input.append(cli)
            print("hello new guys: ", addr)
        else:
            data = conn.recv(1024).decode('utf8')
            if data:
                print('recv: ', data)
                print(input)
            else:
                print('客户端已断开连接')
                if conn in output:
                #output.remove(cli)
                    output.remove(conn)
                input.remove(conn)
'''

import time
import socket
import select
import logging
import queue

g_select_timeout = 10


class Server(object):
    def __init__(self, host='192.168.63.1', port=9999, timeout=2, client_nums=1000):
        self.__host = host
        self.__port = port
        self.__timeout = timeout
        self.__client_nums = client_nums
        self.__buffer_size = 1024

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(False)
        self.server.settimeout(self.__timeout)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # keepalive
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口复用
        server_host = (self.__host, self.__port)
        try:
            self.server.bind(server_host)
            self.server.listen(self.__client_nums)
        except:
            raise
        self.inputs = [self.server]  # select 接收文件描述符列表
        self.outputs = []  # 输出文件描述符列表
        self.message_queues = {}  # 消息队列
        self.client_info = {}

    def run(self):
        while True:
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs, g_select_timeout)
            if not (readable or writable or exceptional):
                continue

            for conn in readable:
                if conn == self.server:  # 是客户端连接
                    connection, client_address = conn.accept()
                    # print "connection", connection
                    print ("%s connect." % str(client_address))
                    connection.setblocking(0)  # 非阻塞
                    self.inputs.append(connection)  # 客户端添加到inputs
                    self.client_info[connection] = str(client_address)
                    self.message_queues[connection] = queue.Queue()  # 每个客户端一个消息队列

                else:  # 是client, 数据发送过来
                    try:
                        data = conn.recv(self.__buffer_size)
                    except:
                        err_msg = "Client Error!"
                        logging.error(err_msg)
                    if data:
                        # print data
                        data = "%s %s say: %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), self.client_info[conn], data)
                        self.message_queues[conn].put(data)  # 队列添加消息

                        if conn in self.outputs:  # 要回复消息
                            self.outputs.append(conn)
                    else:  # 客户端断开
                        # Interpret empty result as closed connection
                        print ("Client:%s Close." % str(self.client_info[conn]))
                        if conn in self.outputs:
                            self.outputs.remove(conn)
                        self.inputs.remove(conn)
                        conn.close()
                        del self.message_queues[conn]
                        del self.client_info[conn]


if "__main__" == __name__:
    s = Server()
    s.run()
