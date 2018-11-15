import os

# 相对路径
BASE_DIR = os.path.dirname(__file__)

options = {
    "port": 9999,
}

# 设置
settings = {
    "template_path": os.path.join(BASE_DIR, "templates"),
    "static_path": os.path.join(BASE_DIR, "static"),
    "xsrf_cookies": False,
}
