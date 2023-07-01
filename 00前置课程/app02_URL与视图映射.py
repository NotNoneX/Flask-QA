# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 11:32
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app02_URL与视图映射.py
""" URL与视图映射 """

from flask import Flask
# 用于获取输入的参数
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


# 带参数的URL 用尖括号<>定义
# 定义类型需要在前面加上 类型和冒号: 如果类型不匹配会报404
@app.route('/blog/<int:article_id>')
def blog(article_id):
    return "你访问的文章id为: %s" % article_id


# /book/list: 默认返回第一页数据
# /book/list?page=2: 返回第二页数据
@app.route('/book/list')
def book():
    # key: 获取键的值  default: 不指定键时的默认值 type: 数据类型
    page = request.args.get(key='page', default=1, type=int)
    return f"您获取的是第{page}页的图书列表"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
