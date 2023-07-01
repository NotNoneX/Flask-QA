# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 15:46
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app00_模板.py
""" 项目初始化模板 """
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
