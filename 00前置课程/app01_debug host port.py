# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 10:53
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app01_debug host port.py
""" debug host 和 port """
from flask import Flask

# __name__: 表示当前app.py文件
# 1, 以后出现bug, 他可以帮助我们快速定位
# 2, 对于寻找模板文件, 有一个相对路径
app = Flask(__name__)


# 创建一个路由和视图函数的映射
@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    # 1, debug模式
    #   1.1 开启后, 只要修改后保存 就会自动加载变化 无需重启服务
    #   1.2 开启后, 浏览器可以看到出错信息
    # 2, 修改host
    #   主要的作用就是为了让其他设备可以访问我们的Flask项目
    # 3, 修改端口号
    #   防止默认的5000端口被其他占用
    app.run(debug=True, host='0.0.0.0', port=5000)
