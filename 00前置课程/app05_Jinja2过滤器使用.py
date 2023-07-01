# -*- coding: UTF-8 -*-
# @Time: 2023/6/14 15:00
# @Author: Rock Candy
# @E-mail: NotNoneX@Gmail.com
# @File: app05_Jinja2过滤器使用.py
"""" Jinja2 过滤器使用
在模板文件内使用管道符| 如下表示获取用户名的长度 而length是一个过滤器
{{ user.username | length }}
"""
from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)


# 自定义过滤器 时间时期格式化
def custom_filter(date, date_format="%Y年%m月%d日 %H:%M"):
    return date.strftime(date_format)


# 导入过滤器 并且命名 然后便可以在HTML模板文件内使用
app.add_template_filter(custom_filter, "date_form")


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route('/')
def hello_world():
    user = User(username='NotNoneX', email='NotNoneX@Gmail.com')
    person = {
        "username": "冰糖",
        "email": "NotNoneX@qq.com"
    }
    return render_template("index.html", user=user, person=person)


@app.route("/filter")
def filter1():
    user = User(username='NotNoneX', email='NotNoneX@Gmail.com')
    current_time = datetime.now()
    return render_template("filter.html", user=user, cur_time=current_time)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
