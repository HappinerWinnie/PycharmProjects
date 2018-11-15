# port=7777
# list=["zhansan", "lisi", "wangwu"]
# dict = {
# 	"name":"zhangsan",
# 	"age":18
# }

#print(__file__)

import os

#绝对路径
#BASE_DIR = os.path.dirname(r'%s'%(os.path.dirname(os.path.abspath(__file__))))

#相对路径
BASE_DIR = os.path.dirname(__file__)
#E:\\ssfs\\sfsfs

options = {
	"port":9999,
	"list":["zhansan", "lisi", "wangwu"],
	"stu":{
 		"name":"zhangsan",
		"age":18
 	}
}

#设置
settings = {
	"template_path":os.path.join(BASE_DIR, "templates"),
    "static_path":os.path.join(BASE_DIR, "static"),
}