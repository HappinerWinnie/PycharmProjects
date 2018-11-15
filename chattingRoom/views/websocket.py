import tornado.websocket

st_words = ["sb", "nmd", "cao", "我操", "fuck", "艹", "尼玛", "zz"]

#WebSocketHandler 继承自 RequestHandler
class websocketHandler(tornado.websocket.WebSocketHandler):
    users = []
    ips = []

    # 如果有客户端连接 自动执行
    def open(self, *args, **kwargs):
        # 记录连接的客户端的信息 一个IP就代表一个客户端
        client = self.request.rempote_ip
        msg = ''
        if client not in self.ips:
            msg = "[%s]：上线了"%(client)
            print(msg)
            self.users.append(self)
            self.ips.append(client)

        # 服务端要向所有的客户端发送新的用户上线的消息
        for user in self.users:
            user.write_message(msg)

    # 有客户端退出的时候会自动执行该函数
    def on_close(self):
        # 通知其他的用户有人下线了
        self.users.remove(self)
        msg = '[%s]下线了！'%(self.request.rempote_ip)
        for user in self.users:
            user.write_message(msg)


    def close(self, code=None, reason=None):

        pass

    def on_message(self, message):
        print(message)
        msg = '[%s]说：%s' %(self.request.rempote_ip, message)
        for user in self.users:
            user.write_message(msg)

    def check_origin(self, origin):

        return True